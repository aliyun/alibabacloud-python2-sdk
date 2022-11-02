# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ClearMajorProtectionBlackIpRequest(TeaModel):
    def __init__(self, instance_id=None, rule_id=None, template_id=None):
        self.instance_id = instance_id  # type: str
        self.rule_id = rule_id  # type: long
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClearMajorProtectionBlackIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ClearMajorProtectionBlackIpResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClearMajorProtectionBlackIpResponseBody, self).to_map()
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


class ClearMajorProtectionBlackIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ClearMajorProtectionBlackIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ClearMajorProtectionBlackIpResponse, self).to_map()
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
            temp_model = ClearMajorProtectionBlackIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDefenseResourceGroupRequest(TeaModel):
    def __init__(self, add_list=None, description=None, group_name=None, instance_id=None):
        self.add_list = add_list  # type: str
        self.description = description  # type: str
        self.group_name = group_name  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDefenseResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_list is not None:
            result['AddList'] = self.add_list
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddList') is not None:
            self.add_list = m.get('AddList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateDefenseResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDefenseResourceGroupResponseBody, self).to_map()
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


class CreateDefenseResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDefenseResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDefenseResourceGroupResponse, self).to_map()
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
            temp_model = CreateDefenseResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDefenseRuleRequest(TeaModel):
    def __init__(self, defense_scene=None, instance_id=None, rules=None, template_id=None):
        self.defense_scene = defense_scene  # type: str
        self.instance_id = instance_id  # type: str
        self.rules = rules  # type: str
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDefenseRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateDefenseRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDefenseRuleResponseBody, self).to_map()
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


class CreateDefenseRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDefenseRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDefenseRuleResponse, self).to_map()
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
            temp_model = CreateDefenseRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDefenseTemplateRequest(TeaModel):
    def __init__(self, defense_scene=None, description=None, instance_id=None, template_name=None,
                 template_origin=None, template_status=None, template_type=None):
        self.defense_scene = defense_scene  # type: str
        self.description = description  # type: str
        self.instance_id = instance_id  # type: str
        self.template_name = template_name  # type: str
        self.template_origin = template_origin  # type: str
        self.template_status = template_status  # type: int
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDefenseTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_origin is not None:
            result['TemplateOrigin'] = self.template_origin
        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateOrigin') is not None:
            self.template_origin = m.get('TemplateOrigin')
        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class CreateDefenseTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_id=None):
        self.request_id = request_id  # type: str
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDefenseTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateDefenseTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDefenseTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDefenseTemplateResponse, self).to_map()
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
            temp_model = CreateDefenseTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainRequestListen(TeaModel):
    def __init__(self, cert_id=None, cipher_suite=None, custom_ciphers=None, enable_tlsv_3=None, exclusive_ip=None,
                 focus_https=None, http_2enabled=None, http_ports=None, https_ports=None, ipv_6enabled=None,
                 protection_resource=None, tlsversion=None, xff_header_mode=None, xff_headers=None):
        self.cert_id = cert_id  # type: str
        self.cipher_suite = cipher_suite  # type: int
        self.custom_ciphers = custom_ciphers  # type: list[str]
        self.enable_tlsv_3 = enable_tlsv_3  # type: bool
        self.exclusive_ip = exclusive_ip  # type: bool
        self.focus_https = focus_https  # type: bool
        self.http_2enabled = http_2enabled  # type: bool
        self.http_ports = http_ports  # type: list[int]
        self.https_ports = https_ports  # type: list[int]
        self.ipv_6enabled = ipv_6enabled  # type: bool
        self.protection_resource = protection_resource  # type: str
        self.tlsversion = tlsversion  # type: str
        self.xff_header_mode = xff_header_mode  # type: int
        self.xff_headers = xff_headers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDomainRequestListen, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cipher_suite is not None:
            result['CipherSuite'] = self.cipher_suite
        if self.custom_ciphers is not None:
            result['CustomCiphers'] = self.custom_ciphers
        if self.enable_tlsv_3 is not None:
            result['EnableTLSv3'] = self.enable_tlsv_3
        if self.exclusive_ip is not None:
            result['ExclusiveIp'] = self.exclusive_ip
        if self.focus_https is not None:
            result['FocusHttps'] = self.focus_https
        if self.http_2enabled is not None:
            result['Http2Enabled'] = self.http_2enabled
        if self.http_ports is not None:
            result['HttpPorts'] = self.http_ports
        if self.https_ports is not None:
            result['HttpsPorts'] = self.https_ports
        if self.ipv_6enabled is not None:
            result['IPv6Enabled'] = self.ipv_6enabled
        if self.protection_resource is not None:
            result['ProtectionResource'] = self.protection_resource
        if self.tlsversion is not None:
            result['TLSVersion'] = self.tlsversion
        if self.xff_header_mode is not None:
            result['XffHeaderMode'] = self.xff_header_mode
        if self.xff_headers is not None:
            result['XffHeaders'] = self.xff_headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CipherSuite') is not None:
            self.cipher_suite = m.get('CipherSuite')
        if m.get('CustomCiphers') is not None:
            self.custom_ciphers = m.get('CustomCiphers')
        if m.get('EnableTLSv3') is not None:
            self.enable_tlsv_3 = m.get('EnableTLSv3')
        if m.get('ExclusiveIp') is not None:
            self.exclusive_ip = m.get('ExclusiveIp')
        if m.get('FocusHttps') is not None:
            self.focus_https = m.get('FocusHttps')
        if m.get('Http2Enabled') is not None:
            self.http_2enabled = m.get('Http2Enabled')
        if m.get('HttpPorts') is not None:
            self.http_ports = m.get('HttpPorts')
        if m.get('HttpsPorts') is not None:
            self.https_ports = m.get('HttpsPorts')
        if m.get('IPv6Enabled') is not None:
            self.ipv_6enabled = m.get('IPv6Enabled')
        if m.get('ProtectionResource') is not None:
            self.protection_resource = m.get('ProtectionResource')
        if m.get('TLSVersion') is not None:
            self.tlsversion = m.get('TLSVersion')
        if m.get('XffHeaderMode') is not None:
            self.xff_header_mode = m.get('XffHeaderMode')
        if m.get('XffHeaders') is not None:
            self.xff_headers = m.get('XffHeaders')
        return self


class CreateDomainRequestRedirectRequestHeaders(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDomainRequestRedirectRequestHeaders, self).to_map()
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


class CreateDomainRequestRedirect(TeaModel):
    def __init__(self, backends=None, connect_timeout=None, focus_http_backend=None, loadbalance=None,
                 read_timeout=None, request_headers=None, sni_enabled=None, sni_host=None, write_timeout=None):
        self.backends = backends  # type: list[str]
        self.connect_timeout = connect_timeout  # type: int
        self.focus_http_backend = focus_http_backend  # type: bool
        self.loadbalance = loadbalance  # type: str
        self.read_timeout = read_timeout  # type: int
        self.request_headers = request_headers  # type: list[CreateDomainRequestRedirectRequestHeaders]
        self.sni_enabled = sni_enabled  # type: bool
        self.sni_host = sni_host  # type: str
        self.write_timeout = write_timeout  # type: int

    def validate(self):
        if self.request_headers:
            for k in self.request_headers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateDomainRequestRedirect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backends is not None:
            result['Backends'] = self.backends
        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout
        if self.focus_http_backend is not None:
            result['FocusHttpBackend'] = self.focus_http_backend
        if self.loadbalance is not None:
            result['Loadbalance'] = self.loadbalance
        if self.read_timeout is not None:
            result['ReadTimeout'] = self.read_timeout
        result['RequestHeaders'] = []
        if self.request_headers is not None:
            for k in self.request_headers:
                result['RequestHeaders'].append(k.to_map() if k else None)
        if self.sni_enabled is not None:
            result['SniEnabled'] = self.sni_enabled
        if self.sni_host is not None:
            result['SniHost'] = self.sni_host
        if self.write_timeout is not None:
            result['WriteTimeout'] = self.write_timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Backends') is not None:
            self.backends = m.get('Backends')
        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')
        if m.get('FocusHttpBackend') is not None:
            self.focus_http_backend = m.get('FocusHttpBackend')
        if m.get('Loadbalance') is not None:
            self.loadbalance = m.get('Loadbalance')
        if m.get('ReadTimeout') is not None:
            self.read_timeout = m.get('ReadTimeout')
        self.request_headers = []
        if m.get('RequestHeaders') is not None:
            for k in m.get('RequestHeaders'):
                temp_model = CreateDomainRequestRedirectRequestHeaders()
                self.request_headers.append(temp_model.from_map(k))
        if m.get('SniEnabled') is not None:
            self.sni_enabled = m.get('SniEnabled')
        if m.get('SniHost') is not None:
            self.sni_host = m.get('SniHost')
        if m.get('WriteTimeout') is not None:
            self.write_timeout = m.get('WriteTimeout')
        return self


class CreateDomainRequest(TeaModel):
    def __init__(self, access_type=None, domain=None, instance_id=None, listen=None, redirect=None, region_id=None):
        self.access_type = access_type  # type: str
        self.domain = domain  # type: str
        self.instance_id = instance_id  # type: str
        self.listen = listen  # type: CreateDomainRequestListen
        self.redirect = redirect  # type: CreateDomainRequestRedirect
        self.region_id = region_id  # type: str

    def validate(self):
        if self.listen:
            self.listen.validate()
        if self.redirect:
            self.redirect.validate()

    def to_map(self):
        _map = super(CreateDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.listen is not None:
            result['Listen'] = self.listen.to_map()
        if self.redirect is not None:
            result['Redirect'] = self.redirect.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Listen') is not None:
            temp_model = CreateDomainRequestListen()
            self.listen = temp_model.from_map(m['Listen'])
        if m.get('Redirect') is not None:
            temp_model = CreateDomainRequestRedirect()
            self.redirect = temp_model.from_map(m['Redirect'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateDomainShrinkRequest(TeaModel):
    def __init__(self, access_type=None, domain=None, instance_id=None, listen_shrink=None, redirect_shrink=None,
                 region_id=None):
        self.access_type = access_type  # type: str
        self.domain = domain  # type: str
        self.instance_id = instance_id  # type: str
        self.listen_shrink = listen_shrink  # type: str
        self.redirect_shrink = redirect_shrink  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDomainShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.listen_shrink is not None:
            result['Listen'] = self.listen_shrink
        if self.redirect_shrink is not None:
            result['Redirect'] = self.redirect_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Listen') is not None:
            self.listen_shrink = m.get('Listen')
        if m.get('Redirect') is not None:
            self.redirect_shrink = m.get('Redirect')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateDomainResponseBodyDomainInfo(TeaModel):
    def __init__(self, cname=None, domain=None):
        self.cname = cname  # type: str
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDomainResponseBodyDomainInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class CreateDomainResponseBody(TeaModel):
    def __init__(self, domain_info=None, request_id=None):
        self.domain_info = domain_info  # type: CreateDomainResponseBodyDomainInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_info:
            self.domain_info.validate()

    def to_map(self):
        _map = super(CreateDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_info is not None:
            result['DomainInfo'] = self.domain_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainInfo') is not None:
            temp_model = CreateDomainResponseBodyDomainInfo()
            self.domain_info = temp_model.from_map(m['DomainInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDomainResponse, self).to_map()
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
            temp_model = CreateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMajorProtectionBlackIpRequest(TeaModel):
    def __init__(self, description=None, expired_time=None, instance_id=None, ip_list=None, rule_id=None,
                 template_id=None):
        self.description = description  # type: str
        self.expired_time = expired_time  # type: long
        self.instance_id = instance_id  # type: str
        self.ip_list = ip_list  # type: str
        self.rule_id = rule_id  # type: long
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMajorProtectionBlackIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateMajorProtectionBlackIpResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMajorProtectionBlackIpResponseBody, self).to_map()
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


class CreateMajorProtectionBlackIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateMajorProtectionBlackIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateMajorProtectionBlackIpResponse, self).to_map()
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
            temp_model = CreateMajorProtectionBlackIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDefenseResourceGroupRequest(TeaModel):
    def __init__(self, group_name=None, instance_id=None):
        self.group_name = group_name  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDefenseResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteDefenseResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDefenseResourceGroupResponseBody, self).to_map()
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


class DeleteDefenseResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDefenseResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDefenseResourceGroupResponse, self).to_map()
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
            temp_model = DeleteDefenseResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDefenseRuleRequest(TeaModel):
    def __init__(self, instance_id=None, rule_ids=None, template_id=None):
        self.instance_id = instance_id  # type: str
        self.rule_ids = rule_ids  # type: str
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDefenseRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteDefenseRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDefenseRuleResponseBody, self).to_map()
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


class DeleteDefenseRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDefenseRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDefenseRuleResponse, self).to_map()
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
            temp_model = DeleteDefenseRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDefenseTemplateRequest(TeaModel):
    def __init__(self, instance_id=None, template_id=None):
        self.instance_id = instance_id  # type: str
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDefenseTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteDefenseTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDefenseTemplateResponseBody, self).to_map()
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


class DeleteDefenseTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDefenseTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDefenseTemplateResponse, self).to_map()
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
            temp_model = DeleteDefenseTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(self, domain=None, instance_id=None, region_id=None):
        self.domain = domain  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainResponseBody, self).to_map()
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


class DeleteDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMajorProtectionBlackIpRequest(TeaModel):
    def __init__(self, instance_id=None, ip_list=None, rule_id=None, template_id=None):
        self.instance_id = instance_id  # type: str
        self.ip_list = ip_list  # type: str
        self.rule_id = rule_id  # type: long
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMajorProtectionBlackIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteMajorProtectionBlackIpResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMajorProtectionBlackIpResponseBody, self).to_map()
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


class DeleteMajorProtectionBlackIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteMajorProtectionBlackIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMajorProtectionBlackIpResponse, self).to_map()
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
            temp_model = DeleteMajorProtectionBlackIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDefenseResourceGroupRequest(TeaModel):
    def __init__(self, group_name=None, instance_id=None):
        self.group_name = group_name  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefenseResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeDefenseResourceGroupResponseBodyGroup(TeaModel):
    def __init__(self, description=None, gmt_create=None, gmt_modified=None, group_name=None, resource_list=None):
        self.description = description  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.group_name = group_name  # type: str
        self.resource_list = resource_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefenseResourceGroupResponseBodyGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.resource_list is not None:
            result['ResourceList'] = self.resource_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ResourceList') is not None:
            self.resource_list = m.get('ResourceList')
        return self


class DescribeDefenseResourceGroupResponseBody(TeaModel):
    def __init__(self, group=None, request_id=None):
        self.group = group  # type: DescribeDefenseResourceGroupResponseBodyGroup
        self.request_id = request_id  # type: str

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        _map = super(DescribeDefenseResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['Group'] = self.group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Group') is not None:
            temp_model = DescribeDefenseResourceGroupResponseBodyGroup()
            self.group = temp_model.from_map(m['Group'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDefenseResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDefenseResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDefenseResourceGroupResponse, self).to_map()
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
            temp_model = DescribeDefenseResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDefenseResourcesRequest(TeaModel):
    def __init__(self, instance_id=None, page_number=None, page_size=None, query=None):
        self.instance_id = instance_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.query = query  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefenseResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class DescribeDefenseResourcesResponseBodyResources(TeaModel):
    def __init__(self, custom_headers=None, description=None, detail=None, gmt_create=None, gmt_modified=None,
                 pattern=None, product=None, resource=None, resource_group=None, resource_origin=None, xff_status=None):
        self.custom_headers = custom_headers  # type: list[str]
        self.description = description  # type: str
        self.detail = detail  # type: dict[str, any]
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.pattern = pattern  # type: str
        self.product = product  # type: str
        self.resource = resource  # type: str
        self.resource_group = resource_group  # type: str
        self.resource_origin = resource_origin  # type: str
        self.xff_status = xff_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefenseResourcesResponseBodyResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_headers is not None:
            result['CustomHeaders'] = self.custom_headers
        if self.description is not None:
            result['Description'] = self.description
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.pattern is not None:
            result['Pattern'] = self.pattern
        if self.product is not None:
            result['Product'] = self.product
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.resource_origin is not None:
            result['ResourceOrigin'] = self.resource_origin
        if self.xff_status is not None:
            result['XffStatus'] = self.xff_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomHeaders') is not None:
            self.custom_headers = m.get('CustomHeaders')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('ResourceOrigin') is not None:
            self.resource_origin = m.get('ResourceOrigin')
        if m.get('XffStatus') is not None:
            self.xff_status = m.get('XffStatus')
        return self


class DescribeDefenseResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, resources=None, total_count=None):
        self.request_id = request_id  # type: str
        self.resources = resources  # type: list[DescribeDefenseResourcesResponseBodyResources]
        self.total_count = total_count  # type: long

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDefenseResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = DescribeDefenseResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDefenseResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDefenseResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDefenseResourcesResponse, self).to_map()
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
            temp_model = DescribeDefenseResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDefenseRuleRequest(TeaModel):
    def __init__(self, instance_id=None, rule_id=None, template_id=None):
        self.instance_id = instance_id  # type: str
        self.rule_id = rule_id  # type: long
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefenseRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeDefenseRuleResponseBodyRule(TeaModel):
    def __init__(self, config=None, defense_origin=None, defense_scene=None, gmt_modified=None, rule_id=None,
                 rule_name=None, status=None, template_id=None):
        self.config = config  # type: str
        self.defense_origin = defense_origin  # type: str
        self.defense_scene = defense_scene  # type: str
        self.gmt_modified = gmt_modified  # type: long
        self.rule_id = rule_id  # type: long
        self.rule_name = rule_name  # type: str
        self.status = status  # type: int
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefenseRuleResponseBodyRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.defense_origin is not None:
            result['DefenseOrigin'] = self.defense_origin
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DefenseOrigin') is not None:
            self.defense_origin = m.get('DefenseOrigin')
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeDefenseRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, rule=None):
        self.request_id = request_id  # type: str
        self.rule = rule  # type: DescribeDefenseRuleResponseBodyRule

    def validate(self):
        if self.rule:
            self.rule.validate()

    def to_map(self):
        _map = super(DescribeDefenseRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule is not None:
            result['Rule'] = self.rule.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rule') is not None:
            temp_model = DescribeDefenseRuleResponseBodyRule()
            self.rule = temp_model.from_map(m['Rule'])
        return self


class DescribeDefenseRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDefenseRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDefenseRuleResponse, self).to_map()
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
            temp_model = DescribeDefenseRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDefenseRulesRequest(TeaModel):
    def __init__(self, instance_id=None, page_number=None, page_size=None, query=None, rule_type=None):
        self.instance_id = instance_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.query = query  # type: str
        self.rule_type = rule_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefenseRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class DescribeDefenseRulesResponseBodyRules(TeaModel):
    def __init__(self, config=None, defense_origin=None, defense_scene=None, gmt_modified=None, rule_id=None,
                 rule_name=None, status=None, template_id=None):
        self.config = config  # type: str
        self.defense_origin = defense_origin  # type: str
        self.defense_scene = defense_scene  # type: str
        self.gmt_modified = gmt_modified  # type: long
        self.rule_id = rule_id  # type: long
        self.rule_name = rule_name  # type: str
        self.status = status  # type: int
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefenseRulesResponseBodyRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.defense_origin is not None:
            result['DefenseOrigin'] = self.defense_origin
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('DefenseOrigin') is not None:
            self.defense_origin = m.get('DefenseOrigin')
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeDefenseRulesResponseBody(TeaModel):
    def __init__(self, request_id=None, rules=None, total_count=None):
        self.request_id = request_id  # type: str
        self.rules = rules  # type: list[DescribeDefenseRulesResponseBodyRules]
        self.total_count = total_count  # type: long

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDefenseRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeDefenseRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDefenseRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDefenseRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDefenseRulesResponse, self).to_map()
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
            temp_model = DescribeDefenseRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDefenseTemplateRequest(TeaModel):
    def __init__(self, instance_id=None, template_id=None):
        self.instance_id = instance_id  # type: str
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefenseTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeDefenseTemplateResponseBodyTemplate(TeaModel):
    def __init__(self, defense_scene=None, description=None, gmt_modified=None, template_id=None,
                 template_name=None, template_origin=None, template_status=None, template_type=None):
        self.defense_scene = defense_scene  # type: str
        self.description = description  # type: str
        self.gmt_modified = gmt_modified  # type: long
        self.template_id = template_id  # type: long
        self.template_name = template_name  # type: str
        self.template_origin = template_origin  # type: str
        self.template_status = template_status  # type: int
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefenseTemplateResponseBodyTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_origin is not None:
            result['TemplateOrigin'] = self.template_origin
        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateOrigin') is not None:
            self.template_origin = m.get('TemplateOrigin')
        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class DescribeDefenseTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template=None):
        self.request_id = request_id  # type: str
        self.template = template  # type: DescribeDefenseTemplateResponseBodyTemplate

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super(DescribeDefenseTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = DescribeDefenseTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class DescribeDefenseTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDefenseTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDefenseTemplateResponse, self).to_map()
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
            temp_model = DescribeDefenseTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainDetailRequest(TeaModel):
    def __init__(self, domain=None, instance_id=None):
        self.domain = domain  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeDomainDetailResponseBodyListen(TeaModel):
    def __init__(self, cert_id=None, cipher_suite=None, custom_ciphers=None, enable_tlsv_3=None, exclusive_ip=None,
                 focus_https=None, http_2enabled=None, http_ports=None, https_ports=None, ipv_6enabled=None,
                 protection_resource=None, tlsversion=None, xff_header_mode=None, xff_headers=None):
        self.cert_id = cert_id  # type: long
        self.cipher_suite = cipher_suite  # type: long
        self.custom_ciphers = custom_ciphers  # type: list[str]
        self.enable_tlsv_3 = enable_tlsv_3  # type: bool
        self.exclusive_ip = exclusive_ip  # type: bool
        self.focus_https = focus_https  # type: bool
        self.http_2enabled = http_2enabled  # type: bool
        self.http_ports = http_ports  # type: list[long]
        self.https_ports = https_ports  # type: list[long]
        self.ipv_6enabled = ipv_6enabled  # type: bool
        self.protection_resource = protection_resource  # type: str
        self.tlsversion = tlsversion  # type: str
        self.xff_header_mode = xff_header_mode  # type: long
        self.xff_headers = xff_headers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainDetailResponseBodyListen, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cipher_suite is not None:
            result['CipherSuite'] = self.cipher_suite
        if self.custom_ciphers is not None:
            result['CustomCiphers'] = self.custom_ciphers
        if self.enable_tlsv_3 is not None:
            result['EnableTLSv3'] = self.enable_tlsv_3
        if self.exclusive_ip is not None:
            result['ExclusiveIp'] = self.exclusive_ip
        if self.focus_https is not None:
            result['FocusHttps'] = self.focus_https
        if self.http_2enabled is not None:
            result['Http2Enabled'] = self.http_2enabled
        if self.http_ports is not None:
            result['HttpPorts'] = self.http_ports
        if self.https_ports is not None:
            result['HttpsPorts'] = self.https_ports
        if self.ipv_6enabled is not None:
            result['IPv6Enabled'] = self.ipv_6enabled
        if self.protection_resource is not None:
            result['ProtectionResource'] = self.protection_resource
        if self.tlsversion is not None:
            result['TLSVersion'] = self.tlsversion
        if self.xff_header_mode is not None:
            result['XffHeaderMode'] = self.xff_header_mode
        if self.xff_headers is not None:
            result['XffHeaders'] = self.xff_headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CipherSuite') is not None:
            self.cipher_suite = m.get('CipherSuite')
        if m.get('CustomCiphers') is not None:
            self.custom_ciphers = m.get('CustomCiphers')
        if m.get('EnableTLSv3') is not None:
            self.enable_tlsv_3 = m.get('EnableTLSv3')
        if m.get('ExclusiveIp') is not None:
            self.exclusive_ip = m.get('ExclusiveIp')
        if m.get('FocusHttps') is not None:
            self.focus_https = m.get('FocusHttps')
        if m.get('Http2Enabled') is not None:
            self.http_2enabled = m.get('Http2Enabled')
        if m.get('HttpPorts') is not None:
            self.http_ports = m.get('HttpPorts')
        if m.get('HttpsPorts') is not None:
            self.https_ports = m.get('HttpsPorts')
        if m.get('IPv6Enabled') is not None:
            self.ipv_6enabled = m.get('IPv6Enabled')
        if m.get('ProtectionResource') is not None:
            self.protection_resource = m.get('ProtectionResource')
        if m.get('TLSVersion') is not None:
            self.tlsversion = m.get('TLSVersion')
        if m.get('XffHeaderMode') is not None:
            self.xff_header_mode = m.get('XffHeaderMode')
        if m.get('XffHeaders') is not None:
            self.xff_headers = m.get('XffHeaders')
        return self


class DescribeDomainDetailResponseBodyRedirectBackends(TeaModel):
    def __init__(self, backend=None):
        self.backend = backend  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainDetailResponseBodyRedirectBackends, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend is not None:
            result['Backend'] = self.backend
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Backend') is not None:
            self.backend = m.get('Backend')
        return self


class DescribeDomainDetailResponseBodyRedirectRequestHeaders(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainDetailResponseBodyRedirectRequestHeaders, self).to_map()
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


