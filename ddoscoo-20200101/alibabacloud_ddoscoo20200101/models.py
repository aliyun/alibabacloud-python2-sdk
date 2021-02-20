# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class AddAutoCcBlacklistRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None, blacklist=None, expire_time=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.blacklist = TeaConverter.to_unicode(blacklist)  # type: unicode
        self.expire_time = expire_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.blacklist is not None:
            result['Blacklist'] = self.blacklist
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Blacklist') is not None:
            self.blacklist = m.get('Blacklist')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class AddAutoCcBlacklistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddAutoCcBlacklistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AddAutoCcBlacklistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddAutoCcBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddAutoCcWhitelistRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None, whitelist=None, expire_time=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.whitelist = TeaConverter.to_unicode(whitelist)  # type: unicode
        self.expire_time = expire_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class AddAutoCcWhitelistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddAutoCcWhitelistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AddAutoCcWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddAutoCcWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateWebCertRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, cert_id=None, cert_name=None, cert=None,
                 key=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.cert_id = cert_id  # type: int
        self.cert_name = TeaConverter.to_unicode(cert_name)  # type: unicode
        self.cert = TeaConverter.to_unicode(cert)  # type: unicode
        self.key = TeaConverter.to_unicode(key)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class AssociateWebCertResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateWebCertResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AssociateWebCertResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AssociateWebCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachSceneDefenseObjectRequest(TeaModel):
    def __init__(self, source_ip=None, policy_id=None, object_type=None, objects=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.policy_id = TeaConverter.to_unicode(policy_id)  # type: unicode
        self.object_type = TeaConverter.to_unicode(object_type)  # type: unicode
        self.objects = TeaConverter.to_unicode(objects)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.objects is not None:
            result['Objects'] = self.objects
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Objects') is not None:
            self.objects = m.get('Objects')
        return self


class AttachSceneDefenseObjectResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AttachSceneDefenseObjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AttachSceneDefenseObjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachSceneDefenseObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigL7RsPolicyRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, policy=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.policy = TeaConverter.to_unicode(policy)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.policy is not None:
            result['Policy'] = self.policy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        return self


class ConfigL7RsPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigL7RsPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ConfigL7RsPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfigL7RsPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigNetworkRegionBlockRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None, config=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.config = TeaConverter.to_unicode(config)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ConfigNetworkRegionBlockResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigNetworkRegionBlockResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ConfigNetworkRegionBlockResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfigNetworkRegionBlockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigNetworkRulesRequest(TeaModel):
    def __init__(self, source_ip=None, network_rules=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.network_rules = TeaConverter.to_unicode(network_rules)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('NetworkRules') is not None:
            self.network_rules = m.get('NetworkRules')
        return self


class ConfigNetworkRulesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigNetworkRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ConfigNetworkRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfigNetworkRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigWebCCTemplateRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, template=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.template = TeaConverter.to_unicode(template)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class ConfigWebCCTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigWebCCTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ConfigWebCCTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfigWebCCTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigWebIpSetRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, black_list=None, white_list=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.black_list = black_list  # type: list[unicode]
        self.white_list = white_list  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.black_list is not None:
            result['BlackList'] = self.black_list
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class ConfigWebIpSetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigWebIpSetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ConfigWebIpSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfigWebIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAsyncTaskRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None, task_type=None, task_params=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.task_type = task_type  # type: int
        self.task_params = TeaConverter.to_unicode(task_params)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        return self


class CreateAsyncTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAsyncTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateAsyncTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNetworkRulesRequest(TeaModel):
    def __init__(self, source_ip=None, network_rules=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.network_rules = TeaConverter.to_unicode(network_rules)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('NetworkRules') is not None:
            self.network_rules = m.get('NetworkRules')
        return self


class CreateNetworkRulesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNetworkRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateNetworkRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateNetworkRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSceneDefensePolicyRequest(TeaModel):
    def __init__(self, source_ip=None, name=None, template=None, start_time=None, end_time=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.template = TeaConverter.to_unicode(template)  # type: unicode
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.name is not None:
            result['Name'] = self.name
        if self.template is not None:
            result['Template'] = self.template
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class CreateSceneDefensePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSceneDefensePolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateSceneDefensePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSceneDefensePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSchedulerRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, rules=None, rule_name=None, rule_type=None,
                 param=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.rules = TeaConverter.to_unicode(rules)  # type: unicode
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode
        self.rule_type = rule_type  # type: int
        self.param = TeaConverter.to_unicode(param)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.param is not None:
            result['Param'] = self.param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        return self


class CreateSchedulerRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, cname=None, rule_name=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.cname = TeaConverter.to_unicode(cname)  # type: unicode
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class CreateSchedulerRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateSchedulerRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSchedulerRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTagResourcesRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.value = TeaConverter.to_unicode(value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class CreateTagResourcesRequest(TeaModel):
    def __init__(self, source_ip=None, region_id=None, resource_group_id=None, resource_type=None,
                 resource_ids=None, tags=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.resource_ids = resource_ids  # type: list[unicode]
        self.tags = tags  # type: list[CreateTagResourcesRequestTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateTagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateTagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWebCCRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, name=None, act=None, count=None,
                 interval=None, mode=None, ttl=None, uri=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.act = TeaConverter.to_unicode(act)  # type: unicode
        self.count = count  # type: int
        self.interval = interval  # type: int
        self.mode = TeaConverter.to_unicode(mode)  # type: unicode
        self.ttl = ttl  # type: int
        self.uri = TeaConverter.to_unicode(uri)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.name is not None:
            result['Name'] = self.name
        if self.act is not None:
            result['Act'] = self.act
        if self.count is not None:
            result['Count'] = self.count
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CreateWebCCRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWebCCRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateWebCCRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateWebCCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWebRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, rs_type=None, rules=None, https_ext=None,
                 defense_id=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.rs_type = rs_type  # type: int
        self.rules = TeaConverter.to_unicode(rules)  # type: unicode
        self.https_ext = TeaConverter.to_unicode(https_ext)  # type: unicode
        self.defense_id = TeaConverter.to_unicode(defense_id)  # type: unicode
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.https_ext is not None:
            result['HttpsExt'] = self.https_ext
        if self.defense_id is not None:
            result['DefenseId'] = self.defense_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('HttpsExt') is not None:
            self.https_ext = m.get('HttpsExt')
        if m.get('DefenseId') is not None:
            self.defense_id = m.get('DefenseId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class CreateWebRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWebRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateWebRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateWebRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAsyncTaskRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None, task_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.task_id = task_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteAsyncTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAsyncTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteAsyncTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutoCcBlacklistRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None, blacklist=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.blacklist = TeaConverter.to_unicode(blacklist)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.blacklist is not None:
            result['Blacklist'] = self.blacklist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Blacklist') is not None:
            self.blacklist = m.get('Blacklist')
        return self


class DeleteAutoCcBlacklistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAutoCcBlacklistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteAutoCcBlacklistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAutoCcBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutoCcWhitelistRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None, whitelist=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.whitelist = TeaConverter.to_unicode(whitelist)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class DeleteAutoCcWhitelistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAutoCcWhitelistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteAutoCcWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAutoCcWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNetworkRuleRequest(TeaModel):
    def __init__(self, source_ip=None, network_rule=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.network_rule = TeaConverter.to_unicode(network_rule)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.network_rule is not None:
            result['NetworkRule'] = self.network_rule
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('NetworkRule') is not None:
            self.network_rule = m.get('NetworkRule')
        return self


class DeleteNetworkRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNetworkRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteNetworkRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNetworkRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSceneDefensePolicyRequest(TeaModel):
    def __init__(self, source_ip=None, policy_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.policy_id = TeaConverter.to_unicode(policy_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DeleteSceneDefensePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSceneDefensePolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteSceneDefensePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSceneDefensePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSchedulerRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, rule_name=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DeleteSchedulerRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSchedulerRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteSchedulerRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSchedulerRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTagResourcesRequest(TeaModel):
    def __init__(self, source_ip=None, region_id=None, resource_group_id=None, resource_type=None, all=None,
                 resource_ids=None, tag_key=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.all = all  # type: bool
        self.resource_ids = resource_ids  # type: list[unicode]
        self.tag_key = tag_key  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class DeleteTagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebCacheCustomRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, rule_names=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.rule_names = rule_names  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.rule_names is not None:
            result['RuleNames'] = self.rule_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RuleNames') is not None:
            self.rule_names = m.get('RuleNames')
        return self


class DeleteWebCacheCustomRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWebCacheCustomRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteWebCacheCustomRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteWebCacheCustomRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebCCRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, name=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteWebCCRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWebCCRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteWebCCRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteWebCCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebPreciseAccessRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, rule_names=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.rule_names = rule_names  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.rule_names is not None:
            result['RuleNames'] = self.rule_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RuleNames') is not None:
            self.rule_names = m.get('RuleNames')
        return self


class DeleteWebPreciseAccessRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWebPreciseAccessRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteWebPreciseAccessRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteWebPreciseAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DeleteWebRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWebRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteWebRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteWebRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAsyncTasksRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None, page_number=None, page_size=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAsyncTasksResponseBodyAsyncTasks(TeaModel):
    def __init__(self, end_time=None, task_type=None, start_time=None, task_params=None, task_status=None,
                 task_result=None, task_id=None):
        self.end_time = end_time  # type: long
        self.task_type = task_type  # type: int
        self.start_time = start_time  # type: long
        self.task_params = TeaConverter.to_unicode(task_params)  # type: unicode
        self.task_status = task_status  # type: int
        self.task_result = TeaConverter.to_unicode(task_result)  # type: unicode
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_result is not None:
            result['TaskResult'] = self.task_result
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeAsyncTasksResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, async_tasks=None):
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.async_tasks = async_tasks  # type: list[DescribeAsyncTasksResponseBodyAsyncTasks]

    def validate(self):
        if self.async_tasks:
            for k in self.async_tasks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AsyncTasks'] = []
        if self.async_tasks is not None:
            for k in self.async_tasks:
                result['AsyncTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.async_tasks = []
        if m.get('AsyncTasks') is not None:
            for k in m.get('AsyncTasks'):
                temp_model = DescribeAsyncTasksResponseBodyAsyncTasks()
                self.async_tasks.append(temp_model.from_map(k))
        return self


class DescribeAsyncTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAsyncTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAsyncTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoCcBlacklistRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None, key_word=None, page_number=None, page_size=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.key_word = TeaConverter.to_unicode(key_word)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAutoCcBlacklistResponseBodyAutoCcBlacklist(TeaModel):
    def __init__(self, type=None, end_time=None, source_ip=None, dest_ip=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.end_time = end_time  # type: long
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.dest_ip = TeaConverter.to_unicode(dest_ip)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.dest_ip is not None:
            result['DestIp'] = self.dest_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('DestIp') is not None:
            self.dest_ip = m.get('DestIp')
        return self


class DescribeAutoCcBlacklistResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, auto_cc_blacklist=None):
        self.total_count = total_count  # type: long
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.auto_cc_blacklist = auto_cc_blacklist  # type: list[DescribeAutoCcBlacklistResponseBodyAutoCcBlacklist]

    def validate(self):
        if self.auto_cc_blacklist:
            for k in self.auto_cc_blacklist:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AutoCcBlacklist'] = []
        if self.auto_cc_blacklist is not None:
            for k in self.auto_cc_blacklist:
                result['AutoCcBlacklist'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.auto_cc_blacklist = []
        if m.get('AutoCcBlacklist') is not None:
            for k in m.get('AutoCcBlacklist'):
                temp_model = DescribeAutoCcBlacklistResponseBodyAutoCcBlacklist()
                self.auto_cc_blacklist.append(temp_model.from_map(k))
        return self


class DescribeAutoCcBlacklistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAutoCcBlacklistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAutoCcBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoCcListCountRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None, query_type=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.query_type = TeaConverter.to_unicode(query_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        return self


class DescribeAutoCcListCountResponseBody(TeaModel):
    def __init__(self, black_count=None, request_id=None, white_count=None):
        self.black_count = black_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.white_count = white_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.black_count is not None:
            result['BlackCount'] = self.black_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.white_count is not None:
            result['WhiteCount'] = self.white_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackCount') is not None:
            self.black_count = m.get('BlackCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WhiteCount') is not None:
            self.white_count = m.get('WhiteCount')
        return self


class DescribeAutoCcListCountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAutoCcListCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAutoCcListCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoCcWhitelistRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None, key_word=None, page_number=None, page_size=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.key_word = TeaConverter.to_unicode(key_word)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAutoCcWhitelistResponseBodyAutoCcWhitelist(TeaModel):
    def __init__(self, type=None, end_time=None, source_ip=None, dest_ip=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.end_time = end_time  # type: long
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.dest_ip = TeaConverter.to_unicode(dest_ip)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.dest_ip is not None:
            result['DestIp'] = self.dest_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('DestIp') is not None:
            self.dest_ip = m.get('DestIp')
        return self


class DescribeAutoCcWhitelistResponseBody(TeaModel):
    def __init__(self, auto_cc_whitelist=None, total_count=None, request_id=None):
        self.auto_cc_whitelist = auto_cc_whitelist  # type: list[DescribeAutoCcWhitelistResponseBodyAutoCcWhitelist]
        self.total_count = total_count  # type: long
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.auto_cc_whitelist:
            for k in self.auto_cc_whitelist:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AutoCcWhitelist'] = []
        if self.auto_cc_whitelist is not None:
            for k in self.auto_cc_whitelist:
                result['AutoCcWhitelist'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.auto_cc_whitelist = []
        if m.get('AutoCcWhitelist') is not None:
            for k in m.get('AutoCcWhitelist'):
                temp_model = DescribeAutoCcWhitelistResponseBodyAutoCcWhitelist()
                self.auto_cc_whitelist.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAutoCcWhitelistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeAutoCcWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAutoCcWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackSourceCidrRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, line=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.line = TeaConverter.to_unicode(line)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        return self


class DescribeBackSourceCidrResponseBody(TeaModel):
    def __init__(self, request_id=None, cidrs=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.cidrs = cidrs  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        return self


class DescribeBackSourceCidrResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeBackSourceCidrResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBackSourceCidrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBlackholeStatusRequest(TeaModel):
    def __init__(self, source_ip=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeBlackholeStatusResponseBodyBlackholeStatus(TeaModel):
    def __init__(self, end_time=None, start_time=None, ip=None, black_status=None):
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.ip = TeaConverter.to_unicode(ip)  # type: unicode
        self.black_status = TeaConverter.to_unicode(black_status)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.black_status is not None:
            result['BlackStatus'] = self.black_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('BlackStatus') is not None:
            self.black_status = m.get('BlackStatus')
        return self


class DescribeBlackholeStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, blackhole_status=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.blackhole_status = blackhole_status  # type: list[DescribeBlackholeStatusResponseBodyBlackholeStatus]

    def validate(self):
        if self.blackhole_status:
            for k in self.blackhole_status:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['BlackholeStatus'] = []
        if self.blackhole_status is not None:
            for k in self.blackhole_status:
                result['BlackholeStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.blackhole_status = []
        if m.get('BlackholeStatus') is not None:
            for k in m.get('BlackholeStatus'):
                temp_model = DescribeBlackholeStatusResponseBodyBlackholeStatus()
                self.blackhole_status.append(temp_model.from_map(k))
        return self


class DescribeBlackholeStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeBlackholeStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBlackholeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBlockStatusRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeBlockStatusResponseBodyStatusListBlockStatusList(TeaModel):
    def __init__(self, end_time=None, start_time=None, line=None, block_status=None):
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.line = TeaConverter.to_unicode(line)  # type: unicode
        self.block_status = TeaConverter.to_unicode(block_status)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.line is not None:
            result['Line'] = self.line
        if self.block_status is not None:
            result['BlockStatus'] = self.block_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('BlockStatus') is not None:
            self.block_status = m.get('BlockStatus')
        return self


class DescribeBlockStatusResponseBodyStatusList(TeaModel):
    def __init__(self, ip=None, block_status_list=None):
        self.ip = TeaConverter.to_unicode(ip)  # type: unicode
        self.block_status_list = block_status_list  # type: list[DescribeBlockStatusResponseBodyStatusListBlockStatusList]

    def validate(self):
        if self.block_status_list:
            for k in self.block_status_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        result['BlockStatusList'] = []
        if self.block_status_list is not None:
            for k in self.block_status_list:
                result['BlockStatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        self.block_status_list = []
        if m.get('BlockStatusList') is not None:
            for k in m.get('BlockStatusList'):
                temp_model = DescribeBlockStatusResponseBodyStatusListBlockStatusList()
                self.block_status_list.append(temp_model.from_map(k))
        return self


class DescribeBlockStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, status_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.status_list = status_list  # type: list[DescribeBlockStatusResponseBodyStatusList]

    def validate(self):
        if self.status_list:
            for k in self.status_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StatusList'] = []
        if self.status_list is not None:
            for k in self.status_list:
                result['StatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.status_list = []
        if m.get('StatusList') is not None:
            for k in m.get('StatusList'):
                temp_model = DescribeBlockStatusResponseBodyStatusList()
                self.status_list.append(temp_model.from_map(k))
        return self


class DescribeBlockStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeBlockStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBlockStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertsRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeCertsResponseBodyCerts(TeaModel):
    def __init__(self, end_date=None, domain_related=None, start_date=None, issuer=None, name=None, common=None,
                 id=None):
        self.end_date = TeaConverter.to_unicode(end_date)  # type: unicode
        self.domain_related = domain_related  # type: bool
        self.start_date = TeaConverter.to_unicode(start_date)  # type: unicode
        self.issuer = TeaConverter.to_unicode(issuer)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.common = TeaConverter.to_unicode(common)  # type: unicode
        self.id = id  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.domain_related is not None:
            result['DomainRelated'] = self.domain_related
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.name is not None:
            result['Name'] = self.name
        if self.common is not None:
            result['Common'] = self.common
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('DomainRelated') is not None:
            self.domain_related = m.get('DomainRelated')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeCertsResponseBody(TeaModel):
    def __init__(self, certs=None, request_id=None):
        self.certs = certs  # type: list[DescribeCertsResponseBodyCerts]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.certs:
            for k in self.certs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Certs'] = []
        if self.certs is not None:
            for k in self.certs:
                result['Certs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.certs = []
        if m.get('Certs') is not None:
            for k in m.get('Certs'):
                temp_model = DescribeCertsResponseBodyCerts()
                self.certs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCertsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeCertsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCertsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCnameReusesRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domains=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domains = domains  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class DescribeCnameReusesResponseBodyCnameReuses(TeaModel):
    def __init__(self, domain=None, cname=None, enable=None):
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.cname = TeaConverter.to_unicode(cname)  # type: unicode
        self.enable = enable  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DescribeCnameReusesResponseBody(TeaModel):
    def __init__(self, request_id=None, cname_reuses=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.cname_reuses = cname_reuses  # type: list[DescribeCnameReusesResponseBodyCnameReuses]

    def validate(self):
        if self.cname_reuses:
            for k in self.cname_reuses:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['CnameReuses'] = []
        if self.cname_reuses is not None:
            for k in self.cname_reuses:
                result['CnameReuses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.cname_reuses = []
        if m.get('CnameReuses') is not None:
            for k in m.get('CnameReuses'):
                temp_model = DescribeCnameReusesResponseBodyCnameReuses()
                self.cname_reuses.append(temp_model.from_map(k))
        return self


class DescribeCnameReusesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeCnameReusesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCnameReusesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosAllEventListRequest(TeaModel):
    def __init__(self, source_ip=None, event_type=None, start_time=None, end_time=None, page_number=None,
                 page_size=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.event_type = TeaConverter.to_unicode(event_type)  # type: unicode
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDDosAllEventListResponseBodyAttackEvents(TeaModel):
    def __init__(self, end_time=None, start_time=None, event_type=None, mbps=None, ip=None, port=None, pps=None):
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.event_type = TeaConverter.to_unicode(event_type)  # type: unicode
        self.mbps = mbps  # type: long
        self.ip = TeaConverter.to_unicode(ip)  # type: unicode
        self.port = TeaConverter.to_unicode(port)  # type: unicode
        self.pps = pps  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.mbps is not None:
            result['Mbps'] = self.mbps
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class DescribeDDosAllEventListResponseBody(TeaModel):
    def __init__(self, request_id=None, total=None, attack_events=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.total = total  # type: long
        self.attack_events = attack_events  # type: list[DescribeDDosAllEventListResponseBodyAttackEvents]

    def validate(self):
        if self.attack_events:
            for k in self.attack_events:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['AttackEvents'] = []
        if self.attack_events is not None:
            for k in self.attack_events:
                result['AttackEvents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.attack_events = []
        if m.get('AttackEvents') is not None:
            for k in m.get('AttackEvents'):
                temp_model = DescribeDDosAllEventListResponseBodyAttackEvents()
                self.attack_events.append(temp_model.from_map(k))
        return self


class DescribeDDosAllEventListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDDosAllEventListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDDosAllEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosEventAreaRequest(TeaModel):
    def __init__(self, source_ip=None, event_type=None, start_time=None, ip=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.event_type = TeaConverter.to_unicode(event_type)  # type: unicode
        self.start_time = start_time  # type: long
        self.ip = TeaConverter.to_unicode(ip)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeDDosEventAreaResponseBodyAreas(TeaModel):
    def __init__(self, in_pkts=None, area=None):
        self.in_pkts = in_pkts  # type: long
        self.area = TeaConverter.to_unicode(area)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.in_pkts is not None:
            result['InPkts'] = self.in_pkts
        if self.area is not None:
            result['Area'] = self.area
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InPkts') is not None:
            self.in_pkts = m.get('InPkts')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        return self


class DescribeDDosEventAreaResponseBody(TeaModel):
    def __init__(self, request_id=None, areas=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.areas = areas  # type: list[DescribeDDosEventAreaResponseBodyAreas]

    def validate(self):
        if self.areas:
            for k in self.areas:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDDosEventAreaResponseBodyAreas()
                self.areas.append(temp_model.from_map(k))
        return self


class DescribeDDosEventAreaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDDosEventAreaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDDosEventAreaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosEventAttackTypeRequest(TeaModel):
    def __init__(self, source_ip=None, event_type=None, start_time=None, ip=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.event_type = TeaConverter.to_unicode(event_type)  # type: unicode
        self.start_time = start_time  # type: long
        self.ip = TeaConverter.to_unicode(ip)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeDDosEventAttackTypeResponseBodyAttackTypes(TeaModel):
    def __init__(self, attack_type=None, in_pkts=None):
        self.attack_type = TeaConverter.to_unicode(attack_type)  # type: unicode
        self.in_pkts = in_pkts  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.in_pkts is not None:
            result['InPkts'] = self.in_pkts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')
        if m.get('InPkts') is not None:
            self.in_pkts = m.get('InPkts')
        return self


class DescribeDDosEventAttackTypeResponseBody(TeaModel):
    def __init__(self, request_id=None, attack_types=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.attack_types = attack_types  # type: list[DescribeDDosEventAttackTypeResponseBodyAttackTypes]

    def validate(self):
        if self.attack_types:
            for k in self.attack_types:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AttackTypes'] = []
        if self.attack_types is not None:
            for k in self.attack_types:
                result['AttackTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.attack_types = []
        if m.get('AttackTypes') is not None:
            for k in m.get('AttackTypes'):
                temp_model = DescribeDDosEventAttackTypeResponseBodyAttackTypes()
                self.attack_types.append(temp_model.from_map(k))
        return self


class DescribeDDosEventAttackTypeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDDosEventAttackTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDDosEventAttackTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosEventIspRequest(TeaModel):
    def __init__(self, source_ip=None, event_type=None, start_time=None, ip=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.event_type = TeaConverter.to_unicode(event_type)  # type: unicode
        self.start_time = start_time  # type: long
        self.ip = TeaConverter.to_unicode(ip)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeDDosEventIspResponseBodyIsps(TeaModel):
    def __init__(self, in_pkts=None, isp=None):
        self.in_pkts = in_pkts  # type: long
        self.isp = TeaConverter.to_unicode(isp)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.in_pkts is not None:
            result['InPkts'] = self.in_pkts
        if self.isp is not None:
            result['Isp'] = self.isp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InPkts') is not None:
            self.in_pkts = m.get('InPkts')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        return self


class DescribeDDosEventIspResponseBody(TeaModel):
    def __init__(self, request_id=None, isps=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.isps = isps  # type: list[DescribeDDosEventIspResponseBodyIsps]

    def validate(self):
        if self.isps:
            for k in self.isps:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Isps'] = []
        if self.isps is not None:
            for k in self.isps:
                result['Isps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.isps = []
        if m.get('Isps') is not None:
            for k in m.get('Isps'):
                temp_model = DescribeDDosEventIspResponseBodyIsps()
                self.isps.append(temp_model.from_map(k))
        return self


class DescribeDDosEventIspResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDDosEventIspResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDDosEventIspResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosEventMaxRequest(TeaModel):
    def __init__(self, source_ip=None, start_time=None, end_time=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDDosEventMaxResponseBody(TeaModel):
    def __init__(self, request_id=None, qps=None, cps=None, mbps=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.qps = qps  # type: long
        self.cps = cps  # type: long
        self.mbps = mbps  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.mbps is not None:
            result['Mbps'] = self.mbps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')
        return self


class DescribeDDosEventMaxResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDDosEventMaxResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDDosEventMaxResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDoSEventsRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, end_time=None, start_time=None, page_size=None,
                 page_number=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeDDoSEventsResponseBodyDDoSEvents(TeaModel):
    def __init__(self, end_time=None, start_time=None, event_type=None, region=None, ip=None, port=None, bps=None,
                 pps=None):
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.event_type = TeaConverter.to_unicode(event_type)  # type: unicode
        self.region = TeaConverter.to_unicode(region)  # type: unicode
        self.ip = TeaConverter.to_unicode(ip)  # type: unicode
        self.port = TeaConverter.to_unicode(port)  # type: unicode
        self.bps = bps  # type: long
        self.pps = pps  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.region is not None:
            result['Region'] = self.region
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class DescribeDDoSEventsResponseBody(TeaModel):
    def __init__(self, request_id=None, total=None, ddo_sevents=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.total = total  # type: long
        self.ddo_sevents = ddo_sevents  # type: list[DescribeDDoSEventsResponseBodyDDoSEvents]

    def validate(self):
        if self.ddo_sevents:
            for k in self.ddo_sevents:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['DDoSEvents'] = []
        if self.ddo_sevents is not None:
            for k in self.ddo_sevents:
                result['DDoSEvents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.ddo_sevents = []
        if m.get('DDoSEvents') is not None:
            for k in m.get('DDoSEvents'):
                temp_model = DescribeDDoSEventsResponseBodyDDoSEvents()
                self.ddo_sevents.append(temp_model.from_map(k))
        return self


class DescribeDDoSEventsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDDoSEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDDoSEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosEventSrcIpRequest(TeaModel):
    def __init__(self, source_ip=None, event_type=None, start_time=None, ip=None, range=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.event_type = TeaConverter.to_unicode(event_type)  # type: unicode
        self.start_time = start_time  # type: long
        self.ip = TeaConverter.to_unicode(ip)  # type: unicode
        self.range = range  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.range is not None:
            result['Range'] = self.range
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Range') is not None:
            self.range = m.get('Range')
        return self


class DescribeDDosEventSrcIpResponseBodyIps(TeaModel):
    def __init__(self, src_ip=None, area_id=None, isp=None):
        self.src_ip = TeaConverter.to_unicode(src_ip)  # type: unicode
        self.area_id = TeaConverter.to_unicode(area_id)  # type: unicode
        self.isp = TeaConverter.to_unicode(isp)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.isp is not None:
            result['Isp'] = self.isp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        return self


class DescribeDDosEventSrcIpResponseBody(TeaModel):
    def __init__(self, request_id=None, ips=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.ips = ips  # type: list[DescribeDDosEventSrcIpResponseBodyIps]

    def validate(self):
        if self.ips:
            for k in self.ips:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Ips'] = []
        if self.ips is not None:
            for k in self.ips:
                result['Ips'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.ips = []
        if m.get('Ips') is not None:
            for k in m.get('Ips'):
                temp_model = DescribeDDosEventSrcIpResponseBodyIps()
                self.ips.append(temp_model.from_map(k))
        return self


class DescribeDDosEventSrcIpResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDDosEventSrcIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDDosEventSrcIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDefenseCountStatisticsRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDefenseCountStatisticsResponseBodyDefenseCountStatistics(TeaModel):
    def __init__(self, max_usable_defense_count_current_month=None, flow_pack_count_remain=None,
                 defense_count_total_usage_of_current_month=None):
        self.max_usable_defense_count_current_month = max_usable_defense_count_current_month  # type: int
        self.flow_pack_count_remain = flow_pack_count_remain  # type: int
        self.defense_count_total_usage_of_current_month = defense_count_total_usage_of_current_month  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_usable_defense_count_current_month is not None:
            result['MaxUsableDefenseCountCurrentMonth'] = self.max_usable_defense_count_current_month
        if self.flow_pack_count_remain is not None:
            result['FlowPackCountRemain'] = self.flow_pack_count_remain
        if self.defense_count_total_usage_of_current_month is not None:
            result['DefenseCountTotalUsageOfCurrentMonth'] = self.defense_count_total_usage_of_current_month
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxUsableDefenseCountCurrentMonth') is not None:
            self.max_usable_defense_count_current_month = m.get('MaxUsableDefenseCountCurrentMonth')
        if m.get('FlowPackCountRemain') is not None:
            self.flow_pack_count_remain = m.get('FlowPackCountRemain')
        if m.get('DefenseCountTotalUsageOfCurrentMonth') is not None:
            self.defense_count_total_usage_of_current_month = m.get('DefenseCountTotalUsageOfCurrentMonth')
        return self


class DescribeDefenseCountStatisticsResponseBody(TeaModel):
    def __init__(self, request_id=None, defense_count_statistics=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.defense_count_statistics = defense_count_statistics  # type: DescribeDefenseCountStatisticsResponseBodyDefenseCountStatistics

    def validate(self):
        if self.defense_count_statistics:
            self.defense_count_statistics.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.defense_count_statistics is not None:
            result['DefenseCountStatistics'] = self.defense_count_statistics.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DefenseCountStatistics') is not None:
            temp_model = DescribeDefenseCountStatisticsResponseBodyDefenseCountStatistics()
            self.defense_count_statistics = temp_model.from_map(m['DefenseCountStatistics'])
        return self


class DescribeDefenseCountStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDefenseCountStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDefenseCountStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDefenseRecordsRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None, instance_id=None, start_time=None,
                 end_time=None, page_number=None, page_size=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDefenseRecordsResponseBodyDefenseRecords(TeaModel):
    def __init__(self, end_time=None, status=None, start_time=None, event_count=None, instance_id=None,
                 attack_peak=None):
        self.end_time = end_time  # type: long
        self.status = status  # type: int
        self.start_time = start_time  # type: long
        self.event_count = event_count  # type: int
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.attack_peak = attack_peak  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.event_count is not None:
            result['EventCount'] = self.event_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.attack_peak is not None:
            result['AttackPeak'] = self.attack_peak
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EventCount') is not None:
            self.event_count = m.get('EventCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AttackPeak') is not None:
            self.attack_peak = m.get('AttackPeak')
        return self


class DescribeDefenseRecordsResponseBody(TeaModel):
    def __init__(self, total_count=None, defense_records=None, request_id=None):
        self.total_count = total_count  # type: long
        self.defense_records = defense_records  # type: list[DescribeDefenseRecordsResponseBodyDefenseRecords]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.defense_records:
            for k in self.defense_records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['DefenseRecords'] = []
        if self.defense_records is not None:
            for k in self.defense_records:
                result['DefenseRecords'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.defense_records = []
        if m.get('DefenseRecords') is not None:
            for k in m.get('DefenseRecords'):
                temp_model = DescribeDefenseRecordsResponseBodyDefenseRecords()
                self.defense_records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDefenseRecordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDefenseRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDefenseRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainAttackEventsRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, start_time=None, end_time=None, domain=None,
                 page_number=None, page_size=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDomainAttackEventsResponseBodyDomainAttackEvents(TeaModel):
    def __init__(self, end_time=None, start_time=None, domain=None, max_qps=None):
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.max_qps = max_qps  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')
        return self


class DescribeDomainAttackEventsResponseBody(TeaModel):
    def __init__(self, total_count=None, domain_attack_events=None, request_id=None):
        self.total_count = total_count  # type: long
        self.domain_attack_events = domain_attack_events  # type: list[DescribeDomainAttackEventsResponseBodyDomainAttackEvents]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.domain_attack_events:
            for k in self.domain_attack_events:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['DomainAttackEvents'] = []
        if self.domain_attack_events is not None:
            for k in self.domain_attack_events:
                result['DomainAttackEvents'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.domain_attack_events = []
        if m.get('DomainAttackEvents') is not None:
            for k in m.get('DomainAttackEvents'):
                temp_model = DescribeDomainAttackEventsResponseBodyDomainAttackEvents()
                self.domain_attack_events.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainAttackEventsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDomainAttackEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainAttackEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainOverviewRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, start_time=None, end_time=None, domain=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainOverviewResponseBody(TeaModel):
    def __init__(self, request_id=None, max_https=None, max_http=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.max_https = max_https  # type: long
        self.max_http = max_http  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_https is not None:
            result['MaxHttps'] = self.max_https
        if self.max_http is not None:
            result['MaxHttp'] = self.max_http
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxHttps') is not None:
            self.max_https = m.get('MaxHttps')
        if m.get('MaxHttp') is not None:
            self.max_http = m.get('MaxHttp')
        return self


class DescribeDomainOverviewResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDomainOverviewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainQPSListRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, start_time=None, end_time=None, interval=None,
                 domain=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.interval = interval  # type: long
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainQPSListResponseBodyDomainQPSList(TeaModel):
    def __init__(self, index=None, time=None, max_attack_qps=None, attack_qps=None, max_qps=None,
                 max_normal_qps=None, total_qps=None, total_count=None, cache_hits=None):
        self.index = index  # type: long
        self.time = time  # type: long
        self.max_attack_qps = max_attack_qps  # type: long
        self.attack_qps = attack_qps  # type: long
        self.max_qps = max_qps  # type: long
        self.max_normal_qps = max_normal_qps  # type: long
        self.total_qps = total_qps  # type: long
        self.total_count = total_count  # type: long
        self.cache_hits = cache_hits  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.time is not None:
            result['Time'] = self.time
        if self.max_attack_qps is not None:
            result['MaxAttackQps'] = self.max_attack_qps
        if self.attack_qps is not None:
            result['AttackQps'] = self.attack_qps
        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps
        if self.max_normal_qps is not None:
            result['MaxNormalQps'] = self.max_normal_qps
        if self.total_qps is not None:
            result['TotalQps'] = self.total_qps
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.cache_hits is not None:
            result['CacheHits'] = self.cache_hits
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('MaxAttackQps') is not None:
            self.max_attack_qps = m.get('MaxAttackQps')
        if m.get('AttackQps') is not None:
            self.attack_qps = m.get('AttackQps')
        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')
        if m.get('MaxNormalQps') is not None:
            self.max_normal_qps = m.get('MaxNormalQps')
        if m.get('TotalQps') is not None:
            self.total_qps = m.get('TotalQps')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('CacheHits') is not None:
            self.cache_hits = m.get('CacheHits')
        return self


class DescribeDomainQPSListResponseBody(TeaModel):
    def __init__(self, domain_qpslist=None, request_id=None):
        self.domain_qpslist = domain_qpslist  # type: list[DescribeDomainQPSListResponseBodyDomainQPSList]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.domain_qpslist:
            for k in self.domain_qpslist:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DomainQPSList'] = []
        if self.domain_qpslist is not None:
            for k in self.domain_qpslist:
                result['DomainQPSList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_qpslist = []
        if m.get('DomainQPSList') is not None:
            for k in m.get('DomainQPSList'):
                temp_model = DescribeDomainQPSListResponseBodyDomainQPSList()
                self.domain_qpslist.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainQPSListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDomainQPSListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainQPSListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainQpsWithCacheRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, start_time=None, end_time=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDomainQpsWithCacheResponseBody(TeaModel):
    def __init__(self, ip_block_qps=None, cc_js_qps=None, blocks=None, precise_blocks=None, request_id=None,
                 precise_js_qps=None, totals=None, start_time=None, cc_block_qps=None, interval=None, region_blocks=None,
                 cache_hits=None):
        self.ip_block_qps = ip_block_qps  # type: list[unicode]
        self.cc_js_qps = cc_js_qps  # type: list[unicode]
        self.blocks = blocks  # type: list[unicode]
        self.precise_blocks = precise_blocks  # type: list[unicode]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.precise_js_qps = precise_js_qps  # type: list[unicode]
        self.totals = totals  # type: list[unicode]
        self.start_time = start_time  # type: long
        self.cc_block_qps = cc_block_qps  # type: list[unicode]
        self.interval = interval  # type: int
        self.region_blocks = region_blocks  # type: list[unicode]
        self.cache_hits = cache_hits  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ip_block_qps is not None:
            result['IpBlockQps'] = self.ip_block_qps
        if self.cc_js_qps is not None:
            result['CcJsQps'] = self.cc_js_qps
        if self.blocks is not None:
            result['Blocks'] = self.blocks
        if self.precise_blocks is not None:
            result['PreciseBlocks'] = self.precise_blocks
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.precise_js_qps is not None:
            result['PreciseJsQps'] = self.precise_js_qps
        if self.totals is not None:
            result['Totals'] = self.totals
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.cc_block_qps is not None:
            result['CcBlockQps'] = self.cc_block_qps
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.region_blocks is not None:
            result['RegionBlocks'] = self.region_blocks
        if self.cache_hits is not None:
            result['CacheHits'] = self.cache_hits
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpBlockQps') is not None:
            self.ip_block_qps = m.get('IpBlockQps')
        if m.get('CcJsQps') is not None:
            self.cc_js_qps = m.get('CcJsQps')
        if m.get('Blocks') is not None:
            self.blocks = m.get('Blocks')
        if m.get('PreciseBlocks') is not None:
            self.precise_blocks = m.get('PreciseBlocks')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PreciseJsQps') is not None:
            self.precise_js_qps = m.get('PreciseJsQps')
        if m.get('Totals') is not None:
            self.totals = m.get('Totals')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('CcBlockQps') is not None:
            self.cc_block_qps = m.get('CcBlockQps')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('RegionBlocks') is not None:
            self.region_blocks = m.get('RegionBlocks')
        if m.get('CacheHits') is not None:
            self.cache_hits = m.get('CacheHits')
        return self


class DescribeDomainQpsWithCacheResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDomainQpsWithCacheResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainQpsWithCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainsRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeDomainsResponseBody(TeaModel):
    def __init__(self, domains=None, request_id=None):
        self.domains = domains  # type: list[unicode]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDomainsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
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


class DescribeDomainStatusCodeCountRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, start_time=None, end_time=None, domain=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainStatusCodeCountResponseBody(TeaModel):
    def __init__(self, request_id=None, status_501=None, status_502=None, status_403=None, status_503=None,
                 status_404=None, status_405=None, status_504=None, status_2xx=None, status_200=None, status_3xx=None,
                 status_4xx=None, status_5xx=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.status_501 = status_501  # type: long
        self.status_502 = status_502  # type: long
        self.status_403 = status_403  # type: long
        self.status_503 = status_503  # type: long
        self.status_404 = status_404  # type: long
        self.status_405 = status_405  # type: long
        self.status_504 = status_504  # type: long
        self.status_2xx = status_2xx  # type: long
        self.status_200 = status_200  # type: long
        self.status_3xx = status_3xx  # type: long
        self.status_4xx = status_4xx  # type: long
        self.status_5xx = status_5xx  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status_501 is not None:
            result['Status501'] = self.status_501
        if self.status_502 is not None:
            result['Status502'] = self.status_502
        if self.status_403 is not None:
            result['Status403'] = self.status_403
        if self.status_503 is not None:
            result['Status503'] = self.status_503
        if self.status_404 is not None:
            result['Status404'] = self.status_404
        if self.status_405 is not None:
            result['Status405'] = self.status_405
        if self.status_504 is not None:
            result['Status504'] = self.status_504
        if self.status_2xx is not None:
            result['Status2XX'] = self.status_2xx
        if self.status_200 is not None:
            result['Status200'] = self.status_200
        if self.status_3xx is not None:
            result['Status3XX'] = self.status_3xx
        if self.status_4xx is not None:
            result['Status4XX'] = self.status_4xx
        if self.status_5xx is not None:
            result['Status5XX'] = self.status_5xx
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status501') is not None:
            self.status_501 = m.get('Status501')
        if m.get('Status502') is not None:
            self.status_502 = m.get('Status502')
        if m.get('Status403') is not None:
            self.status_403 = m.get('Status403')
        if m.get('Status503') is not None:
            self.status_503 = m.get('Status503')
        if m.get('Status404') is not None:
            self.status_404 = m.get('Status404')
        if m.get('Status405') is not None:
            self.status_405 = m.get('Status405')
        if m.get('Status504') is not None:
            self.status_504 = m.get('Status504')
        if m.get('Status2XX') is not None:
            self.status_2xx = m.get('Status2XX')
        if m.get('Status200') is not None:
            self.status_200 = m.get('Status200')
        if m.get('Status3XX') is not None:
            self.status_3xx = m.get('Status3XX')
        if m.get('Status4XX') is not None:
            self.status_4xx = m.get('Status4XX')
        if m.get('Status5XX') is not None:
            self.status_5xx = m.get('Status5XX')
        return self


class DescribeDomainStatusCodeCountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDomainStatusCodeCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainStatusCodeCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainStatusCodeListRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, start_time=None, end_time=None, interval=None,
                 domain=None, query_type=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.interval = interval  # type: long
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.query_type = TeaConverter.to_unicode(query_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        return self


class DescribeDomainStatusCodeListResponseBodyStatusCodeList(TeaModel):
    def __init__(self, status_502=None, index=None, time=None, status_405=None, status_3xx=None, status_503=None,
                 status_4xx=None, status_2xx=None, status_5xx=None, status_504=None, status_403=None, status_200=None,
                 status_404=None, status_501=None):
        self.status_502 = status_502  # type: long
        self.index = index  # type: int
        self.time = time  # type: long
        self.status_405 = status_405  # type: long
        self.status_3xx = status_3xx  # type: long
        self.status_503 = status_503  # type: long
        self.status_4xx = status_4xx  # type: long
        self.status_2xx = status_2xx  # type: long
        self.status_5xx = status_5xx  # type: long
        self.status_504 = status_504  # type: long
        self.status_403 = status_403  # type: long
        self.status_200 = status_200  # type: long
        self.status_404 = status_404  # type: long
        self.status_501 = status_501  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status_502 is not None:
            result['Status502'] = self.status_502
        if self.index is not None:
            result['Index'] = self.index
        if self.time is not None:
            result['Time'] = self.time
        if self.status_405 is not None:
            result['Status405'] = self.status_405
        if self.status_3xx is not None:
            result['Status3XX'] = self.status_3xx
        if self.status_503 is not None:
            result['Status503'] = self.status_503
        if self.status_4xx is not None:
            result['Status4XX'] = self.status_4xx
        if self.status_2xx is not None:
            result['Status2XX'] = self.status_2xx
        if self.status_5xx is not None:
            result['Status5XX'] = self.status_5xx
        if self.status_504 is not None:
            result['Status504'] = self.status_504
        if self.status_403 is not None:
            result['Status403'] = self.status_403
        if self.status_200 is not None:
            result['Status200'] = self.status_200
        if self.status_404 is not None:
            result['Status404'] = self.status_404
        if self.status_501 is not None:
            result['Status501'] = self.status_501
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status502') is not None:
            self.status_502 = m.get('Status502')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Status405') is not None:
            self.status_405 = m.get('Status405')
        if m.get('Status3XX') is not None:
            self.status_3xx = m.get('Status3XX')
        if m.get('Status503') is not None:
            self.status_503 = m.get('Status503')
        if m.get('Status4XX') is not None:
            self.status_4xx = m.get('Status4XX')
        if m.get('Status2XX') is not None:
            self.status_2xx = m.get('Status2XX')
        if m.get('Status5XX') is not None:
            self.status_5xx = m.get('Status5XX')
        if m.get('Status504') is not None:
            self.status_504 = m.get('Status504')
        if m.get('Status403') is not None:
            self.status_403 = m.get('Status403')
        if m.get('Status200') is not None:
            self.status_200 = m.get('Status200')
        if m.get('Status404') is not None:
            self.status_404 = m.get('Status404')
        if m.get('Status501') is not None:
            self.status_501 = m.get('Status501')
        return self


class DescribeDomainStatusCodeListResponseBody(TeaModel):
    def __init__(self, request_id=None, status_code_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.status_code_list = status_code_list  # type: list[DescribeDomainStatusCodeListResponseBodyStatusCodeList]

    def validate(self):
        if self.status_code_list:
            for k in self.status_code_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StatusCodeList'] = []
        if self.status_code_list is not None:
            for k in self.status_code_list:
                result['StatusCodeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.status_code_list = []
        if m.get('StatusCodeList') is not None:
            for k in m.get('StatusCodeList'):
                temp_model = DescribeDomainStatusCodeListResponseBodyStatusCodeList()
                self.status_code_list.append(temp_model.from_map(k))
        return self


class DescribeDomainStatusCodeListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDomainStatusCodeListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainStatusCodeListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainTopAttackListRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, start_time=None, end_time=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDomainTopAttackListResponseBodyAttackList(TeaModel):
    def __init__(self, attack=None, domain=None, count=None):
        self.attack = attack  # type: long
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.count = count  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.attack is not None:
            result['Attack'] = self.attack
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attack') is not None:
            self.attack = m.get('Attack')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeDomainTopAttackListResponseBody(TeaModel):
    def __init__(self, attack_list=None, request_id=None):
        self.attack_list = attack_list  # type: list[DescribeDomainTopAttackListResponseBodyAttackList]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.attack_list:
            for k in self.attack_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AttackList'] = []
        if self.attack_list is not None:
            for k in self.attack_list:
                result['AttackList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.attack_list = []
        if m.get('AttackList') is not None:
            for k in m.get('AttackList'):
                temp_model = DescribeDomainTopAttackListResponseBodyAttackList()
                self.attack_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainTopAttackListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDomainTopAttackListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainTopAttackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainViewSourceCountriesRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, start_time=None, end_time=None, domain=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainViewSourceCountriesResponseBodySourceCountrys(TeaModel):
    def __init__(self, country_id=None, count=None):
        self.country_id = TeaConverter.to_unicode(country_id)  # type: unicode
        self.count = count  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeDomainViewSourceCountriesResponseBody(TeaModel):
    def __init__(self, request_id=None, source_countrys=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.source_countrys = source_countrys  # type: list[DescribeDomainViewSourceCountriesResponseBodySourceCountrys]

    def validate(self):
        if self.source_countrys:
            for k in self.source_countrys:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SourceCountrys'] = []
        if self.source_countrys is not None:
            for k in self.source_countrys:
                result['SourceCountrys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.source_countrys = []
        if m.get('SourceCountrys') is not None:
            for k in m.get('SourceCountrys'):
                temp_model = DescribeDomainViewSourceCountriesResponseBodySourceCountrys()
                self.source_countrys.append(temp_model.from_map(k))
        return self


class DescribeDomainViewSourceCountriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDomainViewSourceCountriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainViewSourceCountriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainViewSourceProvincesRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, start_time=None, end_time=None, domain=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainViewSourceProvincesResponseBodySourceProvinces(TeaModel):
    def __init__(self, province_id=None, count=None):
        self.province_id = TeaConverter.to_unicode(province_id)  # type: unicode
        self.count = count  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.province_id is not None:
            result['ProvinceId'] = self.province_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProvinceId') is not None:
            self.province_id = m.get('ProvinceId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeDomainViewSourceProvincesResponseBody(TeaModel):
    def __init__(self, source_provinces=None, request_id=None):
        self.source_provinces = source_provinces  # type: list[DescribeDomainViewSourceProvincesResponseBodySourceProvinces]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.source_provinces:
            for k in self.source_provinces:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SourceProvinces'] = []
        if self.source_provinces is not None:
            for k in self.source_provinces:
                result['SourceProvinces'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.source_provinces = []
        if m.get('SourceProvinces') is not None:
            for k in m.get('SourceProvinces'):
                temp_model = DescribeDomainViewSourceProvincesResponseBodySourceProvinces()
                self.source_provinces.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainViewSourceProvincesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDomainViewSourceProvincesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainViewSourceProvincesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainViewTopCostTimeRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, start_time=None, end_time=None, domain=None, top=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.top = top  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.top is not None:
            result['Top'] = self.top
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        return self


class DescribeDomainViewTopCostTimeResponseBodyUrlList(TeaModel):
    def __init__(self, domain=None, cost_time=None, url=None):
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.cost_time = cost_time  # type: float
        self.url = TeaConverter.to_unicode(url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeDomainViewTopCostTimeResponseBody(TeaModel):
    def __init__(self, request_id=None, url_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.url_list = url_list  # type: list[DescribeDomainViewTopCostTimeResponseBodyUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDomainViewTopCostTimeResponseBodyUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainViewTopCostTimeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDomainViewTopCostTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainViewTopCostTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainViewTopUrlRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, start_time=None, end_time=None, domain=None, top=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.top = top  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.top is not None:
            result['Top'] = self.top
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        return self


class DescribeDomainViewTopUrlResponseBodyUrlList(TeaModel):
    def __init__(self, domain=None, url=None, count=None):
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.count = count  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.url is not None:
            result['Url'] = self.url
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeDomainViewTopUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, url_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.url_list = url_list  # type: list[DescribeDomainViewTopUrlResponseBodyUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UrlList'] = []
        if self.url_list is not None:
            for k in self.url_list:
                result['UrlList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.url_list = []
        if m.get('UrlList') is not None:
            for k in m.get('UrlList'):
                temp_model = DescribeDomainViewTopUrlResponseBodyUrlList()
                self.url_list.append(temp_model.from_map(k))
        return self


class DescribeDomainViewTopUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDomainViewTopUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainViewTopUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeElasticBandwidthSpecRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeElasticBandwidthSpecResponseBody(TeaModel):
    def __init__(self, request_id=None, elastic_bandwidth_spec=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.elastic_bandwidth_spec = elastic_bandwidth_spec  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.elastic_bandwidth_spec is not None:
            result['ElasticBandwidthSpec'] = self.elastic_bandwidth_spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ElasticBandwidthSpec') is not None:
            self.elastic_bandwidth_spec = m.get('ElasticBandwidthSpec')
        return self


class DescribeElasticBandwidthSpecResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeElasticBandwidthSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeElasticBandwidthSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHealthCheckListRequest(TeaModel):
    def __init__(self, source_ip=None, network_rules=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.network_rules = TeaConverter.to_unicode(network_rules)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('NetworkRules') is not None:
            self.network_rules = m.get('NetworkRules')
        return self


class DescribeHealthCheckListResponseBodyHealthCheckListHealthCheck(TeaModel):
    def __init__(self, timeout=None, type=None, domain=None, interval=None, up=None, down=None, port=None, uri=None):
        self.timeout = timeout  # type: int
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.interval = interval  # type: int
        self.up = up  # type: int
        self.down = down  # type: int
        self.port = port  # type: int
        self.uri = TeaConverter.to_unicode(uri)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.type is not None:
            result['Type'] = self.type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.up is not None:
            result['Up'] = self.up
        if self.down is not None:
            result['Down'] = self.down
        if self.port is not None:
            result['Port'] = self.port
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Up') is not None:
            self.up = m.get('Up')
        if m.get('Down') is not None:
            self.down = m.get('Down')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DescribeHealthCheckListResponseBodyHealthCheckList(TeaModel):
    def __init__(self, frontend_port=None, protocol=None, instance_id=None, health_check=None):
        self.frontend_port = frontend_port  # type: int
        self.protocol = TeaConverter.to_unicode(protocol)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.health_check = health_check  # type: DescribeHealthCheckListResponseBodyHealthCheckListHealthCheck

    def validate(self):
        if self.health_check:
            self.health_check.validate()

    def to_map(self):
        result = dict()
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('HealthCheck') is not None:
            temp_model = DescribeHealthCheckListResponseBodyHealthCheckListHealthCheck()
            self.health_check = temp_model.from_map(m['HealthCheck'])
        return self


class DescribeHealthCheckListResponseBody(TeaModel):
    def __init__(self, request_id=None, health_check_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.health_check_list = health_check_list  # type: list[DescribeHealthCheckListResponseBodyHealthCheckList]

    def validate(self):
        if self.health_check_list:
            for k in self.health_check_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['HealthCheckList'] = []
        if self.health_check_list is not None:
            for k in self.health_check_list:
                result['HealthCheckList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.health_check_list = []
        if m.get('HealthCheckList') is not None:
            for k in m.get('HealthCheckList'):
                temp_model = DescribeHealthCheckListResponseBodyHealthCheckList()
                self.health_check_list.append(temp_model.from_map(k))
        return self


class DescribeHealthCheckListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeHealthCheckListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHealthCheckListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHealthCheckStatusRequest(TeaModel):
    def __init__(self, source_ip=None, network_rules=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.network_rules = TeaConverter.to_unicode(network_rules)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('NetworkRules') is not None:
            self.network_rules = m.get('NetworkRules')
        return self


class DescribeHealthCheckStatusResponseBodyHealthCheckStatusRealServerStatusList(TeaModel):
    def __init__(self, status=None, address=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.address = TeaConverter.to_unicode(address)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.address is not None:
            result['Address'] = self.address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        return self


class DescribeHealthCheckStatusResponseBodyHealthCheckStatus(TeaModel):
    def __init__(self, status=None, frontend_port=None, protocol=None, instance_id=None,
                 real_server_status_list=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.frontend_port = frontend_port  # type: int
        self.protocol = TeaConverter.to_unicode(protocol)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.real_server_status_list = real_server_status_list  # type: list[DescribeHealthCheckStatusResponseBodyHealthCheckStatusRealServerStatusList]

    def validate(self):
        if self.real_server_status_list:
            for k in self.real_server_status_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['RealServerStatusList'] = []
        if self.real_server_status_list is not None:
            for k in self.real_server_status_list:
                result['RealServerStatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.real_server_status_list = []
        if m.get('RealServerStatusList') is not None:
            for k in m.get('RealServerStatusList'):
                temp_model = DescribeHealthCheckStatusResponseBodyHealthCheckStatusRealServerStatusList()
                self.real_server_status_list.append(temp_model.from_map(k))
        return self


class DescribeHealthCheckStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, health_check_status=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.health_check_status = health_check_status  # type: list[DescribeHealthCheckStatusResponseBodyHealthCheckStatus]

    def validate(self):
        if self.health_check_status:
            for k in self.health_check_status:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['HealthCheckStatus'] = []
        if self.health_check_status is not None:
            for k in self.health_check_status:
                result['HealthCheckStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.health_check_status = []
        if m.get('HealthCheckStatus') is not None:
            for k in m.get('HealthCheckStatus'):
                temp_model = DescribeHealthCheckStatusResponseBodyHealthCheckStatus()
                self.health_check_status.append(temp_model.from_map(k))
        return self


class DescribeHealthCheckStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeHealthCheckStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHealthCheckStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceDetailsRequest(TeaModel):
    def __init__(self, source_ip=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfos(TeaModel):
    def __init__(self, status=None, eip=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.eip = TeaConverter.to_unicode(eip)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.eip is not None:
            result['Eip'] = self.eip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        return self


class DescribeInstanceDetailsResponseBodyInstanceDetails(TeaModel):
    def __init__(self, line=None, instance_id=None, eip_infos=None):
        self.line = TeaConverter.to_unicode(line)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.eip_infos = eip_infos  # type: list[DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfos]

    def validate(self):
        if self.eip_infos:
            for k in self.eip_infos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.line is not None:
            result['Line'] = self.line
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['EipInfos'] = []
        if self.eip_infos is not None:
            for k in self.eip_infos:
                result['EipInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.eip_infos = []
        if m.get('EipInfos') is not None:
            for k in m.get('EipInfos'):
                temp_model = DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfos()
                self.eip_infos.append(temp_model.from_map(k))
        return self


class DescribeInstanceDetailsResponseBody(TeaModel):
    def __init__(self, instance_details=None, request_id=None):
        self.instance_details = instance_details  # type: list[DescribeInstanceDetailsResponseBodyInstanceDetails]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.instance_details:
            for k in self.instance_details:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceDetails'] = []
        if self.instance_details is not None:
            for k in self.instance_details:
                result['InstanceDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_details = []
        if m.get('InstanceDetails') is not None:
            for k in m.get('InstanceDetails'):
                temp_model = DescribeInstanceDetailsResponseBodyInstanceDetails()
                self.instance_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceDetailsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeInstanceDetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceIdsRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, edition=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.edition = edition  # type: int
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeInstanceIdsResponseBodyInstanceIds(TeaModel):
    def __init__(self, edition=None, remark=None, instance_id=None):
        self.edition = edition  # type: int
        self.remark = TeaConverter.to_unicode(remark)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceIdsResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_ids=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.instance_ids = instance_ids  # type: list[DescribeInstanceIdsResponseBodyInstanceIds]

    def validate(self):
        if self.instance_ids:
            for k in self.instance_ids:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['InstanceIds'] = []
        if self.instance_ids is not None:
            for k in self.instance_ids:
                result['InstanceIds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instance_ids = []
        if m.get('InstanceIds') is not None:
            for k in m.get('InstanceIds'):
                temp_model = DescribeInstanceIdsResponseBodyInstanceIds()
                self.instance_ids.append(temp_model.from_map(k))
        return self


class DescribeInstanceIdsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeInstanceIdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.value = TeaConverter.to_unicode(value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class DescribeInstancesRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, page_number=None, page_size=None, ip=None,
                 remark=None, edition=None, enabled=None, expire_start_time=None, expire_end_time=None, instance_ids=None,
                 status=None, tag=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.page_number = TeaConverter.to_unicode(page_number)  # type: unicode
        self.page_size = TeaConverter.to_unicode(page_size)  # type: unicode
        self.ip = TeaConverter.to_unicode(ip)  # type: unicode
        self.remark = TeaConverter.to_unicode(remark)  # type: unicode
        self.edition = edition  # type: int
        self.enabled = enabled  # type: int
        self.expire_start_time = expire_start_time  # type: long
        self.expire_end_time = expire_end_time  # type: long
        self.instance_ids = instance_ids  # type: list[unicode]
        self.status = status  # type: list[int]
        self.tag = tag  # type: list[DescribeInstancesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.expire_start_time is not None:
            result['ExpireStartTime'] = self.expire_start_time
        if self.expire_end_time is not None:
            result['ExpireEndTime'] = self.expire_end_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('ExpireStartTime') is not None:
            self.expire_start_time = m.get('ExpireStartTime')
        if m.get('ExpireEndTime') is not None:
            self.expire_end_time = m.get('ExpireEndTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(self, status=None, debt_status=None, edition=None, expire_time=None, remark=None, create_time=None,
                 enabled=None, instance_id=None, conn_instance_id=None):
        self.status = status  # type: int
        self.debt_status = debt_status  # type: int
        self.edition = edition  # type: int
        self.expire_time = expire_time  # type: long
        self.remark = TeaConverter.to_unicode(remark)  # type: unicode
        self.create_time = create_time  # type: long
        self.enabled = enabled  # type: int
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.conn_instance_id = TeaConverter.to_unicode(conn_instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.debt_status is not None:
            result['DebtStatus'] = self.debt_status
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.conn_instance_id is not None:
            result['ConnInstanceId'] = self.conn_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DebtStatus') is not None:
            self.debt_status = m.get('DebtStatus')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ConnInstanceId') is not None:
            self.conn_instance_id = m.get('ConnInstanceId')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(self, instances=None, total_count=None, request_id=None):
        self.instances = instances  # type: list[DescribeInstancesResponseBodyInstances]
        self.total_count = total_count  # type: long
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSpecsRequest(TeaModel):
    def __init__(self, source_ip=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeInstanceSpecsResponseBodyInstanceSpecs(TeaModel):
    def __init__(self, base_bandwidth=None, qps_limit=None, bandwidth_mbps=None, defense_count=None,
                 site_limit=None, port_limit=None, elastic_bandwidth=None, function_version=None, instance_id=None,
                 domain_limit=None):
        self.base_bandwidth = base_bandwidth  # type: int
        self.qps_limit = qps_limit  # type: int
        self.bandwidth_mbps = bandwidth_mbps  # type: int
        self.defense_count = defense_count  # type: int
        self.site_limit = site_limit  # type: int
        self.port_limit = port_limit  # type: int
        self.elastic_bandwidth = elastic_bandwidth  # type: int
        self.function_version = TeaConverter.to_unicode(function_version)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.domain_limit = domain_limit  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.base_bandwidth is not None:
            result['BaseBandwidth'] = self.base_bandwidth
        if self.qps_limit is not None:
            result['QpsLimit'] = self.qps_limit
        if self.bandwidth_mbps is not None:
            result['BandwidthMbps'] = self.bandwidth_mbps
        if self.defense_count is not None:
            result['DefenseCount'] = self.defense_count
        if self.site_limit is not None:
            result['SiteLimit'] = self.site_limit
        if self.port_limit is not None:
            result['PortLimit'] = self.port_limit
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth
        if self.function_version is not None:
            result['FunctionVersion'] = self.function_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain_limit is not None:
            result['DomainLimit'] = self.domain_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BaseBandwidth') is not None:
            self.base_bandwidth = m.get('BaseBandwidth')
        if m.get('QpsLimit') is not None:
            self.qps_limit = m.get('QpsLimit')
        if m.get('BandwidthMbps') is not None:
            self.bandwidth_mbps = m.get('BandwidthMbps')
        if m.get('DefenseCount') is not None:
            self.defense_count = m.get('DefenseCount')
        if m.get('SiteLimit') is not None:
            self.site_limit = m.get('SiteLimit')
        if m.get('PortLimit') is not None:
            self.port_limit = m.get('PortLimit')
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')
        if m.get('FunctionVersion') is not None:
            self.function_version = m.get('FunctionVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DomainLimit') is not None:
            self.domain_limit = m.get('DomainLimit')
        return self


class DescribeInstanceSpecsResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_specs=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.instance_specs = instance_specs  # type: list[DescribeInstanceSpecsResponseBodyInstanceSpecs]

    def validate(self):
        if self.instance_specs:
            for k in self.instance_specs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['InstanceSpecs'] = []
        if self.instance_specs is not None:
            for k in self.instance_specs:
                result['InstanceSpecs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instance_specs = []
        if m.get('InstanceSpecs') is not None:
            for k in m.get('InstanceSpecs'):
                temp_model = DescribeInstanceSpecsResponseBodyInstanceSpecs()
                self.instance_specs.append(temp_model.from_map(k))
        return self


class DescribeInstanceSpecsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeInstanceSpecsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceStatisticsRequest(TeaModel):
    def __init__(self, source_ip=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeInstanceStatisticsResponseBodyInstanceStatistics(TeaModel):
    def __init__(self, domain_usage=None, defense_count_usage=None, instance_id=None, site_usage=None,
                 port_usage=None):
        self.domain_usage = domain_usage  # type: int
        self.defense_count_usage = defense_count_usage  # type: int
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.site_usage = site_usage  # type: int
        self.port_usage = port_usage  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain_usage is not None:
            result['DomainUsage'] = self.domain_usage
        if self.defense_count_usage is not None:
            result['DefenseCountUsage'] = self.defense_count_usage
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.site_usage is not None:
            result['SiteUsage'] = self.site_usage
        if self.port_usage is not None:
            result['PortUsage'] = self.port_usage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainUsage') is not None:
            self.domain_usage = m.get('DomainUsage')
        if m.get('DefenseCountUsage') is not None:
            self.defense_count_usage = m.get('DefenseCountUsage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SiteUsage') is not None:
            self.site_usage = m.get('SiteUsage')
        if m.get('PortUsage') is not None:
            self.port_usage = m.get('PortUsage')
        return self


class DescribeInstanceStatisticsResponseBody(TeaModel):
    def __init__(self, instance_statistics=None, request_id=None):
        self.instance_statistics = instance_statistics  # type: list[DescribeInstanceStatisticsResponseBodyInstanceStatistics]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.instance_statistics:
            for k in self.instance_statistics:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceStatistics'] = []
        if self.instance_statistics is not None:
            for k in self.instance_statistics:
                result['InstanceStatistics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_statistics = []
        if m.get('InstanceStatistics') is not None:
            for k in m.get('InstanceStatistics'):
                temp_model = DescribeInstanceStatisticsResponseBodyInstanceStatistics()
                self.instance_statistics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeInstanceStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceStatusRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None, product_type=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.product_type = product_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class DescribeInstanceStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_id=None, instance_status=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.instance_status = instance_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        return self


class DescribeInstanceStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeInstanceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeL7RsPolicyRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, real_servers=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.real_servers = real_servers  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        return self


class DescribeL7RsPolicyResponseBodyAttributesAttribute(TeaModel):
    def __init__(self, weight=None):
        self.weight = weight  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeL7RsPolicyResponseBodyAttributes(TeaModel):
    def __init__(self, rs_type=None, attribute=None, real_server=None):
        self.rs_type = rs_type  # type: int
        self.attribute = attribute  # type: DescribeL7RsPolicyResponseBodyAttributesAttribute
        self.real_server = TeaConverter.to_unicode(real_server)  # type: unicode

    def validate(self):
        if self.attribute:
            self.attribute.validate()

    def to_map(self):
        result = dict()
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.attribute is not None:
            result['Attribute'] = self.attribute.to_map()
        if self.real_server is not None:
            result['RealServer'] = self.real_server
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        if m.get('Attribute') is not None:
            temp_model = DescribeL7RsPolicyResponseBodyAttributesAttribute()
            self.attribute = temp_model.from_map(m['Attribute'])
        if m.get('RealServer') is not None:
            self.real_server = m.get('RealServer')
        return self


class DescribeL7RsPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, attributes=None, proxy_mode=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.attributes = attributes  # type: list[DescribeL7RsPolicyResponseBodyAttributes]
        self.proxy_mode = TeaConverter.to_unicode(proxy_mode)  # type: unicode

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.proxy_mode is not None:
            result['ProxyMode'] = self.proxy_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = DescribeL7RsPolicyResponseBodyAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('ProxyMode') is not None:
            self.proxy_mode = m.get('ProxyMode')
        return self


class DescribeL7RsPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeL7RsPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeL7RsPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogStoreExistStatusRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeLogStoreExistStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, exist_status=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.exist_status = exist_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.exist_status is not None:
            result['ExistStatus'] = self.exist_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExistStatus') is not None:
            self.exist_status = m.get('ExistStatus')
        return self


class DescribeLogStoreExistStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeLogStoreExistStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLogStoreExistStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNetworkRegionBlockRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeNetworkRegionBlockResponseBodyConfig(TeaModel):
    def __init__(self, region_block_switch=None, provinces=None, countries=None):
        self.region_block_switch = TeaConverter.to_unicode(region_block_switch)  # type: unicode
        self.provinces = provinces  # type: list[unicode]
        self.countries = countries  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_block_switch is not None:
            result['RegionBlockSwitch'] = self.region_block_switch
        if self.provinces is not None:
            result['Provinces'] = self.provinces
        if self.countries is not None:
            result['Countries'] = self.countries
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionBlockSwitch') is not None:
            self.region_block_switch = m.get('RegionBlockSwitch')
        if m.get('Provinces') is not None:
            self.provinces = m.get('Provinces')
        if m.get('Countries') is not None:
            self.countries = m.get('Countries')
        return self


class DescribeNetworkRegionBlockResponseBody(TeaModel):
    def __init__(self, request_id=None, config=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.config = config  # type: DescribeNetworkRegionBlockResponseBodyConfig

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.config is not None:
            result['Config'] = self.config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Config') is not None:
            temp_model = DescribeNetworkRegionBlockResponseBodyConfig()
            self.config = temp_model.from_map(m['Config'])
        return self


class DescribeNetworkRegionBlockResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeNetworkRegionBlockResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNetworkRegionBlockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNetworkRuleAttributesRequest(TeaModel):
    def __init__(self, source_ip=None, network_rules=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.network_rules = TeaConverter.to_unicode(network_rules)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('NetworkRules') is not None:
            self.network_rules = m.get('NetworkRules')
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCcSblack(TeaModel):
    def __init__(self, type=None, expires=None, during=None, cnt=None):
        self.type = type  # type: int
        self.expires = expires  # type: int
        self.during = during  # type: int
        self.cnt = cnt  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.expires is not None:
            result['Expires'] = self.expires
        if self.during is not None:
            result['During'] = self.during
        if self.cnt is not None:
            result['Cnt'] = self.cnt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Expires') is not None:
            self.expires = m.get('Expires')
        if m.get('During') is not None:
            self.during = m.get('During')
        if m.get('Cnt') is not None:
            self.cnt = m.get('Cnt')
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCc(TeaModel):
    def __init__(self, sblack=None):
        self.sblack = sblack  # type: list[DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCcSblack]

    def validate(self):
        if self.sblack:
            for k in self.sblack:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Sblack'] = []
        if self.sblack is not None:
            for k in self.sblack:
                result['Sblack'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.sblack = []
        if m.get('Sblack') is not None:
            for k in m.get('Sblack'):
                temp_model = DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCcSblack()
                self.sblack.append(temp_model.from_map(k))
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigPayloadLen(TeaModel):
    def __init__(self, max=None, min=None):
        self.max = max  # type: int
        self.min = min  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max is not None:
            result['Max'] = self.max
        if self.min is not None:
            result['Min'] = self.min
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSla(TeaModel):
    def __init__(self, maxconn_enable=None, cps_enable=None, cps=None, maxconn=None):
        self.maxconn_enable = maxconn_enable  # type: int
        self.cps_enable = cps_enable  # type: int
        self.cps = cps  # type: int
        self.maxconn = maxconn  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.maxconn_enable is not None:
            result['MaxconnEnable'] = self.maxconn_enable
        if self.cps_enable is not None:
            result['CpsEnable'] = self.cps_enable
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.maxconn is not None:
            result['Maxconn'] = self.maxconn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxconnEnable') is not None:
            self.maxconn_enable = m.get('MaxconnEnable')
        if m.get('CpsEnable') is not None:
            self.cps_enable = m.get('CpsEnable')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('Maxconn') is not None:
            self.maxconn = m.get('Maxconn')
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSlimit(TeaModel):
    def __init__(self, maxconn_enable=None, cps_enable=None, cps=None, pps=None, bps=None, maxconn=None,
                 cps_mode=None):
        self.maxconn_enable = maxconn_enable  # type: int
        self.cps_enable = cps_enable  # type: int
        self.cps = cps  # type: int
        self.pps = pps  # type: long
        self.bps = bps  # type: long
        self.maxconn = maxconn  # type: int
        self.cps_mode = cps_mode  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.maxconn_enable is not None:
            result['MaxconnEnable'] = self.maxconn_enable
        if self.cps_enable is not None:
            result['CpsEnable'] = self.cps_enable
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.maxconn is not None:
            result['Maxconn'] = self.maxconn
        if self.cps_mode is not None:
            result['CpsMode'] = self.cps_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxconnEnable') is not None:
            self.maxconn_enable = m.get('MaxconnEnable')
        if m.get('CpsEnable') is not None:
            self.cps_enable = m.get('CpsEnable')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Maxconn') is not None:
            self.maxconn = m.get('Maxconn')
        if m.get('CpsMode') is not None:
            self.cps_mode = m.get('CpsMode')
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfig(TeaModel):
    def __init__(self, cc=None, payload_len=None, persistence_timeout=None, sla=None, slimit=None, nodata_conn=None,
                 synproxy=None):
        self.cc = cc  # type: DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCc
        self.payload_len = payload_len  # type: DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigPayloadLen
        self.persistence_timeout = persistence_timeout  # type: int
        self.sla = sla  # type: DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSla
        self.slimit = slimit  # type: DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSlimit
        self.nodata_conn = TeaConverter.to_unicode(nodata_conn)  # type: unicode
        self.synproxy = TeaConverter.to_unicode(synproxy)  # type: unicode

    def validate(self):
        if self.cc:
            self.cc.validate()
        if self.payload_len:
            self.payload_len.validate()
        if self.sla:
            self.sla.validate()
        if self.slimit:
            self.slimit.validate()

    def to_map(self):
        result = dict()
        if self.cc is not None:
            result['Cc'] = self.cc.to_map()
        if self.payload_len is not None:
            result['PayloadLen'] = self.payload_len.to_map()
        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout
        if self.sla is not None:
            result['Sla'] = self.sla.to_map()
        if self.slimit is not None:
            result['Slimit'] = self.slimit.to_map()
        if self.nodata_conn is not None:
            result['NodataConn'] = self.nodata_conn
        if self.synproxy is not None:
            result['Synproxy'] = self.synproxy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cc') is not None:
            temp_model = DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCc()
            self.cc = temp_model.from_map(m['Cc'])
        if m.get('PayloadLen') is not None:
            temp_model = DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigPayloadLen()
            self.payload_len = temp_model.from_map(m['PayloadLen'])
        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')
        if m.get('Sla') is not None:
            temp_model = DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSla()
            self.sla = temp_model.from_map(m['Sla'])
        if m.get('Slimit') is not None:
            temp_model = DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSlimit()
            self.slimit = temp_model.from_map(m['Slimit'])
        if m.get('NodataConn') is not None:
            self.nodata_conn = m.get('NodataConn')
        if m.get('Synproxy') is not None:
            self.synproxy = m.get('Synproxy')
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributes(TeaModel):
    def __init__(self, frontend_port=None, protocol=None, instance_id=None, config=None):
        self.frontend_port = frontend_port  # type: int
        self.protocol = TeaConverter.to_unicode(protocol)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.config = config  # type: DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfig

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.config is not None:
            result['Config'] = self.config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Config') is not None:
            temp_model = DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfig()
            self.config = temp_model.from_map(m['Config'])
        return self


class DescribeNetworkRuleAttributesResponseBody(TeaModel):
    def __init__(self, network_rule_attributes=None, request_id=None):
        self.network_rule_attributes = network_rule_attributes  # type: list[DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributes]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.network_rule_attributes:
            for k in self.network_rule_attributes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['NetworkRuleAttributes'] = []
        if self.network_rule_attributes is not None:
            for k in self.network_rule_attributes:
                result['NetworkRuleAttributes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.network_rule_attributes = []
        if m.get('NetworkRuleAttributes') is not None:
            for k in m.get('NetworkRuleAttributes'):
                temp_model = DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributes()
                self.network_rule_attributes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNetworkRuleAttributesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeNetworkRuleAttributesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNetworkRuleAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNetworkRulesRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None, forward_protocol=None, frontend_port=None,
                 page_number=None, page_size=None, is_offset=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.forward_protocol = TeaConverter.to_unicode(forward_protocol)  # type: unicode
        self.frontend_port = frontend_port  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.is_offset = is_offset  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.is_offset is not None:
            result['IsOffset'] = self.is_offset
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('IsOffset') is not None:
            self.is_offset = m.get('IsOffset')
        return self


class DescribeNetworkRulesResponseBodyNetworkRules(TeaModel):
    def __init__(self, frontend_port=None, is_auto_create=None, protocol=None, real_servers=None, instance_id=None,
                 backend_port=None):
        self.frontend_port = frontend_port  # type: int
        self.is_auto_create = is_auto_create  # type: bool
        self.protocol = TeaConverter.to_unicode(protocol)  # type: unicode
        self.real_servers = real_servers  # type: list[unicode]
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.backend_port = backend_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.is_auto_create is not None:
            result['IsAutoCreate'] = self.is_auto_create
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.backend_port is not None:
            result['BackendPort'] = self.backend_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('IsAutoCreate') is not None:
            self.is_auto_create = m.get('IsAutoCreate')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BackendPort') is not None:
            self.backend_port = m.get('BackendPort')
        return self


class DescribeNetworkRulesResponseBody(TeaModel):
    def __init__(self, total_count=None, network_rules=None, request_id=None):
        self.total_count = total_count  # type: long
        self.network_rules = network_rules  # type: list[DescribeNetworkRulesResponseBodyNetworkRules]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.network_rules:
            for k in self.network_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['NetworkRules'] = []
        if self.network_rules is not None:
            for k in self.network_rules:
                result['NetworkRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.network_rules = []
        if m.get('NetworkRules') is not None:
            for k in m.get('NetworkRules'):
                temp_model = DescribeNetworkRulesResponseBodyNetworkRules()
                self.network_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNetworkRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeNetworkRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNetworkRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOpEntitiesRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, entity_type=None, entity_object=None,
                 start_time=None, end_time=None, page_number=None, page_size=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.entity_type = entity_type  # type: int
        self.entity_object = TeaConverter.to_unicode(entity_object)  # type: unicode
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_object is not None:
            result['EntityObject'] = self.entity_object
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeOpEntitiesResponseBodyOpEntities(TeaModel):
    def __init__(self, entity_type=None, entity_object=None, gmt_create=None, op_action=None, op_account=None,
                 op_desc=None):
        self.entity_type = entity_type  # type: int
        self.entity_object = TeaConverter.to_unicode(entity_object)  # type: unicode
        self.gmt_create = gmt_create  # type: long
        self.op_action = op_action  # type: int
        self.op_account = TeaConverter.to_unicode(op_account)  # type: unicode
        self.op_desc = TeaConverter.to_unicode(op_desc)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_object is not None:
            result['EntityObject'] = self.entity_object
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.op_action is not None:
            result['OpAction'] = self.op_action
        if self.op_account is not None:
            result['OpAccount'] = self.op_account
        if self.op_desc is not None:
            result['OpDesc'] = self.op_desc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OpAction') is not None:
            self.op_action = m.get('OpAction')
        if m.get('OpAccount') is not None:
            self.op_account = m.get('OpAccount')
        if m.get('OpDesc') is not None:
            self.op_desc = m.get('OpDesc')
        return self


class DescribeOpEntitiesResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, op_entities=None):
        self.total_count = total_count  # type: long
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.op_entities = op_entities  # type: list[DescribeOpEntitiesResponseBodyOpEntities]

    def validate(self):
        if self.op_entities:
            for k in self.op_entities:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['OpEntities'] = []
        if self.op_entities is not None:
            for k in self.op_entities:
                result['OpEntities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.op_entities = []
        if m.get('OpEntities') is not None:
            for k in m.get('OpEntities'):
                temp_model = DescribeOpEntitiesResponseBodyOpEntities()
                self.op_entities.append(temp_model.from_map(k))
        return self


class DescribeOpEntitiesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeOpEntitiesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeOpEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortAttackMaxFlowRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, end_time=None, start_time=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortAttackMaxFlowResponseBody(TeaModel):
    def __init__(self, pps=None, request_id=None, bps=None):
        self.pps = pps  # type: long
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.bps = bps  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bps is not None:
            result['Bps'] = self.bps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        return self


class DescribePortAttackMaxFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribePortAttackMaxFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePortAttackMaxFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortAutoCcStatusRequest(TeaModel):
    def __init__(self, source_ip=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortAutoCcStatusResponseBodyPortAutoCcStatus(TeaModel):
    def __init__(self, switch=None, mode=None, web_switch=None, web_mode=None):
        self.switch = TeaConverter.to_unicode(switch)  # type: unicode
        self.mode = TeaConverter.to_unicode(mode)  # type: unicode
        self.web_switch = TeaConverter.to_unicode(web_switch)  # type: unicode
        self.web_mode = TeaConverter.to_unicode(web_mode)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.switch is not None:
            result['Switch'] = self.switch
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.web_switch is not None:
            result['WebSwitch'] = self.web_switch
        if self.web_mode is not None:
            result['WebMode'] = self.web_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Switch') is not None:
            self.switch = m.get('Switch')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('WebSwitch') is not None:
            self.web_switch = m.get('WebSwitch')
        if m.get('WebMode') is not None:
            self.web_mode = m.get('WebMode')
        return self


class DescribePortAutoCcStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, port_auto_cc_status=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.port_auto_cc_status = port_auto_cc_status  # type: list[DescribePortAutoCcStatusResponseBodyPortAutoCcStatus]

    def validate(self):
        if self.port_auto_cc_status:
            for k in self.port_auto_cc_status:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PortAutoCcStatus'] = []
        if self.port_auto_cc_status is not None:
            for k in self.port_auto_cc_status:
                result['PortAutoCcStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.port_auto_cc_status = []
        if m.get('PortAutoCcStatus') is not None:
            for k in m.get('PortAutoCcStatus'):
                temp_model = DescribePortAutoCcStatusResponseBodyPortAutoCcStatus()
                self.port_auto_cc_status.append(temp_model.from_map(k))
        return self


class DescribePortAutoCcStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribePortAutoCcStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePortAutoCcStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortConnsCountRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, end_time=None, start_time=None, port=None,
                 instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.port = TeaConverter.to_unicode(port)  # type: unicode
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.port is not None:
            result['Port'] = self.port
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortConnsCountResponseBody(TeaModel):
    def __init__(self, conns=None, request_id=None, cps=None, in_act_conns=None, act_conns=None):
        self.conns = conns  # type: long
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.cps = cps  # type: long
        self.in_act_conns = in_act_conns  # type: long
        self.act_conns = act_conns  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.conns is not None:
            result['Conns'] = self.conns
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.in_act_conns is not None:
            result['InActConns'] = self.in_act_conns
        if self.act_conns is not None:
            result['ActConns'] = self.act_conns
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Conns') is not None:
            self.conns = m.get('Conns')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('InActConns') is not None:
            self.in_act_conns = m.get('InActConns')
        if m.get('ActConns') is not None:
            self.act_conns = m.get('ActConns')
        return self


class DescribePortConnsCountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribePortConnsCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePortConnsCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortConnsListRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, end_time=None, start_time=None, interval=None,
                 port=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.interval = interval  # type: int
        self.port = TeaConverter.to_unicode(port)  # type: unicode
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.port is not None:
            result['Port'] = self.port
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortConnsListResponseBodyConnsList(TeaModel):
    def __init__(self, act_conns=None, in_act_conns=None, index=None, time=None, cps=None, conns=None):
        self.act_conns = act_conns  # type: long
        self.in_act_conns = in_act_conns  # type: long
        self.index = index  # type: long
        self.time = time  # type: long
        self.cps = cps  # type: long
        self.conns = conns  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.act_conns is not None:
            result['ActConns'] = self.act_conns
        if self.in_act_conns is not None:
            result['InActConns'] = self.in_act_conns
        if self.index is not None:
            result['Index'] = self.index
        if self.time is not None:
            result['Time'] = self.time
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.conns is not None:
            result['Conns'] = self.conns
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActConns') is not None:
            self.act_conns = m.get('ActConns')
        if m.get('InActConns') is not None:
            self.in_act_conns = m.get('InActConns')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('Conns') is not None:
            self.conns = m.get('Conns')
        return self


class DescribePortConnsListResponseBody(TeaModel):
    def __init__(self, conns_list=None, request_id=None):
        self.conns_list = conns_list  # type: list[DescribePortConnsListResponseBodyConnsList]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.conns_list:
            for k in self.conns_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ConnsList'] = []
        if self.conns_list is not None:
            for k in self.conns_list:
                result['ConnsList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.conns_list = []
        if m.get('ConnsList') is not None:
            for k in m.get('ConnsList'):
                temp_model = DescribePortConnsListResponseBodyConnsList()
                self.conns_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePortConnsListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribePortConnsListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePortConnsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortFlowListRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, end_time=None, start_time=None, interval=None,
                 instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.interval = interval  # type: int
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortFlowListResponseBodyPortFlowList(TeaModel):
    def __init__(self, index=None, time=None, in_pps=None, in_bps=None, region=None, out_pps=None, attack_pps=None,
                 out_bps=None, attack_bps=None):
        self.index = index  # type: long
        self.time = time  # type: long
        self.in_pps = in_pps  # type: long
        self.in_bps = in_bps  # type: long
        self.region = TeaConverter.to_unicode(region)  # type: unicode
        self.out_pps = out_pps  # type: long
        self.attack_pps = attack_pps  # type: long
        self.out_bps = out_bps  # type: long
        self.attack_bps = attack_bps  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.time is not None:
            result['Time'] = self.time
        if self.in_pps is not None:
            result['InPps'] = self.in_pps
        if self.in_bps is not None:
            result['InBps'] = self.in_bps
        if self.region is not None:
            result['Region'] = self.region
        if self.out_pps is not None:
            result['OutPps'] = self.out_pps
        if self.attack_pps is not None:
            result['AttackPps'] = self.attack_pps
        if self.out_bps is not None:
            result['OutBps'] = self.out_bps
        if self.attack_bps is not None:
            result['AttackBps'] = self.attack_bps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('InPps') is not None:
            self.in_pps = m.get('InPps')
        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('OutPps') is not None:
            self.out_pps = m.get('OutPps')
        if m.get('AttackPps') is not None:
            self.attack_pps = m.get('AttackPps')
        if m.get('OutBps') is not None:
            self.out_bps = m.get('OutBps')
        if m.get('AttackBps') is not None:
            self.attack_bps = m.get('AttackBps')
        return self


class DescribePortFlowListResponseBody(TeaModel):
    def __init__(self, request_id=None, port_flow_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.port_flow_list = port_flow_list  # type: list[DescribePortFlowListResponseBodyPortFlowList]

    def validate(self):
        if self.port_flow_list:
            for k in self.port_flow_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PortFlowList'] = []
        if self.port_flow_list is not None:
            for k in self.port_flow_list:
                result['PortFlowList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.port_flow_list = []
        if m.get('PortFlowList') is not None:
            for k in m.get('PortFlowList'):
                temp_model = DescribePortFlowListResponseBodyPortFlowList()
                self.port_flow_list.append(temp_model.from_map(k))
        return self


class DescribePortFlowListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribePortFlowListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePortFlowListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortMaxConnsRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, end_time=None, start_time=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortMaxConnsResponseBodyPortMaxConns(TeaModel):
    def __init__(self, cps=None, ip=None, port=None):
        self.cps = cps  # type: long
        self.ip = TeaConverter.to_unicode(ip)  # type: unicode
        self.port = TeaConverter.to_unicode(port)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribePortMaxConnsResponseBody(TeaModel):
    def __init__(self, port_max_conns=None, request_id=None):
        self.port_max_conns = port_max_conns  # type: list[DescribePortMaxConnsResponseBodyPortMaxConns]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.port_max_conns:
            for k in self.port_max_conns:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PortMaxConns'] = []
        if self.port_max_conns is not None:
            for k in self.port_max_conns:
                result['PortMaxConns'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.port_max_conns = []
        if m.get('PortMaxConns') is not None:
            for k in m.get('PortMaxConns'):
                temp_model = DescribePortMaxConnsResponseBodyPortMaxConns()
                self.port_max_conns.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePortMaxConnsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribePortMaxConnsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePortMaxConnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortViewSourceCountriesRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, end_time=None, start_time=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortViewSourceCountriesResponseBodySourceCountrys(TeaModel):
    def __init__(self, country_id=None, count=None):
        self.country_id = TeaConverter.to_unicode(country_id)  # type: unicode
        self.count = count  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePortViewSourceCountriesResponseBody(TeaModel):
    def __init__(self, request_id=None, source_countrys=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.source_countrys = source_countrys  # type: list[DescribePortViewSourceCountriesResponseBodySourceCountrys]

    def validate(self):
        if self.source_countrys:
            for k in self.source_countrys:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SourceCountrys'] = []
        if self.source_countrys is not None:
            for k in self.source_countrys:
                result['SourceCountrys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.source_countrys = []
        if m.get('SourceCountrys') is not None:
            for k in m.get('SourceCountrys'):
                temp_model = DescribePortViewSourceCountriesResponseBodySourceCountrys()
                self.source_countrys.append(temp_model.from_map(k))
        return self


class DescribePortViewSourceCountriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribePortViewSourceCountriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePortViewSourceCountriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortViewSourceIspsRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, end_time=None, start_time=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortViewSourceIspsResponseBodyIsps(TeaModel):
    def __init__(self, isp_id=None, count=None):
        self.isp_id = TeaConverter.to_unicode(isp_id)  # type: unicode
        self.count = count  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.isp_id is not None:
            result['IspId'] = self.isp_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IspId') is not None:
            self.isp_id = m.get('IspId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePortViewSourceIspsResponseBody(TeaModel):
    def __init__(self, request_id=None, isps=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.isps = isps  # type: list[DescribePortViewSourceIspsResponseBodyIsps]

    def validate(self):
        if self.isps:
            for k in self.isps:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Isps'] = []
        if self.isps is not None:
            for k in self.isps:
                result['Isps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.isps = []
        if m.get('Isps') is not None:
            for k in m.get('Isps'):
                temp_model = DescribePortViewSourceIspsResponseBodyIsps()
                self.isps.append(temp_model.from_map(k))
        return self


class DescribePortViewSourceIspsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribePortViewSourceIspsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePortViewSourceIspsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortViewSourceProvincesRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, end_time=None, start_time=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortViewSourceProvincesResponseBodySourceProvinces(TeaModel):
    def __init__(self, province_id=None, count=None):
        self.province_id = TeaConverter.to_unicode(province_id)  # type: unicode
        self.count = count  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.province_id is not None:
            result['ProvinceId'] = self.province_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProvinceId') is not None:
            self.province_id = m.get('ProvinceId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePortViewSourceProvincesResponseBody(TeaModel):
    def __init__(self, source_provinces=None, request_id=None):
        self.source_provinces = source_provinces  # type: list[DescribePortViewSourceProvincesResponseBodySourceProvinces]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.source_provinces:
            for k in self.source_provinces:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SourceProvinces'] = []
        if self.source_provinces is not None:
            for k in self.source_provinces:
                result['SourceProvinces'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.source_provinces = []
        if m.get('SourceProvinces') is not None:
            for k in m.get('SourceProvinces'):
                temp_model = DescribePortViewSourceProvincesResponseBodySourceProvinces()
                self.source_provinces.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePortViewSourceProvincesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribePortViewSourceProvincesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePortViewSourceProvincesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSceneDefenseObjectsRequest(TeaModel):
    def __init__(self, source_ip=None, policy_id=None, resource_group_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.policy_id = TeaConverter.to_unicode(policy_id)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSceneDefenseObjectsResponseBodyObjects(TeaModel):
    def __init__(self, domain=None, policy_id=None, vip=None):
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.policy_id = TeaConverter.to_unicode(policy_id)  # type: unicode
        self.vip = TeaConverter.to_unicode(vip)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.vip is not None:
            result['Vip'] = self.vip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Vip') is not None:
            self.vip = m.get('Vip')
        return self


class DescribeSceneDefenseObjectsResponseBody(TeaModel):
    def __init__(self, request_id=None, objects=None, success=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.objects = objects  # type: list[DescribeSceneDefenseObjectsResponseBodyObjects]
        self.success = success  # type: bool

    def validate(self):
        if self.objects:
            for k in self.objects:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Objects'] = []
        if self.objects is not None:
            for k in self.objects:
                result['Objects'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.objects = []
        if m.get('Objects') is not None:
            for k in m.get('Objects'):
                temp_model = DescribeSceneDefenseObjectsResponseBodyObjects()
                self.objects.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSceneDefenseObjectsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeSceneDefenseObjectsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSceneDefenseObjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSceneDefensePoliciesRequest(TeaModel):
    def __init__(self, source_ip=None, template=None, status=None, resource_group_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.template = TeaConverter.to_unicode(template)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.template is not None:
            result['Template'] = self.template
        if self.status is not None:
            result['Status'] = self.status
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSceneDefensePoliciesResponseBodyPoliciesRuntimePolicies(TeaModel):
    def __init__(self, status=None, old_value=None, new_value=None, policy_type=None):
        self.status = status  # type: int
        self.old_value = TeaConverter.to_unicode(old_value)  # type: unicode
        self.new_value = TeaConverter.to_unicode(new_value)  # type: unicode
        self.policy_type = policy_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.old_value is not None:
            result['oldValue'] = self.old_value
        if self.new_value is not None:
            result['NewValue'] = self.new_value
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('oldValue') is not None:
            self.old_value = m.get('oldValue')
        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class DescribeSceneDefensePoliciesResponseBodyPolicies(TeaModel):
    def __init__(self, done=None, end_time=None, status=None, start_time=None, object_count=None, template=None,
                 policy_id=None, name=None, runtime_policies=None):
        self.done = done  # type: int
        self.end_time = end_time  # type: long
        self.status = status  # type: int
        self.start_time = start_time  # type: long
        self.object_count = object_count  # type: int
        self.template = TeaConverter.to_unicode(template)  # type: unicode
        self.policy_id = TeaConverter.to_unicode(policy_id)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.runtime_policies = runtime_policies  # type: list[DescribeSceneDefensePoliciesResponseBodyPoliciesRuntimePolicies]

    def validate(self):
        if self.runtime_policies:
            for k in self.runtime_policies:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.done is not None:
            result['Done'] = self.done
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.object_count is not None:
            result['ObjectCount'] = self.object_count
        if self.template is not None:
            result['Template'] = self.template
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.name is not None:
            result['Name'] = self.name
        result['RuntimePolicies'] = []
        if self.runtime_policies is not None:
            for k in self.runtime_policies:
                result['RuntimePolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Done') is not None:
            self.done = m.get('Done')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ObjectCount') is not None:
            self.object_count = m.get('ObjectCount')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.runtime_policies = []
        if m.get('RuntimePolicies') is not None:
            for k in m.get('RuntimePolicies'):
                temp_model = DescribeSceneDefensePoliciesResponseBodyPoliciesRuntimePolicies()
                self.runtime_policies.append(temp_model.from_map(k))
        return self


class DescribeSceneDefensePoliciesResponseBody(TeaModel):
    def __init__(self, policies=None, request_id=None, success=None):
        self.policies = policies  # type: list[DescribeSceneDefensePoliciesResponseBodyPolicies]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = DescribeSceneDefensePoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSceneDefensePoliciesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeSceneDefensePoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSceneDefensePoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSchedulerRulesRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, rule_name=None, offset=None, page_number=None,
                 page_size=None, is_offset=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode
        self.offset = offset  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.is_offset = is_offset  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.is_offset is not None:
            result['IsOffset'] = self.is_offset
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('IsOffset') is not None:
            self.is_offset = m.get('IsOffset')
        return self


class DescribeSchedulerRulesResponseBodySchedulerRulesParamParamData(TeaModel):
    def __init__(self, cloud_instance_id=None):
        self.cloud_instance_id = TeaConverter.to_unicode(cloud_instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cloud_instance_id is not None:
            result['CloudInstanceId'] = self.cloud_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CloudInstanceId') is not None:
            self.cloud_instance_id = m.get('CloudInstanceId')
        return self


class DescribeSchedulerRulesResponseBodySchedulerRulesParam(TeaModel):
    def __init__(self, param_data=None, param_type=None):
        self.param_data = param_data  # type: DescribeSchedulerRulesResponseBodySchedulerRulesParamParamData
        self.param_type = TeaConverter.to_unicode(param_type)  # type: unicode

    def validate(self):
        if self.param_data:
            self.param_data.validate()

    def to_map(self):
        result = dict()
        if self.param_data is not None:
            result['ParamData'] = self.param_data.to_map()
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParamData') is not None:
            temp_model = DescribeSchedulerRulesResponseBodySchedulerRulesParamParamData()
            self.param_data = temp_model.from_map(m['ParamData'])
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        return self


class DescribeSchedulerRulesResponseBodySchedulerRulesRules(TeaModel):
    def __init__(self, type=None, status=None, value=None, value_type=None, priority=None, restore_delay=None,
                 region_id=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.status = status  # type: int
        self.value = TeaConverter.to_unicode(value)  # type: unicode
        self.value_type = value_type  # type: int
        self.priority = priority  # type: int
        self.restore_delay = restore_delay  # type: int
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.value is not None:
            result['Value'] = self.value
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.restore_delay is not None:
            result['RestoreDelay'] = self.restore_delay
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RestoreDelay') is not None:
            self.restore_delay = m.get('RestoreDelay')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSchedulerRulesResponseBodySchedulerRules(TeaModel):
    def __init__(self, rule_type=None, param=None, cname=None, rules=None, rule_name=None):
        self.rule_type = TeaConverter.to_unicode(rule_type)  # type: unicode
        self.param = param  # type: DescribeSchedulerRulesResponseBodySchedulerRulesParam
        self.cname = TeaConverter.to_unicode(cname)  # type: unicode
        self.rules = rules  # type: list[DescribeSchedulerRulesResponseBodySchedulerRulesRules]
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode

    def validate(self):
        if self.param:
            self.param.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.param is not None:
            result['Param'] = self.param.to_map()
        if self.cname is not None:
            result['Cname'] = self.cname
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Param') is not None:
            temp_model = DescribeSchedulerRulesResponseBodySchedulerRulesParam()
            self.param = temp_model.from_map(m['Param'])
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeSchedulerRulesResponseBodySchedulerRulesRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DescribeSchedulerRulesResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, scheduler_rules=None):
        self.total_count = TeaConverter.to_unicode(total_count)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.scheduler_rules = scheduler_rules  # type: list[DescribeSchedulerRulesResponseBodySchedulerRules]

    def validate(self):
        if self.scheduler_rules:
            for k in self.scheduler_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SchedulerRules'] = []
        if self.scheduler_rules is not None:
            for k in self.scheduler_rules:
                result['SchedulerRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scheduler_rules = []
        if m.get('SchedulerRules') is not None:
            for k in m.get('SchedulerRules'):
                temp_model = DescribeSchedulerRulesResponseBodySchedulerRules()
                self.scheduler_rules.append(temp_model.from_map(k))
        return self


class DescribeSchedulerRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeSchedulerRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSchedulerRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlsAuthStatusRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSlsAuthStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, sls_auth_status=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.sls_auth_status = sls_auth_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_auth_status is not None:
            result['SlsAuthStatus'] = self.sls_auth_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsAuthStatus') is not None:
            self.sls_auth_status = m.get('SlsAuthStatus')
        return self


class DescribeSlsAuthStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeSlsAuthStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSlsAuthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlsLogstoreInfoRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSlsLogstoreInfoResponseBody(TeaModel):
    def __init__(self, project=None, request_id=None, quota=None, log_store=None, used=None, ttl=None):
        self.project = TeaConverter.to_unicode(project)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.quota = quota  # type: long
        self.log_store = TeaConverter.to_unicode(log_store)  # type: unicode
        self.used = used  # type: long
        self.ttl = ttl  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.used is not None:
            result['Used'] = self.used
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Used') is not None:
            self.used = m.get('Used')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class DescribeSlsLogstoreInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeSlsLogstoreInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSlsLogstoreInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlsOpenStatusRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSlsOpenStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, sls_open_status=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.sls_open_status = sls_open_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_open_status is not None:
            result['SlsOpenStatus'] = self.sls_open_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsOpenStatus') is not None:
            self.sls_open_status = m.get('SlsOpenStatus')
        return self


class DescribeSlsOpenStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeSlsOpenStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSlsOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStsGrantStatusRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, role=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.role = TeaConverter.to_unicode(role)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class DescribeStsGrantStatusResponseBodyStsGrant(TeaModel):
    def __init__(self, status=None):
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeStsGrantStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, sts_grant=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.sts_grant = sts_grant  # type: DescribeStsGrantStatusResponseBodyStsGrant

    def validate(self):
        if self.sts_grant:
            self.sts_grant.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sts_grant is not None:
            result['StsGrant'] = self.sts_grant.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StsGrant') is not None:
            temp_model = DescribeStsGrantStatusResponseBodyStsGrant()
            self.sts_grant = temp_model.from_map(m['StsGrant'])
        return self


class DescribeStsGrantStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeStsGrantStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeStsGrantStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagKeysRequest(TeaModel):
    def __init__(self, source_ip=None, region_id=None, resource_group_id=None, resource_type=None, page_size=None,
                 page_number=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeTagKeysResponseBodyTagKeys(TeaModel):
    def __init__(self, tag_count=None, tag_key=None):
        self.tag_count = tag_count  # type: int
        self.tag_key = TeaConverter.to_unicode(tag_key)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class DescribeTagKeysResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, page_size=None, page_number=None, tag_keys=None):
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.tag_keys = tag_keys  # type: list[DescribeTagKeysResponseBodyTagKeys]

    def validate(self):
        if self.tag_keys:
            for k in self.tag_keys:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k in self.tag_keys:
                result['TagKeys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k in m.get('TagKeys'):
                temp_model = DescribeTagKeysResponseBodyTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
        return self


class DescribeTagKeysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeTagKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagResourcesRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.value = TeaConverter.to_unicode(value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, source_ip=None, region_id=None, resource_group_id=None, resource_type=None, next_token=None,
                 resource_ids=None, tags=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.resource_ids = resource_ids  # type: list[unicode]
        self.tags = tags  # type: list[DescribeTagResourcesRequestTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeTagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, resource_type=None, tag_value=None, resource_id=None, tag_key=None):
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.tag_value = TeaConverter.to_unicode(tag_value)  # type: unicode
        self.resource_id = TeaConverter.to_unicode(resource_id)  # type: unicode
        self.tag_key = TeaConverter.to_unicode(tag_key)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class DescribeTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, tag_resource=None):
        self.tag_resource = tag_resource  # type: list[DescribeTagResourcesResponseBodyTagResourcesTagResource]

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = DescribeTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class DescribeTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.tag_resources = tag_resources  # type: DescribeTagResourcesResponseBodyTagResources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = DescribeTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class DescribeTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
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


class DescribeUnBlackholeCountRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeUnBlackholeCountResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, remain_count=None):
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.remain_count = remain_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.remain_count is not None:
            result['RemainCount'] = self.remain_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RemainCount') is not None:
            self.remain_count = m.get('RemainCount')
        return self


class DescribeUnBlackholeCountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeUnBlackholeCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUnBlackholeCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUnBlockCountRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeUnBlockCountResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, remain_count=None):
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.remain_count = remain_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.remain_count is not None:
            result['RemainCount'] = self.remain_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RemainCount') is not None:
            self.remain_count = m.get('RemainCount')
        return self


class DescribeUnBlockCountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeUnBlockCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUnBlockCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebAccessLogDispatchStatusRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None, page_number=None, page_size=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeWebAccessLogDispatchStatusResponseBodySlsConfigStatus(TeaModel):
    def __init__(self, domain=None, enable=None):
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.enable = enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DescribeWebAccessLogDispatchStatusResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, sls_config_status=None):
        self.total_count = total_count  # type: int
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.sls_config_status = sls_config_status  # type: list[DescribeWebAccessLogDispatchStatusResponseBodySlsConfigStatus]

    def validate(self):
        if self.sls_config_status:
            for k in self.sls_config_status:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SlsConfigStatus'] = []
        if self.sls_config_status is not None:
            for k in self.sls_config_status:
                result['SlsConfigStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sls_config_status = []
        if m.get('SlsConfigStatus') is not None:
            for k in m.get('SlsConfigStatus'):
                temp_model = DescribeWebAccessLogDispatchStatusResponseBodySlsConfigStatus()
                self.sls_config_status.append(temp_model.from_map(k))
        return self


class DescribeWebAccessLogDispatchStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeWebAccessLogDispatchStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebAccessLogDispatchStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebAccessLogEmptyCountRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeWebAccessLogEmptyCountResponseBody(TeaModel):
    def __init__(self, request_id=None, available_count=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.available_count = available_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.available_count is not None:
            result['AvailableCount'] = self.available_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AvailableCount') is not None:
            self.available_count = m.get('AvailableCount')
        return self


class DescribeWebAccessLogEmptyCountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeWebAccessLogEmptyCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebAccessLogEmptyCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebAccessLogStatusRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None, domain=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeWebAccessLogStatusResponseBody(TeaModel):
    def __init__(self, sls_project=None, sls_status=None, request_id=None, sls_logstore=None):
        self.sls_project = TeaConverter.to_unicode(sls_project)  # type: unicode
        self.sls_status = sls_status  # type: bool
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.sls_logstore = TeaConverter.to_unicode(sls_logstore)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project
        if self.sls_status is not None:
            result['SlsStatus'] = self.sls_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_logstore is not None:
            result['SlsLogstore'] = self.sls_logstore
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')
        if m.get('SlsStatus') is not None:
            self.sls_status = m.get('SlsStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsLogstore') is not None:
            self.sls_logstore = m.get('SlsLogstore')
        return self


class DescribeWebAccessLogStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeWebAccessLogStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebAccessLogStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebAccessModeRequest(TeaModel):
    def __init__(self, source_ip=None, domains=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.domains = domains  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class DescribeWebAccessModeResponseBodyDomainModes(TeaModel):
    def __init__(self, access_mode=None, domain=None):
        self.access_mode = access_mode  # type: int
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeWebAccessModeResponseBody(TeaModel):
    def __init__(self, request_id=None, domain_modes=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.domain_modes = domain_modes  # type: list[DescribeWebAccessModeResponseBodyDomainModes]

    def validate(self):
        if self.domain_modes:
            for k in self.domain_modes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DomainModes'] = []
        if self.domain_modes is not None:
            for k in self.domain_modes:
                result['DomainModes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.domain_modes = []
        if m.get('DomainModes') is not None:
            for k in m.get('DomainModes'):
                temp_model = DescribeWebAccessModeResponseBodyDomainModes()
                self.domain_modes.append(temp_model.from_map(k))
        return self


class DescribeWebAccessModeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeWebAccessModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebAccessModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebAreaBlockConfigsRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domains=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domains = domains  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigsRegionList(TeaModel):
    def __init__(self, block=None, region=None):
        self.block = block  # type: int
        self.region = TeaConverter.to_unicode(region)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.block is not None:
            result['Block'] = self.block
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigs(TeaModel):
    def __init__(self, domain=None, region_list=None):
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.region_list = region_list  # type: list[DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigsRegionList]

    def validate(self):
        if self.region_list:
            for k in self.region_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        result['RegionList'] = []
        if self.region_list is not None:
            for k in self.region_list:
                result['RegionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        self.region_list = []
        if m.get('RegionList') is not None:
            for k in m.get('RegionList'):
                temp_model = DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigsRegionList()
                self.region_list.append(temp_model.from_map(k))
        return self


class DescribeWebAreaBlockConfigsResponseBody(TeaModel):
    def __init__(self, area_block_configs=None, request_id=None):
        self.area_block_configs = area_block_configs  # type: list[DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigs]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.area_block_configs:
            for k in self.area_block_configs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AreaBlockConfigs'] = []
        if self.area_block_configs is not None:
            for k in self.area_block_configs:
                result['AreaBlockConfigs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.area_block_configs = []
        if m.get('AreaBlockConfigs') is not None:
            for k in m.get('AreaBlockConfigs'):
                temp_model = DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigs()
                self.area_block_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWebAreaBlockConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeWebAreaBlockConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebAreaBlockConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebCacheConfigsRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domains=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domains = domains  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class DescribeWebCacheConfigsResponseBodyDomainCacheConfigsCustomRules(TeaModel):
    def __init__(self, cache_ttl=None, mode=None, name=None, uri=None):
        self.cache_ttl = cache_ttl  # type: long
        self.mode = TeaConverter.to_unicode(mode)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.uri = TeaConverter.to_unicode(uri)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cache_ttl is not None:
            result['CacheTtl'] = self.cache_ttl
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.name is not None:
            result['Name'] = self.name
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CacheTtl') is not None:
            self.cache_ttl = m.get('CacheTtl')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DescribeWebCacheConfigsResponseBodyDomainCacheConfigs(TeaModel):
    def __init__(self, domain=None, custom_rules=None, mode=None, enable=None):
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.custom_rules = custom_rules  # type: list[DescribeWebCacheConfigsResponseBodyDomainCacheConfigsCustomRules]
        self.mode = TeaConverter.to_unicode(mode)  # type: unicode
        self.enable = enable  # type: int

    def validate(self):
        if self.custom_rules:
            for k in self.custom_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        result['CustomRules'] = []
        if self.custom_rules is not None:
            for k in self.custom_rules:
                result['CustomRules'].append(k.to_map() if k else None)
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        self.custom_rules = []
        if m.get('CustomRules') is not None:
            for k in m.get('CustomRules'):
                temp_model = DescribeWebCacheConfigsResponseBodyDomainCacheConfigsCustomRules()
                self.custom_rules.append(temp_model.from_map(k))
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DescribeWebCacheConfigsResponseBody(TeaModel):
    def __init__(self, request_id=None, domain_cache_configs=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.domain_cache_configs = domain_cache_configs  # type: list[DescribeWebCacheConfigsResponseBodyDomainCacheConfigs]

    def validate(self):
        if self.domain_cache_configs:
            for k in self.domain_cache_configs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DomainCacheConfigs'] = []
        if self.domain_cache_configs is not None:
            for k in self.domain_cache_configs:
                result['DomainCacheConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.domain_cache_configs = []
        if m.get('DomainCacheConfigs') is not None:
            for k in m.get('DomainCacheConfigs'):
                temp_model = DescribeWebCacheConfigsResponseBodyDomainCacheConfigs()
                self.domain_cache_configs.append(temp_model.from_map(k))
        return self


class DescribeWebCacheConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeWebCacheConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebCacheConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebCcProtectSwitchRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domains=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domains = domains  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class DescribeWebCcProtectSwitchResponseBodyProtectSwitchList(TeaModel):
    def __init__(self, black_white_list_enable=None, ai_template=None, precise_rule_enable=None, domain=None,
                 ai_mode=None, ai_rule_enable=None, region_block_enable=None, cc_template=None, cc_custom_rule_enable=None,
                 cc_enable=None):
        self.black_white_list_enable = black_white_list_enable  # type: int
        self.ai_template = TeaConverter.to_unicode(ai_template)  # type: unicode
        self.precise_rule_enable = precise_rule_enable  # type: int
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.ai_mode = TeaConverter.to_unicode(ai_mode)  # type: unicode
        self.ai_rule_enable = ai_rule_enable  # type: int
        self.region_block_enable = region_block_enable  # type: int
        self.cc_template = TeaConverter.to_unicode(cc_template)  # type: unicode
        self.cc_custom_rule_enable = cc_custom_rule_enable  # type: int
        self.cc_enable = cc_enable  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.black_white_list_enable is not None:
            result['BlackWhiteListEnable'] = self.black_white_list_enable
        if self.ai_template is not None:
            result['AiTemplate'] = self.ai_template
        if self.precise_rule_enable is not None:
            result['PreciseRuleEnable'] = self.precise_rule_enable
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.ai_mode is not None:
            result['AiMode'] = self.ai_mode
        if self.ai_rule_enable is not None:
            result['AiRuleEnable'] = self.ai_rule_enable
        if self.region_block_enable is not None:
            result['RegionBlockEnable'] = self.region_block_enable
        if self.cc_template is not None:
            result['CcTemplate'] = self.cc_template
        if self.cc_custom_rule_enable is not None:
            result['CcCustomRuleEnable'] = self.cc_custom_rule_enable
        if self.cc_enable is not None:
            result['CcEnable'] = self.cc_enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackWhiteListEnable') is not None:
            self.black_white_list_enable = m.get('BlackWhiteListEnable')
        if m.get('AiTemplate') is not None:
            self.ai_template = m.get('AiTemplate')
        if m.get('PreciseRuleEnable') is not None:
            self.precise_rule_enable = m.get('PreciseRuleEnable')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('AiMode') is not None:
            self.ai_mode = m.get('AiMode')
        if m.get('AiRuleEnable') is not None:
            self.ai_rule_enable = m.get('AiRuleEnable')
        if m.get('RegionBlockEnable') is not None:
            self.region_block_enable = m.get('RegionBlockEnable')
        if m.get('CcTemplate') is not None:
            self.cc_template = m.get('CcTemplate')
        if m.get('CcCustomRuleEnable') is not None:
            self.cc_custom_rule_enable = m.get('CcCustomRuleEnable')
        if m.get('CcEnable') is not None:
            self.cc_enable = m.get('CcEnable')
        return self


class DescribeWebCcProtectSwitchResponseBody(TeaModel):
    def __init__(self, request_id=None, protect_switch_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.protect_switch_list = protect_switch_list  # type: list[DescribeWebCcProtectSwitchResponseBodyProtectSwitchList]

    def validate(self):
        if self.protect_switch_list:
            for k in self.protect_switch_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ProtectSwitchList'] = []
        if self.protect_switch_list is not None:
            for k in self.protect_switch_list:
                result['ProtectSwitchList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.protect_switch_list = []
        if m.get('ProtectSwitchList') is not None:
            for k in m.get('ProtectSwitchList'):
                temp_model = DescribeWebCcProtectSwitchResponseBodyProtectSwitchList()
                self.protect_switch_list.append(temp_model.from_map(k))
        return self


class DescribeWebCcProtectSwitchResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeWebCcProtectSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebCcProtectSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebCCRulesRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, offset=None, page_number=None,
                 page_size=None, is_offset=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.offset = offset  # type: int
        self.page_number = page_number  # type: int
        self.page_size = TeaConverter.to_unicode(page_size)  # type: unicode
        self.is_offset = is_offset  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.is_offset is not None:
            result['IsOffset'] = self.is_offset
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('IsOffset') is not None:
            self.is_offset = m.get('IsOffset')
        return self


class DescribeWebCCRulesResponseBodyWebCCRules(TeaModel):
    def __init__(self, ttl=None, act=None, interval=None, mode=None, name=None, uri=None, count=None):
        self.ttl = ttl  # type: int
        self.act = TeaConverter.to_unicode(act)  # type: unicode
        self.interval = interval  # type: int
        self.mode = TeaConverter.to_unicode(mode)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.uri = TeaConverter.to_unicode(uri)  # type: unicode
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.act is not None:
            result['Act'] = self.act
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.name is not None:
            result['Name'] = self.name
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeWebCCRulesResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, web_ccrules=None):
        self.total_count = total_count  # type: long
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.web_ccrules = web_ccrules  # type: list[DescribeWebCCRulesResponseBodyWebCCRules]

    def validate(self):
        if self.web_ccrules:
            for k in self.web_ccrules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['WebCCRules'] = []
        if self.web_ccrules is not None:
            for k in self.web_ccrules:
                result['WebCCRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.web_ccrules = []
        if m.get('WebCCRules') is not None:
            for k in m.get('WebCCRules'):
                temp_model = DescribeWebCCRulesResponseBodyWebCCRules()
                self.web_ccrules.append(temp_model.from_map(k))
        return self


class DescribeWebCCRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeWebCCRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebCCRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebCustomPortsRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeWebCustomPortsResponseBodyWebCustomPorts(TeaModel):
    def __init__(self, proxy_ports=None, proxy_type=None):
        self.proxy_ports = proxy_ports  # type: list[unicode]
        self.proxy_type = TeaConverter.to_unicode(proxy_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.proxy_ports is not None:
            result['ProxyPorts'] = self.proxy_ports
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProxyPorts') is not None:
            self.proxy_ports = m.get('ProxyPorts')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        return self


class DescribeWebCustomPortsResponseBody(TeaModel):
    def __init__(self, request_id=None, web_custom_ports=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.web_custom_ports = web_custom_ports  # type: list[DescribeWebCustomPortsResponseBodyWebCustomPorts]

    def validate(self):
        if self.web_custom_ports:
            for k in self.web_custom_ports:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['WebCustomPorts'] = []
        if self.web_custom_ports is not None:
            for k in self.web_custom_ports:
                result['WebCustomPorts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.web_custom_ports = []
        if m.get('WebCustomPorts') is not None:
            for k in m.get('WebCustomPorts'):
                temp_model = DescribeWebCustomPortsResponseBodyWebCustomPorts()
                self.web_custom_ports.append(temp_model.from_map(k))
        return self


class DescribeWebCustomPortsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeWebCustomPortsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebCustomPortsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebInstanceRelationsRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domains=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domains = domains  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class DescribeWebInstanceRelationsResponseBodyWebInstanceRelationsInstanceDetails(TeaModel):
    def __init__(self, eip_list=None, function_version=None, instance_id=None):
        self.eip_list = eip_list  # type: list[unicode]
        self.function_version = TeaConverter.to_unicode(function_version)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.eip_list is not None:
            result['EipList'] = self.eip_list
        if self.function_version is not None:
            result['FunctionVersion'] = self.function_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EipList') is not None:
            self.eip_list = m.get('EipList')
        if m.get('FunctionVersion') is not None:
            self.function_version = m.get('FunctionVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeWebInstanceRelationsResponseBodyWebInstanceRelations(TeaModel):
    def __init__(self, domain=None, instance_details=None):
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.instance_details = instance_details  # type: list[DescribeWebInstanceRelationsResponseBodyWebInstanceRelationsInstanceDetails]

    def validate(self):
        if self.instance_details:
            for k in self.instance_details:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        result['InstanceDetails'] = []
        if self.instance_details is not None:
            for k in self.instance_details:
                result['InstanceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        self.instance_details = []
        if m.get('InstanceDetails') is not None:
            for k in m.get('InstanceDetails'):
                temp_model = DescribeWebInstanceRelationsResponseBodyWebInstanceRelationsInstanceDetails()
                self.instance_details.append(temp_model.from_map(k))
        return self


class DescribeWebInstanceRelationsResponseBody(TeaModel):
    def __init__(self, request_id=None, web_instance_relations=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.web_instance_relations = web_instance_relations  # type: list[DescribeWebInstanceRelationsResponseBodyWebInstanceRelations]

    def validate(self):
        if self.web_instance_relations:
            for k in self.web_instance_relations:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['WebInstanceRelations'] = []
        if self.web_instance_relations is not None:
            for k in self.web_instance_relations:
                result['WebInstanceRelations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.web_instance_relations = []
        if m.get('WebInstanceRelations') is not None:
            for k in m.get('WebInstanceRelations'):
                temp_model = DescribeWebInstanceRelationsResponseBodyWebInstanceRelations()
                self.web_instance_relations.append(temp_model.from_map(k))
        return self


class DescribeWebInstanceRelationsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeWebInstanceRelationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebInstanceRelationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebPreciseAccessRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domains=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domains = domains  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleListConditionList(TeaModel):
    def __init__(self, match_method=None, field=None, content=None, header_name=None):
        self.match_method = TeaConverter.to_unicode(match_method)  # type: unicode
        self.field = TeaConverter.to_unicode(field)  # type: unicode
        self.content = TeaConverter.to_unicode(content)  # type: unicode
        self.header_name = TeaConverter.to_unicode(header_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.match_method is not None:
            result['MatchMethod'] = self.match_method
        if self.field is not None:
            result['Field'] = self.field
        if self.content is not None:
            result['Content'] = self.content
        if self.header_name is not None:
            result['HeaderName'] = self.header_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MatchMethod') is not None:
            self.match_method = m.get('MatchMethod')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('HeaderName') is not None:
            self.header_name = m.get('HeaderName')
        return self


class DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleList(TeaModel):
    def __init__(self, action=None, owner=None, expires=None, name=None, condition_list=None):
        self.action = TeaConverter.to_unicode(action)  # type: unicode
        self.owner = TeaConverter.to_unicode(owner)  # type: unicode
        self.expires = expires  # type: long
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.condition_list = condition_list  # type: list[DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleListConditionList]

    def validate(self):
        if self.condition_list:
            for k in self.condition_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.expires is not None:
            result['Expires'] = self.expires
        if self.name is not None:
            result['Name'] = self.name
        result['ConditionList'] = []
        if self.condition_list is not None:
            for k in self.condition_list:
                result['ConditionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Expires') is not None:
            self.expires = m.get('Expires')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.condition_list = []
        if m.get('ConditionList') is not None:
            for k in m.get('ConditionList'):
                temp_model = DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleListConditionList()
                self.condition_list.append(temp_model.from_map(k))
        return self


class DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigList(TeaModel):
    def __init__(self, domain=None, rule_list=None):
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.rule_list = rule_list  # type: list[DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleList]

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleList()
                self.rule_list.append(temp_model.from_map(k))
        return self


class DescribeWebPreciseAccessRuleResponseBody(TeaModel):
    def __init__(self, precise_access_config_list=None, request_id=None):
        self.precise_access_config_list = precise_access_config_list  # type: list[DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigList]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.precise_access_config_list:
            for k in self.precise_access_config_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PreciseAccessConfigList'] = []
        if self.precise_access_config_list is not None:
            for k in self.precise_access_config_list:
                result['PreciseAccessConfigList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.precise_access_config_list = []
        if m.get('PreciseAccessConfigList') is not None:
            for k in m.get('PreciseAccessConfigList'):
                temp_model = DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigList()
                self.precise_access_config_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWebPreciseAccessRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeWebPreciseAccessRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebPreciseAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebRulesRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, query_domain_pattern=None,
                 page_number=None, page_size=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.query_domain_pattern = TeaConverter.to_unicode(query_domain_pattern)  # type: unicode
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.query_domain_pattern is not None:
            result['QueryDomainPattern'] = self.query_domain_pattern
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('QueryDomainPattern') is not None:
            self.query_domain_pattern = m.get('QueryDomainPattern')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeWebRulesResponseBodyWebRulesRealServers(TeaModel):
    def __init__(self, rs_type=None, real_server=None):
        self.rs_type = rs_type  # type: int
        self.real_server = TeaConverter.to_unicode(real_server)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.real_server is not None:
            result['RealServer'] = self.real_server
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        if m.get('RealServer') is not None:
            self.real_server = m.get('RealServer')
        return self


class DescribeWebRulesResponseBodyWebRulesProxyTypes(TeaModel):
    def __init__(self, proxy_ports=None, proxy_type=None):
        self.proxy_ports = proxy_ports  # type: list[unicode]
        self.proxy_type = TeaConverter.to_unicode(proxy_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.proxy_ports is not None:
            result['ProxyPorts'] = self.proxy_ports
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProxyPorts') is not None:
            self.proxy_ports = m.get('ProxyPorts')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        return self


class DescribeWebRulesResponseBodyWebRules(TeaModel):
    def __init__(self, domain=None, http_2https_enable=None, custom_ciphers=None, black_list=None, white_list=None,
                 real_servers=None, proxy_types=None, ssl_protocols=None, cc_template=None, cc_enabled=None, ssl_ciphers=None,
                 cc_rule_enabled=None, ssl_13enabled=None, proxy_enabled=None, cert_name=None, policy_mode=None, cname=None,
                 http_2enable=None, https_2http_enable=None):
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.http_2https_enable = http_2https_enable  # type: bool
        self.custom_ciphers = custom_ciphers  # type: list[unicode]
        self.black_list = black_list  # type: list[unicode]
        self.white_list = white_list  # type: list[unicode]
        self.real_servers = real_servers  # type: list[DescribeWebRulesResponseBodyWebRulesRealServers]
        self.proxy_types = proxy_types  # type: list[DescribeWebRulesResponseBodyWebRulesProxyTypes]
        self.ssl_protocols = TeaConverter.to_unicode(ssl_protocols)  # type: unicode
        self.cc_template = TeaConverter.to_unicode(cc_template)  # type: unicode
        self.cc_enabled = cc_enabled  # type: bool
        self.ssl_ciphers = TeaConverter.to_unicode(ssl_ciphers)  # type: unicode
        self.cc_rule_enabled = cc_rule_enabled  # type: bool
        self.ssl_13enabled = ssl_13enabled  # type: bool
        self.proxy_enabled = proxy_enabled  # type: bool
        self.cert_name = TeaConverter.to_unicode(cert_name)  # type: unicode
        self.policy_mode = TeaConverter.to_unicode(policy_mode)  # type: unicode
        self.cname = TeaConverter.to_unicode(cname)  # type: unicode
        self.http_2enable = http_2enable  # type: bool
        self.https_2http_enable = https_2http_enable  # type: bool

    def validate(self):
        if self.real_servers:
            for k in self.real_servers:
                if k:
                    k.validate()
        if self.proxy_types:
            for k in self.proxy_types:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.http_2https_enable is not None:
            result['Http2HttpsEnable'] = self.http_2https_enable
        if self.custom_ciphers is not None:
            result['CustomCiphers'] = self.custom_ciphers
        if self.black_list is not None:
            result['BlackList'] = self.black_list
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        result['RealServers'] = []
        if self.real_servers is not None:
            for k in self.real_servers:
                result['RealServers'].append(k.to_map() if k else None)
        result['ProxyTypes'] = []
        if self.proxy_types is not None:
            for k in self.proxy_types:
                result['ProxyTypes'].append(k.to_map() if k else None)
        if self.ssl_protocols is not None:
            result['SslProtocols'] = self.ssl_protocols
        if self.cc_template is not None:
            result['CcTemplate'] = self.cc_template
        if self.cc_enabled is not None:
            result['CcEnabled'] = self.cc_enabled
        if self.ssl_ciphers is not None:
            result['SslCiphers'] = self.ssl_ciphers
        if self.cc_rule_enabled is not None:
            result['CcRuleEnabled'] = self.cc_rule_enabled
        if self.ssl_13enabled is not None:
            result['Ssl13Enabled'] = self.ssl_13enabled
        if self.proxy_enabled is not None:
            result['ProxyEnabled'] = self.proxy_enabled
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.policy_mode is not None:
            result['PolicyMode'] = self.policy_mode
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.http_2enable is not None:
            result['Http2Enable'] = self.http_2enable
        if self.https_2http_enable is not None:
            result['Https2HttpEnable'] = self.https_2http_enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Http2HttpsEnable') is not None:
            self.http_2https_enable = m.get('Http2HttpsEnable')
        if m.get('CustomCiphers') is not None:
            self.custom_ciphers = m.get('CustomCiphers')
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        self.real_servers = []
        if m.get('RealServers') is not None:
            for k in m.get('RealServers'):
                temp_model = DescribeWebRulesResponseBodyWebRulesRealServers()
                self.real_servers.append(temp_model.from_map(k))
        self.proxy_types = []
        if m.get('ProxyTypes') is not None:
            for k in m.get('ProxyTypes'):
                temp_model = DescribeWebRulesResponseBodyWebRulesProxyTypes()
                self.proxy_types.append(temp_model.from_map(k))
        if m.get('SslProtocols') is not None:
            self.ssl_protocols = m.get('SslProtocols')
        if m.get('CcTemplate') is not None:
            self.cc_template = m.get('CcTemplate')
        if m.get('CcEnabled') is not None:
            self.cc_enabled = m.get('CcEnabled')
        if m.get('SslCiphers') is not None:
            self.ssl_ciphers = m.get('SslCiphers')
        if m.get('CcRuleEnabled') is not None:
            self.cc_rule_enabled = m.get('CcRuleEnabled')
        if m.get('Ssl13Enabled') is not None:
            self.ssl_13enabled = m.get('Ssl13Enabled')
        if m.get('ProxyEnabled') is not None:
            self.proxy_enabled = m.get('ProxyEnabled')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('PolicyMode') is not None:
            self.policy_mode = m.get('PolicyMode')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Http2Enable') is not None:
            self.http_2enable = m.get('Http2Enable')
        if m.get('Https2HttpEnable') is not None:
            self.https_2http_enable = m.get('Https2HttpEnable')
        return self


class DescribeWebRulesResponseBody(TeaModel):
    def __init__(self, total_count=None, web_rules=None, request_id=None):
        self.total_count = total_count  # type: long
        self.web_rules = web_rules  # type: list[DescribeWebRulesResponseBodyWebRules]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.web_rules:
            for k in self.web_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['WebRules'] = []
        if self.web_rules is not None:
            for k in self.web_rules:
                result['WebRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.web_rules = []
        if m.get('WebRules') is not None:
            for k in m.get('WebRules'):
                temp_model = DescribeWebRulesResponseBodyWebRules()
                self.web_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWebRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeWebRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachSceneDefenseObjectRequest(TeaModel):
    def __init__(self, source_ip=None, policy_id=None, object_type=None, objects=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.policy_id = TeaConverter.to_unicode(policy_id)  # type: unicode
        self.object_type = TeaConverter.to_unicode(object_type)  # type: unicode
        self.objects = TeaConverter.to_unicode(objects)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.objects is not None:
            result['Objects'] = self.objects
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Objects') is not None:
            self.objects = m.get('Objects')
        return self


class DetachSceneDefenseObjectResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DetachSceneDefenseObjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DetachSceneDefenseObjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachSceneDefenseObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableSceneDefensePolicyRequest(TeaModel):
    def __init__(self, source_ip=None, policy_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.policy_id = TeaConverter.to_unicode(policy_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DisableSceneDefensePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableSceneDefensePolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DisableSceneDefensePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableSceneDefensePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableWebAccessLogConfigRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None, domain=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DisableWebAccessLogConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableWebAccessLogConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DisableWebAccessLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableWebAccessLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableWebCCRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DisableWebCCResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableWebCCResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DisableWebCCResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableWebCCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableWebCCRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DisableWebCCRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableWebCCRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DisableWebCCRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableWebCCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EmptyAutoCcBlacklistRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class EmptyAutoCcBlacklistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EmptyAutoCcBlacklistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: EmptyAutoCcBlacklistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EmptyAutoCcBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EmptyAutoCcWhitelistRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class EmptyAutoCcWhitelistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EmptyAutoCcWhitelistResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: EmptyAutoCcWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EmptyAutoCcWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EmptySlsLogstoreRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class EmptySlsLogstoreResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EmptySlsLogstoreResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: EmptySlsLogstoreResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EmptySlsLogstoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableSceneDefensePolicyRequest(TeaModel):
    def __init__(self, source_ip=None, policy_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.policy_id = TeaConverter.to_unicode(policy_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class EnableSceneDefensePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableSceneDefensePolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: EnableSceneDefensePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableSceneDefensePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableWebAccessLogConfigRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, resource_group_id=None, domain=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class EnableWebAccessLogConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableWebAccessLogConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: EnableWebAccessLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableWebAccessLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableWebCCRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class EnableWebCCResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableWebCCResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: EnableWebCCResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableWebCCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableWebCCRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class EnableWebCCRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableWebCCRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: EnableWebCCRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableWebCCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBlackholeStatusRequest(TeaModel):
    def __init__(self, source_ip=None, blackhole_status=None, instance_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.blackhole_status = TeaConverter.to_unicode(blackhole_status)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.blackhole_status is not None:
            result['BlackholeStatus'] = self.blackhole_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('BlackholeStatus') is not None:
            self.blackhole_status = m.get('BlackholeStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyBlackholeStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyBlackholeStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyBlackholeStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyBlackholeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBlockStatusRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, status=None, duration=None, instance_id=None, lines=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.duration = duration  # type: int
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.lines = lines  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.status is not None:
            result['Status'] = self.status
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lines is not None:
            result['Lines'] = self.lines
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lines') is not None:
            self.lines = m.get('Lines')
        return self


class ModifyBlockStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyBlockStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyBlockStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyBlockStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCnameReuseRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, cname=None, enable=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.cname = TeaConverter.to_unicode(cname)  # type: unicode
        self.enable = enable  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ModifyCnameReuseResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyCnameReuseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyCnameReuseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyCnameReuseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyElasticBandWidthRequest(TeaModel):
    def __init__(self, source_ip=None, elastic_bandwidth=None, instance_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.elastic_bandwidth = elastic_bandwidth  # type: int
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyElasticBandWidthResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyElasticBandWidthResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyElasticBandWidthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyElasticBandWidthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFullLogTtlRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, ttl=None, resource_group_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.ttl = ttl  # type: int
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyFullLogTtlResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyFullLogTtlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyFullLogTtlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyFullLogTtlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHealthCheckConfigRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None, forward_protocol=None, frontend_port=None,
                 health_check=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.forward_protocol = TeaConverter.to_unicode(forward_protocol)  # type: unicode
        self.frontend_port = frontend_port  # type: int
        self.health_check = TeaConverter.to_unicode(health_check)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        return self


class ModifyHealthCheckConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyHealthCheckConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyHealthCheckConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHealthCheckConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHttp2EnableRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, enable=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.enable = enable  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ModifyHttp2EnableResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyHttp2EnableResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyHttp2EnableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHttp2EnableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceRemarkRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None, remark=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.remark = TeaConverter.to_unicode(remark)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ModifyInstanceRemarkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceRemarkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyInstanceRemarkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNetworkRuleAttributeRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None, forward_protocol=None, frontend_port=None, config=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.forward_protocol = TeaConverter.to_unicode(forward_protocol)  # type: unicode
        self.frontend_port = frontend_port  # type: int
        self.config = TeaConverter.to_unicode(config)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ModifyNetworkRuleAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyNetworkRuleAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyNetworkRuleAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyNetworkRuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPortAutoCcStatusRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, instance_id=None, switch=None, mode=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.switch = TeaConverter.to_unicode(switch)  # type: unicode
        self.mode = TeaConverter.to_unicode(mode)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.switch is not None:
            result['Switch'] = self.switch
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Switch') is not None:
            self.switch = m.get('Switch')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class ModifyPortAutoCcStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyPortAutoCcStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyPortAutoCcStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyPortAutoCcStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySceneDefensePolicyRequest(TeaModel):
    def __init__(self, source_ip=None, policy_id=None, name=None, template=None, start_time=None, end_time=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.policy_id = TeaConverter.to_unicode(policy_id)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.template = TeaConverter.to_unicode(template)  # type: unicode
        self.start_time = start_time  # type: long
        self.end_time = end_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.name is not None:
            result['Name'] = self.name
        if self.template is not None:
            result['Template'] = self.template
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class ModifySceneDefensePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifySceneDefensePolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifySceneDefensePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySceneDefensePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySchedulerRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, rules=None, rule_name=None, rule_type=None,
                 param=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.rules = TeaConverter.to_unicode(rules)  # type: unicode
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode
        self.rule_type = rule_type  # type: int
        self.param = TeaConverter.to_unicode(param)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.param is not None:
            result['Param'] = self.param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        return self


class ModifySchedulerRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, cname=None, rule_name=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.cname = TeaConverter.to_unicode(cname)  # type: unicode
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ModifySchedulerRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifySchedulerRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySchedulerRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTlsConfigRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, config=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.config = TeaConverter.to_unicode(config)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ModifyTlsConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyTlsConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyTlsConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyTlsConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebAccessModeRequest(TeaModel):
    def __init__(self, source_ip=None, domain=None, access_mode=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.access_mode = access_mode  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        return self


class ModifyWebAccessModeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWebAccessModeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyWebAccessModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebAccessModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebAIProtectModeRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, config=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.config = TeaConverter.to_unicode(config)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ModifyWebAIProtectModeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWebAIProtectModeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyWebAIProtectModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebAIProtectModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebAIProtectSwitchRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, config=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.config = TeaConverter.to_unicode(config)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ModifyWebAIProtectSwitchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWebAIProtectSwitchResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyWebAIProtectSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebAIProtectSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebAreaBlockRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, regions=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.regions = regions  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.regions is not None:
            result['Regions'] = self.regions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        return self


class ModifyWebAreaBlockResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWebAreaBlockResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyWebAreaBlockResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebAreaBlockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebAreaBlockSwitchRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, config=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.config = TeaConverter.to_unicode(config)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ModifyWebAreaBlockSwitchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWebAreaBlockSwitchResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyWebAreaBlockSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebAreaBlockSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebCacheCustomRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, rules=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.rules = TeaConverter.to_unicode(rules)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.rules is not None:
            result['Rules'] = self.rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        return self


class ModifyWebCacheCustomRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWebCacheCustomRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyWebCacheCustomRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebCacheCustomRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebCacheModeRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, mode=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.mode = TeaConverter.to_unicode(mode)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class ModifyWebCacheModeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWebCacheModeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyWebCacheModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebCacheModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebCacheSwitchRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, enable=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.enable = enable  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ModifyWebCacheSwitchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWebCacheSwitchResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyWebCacheSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebCacheSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebCCRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, name=None, act=None, count=None,
                 interval=None, mode=None, ttl=None, uri=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.act = TeaConverter.to_unicode(act)  # type: unicode
        self.count = count  # type: int
        self.interval = interval  # type: int
        self.mode = TeaConverter.to_unicode(mode)  # type: unicode
        self.ttl = ttl  # type: int
        self.uri = TeaConverter.to_unicode(uri)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.name is not None:
            result['Name'] = self.name
        if self.act is not None:
            result['Act'] = self.act
        if self.count is not None:
            result['Count'] = self.count
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class ModifyWebCCRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWebCCRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyWebCCRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebCCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebIpSetSwitchRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, config=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.config = TeaConverter.to_unicode(config)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ModifyWebIpSetSwitchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWebIpSetSwitchResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyWebIpSetSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebIpSetSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebPreciseAccessRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, rules=None, expires=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.rules = TeaConverter.to_unicode(rules)  # type: unicode
        self.expires = expires  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.expires is not None:
            result['Expires'] = self.expires
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('Expires') is not None:
            self.expires = m.get('Expires')
        return self


class ModifyWebPreciseAccessRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWebPreciseAccessRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyWebPreciseAccessRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebPreciseAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebPreciseAccessSwitchRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, config=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.config = TeaConverter.to_unicode(config)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class ModifyWebPreciseAccessSwitchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWebPreciseAccessSwitchResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyWebPreciseAccessSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebPreciseAccessSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebRuleRequest(TeaModel):
    def __init__(self, source_ip=None, resource_group_id=None, domain=None, proxy_types=None, rs_type=None,
                 https_ext=None, real_servers=None, instance_ids=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.resource_group_id = TeaConverter.to_unicode(resource_group_id)  # type: unicode
        self.domain = TeaConverter.to_unicode(domain)  # type: unicode
        self.proxy_types = TeaConverter.to_unicode(proxy_types)  # type: unicode
        self.rs_type = rs_type  # type: int
        self.https_ext = TeaConverter.to_unicode(https_ext)  # type: unicode
        self.real_servers = real_servers  # type: list[unicode]
        self.instance_ids = instance_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.proxy_types is not None:
            result['ProxyTypes'] = self.proxy_types
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.https_ext is not None:
            result['HttpsExt'] = self.https_ext
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ProxyTypes') is not None:
            self.proxy_types = m.get('ProxyTypes')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        if m.get('HttpsExt') is not None:
            self.https_ext = m.get('HttpsExt')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class ModifyWebRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWebRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyWebRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstanceRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ReleaseInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ReleaseInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleaseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchSchedulerRuleRequest(TeaModel):
    def __init__(self, source_ip=None, rule_name=None, rule_type=None, switch_data=None):
        self.source_ip = TeaConverter.to_unicode(source_ip)  # type: unicode
        self.rule_name = TeaConverter.to_unicode(rule_name)  # type: unicode
        self.rule_type = rule_type  # type: int
        self.switch_data = TeaConverter.to_unicode(switch_data)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.switch_data is not None:
            result['SwitchData'] = self.switch_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('SwitchData') is not None:
            self.switch_data = m.get('SwitchData')
        return self


class SwitchSchedulerRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SwitchSchedulerRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SwitchSchedulerRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SwitchSchedulerRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


