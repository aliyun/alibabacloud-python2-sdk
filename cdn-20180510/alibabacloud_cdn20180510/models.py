# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddCdnDomainRequest(TeaModel):
    def __init__(self, cdn_type=None, check_url=None, domain_name=None, owner_account=None, owner_id=None,
                 resource_group_id=None, scope=None, security_token=None, sources=None, top_level_domain=None):
        self.cdn_type = cdn_type  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddCdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFCTriggerRequest(TeaModel):
    def __init__(self, event_meta_name=None, event_meta_version=None, function_arn=None, notes=None, owner_id=None,
                 role_arn=None, source_arn=None, trigger_arn=None):
        self.event_meta_name = event_meta_name  # type: str
        self.event_meta_version = event_meta_version  # type: str
        self.function_arn = function_arn  # type: str
        self.notes = notes  # type: str
        self.owner_id = owner_id  # type: long
        self.role_arn = role_arn  # type: str
        self.source_arn = source_arn  # type: str
        self.trigger_arn = trigger_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFCTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_meta_name is not None:
            result['EventMetaName'] = self.event_meta_name
        if self.event_meta_version is not None:
            result['EventMetaVersion'] = self.event_meta_version
        if self.function_arn is not None:
            result['FunctionARN'] = self.function_arn
        if self.notes is not None:
            result['Notes'] = self.notes
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        if self.source_arn is not None:
            result['SourceARN'] = self.source_arn
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventMetaName') is not None:
            self.event_meta_name = m.get('EventMetaName')
        if m.get('EventMetaVersion') is not None:
            self.event_meta_version = m.get('EventMetaVersion')
        if m.get('FunctionARN') is not None:
            self.function_arn = m.get('FunctionARN')
        if m.get('Notes') is not None:
            self.notes = m.get('Notes')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        if m.get('SourceARN') is not None:
            self.source_arn = m.get('SourceARN')
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        return self


class AddFCTriggerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFCTriggerResponseBody, self).to_map()
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


class AddFCTriggerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddFCTriggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddFCTriggerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddFCTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddCdnDomainRequest(TeaModel):
    def __init__(self, cdn_type=None, check_url=None, domain_name=None, owner_account=None, owner_id=None,
                 resource_group_id=None, scope=None, security_token=None, sources=None, top_level_domain=None):
        self.cdn_type = cdn_type  # type: str
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
        _map = super(BatchAddCdnDomainRequest, self).to_map()
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


class BatchAddCdnDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchAddCdnDomainResponseBody, self).to_map()
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


class BatchAddCdnDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchAddCdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchAddCdnDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchAddCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteCdnDomainConfigRequest(TeaModel):
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
        _map = super(BatchDeleteCdnDomainConfigRequest, self).to_map()
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


class BatchDeleteCdnDomainConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchDeleteCdnDomainConfigResponseBody, self).to_map()
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


class BatchDeleteCdnDomainConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchDeleteCdnDomainConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchDeleteCdnDomainConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchDeleteCdnDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSetCdnDomainConfigRequest(TeaModel):
    def __init__(self, domain_names=None, functions=None, owner_account=None, owner_id=None, security_token=None):
        self.domain_names = domain_names  # type: str
        self.functions = functions  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSetCdnDomainConfigRequest, self).to_map()
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


class BatchSetCdnDomainConfigResponseBodyDomainConfigListDomainConfigModel(TeaModel):
    def __init__(self, config_id=None, domain_name=None, function_name=None):
        self.config_id = config_id  # type: long
        self.domain_name = domain_name  # type: str
        self.function_name = function_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSetCdnDomainConfigResponseBodyDomainConfigListDomainConfigModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        return self


class BatchSetCdnDomainConfigResponseBodyDomainConfigList(TeaModel):
    def __init__(self, domain_config_model=None):
        self.domain_config_model = domain_config_model  # type: list[BatchSetCdnDomainConfigResponseBodyDomainConfigListDomainConfigModel]

    def validate(self):
        if self.domain_config_model:
            for k in self.domain_config_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchSetCdnDomainConfigResponseBodyDomainConfigList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainConfigModel'] = []
        if self.domain_config_model is not None:
            for k in self.domain_config_model:
                result['DomainConfigModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_config_model = []
        if m.get('DomainConfigModel') is not None:
            for k in m.get('DomainConfigModel'):
                temp_model = BatchSetCdnDomainConfigResponseBodyDomainConfigListDomainConfigModel()
                self.domain_config_model.append(temp_model.from_map(k))
        return self


class BatchSetCdnDomainConfigResponseBody(TeaModel):
    def __init__(self, domain_config_list=None, request_id=None):
        self.domain_config_list = domain_config_list  # type: BatchSetCdnDomainConfigResponseBodyDomainConfigList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_config_list:
            self.domain_config_list.validate()

    def to_map(self):
        _map = super(BatchSetCdnDomainConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_config_list is not None:
            result['DomainConfigList'] = self.domain_config_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainConfigList') is not None:
            temp_model = BatchSetCdnDomainConfigResponseBodyDomainConfigList()
            self.domain_config_list = temp_model.from_map(m['DomainConfigList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchSetCdnDomainConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchSetCdnDomainConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchSetCdnDomainConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchSetCdnDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSetCdnDomainServerCertificateRequest(TeaModel):
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
        _map = super(BatchSetCdnDomainServerCertificateRequest, self).to_map()
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


class BatchSetCdnDomainServerCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSetCdnDomainServerCertificateResponseBody, self).to_map()
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


class BatchSetCdnDomainServerCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchSetCdnDomainServerCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchSetCdnDomainServerCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchSetCdnDomainServerCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStartCdnDomainRequest(TeaModel):
    def __init__(self, domain_names=None, owner_id=None, security_token=None):
        self.domain_names = domain_names  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStartCdnDomainRequest, self).to_map()
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


class BatchStartCdnDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStartCdnDomainResponseBody, self).to_map()
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


class BatchStartCdnDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchStartCdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchStartCdnDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchStartCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStopCdnDomainRequest(TeaModel):
    def __init__(self, domain_names=None, owner_id=None, security_token=None):
        self.domain_names = domain_names  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopCdnDomainRequest, self).to_map()
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


class BatchStopCdnDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopCdnDomainResponseBody, self).to_map()
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


class BatchStopCdnDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchStopCdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchStopCdnDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchStopCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateCdnDomainRequest(TeaModel):
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
        _map = super(BatchUpdateCdnDomainRequest, self).to_map()
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


class BatchUpdateCdnDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchUpdateCdnDomainResponseBody, self).to_map()
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


class BatchUpdateCdnDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchUpdateCdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchUpdateCdnDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchUpdateCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCdnCertificateSigningRequestRequest(TeaModel):
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
        _map = super(CreateCdnCertificateSigningRequestRequest, self).to_map()
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


class CreateCdnCertificateSigningRequestResponseBody(TeaModel):
    def __init__(self, common_name=None, csr=None, pub_md_5=None, request_id=None):
        self.common_name = common_name  # type: str
        self.csr = csr  # type: str
        self.pub_md_5 = pub_md_5  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCdnCertificateSigningRequestResponseBody, self).to_map()
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


class CreateCdnCertificateSigningRequestResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateCdnCertificateSigningRequestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCdnCertificateSigningRequestResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateCdnCertificateSigningRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCdnComputeDomainRequest(TeaModel):
    def __init__(self, coverage=None, domain_name=None, owner_id=None):
        self.coverage = coverage  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCdnComputeDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coverage is not None:
            result['Coverage'] = self.coverage
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class CreateCdnComputeDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCdnComputeDomainResponseBody, self).to_map()
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


class CreateCdnComputeDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateCdnComputeDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCdnComputeDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateCdnComputeDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCdnDeliverTaskRequest(TeaModel):
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
        _map = super(CreateCdnDeliverTaskRequest, self).to_map()
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


class CreateCdnDeliverTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCdnDeliverTaskResponseBody, self).to_map()
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


class CreateCdnDeliverTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateCdnDeliverTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCdnDeliverTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateCdnDeliverTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCdnSubTaskRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, report_ids=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.report_ids = report_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCdnSubTaskRequest, self).to_map()
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


class CreateCdnSubTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCdnSubTaskResponseBody, self).to_map()
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


class CreateCdnSubTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateCdnSubTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCdnSubTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateCdnSubTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIllegalUrlExportTaskRequest(TeaModel):
    def __init__(self, owner_id=None, task_name=None, time_point=None):
        self.owner_id = owner_id  # type: long
        self.task_name = task_name  # type: str
        self.time_point = time_point  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIllegalUrlExportTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.time_point is not None:
            result['TimePoint'] = self.time_point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')
        return self


class CreateIllegalUrlExportTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIllegalUrlExportTaskResponseBody, self).to_map()
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


class CreateIllegalUrlExportTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateIllegalUrlExportTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIllegalUrlExportTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateIllegalUrlExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRealTimeLogDeliveryRequest(TeaModel):
    def __init__(self, domain=None, logstore=None, owner_id=None, project=None, region=None):
        self.domain = domain  # type: str
        self.logstore = logstore  # type: str
        self.owner_id = owner_id  # type: long
        self.project = project  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRealTimeLogDeliveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class CreateRealTimeLogDeliveryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRealTimeLogDeliveryResponseBody, self).to_map()
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


class CreateRealTimeLogDeliveryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateRealTimeLogDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRealTimeLogDeliveryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRealTimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUsageDetailDataExportTaskRequest(TeaModel):
    def __init__(self, domain_names=None, end_time=None, group=None, language=None, owner_id=None, start_time=None,
                 task_name=None, type=None):
        self.domain_names = domain_names  # type: str
        self.end_time = end_time  # type: str
        self.group = group  # type: str
        self.language = language  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.task_name = task_name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUsageDetailDataExportTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group is not None:
            result['Group'] = self.group
        if self.language is not None:
            result['Language'] = self.language
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateUsageDetailDataExportTaskResponseBody(TeaModel):
    def __init__(self, end_time=None, request_id=None, start_time=None, task_id=None):
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUsageDetailDataExportTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateUsageDetailDataExportTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateUsageDetailDataExportTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUsageDetailDataExportTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUsageDetailDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserUsageDataExportTaskRequest(TeaModel):
    def __init__(self, end_time=None, language=None, owner_id=None, start_time=None, task_name=None):
        self.end_time = end_time  # type: str
        self.language = language  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserUsageDataExportTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.language is not None:
            result['Language'] = self.language
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateUserUsageDataExportTaskResponseBody(TeaModel):
    def __init__(self, end_time=None, request_id=None, start_time=None, task_id=None):
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserUsageDataExportTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateUserUsageDataExportTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateUserUsageDataExportTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUserUsageDataExportTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUserUsageDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCdnDeliverTaskRequest(TeaModel):
    def __init__(self, deliver_id=None, owner_id=None):
        self.deliver_id = deliver_id  # type: long
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCdnDeliverTaskRequest, self).to_map()
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


class DeleteCdnDeliverTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCdnDeliverTaskResponseBody, self).to_map()
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


class DeleteCdnDeliverTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteCdnDeliverTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCdnDeliverTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteCdnDeliverTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCdnDomainRequest(TeaModel):
    def __init__(self, domain_name=None, owner_account=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCdnDomainRequest, self).to_map()
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


class DeleteCdnDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCdnDomainResponseBody, self).to_map()
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


class DeleteCdnDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteCdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCdnDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCdnSubTaskRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCdnSubTaskRequest, self).to_map()
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


class DeleteCdnSubTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCdnSubTaskResponseBody, self).to_map()
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


class DeleteCdnSubTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteCdnSubTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCdnSubTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteCdnSubTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFCTriggerRequest(TeaModel):
    def __init__(self, owner_id=None, trigger_arn=None):
        self.owner_id = owner_id  # type: long
        self.trigger_arn = trigger_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFCTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        return self


class DeleteFCTriggerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFCTriggerResponseBody, self).to_map()
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


class DeleteFCTriggerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteFCTriggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFCTriggerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFCTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRealtimeLogDeliveryRequest(TeaModel):
    def __init__(self, domain=None, logstore=None, owner_id=None, project=None, region=None):
        self.domain = domain  # type: str
        self.logstore = logstore  # type: str
        self.owner_id = owner_id  # type: long
        self.project = project  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRealtimeLogDeliveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DeleteRealtimeLogDeliveryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRealtimeLogDeliveryResponseBody, self).to_map()
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


class DeleteRealtimeLogDeliveryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteRealtimeLogDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRealtimeLogDeliveryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteRealtimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSpecificConfigRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, owner_id=None, security_token=None):
        self.config_id = config_id  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSpecificConfigRequest, self).to_map()
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


class DeleteSpecificConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSpecificConfigResponseBody, self).to_map()
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


class DeleteSpecificConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSpecificConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSpecificConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSpecificConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSpecificStagingConfigRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, owner_id=None, security_token=None):
        self.config_id = config_id  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSpecificStagingConfigRequest, self).to_map()
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


class DeleteSpecificStagingConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSpecificStagingConfigResponseBody, self).to_map()
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


class DeleteSpecificStagingConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSpecificStagingConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSpecificStagingConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSpecificStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUsageDetailDataExportTaskRequest(TeaModel):
    def __init__(self, owner_id=None, task_id=None):
        self.owner_id = owner_id  # type: long
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUsageDetailDataExportTaskRequest, self).to_map()
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


class DeleteUsageDetailDataExportTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUsageDetailDataExportTaskResponseBody, self).to_map()
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


class DeleteUsageDetailDataExportTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteUsageDetailDataExportTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUsageDetailDataExportTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUsageDetailDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserUsageDataExportTaskRequest(TeaModel):
    def __init__(self, owner_id=None, task_id=None):
        self.owner_id = owner_id  # type: long
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserUsageDataExportTaskRequest, self).to_map()
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


class DeleteUserUsageDataExportTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserUsageDataExportTaskResponseBody, self).to_map()
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


class DeleteUserUsageDataExportTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteUserUsageDataExportTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserUsageDataExportTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserUsageDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeActiveVersionOfConfigGroupRequest(TeaModel):
    def __init__(self, config_group_id=None, env=None, owner_id=None):
        self.config_group_id = config_group_id  # type: str
        self.env = env  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeActiveVersionOfConfigGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_group_id is not None:
            result['ConfigGroupId'] = self.config_group_id
        if self.env is not None:
            result['Env'] = self.env
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigGroupId') is not None:
            self.config_group_id = m.get('ConfigGroupId')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeActiveVersionOfConfigGroupResponseBody(TeaModel):
    def __init__(self, base_version_id=None, config_group_id=None, create_time=None, description=None,
                 operator=None, request_id=None, seq_id=None, status=None, update_time=None, version_id=None):
        self.base_version_id = base_version_id  # type: str
        self.config_group_id = config_group_id  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.operator = operator  # type: str
        self.request_id = request_id  # type: str
        self.seq_id = seq_id  # type: long
        self.status = status  # type: str
        self.update_time = update_time  # type: str
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeActiveVersionOfConfigGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_version_id is not None:
            result['BaseVersionId'] = self.base_version_id
        if self.config_group_id is not None:
            result['ConfigGroupId'] = self.config_group_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.seq_id is not None:
            result['SeqId'] = self.seq_id
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BaseVersionId') is not None:
            self.base_version_id = m.get('BaseVersionId')
        if m.get('ConfigGroupId') is not None:
            self.config_group_id = m.get('ConfigGroupId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SeqId') is not None:
            self.seq_id = m.get('SeqId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DescribeActiveVersionOfConfigGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeActiveVersionOfConfigGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeActiveVersionOfConfigGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeActiveVersionOfConfigGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBlockedRegionsRequest(TeaModel):
    def __init__(self, language=None, owner_id=None):
        self.language = language  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBlockedRegionsRequest, self).to_map()
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


class DescribeBlockedRegionsResponseBodyInfoListInfoItem(TeaModel):
    def __init__(self, continent=None, countries_and_regions=None, countries_and_regions_name=None):
        self.continent = continent  # type: str
        self.countries_and_regions = countries_and_regions  # type: str
        self.countries_and_regions_name = countries_and_regions_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBlockedRegionsResponseBodyInfoListInfoItem, self).to_map()
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


class DescribeBlockedRegionsResponseBodyInfoList(TeaModel):
    def __init__(self, info_item=None):
        self.info_item = info_item  # type: list[DescribeBlockedRegionsResponseBodyInfoListInfoItem]

    def validate(self):
        if self.info_item:
            for k in self.info_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBlockedRegionsResponseBodyInfoList, self).to_map()
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
                temp_model = DescribeBlockedRegionsResponseBodyInfoListInfoItem()
                self.info_item.append(temp_model.from_map(k))
        return self


class DescribeBlockedRegionsResponseBody(TeaModel):
    def __init__(self, info_list=None, request_id=None):
        self.info_list = info_list  # type: DescribeBlockedRegionsResponseBodyInfoList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.info_list:
            self.info_list.validate()

    def to_map(self):
        _map = super(DescribeBlockedRegionsResponseBody, self).to_map()
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
            temp_model = DescribeBlockedRegionsResponseBodyInfoList()
            self.info_list = temp_model.from_map(m['InfoList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBlockedRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBlockedRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBlockedRegionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBlockedRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnCertificateDetailRequest(TeaModel):
    def __init__(self, cert_name=None, owner_id=None, security_token=None):
        self.cert_name = cert_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnCertificateDetailRequest, self).to_map()
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


class DescribeCdnCertificateDetailResponseBody(TeaModel):
    def __init__(self, cert=None, cert_id=None, cert_name=None, key=None, request_id=None):
        self.cert = cert  # type: str
        self.cert_id = cert_id  # type: long
        self.cert_name = cert_name  # type: str
        self.key = key  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnCertificateDetailResponseBody, self).to_map()
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


class DescribeCdnCertificateDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnCertificateDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnCertificateDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnCertificateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnCertificateListRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnCertificateListRequest, self).to_map()
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


class DescribeCdnCertificateListResponseBodyCertificateListModelCertListCert(TeaModel):
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
        _map = super(DescribeCdnCertificateListResponseBodyCertificateListModelCertListCert, self).to_map()
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


class DescribeCdnCertificateListResponseBodyCertificateListModelCertList(TeaModel):
    def __init__(self, cert=None):
        self.cert = cert  # type: list[DescribeCdnCertificateListResponseBodyCertificateListModelCertListCert]

    def validate(self):
        if self.cert:
            for k in self.cert:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnCertificateListResponseBodyCertificateListModelCertList, self).to_map()
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
                temp_model = DescribeCdnCertificateListResponseBodyCertificateListModelCertListCert()
                self.cert.append(temp_model.from_map(k))
        return self


class DescribeCdnCertificateListResponseBodyCertificateListModel(TeaModel):
    def __init__(self, cert_list=None, count=None):
        self.cert_list = cert_list  # type: DescribeCdnCertificateListResponseBodyCertificateListModelCertList
        self.count = count  # type: int

    def validate(self):
        if self.cert_list:
            self.cert_list.validate()

    def to_map(self):
        _map = super(DescribeCdnCertificateListResponseBodyCertificateListModel, self).to_map()
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
            temp_model = DescribeCdnCertificateListResponseBodyCertificateListModelCertList()
            self.cert_list = temp_model.from_map(m['CertList'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeCdnCertificateListResponseBody(TeaModel):
    def __init__(self, certificate_list_model=None, request_id=None):
        self.certificate_list_model = certificate_list_model  # type: DescribeCdnCertificateListResponseBodyCertificateListModel
        self.request_id = request_id  # type: str

    def validate(self):
        if self.certificate_list_model:
            self.certificate_list_model.validate()

    def to_map(self):
        _map = super(DescribeCdnCertificateListResponseBody, self).to_map()
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
            temp_model = DescribeCdnCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m['CertificateListModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnCertificateListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnCertificateListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnCertificateListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnCertificateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnComputeUserDomainRequest(TeaModel):
    def __init__(self, owner_id=None, page_number=None, page_size=None):
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnComputeUserDomainRequest, self).to_map()
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


class DescribeCdnComputeUserDomainResponseBodyDomainsPageData(TeaModel):
    def __init__(self, cname=None, domain_name=None, domain_status=None, gmt_created=None, gmt_modified=None):
        self.cname = cname  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnComputeUserDomainResponseBodyDomainsPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class DescribeCdnComputeUserDomainResponseBodyDomains(TeaModel):
    def __init__(self, page_data=None):
        self.page_data = page_data  # type: list[DescribeCdnComputeUserDomainResponseBodyDomainsPageData]

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnComputeUserDomainResponseBodyDomains, self).to_map()
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
                temp_model = DescribeCdnComputeUserDomainResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeCdnComputeUserDomainResponseBody(TeaModel):
    def __init__(self, domains=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.domains = domains  # type: DescribeCdnComputeUserDomainResponseBodyDomains
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super(DescribeCdnComputeUserDomainResponseBody, self).to_map()
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
            temp_model = DescribeCdnComputeUserDomainResponseBodyDomains()
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


class DescribeCdnComputeUserDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnComputeUserDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnComputeUserDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnComputeUserDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDeletedDomainsRequest(TeaModel):
    def __init__(self, owner_id=None, page_number=None, page_size=None):
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDeletedDomainsRequest, self).to_map()
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


class DescribeCdnDeletedDomainsResponseBodyDomainsPageData(TeaModel):
    def __init__(self, domain_name=None, gmt_modified=None):
        self.domain_name = domain_name  # type: str
        self.gmt_modified = gmt_modified  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDeletedDomainsResponseBodyDomainsPageData, self).to_map()
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