class DescribeDomainDetailResponseBodyRedirect(TeaModel):
    def __init__(self, backends=None, connect_timeout=None, focus_http_backend=None, loadbalance=None,
                 read_timeout=None, request_headers=None, sni_enabled=None, sni_host=None, write_timeout=None):
        self.backends = backends  # type: list[DescribeDomainDetailResponseBodyRedirectBackends]
        self.connect_timeout = connect_timeout  # type: int
        self.focus_http_backend = focus_http_backend  # type: bool
        self.loadbalance = loadbalance  # type: str
        self.read_timeout = read_timeout  # type: int
        self.request_headers = request_headers  # type: list[DescribeDomainDetailResponseBodyRedirectRequestHeaders]
        self.sni_enabled = sni_enabled  # type: bool
        self.sni_host = sni_host  # type: str
        self.write_timeout = write_timeout  # type: int

    def validate(self):
        if self.backends:
            for k in self.backends:
                if k:
                    k.validate()
        if self.request_headers:
            for k in self.request_headers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainDetailResponseBodyRedirect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Backends'] = []
        if self.backends is not None:
            for k in self.backends:
                result['Backends'].append(k.to_map() if k else None)
        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout
        if self.focus_http_backend is not None:
            result['FocusHttpBackend'] = self.focus_http_backend
        if self.loadbalance is not None:
            result['Loadbalance'] = self.loadbalance
        if self.read_timeout is not None:
            result['ReadTimeout'] = self.read_timeout
        result['RequestHeaders'] = []
        if self.request_headers is not None:
            for k in self.request_headers:
                result['RequestHeaders'].append(k.to_map() if k else None)
        if self.sni_enabled is not None:
            result['SniEnabled'] = self.sni_enabled
        if self.sni_host is not None:
            result['SniHost'] = self.sni_host
        if self.write_timeout is not None:
            result['WriteTimeout'] = self.write_timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.backends = []
        if m.get('Backends') is not None:
            for k in m.get('Backends'):
                temp_model = DescribeDomainDetailResponseBodyRedirectBackends()
                self.backends.append(temp_model.from_map(k))
        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')
        if m.get('FocusHttpBackend') is not None:
            self.focus_http_backend = m.get('FocusHttpBackend')
        if m.get('Loadbalance') is not None:
            self.loadbalance = m.get('Loadbalance')
        if m.get('ReadTimeout') is not None:
            self.read_timeout = m.get('ReadTimeout')
        self.request_headers = []
        if m.get('RequestHeaders') is not None:
            for k in m.get('RequestHeaders'):
                temp_model = DescribeDomainDetailResponseBodyRedirectRequestHeaders()
                self.request_headers.append(temp_model.from_map(k))
        if m.get('SniEnabled') is not None:
            self.sni_enabled = m.get('SniEnabled')
        if m.get('SniHost') is not None:
            self.sni_host = m.get('SniHost')
        if m.get('WriteTimeout') is not None:
            self.write_timeout = m.get('WriteTimeout')
        return self