class DescribeCdnDeletedDomainsResponseBodyDomains(TeaModel):
    def __init__(self, page_data=None):
        self.page_data = page_data  # type: list[DescribeCdnDeletedDomainsResponseBodyDomainsPageData]

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnDeletedDomainsResponseBodyDomains, self).to_map()
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
                temp_model = DescribeCdnDeletedDomainsResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeCdnDeletedDomainsResponseBody(TeaModel):
    def __init__(self, domains=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.domains = domains  # type: DescribeCdnDeletedDomainsResponseBodyDomains
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super(DescribeCdnDeletedDomainsResponseBody, self).to_map()
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
            temp_model = DescribeCdnDeletedDomainsResponseBodyDomains()
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


class DescribeCdnDeletedDomainsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnDeletedDomainsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnDeletedDomainsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnDeletedDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDeliverListRequest(TeaModel):
    def __init__(self, deliver_id=None, owner_id=None):
        self.deliver_id = deliver_id  # type: long
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDeliverListRequest, self).to_map()
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


class DescribeCdnDeliverListResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDeliverListResponseBody, self).to_map()
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


class DescribeCdnDeliverListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnDeliverListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnDeliverListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnDeliverListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainByCertificateRequest(TeaModel):
    def __init__(self, owner_id=None, sslpub=None):
        self.owner_id = owner_id  # type: long
        self.sslpub = sslpub  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainByCertificateRequest, self).to_map()
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


class DescribeCdnDomainByCertificateResponseBodyCertInfosCertInfo(TeaModel):
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
        _map = super(DescribeCdnDomainByCertificateResponseBodyCertInfosCertInfo, self).to_map()
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


class DescribeCdnDomainByCertificateResponseBodyCertInfos(TeaModel):
    def __init__(self, cert_info=None):
        self.cert_info = cert_info  # type: list[DescribeCdnDomainByCertificateResponseBodyCertInfosCertInfo]

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainByCertificateResponseBodyCertInfos, self).to_map()
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
                temp_model = DescribeCdnDomainByCertificateResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainByCertificateResponseBody(TeaModel):
    def __init__(self, cert_infos=None, request_id=None):
        self.cert_infos = cert_infos  # type: DescribeCdnDomainByCertificateResponseBodyCertInfos
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainByCertificateResponseBody, self).to_map()
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
            temp_model = DescribeCdnDomainByCertificateResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnDomainByCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnDomainByCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainByCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnDomainByCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainConfigsRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, function_names=None, owner_id=None, security_token=None):
        self.config_id = config_id  # type: str
        self.domain_name = domain_name  # type: str
        self.function_names = function_names  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainConfigsRequest, self).to_map()
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


class DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg(TeaModel):
    def __init__(self, arg_name=None, arg_value=None):
        self.arg_name = arg_name  # type: str
        self.arg_value = arg_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg, self).to_map()
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


class DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs(TeaModel):
    def __init__(self, function_arg=None):
        self.function_arg = function_arg  # type: list[DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg]

    def validate(self):
        if self.function_arg:
            for k in self.function_arg:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs, self).to_map()
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
                temp_model = DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg()
                self.function_arg.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfig(TeaModel):
    def __init__(self, config_id=None, function_args=None, function_name=None, status=None):
        self.config_id = config_id  # type: str
        self.function_args = function_args  # type: DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs
        self.function_name = function_name  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfig, self).to_map()
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
            temp_model = DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs()
            self.function_args = temp_model.from_map(m['FunctionArgs'])
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCdnDomainConfigsResponseBodyDomainConfigs(TeaModel):
    def __init__(self, domain_config=None):
        self.domain_config = domain_config  # type: list[DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfig]

    def validate(self):
        if self.domain_config:
            for k in self.domain_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainConfigsResponseBodyDomainConfigs, self).to_map()
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
                temp_model = DescribeCdnDomainConfigsResponseBodyDomainConfigsDomainConfig()
                self.domain_config.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainConfigsResponseBody(TeaModel):
    def __init__(self, domain_configs=None, request_id=None):
        self.domain_configs = domain_configs  # type: DescribeCdnDomainConfigsResponseBodyDomainConfigs
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_configs:
            self.domain_configs.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainConfigsResponseBody, self).to_map()
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
            temp_model = DescribeCdnDomainConfigsResponseBodyDomainConfigs()
            self.domain_configs = temp_model.from_map(m['DomainConfigs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnDomainConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnDomainConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnDomainConfigsResponseBody()
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


class DescribeCdnDomainDetailResponseBodyGetDomainDetailModel(TeaModel):
    def __init__(self, cdn_type=None, cname=None, description=None, domain_name=None, domain_status=None,
                 gmt_created=None, gmt_modified=None, https_cname=None, resource_group_id=None, scope=None,
                 server_certificate_status=None, source_models=None):
        self.cdn_type = cdn_type  # type: str
        self.cname = cname  # type: str
        self.description = description  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.https_cname = https_cname  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.scope = scope  # type: str
        self.server_certificate_status = server_certificate_status  # type: str
        self.source_models = source_models  # type: DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModels

    def validate(self):
        if self.source_models:
            self.source_models.validate()

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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
        if self.source_models is not None:
            result['SourceModels'] = self.source_models.to_map()
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        if m.get('SourceModels') is not None:
            temp_model = DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModels()
            self.source_models = temp_model.from_map(m['SourceModels'])
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnDomainDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnDomainDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainLogsRequest(TeaModel):
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
        _map = super(DescribeCdnDomainLogsRequest, self).to_map()
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


class DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail(TeaModel):
    def __init__(self, end_time=None, log_name=None, log_path=None, log_size=None, start_time=None):
        self.end_time = end_time  # type: str
        self.log_name = log_name  # type: str
        self.log_path = log_path  # type: str
        self.log_size = log_size  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail, self).to_map()
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


class DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfos(TeaModel):
    def __init__(self, log_info_detail=None):
        self.log_info_detail = log_info_detail  # type: list[DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail]

    def validate(self):
        if self.log_info_detail:
            for k in self.log_info_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfos, self).to_map()
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
                temp_model = DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail()
                self.log_info_detail.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailPageInfos(TeaModel):
    def __init__(self, page_index=None, page_size=None, total=None):
        self.page_index = page_index  # type: long
        self.page_size = page_size  # type: long
        self.total = total  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailPageInfos, self).to_map()
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


class DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetail(TeaModel):
    def __init__(self, domain_name=None, log_count=None, log_infos=None, page_infos=None):
        self.domain_name = domain_name  # type: str
        self.log_count = log_count  # type: long
        self.log_infos = log_infos  # type: DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfos
        self.page_infos = page_infos  # type: DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailPageInfos

    def validate(self):
        if self.log_infos:
            self.log_infos.validate()
        if self.page_infos:
            self.page_infos.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.log_count is not None:
            result['LogCount'] = self.log_count
        if self.log_infos is not None:
            result['LogInfos'] = self.log_infos.to_map()
        if self.page_infos is not None:
            result['PageInfos'] = self.page_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LogCount') is not None:
            self.log_count = m.get('LogCount')
        if m.get('LogInfos') is not None:
            temp_model = DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailLogInfos()
            self.log_infos = temp_model.from_map(m['LogInfos'])
        if m.get('PageInfos') is not None:
            temp_model = DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetailPageInfos()
            self.page_infos = temp_model.from_map(m['PageInfos'])
        return self


class DescribeCdnDomainLogsResponseBodyDomainLogDetails(TeaModel):
    def __init__(self, domain_log_detail=None):
        self.domain_log_detail = domain_log_detail  # type: list[DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetail]

    def validate(self):
        if self.domain_log_detail:
            for k in self.domain_log_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainLogsResponseBodyDomainLogDetails, self).to_map()
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
                temp_model = DescribeCdnDomainLogsResponseBodyDomainLogDetailsDomainLogDetail()
                self.domain_log_detail.append(temp_model.from_map(k))
        return self


class DescribeCdnDomainLogsResponseBody(TeaModel):
    def __init__(self, domain_log_details=None, request_id=None):
        self.domain_log_details = domain_log_details  # type: DescribeCdnDomainLogsResponseBodyDomainLogDetails
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_log_details:
            self.domain_log_details.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_log_details is not None:
            result['DomainLogDetails'] = self.domain_log_details.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainLogDetails') is not None:
            temp_model = DescribeCdnDomainLogsResponseBodyDomainLogDetails()
            self.domain_log_details = temp_model.from_map(m['DomainLogDetails'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnDomainLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnDomainLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnDomainLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnDomainStagingConfigRequest(TeaModel):
    def __init__(self, domain_name=None, function_names=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.function_names = function_names  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainStagingConfigRequest, self).to_map()
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


class DescribeCdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs(TeaModel):
    def __init__(self, arg_name=None, arg_value=None):
        self.arg_name = arg_name  # type: str
        self.arg_value = arg_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs, self).to_map()
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


class DescribeCdnDomainStagingConfigResponseBodyDomainConfigs(TeaModel):
    def __init__(self, config_id=None, function_args=None, function_name=None, status=None):
        self.config_id = config_id  # type: str
        self.function_args = function_args  # type: list[DescribeCdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs]
        self.function_name = function_name  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.function_args:
            for k in self.function_args:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainStagingConfigResponseBodyDomainConfigs, self).to_map()
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
                temp_model = DescribeCdnDomainStagingConfigResponseBodyDomainConfigsFunctionArgs()
                self.function_args.append(temp_model.from_map(k))
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCdnDomainStagingConfigResponseBody(TeaModel):
    def __init__(self, domain_configs=None, request_id=None):
        self.domain_configs = domain_configs  # type: list[DescribeCdnDomainStagingConfigResponseBodyDomainConfigs]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_configs:
            for k in self.domain_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainStagingConfigResponseBody, self).to_map()
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
                temp_model = DescribeCdnDomainStagingConfigResponseBodyDomainConfigs()
                self.domain_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnDomainStagingConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnDomainStagingConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnDomainStagingConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnDomainStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnHttpsDomainListRequest(TeaModel):
    def __init__(self, keyword=None, owner_id=None, page_number=None, page_size=None):
        self.keyword = keyword  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnHttpsDomainListRequest, self).to_map()
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


class DescribeCdnHttpsDomainListResponseBodyCertInfosCertInfo(TeaModel):
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
        _map = super(DescribeCdnHttpsDomainListResponseBodyCertInfosCertInfo, self).to_map()
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


class DescribeCdnHttpsDomainListResponseBodyCertInfos(TeaModel):
    def __init__(self, cert_info=None):
        self.cert_info = cert_info  # type: list[DescribeCdnHttpsDomainListResponseBodyCertInfosCertInfo]

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnHttpsDomainListResponseBodyCertInfos, self).to_map()
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
                temp_model = DescribeCdnHttpsDomainListResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeCdnHttpsDomainListResponseBody(TeaModel):
    def __init__(self, cert_infos=None, request_id=None, total_count=None):
        self.cert_infos = cert_infos  # type: DescribeCdnHttpsDomainListResponseBodyCertInfos
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super(DescribeCdnHttpsDomainListResponseBody, self).to_map()
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
            temp_model = DescribeCdnHttpsDomainListResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCdnHttpsDomainListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnHttpsDomainListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnHttpsDomainListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnHttpsDomainListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnRegionAndIspRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnRegionAndIspRequest, self).to_map()
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


class DescribeCdnRegionAndIspResponseBodyIspsIsp(TeaModel):
    def __init__(self, name_en=None, name_zh=None):
        self.name_en = name_en  # type: str
        self.name_zh = name_zh  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnRegionAndIspResponseBodyIspsIsp, self).to_map()
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


class DescribeCdnRegionAndIspResponseBodyIsps(TeaModel):
    def __init__(self, isp=None):
        self.isp = isp  # type: list[DescribeCdnRegionAndIspResponseBodyIspsIsp]

    def validate(self):
        if self.isp:
            for k in self.isp:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnRegionAndIspResponseBodyIsps, self).to_map()
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
                temp_model = DescribeCdnRegionAndIspResponseBodyIspsIsp()
                self.isp.append(temp_model.from_map(k))
        return self


class DescribeCdnRegionAndIspResponseBodyRegionsRegion(TeaModel):
    def __init__(self, name_en=None, name_zh=None):
        self.name_en = name_en  # type: str
        self.name_zh = name_zh  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnRegionAndIspResponseBodyRegionsRegion, self).to_map()
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


class DescribeCdnRegionAndIspResponseBodyRegions(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: list[DescribeCdnRegionAndIspResponseBodyRegionsRegion]

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnRegionAndIspResponseBodyRegions, self).to_map()
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
                temp_model = DescribeCdnRegionAndIspResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeCdnRegionAndIspResponseBody(TeaModel):
    def __init__(self, isps=None, regions=None, request_id=None):
        self.isps = isps  # type: DescribeCdnRegionAndIspResponseBodyIsps
        self.regions = regions  # type: DescribeCdnRegionAndIspResponseBodyRegions
        self.request_id = request_id  # type: str

    def validate(self):
        if self.isps:
            self.isps.validate()
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeCdnRegionAndIspResponseBody, self).to_map()
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
            temp_model = DescribeCdnRegionAndIspResponseBodyIsps()
            self.isps = temp_model.from_map(m['Isps'])
        if m.get('Regions') is not None:
            temp_model = DescribeCdnRegionAndIspResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnRegionAndIspResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnRegionAndIspResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnRegionAndIspResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnRegionAndIspResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnReportRequest(TeaModel):
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
        _map = super(DescribeCdnReportRequest, self).to_map()
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


class DescribeCdnReportResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnReportResponseBody, self).to_map()
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


class DescribeCdnReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnReportResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnReportListRequest(TeaModel):
    def __init__(self, owner_id=None, report_id=None):
        self.owner_id = owner_id  # type: long
        self.report_id = report_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnReportListRequest, self).to_map()
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


class DescribeCdnReportListResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnReportListResponseBody, self).to_map()
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


class DescribeCdnReportListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnReportListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnReportListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnReportListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnSMCertificateDetailRequest(TeaModel):
    def __init__(self, cert_identifier=None, owner_id=None, security_token=None):
        self.cert_identifier = cert_identifier  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnSMCertificateDetailRequest, self).to_map()
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


class DescribeCdnSMCertificateDetailResponseBody(TeaModel):
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
        _map = super(DescribeCdnSMCertificateDetailResponseBody, self).to_map()
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


class DescribeCdnSMCertificateDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnSMCertificateDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnSMCertificateDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnSMCertificateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnSMCertificateListRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnSMCertificateListRequest, self).to_map()
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


class DescribeCdnSMCertificateListResponseBodyCertificateListModelCertListCert(TeaModel):
    def __init__(self, cert_identifier=None, cert_name=None, common=None, issuer=None):
        self.cert_identifier = cert_identifier  # type: str
        self.cert_name = cert_name  # type: str
        self.common = common  # type: str
        self.issuer = issuer  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnSMCertificateListResponseBodyCertificateListModelCertListCert, self).to_map()
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


class DescribeCdnSMCertificateListResponseBodyCertificateListModelCertList(TeaModel):
    def __init__(self, cert=None):
        self.cert = cert  # type: list[DescribeCdnSMCertificateListResponseBodyCertificateListModelCertListCert]

    def validate(self):
        if self.cert:
            for k in self.cert:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnSMCertificateListResponseBodyCertificateListModelCertList, self).to_map()
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
                temp_model = DescribeCdnSMCertificateListResponseBodyCertificateListModelCertListCert()
                self.cert.append(temp_model.from_map(k))
        return self


class DescribeCdnSMCertificateListResponseBodyCertificateListModel(TeaModel):
    def __init__(self, cert_list=None, count=None):
        self.cert_list = cert_list  # type: DescribeCdnSMCertificateListResponseBodyCertificateListModelCertList
        self.count = count  # type: int

    def validate(self):
        if self.cert_list:
            self.cert_list.validate()

    def to_map(self):
        _map = super(DescribeCdnSMCertificateListResponseBodyCertificateListModel, self).to_map()
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
            temp_model = DescribeCdnSMCertificateListResponseBodyCertificateListModelCertList()
            self.cert_list = temp_model.from_map(m['CertList'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeCdnSMCertificateListResponseBody(TeaModel):
    def __init__(self, certificate_list_model=None, request_id=None):
        self.certificate_list_model = certificate_list_model  # type: DescribeCdnSMCertificateListResponseBodyCertificateListModel
        self.request_id = request_id  # type: str

    def validate(self):
        if self.certificate_list_model:
            self.certificate_list_model.validate()

    def to_map(self):
        _map = super(DescribeCdnSMCertificateListResponseBody, self).to_map()
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
            temp_model = DescribeCdnSMCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m['CertificateListModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnSMCertificateListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnSMCertificateListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnSMCertificateListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnSMCertificateListResponseBody()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnSubListRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnSubListRequest, self).to_map()
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


class DescribeCdnSubListResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnSubListResponseBody, self).to_map()
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


class DescribeCdnSubListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnSubListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnSubListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnSubListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserBillHistoryRequest(TeaModel):
    def __init__(self, end_time=None, owner_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnUserBillHistoryRequest, self).to_map()
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


class DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem(TeaModel):
    def __init__(self, bandwidth=None, cdn_region=None, charge_type=None, count=None, flow=None):
        self.bandwidth = bandwidth  # type: float
        self.cdn_region = cdn_region  # type: str
        self.charge_type = charge_type  # type: str
        self.count = count  # type: float
        self.flow = flow  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem, self).to_map()
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


class DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData(TeaModel):
    def __init__(self, billing_data_item=None):
        self.billing_data_item = billing_data_item  # type: list[DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem]

    def validate(self):
        if self.billing_data_item:
            for k in self.billing_data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData, self).to_map()
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
                temp_model = DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem()
                self.billing_data_item.append(temp_model.from_map(k))
        return self


class DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem(TeaModel):
    def __init__(self, bill_time=None, bill_type=None, billing_data=None, dimension=None):
        self.bill_time = bill_time  # type: str
        self.bill_type = bill_type  # type: str
        self.billing_data = billing_data  # type: DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData
        self.dimension = dimension  # type: str

    def validate(self):
        if self.billing_data:
            self.billing_data.validate()

    def to_map(self):
        _map = super(DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem, self).to_map()
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
            temp_model = DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData()
            self.billing_data = temp_model.from_map(m['BillingData'])
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        return self


class DescribeCdnUserBillHistoryResponseBodyBillHistoryData(TeaModel):
    def __init__(self, bill_history_data_item=None):
        self.bill_history_data_item = bill_history_data_item  # type: list[DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem]

    def validate(self):
        if self.bill_history_data_item:
            for k in self.bill_history_data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnUserBillHistoryResponseBodyBillHistoryData, self).to_map()
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
                temp_model = DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem()
                self.bill_history_data_item.append(temp_model.from_map(k))
        return self


class DescribeCdnUserBillHistoryResponseBody(TeaModel):
    def __init__(self, bill_history_data=None, request_id=None):
        self.bill_history_data = bill_history_data  # type: DescribeCdnUserBillHistoryResponseBodyBillHistoryData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.bill_history_data:
            self.bill_history_data.validate()

    def to_map(self):
        _map = super(DescribeCdnUserBillHistoryResponseBody, self).to_map()
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
            temp_model = DescribeCdnUserBillHistoryResponseBodyBillHistoryData()
            self.bill_history_data = temp_model.from_map(m['BillHistoryData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnUserBillHistoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnUserBillHistoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnUserBillHistoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnUserBillHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserBillPredictionRequest(TeaModel):
    def __init__(self, area=None, dimension=None, end_time=None, owner_id=None, start_time=None):
        self.area = area  # type: str
        self.dimension = dimension  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnUserBillPredictionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCdnUserBillPredictionResponseBodyBillPredictionDataBillPredictionDataItem(TeaModel):
    def __init__(self, area=None, time_stp=None, value=None):
        self.area = area  # type: str
        self.time_stp = time_stp  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnUserBillPredictionResponseBodyBillPredictionDataBillPredictionDataItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.time_stp is not None:
            result['TimeStp'] = self.time_stp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('TimeStp') is not None:
            self.time_stp = m.get('TimeStp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeCdnUserBillPredictionResponseBodyBillPredictionData(TeaModel):
    def __init__(self, bill_prediction_data_item=None):
        self.bill_prediction_data_item = bill_prediction_data_item  # type: list[DescribeCdnUserBillPredictionResponseBodyBillPredictionDataBillPredictionDataItem]

    def validate(self):
        if self.bill_prediction_data_item:
            for k in self.bill_prediction_data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnUserBillPredictionResponseBodyBillPredictionData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BillPredictionDataItem'] = []
        if self.bill_prediction_data_item is not None:
            for k in self.bill_prediction_data_item:
                result['BillPredictionDataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bill_prediction_data_item = []
        if m.get('BillPredictionDataItem') is not None:
            for k in m.get('BillPredictionDataItem'):
                temp_model = DescribeCdnUserBillPredictionResponseBodyBillPredictionDataBillPredictionDataItem()
                self.bill_prediction_data_item.append(temp_model.from_map(k))
        return self


class DescribeCdnUserBillPredictionResponseBody(TeaModel):
    def __init__(self, bill_prediction_data=None, bill_type=None, end_time=None, request_id=None, start_time=None):
        self.bill_prediction_data = bill_prediction_data  # type: DescribeCdnUserBillPredictionResponseBodyBillPredictionData
        self.bill_type = bill_type  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.bill_prediction_data:
            self.bill_prediction_data.validate()

    def to_map(self):
        _map = super(DescribeCdnUserBillPredictionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_prediction_data is not None:
            result['BillPredictionData'] = self.bill_prediction_data.to_map()
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillPredictionData') is not None:
            temp_model = DescribeCdnUserBillPredictionResponseBodyBillPredictionData()
            self.bill_prediction_data = temp_model.from_map(m['BillPredictionData'])
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCdnUserBillPredictionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnUserBillPredictionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnUserBillPredictionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnUserBillPredictionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserBillTypeRequest(TeaModel):
    def __init__(self, end_time=None, owner_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnUserBillTypeRequest, self).to_map()
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


class DescribeCdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem(TeaModel):
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
        _map = super(DescribeCdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem, self).to_map()
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


class DescribeCdnUserBillTypeResponseBodyBillTypeData(TeaModel):
    def __init__(self, bill_type_data_item=None):
        self.bill_type_data_item = bill_type_data_item  # type: list[DescribeCdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem]

    def validate(self):
        if self.bill_type_data_item:
            for k in self.bill_type_data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnUserBillTypeResponseBodyBillTypeData, self).to_map()
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
                temp_model = DescribeCdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem()
                self.bill_type_data_item.append(temp_model.from_map(k))
        return self


class DescribeCdnUserBillTypeResponseBody(TeaModel):
    def __init__(self, bill_type_data=None, request_id=None):
        self.bill_type_data = bill_type_data  # type: DescribeCdnUserBillTypeResponseBodyBillTypeData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.bill_type_data:
            self.bill_type_data.validate()

    def to_map(self):
        _map = super(DescribeCdnUserBillTypeResponseBody, self).to_map()
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
            temp_model = DescribeCdnUserBillTypeResponseBodyBillTypeData()
            self.bill_type_data = temp_model.from_map(m['BillTypeData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnUserBillTypeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnUserBillTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnUserBillTypeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnUserBillTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserConfigsRequest(TeaModel):
    def __init__(self, function_name=None, owner_id=None):
        self.function_name = function_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnUserConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeCdnUserConfigsResponseBodyConfigs(TeaModel):
    def __init__(self, arg_name=None, arg_value=None, function_name=None):
        self.arg_name = arg_name  # type: str
        self.arg_value = arg_value  # type: str
        self.function_name = function_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnUserConfigsResponseBodyConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name
        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')
        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        return self


class DescribeCdnUserConfigsResponseBody(TeaModel):
    def __init__(self, configs=None, request_id=None):
        self.configs = configs  # type: list[DescribeCdnUserConfigsResponseBodyConfigs]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnUserConfigsResponseBody, self).to_map()
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
                temp_model = DescribeCdnUserConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnUserConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnUserConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnUserConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnUserConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserDomainsByFuncRequest(TeaModel):
    def __init__(self, func_id=None, owner_id=None, page_number=None, page_size=None, resource_group_id=None):
        self.func_id = func_id  # type: int
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnUserDomainsByFuncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource(TeaModel):
    def __init__(self, content=None, port=None, priority=None, type=None, weight=None):
        self.content = content  # type: str
        self.port = port  # type: int
        self.priority = priority  # type: str
        self.type = type  # type: str
        self.weight = weight  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource, self).to_map()
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


class DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSources(TeaModel):
    def __init__(self, source=None):
        self.source = source  # type: list[DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource]

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSources, self).to_map()
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
                temp_model = DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeCdnUserDomainsByFuncResponseBodyDomainsPageData(TeaModel):
    def __init__(self, cdn_type=None, cname=None, description=None, domain_name=None, domain_status=None,
                 gmt_created=None, gmt_modified=None, resource_group_id=None, sources=None, ssl_protocol=None):
        self.cdn_type = cdn_type  # type: str
        self.cname = cname  # type: str
        self.description = description  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.sources = sources  # type: DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSources
        self.ssl_protocol = ssl_protocol  # type: str

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super(DescribeCdnUserDomainsByFuncResponseBodyDomainsPageData, self).to_map()
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
        if m.get('Sources') is not None:
            temp_model = DescribeCdnUserDomainsByFuncResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m['Sources'])
        if m.get('SslProtocol') is not None:
            self.ssl_protocol = m.get('SslProtocol')
        return self


class DescribeCdnUserDomainsByFuncResponseBodyDomains(TeaModel):
    def __init__(self, page_data=None):
        self.page_data = page_data  # type: list[DescribeCdnUserDomainsByFuncResponseBodyDomainsPageData]

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnUserDomainsByFuncResponseBodyDomains, self).to_map()
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
                temp_model = DescribeCdnUserDomainsByFuncResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeCdnUserDomainsByFuncResponseBody(TeaModel):
    def __init__(self, domains=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.domains = domains  # type: DescribeCdnUserDomainsByFuncResponseBodyDomains
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super(DescribeCdnUserDomainsByFuncResponseBody, self).to_map()
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
            temp_model = DescribeCdnUserDomainsByFuncResponseBodyDomains()
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


class DescribeCdnUserDomainsByFuncResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnUserDomainsByFuncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnUserDomainsByFuncResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnUserDomainsByFuncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserQuotaRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnUserQuotaRequest, self).to_map()
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


class DescribeCdnUserQuotaResponseBody(TeaModel):
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
        _map = super(DescribeCdnUserQuotaResponseBody, self).to_map()
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


class DescribeCdnUserQuotaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnUserQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnUserQuotaResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnUserQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnUserResourcePackageRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, status=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnUserResourcePackageRequest, self).to_map()
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


class DescribeCdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo(TeaModel):
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
        _map = super(DescribeCdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo, self).to_map()
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


class DescribeCdnUserResourcePackageResponseBodyResourcePackageInfos(TeaModel):
    def __init__(self, resource_package_info=None):
        self.resource_package_info = resource_package_info  # type: list[DescribeCdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo]

    def validate(self):
        if self.resource_package_info:
            for k in self.resource_package_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnUserResourcePackageResponseBodyResourcePackageInfos, self).to_map()
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
                temp_model = DescribeCdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo()
                self.resource_package_info.append(temp_model.from_map(k))
        return self


class DescribeCdnUserResourcePackageResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_package_infos=None):
        self.request_id = request_id  # type: str
        self.resource_package_infos = resource_package_infos  # type: DescribeCdnUserResourcePackageResponseBodyResourcePackageInfos

    def validate(self):
        if self.resource_package_infos:
            self.resource_package_infos.validate()

    def to_map(self):
        _map = super(DescribeCdnUserResourcePackageResponseBody, self).to_map()
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
            temp_model = DescribeCdnUserResourcePackageResponseBodyResourcePackageInfos()
            self.resource_package_infos = temp_model.from_map(m['ResourcePackageInfos'])
        return self


class DescribeCdnUserResourcePackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnUserResourcePackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnUserResourcePackageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnUserResourcePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnWafDomainRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, region_id=None, resource_group_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnWafDomainRequest, self).to_map()
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


class DescribeCdnWafDomainResponseBodyOutPutDomains(TeaModel):
    def __init__(self, acl_status=None, cc_status=None, domain=None, status=None, waf_status=None):
        self.acl_status = acl_status  # type: str
        self.cc_status = cc_status  # type: str
        self.domain = domain  # type: str
        self.status = status  # type: str
        self.waf_status = waf_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCdnWafDomainResponseBodyOutPutDomains, self).to_map()
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


class DescribeCdnWafDomainResponseBody(TeaModel):
    def __init__(self, out_put_domains=None, request_id=None, total_count=None):
        self.out_put_domains = out_put_domains  # type: list[DescribeCdnWafDomainResponseBodyOutPutDomains]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.out_put_domains:
            for k in self.out_put_domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCdnWafDomainResponseBody, self).to_map()
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
                temp_model = DescribeCdnWafDomainResponseBodyOutPutDomains()
                self.out_put_domains.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCdnWafDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCdnWafDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCdnWafDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCdnWafDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertificateInfoByIDRequest(TeaModel):
    def __init__(self, cert_id=None, owner_id=None):
        self.cert_id = cert_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCertificateInfoByIDRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeCertificateInfoByIDResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(self, cert_expire_time=None, cert_id=None, cert_name=None, cert_type=None, create_time=None,
                 domain_list=None, https_crt=None):
        self.cert_expire_time = cert_expire_time  # type: str
        self.cert_id = cert_id  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_type = cert_type  # type: str
        self.create_time = create_time  # type: str
        self.domain_list = domain_list  # type: str
        self.https_crt = https_crt  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCertificateInfoByIDResponseBodyCertInfosCertInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.https_crt is not None:
            result['HttpsCrt'] = self.https_crt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('HttpsCrt') is not None:
            self.https_crt = m.get('HttpsCrt')
        return self


class DescribeCertificateInfoByIDResponseBodyCertInfos(TeaModel):
    def __init__(self, cert_info=None):
        self.cert_info = cert_info  # type: list[DescribeCertificateInfoByIDResponseBodyCertInfosCertInfo]

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCertificateInfoByIDResponseBodyCertInfos, self).to_map()
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
                temp_model = DescribeCertificateInfoByIDResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeCertificateInfoByIDResponseBody(TeaModel):
    def __init__(self, cert_infos=None, request_id=None):
        self.cert_infos = cert_infos  # type: DescribeCertificateInfoByIDResponseBodyCertInfos
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super(DescribeCertificateInfoByIDResponseBody, self).to_map()
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
            temp_model = DescribeCertificateInfoByIDResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCertificateInfoByIDResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCertificateInfoByIDResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCertificateInfoByIDResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCertificateInfoByIDResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConfigGroupDetailRequest(TeaModel):
    def __init__(self, config_group_id=None, config_group_name=None, owner_id=None):
        self.config_group_id = config_group_id  # type: str
        self.config_group_name = config_group_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeConfigGroupDetailRequest, self).to_map()
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


class DescribeConfigGroupDetailResponseBody(TeaModel):
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
        _map = super(DescribeConfigGroupDetailResponseBody, self).to_map()
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


class DescribeConfigGroupDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeConfigGroupDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeConfigGroupDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeConfigGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConfigOfVersionRequest(TeaModel):
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
        _map = super(DescribeConfigOfVersionRequest, self).to_map()
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


class DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgsFunctionArg(TeaModel):
    def __init__(self, arg_name=None, arg_value=None):
        self.arg_name = arg_name  # type: str
        self.arg_value = arg_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgsFunctionArg, self).to_map()
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


class DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgs(TeaModel):
    def __init__(self, function_arg=None):
        self.function_arg = function_arg  # type: list[DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgsFunctionArg]

    def validate(self):
        if self.function_arg:
            for k in self.function_arg:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgs, self).to_map()
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
                temp_model = DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgsFunctionArg()
                self.function_arg.append(temp_model.from_map(k))
        return self


class DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfig(TeaModel):
    def __init__(self, config_id=None, function_args=None, function_name=None, status=None):
        self.config_id = config_id  # type: str
        self.function_args = function_args  # type: DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgs
        self.function_name = function_name  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
        _map = super(DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfig, self).to_map()
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
            temp_model = DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfigFunctionArgs()
            self.function_args = temp_model.from_map(m['FunctionArgs'])
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeConfigOfVersionResponseBodyVersionConfigs(TeaModel):
    def __init__(self, version_config=None):
        self.version_config = version_config  # type: list[DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfig]

    def validate(self):
        if self.version_config:
            for k in self.version_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeConfigOfVersionResponseBodyVersionConfigs, self).to_map()
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
                temp_model = DescribeConfigOfVersionResponseBodyVersionConfigsVersionConfig()
                self.version_config.append(temp_model.from_map(k))
        return self


class DescribeConfigOfVersionResponseBody(TeaModel):
    def __init__(self, request_id=None, version_configs=None):
        self.request_id = request_id  # type: str
        self.version_configs = version_configs  # type: DescribeConfigOfVersionResponseBodyVersionConfigs

    def validate(self):
        if self.version_configs:
            self.version_configs.validate()

    def to_map(self):
        _map = super(DescribeConfigOfVersionResponseBody, self).to_map()
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
            temp_model = DescribeConfigOfVersionResponseBodyVersionConfigs()
            self.version_configs = temp_model.from_map(m['VersionConfigs'])
        return self


class DescribeConfigOfVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeConfigOfVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeConfigOfVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeConfigOfVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomLogConfigRequest(TeaModel):
    def __init__(self, config_id=None, owner_id=None):
        self.config_id = config_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomLogConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeCustomLogConfigResponseBody(TeaModel):
    def __init__(self, remark=None, request_id=None, sample=None, tag=None):
        self.remark = remark  # type: str
        self.request_id = request_id  # type: str
        self.sample = sample  # type: str
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCustomLogConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DescribeCustomLogConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCustomLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCustomLogConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCustomLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainAverageResponseTimeRequest(TeaModel):
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
        _map = super(DescribeDomainAverageResponseTimeRequest, self).to_map()
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


class DescribeDomainAverageResponseTimeResponseBodyAvgRTPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainAverageResponseTimeResponseBodyAvgRTPerIntervalDataModule, self).to_map()
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


class DescribeDomainAverageResponseTimeResponseBodyAvgRTPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainAverageResponseTimeResponseBodyAvgRTPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainAverageResponseTimeResponseBodyAvgRTPerInterval, self).to_map()
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
                temp_model = DescribeDomainAverageResponseTimeResponseBodyAvgRTPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainAverageResponseTimeResponseBody(TeaModel):
    def __init__(self, avg_rtper_interval=None, data_interval=None, domain_name=None, end_time=None,
                 request_id=None, start_time=None):
        self.avg_rtper_interval = avg_rtper_interval  # type: DescribeDomainAverageResponseTimeResponseBodyAvgRTPerInterval
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.avg_rtper_interval:
            self.avg_rtper_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainAverageResponseTimeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_rtper_interval is not None:
            result['AvgRTPerInterval'] = self.avg_rtper_interval.to_map()
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
        if m.get('AvgRTPerInterval') is not None:
            temp_model = DescribeDomainAverageResponseTimeResponseBodyAvgRTPerInterval()
            self.avg_rtper_interval = temp_model.from_map(m['AvgRTPerInterval'])
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


class DescribeDomainAverageResponseTimeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainAverageResponseTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainAverageResponseTimeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainAverageResponseTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainBpsDataRequest(TeaModel):
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
        _map = super(DescribeDomainBpsDataRequest, self).to_map()
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


class DescribeDomainBpsDataResponseBodyBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, domestic_value=None, https_domestic_value=None, https_overseas_value=None, https_value=None,
                 overseas_value=None, time_stamp=None, value=None):
        self.domestic_value = domestic_value  # type: str
        self.https_domestic_value = https_domestic_value  # type: str
        self.https_overseas_value = https_overseas_value  # type: str
        self.https_value = https_value  # type: str
        self.overseas_value = overseas_value  # type: str
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainBpsDataResponseBodyBpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        if self.https_domestic_value is not None:
            result['HttpsDomesticValue'] = self.https_domestic_value
        if self.https_overseas_value is not None:
            result['HttpsOverseasValue'] = self.https_overseas_value
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        if m.get('HttpsDomesticValue') is not None:
            self.https_domestic_value = m.get('HttpsDomesticValue')
        if m.get('HttpsOverseasValue') is not None:
            self.https_overseas_value = m.get('HttpsOverseasValue')
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
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
                 isp_name_en=None, location_name_en=None, request_id=None, start_time=None):
        self.bps_data_per_interval = bps_data_per_interval  # type: DescribeDomainBpsDataResponseBodyBpsDataPerInterval
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.isp_name_en = isp_name_en  # type: str
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
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
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
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainBpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainBpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainBpsDataByLayerRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, isp_name_en=None, layer=None,
                 location_name_en=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.layer = layer  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainBpsDataByLayerRequest, self).to_map()
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
        if self.layer is not None:
            result['Layer'] = self.layer
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
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainBpsDataByLayerResponseBodyBpsDataIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, traffic_value=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.traffic_value = traffic_value  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainBpsDataByLayerResponseBodyBpsDataIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.traffic_value is not None:
            result['TrafficValue'] = self.traffic_value
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TrafficValue') is not None:
            self.traffic_value = m.get('TrafficValue')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainBpsDataByLayerResponseBodyBpsDataInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainBpsDataByLayerResponseBodyBpsDataIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainBpsDataByLayerResponseBodyBpsDataInterval, self).to_map()
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
                temp_model = DescribeDomainBpsDataByLayerResponseBodyBpsDataIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainBpsDataByLayerResponseBody(TeaModel):
    def __init__(self, bps_data_interval=None, data_interval=None, request_id=None):
        self.bps_data_interval = bps_data_interval  # type: DescribeDomainBpsDataByLayerResponseBodyBpsDataInterval
        self.data_interval = data_interval  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.bps_data_interval:
            self.bps_data_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainBpsDataByLayerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps_data_interval is not None:
            result['BpsDataInterval'] = self.bps_data_interval.to_map()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BpsDataInterval') is not None:
            temp_model = DescribeDomainBpsDataByLayerResponseBodyBpsDataInterval()
            self.bps_data_interval = temp_model.from_map(m['BpsDataInterval'])
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainBpsDataByLayerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainBpsDataByLayerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainBpsDataByLayerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainBpsDataByLayerResponseBody()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainBpsDataByTimeStampResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainBpsDataByTimeStampResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainCcActivityLogRequest(TeaModel):
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
        _map = super(DescribeDomainCcActivityLogRequest, self).to_map()
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


class DescribeDomainCcActivityLogResponseBodyActivityLog(TeaModel):
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
        _map = super(DescribeDomainCcActivityLogResponseBodyActivityLog, self).to_map()
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


class DescribeDomainCcActivityLogResponseBody(TeaModel):
    def __init__(self, activity_log=None, page_index=None, page_size=None, request_id=None, total=None):
        self.activity_log = activity_log  # type: list[DescribeDomainCcActivityLogResponseBodyActivityLog]
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
        _map = super(DescribeDomainCcActivityLogResponseBody, self).to_map()
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
                temp_model = DescribeDomainCcActivityLogResponseBodyActivityLog()
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


class DescribeDomainCcActivityLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainCcActivityLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainCcActivityLogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainCcActivityLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainCertificateInfoRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainCertificateInfoRequest, self).to_map()
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


class DescribeDomainCertificateInfoResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(self, cert_domain_name=None, cert_expire_time=None, cert_life=None, cert_name=None, cert_org=None,
                 cert_start_time=None, cert_type=None, cert_update_time=None, domain_cname_status=None, domain_name=None,
                 server_certificate=None, server_certificate_status=None, status=None):
        self.cert_domain_name = cert_domain_name  # type: str
        self.cert_expire_time = cert_expire_time  # type: str
        self.cert_life = cert_life  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_org = cert_org  # type: str
        self.cert_start_time = cert_start_time  # type: str
        self.cert_type = cert_type  # type: str
        self.cert_update_time = cert_update_time  # type: str
        self.domain_cname_status = domain_cname_status  # type: str
        self.domain_name = domain_name  # type: str
        self.server_certificate = server_certificate  # type: str
        self.server_certificate_status = server_certificate_status  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainCertificateInfoResponseBodyCertInfosCertInfo, self).to_map()
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
        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_update_time is not None:
            result['CertUpdateTime'] = self.cert_update_time
        if self.domain_cname_status is not None:
            result['DomainCnameStatus'] = self.domain_cname_status
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.server_certificate is not None:
            result['ServerCertificate'] = self.server_certificate
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
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
        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertUpdateTime') is not None:
            self.cert_update_time = m.get('CertUpdateTime')
        if m.get('DomainCnameStatus') is not None:
            self.domain_cname_status = m.get('DomainCnameStatus')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ServerCertificate') is not None:
            self.server_certificate = m.get('ServerCertificate')
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDomainCertificateInfoResponseBodyCertInfos(TeaModel):
    def __init__(self, cert_info=None):
        self.cert_info = cert_info  # type: list[DescribeDomainCertificateInfoResponseBodyCertInfosCertInfo]

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainCertificateInfoResponseBodyCertInfos, self).to_map()
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
                temp_model = DescribeDomainCertificateInfoResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeDomainCertificateInfoResponseBody(TeaModel):
    def __init__(self, cert_infos=None, request_id=None):
        self.cert_infos = cert_infos  # type: DescribeDomainCertificateInfoResponseBodyCertInfos
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super(DescribeDomainCertificateInfoResponseBody, self).to_map()
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
            temp_model = DescribeDomainCertificateInfoResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainCertificateInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainCertificateInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainCertificateInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainCertificateInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainCustomLogConfigRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainCustomLogConfigRequest, self).to_map()
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


class DescribeDomainCustomLogConfigResponseBody(TeaModel):
    def __init__(self, config_id=None, remark=None, request_id=None, sample=None, tag=None):
        self.config_id = config_id  # type: str
        self.remark = remark  # type: str
        self.request_id = request_id  # type: str
        self.sample = sample  # type: str
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainCustomLogConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DescribeDomainCustomLogConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainCustomLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainCustomLogConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainCustomLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainDetailDataByLayerRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, field=None, isp_name_en=None, layer=None,
                 location_name_en=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.field = field  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.layer = layer  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainDetailDataByLayerRequest, self).to_map()
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
        if self.layer is not None:
            result['Layer'] = self.layer
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
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainDetailDataByLayerResponseBodyDataDataModule(TeaModel):
    def __init__(self, acc=None, bps=None, domain_name=None, http_code=None, ipv_6acc=None, ipv_6bps=None,
                 ipv_6qps=None, ipv_6traf=None, qps=None, time_stamp=None, traf=None):
        self.acc = acc  # type: long
        self.bps = bps  # type: float
        self.domain_name = domain_name  # type: str
        self.http_code = http_code  # type: str
        self.ipv_6acc = ipv_6acc  # type: long
        self.ipv_6bps = ipv_6bps  # type: float
        self.ipv_6qps = ipv_6qps  # type: float
        self.ipv_6traf = ipv_6traf  # type: long
        self.qps = qps  # type: float
        self.time_stamp = time_stamp  # type: str
        self.traf = traf  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainDetailDataByLayerResponseBodyDataDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acc is not None:
            result['Acc'] = self.acc
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.ipv_6acc is not None:
            result['Ipv6Acc'] = self.ipv_6acc
        if self.ipv_6bps is not None:
            result['Ipv6Bps'] = self.ipv_6bps
        if self.ipv_6qps is not None:
            result['Ipv6Qps'] = self.ipv_6qps
        if self.ipv_6traf is not None:
            result['Ipv6Traf'] = self.ipv_6traf
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.traf is not None:
            result['Traf'] = self.traf
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('Ipv6Acc') is not None:
            self.ipv_6acc = m.get('Ipv6Acc')
        if m.get('Ipv6Bps') is not None:
            self.ipv_6bps = m.get('Ipv6Bps')
        if m.get('Ipv6Qps') is not None:
            self.ipv_6qps = m.get('Ipv6Qps')
        if m.get('Ipv6Traf') is not None:
            self.ipv_6traf = m.get('Ipv6Traf')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Traf') is not None:
            self.traf = m.get('Traf')
        return self