class DescribeDomainDetailResponseBody(TeaModel):
    def __init__(self, cname=None, domain=None, listen=None, redirect=None, request_id=None, status=None):
        self.cname = cname  # type: str
        self.domain = domain  # type: str
        self.listen = listen  # type: DescribeDomainDetailResponseBodyListen
        self.redirect = redirect  # type: DescribeDomainDetailResponseBodyRedirect
        self.request_id = request_id  # type: str
        self.status = status  # type: long

    def validate(self):
        if self.listen:
            self.listen.validate()
        if self.redirect:
            self.redirect.validate()

    def to_map(self):
        _map = super(DescribeDomainDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.listen is not None:
            result['Listen'] = self.listen.to_map()
        if self.redirect is not None:
            result['Redirect'] = self.redirect.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Listen') is not None:
            temp_model = DescribeDomainDetailResponseBodyListen()
            self.listen = temp_model.from_map(m['Listen'])
        if m.get('Redirect') is not None:
            temp_model = DescribeDomainDetailResponseBodyRedirect()
            self.redirect = temp_model.from_map(m['Redirect'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDomainDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainDetailResponse, self).to_map()
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
            temp_model = DescribeDomainDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainsRequest(TeaModel):
    def __init__(self, backend=None, domain=None, instance_id=None, page_number=None, page_size=None):
        self.backend = backend  # type: str
        self.domain = domain  # type: str
        self.instance_id = instance_id  # type: str
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend is not None:
            result['Backend'] = self.backend
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Backend') is not None:
            self.backend = m.get('Backend')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDomainsResponseBodyDomainsBackedsHttp(TeaModel):
    def __init__(self, backend=None):
        self.backend = backend  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainsResponseBodyDomainsBackedsHttp, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend is not None:
            result['Backend'] = self.backend
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Backend') is not None:
            self.backend = m.get('Backend')
        return self


class DescribeDomainsResponseBodyDomainsBackedsHttps(TeaModel):
    def __init__(self, backend=None):
        self.backend = backend  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainsResponseBodyDomainsBackedsHttps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend is not None:
            result['Backend'] = self.backend
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Backend') is not None:
            self.backend = m.get('Backend')
        return self


class DescribeDomainsResponseBodyDomainsBackeds(TeaModel):
    def __init__(self, http=None, https=None):
        self.http = http  # type: list[DescribeDomainsResponseBodyDomainsBackedsHttp]
        self.https = https  # type: list[DescribeDomainsResponseBodyDomainsBackedsHttps]

    def validate(self):
        if self.http:
            for k in self.http:
                if k:
                    k.validate()
        if self.https:
            for k in self.https:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainsResponseBodyDomainsBackeds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Http'] = []
        if self.http is not None:
            for k in self.http:
                result['Http'].append(k.to_map() if k else None)
        result['Https'] = []
        if self.https is not None:
            for k in self.https:
                result['Https'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.http = []
        if m.get('Http') is not None:
            for k in m.get('Http'):
                temp_model = DescribeDomainsResponseBodyDomainsBackedsHttp()
                self.http.append(temp_model.from_map(k))
        self.https = []
        if m.get('Https') is not None:
            for k in m.get('Https'):
                temp_model = DescribeDomainsResponseBodyDomainsBackedsHttps()
                self.https.append(temp_model.from_map(k))
        return self


class DescribeDomainsResponseBodyDomainsListenPorts(TeaModel):
    def __init__(self, http=None, https=None):
        self.http = http  # type: list[long]
        self.https = https  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainsResponseBodyDomainsListenPorts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http is not None:
            result['Http'] = self.http
        if self.https is not None:
            result['Https'] = self.https
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Http') is not None:
            self.http = m.get('Http')
        if m.get('Https') is not None:
            self.https = m.get('Https')
        return self


class DescribeDomainsResponseBodyDomains(TeaModel):
    def __init__(self, backeds=None, cname=None, domain=None, listen_ports=None, status=None):
        self.backeds = backeds  # type: DescribeDomainsResponseBodyDomainsBackeds
        self.cname = cname  # type: str
        self.domain = domain  # type: str
        self.listen_ports = listen_ports  # type: DescribeDomainsResponseBodyDomainsListenPorts
        self.status = status  # type: int

    def validate(self):
        if self.backeds:
            self.backeds.validate()
        if self.listen_ports:
            self.listen_ports.validate()

    def to_map(self):
        _map = super(DescribeDomainsResponseBodyDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backeds is not None:
            result['Backeds'] = self.backeds.to_map()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.listen_ports is not None:
            result['ListenPorts'] = self.listen_ports.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Backeds') is not None:
            temp_model = DescribeDomainsResponseBodyDomainsBackeds()
            self.backeds = temp_model.from_map(m['Backeds'])
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ListenPorts') is not None:
            temp_model = DescribeDomainsResponseBodyDomainsListenPorts()
            self.listen_ports = temp_model.from_map(m['ListenPorts'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDomainsResponseBody(TeaModel):
    def __init__(self, domains=None, request_id=None, total_count=None):
        self.domains = domains  # type: list[DescribeDomainsResponseBodyDomains]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = DescribeDomainsResponseBodyDomains()
                self.domains.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDomainsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowChartRequest(TeaModel):
    def __init__(self, end_timestamp=None, instance_id=None, interval=None, resource=None, start_timestamp=None):
        self.end_timestamp = end_timestamp  # type: str
        self.instance_id = instance_id  # type: str
        self.interval = interval  # type: str
        self.resource = resource  # type: str
        self.start_timestamp = start_timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowChartRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeFlowChartResponseBodyFlowChart(TeaModel):
    def __init__(self, acl_custom_block_sum=None, acl_custom_reports_sum=None, anti_scan_block_sum=None,
                 antibot_block_sum=None, antibot_report_sum=None, antiscan_reports_sum=None, blacklist_block_sum=None,
                 blacklist_reports_sum=None, cc_custom_block_sum=None, cc_custom_reports_sum=None, cc_system_blocks_sum=None,
                 cc_system_reports_sum=None, count=None, in_bytes=None, index=None, max_pv=None, out_bytes=None,
                 region_block_blocks_sum=None, region_block_reports_sum=None, waf_block_sum=None, waf_report_sum=None):
        self.acl_custom_block_sum = acl_custom_block_sum  # type: long
        self.acl_custom_reports_sum = acl_custom_reports_sum  # type: long
        self.anti_scan_block_sum = anti_scan_block_sum  # type: long
        self.antibot_block_sum = antibot_block_sum  # type: long
        self.antibot_report_sum = antibot_report_sum  # type: str
        self.antiscan_reports_sum = antiscan_reports_sum  # type: long
        self.blacklist_block_sum = blacklist_block_sum  # type: str
        self.blacklist_reports_sum = blacklist_reports_sum  # type: long
        self.cc_custom_block_sum = cc_custom_block_sum  # type: long
        self.cc_custom_reports_sum = cc_custom_reports_sum  # type: long
        self.cc_system_blocks_sum = cc_system_blocks_sum  # type: long
        self.cc_system_reports_sum = cc_system_reports_sum  # type: long
        self.count = count  # type: long
        self.in_bytes = in_bytes  # type: long
        self.index = index  # type: long
        self.max_pv = max_pv  # type: long
        self.out_bytes = out_bytes  # type: long
        self.region_block_blocks_sum = region_block_blocks_sum  # type: long
        self.region_block_reports_sum = region_block_reports_sum  # type: long
        self.waf_block_sum = waf_block_sum  # type: long
        self.waf_report_sum = waf_report_sum  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowChartResponseBodyFlowChart, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_custom_block_sum is not None:
            result['AclCustomBlockSum'] = self.acl_custom_block_sum
        if self.acl_custom_reports_sum is not None:
            result['AclCustomReportsSum'] = self.acl_custom_reports_sum
        if self.anti_scan_block_sum is not None:
            result['AntiScanBlockSum'] = self.anti_scan_block_sum
        if self.antibot_block_sum is not None:
            result['AntibotBlockSum'] = self.antibot_block_sum
        if self.antibot_report_sum is not None:
            result['AntibotReportSum'] = self.antibot_report_sum
        if self.antiscan_reports_sum is not None:
            result['AntiscanReportsSum'] = self.antiscan_reports_sum
        if self.blacklist_block_sum is not None:
            result['BlacklistBlockSum'] = self.blacklist_block_sum
        if self.blacklist_reports_sum is not None:
            result['BlacklistReportsSum'] = self.blacklist_reports_sum
        if self.cc_custom_block_sum is not None:
            result['CcCustomBlockSum'] = self.cc_custom_block_sum
        if self.cc_custom_reports_sum is not None:
            result['CcCustomReportsSum'] = self.cc_custom_reports_sum
        if self.cc_system_blocks_sum is not None:
            result['CcSystemBlocksSum'] = self.cc_system_blocks_sum
        if self.cc_system_reports_sum is not None:
            result['CcSystemReportsSum'] = self.cc_system_reports_sum
        if self.count is not None:
            result['Count'] = self.count
        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes
        if self.index is not None:
            result['Index'] = self.index
        if self.max_pv is not None:
            result['MaxPv'] = self.max_pv
        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes
        if self.region_block_blocks_sum is not None:
            result['RegionBlockBlocksSum'] = self.region_block_blocks_sum
        if self.region_block_reports_sum is not None:
            result['RegionBlockReportsSum'] = self.region_block_reports_sum
        if self.waf_block_sum is not None:
            result['WafBlockSum'] = self.waf_block_sum
        if self.waf_report_sum is not None:
            result['WafReportSum'] = self.waf_report_sum
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclCustomBlockSum') is not None:
            self.acl_custom_block_sum = m.get('AclCustomBlockSum')
        if m.get('AclCustomReportsSum') is not None:
            self.acl_custom_reports_sum = m.get('AclCustomReportsSum')
        if m.get('AntiScanBlockSum') is not None:
            self.anti_scan_block_sum = m.get('AntiScanBlockSum')
        if m.get('AntibotBlockSum') is not None:
            self.antibot_block_sum = m.get('AntibotBlockSum')
        if m.get('AntibotReportSum') is not None:
            self.antibot_report_sum = m.get('AntibotReportSum')
        if m.get('AntiscanReportsSum') is not None:
            self.antiscan_reports_sum = m.get('AntiscanReportsSum')
        if m.get('BlacklistBlockSum') is not None:
            self.blacklist_block_sum = m.get('BlacklistBlockSum')
        if m.get('BlacklistReportsSum') is not None:
            self.blacklist_reports_sum = m.get('BlacklistReportsSum')
        if m.get('CcCustomBlockSum') is not None:
            self.cc_custom_block_sum = m.get('CcCustomBlockSum')
        if m.get('CcCustomReportsSum') is not None:
            self.cc_custom_reports_sum = m.get('CcCustomReportsSum')
        if m.get('CcSystemBlocksSum') is not None:
            self.cc_system_blocks_sum = m.get('CcSystemBlocksSum')
        if m.get('CcSystemReportsSum') is not None:
            self.cc_system_reports_sum = m.get('CcSystemReportsSum')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('MaxPv') is not None:
            self.max_pv = m.get('MaxPv')
        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')
        if m.get('RegionBlockBlocksSum') is not None:
            self.region_block_blocks_sum = m.get('RegionBlockBlocksSum')
        if m.get('RegionBlockReportsSum') is not None:
            self.region_block_reports_sum = m.get('RegionBlockReportsSum')
        if m.get('WafBlockSum') is not None:
            self.waf_block_sum = m.get('WafBlockSum')
        if m.get('WafReportSum') is not None:
            self.waf_report_sum = m.get('WafReportSum')
        return self


class DescribeFlowChartResponseBody(TeaModel):
    def __init__(self, flow_chart=None, request_id=None):
        self.flow_chart = flow_chart  # type: list[DescribeFlowChartResponseBodyFlowChart]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.flow_chart:
            for k in self.flow_chart:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFlowChartResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FlowChart'] = []
        if self.flow_chart is not None:
            for k in self.flow_chart:
                result['FlowChart'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.flow_chart = []
        if m.get('FlowChart') is not None:
            for k in m.get('FlowChart'):
                temp_model = DescribeFlowChartResponseBodyFlowChart()
                self.flow_chart.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFlowChartResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFlowChartResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFlowChartResponse, self).to_map()
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
            temp_model = DescribeFlowChartResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowTopResourceRequest(TeaModel):
    def __init__(self, end_timestamp=None, instance_id=None, start_timestamp=None):
        self.end_timestamp = end_timestamp  # type: str
        self.instance_id = instance_id  # type: str
        self.start_timestamp = start_timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowTopResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeFlowTopResourceResponseBodyRuleHitsTopResource(TeaModel):
    def __init__(self, count=None, resource=None):
        self.count = count  # type: long
        self.resource = resource  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowTopResourceResponseBodyRuleHitsTopResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.resource is not None:
            result['Resource'] = self.resource
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        return self


class DescribeFlowTopResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, rule_hits_top_resource=None):
        self.request_id = request_id  # type: str
        self.rule_hits_top_resource = rule_hits_top_resource  # type: list[DescribeFlowTopResourceResponseBodyRuleHitsTopResource]

    def validate(self):
        if self.rule_hits_top_resource:
            for k in self.rule_hits_top_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFlowTopResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleHitsTopResource'] = []
        if self.rule_hits_top_resource is not None:
            for k in self.rule_hits_top_resource:
                result['RuleHitsTopResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_hits_top_resource = []
        if m.get('RuleHitsTopResource') is not None:
            for k in m.get('RuleHitsTopResource'):
                temp_model = DescribeFlowTopResourceResponseBodyRuleHitsTopResource()
                self.rule_hits_top_resource.append(temp_model.from_map(k))
        return self


class DescribeFlowTopResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFlowTopResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFlowTopResourceResponse, self).to_map()
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
            temp_model = DescribeFlowTopResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowTopUrlRequest(TeaModel):
    def __init__(self, end_timestamp=None, instance_id=None, resource=None, start_timestamp=None):
        self.end_timestamp = end_timestamp  # type: str
        self.instance_id = instance_id  # type: str
        self.resource = resource  # type: str
        self.start_timestamp = start_timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowTopUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeFlowTopUrlResponseBodyRuleHitsTopUrl(TeaModel):
    def __init__(self, count=None, url=None):
        self.count = count  # type: long
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowTopUrlResponseBodyRuleHitsTopUrl, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeFlowTopUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, rule_hits_top_url=None):
        self.request_id = request_id  # type: str
        self.rule_hits_top_url = rule_hits_top_url  # type: list[DescribeFlowTopUrlResponseBodyRuleHitsTopUrl]

    def validate(self):
        if self.rule_hits_top_url:
            for k in self.rule_hits_top_url:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFlowTopUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleHitsTopUrl'] = []
        if self.rule_hits_top_url is not None:
            for k in self.rule_hits_top_url:
                result['RuleHitsTopUrl'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_hits_top_url = []
        if m.get('RuleHitsTopUrl') is not None:
            for k in m.get('RuleHitsTopUrl'):
                temp_model = DescribeFlowTopUrlResponseBodyRuleHitsTopUrl()
                self.rule_hits_top_url.append(temp_model.from_map(k))
        return self


class DescribeFlowTopUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFlowTopUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFlowTopUrlResponse, self).to_map()
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
            temp_model = DescribeFlowTopUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(self, region_id=None, resource_group_id=None):
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeInstanceResponseBodyDetails(TeaModel):
    def __init__(self, acl_rule_max_ip_count=None, anti_scan=None, anti_scan_template_max_count=None,
                 backend_max_count=None, base_waf_group=None, base_waf_group_rule_in_template_max_count=None,
                 base_waf_group_rule_template_max_count=None, bot=None, bot_app=None, bot_template_max_count=None, bot_web=None,
                 cname_resource_max_count=None, custom_response=None, custom_response_rule_in_template_max_count=None,
                 custom_response_template_max_count=None, custom_rule=None, custom_rule_action=None, custom_rule_condition=None,
                 custom_rule_in_template_max_count=None, custom_rule_ratelimitor=None, custom_rule_template_max_count=None,
                 defense_group_max_count=None, defense_object_in_group_max_count=None, defense_object_in_template_max_count=None,
                 defense_object_max_count=None, dlp=None, dlp_rule_in_template_max_count=None, dlp_template_max_count=None,
                 exclusive_ip=None, gslb=None, http_ports=None, https_ports=None, ip_blacklist=None,
                 ip_blacklist_ip_in_rule_max_count=None, ip_blacklist_rule_in_template_max_count=None, ip_blacklist_template_max_count=None,
                 ipv_6=None, log_service=None, major_protection=None, major_protection_template_max_count=None,
                 tamperproof=None, tamperproof_rule_in_template_max_count=None, tamperproof_template_max_count=None,
                 vast_ip_blacklist_in_file_max_count=None, vast_ip_blacklist_in_operation_max_count=None, vast_ip_blacklist_max_count=None,
                 whitelist=None, whitelist_logical=None, whitelist_rule_condition=None,
                 whitelist_rule_in_template_max_count=None, whitelist_template_max_count=None):
        self.acl_rule_max_ip_count = acl_rule_max_ip_count  # type: long
        self.anti_scan = anti_scan  # type: bool
        self.anti_scan_template_max_count = anti_scan_template_max_count  # type: long
        self.backend_max_count = backend_max_count  # type: long
        self.base_waf_group = base_waf_group  # type: bool
        self.base_waf_group_rule_in_template_max_count = base_waf_group_rule_in_template_max_count  # type: long
        self.base_waf_group_rule_template_max_count = base_waf_group_rule_template_max_count  # type: long
        self.bot = bot  # type: bool
        self.bot_app = bot_app  # type: str
        self.bot_template_max_count = bot_template_max_count  # type: long
        self.bot_web = bot_web  # type: str
        self.cname_resource_max_count = cname_resource_max_count  # type: long
        self.custom_response = custom_response  # type: bool
        self.custom_response_rule_in_template_max_count = custom_response_rule_in_template_max_count  # type: long
        self.custom_response_template_max_count = custom_response_template_max_count  # type: long
        self.custom_rule = custom_rule  # type: bool
        self.custom_rule_action = custom_rule_action  # type: str
        self.custom_rule_condition = custom_rule_condition  # type: str
        self.custom_rule_in_template_max_count = custom_rule_in_template_max_count  # type: long
        self.custom_rule_ratelimitor = custom_rule_ratelimitor  # type: str
        self.custom_rule_template_max_count = custom_rule_template_max_count  # type: long
        self.defense_group_max_count = defense_group_max_count  # type: long
        self.defense_object_in_group_max_count = defense_object_in_group_max_count  # type: long
        self.defense_object_in_template_max_count = defense_object_in_template_max_count  # type: long
        self.defense_object_max_count = defense_object_max_count  # type: long
        self.dlp = dlp  # type: bool
        self.dlp_rule_in_template_max_count = dlp_rule_in_template_max_count  # type: long
        self.dlp_template_max_count = dlp_template_max_count  # type: long
        self.exclusive_ip = exclusive_ip  # type: bool
        self.gslb = gslb  # type: bool
        self.http_ports = http_ports  # type: str
        self.https_ports = https_ports  # type: str
        self.ip_blacklist = ip_blacklist  # type: bool
        self.ip_blacklist_ip_in_rule_max_count = ip_blacklist_ip_in_rule_max_count  # type: long
        self.ip_blacklist_rule_in_template_max_count = ip_blacklist_rule_in_template_max_count  # type: long
        self.ip_blacklist_template_max_count = ip_blacklist_template_max_count  # type: long
        self.ipv_6 = ipv_6  # type: bool
        self.log_service = log_service  # type: bool
        self.major_protection = major_protection  # type: bool
        self.major_protection_template_max_count = major_protection_template_max_count  # type: long
        self.tamperproof = tamperproof  # type: bool
        self.tamperproof_rule_in_template_max_count = tamperproof_rule_in_template_max_count  # type: long
        self.tamperproof_template_max_count = tamperproof_template_max_count  # type: long
        self.vast_ip_blacklist_in_file_max_count = vast_ip_blacklist_in_file_max_count  # type: long
        self.vast_ip_blacklist_in_operation_max_count = vast_ip_blacklist_in_operation_max_count  # type: long
        self.vast_ip_blacklist_max_count = vast_ip_blacklist_max_count  # type: long
        self.whitelist = whitelist  # type: bool
        self.whitelist_logical = whitelist_logical  # type: str
        self.whitelist_rule_condition = whitelist_rule_condition  # type: str
        self.whitelist_rule_in_template_max_count = whitelist_rule_in_template_max_count  # type: long
        self.whitelist_template_max_count = whitelist_template_max_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_rule_max_ip_count is not None:
            result['AclRuleMaxIpCount'] = self.acl_rule_max_ip_count
        if self.anti_scan is not None:
            result['AntiScan'] = self.anti_scan
        if self.anti_scan_template_max_count is not None:
            result['AntiScanTemplateMaxCount'] = self.anti_scan_template_max_count
        if self.backend_max_count is not None:
            result['BackendMaxCount'] = self.backend_max_count
        if self.base_waf_group is not None:
            result['BaseWafGroup'] = self.base_waf_group
        if self.base_waf_group_rule_in_template_max_count is not None:
            result['BaseWafGroupRuleInTemplateMaxCount'] = self.base_waf_group_rule_in_template_max_count
        if self.base_waf_group_rule_template_max_count is not None:
            result['BaseWafGroupRuleTemplateMaxCount'] = self.base_waf_group_rule_template_max_count
        if self.bot is not None:
            result['Bot'] = self.bot
        if self.bot_app is not None:
            result['BotApp'] = self.bot_app
        if self.bot_template_max_count is not None:
            result['BotTemplateMaxCount'] = self.bot_template_max_count
        if self.bot_web is not None:
            result['BotWeb'] = self.bot_web
        if self.cname_resource_max_count is not None:
            result['CnameResourceMaxCount'] = self.cname_resource_max_count
        if self.custom_response is not None:
            result['CustomResponse'] = self.custom_response
        if self.custom_response_rule_in_template_max_count is not None:
            result['CustomResponseRuleInTemplateMaxCount'] = self.custom_response_rule_in_template_max_count
        if self.custom_response_template_max_count is not None:
            result['CustomResponseTemplateMaxCount'] = self.custom_response_template_max_count
        if self.custom_rule is not None:
            result['CustomRule'] = self.custom_rule
        if self.custom_rule_action is not None:
            result['CustomRuleAction'] = self.custom_rule_action
        if self.custom_rule_condition is not None:
            result['CustomRuleCondition'] = self.custom_rule_condition
        if self.custom_rule_in_template_max_count is not None:
            result['CustomRuleInTemplateMaxCount'] = self.custom_rule_in_template_max_count
        if self.custom_rule_ratelimitor is not None:
            result['CustomRuleRatelimitor'] = self.custom_rule_ratelimitor
        if self.custom_rule_template_max_count is not None:
            result['CustomRuleTemplateMaxCount'] = self.custom_rule_template_max_count
        if self.defense_group_max_count is not None:
            result['DefenseGroupMaxCount'] = self.defense_group_max_count
        if self.defense_object_in_group_max_count is not None:
            result['DefenseObjectInGroupMaxCount'] = self.defense_object_in_group_max_count
        if self.defense_object_in_template_max_count is not None:
            result['DefenseObjectInTemplateMaxCount'] = self.defense_object_in_template_max_count
        if self.defense_object_max_count is not None:
            result['DefenseObjectMaxCount'] = self.defense_object_max_count
        if self.dlp is not None:
            result['Dlp'] = self.dlp
        if self.dlp_rule_in_template_max_count is not None:
            result['DlpRuleInTemplateMaxCount'] = self.dlp_rule_in_template_max_count
        if self.dlp_template_max_count is not None:
            result['DlpTemplateMaxCount'] = self.dlp_template_max_count
        if self.exclusive_ip is not None:
            result['ExclusiveIp'] = self.exclusive_ip
        if self.gslb is not None:
            result['Gslb'] = self.gslb
        if self.http_ports is not None:
            result['HttpPorts'] = self.http_ports
        if self.https_ports is not None:
            result['HttpsPorts'] = self.https_ports
        if self.ip_blacklist is not None:
            result['IpBlacklist'] = self.ip_blacklist
        if self.ip_blacklist_ip_in_rule_max_count is not None:
            result['IpBlacklistIpInRuleMaxCount'] = self.ip_blacklist_ip_in_rule_max_count
        if self.ip_blacklist_rule_in_template_max_count is not None:
            result['IpBlacklistRuleInTemplateMaxCount'] = self.ip_blacklist_rule_in_template_max_count
        if self.ip_blacklist_template_max_count is not None:
            result['IpBlacklistTemplateMaxCount'] = self.ip_blacklist_template_max_count
        if self.ipv_6 is not None:
            result['Ipv6'] = self.ipv_6
        if self.log_service is not None:
            result['LogService'] = self.log_service
        if self.major_protection is not None:
            result['MajorProtection'] = self.major_protection
        if self.major_protection_template_max_count is not None:
            result['MajorProtectionTemplateMaxCount'] = self.major_protection_template_max_count
        if self.tamperproof is not None:
            result['Tamperproof'] = self.tamperproof
        if self.tamperproof_rule_in_template_max_count is not None:
            result['TamperproofRuleInTemplateMaxCount'] = self.tamperproof_rule_in_template_max_count
        if self.tamperproof_template_max_count is not None:
            result['TamperproofTemplateMaxCount'] = self.tamperproof_template_max_count
        if self.vast_ip_blacklist_in_file_max_count is not None:
            result['VastIpBlacklistInFileMaxCount'] = self.vast_ip_blacklist_in_file_max_count
        if self.vast_ip_blacklist_in_operation_max_count is not None:
            result['VastIpBlacklistInOperationMaxCount'] = self.vast_ip_blacklist_in_operation_max_count
        if self.vast_ip_blacklist_max_count is not None:
            result['VastIpBlacklistMaxCount'] = self.vast_ip_blacklist_max_count
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        if self.whitelist_logical is not None:
            result['WhitelistLogical'] = self.whitelist_logical
        if self.whitelist_rule_condition is not None:
            result['WhitelistRuleCondition'] = self.whitelist_rule_condition
        if self.whitelist_rule_in_template_max_count is not None:
            result['WhitelistRuleInTemplateMaxCount'] = self.whitelist_rule_in_template_max_count
        if self.whitelist_template_max_count is not None:
            result['WhitelistTemplateMaxCount'] = self.whitelist_template_max_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclRuleMaxIpCount') is not None:
            self.acl_rule_max_ip_count = m.get('AclRuleMaxIpCount')
        if m.get('AntiScan') is not None:
            self.anti_scan = m.get('AntiScan')
        if m.get('AntiScanTemplateMaxCount') is not None:
            self.anti_scan_template_max_count = m.get('AntiScanTemplateMaxCount')
        if m.get('BackendMaxCount') is not None:
            self.backend_max_count = m.get('BackendMaxCount')
        if m.get('BaseWafGroup') is not None:
            self.base_waf_group = m.get('BaseWafGroup')
        if m.get('BaseWafGroupRuleInTemplateMaxCount') is not None:
            self.base_waf_group_rule_in_template_max_count = m.get('BaseWafGroupRuleInTemplateMaxCount')
        if m.get('BaseWafGroupRuleTemplateMaxCount') is not None:
            self.base_waf_group_rule_template_max_count = m.get('BaseWafGroupRuleTemplateMaxCount')
        if m.get('Bot') is not None:
            self.bot = m.get('Bot')
        if m.get('BotApp') is not None:
            self.bot_app = m.get('BotApp')
        if m.get('BotTemplateMaxCount') is not None:
            self.bot_template_max_count = m.get('BotTemplateMaxCount')
        if m.get('BotWeb') is not None:
            self.bot_web = m.get('BotWeb')
        if m.get('CnameResourceMaxCount') is not None:
            self.cname_resource_max_count = m.get('CnameResourceMaxCount')
        if m.get('CustomResponse') is not None:
            self.custom_response = m.get('CustomResponse')
        if m.get('CustomResponseRuleInTemplateMaxCount') is not None:
            self.custom_response_rule_in_template_max_count = m.get('CustomResponseRuleInTemplateMaxCount')
        if m.get('CustomResponseTemplateMaxCount') is not None:
            self.custom_response_template_max_count = m.get('CustomResponseTemplateMaxCount')
        if m.get('CustomRule') is not None:
            self.custom_rule = m.get('CustomRule')
        if m.get('CustomRuleAction') is not None:
            self.custom_rule_action = m.get('CustomRuleAction')
        if m.get('CustomRuleCondition') is not None:
            self.custom_rule_condition = m.get('CustomRuleCondition')
        if m.get('CustomRuleInTemplateMaxCount') is not None:
            self.custom_rule_in_template_max_count = m.get('CustomRuleInTemplateMaxCount')
        if m.get('CustomRuleRatelimitor') is not None:
            self.custom_rule_ratelimitor = m.get('CustomRuleRatelimitor')
        if m.get('CustomRuleTemplateMaxCount') is not None:
            self.custom_rule_template_max_count = m.get('CustomRuleTemplateMaxCount')
        if m.get('DefenseGroupMaxCount') is not None:
            self.defense_group_max_count = m.get('DefenseGroupMaxCount')
        if m.get('DefenseObjectInGroupMaxCount') is not None:
            self.defense_object_in_group_max_count = m.get('DefenseObjectInGroupMaxCount')
        if m.get('DefenseObjectInTemplateMaxCount') is not None:
            self.defense_object_in_template_max_count = m.get('DefenseObjectInTemplateMaxCount')
        if m.get('DefenseObjectMaxCount') is not None:
            self.defense_object_max_count = m.get('DefenseObjectMaxCount')
        if m.get('Dlp') is not None:
            self.dlp = m.get('Dlp')
        if m.get('DlpRuleInTemplateMaxCount') is not None:
            self.dlp_rule_in_template_max_count = m.get('DlpRuleInTemplateMaxCount')
        if m.get('DlpTemplateMaxCount') is not None:
            self.dlp_template_max_count = m.get('DlpTemplateMaxCount')
        if m.get('ExclusiveIp') is not None:
            self.exclusive_ip = m.get('ExclusiveIp')
        if m.get('Gslb') is not None:
            self.gslb = m.get('Gslb')
        if m.get('HttpPorts') is not None:
            self.http_ports = m.get('HttpPorts')
        if m.get('HttpsPorts') is not None:
            self.https_ports = m.get('HttpsPorts')
        if m.get('IpBlacklist') is not None:
            self.ip_blacklist = m.get('IpBlacklist')
        if m.get('IpBlacklistIpInRuleMaxCount') is not None:
            self.ip_blacklist_ip_in_rule_max_count = m.get('IpBlacklistIpInRuleMaxCount')
        if m.get('IpBlacklistRuleInTemplateMaxCount') is not None:
            self.ip_blacklist_rule_in_template_max_count = m.get('IpBlacklistRuleInTemplateMaxCount')
        if m.get('IpBlacklistTemplateMaxCount') is not None:
            self.ip_blacklist_template_max_count = m.get('IpBlacklistTemplateMaxCount')
        if m.get('Ipv6') is not None:
            self.ipv_6 = m.get('Ipv6')
        if m.get('LogService') is not None:
            self.log_service = m.get('LogService')
        if m.get('MajorProtection') is not None:
            self.major_protection = m.get('MajorProtection')
        if m.get('MajorProtectionTemplateMaxCount') is not None:
            self.major_protection_template_max_count = m.get('MajorProtectionTemplateMaxCount')
        if m.get('Tamperproof') is not None:
            self.tamperproof = m.get('Tamperproof')
        if m.get('TamperproofRuleInTemplateMaxCount') is not None:
            self.tamperproof_rule_in_template_max_count = m.get('TamperproofRuleInTemplateMaxCount')
        if m.get('TamperproofTemplateMaxCount') is not None:
            self.tamperproof_template_max_count = m.get('TamperproofTemplateMaxCount')
        if m.get('VastIpBlacklistInFileMaxCount') is not None:
            self.vast_ip_blacklist_in_file_max_count = m.get('VastIpBlacklistInFileMaxCount')
        if m.get('VastIpBlacklistInOperationMaxCount') is not None:
            self.vast_ip_blacklist_in_operation_max_count = m.get('VastIpBlacklistInOperationMaxCount')
        if m.get('VastIpBlacklistMaxCount') is not None:
            self.vast_ip_blacklist_max_count = m.get('VastIpBlacklistMaxCount')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        if m.get('WhitelistLogical') is not None:
            self.whitelist_logical = m.get('WhitelistLogical')
        if m.get('WhitelistRuleCondition') is not None:
            self.whitelist_rule_condition = m.get('WhitelistRuleCondition')
        if m.get('WhitelistRuleInTemplateMaxCount') is not None:
            self.whitelist_rule_in_template_max_count = m.get('WhitelistRuleInTemplateMaxCount')
        if m.get('WhitelistTemplateMaxCount') is not None:
            self.whitelist_template_max_count = m.get('WhitelistTemplateMaxCount')
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(self, details=None, edition=None, end_time=None, in_debt=None, instance_id=None, pay_type=None,
                 region_id=None, request_id=None, start_time=None, status=None):
        self.details = details  # type: DescribeInstanceResponseBodyDetails
        self.edition = edition  # type: str
        self.end_time = end_time  # type: long
        self.in_debt = in_debt  # type: str
        self.instance_id = instance_id  # type: str
        self.pay_type = pay_type  # type: str
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: int

    def validate(self):
        if self.details:
            self.details.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.details is not None:
            result['Details'] = self.details.to_map()
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Details') is not None:
            temp_model = DescribeInstanceResponseBodyDetails()
            self.details = temp_model.from_map(m['Details'])
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponse, self).to_map()
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
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMajorProtectionBlackIpsRequest(TeaModel):
    def __init__(self, instance_id=None, ip_like=None, order_by=None, page_number=None, page_size=None, rule_id=None,
                 template_id=None):
        self.instance_id = instance_id  # type: str
        self.ip_like = ip_like  # type: str
        self.order_by = order_by  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.rule_id = rule_id  # type: long
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMajorProtectionBlackIpsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_like is not None:
            result['IpLike'] = self.ip_like
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpLike') is not None:
            self.ip_like = m.get('IpLike')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeMajorProtectionBlackIpsResponseBodyIpList(TeaModel):
    def __init__(self, description=None, expired_time=None, gmt_modified=None, ip=None, rule_id=None,
                 template_id=None):
        self.description = description  # type: str
        self.expired_time = expired_time  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.ip = ip  # type: str
        self.rule_id = rule_id  # type: long
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMajorProtectionBlackIpsResponseBodyIpList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeMajorProtectionBlackIpsResponseBody(TeaModel):
    def __init__(self, ip_list=None, request_id=None, total_count=None):
        self.ip_list = ip_list  # type: list[DescribeMajorProtectionBlackIpsResponseBodyIpList]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.ip_list:
            for k in self.ip_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMajorProtectionBlackIpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpList'] = []
        if self.ip_list is not None:
            for k in self.ip_list:
                result['IpList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ip_list = []
        if m.get('IpList') is not None:
            for k in m.get('IpList'):
                temp_model = DescribeMajorProtectionBlackIpsResponseBodyIpList()
                self.ip_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeMajorProtectionBlackIpsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeMajorProtectionBlackIpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeMajorProtectionBlackIpsResponse, self).to_map()
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
            temp_model = DescribeMajorProtectionBlackIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePeakTrendRequest(TeaModel):
    def __init__(self, end_timestamp=None, instance_id=None, interval=None, resource=None, start_timestamp=None):
        self.end_timestamp = end_timestamp  # type: str
        self.instance_id = instance_id  # type: str
        self.interval = interval  # type: str
        self.resource = resource  # type: str
        self.start_timestamp = start_timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePeakTrendRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribePeakTrendResponseBodyFlowChart(TeaModel):
    def __init__(self, acl_sum=None, anti_scan_sum=None, cc_sum=None, count=None, index=None, waf_sum=None):
        self.acl_sum = acl_sum  # type: long
        self.anti_scan_sum = anti_scan_sum  # type: long
        self.cc_sum = cc_sum  # type: long
        self.count = count  # type: long
        self.index = index  # type: long
        self.waf_sum = waf_sum  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePeakTrendResponseBodyFlowChart, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_sum is not None:
            result['AclSum'] = self.acl_sum
        if self.anti_scan_sum is not None:
            result['AntiScanSum'] = self.anti_scan_sum
        if self.cc_sum is not None:
            result['CcSum'] = self.cc_sum
        if self.count is not None:
            result['Count'] = self.count
        if self.index is not None:
            result['Index'] = self.index
        if self.waf_sum is not None:
            result['WafSum'] = self.waf_sum
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclSum') is not None:
            self.acl_sum = m.get('AclSum')
        if m.get('AntiScanSum') is not None:
            self.anti_scan_sum = m.get('AntiScanSum')
        if m.get('CcSum') is not None:
            self.cc_sum = m.get('CcSum')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('WafSum') is not None:
            self.waf_sum = m.get('WafSum')
        return self


class DescribePeakTrendResponseBody(TeaModel):
    def __init__(self, flow_chart=None, request_id=None):
        self.flow_chart = flow_chart  # type: list[DescribePeakTrendResponseBodyFlowChart]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.flow_chart:
            for k in self.flow_chart:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePeakTrendResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FlowChart'] = []
        if self.flow_chart is not None:
            for k in self.flow_chart:
                result['FlowChart'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.flow_chart = []
        if m.get('FlowChart') is not None:
            for k in m.get('FlowChart'):
                temp_model = DescribePeakTrendResponseBodyFlowChart()
                self.flow_chart.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePeakTrendResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePeakTrendResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePeakTrendResponse, self).to_map()
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
            temp_model = DescribePeakTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceLogStatusRequest(TeaModel):
    def __init__(self, instance_id=None, resources=None):
        self.instance_id = instance_id  # type: str
        self.resources = resources  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourceLogStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class DescribeResourceLogStatusResponseBodyResult(TeaModel):
    def __init__(self, resource=None, status=None):
        self.resource = resource  # type: str
        self.status = status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourceLogStatusResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeResourceLogStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: list[DescribeResourceLogStatusResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeResourceLogStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeResourceLogStatusResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeResourceLogStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeResourceLogStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeResourceLogStatusResponse, self).to_map()
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
            temp_model = DescribeResourceLogStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourcePortRequest(TeaModel):
    def __init__(self, instance_id=None, resource_instance_id=None):
        self.instance_id = instance_id  # type: str
        self.resource_instance_id = resource_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourcePortRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')
        return self


class DescribeResourcePortResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_ports=None):
        self.request_id = request_id  # type: str
        self.resource_ports = resource_ports  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourcePortResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_ports is not None:
            result['ResourcePorts'] = self.resource_ports
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourcePorts') is not None:
            self.resource_ports = m.get('ResourcePorts')
        return self


class DescribeResourcePortResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeResourcePortResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeResourcePortResponse, self).to_map()
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
            temp_model = DescribeResourcePortResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResponseCodeTrendGraphRequest(TeaModel):
    def __init__(self, end_timestamp=None, instance_id=None, interval=None, resource=None, start_timestamp=None,
                 type=None):
        self.end_timestamp = end_timestamp  # type: str
        self.instance_id = instance_id  # type: str
        self.interval = interval  # type: str
        self.resource = resource  # type: str
        self.start_timestamp = start_timestamp  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResponseCodeTrendGraphRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeResponseCodeTrendGraphResponseBodyResponseCodes(TeaModel):
    def __init__(self, code_302pv=None, code_405pv=None, code_499pv=None, code_5xx_pv=None, index=None):
        self.code_302pv = code_302pv  # type: long
        self.code_405pv = code_405pv  # type: long
        self.code_499pv = code_499pv  # type: long
        self.code_5xx_pv = code_5xx_pv  # type: long
        self.index = index  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResponseCodeTrendGraphResponseBodyResponseCodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_302pv is not None:
            result['302Pv'] = self.code_302pv
        if self.code_405pv is not None:
            result['405Pv'] = self.code_405pv
        if self.code_499pv is not None:
            result['499Pv'] = self.code_499pv
        if self.code_5xx_pv is not None:
            result['5xxPv'] = self.code_5xx_pv
        if self.index is not None:
            result['Index'] = self.index
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('302Pv') is not None:
            self.code_302pv = m.get('302Pv')
        if m.get('405Pv') is not None:
            self.code_405pv = m.get('405Pv')
        if m.get('499Pv') is not None:
            self.code_499pv = m.get('499Pv')
        if m.get('5xxPv') is not None:
            self.code_5xx_pv = m.get('5xxPv')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        return self


class DescribeResponseCodeTrendGraphResponseBody(TeaModel):
    def __init__(self, request_id=None, response_codes=None):
        self.request_id = request_id  # type: str
        self.response_codes = response_codes  # type: list[DescribeResponseCodeTrendGraphResponseBodyResponseCodes]

    def validate(self):
        if self.response_codes:
            for k in self.response_codes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeResponseCodeTrendGraphResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResponseCodes'] = []
        if self.response_codes is not None:
            for k in self.response_codes:
                result['ResponseCodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.response_codes = []
        if m.get('ResponseCodes') is not None:
            for k in m.get('ResponseCodes'):
                temp_model = DescribeResponseCodeTrendGraphResponseBodyResponseCodes()
                self.response_codes.append(temp_model.from_map(k))
        return self


class DescribeResponseCodeTrendGraphResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeResponseCodeTrendGraphResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeResponseCodeTrendGraphResponse, self).to_map()
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
            temp_model = DescribeResponseCodeTrendGraphResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRuleGroupsRequest(TeaModel):
    def __init__(self, instance_id=None, page_number=None, page_size=None, search_type=None, search_value=None):
        self.instance_id = instance_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.search_type = search_type  # type: str
        self.search_value = search_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRuleGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_type is not None:
            result['SearchType'] = self.search_type
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        return self


class DescribeRuleGroupsResponseBodyRuleGroups(TeaModel):
    def __init__(self, gmt_modified=None, rule_group_id=None, rule_group_name=None, rule_total_count=None):
        self.gmt_modified = gmt_modified  # type: long
        self.rule_group_id = rule_group_id  # type: long
        self.rule_group_name = rule_group_name  # type: str
        self.rule_total_count = rule_total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRuleGroupsResponseBodyRuleGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.rule_group_id is not None:
            result['RuleGroupId'] = self.rule_group_id
        if self.rule_group_name is not None:
            result['RuleGroupName'] = self.rule_group_name
        if self.rule_total_count is not None:
            result['RuleTotalCount'] = self.rule_total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RuleGroupId') is not None:
            self.rule_group_id = m.get('RuleGroupId')
        if m.get('RuleGroupName') is not None:
            self.rule_group_name = m.get('RuleGroupName')
        if m.get('RuleTotalCount') is not None:
            self.rule_total_count = m.get('RuleTotalCount')
        return self


class DescribeRuleGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, rule_groups=None, total_count=None):
        self.request_id = request_id  # type: str
        self.rule_groups = rule_groups  # type: list[DescribeRuleGroupsResponseBodyRuleGroups]
        self.total_count = total_count  # type: long

    def validate(self):
        if self.rule_groups:
            for k in self.rule_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRuleGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleGroups'] = []
        if self.rule_groups is not None:
            for k in self.rule_groups:
                result['RuleGroups'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_groups = []
        if m.get('RuleGroups') is not None:
            for k in m.get('RuleGroups'):
                temp_model = DescribeRuleGroupsResponseBodyRuleGroups()
                self.rule_groups.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRuleGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRuleGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRuleGroupsResponse, self).to_map()
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
            temp_model = DescribeRuleGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRuleHitsTopClientIpRequest(TeaModel):
    def __init__(self, end_timestamp=None, instance_id=None, resource=None, rule_type=None, start_timestamp=None):
        self.end_timestamp = end_timestamp  # type: str
        self.instance_id = instance_id  # type: str
        self.resource = resource  # type: str
        self.rule_type = rule_type  # type: str
        self.start_timestamp = start_timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRuleHitsTopClientIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeRuleHitsTopClientIpResponseBodyRuleHitsTopClientIp(TeaModel):
    def __init__(self, client_ip=None, count=None):
        self.client_ip = client_ip  # type: str
        self.count = count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRuleHitsTopClientIpResponseBodyRuleHitsTopClientIp, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeRuleHitsTopClientIpResponseBody(TeaModel):
    def __init__(self, request_id=None, rule_hits_top_client_ip=None):
        self.request_id = request_id  # type: str
        self.rule_hits_top_client_ip = rule_hits_top_client_ip  # type: list[DescribeRuleHitsTopClientIpResponseBodyRuleHitsTopClientIp]

    def validate(self):
        if self.rule_hits_top_client_ip:
            for k in self.rule_hits_top_client_ip:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRuleHitsTopClientIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleHitsTopClientIp'] = []
        if self.rule_hits_top_client_ip is not None:
            for k in self.rule_hits_top_client_ip:
                result['RuleHitsTopClientIp'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_hits_top_client_ip = []
        if m.get('RuleHitsTopClientIp') is not None:
            for k in m.get('RuleHitsTopClientIp'):
                temp_model = DescribeRuleHitsTopClientIpResponseBodyRuleHitsTopClientIp()
                self.rule_hits_top_client_ip.append(temp_model.from_map(k))
        return self


class DescribeRuleHitsTopClientIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRuleHitsTopClientIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRuleHitsTopClientIpResponse, self).to_map()
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
            temp_model = DescribeRuleHitsTopClientIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRuleHitsTopResourceRequest(TeaModel):
    def __init__(self, end_timestamp=None, instance_id=None, rule_type=None, start_timestamp=None):
        self.end_timestamp = end_timestamp  # type: str
        self.instance_id = instance_id  # type: str
        self.rule_type = rule_type  # type: str
        self.start_timestamp = start_timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRuleHitsTopResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeRuleHitsTopResourceResponseBodyRuleHitsTopResource(TeaModel):
    def __init__(self, count=None, resource=None):
        self.count = count  # type: long
        self.resource = resource  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRuleHitsTopResourceResponseBodyRuleHitsTopResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.resource is not None:
            result['Resource'] = self.resource
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        return self


class DescribeRuleHitsTopResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, rule_hits_top_resource=None):
        self.request_id = request_id  # type: str
        self.rule_hits_top_resource = rule_hits_top_resource  # type: list[DescribeRuleHitsTopResourceResponseBodyRuleHitsTopResource]

    def validate(self):
        if self.rule_hits_top_resource:
            for k in self.rule_hits_top_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRuleHitsTopResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleHitsTopResource'] = []
        if self.rule_hits_top_resource is not None:
            for k in self.rule_hits_top_resource:
                result['RuleHitsTopResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_hits_top_resource = []
        if m.get('RuleHitsTopResource') is not None:
            for k in m.get('RuleHitsTopResource'):
                temp_model = DescribeRuleHitsTopResourceResponseBodyRuleHitsTopResource()
                self.rule_hits_top_resource.append(temp_model.from_map(k))
        return self


class DescribeRuleHitsTopResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRuleHitsTopResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRuleHitsTopResourceResponse, self).to_map()
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
            temp_model = DescribeRuleHitsTopResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRuleHitsTopRuleIdRequest(TeaModel):
    def __init__(self, end_timestamp=None, instance_id=None, resource=None, rule_type=None, start_timestamp=None):
        self.end_timestamp = end_timestamp  # type: str
        self.instance_id = instance_id  # type: str
        self.resource = resource  # type: str
        self.rule_type = rule_type  # type: str
        self.start_timestamp = start_timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRuleHitsTopRuleIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeRuleHitsTopRuleIdResponseBodyRuleHitsTopRuleId(TeaModel):
    def __init__(self, count=None, resource=None, rule_id=None):
        self.count = count  # type: long
        self.resource = resource  # type: str
        self.rule_id = rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRuleHitsTopRuleIdResponseBodyRuleHitsTopRuleId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeRuleHitsTopRuleIdResponseBody(TeaModel):
    def __init__(self, request_id=None, rule_hits_top_rule_id=None):
        self.request_id = request_id  # type: str
        self.rule_hits_top_rule_id = rule_hits_top_rule_id  # type: list[DescribeRuleHitsTopRuleIdResponseBodyRuleHitsTopRuleId]

    def validate(self):
        if self.rule_hits_top_rule_id:
            for k in self.rule_hits_top_rule_id:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRuleHitsTopRuleIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleHitsTopRuleId'] = []
        if self.rule_hits_top_rule_id is not None:
            for k in self.rule_hits_top_rule_id:
                result['RuleHitsTopRuleId'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_hits_top_rule_id = []
        if m.get('RuleHitsTopRuleId') is not None:
            for k in m.get('RuleHitsTopRuleId'):
                temp_model = DescribeRuleHitsTopRuleIdResponseBodyRuleHitsTopRuleId()
                self.rule_hits_top_rule_id.append(temp_model.from_map(k))
        return self


class DescribeRuleHitsTopRuleIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRuleHitsTopRuleIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRuleHitsTopRuleIdResponse, self).to_map()
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
            temp_model = DescribeRuleHitsTopRuleIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRuleHitsTopTuleTypeRequest(TeaModel):
    def __init__(self, end_timestamp=None, instance_id=None, resource=None, start_timestamp=None):
        self.end_timestamp = end_timestamp  # type: str
        self.instance_id = instance_id  # type: str
        self.resource = resource  # type: str
        self.start_timestamp = start_timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRuleHitsTopTuleTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeRuleHitsTopTuleTypeResponseBodyRuleHitsTopTuleType(TeaModel):
    def __init__(self, count=None, rule_type=None):
        self.count = count  # type: long
        self.rule_type = rule_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRuleHitsTopTuleTypeResponseBodyRuleHitsTopTuleType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class DescribeRuleHitsTopTuleTypeResponseBody(TeaModel):
    def __init__(self, request_id=None, rule_hits_top_tule_type=None):
        self.request_id = request_id  # type: str
        self.rule_hits_top_tule_type = rule_hits_top_tule_type  # type: list[DescribeRuleHitsTopTuleTypeResponseBodyRuleHitsTopTuleType]

    def validate(self):
        if self.rule_hits_top_tule_type:
            for k in self.rule_hits_top_tule_type:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRuleHitsTopTuleTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleHitsTopTuleType'] = []
        if self.rule_hits_top_tule_type is not None:
            for k in self.rule_hits_top_tule_type:
                result['RuleHitsTopTuleType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_hits_top_tule_type = []
        if m.get('RuleHitsTopTuleType') is not None:
            for k in m.get('RuleHitsTopTuleType'):
                temp_model = DescribeRuleHitsTopTuleTypeResponseBodyRuleHitsTopTuleType()
                self.rule_hits_top_tule_type.append(temp_model.from_map(k))
        return self


class DescribeRuleHitsTopTuleTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRuleHitsTopTuleTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRuleHitsTopTuleTypeResponse, self).to_map()
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
            temp_model = DescribeRuleHitsTopTuleTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRuleHitsTopUaRequest(TeaModel):
    def __init__(self, end_timestamp=None, instance_id=None, resource=None, start_timestamp=None):
        self.end_timestamp = end_timestamp  # type: str
        self.instance_id = instance_id  # type: str
        self.resource = resource  # type: str
        self.start_timestamp = start_timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRuleHitsTopUaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeRuleHitsTopUaResponseBodyRuleHitsTopUa(TeaModel):
    def __init__(self, count=None, ua=None):
        self.count = count  # type: long
        self.ua = ua  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRuleHitsTopUaResponseBodyRuleHitsTopUa, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.ua is not None:
            result['Ua'] = self.ua
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Ua') is not None:
            self.ua = m.get('Ua')
        return self


class DescribeRuleHitsTopUaResponseBody(TeaModel):
    def __init__(self, request_id=None, rule_hits_top_ua=None):
        self.request_id = request_id  # type: str
        self.rule_hits_top_ua = rule_hits_top_ua  # type: list[DescribeRuleHitsTopUaResponseBodyRuleHitsTopUa]

    def validate(self):
        if self.rule_hits_top_ua:
            for k in self.rule_hits_top_ua:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRuleHitsTopUaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleHitsTopUa'] = []
        if self.rule_hits_top_ua is not None:
            for k in self.rule_hits_top_ua:
                result['RuleHitsTopUa'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_hits_top_ua = []
        if m.get('RuleHitsTopUa') is not None:
            for k in m.get('RuleHitsTopUa'):
                temp_model = DescribeRuleHitsTopUaResponseBodyRuleHitsTopUa()
                self.rule_hits_top_ua.append(temp_model.from_map(k))
        return self


class DescribeRuleHitsTopUaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRuleHitsTopUaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRuleHitsTopUaResponse, self).to_map()
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
            temp_model = DescribeRuleHitsTopUaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRuleHitsTopUrlRequest(TeaModel):
    def __init__(self, end_timestamp=None, instance_id=None, resource=None, rule_type=None, start_timestamp=None):
        self.end_timestamp = end_timestamp  # type: str
        self.instance_id = instance_id  # type: str
        self.resource = resource  # type: str
        self.rule_type = rule_type  # type: str
        self.start_timestamp = start_timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRuleHitsTopUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeRuleHitsTopUrlResponseBodyRuleHitsTopUrl(TeaModel):
    def __init__(self, count=None, url=None):
        self.count = count  # type: long
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRuleHitsTopUrlResponseBodyRuleHitsTopUrl, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeRuleHitsTopUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, rule_hits_top_url=None):
        self.request_id = request_id  # type: str
        self.rule_hits_top_url = rule_hits_top_url  # type: list[DescribeRuleHitsTopUrlResponseBodyRuleHitsTopUrl]

    def validate(self):
        if self.rule_hits_top_url:
            for k in self.rule_hits_top_url:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRuleHitsTopUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleHitsTopUrl'] = []
        if self.rule_hits_top_url is not None:
            for k in self.rule_hits_top_url:
                result['RuleHitsTopUrl'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_hits_top_url = []
        if m.get('RuleHitsTopUrl') is not None:
            for k in m.get('RuleHitsTopUrl'):
                temp_model = DescribeRuleHitsTopUrlResponseBodyRuleHitsTopUrl()
                self.rule_hits_top_url.append(temp_model.from_map(k))
        return self


class DescribeRuleHitsTopUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRuleHitsTopUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRuleHitsTopUrlResponse, self).to_map()
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
            temp_model = DescribeRuleHitsTopUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTemplateResourcesRequest(TeaModel):
    def __init__(self, instance_id=None, resource_type=None, template_id=None):
        self.instance_id = instance_id  # type: str
        self.resource_type = resource_type  # type: str
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplateResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeTemplateResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, resources=None):
        self.request_id = request_id  # type: str
        self.resources = resources  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTemplateResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class DescribeTemplateResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTemplateResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTemplateResourcesResponse, self).to_map()
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
            temp_model = DescribeTemplateResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVisitTopIpRequest(TeaModel):
    def __init__(self, end_timestamp=None, instance_id=None, resource=None, start_timestamp=None):
        self.end_timestamp = end_timestamp  # type: str
        self.instance_id = instance_id  # type: str
        self.resource = resource  # type: str
        self.start_timestamp = start_timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVisitTopIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeVisitTopIpResponseBodyTopIp(TeaModel):
    def __init__(self, area=None, count=None, ip=None, isp=None):
        self.area = area  # type: str
        self.count = count  # type: long
        self.ip = ip  # type: str
        self.isp = isp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVisitTopIpResponseBodyTopIp, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.count is not None:
            result['Count'] = self.count
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.isp is not None:
            result['Isp'] = self.isp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        return self