class DescribeDomainDetailDataByLayerResponseBodyData(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainDetailDataByLayerResponseBodyDataDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainDetailDataByLayerResponseBodyData, self).to_map()
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
                temp_model = DescribeDomainDetailDataByLayerResponseBodyDataDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainDetailDataByLayerResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeDomainDetailDataByLayerResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDomainDetailDataByLayerResponseBody, self).to_map()
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
            temp_model = DescribeDomainDetailDataByLayerResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainDetailDataByLayerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainDetailDataByLayerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainDetailDataByLayerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainDetailDataByLayerResponseBody()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainFileSizeProportionDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainFileSizeProportionDataResponseBody()
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
    def __init__(self, https_value=None, time_stamp=None, value=None):
        self.https_value = https_value  # type: str
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainHitRateDataResponseBodyHitRateIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainHitRateDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainHttpCodeDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainHttpCodeDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainHttpCodeDataByLayerRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, isp_name_en=None, layer=None,
                 location_name_en=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.layer = layer  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainHttpCodeDataByLayerRequest, self).to_map()
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
        if self.layer is not None:
            result['Layer'] = self.layer
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
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, total_value=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.total_value = total_value  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.total_value is not None:
            result['TotalValue'] = self.total_value
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TotalValue') is not None:
            self.total_value = m.get('TotalValue')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataInterval, self).to_map()
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
                temp_model = DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainHttpCodeDataByLayerResponseBody(TeaModel):
    def __init__(self, data_interval=None, http_code_data_interval=None, request_id=None):
        self.data_interval = data_interval  # type: str
        self.http_code_data_interval = http_code_data_interval  # type: DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataInterval
        self.request_id = request_id  # type: str

    def validate(self):
        if self.http_code_data_interval:
            self.http_code_data_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainHttpCodeDataByLayerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.http_code_data_interval is not None:
            result['HttpCodeDataInterval'] = self.http_code_data_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('HttpCodeDataInterval') is not None:
            temp_model = DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataInterval()
            self.http_code_data_interval = temp_model.from_map(m['HttpCodeDataInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainHttpCodeDataByLayerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainHttpCodeDataByLayerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainHttpCodeDataByLayerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainHttpCodeDataByLayerResponseBody()
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
                 bytes_proportion=None, isp=None, isp_ename=None, proportion=None, qps=None, req_err_rate=None, total_bytes=None,
                 total_query=None):
        self.avg_object_size = avg_object_size  # type: str
        self.avg_response_rate = avg_response_rate  # type: str
        self.avg_response_time = avg_response_time  # type: str
        self.bps = bps  # type: str
        self.bytes_proportion = bytes_proportion  # type: str
        self.isp = isp  # type: str
        self.isp_ename = isp_ename  # type: str
        self.proportion = proportion  # type: str
        self.qps = qps  # type: str
        self.req_err_rate = req_err_rate  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainISPDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainISPDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainMax95BpsDataRequest(TeaModel):
    def __init__(self, cycle=None, domain_name=None, end_time=None, owner_id=None, start_time=None, time_point=None):
        self.cycle = cycle  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.time_point = time_point  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainMax95BpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cycle is not None:
            result['Cycle'] = self.cycle
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_point is not None:
            result['TimePoint'] = self.time_point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cycle') is not None:
            self.cycle = m.get('Cycle')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')
        return self


class DescribeDomainMax95BpsDataResponseBody(TeaModel):
    def __init__(self, domain_name=None, domestic_max_95bps=None, end_time=None, max_95bps=None,
                 overseas_max_95bps=None, request_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.domestic_max_95bps = domestic_max_95bps  # type: str
        self.end_time = end_time  # type: str
        self.max_95bps = max_95bps  # type: str
        self.overseas_max_95bps = overseas_max_95bps  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainMax95BpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domestic_max_95bps is not None:
            result['DomesticMax95Bps'] = self.domestic_max_95bps
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_95bps is not None:
            result['Max95Bps'] = self.max_95bps
        if self.overseas_max_95bps is not None:
            result['OverseasMax95Bps'] = self.overseas_max_95bps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomesticMax95Bps') is not None:
            self.domestic_max_95bps = m.get('DomesticMax95Bps')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Max95Bps') is not None:
            self.max_95bps = m.get('Max95Bps')
        if m.get('OverseasMax95Bps') is not None:
            self.overseas_max_95bps = m.get('OverseasMax95Bps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainMax95BpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainMax95BpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainMax95BpsDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainMax95BpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainMultiUsageDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainMultiUsageDataRequest, self).to_map()
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


class DescribeDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule(TeaModel):
    def __init__(self, domain=None, request=None, time_stamp=None, type=None):
        self.domain = domain  # type: str
        self.request = request  # type: long
        self.time_stamp = time_stamp  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule, self).to_map()
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


class DescribeDomainMultiUsageDataResponseBodyRequestPerInterval(TeaModel):
    def __init__(self, request_data_module=None):
        self.request_data_module = request_data_module  # type: list[DescribeDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule]

    def validate(self):
        if self.request_data_module:
            for k in self.request_data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainMultiUsageDataResponseBodyRequestPerInterval, self).to_map()
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
                temp_model = DescribeDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule()
                self.request_data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule(TeaModel):
    def __init__(self, area=None, bps=None, domain=None, time_stamp=None, type=None):
        self.area = area  # type: str
        self.bps = bps  # type: float
        self.domain = domain  # type: str
        self.time_stamp = time_stamp  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule, self).to_map()
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


class DescribeDomainMultiUsageDataResponseBodyTrafficPerInterval(TeaModel):
    def __init__(self, traffic_data_module=None):
        self.traffic_data_module = traffic_data_module  # type: list[DescribeDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule]

    def validate(self):
        if self.traffic_data_module:
            for k in self.traffic_data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainMultiUsageDataResponseBodyTrafficPerInterval, self).to_map()
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
                temp_model = DescribeDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule()
                self.traffic_data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainMultiUsageDataResponseBody(TeaModel):
    def __init__(self, end_time=None, request_id=None, request_per_interval=None, start_time=None,
                 traffic_per_interval=None):
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.request_per_interval = request_per_interval  # type: DescribeDomainMultiUsageDataResponseBodyRequestPerInterval
        self.start_time = start_time  # type: str
        self.traffic_per_interval = traffic_per_interval  # type: DescribeDomainMultiUsageDataResponseBodyTrafficPerInterval

    def validate(self):
        if self.request_per_interval:
            self.request_per_interval.validate()
        if self.traffic_per_interval:
            self.traffic_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainMultiUsageDataResponseBody, self).to_map()
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
            temp_model = DescribeDomainMultiUsageDataResponseBodyRequestPerInterval()
            self.request_per_interval = temp_model.from_map(m['RequestPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TrafficPerInterval') is not None:
            temp_model = DescribeDomainMultiUsageDataResponseBodyTrafficPerInterval()
            self.traffic_per_interval = temp_model.from_map(m['TrafficPerInterval'])
        return self


class DescribeDomainMultiUsageDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainMultiUsageDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainMultiUsageDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainMultiUsageDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainNamesOfVersionRequest(TeaModel):
    def __init__(self, owner_id=None, page_index=None, page_size=None, version_id=None):
        self.owner_id = owner_id  # type: long
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: str
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainNamesOfVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DescribeDomainNamesOfVersionResponseBodyContents(TeaModel):
    def __init__(self, domain_id=None, domain_name=None):
        self.domain_id = domain_id  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainNamesOfVersionResponseBodyContents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeDomainNamesOfVersionResponseBody(TeaModel):
    def __init__(self, contents=None, request_id=None, total_count=None):
        self.contents = contents  # type: list[DescribeDomainNamesOfVersionResponseBodyContents]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.contents:
            for k in self.contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainNamesOfVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Contents'] = []
        if self.contents is not None:
            for k in self.contents:
                result['Contents'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.contents = []
        if m.get('Contents') is not None:
            for k in m.get('Contents'):
                temp_model = DescribeDomainNamesOfVersionResponseBodyContents()
                self.contents.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDomainNamesOfVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainNamesOfVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainNamesOfVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainNamesOfVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainPathDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, page_number=None, page_size=None, path=None,
                 start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.path = path  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainPathDataRequest, self).to_map()
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
        if self.path is not None:
            result['Path'] = self.path
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
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainPathDataResponseBodyPathDataPerIntervalUsageData(TeaModel):
    def __init__(self, acc=None, path=None, time=None, traffic=None):
        self.acc = acc  # type: int
        self.path = path  # type: str
        self.time = time  # type: str
        self.traffic = traffic  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainPathDataResponseBodyPathDataPerIntervalUsageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acc is not None:
            result['Acc'] = self.acc
        if self.path is not None:
            result['Path'] = self.path
        if self.time is not None:
            result['Time'] = self.time
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        return self


class DescribeDomainPathDataResponseBodyPathDataPerInterval(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data  # type: list[DescribeDomainPathDataResponseBodyPathDataPerIntervalUsageData]

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainPathDataResponseBodyPathDataPerInterval, self).to_map()
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
                temp_model = DescribeDomainPathDataResponseBodyPathDataPerIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainPathDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, page_number=None, page_size=None,
                 path_data_per_interval=None, start_time=None, total_count=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.path_data_per_interval = path_data_per_interval  # type: DescribeDomainPathDataResponseBodyPathDataPerInterval
        self.start_time = start_time  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.path_data_per_interval:
            self.path_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainPathDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.path_data_per_interval is not None:
            result['PathDataPerInterval'] = self.path_data_per_interval.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PathDataPerInterval') is not None:
            temp_model = DescribeDomainPathDataResponseBodyPathDataPerInterval()
            self.path_data_per_interval = temp_model.from_map(m['PathDataPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDomainPathDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainPathDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainPathDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainPathDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainPvDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainPvDataRequest, self).to_map()
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


class DescribeDomainPvDataResponseBodyPvDataIntervalUsageData(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainPvDataResponseBodyPvDataIntervalUsageData, self).to_map()
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


class DescribeDomainPvDataResponseBodyPvDataInterval(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data  # type: list[DescribeDomainPvDataResponseBodyPvDataIntervalUsageData]

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainPvDataResponseBodyPvDataInterval, self).to_map()
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
                temp_model = DescribeDomainPvDataResponseBodyPvDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainPvDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, pv_data_interval=None, request_id=None,
                 start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.pv_data_interval = pv_data_interval  # type: DescribeDomainPvDataResponseBodyPvDataInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.pv_data_interval:
            self.pv_data_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainPvDataResponseBody, self).to_map()
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
            temp_model = DescribeDomainPvDataResponseBodyPvDataInterval()
            self.pv_data_interval = temp_model.from_map(m['PvDataInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainPvDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainPvDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainPvDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainPvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainQpsDataRequest(TeaModel):
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
        _map = super(DescribeDomainQpsDataRequest, self).to_map()
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


class DescribeDomainQpsDataResponseBodyQpsDataIntervalDataModule(TeaModel):
    def __init__(self, acc_domestic_value=None, acc_overseas_value=None, acc_value=None, domestic_value=None,
                 https_acc_domestic_value=None, https_acc_overseas_value=None, https_acc_value=None, https_domestic_value=None,
                 https_overseas_value=None, https_value=None, overseas_value=None, time_stamp=None, value=None):
        self.acc_domestic_value = acc_domestic_value  # type: str
        self.acc_overseas_value = acc_overseas_value  # type: str
        self.acc_value = acc_value  # type: str
        self.domestic_value = domestic_value  # type: str
        self.https_acc_domestic_value = https_acc_domestic_value  # type: str
        self.https_acc_overseas_value = https_acc_overseas_value  # type: str
        self.https_acc_value = https_acc_value  # type: str
        self.https_domestic_value = https_domestic_value  # type: str
        self.https_overseas_value = https_overseas_value  # type: str
        self.https_value = https_value  # type: str
        self.overseas_value = overseas_value  # type: str
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
        if self.https_acc_domestic_value is not None:
            result['HttpsAccDomesticValue'] = self.https_acc_domestic_value
        if self.https_acc_overseas_value is not None:
            result['HttpsAccOverseasValue'] = self.https_acc_overseas_value
        if self.https_acc_value is not None:
            result['HttpsAccValue'] = self.https_acc_value
        if self.https_domestic_value is not None:
            result['HttpsDomesticValue'] = self.https_domestic_value
        if self.https_overseas_value is not None:
            result['HttpsOverseasValue'] = self.https_overseas_value
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
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
        if m.get('HttpsAccDomesticValue') is not None:
            self.https_acc_domestic_value = m.get('HttpsAccDomesticValue')
        if m.get('HttpsAccOverseasValue') is not None:
            self.https_acc_overseas_value = m.get('HttpsAccOverseasValue')
        if m.get('HttpsAccValue') is not None:
            self.https_acc_value = m.get('HttpsAccValue')
        if m.get('HttpsDomesticValue') is not None:
            self.https_domestic_value = m.get('HttpsDomesticValue')
        if m.get('HttpsOverseasValue') is not None:
            self.https_overseas_value = m.get('HttpsOverseasValue')
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainQpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainQpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainQpsDataByLayerRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, isp_name_en=None, layer=None,
                 location_name_en=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.layer = layer  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainQpsDataByLayerRequest, self).to_map()
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
        if self.layer is not None:
            result['Layer'] = self.layer
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
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainQpsDataByLayerResponseBodyQpsDataIntervalDataModule(TeaModel):
    def __init__(self, acc_domestic_value=None, acc_overseas_value=None, acc_value=None, domestic_value=None,
                 overseas_value=None, time_stamp=None, value=None):
        self.acc_domestic_value = acc_domestic_value  # type: str
        self.acc_overseas_value = acc_overseas_value  # type: str
        self.acc_value = acc_value  # type: str
        self.domestic_value = domestic_value  # type: str
        self.overseas_value = overseas_value  # type: str
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainQpsDataByLayerResponseBodyQpsDataIntervalDataModule, self).to_map()
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
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
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
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainQpsDataByLayerResponseBodyQpsDataInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainQpsDataByLayerResponseBodyQpsDataIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainQpsDataByLayerResponseBodyQpsDataInterval, self).to_map()
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
                temp_model = DescribeDomainQpsDataByLayerResponseBodyQpsDataIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainQpsDataByLayerResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, layer=None, qps_data_interval=None,
                 request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.layer = layer  # type: str
        self.qps_data_interval = qps_data_interval  # type: DescribeDomainQpsDataByLayerResponseBodyQpsDataInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.qps_data_interval:
            self.qps_data_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainQpsDataByLayerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.layer is not None:
            result['Layer'] = self.layer
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
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('QpsDataInterval') is not None:
            temp_model = DescribeDomainQpsDataByLayerResponseBodyQpsDataInterval()
            self.qps_data_interval = temp_model.from_map(m['QpsDataInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainQpsDataByLayerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainQpsDataByLayerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainQpsDataByLayerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainQpsDataByLayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeBpsDataRequest(TeaModel):
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
        _map = super(DescribeDomainRealTimeBpsDataRequest, self).to_map()
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


class DescribeDomainRealTimeBpsDataResponseBodyDataBpsModel(TeaModel):
    def __init__(self, bps=None, time_stamp=None):
        self.bps = bps  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRealTimeBpsDataResponseBodyDataBpsModel, self).to_map()
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


class DescribeDomainRealTimeBpsDataResponseBodyData(TeaModel):
    def __init__(self, bps_model=None):
        self.bps_model = bps_model  # type: list[DescribeDomainRealTimeBpsDataResponseBodyDataBpsModel]

    def validate(self):
        if self.bps_model:
            for k in self.bps_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeBpsDataResponseBodyData, self).to_map()
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
                temp_model = DescribeDomainRealTimeBpsDataResponseBodyDataBpsModel()
                self.bps_model.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeBpsDataResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeDomainRealTimeBpsDataResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeBpsDataResponseBody, self).to_map()
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
            temp_model = DescribeDomainRealTimeBpsDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainRealTimeBpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainRealTimeBpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeBpsDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeByteHitRateDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRealTimeByteHitRateDataRequest, self).to_map()
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


class DescribeDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel(TeaModel):
    def __init__(self, byte_hit_rate=None, time_stamp=None):
        self.byte_hit_rate = byte_hit_rate  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel, self).to_map()
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


class DescribeDomainRealTimeByteHitRateDataResponseBodyData(TeaModel):
    def __init__(self, byte_hit_rate_data_model=None):
        self.byte_hit_rate_data_model = byte_hit_rate_data_model  # type: list[DescribeDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel]

    def validate(self):
        if self.byte_hit_rate_data_model:
            for k in self.byte_hit_rate_data_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeByteHitRateDataResponseBodyData, self).to_map()
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
                temp_model = DescribeDomainRealTimeByteHitRateDataResponseBodyDataByteHitRateDataModel()
                self.byte_hit_rate_data_model.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeByteHitRateDataResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeDomainRealTimeByteHitRateDataResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeByteHitRateDataResponseBody, self).to_map()
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
            temp_model = DescribeDomainRealTimeByteHitRateDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainRealTimeByteHitRateDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainRealTimeByteHitRateDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeByteHitRateDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeByteHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeDetailDataRequest(TeaModel):
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
        _map = super(DescribeDomainRealTimeDetailDataRequest, self).to_map()
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


class DescribeDomainRealTimeDetailDataResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRealTimeDetailDataResponseBody, self).to_map()
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


class DescribeDomainRealTimeDetailDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainRealTimeDetailDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeDetailDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeDetailDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeHttpCodeDataRequest(TeaModel):
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
        _map = super(DescribeDomainRealTimeHttpCodeDataRequest, self).to_map()
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


class DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData(TeaModel):
    def __init__(self, code=None, count=None, proportion=None):
        self.code = code  # type: str
        self.count = count  # type: str
        self.proportion = proportion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData, self).to_map()
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


class DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue(TeaModel):
    def __init__(self, real_time_code_proportion_data=None):
        self.real_time_code_proportion_data = real_time_code_proportion_data  # type: list[DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData]

    def validate(self):
        if self.real_time_code_proportion_data:
            for k in self.real_time_code_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue, self).to_map()
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
                temp_model = DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData()
                self.real_time_code_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData, self).to_map()
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
            temp_model = DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data  # type: list[DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData]

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData, self).to_map()
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
                temp_model = DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeHttpCodeDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, real_time_http_code_data=None,
                 request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.real_time_http_code_data = real_time_http_code_data  # type: DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.real_time_http_code_data:
            self.real_time_http_code_data.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeHttpCodeDataResponseBody, self).to_map()
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
            temp_model = DescribeDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData()
            self.real_time_http_code_data = temp_model.from_map(m['RealTimeHttpCodeData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeHttpCodeDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainRealTimeHttpCodeDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeHttpCodeDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeQpsDataRequest(TeaModel):
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
        _map = super(DescribeDomainRealTimeQpsDataRequest, self).to_map()
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


class DescribeDomainRealTimeQpsDataResponseBodyDataQpsModel(TeaModel):
    def __init__(self, qps=None, time_stamp=None):
        self.qps = qps  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRealTimeQpsDataResponseBodyDataQpsModel, self).to_map()
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


class DescribeDomainRealTimeQpsDataResponseBodyData(TeaModel):
    def __init__(self, qps_model=None):
        self.qps_model = qps_model  # type: list[DescribeDomainRealTimeQpsDataResponseBodyDataQpsModel]

    def validate(self):
        if self.qps_model:
            for k in self.qps_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeQpsDataResponseBodyData, self).to_map()
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
                temp_model = DescribeDomainRealTimeQpsDataResponseBodyDataQpsModel()
                self.qps_model.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeQpsDataResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeDomainRealTimeQpsDataResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeQpsDataResponseBody, self).to_map()
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
            temp_model = DescribeDomainRealTimeQpsDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainRealTimeQpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainRealTimeQpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeQpsDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeQpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeReqHitRateDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRealTimeReqHitRateDataRequest, self).to_map()
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


class DescribeDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel(TeaModel):
    def __init__(self, req_hit_rate=None, time_stamp=None):
        self.req_hit_rate = req_hit_rate  # type: float
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel, self).to_map()
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


class DescribeDomainRealTimeReqHitRateDataResponseBodyData(TeaModel):
    def __init__(self, req_hit_rate_data_model=None):
        self.req_hit_rate_data_model = req_hit_rate_data_model  # type: list[DescribeDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel]

    def validate(self):
        if self.req_hit_rate_data_model:
            for k in self.req_hit_rate_data_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeReqHitRateDataResponseBodyData, self).to_map()
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
                temp_model = DescribeDomainRealTimeReqHitRateDataResponseBodyDataReqHitRateDataModel()
                self.req_hit_rate_data_model.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeReqHitRateDataResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: DescribeDomainRealTimeReqHitRateDataResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeReqHitRateDataResponseBody, self).to_map()
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
            temp_model = DescribeDomainRealTimeReqHitRateDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainRealTimeReqHitRateDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainRealTimeReqHitRateDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeReqHitRateDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeReqHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeSrcBpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRealTimeSrcBpsDataRequest, self).to_map()
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


class DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule, self).to_map()
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


class DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval, self).to_map()
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
                temp_model = DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeSrcBpsDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None,
                 real_time_src_bps_data_per_interval=None, request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.real_time_src_bps_data_per_interval = real_time_src_bps_data_per_interval  # type: DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.real_time_src_bps_data_per_interval:
            self.real_time_src_bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeSrcBpsDataResponseBody, self).to_map()
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
            temp_model = DescribeDomainRealTimeSrcBpsDataResponseBodyRealTimeSrcBpsDataPerInterval()
            self.real_time_src_bps_data_per_interval = temp_model.from_map(m['RealTimeSrcBpsDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeSrcBpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainRealTimeSrcBpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeSrcBpsDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeSrcBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeSrcHttpCodeDataRequest(TeaModel):
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
        _map = super(DescribeDomainRealTimeSrcHttpCodeDataRequest, self).to_map()
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


class DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData(TeaModel):
    def __init__(self, code=None, count=None, proportion=None):
        self.code = code  # type: str
        self.count = count  # type: str
        self.proportion = proportion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData, self).to_map()
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


class DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValue(TeaModel):
    def __init__(self, real_time_src_code_proportion_data=None):
        self.real_time_src_code_proportion_data = real_time_src_code_proportion_data  # type: list[DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData]

    def validate(self):
        if self.real_time_src_code_proportion_data:
            for k in self.real_time_src_code_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValue, self).to_map()
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
                temp_model = DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValueRealTimeSrcCodeProportionData()
                self.real_time_src_code_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageData(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValue

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageData, self).to_map()
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
            temp_model = DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data  # type: list[DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageData]

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData, self).to_map()
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
                temp_model = DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeSrcHttpCodeDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, real_time_src_http_code_data=None,
                 request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.real_time_src_http_code_data = real_time_src_http_code_data  # type: DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.real_time_src_http_code_data:
            self.real_time_src_http_code_data.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeSrcHttpCodeDataResponseBody, self).to_map()
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
            temp_model = DescribeDomainRealTimeSrcHttpCodeDataResponseBodyRealTimeSrcHttpCodeData()
            self.real_time_src_http_code_data = temp_model.from_map(m['RealTimeSrcHttpCodeData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeSrcHttpCodeDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainRealTimeSrcHttpCodeDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeSrcHttpCodeDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeSrcHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeSrcTrafficDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRealTimeSrcTrafficDataRequest, self).to_map()
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


class DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule, self).to_map()
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


class DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval, self).to_map()
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
                temp_model = DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeSrcTrafficDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None,
                 real_time_src_traffic_data_per_interval=None, request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.real_time_src_traffic_data_per_interval = real_time_src_traffic_data_per_interval  # type: DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.real_time_src_traffic_data_per_interval:
            self.real_time_src_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeSrcTrafficDataResponseBody, self).to_map()
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
            temp_model = DescribeDomainRealTimeSrcTrafficDataResponseBodyRealTimeSrcTrafficDataPerInterval()
            self.real_time_src_traffic_data_per_interval = temp_model.from_map(m['RealTimeSrcTrafficDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeSrcTrafficDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainRealTimeSrcTrafficDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeSrcTrafficDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeSrcTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealTimeTrafficDataRequest(TeaModel):
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
        _map = super(DescribeDomainRealTimeTrafficDataRequest, self).to_map()
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


class DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule, self).to_map()
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


class DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval, self).to_map()
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
                temp_model = DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainRealTimeTrafficDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None,
                 real_time_traffic_data_per_interval=None, request_id=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.real_time_traffic_data_per_interval = real_time_traffic_data_per_interval  # type: DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.real_time_traffic_data_per_interval:
            self.real_time_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeTrafficDataResponseBody, self).to_map()
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
            temp_model = DescribeDomainRealTimeTrafficDataResponseBodyRealTimeTrafficDataPerInterval()
            self.real_time_traffic_data_per_interval = temp_model.from_map(m['RealTimeTrafficDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainRealTimeTrafficDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainRealTimeTrafficDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainRealTimeTrafficDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealTimeTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRealtimeLogDeliveryRequest(TeaModel):
    def __init__(self, domain=None, owner_id=None):
        self.domain = domain  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRealtimeLogDeliveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDomainRealtimeLogDeliveryResponseBody(TeaModel):
    def __init__(self, logstore=None, project=None, region=None, request_id=None, status=None):
        self.logstore = logstore  # type: str
        self.project = project  # type: str
        self.region = region  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRealtimeLogDeliveryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDomainRealtimeLogDeliveryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainRealtimeLogDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainRealtimeLogDeliveryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainRealtimeLogDeliveryResponseBody()
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
                 bytes_proportion=None, proportion=None, qps=None, region=None, region_ename=None, req_err_rate=None,
                 total_bytes=None, total_query=None):
        self.avg_object_size = avg_object_size  # type: str
        self.avg_response_rate = avg_response_rate  # type: str
        self.avg_response_time = avg_response_time  # type: str
        self.bps = bps  # type: str
        self.bytes_proportion = bytes_proportion  # type: str
        self.proportion = proportion  # type: str
        self.qps = qps  # type: str
        self.region = region  # type: str
        self.region_ename = region_ename  # type: str
        self.req_err_rate = req_err_rate  # type: str
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
        if m.get('ReqErrRate') is not None:
            self.req_err_rate = m.get('ReqErrRate')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainRegionDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    def __init__(self, https_value=None, time_stamp=None, value=None):
        self.https_value = https_value  # type: str
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainReqHitRateDataResponseBodyReqHitRateIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainReqHitRateDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainReqHitRateDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSrcBpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

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


class DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, https_value=None, time_stamp=None, value=None):
        self.https_value = https_value  # type: str
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSrcBpsDataResponseBodySrcBpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainSrcBpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainSrcBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSrcHttpCodeDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSrcHttpCodeDataRequest, self).to_map()
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


class DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData(TeaModel):
    def __init__(self, code=None, count=None, proportion=None):
        self.code = code  # type: str
        self.count = count  # type: str
        self.proportion = proportion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData, self).to_map()
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


class DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValue(TeaModel):
    def __init__(self, code_proportion_data=None):
        self.code_proportion_data = code_proportion_data  # type: list[DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData]

    def validate(self):
        if self.code_proportion_data:
            for k in self.code_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValue, self).to_map()
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
                temp_model = DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData()
                self.code_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageData(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValue

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageData, self).to_map()
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
            temp_model = DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeData(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data  # type: list[DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageData]

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeData, self).to_map()
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
                temp_model = DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcHttpCodeDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, http_code_data=None, request_id=None,
                 start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.http_code_data = http_code_data  # type: DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeData
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.http_code_data:
            self.http_code_data.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcHttpCodeDataResponseBody, self).to_map()
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
            temp_model = DescribeDomainSrcHttpCodeDataResponseBodyHttpCodeData()
            self.http_code_data = temp_model.from_map(m['HttpCodeData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainSrcHttpCodeDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainSrcHttpCodeDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcHttpCodeDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainSrcHttpCodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSrcQpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSrcQpsDataRequest, self).to_map()
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


class DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerIntervalDataModule, self).to_map()
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


class DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerInterval, self).to_map()
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
                temp_model = DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcQpsDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None,
                 src_qps_data_per_interval=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.src_qps_data_per_interval = src_qps_data_per_interval  # type: DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerInterval
        self.start_time = start_time  # type: str

    def validate(self):
        if self.src_qps_data_per_interval:
            self.src_qps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcQpsDataResponseBody, self).to_map()
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
        if self.src_qps_data_per_interval is not None:
            result['SrcQpsDataPerInterval'] = self.src_qps_data_per_interval.to_map()
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
        if m.get('SrcQpsDataPerInterval') is not None:
            temp_model = DescribeDomainSrcQpsDataResponseBodySrcQpsDataPerInterval()
            self.src_qps_data_per_interval = temp_model.from_map(m['SrcQpsDataPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainSrcQpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainSrcQpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcQpsDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainSrcQpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSrcTopUrlVisitRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, sort_by=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.sort_by = sort_by  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSrcTopUrlVisitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
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
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyAllUrlListUrlList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, url_detail=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.url_detail = url_detail  # type: str
        self.visit_data = visit_data  # type: str
        self.visit_proportion = visit_proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSrcTopUrlVisitResponseBodyAllUrlListUrlList, self).to_map()
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


class DescribeDomainSrcTopUrlVisitResponseBodyAllUrlList(TeaModel):
    def __init__(self, url_list=None):
        self.url_list = url_list  # type: list[DescribeDomainSrcTopUrlVisitResponseBodyAllUrlListUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcTopUrlVisitResponseBodyAllUrlList, self).to_map()
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
                temp_model = DescribeDomainSrcTopUrlVisitResponseBodyAllUrlListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl200ListUrlList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, url_detail=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.url_detail = url_detail  # type: str
        self.visit_data = visit_data  # type: str
        self.visit_proportion = visit_proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSrcTopUrlVisitResponseBodyUrl200ListUrlList, self).to_map()
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


class DescribeDomainSrcTopUrlVisitResponseBodyUrl200List(TeaModel):
    def __init__(self, url_list=None):
        self.url_list = url_list  # type: list[DescribeDomainSrcTopUrlVisitResponseBodyUrl200ListUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcTopUrlVisitResponseBodyUrl200List, self).to_map()
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
                temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl200ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl300ListUrlList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, url_detail=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.url_detail = url_detail  # type: str
        self.visit_data = visit_data  # type: str
        self.visit_proportion = visit_proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSrcTopUrlVisitResponseBodyUrl300ListUrlList, self).to_map()
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


class DescribeDomainSrcTopUrlVisitResponseBodyUrl300List(TeaModel):
    def __init__(self, url_list=None):
        self.url_list = url_list  # type: list[DescribeDomainSrcTopUrlVisitResponseBodyUrl300ListUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcTopUrlVisitResponseBodyUrl300List, self).to_map()
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
                temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl300ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl400ListUrlList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, url_detail=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.url_detail = url_detail  # type: str
        self.visit_data = visit_data  # type: str
        self.visit_proportion = visit_proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSrcTopUrlVisitResponseBodyUrl400ListUrlList, self).to_map()
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


class DescribeDomainSrcTopUrlVisitResponseBodyUrl400List(TeaModel):
    def __init__(self, url_list=None):
        self.url_list = url_list  # type: list[DescribeDomainSrcTopUrlVisitResponseBodyUrl400ListUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcTopUrlVisitResponseBodyUrl400List, self).to_map()
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
                temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl400ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTopUrlVisitResponseBodyUrl500ListUrlList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, url_detail=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.url_detail = url_detail  # type: str
        self.visit_data = visit_data  # type: str
        self.visit_proportion = visit_proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSrcTopUrlVisitResponseBodyUrl500ListUrlList, self).to_map()
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


class DescribeDomainSrcTopUrlVisitResponseBodyUrl500List(TeaModel):
    def __init__(self, url_list=None):
        self.url_list = url_list  # type: list[DescribeDomainSrcTopUrlVisitResponseBodyUrl500ListUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcTopUrlVisitResponseBodyUrl500List, self).to_map()
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
                temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl500ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTopUrlVisitResponseBody(TeaModel):
    def __init__(self, all_url_list=None, domain_name=None, request_id=None, start_time=None, url_200list=None,
                 url_300list=None, url_400list=None, url_500list=None):
        self.all_url_list = all_url_list  # type: DescribeDomainSrcTopUrlVisitResponseBodyAllUrlList
        self.domain_name = domain_name  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.url_200list = url_200list  # type: DescribeDomainSrcTopUrlVisitResponseBodyUrl200List
        self.url_300list = url_300list  # type: DescribeDomainSrcTopUrlVisitResponseBodyUrl300List
        self.url_400list = url_400list  # type: DescribeDomainSrcTopUrlVisitResponseBodyUrl400List
        self.url_500list = url_500list  # type: DescribeDomainSrcTopUrlVisitResponseBodyUrl500List

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
        _map = super(DescribeDomainSrcTopUrlVisitResponseBody, self).to_map()
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
            temp_model = DescribeDomainSrcTopUrlVisitResponseBodyAllUrlList()
            self.all_url_list = temp_model.from_map(m['AllUrlList'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Url200List') is not None:
            temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl200List()
            self.url_200list = temp_model.from_map(m['Url200List'])
        if m.get('Url300List') is not None:
            temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl300List()
            self.url_300list = temp_model.from_map(m['Url300List'])
        if m.get('Url400List') is not None:
            temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl400List()
            self.url_400list = temp_model.from_map(m['Url400List'])
        if m.get('Url500List') is not None:
            temp_model = DescribeDomainSrcTopUrlVisitResponseBodyUrl500List()
            self.url_500list = temp_model.from_map(m['Url500List'])
        return self


class DescribeDomainSrcTopUrlVisitResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainSrcTopUrlVisitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcTopUrlVisitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainSrcTopUrlVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSrcTrafficDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSrcTrafficDataRequest, self).to_map()
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


class DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, https_value=None, time_stamp=None, value=None):
        self.https_value = https_value  # type: str
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerInterval, self).to_map()
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
                temp_model = DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainSrcTrafficDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None,
                 src_traffic_data_per_interval=None, start_time=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.src_traffic_data_per_interval = src_traffic_data_per_interval  # type: DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerInterval
        self.start_time = start_time  # type: str

    def validate(self):
        if self.src_traffic_data_per_interval:
            self.src_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcTrafficDataResponseBody, self).to_map()
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
        if self.src_traffic_data_per_interval is not None:
            result['SrcTrafficDataPerInterval'] = self.src_traffic_data_per_interval.to_map()
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
        if m.get('SrcTrafficDataPerInterval') is not None:
            temp_model = DescribeDomainSrcTrafficDataResponseBodySrcTrafficDataPerInterval()
            self.src_traffic_data_per_interval = temp_model.from_map(m['SrcTrafficDataPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainSrcTrafficDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainSrcTrafficDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainSrcTrafficDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainSrcTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainTopClientIpVisitRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, limit=None, location_name_en=None, owner_id=None,
                 sort_by=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.limit = limit  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.sort_by = sort_by  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainTopClientIpVisitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
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
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainTopClientIpVisitResponseBodyClientIpList(TeaModel):
    def __init__(self, acc=None, client_ip=None, rank=None, traffic=None):
        self.acc = acc  # type: long
        self.client_ip = client_ip  # type: str
        self.rank = rank  # type: int
        self.traffic = traffic  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainTopClientIpVisitResponseBodyClientIpList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acc is not None:
            result['Acc'] = self.acc
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        return self


class DescribeDomainTopClientIpVisitResponseBody(TeaModel):
    def __init__(self, client_ip_list=None, request_id=None):
        self.client_ip_list = client_ip_list  # type: list[DescribeDomainTopClientIpVisitResponseBodyClientIpList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.client_ip_list:
            for k in self.client_ip_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainTopClientIpVisitResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClientIpList'] = []
        if self.client_ip_list is not None:
            for k in self.client_ip_list:
                result['ClientIpList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.client_ip_list = []
        if m.get('ClientIpList') is not None:
            for k in m.get('ClientIpList'):
                temp_model = DescribeDomainTopClientIpVisitResponseBodyClientIpList()
                self.client_ip_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainTopClientIpVisitResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainTopClientIpVisitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainTopClientIpVisitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainTopClientIpVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainTopReferVisitRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, percent=None, sort_by=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.percent = percent  # type: str
        self.sort_by = sort_by  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainTopReferVisitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
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
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainTopReferVisitResponseBodyTopReferListReferList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, refer_detail=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.refer_detail = refer_detail  # type: str
        self.visit_data = visit_data  # type: str
        self.visit_proportion = visit_proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainTopReferVisitResponseBodyTopReferListReferList, self).to_map()
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


class DescribeDomainTopReferVisitResponseBodyTopReferList(TeaModel):
    def __init__(self, refer_list=None):
        self.refer_list = refer_list  # type: list[DescribeDomainTopReferVisitResponseBodyTopReferListReferList]

    def validate(self):
        if self.refer_list:
            for k in self.refer_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainTopReferVisitResponseBodyTopReferList, self).to_map()
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
                temp_model = DescribeDomainTopReferVisitResponseBodyTopReferListReferList()
                self.refer_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopReferVisitResponseBody(TeaModel):
    def __init__(self, domain_name=None, request_id=None, start_time=None, top_refer_list=None):
        self.domain_name = domain_name  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.top_refer_list = top_refer_list  # type: DescribeDomainTopReferVisitResponseBodyTopReferList

    def validate(self):
        if self.top_refer_list:
            self.top_refer_list.validate()

    def to_map(self):
        _map = super(DescribeDomainTopReferVisitResponseBody, self).to_map()
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
            temp_model = DescribeDomainTopReferVisitResponseBodyTopReferList()
            self.top_refer_list = temp_model.from_map(m['TopReferList'])
        return self


class DescribeDomainTopReferVisitResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainTopReferVisitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainTopReferVisitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainTopReferVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainTopUrlVisitRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, sort_by=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.sort_by = sort_by  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainTopUrlVisitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
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
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainTopUrlVisitResponseBodyAllUrlListUrlList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, url_detail=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.url_detail = url_detail  # type: str
        self.visit_data = visit_data  # type: str
        self.visit_proportion = visit_proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainTopUrlVisitResponseBodyAllUrlListUrlList, self).to_map()
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


class DescribeDomainTopUrlVisitResponseBodyAllUrlList(TeaModel):
    def __init__(self, url_list=None):
        self.url_list = url_list  # type: list[DescribeDomainTopUrlVisitResponseBodyAllUrlListUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainTopUrlVisitResponseBodyAllUrlList, self).to_map()
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
                temp_model = DescribeDomainTopUrlVisitResponseBodyAllUrlListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl200ListUrlList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, url_detail=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.url_detail = url_detail  # type: str
        self.visit_data = visit_data  # type: str
        self.visit_proportion = visit_proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainTopUrlVisitResponseBodyUrl200ListUrlList, self).to_map()
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


class DescribeDomainTopUrlVisitResponseBodyUrl200List(TeaModel):
    def __init__(self, url_list=None):
        self.url_list = url_list  # type: list[DescribeDomainTopUrlVisitResponseBodyUrl200ListUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainTopUrlVisitResponseBodyUrl200List, self).to_map()
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
                temp_model = DescribeDomainTopUrlVisitResponseBodyUrl200ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl300ListUrlList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, url_detail=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.url_detail = url_detail  # type: str
        self.visit_data = visit_data  # type: str
        self.visit_proportion = visit_proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainTopUrlVisitResponseBodyUrl300ListUrlList, self).to_map()
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


class DescribeDomainTopUrlVisitResponseBodyUrl300List(TeaModel):
    def __init__(self, url_list=None):
        self.url_list = url_list  # type: list[DescribeDomainTopUrlVisitResponseBodyUrl300ListUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainTopUrlVisitResponseBodyUrl300List, self).to_map()
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
                temp_model = DescribeDomainTopUrlVisitResponseBodyUrl300ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl400ListUrlList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, url_detail=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.url_detail = url_detail  # type: str
        self.visit_data = visit_data  # type: str
        self.visit_proportion = visit_proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainTopUrlVisitResponseBodyUrl400ListUrlList, self).to_map()
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


class DescribeDomainTopUrlVisitResponseBodyUrl400List(TeaModel):
    def __init__(self, url_list=None):
        self.url_list = url_list  # type: list[DescribeDomainTopUrlVisitResponseBodyUrl400ListUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainTopUrlVisitResponseBodyUrl400List, self).to_map()
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
                temp_model = DescribeDomainTopUrlVisitResponseBodyUrl400ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopUrlVisitResponseBodyUrl500ListUrlList(TeaModel):
    def __init__(self, flow=None, flow_proportion=None, url_detail=None, visit_data=None, visit_proportion=None):
        self.flow = flow  # type: str
        self.flow_proportion = flow_proportion  # type: float
        self.url_detail = url_detail  # type: str
        self.visit_data = visit_data  # type: str
        self.visit_proportion = visit_proportion  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainTopUrlVisitResponseBodyUrl500ListUrlList, self).to_map()
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