class DescribeVisitTopIpResponseBody(TeaModel):
    def __init__(self, request_id=None, top_ip=None):
        self.request_id = request_id  # type: str
        self.top_ip = top_ip  # type: list[DescribeVisitTopIpResponseBodyTopIp]

    def validate(self):
        if self.top_ip:
            for k in self.top_ip:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVisitTopIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TopIp'] = []
        if self.top_ip is not None:
            for k in self.top_ip:
                result['TopIp'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.top_ip = []
        if m.get('TopIp') is not None:
            for k in m.get('TopIp'):
                temp_model = DescribeVisitTopIpResponseBodyTopIp()
                self.top_ip.append(temp_model.from_map(k))
        return self


class DescribeVisitTopIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVisitTopIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVisitTopIpResponse, self).to_map()
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
            temp_model = DescribeVisitTopIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVisitUasRequest(TeaModel):
    def __init__(self, end_timestamp=None, instance_id=None, resource=None, start_timestamp=None):
        self.end_timestamp = end_timestamp  # type: str
        self.instance_id = instance_id  # type: str
        self.resource = resource  # type: str
        self.start_timestamp = start_timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVisitUasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeVisitUasResponseBodyUas(TeaModel):
    def __init__(self, count=None, ua=None):
        self.count = count  # type: long
        self.ua = ua  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVisitUasResponseBodyUas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.ua is not None:
            result['Ua'] = self.ua
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Ua') is not None:
            self.ua = m.get('Ua')
        return self


class DescribeVisitUasResponseBody(TeaModel):
    def __init__(self, request_id=None, uas=None):
        self.request_id = request_id  # type: str
        self.uas = uas  # type: list[DescribeVisitUasResponseBodyUas]

    def validate(self):
        if self.uas:
            for k in self.uas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVisitUasResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Uas'] = []
        if self.uas is not None:
            for k in self.uas:
                result['Uas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.uas = []
        if m.get('Uas') is not None:
            for k in m.get('Uas'):
                temp_model = DescribeVisitUasResponseBodyUas()
                self.uas.append(temp_model.from_map(k))
        return self


class DescribeVisitUasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVisitUasResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVisitUasResponse, self).to_map()
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
            temp_model = DescribeVisitUasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWafSourceIpSegmentRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWafSourceIpSegmentRequest, self).to_map()
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


class DescribeWafSourceIpSegmentResponseBodyWafSourceIp(TeaModel):
    def __init__(self, ipv_4=None, ipv_6=None):
        self.ipv_4 = ipv_4  # type: list[str]
        self.ipv_6 = ipv_6  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWafSourceIpSegmentResponseBodyWafSourceIp, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipv_4 is not None:
            result['IPv4'] = self.ipv_4
        if self.ipv_6 is not None:
            result['IPv6'] = self.ipv_6
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IPv4') is not None:
            self.ipv_4 = m.get('IPv4')
        if m.get('IPv6') is not None:
            self.ipv_6 = m.get('IPv6')
        return self


class DescribeWafSourceIpSegmentResponseBody(TeaModel):
    def __init__(self, request_id=None, waf_source_ip=None):
        self.request_id = request_id  # type: str
        self.waf_source_ip = waf_source_ip  # type: DescribeWafSourceIpSegmentResponseBodyWafSourceIp

    def validate(self):
        if self.waf_source_ip:
            self.waf_source_ip.validate()

    def to_map(self):
        _map = super(DescribeWafSourceIpSegmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.waf_source_ip is not None:
            result['WafSourceIp'] = self.waf_source_ip.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WafSourceIp') is not None:
            temp_model = DescribeWafSourceIpSegmentResponseBodyWafSourceIp()
            self.waf_source_ip = temp_model.from_map(m['WafSourceIp'])
        return self


class DescribeWafSourceIpSegmentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWafSourceIpSegmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWafSourceIpSegmentResponse, self).to_map()
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
            temp_model = DescribeWafSourceIpSegmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDefenseResourceGroupRequest(TeaModel):
    def __init__(self, add_list=None, delete_list=None, description=None, group_name=None, instance_id=None):
        self.add_list = add_list  # type: str
        self.delete_list = delete_list  # type: str
        self.description = description  # type: str
        self.group_name = group_name  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDefenseResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_list is not None:
            result['AddList'] = self.add_list
        if self.delete_list is not None:
            result['DeleteList'] = self.delete_list
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddList') is not None:
            self.add_list = m.get('AddList')
        if m.get('DeleteList') is not None:
            self.delete_list = m.get('DeleteList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyDefenseResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDefenseResourceGroupResponseBody, self).to_map()
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


class ModifyDefenseResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDefenseResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDefenseResourceGroupResponse, self).to_map()
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
            temp_model = ModifyDefenseResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDefenseRuleRequest(TeaModel):
    def __init__(self, defense_scene=None, instance_id=None, rules=None, template_id=None):
        self.defense_scene = defense_scene  # type: str
        self.instance_id = instance_id  # type: str
        self.rules = rules  # type: str
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDefenseRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ModifyDefenseRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDefenseRuleResponseBody, self).to_map()
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


class ModifyDefenseRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDefenseRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDefenseRuleResponse, self).to_map()
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
            temp_model = ModifyDefenseRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDefenseRuleStatusRequest(TeaModel):
    def __init__(self, instance_id=None, rule_id=None, rule_status=None, template_id=None):
        self.instance_id = instance_id  # type: str
        self.rule_id = rule_id  # type: long
        self.rule_status = rule_status  # type: int
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDefenseRuleStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ModifyDefenseRuleStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDefenseRuleStatusResponseBody, self).to_map()
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


class ModifyDefenseRuleStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDefenseRuleStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDefenseRuleStatusResponse, self).to_map()
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
            temp_model = ModifyDefenseRuleStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDefenseTemplateRequest(TeaModel):
    def __init__(self, description=None, instance_id=None, template_id=None, template_name=None):
        self.description = description  # type: str
        self.instance_id = instance_id  # type: str
        self.template_id = template_id  # type: long
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDefenseTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ModifyDefenseTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDefenseTemplateResponseBody, self).to_map()
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


class ModifyDefenseTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDefenseTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDefenseTemplateResponse, self).to_map()
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
            temp_model = ModifyDefenseTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDefenseTemplateStatusRequest(TeaModel):
    def __init__(self, instance_id=None, template_id=None, template_status=None):
        self.instance_id = instance_id  # type: str
        self.template_id = template_id  # type: long
        self.template_status = template_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDefenseTemplateStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')
        return self


class ModifyDefenseTemplateStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDefenseTemplateStatusResponseBody, self).to_map()
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


class ModifyDefenseTemplateStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDefenseTemplateStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDefenseTemplateStatusResponse, self).to_map()
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
            temp_model = ModifyDefenseTemplateStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDomainRequestListen(TeaModel):
    def __init__(self, cert_id=None, cipher_suite=None, custom_ciphers=None, enable_tlsv_3=None, exclusive_ip=None,
                 focus_https=None, http_2enabled=None, http_ports=None, https_ports=None, ipv_6enabled=None,
                 protection_resource=None, tlsversion=None, xff_header_mode=None, xff_headers=None):
        self.cert_id = cert_id  # type: str
        self.cipher_suite = cipher_suite  # type: int
        self.custom_ciphers = custom_ciphers  # type: list[str]
        self.enable_tlsv_3 = enable_tlsv_3  # type: bool
        self.exclusive_ip = exclusive_ip  # type: bool
        self.focus_https = focus_https  # type: bool
        self.http_2enabled = http_2enabled  # type: bool
        self.http_ports = http_ports  # type: list[int]
        self.https_ports = https_ports  # type: list[int]
        self.ipv_6enabled = ipv_6enabled  # type: bool
        self.protection_resource = protection_resource  # type: str
        self.tlsversion = tlsversion  # type: str
        self.xff_header_mode = xff_header_mode  # type: int
        self.xff_headers = xff_headers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDomainRequestListen, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cipher_suite is not None:
            result['CipherSuite'] = self.cipher_suite
        if self.custom_ciphers is not None:
            result['CustomCiphers'] = self.custom_ciphers
        if self.enable_tlsv_3 is not None:
            result['EnableTLSv3'] = self.enable_tlsv_3
        if self.exclusive_ip is not None:
            result['ExclusiveIp'] = self.exclusive_ip
        if self.focus_https is not None:
            result['FocusHttps'] = self.focus_https
        if self.http_2enabled is not None:
            result['Http2Enabled'] = self.http_2enabled
        if self.http_ports is not None:
            result['HttpPorts'] = self.http_ports
        if self.https_ports is not None:
            result['HttpsPorts'] = self.https_ports
        if self.ipv_6enabled is not None:
            result['IPv6Enabled'] = self.ipv_6enabled
        if self.protection_resource is not None:
            result['ProtectionResource'] = self.protection_resource
        if self.tlsversion is not None:
            result['TLSVersion'] = self.tlsversion
        if self.xff_header_mode is not None:
            result['XffHeaderMode'] = self.xff_header_mode
        if self.xff_headers is not None:
            result['XffHeaders'] = self.xff_headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CipherSuite') is not None:
            self.cipher_suite = m.get('CipherSuite')
        if m.get('CustomCiphers') is not None:
            self.custom_ciphers = m.get('CustomCiphers')
        if m.get('EnableTLSv3') is not None:
            self.enable_tlsv_3 = m.get('EnableTLSv3')
        if m.get('ExclusiveIp') is not None:
            self.exclusive_ip = m.get('ExclusiveIp')
        if m.get('FocusHttps') is not None:
            self.focus_https = m.get('FocusHttps')
        if m.get('Http2Enabled') is not None:
            self.http_2enabled = m.get('Http2Enabled')
        if m.get('HttpPorts') is not None:
            self.http_ports = m.get('HttpPorts')
        if m.get('HttpsPorts') is not None:
            self.https_ports = m.get('HttpsPorts')
        if m.get('IPv6Enabled') is not None:
            self.ipv_6enabled = m.get('IPv6Enabled')
        if m.get('ProtectionResource') is not None:
            self.protection_resource = m.get('ProtectionResource')
        if m.get('TLSVersion') is not None:
            self.tlsversion = m.get('TLSVersion')
        if m.get('XffHeaderMode') is not None:
            self.xff_header_mode = m.get('XffHeaderMode')
        if m.get('XffHeaders') is not None:
            self.xff_headers = m.get('XffHeaders')
        return self


class ModifyDomainRequestRedirectRequestHeaders(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDomainRequestRedirectRequestHeaders, self).to_map()
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


class ModifyDomainRequestRedirect(TeaModel):
    def __init__(self, backends=None, connect_timeout=None, focus_http_backend=None, loadbalance=None,
                 read_timeout=None, request_headers=None, sni_enabled=None, sni_host=None, write_timeout=None):
        self.backends = backends  # type: list[str]
        self.connect_timeout = connect_timeout  # type: int
        self.focus_http_backend = focus_http_backend  # type: bool
        self.loadbalance = loadbalance  # type: str
        self.read_timeout = read_timeout  # type: int
        self.request_headers = request_headers  # type: list[ModifyDomainRequestRedirectRequestHeaders]
        self.sni_enabled = sni_enabled  # type: bool
        self.sni_host = sni_host  # type: str
        self.write_timeout = write_timeout  # type: int

    def validate(self):
        if self.request_headers:
            for k in self.request_headers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyDomainRequestRedirect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backends is not None:
            result['Backends'] = self.backends
        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout
        if self.focus_http_backend is not None:
            result['FocusHttpBackend'] = self.focus_http_backend
        if self.loadbalance is not None:
            result['Loadbalance'] = self.loadbalance
        if self.read_timeout is not None:
            result['ReadTimeout'] = self.read_timeout
        result['RequestHeaders'] = []
        if self.request_headers is not None:
            for k in self.request_headers:
                result['RequestHeaders'].append(k.to_map() if k else None)
        if self.sni_enabled is not None:
            result['SniEnabled'] = self.sni_enabled
        if self.sni_host is not None:
            result['SniHost'] = self.sni_host
        if self.write_timeout is not None:
            result['WriteTimeout'] = self.write_timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Backends') is not None:
            self.backends = m.get('Backends')
        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')
        if m.get('FocusHttpBackend') is not None:
            self.focus_http_backend = m.get('FocusHttpBackend')
        if m.get('Loadbalance') is not None:
            self.loadbalance = m.get('Loadbalance')
        if m.get('ReadTimeout') is not None:
            self.read_timeout = m.get('ReadTimeout')
        self.request_headers = []
        if m.get('RequestHeaders') is not None:
            for k in m.get('RequestHeaders'):
                temp_model = ModifyDomainRequestRedirectRequestHeaders()
                self.request_headers.append(temp_model.from_map(k))
        if m.get('SniEnabled') is not None:
            self.sni_enabled = m.get('SniEnabled')
        if m.get('SniHost') is not None:
            self.sni_host = m.get('SniHost')
        if m.get('WriteTimeout') is not None:
            self.write_timeout = m.get('WriteTimeout')
        return self


class ModifyDomainRequest(TeaModel):
    def __init__(self, access_type=None, domain=None, instance_id=None, listen=None, redirect=None, region_id=None):
        self.access_type = access_type  # type: str
        self.domain = domain  # type: str
        self.instance_id = instance_id  # type: str
        self.listen = listen  # type: ModifyDomainRequestListen
        self.redirect = redirect  # type: ModifyDomainRequestRedirect
        self.region_id = region_id  # type: str

    def validate(self):
        if self.listen:
            self.listen.validate()
        if self.redirect:
            self.redirect.validate()

    def to_map(self):
        _map = super(ModifyDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.listen is not None:
            result['Listen'] = self.listen.to_map()
        if self.redirect is not None:
            result['Redirect'] = self.redirect.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Listen') is not None:
            temp_model = ModifyDomainRequestListen()
            self.listen = temp_model.from_map(m['Listen'])
        if m.get('Redirect') is not None:
            temp_model = ModifyDomainRequestRedirect()
            self.redirect = temp_model.from_map(m['Redirect'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDomainShrinkRequest(TeaModel):
    def __init__(self, access_type=None, domain=None, instance_id=None, listen_shrink=None, redirect_shrink=None,
                 region_id=None):
        self.access_type = access_type  # type: str
        self.domain = domain  # type: str
        self.instance_id = instance_id  # type: str
        self.listen_shrink = listen_shrink  # type: str
        self.redirect_shrink = redirect_shrink  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDomainShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.listen_shrink is not None:
            result['Listen'] = self.listen_shrink
        if self.redirect_shrink is not None:
            result['Redirect'] = self.redirect_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Listen') is not None:
            self.listen_shrink = m.get('Listen')
        if m.get('Redirect') is not None:
            self.redirect_shrink = m.get('Redirect')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDomainResponseBodyDomainInfo(TeaModel):
    def __init__(self, cname=None, domain=None):
        self.cname = cname  # type: str
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDomainResponseBodyDomainInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class ModifyDomainResponseBody(TeaModel):
    def __init__(self, domain_info=None, request_id=None):
        self.domain_info = domain_info  # type: ModifyDomainResponseBodyDomainInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_info:
            self.domain_info.validate()

    def to_map(self):
        _map = super(ModifyDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_info is not None:
            result['DomainInfo'] = self.domain_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainInfo') is not None:
            temp_model = ModifyDomainResponseBodyDomainInfo()
            self.domain_info = temp_model.from_map(m['DomainInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDomainResponse, self).to_map()
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
            temp_model = ModifyDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMajorProtectionBlackIpRequest(TeaModel):
    def __init__(self, description=None, expired_time=None, instance_id=None, ip_list=None, rule_id=None,
                 template_id=None):
        self.description = description  # type: str
        self.expired_time = expired_time  # type: long
        self.instance_id = instance_id  # type: str
        self.ip_list = ip_list  # type: str
        self.rule_id = rule_id  # type: long
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyMajorProtectionBlackIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ModifyMajorProtectionBlackIpResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyMajorProtectionBlackIpResponseBody, self).to_map()
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


class ModifyMajorProtectionBlackIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyMajorProtectionBlackIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyMajorProtectionBlackIpResponse, self).to_map()
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
            temp_model = ModifyMajorProtectionBlackIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyResourceLogStatusRequest(TeaModel):
    def __init__(self, instance_id=None, resource=None, status=None):
        self.instance_id = instance_id  # type: str
        self.resource = resource  # type: str
        self.status = status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyResourceLogStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyResourceLogStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, status=None):
        self.request_id = request_id  # type: str
        self.status = status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyResourceLogStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyResourceLogStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyResourceLogStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyResourceLogStatusResponse, self).to_map()
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
            temp_model = ModifyResourceLogStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTemplateResourcesRequest(TeaModel):
    def __init__(self, bind_resource_groups=None, bind_resources=None, instance_id=None, template_id=None,
                 unbind_resource_groups=None, unbind_resources=None):
        self.bind_resource_groups = bind_resource_groups  # type: list[str]
        self.bind_resources = bind_resources  # type: list[str]
        self.instance_id = instance_id  # type: str
        self.template_id = template_id  # type: long
        self.unbind_resource_groups = unbind_resource_groups  # type: list[str]
        self.unbind_resources = unbind_resources  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTemplateResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_resource_groups is not None:
            result['BindResourceGroups'] = self.bind_resource_groups
        if self.bind_resources is not None:
            result['BindResources'] = self.bind_resources
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.unbind_resource_groups is not None:
            result['UnbindResourceGroups'] = self.unbind_resource_groups
        if self.unbind_resources is not None:
            result['UnbindResources'] = self.unbind_resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindResourceGroups') is not None:
            self.bind_resource_groups = m.get('BindResourceGroups')
        if m.get('BindResources') is not None:
            self.bind_resources = m.get('BindResources')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UnbindResourceGroups') is not None:
            self.unbind_resource_groups = m.get('UnbindResourceGroups')
        if m.get('UnbindResources') is not None:
            self.unbind_resources = m.get('UnbindResources')
        return self


class ModifyTemplateResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTemplateResourcesResponseBody, self).to_map()
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


class ModifyTemplateResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyTemplateResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTemplateResourcesResponse, self).to_map()
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
            temp_model = ModifyTemplateResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