class DescribeDomainTopUrlVisitResponseBodyUrl500List(TeaModel):
    def __init__(self, url_list=None):
        self.url_list = url_list  # type: list[DescribeDomainTopUrlVisitResponseBodyUrl500ListUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainTopUrlVisitResponseBodyUrl500List, self).to_map()
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
                temp_model = DescribeDomainTopUrlVisitResponseBodyUrl500ListUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainTopUrlVisitResponseBody(TeaModel):
    def __init__(self, all_url_list=None, domain_name=None, request_id=None, start_time=None, url_200list=None,
                 url_300list=None, url_400list=None, url_500list=None):
        self.all_url_list = all_url_list  # type: DescribeDomainTopUrlVisitResponseBodyAllUrlList
        self.domain_name = domain_name  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.url_200list = url_200list  # type: DescribeDomainTopUrlVisitResponseBodyUrl200List
        self.url_300list = url_300list  # type: DescribeDomainTopUrlVisitResponseBodyUrl300List
        self.url_400list = url_400list  # type: DescribeDomainTopUrlVisitResponseBodyUrl400List
        self.url_500list = url_500list  # type: DescribeDomainTopUrlVisitResponseBodyUrl500List

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
        _map = super(DescribeDomainTopUrlVisitResponseBody, self).to_map()
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
            temp_model = DescribeDomainTopUrlVisitResponseBodyAllUrlList()
            self.all_url_list = temp_model.from_map(m['AllUrlList'])
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Url200List') is not None:
            temp_model = DescribeDomainTopUrlVisitResponseBodyUrl200List()
            self.url_200list = temp_model.from_map(m['Url200List'])
        if m.get('Url300List') is not None:
            temp_model = DescribeDomainTopUrlVisitResponseBodyUrl300List()
            self.url_300list = temp_model.from_map(m['Url300List'])
        if m.get('Url400List') is not None:
            temp_model = DescribeDomainTopUrlVisitResponseBodyUrl400List()
            self.url_400list = temp_model.from_map(m['Url400List'])
        if m.get('Url500List') is not None:
            temp_model = DescribeDomainTopUrlVisitResponseBodyUrl500List()
            self.url_500list = temp_model.from_map(m['Url500List'])
        return self


class DescribeDomainTopUrlVisitResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainTopUrlVisitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainTopUrlVisitResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainTopUrlVisitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainTrafficDataRequest(TeaModel):
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
        _map = super(DescribeDomainTrafficDataRequest, self).to_map()
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


class DescribeDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, domestic_value=None, https_domestic_value=None, https_overseas_value=None, https_value=None,
                 overseas_value=None, time_stamp=None, value=None):
        self.domestic_value = domestic_value  # type: str
        self.https_domestic_value = https_domestic_value  # type: str
        self.https_overseas_value = https_overseas_value  # type: str
        self.https_value = https_value  # type: str
        self.overseas_value = overseas_value  # type: str
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        if self.https_domestic_value is not None:
            result['HttpsDomesticValue'] = self.https_domestic_value
        if self.https_overseas_value is not None:
            result['HttpsOverseasValue'] = self.https_overseas_value
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        if m.get('HttpsDomesticValue') is not None:
            self.https_domestic_value = m.get('HttpsDomesticValue')
        if m.get('HttpsOverseasValue') is not None:
            self.https_overseas_value = m.get('HttpsOverseasValue')
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDomainTrafficDataResponseBodyTrafficDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainTrafficDataResponseBodyTrafficDataPerInterval, self).to_map()
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
                temp_model = DescribeDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainTrafficDataResponseBody(TeaModel):
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None, start_time=None,
                 traffic_data_per_interval=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.traffic_data_per_interval = traffic_data_per_interval  # type: DescribeDomainTrafficDataResponseBodyTrafficDataPerInterval

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainTrafficDataResponseBody, self).to_map()
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
            temp_model = DescribeDomainTrafficDataResponseBodyTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(m['TrafficDataPerInterval'])
        return self


class DescribeDomainTrafficDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainTrafficDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainTrafficDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainUsageDataRequest(TeaModel):
    def __init__(self, area=None, data_protocol=None, domain_name=None, end_time=None, field=None, interval=None,
                 owner_id=None, start_time=None, type=None):
        self.area = area  # type: str
        self.data_protocol = data_protocol  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.field = field  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainUsageDataRequest, self).to_map()
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
        if self.type is not None:
            result['Type'] = self.type
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
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDomainUsageDataResponseBodyUsageDataPerIntervalDataModule(TeaModel):
    def __init__(self, peak_time=None, special_value=None, time_stamp=None, value=None):
        self.peak_time = peak_time  # type: str
        self.special_value = special_value  # type: str
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainUsageDataResponseBodyUsageDataPerIntervalDataModule, self).to_map()
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


class DescribeDomainUsageDataResponseBodyUsageDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeDomainUsageDataResponseBodyUsageDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainUsageDataResponseBodyUsageDataPerInterval, self).to_map()
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
                temp_model = DescribeDomainUsageDataResponseBodyUsageDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeDomainUsageDataResponseBody(TeaModel):
    def __init__(self, area=None, data_interval=None, domain_name=None, end_time=None, request_id=None,
                 start_time=None, type=None, usage_data_per_interval=None):
        self.area = area  # type: str
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.type = type  # type: str
        self.usage_data_per_interval = usage_data_per_interval  # type: DescribeDomainUsageDataResponseBodyUsageDataPerInterval

    def validate(self):
        if self.usage_data_per_interval:
            self.usage_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeDomainUsageDataResponseBody, self).to_map()
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
            temp_model = DescribeDomainUsageDataResponseBodyUsageDataPerInterval()
            self.usage_data_per_interval = temp_model.from_map(m['UsageDataPerInterval'])
        return self


class DescribeDomainUsageDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainUsageDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainUsageDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainUsageDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainUvDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainUvDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    def __init__(self, cdn_type=None, create_time=None, domain_cname=None, domain_name=None, status=None,
                 update_time=None):
        self.cdn_type = cdn_type  # type: str
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
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
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
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainsBySourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainsUsageByDayResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainsUsageByDayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEsExceptionDataRequest(TeaModel):
    def __init__(self, end_time=None, owner_id=None, rule_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.rule_id = rule_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEsExceptionDataRequest, self).to_map()
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


class DescribeEsExceptionDataResponseBodyContents(TeaModel):
    def __init__(self, columns=None, name=None, points=None):
        self.columns = columns  # type: list[str]
        self.name = name  # type: str
        self.points = points  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEsExceptionDataResponseBodyContents, self).to_map()
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


class DescribeEsExceptionDataResponseBody(TeaModel):
    def __init__(self, contents=None, request_id=None):
        self.contents = contents  # type: list[DescribeEsExceptionDataResponseBodyContents]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.contents:
            for k in self.contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEsExceptionDataResponseBody, self).to_map()
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
                temp_model = DescribeEsExceptionDataResponseBodyContents()
                self.contents.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEsExceptionDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeEsExceptionDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEsExceptionDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEsExceptionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEsExecuteDataRequest(TeaModel):
    def __init__(self, end_time=None, owner_id=None, rule_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.rule_id = rule_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEsExecuteDataRequest, self).to_map()
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


class DescribeEsExecuteDataResponseBodyContents(TeaModel):
    def __init__(self, columns=None, name=None, points=None):
        self.columns = columns  # type: list[str]
        self.name = name  # type: str
        self.points = points  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEsExecuteDataResponseBodyContents, self).to_map()
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


class DescribeEsExecuteDataResponseBody(TeaModel):
    def __init__(self, contents=None, request_id=None):
        self.contents = contents  # type: list[DescribeEsExecuteDataResponseBodyContents]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.contents:
            for k in self.contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEsExecuteDataResponseBody, self).to_map()
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
                temp_model = DescribeEsExecuteDataResponseBodyContents()
                self.contents.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEsExecuteDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeEsExecuteDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEsExecuteDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEsExecuteDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFCTriggerRequest(TeaModel):
    def __init__(self, owner_id=None, trigger_arn=None):
        self.owner_id = owner_id  # type: long
        self.trigger_arn = trigger_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFCTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        return self


class DescribeFCTriggerResponseBodyFCTrigger(TeaModel):
    def __init__(self, event_meta_name=None, event_meta_version=None, notes=None, role_arn=None, source_arn=None,
                 trigger_arn=None):
        self.event_meta_name = event_meta_name  # type: str
        self.event_meta_version = event_meta_version  # type: str
        self.notes = notes  # type: str
        self.role_arn = role_arn  # type: str
        self.source_arn = source_arn  # type: str
        self.trigger_arn = trigger_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFCTriggerResponseBodyFCTrigger, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_meta_name is not None:
            result['EventMetaName'] = self.event_meta_name
        if self.event_meta_version is not None:
            result['EventMetaVersion'] = self.event_meta_version
        if self.notes is not None:
            result['Notes'] = self.notes
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        if self.source_arn is not None:
            result['SourceArn'] = self.source_arn
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventMetaName') is not None:
            self.event_meta_name = m.get('EventMetaName')
        if m.get('EventMetaVersion') is not None:
            self.event_meta_version = m.get('EventMetaVersion')
        if m.get('Notes') is not None:
            self.notes = m.get('Notes')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        if m.get('SourceArn') is not None:
            self.source_arn = m.get('SourceArn')
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        return self


class DescribeFCTriggerResponseBody(TeaModel):
    def __init__(self, fctrigger=None, request_id=None):
        self.fctrigger = fctrigger  # type: DescribeFCTriggerResponseBodyFCTrigger
        self.request_id = request_id  # type: str

    def validate(self):
        if self.fctrigger:
            self.fctrigger.validate()

    def to_map(self):
        _map = super(DescribeFCTriggerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fctrigger is not None:
            result['FCTrigger'] = self.fctrigger.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FCTrigger') is not None:
            temp_model = DescribeFCTriggerResponseBodyFCTrigger()
            self.fctrigger = temp_model.from_map(m['FCTrigger'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFCTriggerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeFCTriggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFCTriggerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFCTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIllegalUrlExportTaskRequest(TeaModel):
    def __init__(self, owner_id=None, task_id=None):
        self.owner_id = owner_id  # type: long
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIllegalUrlExportTaskRequest, self).to_map()
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


class DescribeIllegalUrlExportTaskResponseBody(TeaModel):
    def __init__(self, download_url=None, request_id=None, status=None):
        self.download_url = download_url  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIllegalUrlExportTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeIllegalUrlExportTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeIllegalUrlExportTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIllegalUrlExportTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeIllegalUrlExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpInfoRequest(TeaModel):
    def __init__(self, ip=None, owner_id=None, security_token=None):
        self.ip = ip  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpInfoRequest, self).to_map()
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


class DescribeIpInfoResponseBody(TeaModel):
    def __init__(self, cdn_ip=None, isp=None, isp_ename=None, region=None, region_ename=None, request_id=None):
        self.cdn_ip = cdn_ip  # type: str
        self.isp = isp  # type: str
        self.isp_ename = isp_ename  # type: str
        self.region = region  # type: str
        self.region_ename = region_ename  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIpInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_ip is not None:
            result['CdnIp'] = self.cdn_ip
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
        if m.get('CdnIp') is not None:
            self.cdn_ip = m.get('CdnIp')
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


class DescribeIpInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeIpInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIpInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeIpInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeL2VipsByDomainRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeL2VipsByDomainRequest, self).to_map()
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


class DescribeL2VipsByDomainResponseBodyVips(TeaModel):
    def __init__(self, vip=None):
        self.vip = vip  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeL2VipsByDomainResponseBodyVips, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vip is not None:
            result['Vip'] = self.vip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Vip') is not None:
            self.vip = m.get('Vip')
        return self


class DescribeL2VipsByDomainResponseBody(TeaModel):
    def __init__(self, domain_name=None, request_id=None, vips=None):
        self.domain_name = domain_name  # type: str
        self.request_id = request_id  # type: str
        self.vips = vips  # type: DescribeL2VipsByDomainResponseBodyVips

    def validate(self):
        if self.vips:
            self.vips.validate()

    def to_map(self):
        _map = super(DescribeL2VipsByDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vips is not None:
            result['Vips'] = self.vips.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Vips') is not None:
            temp_model = DescribeL2VipsByDomainResponseBodyVips()
            self.vips = temp_model.from_map(m['Vips'])
        return self


class DescribeL2VipsByDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeL2VipsByDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeL2VipsByDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeL2VipsByDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRangeDataByLocateAndIspServiceRequest(TeaModel):
    def __init__(self, domain_names=None, end_time=None, isp_names=None, location_names=None, owner_id=None,
                 start_time=None):
        self.domain_names = domain_names  # type: str
        self.end_time = end_time  # type: str
        self.isp_names = isp_names  # type: str
        self.location_names = location_names  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRangeDataByLocateAndIspServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_names is not None:
            result['IspNames'] = self.isp_names
        if self.location_names is not None:
            result['LocationNames'] = self.location_names
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IspNames') is not None:
            self.isp_names = m.get('IspNames')
        if m.get('LocationNames') is not None:
            self.location_names = m.get('LocationNames')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeRangeDataByLocateAndIspServiceResponseBody(TeaModel):
    def __init__(self, json_result=None, request_id=None):
        self.json_result = json_result  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRangeDataByLocateAndIspServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_result is not None:
            result['JsonResult'] = self.json_result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonResult') is not None:
            self.json_result = m.get('JsonResult')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRangeDataByLocateAndIspServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRangeDataByLocateAndIspServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRangeDataByLocateAndIspServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRangeDataByLocateAndIspServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRealtimeDeliveryAccRequest(TeaModel):
    def __init__(self, end_time=None, interval=None, log_store=None, owner_id=None, project=None, start_time=None):
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.log_store = log_store  # type: str
        self.owner_id = owner_id  # type: long
        self.project = project  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRealtimeDeliveryAccRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project is not None:
            result['Project'] = self.project
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccDataAccData(TeaModel):
    def __init__(self, failed_num=None, success_num=None, time_stamp=None):
        self.failed_num = failed_num  # type: int
        self.success_num = success_num  # type: int
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccDataAccData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_num is not None:
            result['FailedNum'] = self.failed_num
        if self.success_num is not None:
            result['SuccessNum'] = self.success_num
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailedNum') is not None:
            self.failed_num = m.get('FailedNum')
        if m.get('SuccessNum') is not None:
            self.success_num = m.get('SuccessNum')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccData(TeaModel):
    def __init__(self, acc_data=None):
        self.acc_data = acc_data  # type: list[DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccDataAccData]

    def validate(self):
        if self.acc_data:
            for k in self.acc_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccData'] = []
        if self.acc_data is not None:
            for k in self.acc_data:
                result['AccData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.acc_data = []
        if m.get('AccData') is not None:
            for k in m.get('AccData'):
                temp_model = DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccDataAccData()
                self.acc_data.append(temp_model.from_map(k))
        return self


class DescribeRealtimeDeliveryAccResponseBody(TeaModel):
    def __init__(self, reat_time_delivery_acc_data=None, request_id=None):
        self.reat_time_delivery_acc_data = reat_time_delivery_acc_data  # type: DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.reat_time_delivery_acc_data:
            self.reat_time_delivery_acc_data.validate()

    def to_map(self):
        _map = super(DescribeRealtimeDeliveryAccResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reat_time_delivery_acc_data is not None:
            result['ReatTimeDeliveryAccData'] = self.reat_time_delivery_acc_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReatTimeDeliveryAccData') is not None:
            temp_model = DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccData()
            self.reat_time_delivery_acc_data = temp_model.from_map(m['ReatTimeDeliveryAccData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRealtimeDeliveryAccResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRealtimeDeliveryAccResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRealtimeDeliveryAccResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRealtimeDeliveryAccResponseBody()
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
    def __init__(self, block_quota=None, block_remain=None, dir_quota=None, dir_remain=None,
                 preload_edge_quota=None, preload_edge_remain=None, preload_quota=None, preload_remain=None, regex_quota=None,
                 regex_remain=None, request_id=None, url_quota=None, url_remain=None):
        self.block_quota = block_quota  # type: str
        self.block_remain = block_remain  # type: str
        self.dir_quota = dir_quota  # type: str
        self.dir_remain = dir_remain  # type: str
        self.preload_edge_quota = preload_edge_quota  # type: str
        self.preload_edge_remain = preload_edge_remain  # type: str
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
        if self.preload_edge_quota is not None:
            result['PreloadEdgeQuota'] = self.preload_edge_quota
        if self.preload_edge_remain is not None:
            result['PreloadEdgeRemain'] = self.preload_edge_remain
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
        if m.get('PreloadEdgeQuota') is not None:
            self.preload_edge_quota = m.get('PreloadEdgeQuota')
        if m.get('PreloadEdgeRemain') is not None:
            self.preload_edge_remain = m.get('PreloadEdgeRemain')
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


class DescribeRefreshQuotaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRefreshQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRefreshQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRefreshTaskByIdRequest(TeaModel):
    def __init__(self, owner_id=None, task_id=None):
        self.owner_id = owner_id  # type: long
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRefreshTaskByIdRequest, self).to_map()
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


class DescribeRefreshTaskByIdResponseBodyTasks(TeaModel):
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
        _map = super(DescribeRefreshTaskByIdResponseBodyTasks, self).to_map()
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


class DescribeRefreshTaskByIdResponseBody(TeaModel):
    def __init__(self, request_id=None, tasks=None, total_count=None):
        self.request_id = request_id  # type: str
        self.tasks = tasks  # type: list[DescribeRefreshTaskByIdResponseBodyTasks]
        self.total_count = total_count  # type: long

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRefreshTaskByIdResponseBody, self).to_map()
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
                temp_model = DescribeRefreshTaskByIdResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRefreshTaskByIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRefreshTaskByIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRefreshTaskByIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRefreshTaskByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRefreshTasksRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, object_path=None, object_type=None, owner_id=None,
                 page_number=None, page_size=None, resource_group_id=None, security_token=None, start_time=None, status=None,
                 task_id=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.object_path = object_path  # type: str
        self.object_type = object_type  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.security_token = security_token  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRefreshTasksRequest, self).to_map()
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeRefreshTasksResponseBodyTasksCDNTask(TeaModel):
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
        _map = super(DescribeRefreshTasksResponseBodyTasksCDNTask, self).to_map()
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


class DescribeRefreshTasksResponseBodyTasks(TeaModel):
    def __init__(self, cdntask=None):
        self.cdntask = cdntask  # type: list[DescribeRefreshTasksResponseBodyTasksCDNTask]

    def validate(self):
        if self.cdntask:
            for k in self.cdntask:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRefreshTasksResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CDNTask'] = []
        if self.cdntask is not None:
            for k in self.cdntask:
                result['CDNTask'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cdntask = []
        if m.get('CDNTask') is not None:
            for k in m.get('CDNTask'):
                temp_model = DescribeRefreshTasksResponseBodyTasksCDNTask()
                self.cdntask.append(temp_model.from_map(k))
        return self


class DescribeRefreshTasksResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, tasks=None, total_count=None):
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.tasks = tasks  # type: DescribeRefreshTasksResponseBodyTasks
        self.total_count = total_count  # type: long

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        _map = super(DescribeRefreshTasksResponseBody, self).to_map()
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
            temp_model = DescribeRefreshTasksResponseBodyTasks()
            self.tasks = temp_model.from_map(m['Tasks'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRefreshTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRefreshTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRefreshTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRefreshTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStagingIpRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStagingIpRequest, self).to_map()
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


class DescribeStagingIpResponseBodyIPV4s(TeaModel):
    def __init__(self, ipv4=None):
        self.ipv4 = ipv4  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStagingIpResponseBodyIPV4s, self).to_map()
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


class DescribeStagingIpResponseBody(TeaModel):
    def __init__(self, ipv4s=None, request_id=None):
        self.ipv4s = ipv4s  # type: DescribeStagingIpResponseBodyIPV4s
        self.request_id = request_id  # type: str

    def validate(self):
        if self.ipv4s:
            self.ipv4s.validate()

    def to_map(self):
        _map = super(DescribeStagingIpResponseBody, self).to_map()
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
            temp_model = DescribeStagingIpResponseBodyIPV4s()
            self.ipv4s = temp_model.from_map(m['IPV4s'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeStagingIpResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeStagingIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeStagingIpResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeStagingIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTagResourcesRequestTag, self).to_map()
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


class DescribeTagResourcesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_id=None, resource_type=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
        self.tag = tag  # type: list[DescribeTagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTagResourcesRequest, self).to_map()
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
                temp_model = DescribeTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeTagResourcesResponseBodyTagResourcesTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTagResourcesResponseBodyTagResourcesTag, self).to_map()
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


class DescribeTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, resource_id=None, tag=None):
        self.resource_id = resource_id  # type: str
        self.tag = tag  # type: list[DescribeTagResourcesResponseBodyTagResourcesTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTagResourcesResponseBodyTagResources, self).to_map()
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
                temp_model = DescribeTagResourcesResponseBodyTagResourcesTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeTagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, tag_resources=None):
        self.request_id = request_id  # type: str
        self.tag_resources = tag_resources  # type: list[DescribeTagResourcesResponseBodyTagResources]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTagResourcesResponseBody, self).to_map()
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
                temp_model = DescribeTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class DescribeTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTopDomainsByFlowRequest(TeaModel):
    def __init__(self, end_time=None, limit=None, owner_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.limit = limit  # type: long
        self.owner_id = owner_id  # type: long
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeTopDomainsByFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTopDomainsByFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserCertificateExpireCountRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserCertificateExpireCountRequest, self).to_map()
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


class DescribeUserCertificateExpireCountResponseBody(TeaModel):
    def __init__(self, expire_within_30days_count=None, expired_count=None, request_id=None):
        self.expire_within_30days_count = expire_within_30days_count  # type: int
        self.expired_count = expired_count  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserCertificateExpireCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_within_30days_count is not None:
            result['ExpireWithin30DaysCount'] = self.expire_within_30days_count
        if self.expired_count is not None:
            result['ExpiredCount'] = self.expired_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpireWithin30DaysCount') is not None:
            self.expire_within_30days_count = m.get('ExpireWithin30DaysCount')
        if m.get('ExpiredCount') is not None:
            self.expired_count = m.get('ExpiredCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserCertificateExpireCountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserCertificateExpireCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserCertificateExpireCountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserCertificateExpireCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserConfigsRequest(TeaModel):
    def __init__(self, config=None, owner_id=None, security_token=None):
        self.config = config  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeUserConfigsResponseBodyConfigsOssLogConfig(TeaModel):
    def __init__(self, bucket=None, enable=None, prefix=None):
        self.bucket = bucket  # type: str
        self.enable = enable  # type: str
        self.prefix = prefix  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserConfigsResponseBodyConfigsOssLogConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class DescribeUserConfigsResponseBodyConfigsWafConfig(TeaModel):
    def __init__(self, enable=None):
        self.enable = enable  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserConfigsResponseBodyConfigsWafConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DescribeUserConfigsResponseBodyConfigs(TeaModel):
    def __init__(self, oss_log_config=None, waf_config=None):
        self.oss_log_config = oss_log_config  # type: DescribeUserConfigsResponseBodyConfigsOssLogConfig
        self.waf_config = waf_config  # type: DescribeUserConfigsResponseBodyConfigsWafConfig

    def validate(self):
        if self.oss_log_config:
            self.oss_log_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        _map = super(DescribeUserConfigsResponseBodyConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_log_config is not None:
            result['OssLogConfig'] = self.oss_log_config.to_map()
        if self.waf_config is not None:
            result['WafConfig'] = self.waf_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssLogConfig') is not None:
            temp_model = DescribeUserConfigsResponseBodyConfigsOssLogConfig()
            self.oss_log_config = temp_model.from_map(m['OssLogConfig'])
        if m.get('WafConfig') is not None:
            temp_model = DescribeUserConfigsResponseBodyConfigsWafConfig()
            self.waf_config = temp_model.from_map(m['WafConfig'])
        return self


class DescribeUserConfigsResponseBody(TeaModel):
    def __init__(self, configs=None, request_id=None):
        self.configs = configs  # type: DescribeUserConfigsResponseBodyConfigs
        self.request_id = request_id  # type: str

    def validate(self):
        if self.configs:
            self.configs.validate()

    def to_map(self):
        _map = super(DescribeUserConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs is not None:
            result['Configs'] = self.configs.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Configs') is not None:
            temp_model = DescribeUserConfigsResponseBodyConfigs()
            self.configs = temp_model.from_map(m['Configs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserDomainsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserDomainsRequestTag, self).to_map()
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


class DescribeUserDomainsRequest(TeaModel):
    def __init__(self, cdn_type=None, change_end_time=None, change_start_time=None, check_domain_show=None,
                 coverage=None, domain_name=None, domain_search_type=None, domain_status=None, owner_id=None,
                 page_number=None, page_size=None, resource_group_id=None, security_token=None, source=None, tag=None):
        self.cdn_type = cdn_type  # type: str
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
        self.source = source  # type: str
        self.tag = tag  # type: list[DescribeUserDomainsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUserDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
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
        if self.source is not None:
            result['Source'] = self.source
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
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
        if m.get('Source') is not None:
            self.source = m.get('Source')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeUserDomainsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeUserDomainsResponseBodyDomainsPageDataSourcesSource(TeaModel):
    def __init__(self, content=None, port=None, priority=None, type=None, weight=None):
        self.content = content  # type: str
        self.port = port  # type: int
        self.priority = priority  # type: str
        self.type = type  # type: str
        self.weight = weight  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserDomainsResponseBodyDomainsPageDataSourcesSource, self).to_map()
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


class DescribeUserDomainsResponseBodyDomainsPageDataSources(TeaModel):
    def __init__(self, source=None):
        self.source = source  # type: list[DescribeUserDomainsResponseBodyDomainsPageDataSourcesSource]

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUserDomainsResponseBodyDomainsPageDataSources, self).to_map()
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
                temp_model = DescribeUserDomainsResponseBodyDomainsPageDataSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeUserDomainsResponseBodyDomainsPageData(TeaModel):
    def __init__(self, cdn_type=None, cname=None, coverage=None, description=None, domain_name=None,
                 domain_status=None, gmt_created=None, gmt_modified=None, resource_group_id=None, sandbox=None, sources=None,
                 ssl_protocol=None):
        self.cdn_type = cdn_type  # type: str
        self.cname = cname  # type: str
        self.coverage = coverage  # type: str
        self.description = description  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.sandbox = sandbox  # type: str
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
        if self.coverage is not None:
            result['Coverage'] = self.coverage
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
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserDomainsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserTagsRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserTagsRequest, self).to_map()
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


class DescribeUserTagsResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserTagsResponseBodyTags, self).to_map()
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


class DescribeUserTagsResponseBody(TeaModel):
    def __init__(self, request_id=None, tags=None):
        self.request_id = request_id  # type: str
        self.tags = tags  # type: list[DescribeUserTagsResponseBodyTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUserTagsResponseBody, self).to_map()
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
                temp_model = DescribeUserTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeUserTagsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserTagsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserUsageDataExportTaskRequest(TeaModel):
    def __init__(self, owner_id=None, page_number=None, page_size=None):
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserUsageDataExportTaskRequest, self).to_map()
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


class DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig(TeaModel):
    def __init__(self, end_time=None, start_time=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItem(TeaModel):
    def __init__(self, create_time=None, download_url=None, status=None, task_config=None, task_id=None,
                 task_name=None, update_time=None):
        self.create_time = create_time  # type: str
        self.download_url = download_url  # type: str
        self.status = status  # type: str
        self.task_config = task_config  # type: DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        if self.task_config:
            self.task_config.validate()

    def to_map(self):
        _map = super(DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.status is not None:
            result['Status'] = self.status
        if self.task_config is not None:
            result['TaskConfig'] = self.task_config.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskConfig') is not None:
            temp_model = DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig()
            self.task_config = temp_model.from_map(m['TaskConfig'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageData(TeaModel):
    def __init__(self, data_item=None):
        self.data_item = data_item  # type: list[DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItem]

    def validate(self):
        if self.data_item:
            for k in self.data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataItem'] = []
        if self.data_item is not None:
            for k in self.data_item:
                result['DataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_item = []
        if m.get('DataItem') is not None:
            for k in m.get('DataItem'):
                temp_model = DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageDataDataItem()
                self.data_item.append(temp_model.from_map(k))
        return self


class DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPage(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, total_count=None):
        self.data = data  # type: DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageData
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPageData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeUserUsageDataExportTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, usage_data_per_page=None):
        self.request_id = request_id  # type: str
        self.usage_data_per_page = usage_data_per_page  # type: DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPage

    def validate(self):
        if self.usage_data_per_page:
            self.usage_data_per_page.validate()

    def to_map(self):
        _map = super(DescribeUserUsageDataExportTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.usage_data_per_page is not None:
            result['UsageDataPerPage'] = self.usage_data_per_page.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UsageDataPerPage') is not None:
            temp_model = DescribeUserUsageDataExportTaskResponseBodyUsageDataPerPage()
            self.usage_data_per_page = temp_model.from_map(m['UsageDataPerPage'])
        return self


class DescribeUserUsageDataExportTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserUsageDataExportTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserUsageDataExportTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserUsageDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserUsageDetailDataExportTaskRequest(TeaModel):
    def __init__(self, owner_id=None, page_number=None, page_size=None):
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserUsageDetailDataExportTaskRequest, self).to_map()
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


class DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig(TeaModel):
    def __init__(self, end_time=None, start_time=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItem(TeaModel):
    def __init__(self, create_time=None, download_url=None, status=None, task_config=None, task_id=None,
                 task_name=None, update_time=None):
        self.create_time = create_time  # type: str
        self.download_url = download_url  # type: str
        self.status = status  # type: str
        self.task_config = task_config  # type: DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        if self.task_config:
            self.task_config.validate()

    def to_map(self):
        _map = super(DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.status is not None:
            result['Status'] = self.status
        if self.task_config is not None:
            result['TaskConfig'] = self.task_config.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskConfig') is not None:
            temp_model = DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItemTaskConfig()
            self.task_config = temp_model.from_map(m['TaskConfig'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageData(TeaModel):
    def __init__(self, data_item=None):
        self.data_item = data_item  # type: list[DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItem]

    def validate(self):
        if self.data_item:
            for k in self.data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataItem'] = []
        if self.data_item is not None:
            for k in self.data_item:
                result['DataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_item = []
        if m.get('DataItem') is not None:
            for k in m.get('DataItem'):
                temp_model = DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageDataDataItem()
                self.data_item.append(temp_model.from_map(k))
        return self


class DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPage(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, total_count=None):
        self.data = data  # type: DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageData
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPageData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeUserUsageDetailDataExportTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, usage_data_per_page=None):
        self.request_id = request_id  # type: str
        self.usage_data_per_page = usage_data_per_page  # type: DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPage

    def validate(self):
        if self.usage_data_per_page:
            self.usage_data_per_page.validate()

    def to_map(self):
        _map = super(DescribeUserUsageDetailDataExportTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.usage_data_per_page is not None:
            result['UsageDataPerPage'] = self.usage_data_per_page.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UsageDataPerPage') is not None:
            temp_model = DescribeUserUsageDetailDataExportTaskResponseBodyUsageDataPerPage()
            self.usage_data_per_page = temp_model.from_map(m['UsageDataPerPage'])
        return self


class DescribeUserUsageDetailDataExportTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserUsageDetailDataExportTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserUsageDetailDataExportTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserUsageDetailDataExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserVipsByDomainRequest(TeaModel):
    def __init__(self, available=None, domain_name=None, owner_id=None):
        self.available = available  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserVipsByDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available is not None:
            result['Available'] = self.available
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeUserVipsByDomainResponseBodyVips(TeaModel):
    def __init__(self, vip=None):
        self.vip = vip  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserVipsByDomainResponseBodyVips, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vip is not None:
            result['Vip'] = self.vip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Vip') is not None:
            self.vip = m.get('Vip')
        return self


class DescribeUserVipsByDomainResponseBody(TeaModel):
    def __init__(self, domain_name=None, request_id=None, vips=None):
        self.domain_name = domain_name  # type: str
        self.request_id = request_id  # type: str
        self.vips = vips  # type: DescribeUserVipsByDomainResponseBodyVips

    def validate(self):
        if self.vips:
            self.vips.validate()

    def to_map(self):
        _map = super(DescribeUserVipsByDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vips is not None:
            result['Vips'] = self.vips.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Vips') is not None:
            temp_model = DescribeUserVipsByDomainResponseBodyVips()
            self.vips = temp_model.from_map(m['Vips'])
        return self


class DescribeUserVipsByDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserVipsByDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserVipsByDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserVipsByDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifyContentRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVerifyContentRequest, self).to_map()
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


class DescribeVerifyContentResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVerifyContentResponseBody, self).to_map()
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


class DescribeVerifyContentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVerifyContentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVerifyContentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVerifyContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableRealtimeLogDeliveryRequest(TeaModel):
    def __init__(self, domain=None, owner_id=None):
        self.domain = domain  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableRealtimeLogDeliveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DisableRealtimeLogDeliveryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableRealtimeLogDeliveryResponseBody, self).to_map()
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


class DisableRealtimeLogDeliveryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableRealtimeLogDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableRealtimeLogDeliveryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableRealtimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableRealtimeLogDeliveryRequest(TeaModel):
    def __init__(self, domain=None, owner_id=None):
        self.domain = domain  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableRealtimeLogDeliveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class EnableRealtimeLogDeliveryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableRealtimeLogDeliveryResponseBody, self).to_map()
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


class EnableRealtimeLogDeliveryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableRealtimeLogDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableRealtimeLogDeliveryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableRealtimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDomainsByLogConfigIdRequest(TeaModel):
    def __init__(self, config_id=None, owner_id=None):
        self.config_id = config_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDomainsByLogConfigIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ListDomainsByLogConfigIdResponseBodyDomains(TeaModel):
    def __init__(self, domain=None):
        self.domain = domain  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDomainsByLogConfigIdResponseBodyDomains, self).to_map()
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


class ListDomainsByLogConfigIdResponseBody(TeaModel):
    def __init__(self, domains=None, request_id=None):
        self.domains = domains  # type: ListDomainsByLogConfigIdResponseBodyDomains
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super(ListDomainsByLogConfigIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domains') is not None:
            temp_model = ListDomainsByLogConfigIdResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDomainsByLogConfigIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDomainsByLogConfigIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDomainsByLogConfigIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDomainsByLogConfigIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFCTriggerRequest(TeaModel):
    def __init__(self, event_meta_name=None, event_meta_version=None, owner_id=None):
        self.event_meta_name = event_meta_name  # type: str
        self.event_meta_version = event_meta_version  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFCTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_meta_name is not None:
            result['EventMetaName'] = self.event_meta_name
        if self.event_meta_version is not None:
            result['EventMetaVersion'] = self.event_meta_version
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventMetaName') is not None:
            self.event_meta_name = m.get('EventMetaName')
        if m.get('EventMetaVersion') is not None:
            self.event_meta_version = m.get('EventMetaVersion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ListFCTriggerResponseBodyFCTriggers(TeaModel):
    def __init__(self, event_meta_name=None, event_meta_version=None, notes=None, role_arn=None, source_arn=None,
                 trigger_arn=None):
        self.event_meta_name = event_meta_name  # type: str
        self.event_meta_version = event_meta_version  # type: str
        self.notes = notes  # type: str
        self.role_arn = role_arn  # type: str
        self.source_arn = source_arn  # type: str
        self.trigger_arn = trigger_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFCTriggerResponseBodyFCTriggers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_meta_name is not None:
            result['EventMetaName'] = self.event_meta_name
        if self.event_meta_version is not None:
            result['EventMetaVersion'] = self.event_meta_version
        if self.notes is not None:
            result['Notes'] = self.notes
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        if self.source_arn is not None:
            result['SourceArn'] = self.source_arn
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventMetaName') is not None:
            self.event_meta_name = m.get('EventMetaName')
        if m.get('EventMetaVersion') is not None:
            self.event_meta_version = m.get('EventMetaVersion')
        if m.get('Notes') is not None:
            self.notes = m.get('Notes')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        if m.get('SourceArn') is not None:
            self.source_arn = m.get('SourceArn')
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        return self


class ListFCTriggerResponseBody(TeaModel):
    def __init__(self, fctriggers=None, request_id=None):
        self.fctriggers = fctriggers  # type: list[ListFCTriggerResponseBodyFCTriggers]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.fctriggers:
            for k in self.fctriggers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFCTriggerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FCTriggers'] = []
        if self.fctriggers is not None:
            for k in self.fctriggers:
                result['FCTriggers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.fctriggers = []
        if m.get('FCTriggers') is not None:
            for k in m.get('FCTriggers'):
                temp_model = ListFCTriggerResponseBodyFCTriggers()
                self.fctriggers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFCTriggerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFCTriggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFCTriggerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFCTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRealtimeLogDeliveryDomainsRequest(TeaModel):
    def __init__(self, logstore=None, owner_id=None, project=None, region=None):
        self.logstore = logstore  # type: str
        self.owner_id = owner_id  # type: long
        self.project = project  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRealtimeLogDeliveryDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ListRealtimeLogDeliveryDomainsResponseBodyContentDomains(TeaModel):
    def __init__(self, domain_name=None, status=None):
        self.domain_name = domain_name  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRealtimeLogDeliveryDomainsResponseBodyContentDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListRealtimeLogDeliveryDomainsResponseBodyContent(TeaModel):
    def __init__(self, domains=None):
        self.domains = domains  # type: list[ListRealtimeLogDeliveryDomainsResponseBodyContentDomains]

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRealtimeLogDeliveryDomainsResponseBodyContent, self).to_map()
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
                temp_model = ListRealtimeLogDeliveryDomainsResponseBodyContentDomains()
                self.domains.append(temp_model.from_map(k))
        return self


class ListRealtimeLogDeliveryDomainsResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: ListRealtimeLogDeliveryDomainsResponseBodyContent
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(ListRealtimeLogDeliveryDomainsResponseBody, self).to_map()
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
            temp_model = ListRealtimeLogDeliveryDomainsResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRealtimeLogDeliveryDomainsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRealtimeLogDeliveryDomainsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRealtimeLogDeliveryDomainsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRealtimeLogDeliveryDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRealtimeLogDeliveryInfosRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRealtimeLogDeliveryInfosRequest, self).to_map()
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


class ListRealtimeLogDeliveryInfosResponseBodyContentRealtimeLogDeliveryInfos(TeaModel):
    def __init__(self, logstore=None, project=None, region=None):
        self.logstore = logstore  # type: str
        self.project = project  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRealtimeLogDeliveryInfosResponseBodyContentRealtimeLogDeliveryInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ListRealtimeLogDeliveryInfosResponseBodyContent(TeaModel):
    def __init__(self, realtime_log_delivery_infos=None):
        self.realtime_log_delivery_infos = realtime_log_delivery_infos  # type: list[ListRealtimeLogDeliveryInfosResponseBodyContentRealtimeLogDeliveryInfos]

    def validate(self):
        if self.realtime_log_delivery_infos:
            for k in self.realtime_log_delivery_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRealtimeLogDeliveryInfosResponseBodyContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RealtimeLogDeliveryInfos'] = []
        if self.realtime_log_delivery_infos is not None:
            for k in self.realtime_log_delivery_infos:
                result['RealtimeLogDeliveryInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.realtime_log_delivery_infos = []
        if m.get('RealtimeLogDeliveryInfos') is not None:
            for k in m.get('RealtimeLogDeliveryInfos'):
                temp_model = ListRealtimeLogDeliveryInfosResponseBodyContentRealtimeLogDeliveryInfos()
                self.realtime_log_delivery_infos.append(temp_model.from_map(k))
        return self


class ListRealtimeLogDeliveryInfosResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: ListRealtimeLogDeliveryInfosResponseBodyContent
        self.request_id = request_id  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(ListRealtimeLogDeliveryInfosResponseBody, self).to_map()
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
            temp_model = ListRealtimeLogDeliveryInfosResponseBodyContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRealtimeLogDeliveryInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRealtimeLogDeliveryInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRealtimeLogDeliveryInfosResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRealtimeLogDeliveryInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserCustomLogConfigRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserCustomLogConfigRequest, self).to_map()
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


class ListUserCustomLogConfigResponseBodyConfigIds(TeaModel):
    def __init__(self, config_id=None):
        self.config_id = config_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserCustomLogConfigResponseBodyConfigIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class ListUserCustomLogConfigResponseBody(TeaModel):
    def __init__(self, config_ids=None, request_id=None):
        self.config_ids = config_ids  # type: ListUserCustomLogConfigResponseBodyConfigIds
        self.request_id = request_id  # type: str

    def validate(self):
        if self.config_ids:
            self.config_ids.validate()

    def to_map(self):
        _map = super(ListUserCustomLogConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_ids is not None:
            result['ConfigIds'] = self.config_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigIds') is not None:
            temp_model = ListUserCustomLogConfigResponseBodyConfigIds()
            self.config_ids = temp_model.from_map(m['ConfigIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUserCustomLogConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListUserCustomLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserCustomLogConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserCustomLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCdnDomainRequest(TeaModel):
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
        _map = super(ModifyCdnDomainRequest, self).to_map()
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


class ModifyCdnDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyCdnDomainResponseBody, self).to_map()
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


class ModifyCdnDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyCdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyCdnDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCdnDomainSchdmByPropertyRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, property=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.property = property  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyCdnDomainSchdmByPropertyRequest, self).to_map()
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


class ModifyCdnDomainSchdmByPropertyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyCdnDomainSchdmByPropertyResponseBody, self).to_map()
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


class ModifyCdnDomainSchdmByPropertyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyCdnDomainSchdmByPropertyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyCdnDomainSchdmByPropertyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyCdnDomainSchdmByPropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDomainCustomLogConfigRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, owner_id=None):
        self.config_id = config_id  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDomainCustomLogConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ModifyDomainCustomLogConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDomainCustomLogConfigResponseBody, self).to_map()
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


class ModifyDomainCustomLogConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDomainCustomLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDomainCustomLogConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDomainCustomLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRealtimeLogDeliveryRequest(TeaModel):
    def __init__(self, domain=None, logstore=None, owner_id=None, project=None, region=None):
        self.domain = domain  # type: str
        self.logstore = logstore  # type: str
        self.owner_id = owner_id  # type: long
        self.project = project  # type: str
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyRealtimeLogDeliveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project is not None:
            result['Project'] = self.project
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ModifyRealtimeLogDeliveryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyRealtimeLogDeliveryResponseBody, self).to_map()
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


class ModifyRealtimeLogDeliveryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyRealtimeLogDeliveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyRealtimeLogDeliveryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyRealtimeLogDeliveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserCustomLogConfigRequest(TeaModel):
    def __init__(self, config_id=None, owner_id=None, tag=None):
        self.config_id = config_id  # type: str
        self.owner_id = owner_id  # type: long
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserCustomLogConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ModifyUserCustomLogConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserCustomLogConfigResponseBody, self).to_map()
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


class ModifyUserCustomLogConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyUserCustomLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyUserCustomLogConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyUserCustomLogConfigResponseBody()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OpenCdnServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OpenCdnServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishStagingConfigToProductionRequest(TeaModel):
    def __init__(self, domain_name=None, function_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.function_name = function_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishStagingConfigToProductionRequest, self).to_map()
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


class PublishStagingConfigToProductionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublishStagingConfigToProductionResponseBody, self).to_map()
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


class PublishStagingConfigToProductionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PublishStagingConfigToProductionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublishStagingConfigToProductionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PublishStagingConfigToProductionResponseBody()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PushObjectCacheResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RefreshObjectCachesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RefreshObjectCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackStagingConfigRequest(TeaModel):
    def __init__(self, domain_name=None, function_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.function_name = function_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RollbackStagingConfigRequest, self).to_map()
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


class RollbackStagingConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RollbackStagingConfigResponseBody, self).to_map()
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


class RollbackStagingConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RollbackStagingConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RollbackStagingConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RollbackStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCcConfigRequest(TeaModel):
    def __init__(self, allow_ips=None, block_ips=None, domain_name=None, owner_id=None, security_token=None):
        self.allow_ips = allow_ips  # type: str
        self.block_ips = block_ips  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetCcConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_ips is not None:
            result['AllowIps'] = self.allow_ips
        if self.block_ips is not None:
            result['BlockIps'] = self.block_ips
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowIps') is not None:
            self.allow_ips = m.get('AllowIps')
        if m.get('BlockIps') is not None:
            self.block_ips = m.get('BlockIps')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetCcConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetCcConfigResponseBody, self).to_map()
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


class SetCcConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetCcConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetCcConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetCcConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCdnDomainCSRCertificateRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, server_certificate=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.server_certificate = server_certificate  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetCdnDomainCSRCertificateRequest, self).to_map()
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


class SetCdnDomainCSRCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetCdnDomainCSRCertificateResponseBody, self).to_map()
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


class SetCdnDomainCSRCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetCdnDomainCSRCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetCdnDomainCSRCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetCdnDomainCSRCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCdnDomainSMCertificateRequest(TeaModel):
    def __init__(self, cert_identifier=None, domain_name=None, owner_id=None, sslprotocol=None, security_token=None):
        self.cert_identifier = cert_identifier  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.sslprotocol = sslprotocol  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetCdnDomainSMCertificateRequest, self).to_map()
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


class SetCdnDomainSMCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetCdnDomainSMCertificateResponseBody, self).to_map()
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


class SetCdnDomainSMCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetCdnDomainSMCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetCdnDomainSMCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetCdnDomainSMCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCdnDomainStagingConfigRequest(TeaModel):
    def __init__(self, domain_name=None, functions=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.functions = functions  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetCdnDomainStagingConfigRequest, self).to_map()
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


class SetCdnDomainStagingConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetCdnDomainStagingConfigResponseBody, self).to_map()
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


class SetCdnDomainStagingConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetCdnDomainStagingConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetCdnDomainStagingConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetCdnDomainStagingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetConfigOfVersionRequest(TeaModel):
    def __init__(self, config_id=None, function_args=None, function_id=None, function_matches=None,
                 function_name=None, owner_account=None, owner_id=None, security_token=None, version_id=None):
        self.config_id = config_id  # type: str
        self.function_args = function_args  # type: str
        self.function_id = function_id  # type: long
        self.function_matches = function_matches  # type: str
        self.function_name = function_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetConfigOfVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args
        if self.function_id is not None:
            result['FunctionId'] = self.function_id
        if self.function_matches is not None:
            result['FunctionMatches'] = self.function_matches
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
        if m.get('FunctionMatches') is not None:
            self.function_matches = m.get('FunctionMatches')
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


class SetConfigOfVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetConfigOfVersionResponseBody, self).to_map()
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


class SetConfigOfVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetConfigOfVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetConfigOfVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetConfigOfVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainGreenManagerConfigRequest(TeaModel):
    def __init__(self, domain_name=None, enable=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.enable = enable  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDomainGreenManagerConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class SetDomainGreenManagerConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDomainGreenManagerConfigResponseBody, self).to_map()
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


class SetDomainGreenManagerConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDomainGreenManagerConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDomainGreenManagerConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetDomainGreenManagerConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainServerCertificateRequest(TeaModel):
    def __init__(self, cert_name=None, cert_type=None, domain_name=None, force_set=None, owner_id=None,
                 private_key=None, security_token=None, server_certificate=None, server_certificate_status=None):
        self.cert_name = cert_name  # type: str
        self.cert_type = cert_type  # type: str
        self.domain_name = domain_name  # type: str
        self.force_set = force_set  # type: str
        self.owner_id = owner_id  # type: long
        self.private_key = private_key  # type: str
        self.security_token = security_token  # type: str
        self.server_certificate = server_certificate  # type: str
        self.server_certificate_status = server_certificate_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDomainServerCertificateRequest, self).to_map()
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
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.server_certificate is not None:
            result['ServerCertificate'] = self.server_certificate
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
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
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServerCertificate') is not None:
            self.server_certificate = m.get('ServerCertificate')
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        return self


class SetDomainServerCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDomainServerCertificateResponseBody, self).to_map()
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


class SetDomainServerCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDomainServerCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDomainServerCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetDomainServerCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetErrorPageConfigRequest(TeaModel):
    def __init__(self, custom_page_url=None, domain_name=None, owner_id=None, page_type=None, security_token=None):
        self.custom_page_url = custom_page_url  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.page_type = page_type  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetErrorPageConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_page_url is not None:
            result['CustomPageUrl'] = self.custom_page_url
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_type is not None:
            result['PageType'] = self.page_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomPageUrl') is not None:
            self.custom_page_url = m.get('CustomPageUrl')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageType') is not None:
            self.page_type = m.get('PageType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetErrorPageConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetErrorPageConfigResponseBody, self).to_map()
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


class SetErrorPageConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetErrorPageConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetErrorPageConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetErrorPageConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetFileCacheExpiredConfigRequest(TeaModel):
    def __init__(self, cache_content=None, domain_name=None, owner_id=None, security_token=None, ttl=None,
                 weight=None):
        self.cache_content = cache_content  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.ttl = ttl  # type: str
        self.weight = weight  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetFileCacheExpiredConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_content is not None:
            result['CacheContent'] = self.cache_content
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.ttl is not None:
            result['TTL'] = self.ttl
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CacheContent') is not None:
            self.cache_content = m.get('CacheContent')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class SetFileCacheExpiredConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetFileCacheExpiredConfigResponseBody, self).to_map()
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


class SetFileCacheExpiredConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetFileCacheExpiredConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetFileCacheExpiredConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetFileCacheExpiredConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetForceRedirectConfigRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, redirect_type=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.redirect_type = redirect_type  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetForceRedirectConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.redirect_type is not None:
            result['RedirectType'] = self.redirect_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RedirectType') is not None:
            self.redirect_type = m.get('RedirectType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetForceRedirectConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetForceRedirectConfigResponseBody, self).to_map()
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


class SetForceRedirectConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetForceRedirectConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetForceRedirectConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetForceRedirectConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetForwardSchemeConfigRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, enable=None, owner_id=None, scheme_origin=None,
                 scheme_origin_port=None):
        self.config_id = config_id  # type: long
        self.domain_name = domain_name  # type: str
        self.enable = enable  # type: str
        self.owner_id = owner_id  # type: long
        self.scheme_origin = scheme_origin  # type: str
        self.scheme_origin_port = scheme_origin_port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetForwardSchemeConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.scheme_origin is not None:
            result['SchemeOrigin'] = self.scheme_origin
        if self.scheme_origin_port is not None:
            result['SchemeOriginPort'] = self.scheme_origin_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SchemeOrigin') is not None:
            self.scheme_origin = m.get('SchemeOrigin')
        if m.get('SchemeOriginPort') is not None:
            self.scheme_origin_port = m.get('SchemeOriginPort')
        return self


class SetForwardSchemeConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetForwardSchemeConfigResponseBody, self).to_map()
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


class SetForwardSchemeConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetForwardSchemeConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetForwardSchemeConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetForwardSchemeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetHttpErrorPageConfigRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, error_code=None, owner_id=None, page_url=None):
        self.config_id = config_id  # type: long
        self.domain_name = domain_name  # type: str
        self.error_code = error_code  # type: str
        self.owner_id = owner_id  # type: long
        self.page_url = page_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetHttpErrorPageConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_url is not None:
            result['PageUrl'] = self.page_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageUrl') is not None:
            self.page_url = m.get('PageUrl')
        return self


class SetHttpErrorPageConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetHttpErrorPageConfigResponseBody, self).to_map()
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


class SetHttpErrorPageConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetHttpErrorPageConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetHttpErrorPageConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetHttpErrorPageConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetHttpHeaderConfigRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, header_key=None, header_value=None, owner_id=None,
                 security_token=None):
        self.config_id = config_id  # type: long
        self.domain_name = domain_name  # type: str
        self.header_key = header_key  # type: str
        self.header_value = header_value  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetHttpHeaderConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.header_key is not None:
            result['HeaderKey'] = self.header_key
        if self.header_value is not None:
            result['HeaderValue'] = self.header_value
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
        if m.get('HeaderKey') is not None:
            self.header_key = m.get('HeaderKey')
        if m.get('HeaderValue') is not None:
            self.header_value = m.get('HeaderValue')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetHttpHeaderConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetHttpHeaderConfigResponseBody, self).to_map()
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


class SetHttpHeaderConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetHttpHeaderConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetHttpHeaderConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetHttpHeaderConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetHttpsOptionConfigRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, http_2=None, owner_id=None):
        self.config_id = config_id  # type: long
        self.domain_name = domain_name  # type: str
        self.http_2 = http_2  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetHttpsOptionConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.http_2 is not None:
            result['Http2'] = self.http_2
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Http2') is not None:
            self.http_2 = m.get('Http2')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class SetHttpsOptionConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetHttpsOptionConfigResponseBody, self).to_map()
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


class SetHttpsOptionConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetHttpsOptionConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetHttpsOptionConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetHttpsOptionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetIgnoreQueryStringConfigRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, enable=None, hash_key_args=None, keep_oss_args=None,
                 owner_id=None):
        self.config_id = config_id  # type: long
        self.domain_name = domain_name  # type: str
        self.enable = enable  # type: str
        self.hash_key_args = hash_key_args  # type: str
        self.keep_oss_args = keep_oss_args  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetIgnoreQueryStringConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.hash_key_args is not None:
            result['HashKeyArgs'] = self.hash_key_args
        if self.keep_oss_args is not None:
            result['KeepOssArgs'] = self.keep_oss_args
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('HashKeyArgs') is not None:
            self.hash_key_args = m.get('HashKeyArgs')
        if m.get('KeepOssArgs') is not None:
            self.keep_oss_args = m.get('KeepOssArgs')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class SetIgnoreQueryStringConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetIgnoreQueryStringConfigResponseBody, self).to_map()
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


class SetIgnoreQueryStringConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetIgnoreQueryStringConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetIgnoreQueryStringConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetIgnoreQueryStringConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetIpAllowListConfigRequest(TeaModel):
    def __init__(self, allow_ips=None, domain_name=None, owner_id=None, security_token=None):
        self.allow_ips = allow_ips  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetIpAllowListConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_ips is not None:
            result['AllowIps'] = self.allow_ips
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowIps') is not None:
            self.allow_ips = m.get('AllowIps')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetIpAllowListConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetIpAllowListConfigResponseBody, self).to_map()
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


class SetIpAllowListConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetIpAllowListConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetIpAllowListConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetIpAllowListConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetIpBlackListConfigRequest(TeaModel):
    def __init__(self, block_ips=None, config_id=None, domain_name=None, owner_id=None):
        self.block_ips = block_ips  # type: str
        self.config_id = config_id  # type: long
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetIpBlackListConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_ips is not None:
            result['BlockIps'] = self.block_ips
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockIps') is not None:
            self.block_ips = m.get('BlockIps')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class SetIpBlackListConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetIpBlackListConfigResponseBody, self).to_map()
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


class SetIpBlackListConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetIpBlackListConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetIpBlackListConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetIpBlackListConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetOptimizeConfigRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, enable=None, owner_id=None):
        self.config_id = config_id  # type: long
        self.domain_name = domain_name  # type: str
        self.enable = enable  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetOptimizeConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class SetOptimizeConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetOptimizeConfigResponseBody, self).to_map()
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


class SetOptimizeConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetOptimizeConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetOptimizeConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetOptimizeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPageCompressConfigRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, enable=None, owner_id=None):
        self.config_id = config_id  # type: long
        self.domain_name = domain_name  # type: str
        self.enable = enable  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetPageCompressConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class SetPageCompressConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetPageCompressConfigResponseBody, self).to_map()
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


class SetPageCompressConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetPageCompressConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetPageCompressConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetPageCompressConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRangeConfigRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, enable=None, owner_id=None):
        self.config_id = config_id  # type: long
        self.domain_name = domain_name  # type: str
        self.enable = enable  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetRangeConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class SetRangeConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetRangeConfigResponseBody, self).to_map()
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


class SetRangeConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetRangeConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetRangeConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetRangeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRefererConfigRequest(TeaModel):
    def __init__(self, allow_empty=None, disable_ast=None, domain_name=None, owner_id=None, refer_list=None,
                 refer_type=None, security_token=None):
        self.allow_empty = allow_empty  # type: str
        self.disable_ast = disable_ast  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.refer_list = refer_list  # type: str
        self.refer_type = refer_type  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetRefererConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_empty is not None:
            result['AllowEmpty'] = self.allow_empty
        if self.disable_ast is not None:
            result['DisableAst'] = self.disable_ast
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.refer_list is not None:
            result['ReferList'] = self.refer_list
        if self.refer_type is not None:
            result['ReferType'] = self.refer_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowEmpty') is not None:
            self.allow_empty = m.get('AllowEmpty')
        if m.get('DisableAst') is not None:
            self.disable_ast = m.get('DisableAst')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ReferList') is not None:
            self.refer_list = m.get('ReferList')
        if m.get('ReferType') is not None:
            self.refer_type = m.get('ReferType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetRefererConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetRefererConfigResponseBody, self).to_map()
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


class SetRefererConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetRefererConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetRefererConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetRefererConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRemoveQueryStringConfigRequest(TeaModel):
    def __init__(self, ali_remove_args=None, config_id=None, domain_name=None, keep_oss_args=None, owner_id=None):
        self.ali_remove_args = ali_remove_args  # type: str
        self.config_id = config_id  # type: long
        self.domain_name = domain_name  # type: str
        self.keep_oss_args = keep_oss_args  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetRemoveQueryStringConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_remove_args is not None:
            result['AliRemoveArgs'] = self.ali_remove_args
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.keep_oss_args is not None:
            result['KeepOssArgs'] = self.keep_oss_args
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliRemoveArgs') is not None:
            self.ali_remove_args = m.get('AliRemoveArgs')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('KeepOssArgs') is not None:
            self.keep_oss_args = m.get('KeepOssArgs')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class SetRemoveQueryStringConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetRemoveQueryStringConfigResponseBody, self).to_map()
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


class SetRemoveQueryStringConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetRemoveQueryStringConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetRemoveQueryStringConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetRemoveQueryStringConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetReqAuthConfigRequest(TeaModel):
    def __init__(self, auth_remote_desc=None, auth_type=None, domain_name=None, key_1=None, key_2=None,
                 owner_id=None, security_token=None, time_out=None):
        self.auth_remote_desc = auth_remote_desc  # type: str
        self.auth_type = auth_type  # type: str
        self.domain_name = domain_name  # type: str
        self.key_1 = key_1  # type: str
        self.key_2 = key_2  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.time_out = time_out  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetReqAuthConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_remote_desc is not None:
            result['AuthRemoteDesc'] = self.auth_remote_desc
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.key_1 is not None:
            result['Key1'] = self.key_1
        if self.key_2 is not None:
            result['Key2'] = self.key_2
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.time_out is not None:
            result['TimeOut'] = self.time_out
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthRemoteDesc') is not None:
            self.auth_remote_desc = m.get('AuthRemoteDesc')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Key1') is not None:
            self.key_1 = m.get('Key1')
        if m.get('Key2') is not None:
            self.key_2 = m.get('Key2')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TimeOut') is not None:
            self.time_out = m.get('TimeOut')
        return self


class SetReqAuthConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetReqAuthConfigResponseBody, self).to_map()
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


class SetReqAuthConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetReqAuthConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetReqAuthConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetReqAuthConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetReqHeaderConfigRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, key=None, owner_id=None, security_token=None, value=None):
        self.config_id = config_id  # type: long
        self.domain_name = domain_name  # type: str
        self.key = key  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetReqHeaderConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.key is not None:
            result['Key'] = self.key
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SetReqHeaderConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetReqHeaderConfigResponseBody, self).to_map()
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


class SetReqHeaderConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetReqHeaderConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetReqHeaderConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetReqHeaderConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSourceHostConfigRequest(TeaModel):
    def __init__(self, back_src_domain=None, domain_name=None, enable=None, owner_id=None, security_token=None):
        self.back_src_domain = back_src_domain  # type: str
        self.domain_name = domain_name  # type: str
        self.enable = enable  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSourceHostConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.back_src_domain is not None:
            result['BackSrcDomain'] = self.back_src_domain
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackSrcDomain') is not None:
            self.back_src_domain = m.get('BackSrcDomain')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetSourceHostConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSourceHostConfigResponseBody, self).to_map()
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


class SetSourceHostConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetSourceHostConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetSourceHostConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetSourceHostConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetUserGreenManagerConfigRequest(TeaModel):
    def __init__(self, owner_id=None, quota=None, ratio=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.quota = quota  # type: str
        self.ratio = ratio  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetUserGreenManagerConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetUserGreenManagerConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetUserGreenManagerConfigResponseBody, self).to_map()
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


class SetUserGreenManagerConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetUserGreenManagerConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetUserGreenManagerConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetUserGreenManagerConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetWaitingRoomConfigRequest(TeaModel):
    def __init__(self, allow_pct=None, domain_name=None, gap_time=None, max_time_wait=None, owner_id=None,
                 wait_uri=None, wait_url=None):
        self.allow_pct = allow_pct  # type: int
        self.domain_name = domain_name  # type: str
        self.gap_time = gap_time  # type: int
        self.max_time_wait = max_time_wait  # type: int
        self.owner_id = owner_id  # type: long
        self.wait_uri = wait_uri  # type: str
        self.wait_url = wait_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetWaitingRoomConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_pct is not None:
            result['AllowPct'] = self.allow_pct
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.gap_time is not None:
            result['GapTime'] = self.gap_time
        if self.max_time_wait is not None:
            result['MaxTimeWait'] = self.max_time_wait
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.wait_uri is not None:
            result['WaitUri'] = self.wait_uri
        if self.wait_url is not None:
            result['WaitUrl'] = self.wait_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowPct') is not None:
            self.allow_pct = m.get('AllowPct')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GapTime') is not None:
            self.gap_time = m.get('GapTime')
        if m.get('MaxTimeWait') is not None:
            self.max_time_wait = m.get('MaxTimeWait')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('WaitUri') is not None:
            self.wait_uri = m.get('WaitUri')
        if m.get('WaitUrl') is not None:
            self.wait_url = m.get('WaitUrl')
        return self


class SetWaitingRoomConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetWaitingRoomConfigResponseBody, self).to_map()
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


class SetWaitingRoomConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetWaitingRoomConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetWaitingRoomConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetWaitingRoomConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartCdnDomainRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartCdnDomainRequest, self).to_map()
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


class StartCdnDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartCdnDomainResponseBody, self).to_map()
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


class StartCdnDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartCdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartCdnDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopCdnDomainRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopCdnDomainRequest, self).to_map()
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


class StopCdnDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopCdnDomainResponseBody, self).to_map()
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


class StopCdnDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopCdnDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopCdnDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopCdnDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesRequestTag, self).to_map()
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


class TagResourcesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_id=None, resource_type=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
        self.tag = tag  # type: list[TagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TagResourcesRequest, self).to_map()
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
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
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


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, owner_id=None, resource_id=None, resource_type=None, tag_key=None):
        self.all = all  # type: bool
        self.owner_id = owner_id  # type: long
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
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


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
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


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UntagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCdnDeliverTaskRequest(TeaModel):
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
        _map = super(UpdateCdnDeliverTaskRequest, self).to_map()
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


class UpdateCdnDeliverTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCdnDeliverTaskResponseBody, self).to_map()
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


class UpdateCdnDeliverTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateCdnDeliverTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCdnDeliverTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateCdnDeliverTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCdnSubTaskRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, report_ids=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.report_ids = report_ids  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCdnSubTaskRequest, self).to_map()
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


class UpdateCdnSubTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCdnSubTaskResponseBody, self).to_map()
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


class UpdateCdnSubTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateCdnSubTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCdnSubTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateCdnSubTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFCTriggerRequest(TeaModel):
    def __init__(self, function_arn=None, notes=None, owner_id=None, role_arn=None, source_arn=None,
                 trigger_arn=None):
        self.function_arn = function_arn  # type: str
        self.notes = notes  # type: str
        self.owner_id = owner_id  # type: long
        self.role_arn = role_arn  # type: str
        self.source_arn = source_arn  # type: str
        self.trigger_arn = trigger_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFCTriggerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_arn is not None:
            result['FunctionARN'] = self.function_arn
        if self.notes is not None:
            result['Notes'] = self.notes
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn
        if self.source_arn is not None:
            result['SourceARN'] = self.source_arn
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FunctionARN') is not None:
            self.function_arn = m.get('FunctionARN')
        if m.get('Notes') is not None:
            self.notes = m.get('Notes')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')
        if m.get('SourceARN') is not None:
            self.source_arn = m.get('SourceARN')
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')
        return self


class UpdateFCTriggerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFCTriggerResponseBody, self).to_map()
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


class UpdateFCTriggerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateFCTriggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFCTriggerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateFCTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyDomainOwnerRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, verify_type=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.verify_type = verify_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyDomainOwnerRequest, self).to_map()
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


class VerifyDomainOwnerResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyDomainOwnerResponseBody, self).to_map()
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


class VerifyDomainOwnerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: VerifyDomainOwnerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyDomainOwnerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = VerifyDomainOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


