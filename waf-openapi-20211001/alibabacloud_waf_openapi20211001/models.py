# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ClearMajorProtectionBlackIpRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, resource_manager_resource_group_id=None, rule_id=None,
                 template_id=None):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The ID of the IP address blacklist rule for major event protection.
        self.rule_id = rule_id  # type: long
        # The ID of the IP address blacklist rule template for major event protection.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ClearMajorProtectionBlackIpResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, add_list=None, description=None, group_name=None, instance_id=None, region_id=None,
                 resource_manager_resource_group_id=None):
        # The protected objects that you want to add to the protected object group. You can add multiple protected objects to a protected object group at the same time. You can specify multiple protected objects. Separate them with commas (,).
        self.add_list = add_list  # type: str
        # The description of the protected object group.
        self.description = description  # type: str
        # The name of the protected object group that you want to create.
        self.group_name = group_name  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        return self


class CreateDefenseResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, defense_scene=None, instance_id=None, region_id=None,
                 resource_manager_resource_group_id=None, rules=None, template_id=None):
        # The module to which the protection rule that you want to create belongs.
        # 
        # *   **waf_group:** the basic protection rule module.
        # *   **antiscan:** the scan protection module.
        # *   **ip_blacklist:** the IP address blacklist module.
        # *   **custom_acl:** the custom rule module.
        # *   **whitelist:** the whitelist module.
        # *   **region_block:** the region blacklist module.
        # *   **custom_response:** the custom response module.
        # *   **cc:** the HTTP flood protection module.
        # *   **tamperproof:** the website tamper-proofing module.
        # *   **dlp:** the data leakage prevention module.
        self.defense_scene = defense_scene  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The configurations of the protection rule. Specify a string that contains multiple parameters in the JSON format.
        # 
        # >  The parameters vary based on the value of the **DefenseScene** parameter. For more information, see the "**Protection rule parameters**" section in this topic.
        self.rules = rules  # type: str
        # The ID of the protection rule template for which you want to create a protection rule.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateDefenseRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, defense_scene=None, description=None, instance_id=None, region_id=None,
                 resource_manager_resource_group_id=None, template_name=None, template_origin=None, template_status=None, template_type=None):
        # The scenario in which you want to use the protection rule template. For more information, see the description of the **DefenseScene** parameter in the [CreateDefenseRule](~~CreateDefenseRule~~) topic.
        self.defense_scene = defense_scene  # type: str
        # The description of the protection rule template.
        self.description = description  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The name of the protection rule template.
        self.template_name = template_name  # type: str
        # The origin of the protection rule template that you want to create. Set the value to **custom**. The value specifies that the protection rule template is a custom template.
        self.template_origin = template_origin  # type: str
        # The status of the protection rule template. Valid values:
        # 
        # *   **0:** disabled.
        # *   **1:** enabled.
        self.template_status = template_status  # type: int
        # The type of the protection rule template. Valid values:
        # 
        # *   **user_default:** default template.
        # *   **user_custom:** custom template.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the protection rule template.
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
                 protection_resource=None, sm2access_only=None, sm2cert_id=None, sm2enabled=None, tlsversion=None, xff_header_mode=None,
                 xff_headers=None):
        # The ID of the certificate that you want to add. This parameter is available only if you specify **HttpsPorts**.
        self.cert_id = cert_id  # type: str
        # The type of cipher suite that you want to add. This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **1:** all cipher suites.
        # *   **2:** strong cipher suites. You can select this value only if you set **TLSVersion** to **tlsv1.2**.
        # *   **99:** custom cipher suites.
        self.cipher_suite = cipher_suite  # type: int
        # The custom cipher suite that you want to add.
        self.custom_ciphers = custom_ciphers  # type: list[str]
        # Specifies whether to support TLS 1.3. This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable_tlsv_3 = enable_tlsv_3  # type: bool
        # Specifies whether to enable an exclusive IP address. This parameter is available only if you set **IPv6Enabled** to **false** and **ProtectionResource** to **share**. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.exclusive_ip = exclusive_ip  # type: bool
        # Specifies whether to enable HTTP to HTTPS redirection. This parameter is available only if you specify HttpsPorts and leave HttpPorts empty. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.focus_https = focus_https  # type: bool
        # Specifies whether to enable HTTP/2. This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.http_2enabled = http_2enabled  # type: bool
        # The HTTP listener port.
        self.http_ports = http_ports  # type: list[int]
        # The HTTPS listener port.
        self.https_ports = https_ports  # type: list[int]
        # Specifies whether to enable IPv6. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.ipv_6enabled = ipv_6enabled  # type: bool
        # The type of the protection resource. Valid values:
        # 
        # *   **share:** a shared cluster. This is the default value.
        # *   **gslb:** shared cluster-based intelligent load balancing.
        self.protection_resource = protection_resource  # type: str
        # Specifies whether to allow access only from SM certificate-based clients. This parameter is available only if you set SM2Enabled to true.
        # 
        # *   true
        # *   false
        self.sm2access_only = sm2access_only  # type: bool
        # The ID of the SM certificate that you want to add. This parameter is available only if you set SM2Enabled to true.
        self.sm2cert_id = sm2cert_id  # type: str
        # Specifies whether to enable the ShangMi (SM) certificate.
        self.sm2enabled = sm2enabled  # type: bool
        # The version of the Transport Layer Security (TLS) protocol. This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **tlsv1**\
        # *   **tlsv1.1**\
        # *   **tlsv1.2**\
        self.tlsversion = tlsversion  # type: str
        # The method that you want WAF to use to obtain the actual IP address of a client. Valid values:
        # 
        # *   **0:** No Layer 7 proxies are deployed in front of WAF. This is the default value.
        # *   **1:** WAF reads the first value of the X-Forwarded-For (XFF) header field as the IP address of the client.
        # *   **2:** WAF reads the value of a custom header field as the IP address of the client.
        self.xff_header_mode = xff_header_mode  # type: int
        # The custom header field that you want WAF to use to obtain the actual IP address of a client.
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
        if self.sm2access_only is not None:
            result['SM2AccessOnly'] = self.sm2access_only
        if self.sm2cert_id is not None:
            result['SM2CertId'] = self.sm2cert_id
        if self.sm2enabled is not None:
            result['SM2Enabled'] = self.sm2enabled
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
        if m.get('SM2AccessOnly') is not None:
            self.sm2access_only = m.get('SM2AccessOnly')
        if m.get('SM2CertId') is not None:
            self.sm2cert_id = m.get('SM2CertId')
        if m.get('SM2Enabled') is not None:
            self.sm2enabled = m.get('SM2Enabled')
        if m.get('TLSVersion') is not None:
            self.tlsversion = m.get('TLSVersion')
        if m.get('XffHeaderMode') is not None:
            self.xff_header_mode = m.get('XffHeaderMode')
        if m.get('XffHeaders') is not None:
            self.xff_headers = m.get('XffHeaders')
        return self


class CreateDomainRequestRedirectRequestHeaders(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the custom header field.
        self.key = key  # type: str
        # The value of the custom header field.
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
    def __init__(self, backends=None, cname_enabled=None, connect_timeout=None, focus_http_backend=None,
                 keepalive=None, keepalive_requests=None, keepalive_timeout=None, loadbalance=None, read_timeout=None,
                 request_headers=None, retry=None, routing_rules=None, sni_enabled=None, sni_host=None, write_timeout=None):
        # The IP addresses or domain names of the origin server.
        self.backends = backends  # type: list[str]
        # Specifies whether to enable the public cloud disaster recovery feature. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.cname_enabled = cname_enabled  # type: bool
        # The connection timeout period. Unit: seconds. Valid values: 1 to 3600.
        self.connect_timeout = connect_timeout  # type: int
        # Specifies whether to enable HTTPS to HTTP redirection for back-to-origin requests. This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.focus_http_backend = focus_http_backend  # type: bool
        # Specifies whether to enable the persistent connection feature. Valid values:
        # 
        # *   **true** (default)
        # *   **false**\
        self.keepalive = keepalive  # type: bool
        # The number of reused persistent connections. Valid values: 60 to 1000.
        # 
        # > This parameter specifies the number of reused persistent connections after you enable the persistent connection feature.
        self.keepalive_requests = keepalive_requests  # type: int
        # The timeout period of persistent connections that are in the Idle state. Valid values: 1 to 60. Default value: 15. Unit: seconds.
        # 
        # > This parameter specifies the period of time during which a reused persistent connection is allowed to remain in the Idle state before the persistent connection is released.
        self.keepalive_timeout = keepalive_timeout  # type: int
        # The load balancing algorithm that you want WAF to use to forward requests to the origin server. Valid values:
        # 
        # *   **iphash**\
        # *   **roundRobin**\
        # *   **leastTime**. You can select this value only if you set **ProtectionResource** to **gslb**.
        self.loadbalance = loadbalance  # type: str
        # The read timeout period. Unit: seconds. Valid values: 1 to 3600.
        self.read_timeout = read_timeout  # type: int
        # The key-value pairs that you want to use to label the requests that pass through the WAF instance.
        # 
        # WAF automatically adds the key-value pairs to request headers. This way, the backend service can identify requests that pass through WAF.
        self.request_headers = request_headers  # type: list[CreateDomainRequestRedirectRequestHeaders]
        # Specifies whether WAF retries to forward requests when the requests fail to be forwarded to the origin server. Valid values:
        # 
        # *   **true** (default)
        # *   **false**\
        self.retry = retry  # type: bool
        # The forwarding rules that you want to configure for the domain name that you want to add to WAF in hybrid cloud mode. Set the value to a string that consists of JSON arrays. Each element in a JSON array is a JSON struct that contains the following fields:
        # 
        # *   **rs:** The back-to-origin IP addresses or CNAMEs. The value must be of the ARRAY type.
        # *   **location:** The name of the protection node. The value must be of the STRING type.
        # *   **locationId:** The ID of the protection node. The value must be of the LONG type.
        self.routing_rules = routing_rules  # type: str
        # Specifies whether to enable origin Server Name Indication (SNI). This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.sni_enabled = sni_enabled  # type: bool
        # The value of the SNI field. If you do not specify this parameter, the **Host** field value in the request header is used. If you want WAF to use an SNI field value that is different from the Host field value in back-to-origin requests, you can specify a custom value for the SNI field.
        # 
        # > You must specify this parameter only if you set **SniEnabled** to **true**.
        self.sni_host = sni_host  # type: str
        # The write timeout period. Unit: seconds. Valid values: 1 to 3600.
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
        if self.cname_enabled is not None:
            result['CnameEnabled'] = self.cname_enabled
        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout
        if self.focus_http_backend is not None:
            result['FocusHttpBackend'] = self.focus_http_backend
        if self.keepalive is not None:
            result['Keepalive'] = self.keepalive
        if self.keepalive_requests is not None:
            result['KeepaliveRequests'] = self.keepalive_requests
        if self.keepalive_timeout is not None:
            result['KeepaliveTimeout'] = self.keepalive_timeout
        if self.loadbalance is not None:
            result['Loadbalance'] = self.loadbalance
        if self.read_timeout is not None:
            result['ReadTimeout'] = self.read_timeout
        result['RequestHeaders'] = []
        if self.request_headers is not None:
            for k in self.request_headers:
                result['RequestHeaders'].append(k.to_map() if k else None)
        if self.retry is not None:
            result['Retry'] = self.retry
        if self.routing_rules is not None:
            result['RoutingRules'] = self.routing_rules
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
        if m.get('CnameEnabled') is not None:
            self.cname_enabled = m.get('CnameEnabled')
        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')
        if m.get('FocusHttpBackend') is not None:
            self.focus_http_backend = m.get('FocusHttpBackend')
        if m.get('Keepalive') is not None:
            self.keepalive = m.get('Keepalive')
        if m.get('KeepaliveRequests') is not None:
            self.keepalive_requests = m.get('KeepaliveRequests')
        if m.get('KeepaliveTimeout') is not None:
            self.keepalive_timeout = m.get('KeepaliveTimeout')
        if m.get('Loadbalance') is not None:
            self.loadbalance = m.get('Loadbalance')
        if m.get('ReadTimeout') is not None:
            self.read_timeout = m.get('ReadTimeout')
        self.request_headers = []
        if m.get('RequestHeaders') is not None:
            for k in m.get('RequestHeaders'):
                temp_model = CreateDomainRequestRedirectRequestHeaders()
                self.request_headers.append(temp_model.from_map(k))
        if m.get('Retry') is not None:
            self.retry = m.get('Retry')
        if m.get('RoutingRules') is not None:
            self.routing_rules = m.get('RoutingRules')
        if m.get('SniEnabled') is not None:
            self.sni_enabled = m.get('SniEnabled')
        if m.get('SniHost') is not None:
            self.sni_host = m.get('SniHost')
        if m.get('WriteTimeout') is not None:
            self.write_timeout = m.get('WriteTimeout')
        return self


class CreateDomainRequest(TeaModel):
    def __init__(self, access_type=None, domain=None, instance_id=None, listen=None, redirect=None, region_id=None,
                 resource_manager_resource_group_id=None, source_ip=None):
        # The mode in which you want to add the domain name to WAF. Valid values:
        # 
        # *   **share:** adds the domain name to WAF in CNAME record mode. This is the default value.
        # *   **hybrid_cloud_cname:** adds the domain name to WAF in hybrid cloud reverse proxy mode.
        self.access_type = access_type  # type: str
        # The domain name that you want to add to WAF.
        self.domain = domain  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # > You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The configurations of the listeners.
        self.listen = listen  # type: CreateDomainRequestListen
        # The configurations of the forwarding rule.
        self.redirect = redirect  # type: CreateDomainRequestRedirect
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou**: the Chinese mainland
        # *   **ap-southeast-1**: outside the Chinese mainland
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The source IP address of the request. You do not need to specify this parameter. It is automatically obtained by the system.
        self.source_ip = source_ip  # type: str

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
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
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
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class CreateDomainShrinkRequest(TeaModel):
    def __init__(self, access_type=None, domain=None, instance_id=None, listen_shrink=None, redirect_shrink=None,
                 region_id=None, resource_manager_resource_group_id=None, source_ip=None):
        # The mode in which you want to add the domain name to WAF. Valid values:
        # 
        # *   **share:** adds the domain name to WAF in CNAME record mode. This is the default value.
        # *   **hybrid_cloud_cname:** adds the domain name to WAF in hybrid cloud reverse proxy mode.
        self.access_type = access_type  # type: str
        # The domain name that you want to add to WAF.
        self.domain = domain  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # > You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The configurations of the listeners.
        self.listen_shrink = listen_shrink  # type: str
        # The configurations of the forwarding rule.
        self.redirect_shrink = redirect_shrink  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou**: the Chinese mainland
        # *   **ap-southeast-1**: outside the Chinese mainland
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The source IP address of the request. You do not need to specify this parameter. It is automatically obtained by the system.
        self.source_ip = source_ip  # type: str

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
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
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
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class CreateDomainResponseBodyDomainInfo(TeaModel):
    def __init__(self, cname=None, domain=None):
        # The CNAME that is assigned by WAF to the domain name.
        self.cname = cname  # type: str
        # The domain name that you added to WAF.
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
        # The information about the domain name.
        self.domain_info = domain_info  # type: CreateDomainResponseBodyDomainInfo
        # The ID of the request.
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
    def __init__(self, description=None, expired_time=None, instance_id=None, ip_list=None, region_id=None,
                 resource_manager_resource_group_id=None, rule_id=None, template_id=None):
        # The description of the IP address blacklist.
        self.description = description  # type: str
        # The time after which the IP address blacklist becomes invalid. Unit: seconds.
        # 
        # >  If you set the value to **0**, the blacklist is permanently valid.
        self.expired_time = expired_time  # type: long
        # The ID of the Web Application Firewall (WAF) instance.
        self.instance_id = instance_id  # type: str
        # The IP addresses that you want to add to the IP address blacklist. CIDR blocks and IP addresses are supported. IPv4 and IPv6 addresses are supported. Separate the CIDR blocks or IP addresses with commas (,). For more information, see [Protection for major events](~~425591~~).
        self.ip_list = ip_list  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The ID of the IP address blacklist rule for major event protection.
        self.rule_id = rule_id  # type: long
        # The ID of the major event protection template.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateMajorProtectionBlackIpResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, group_name=None, instance_id=None, region_id=None, resource_manager_resource_group_id=None):
        # The name of the protected object group that you want to delete.
        self.group_name = group_name  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        return self


class DeleteDefenseResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, instance_id=None, region_id=None, resource_manager_resource_group_id=None, rule_ids=None,
                 template_id=None):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The IDs of the protection rules that you want to delete. Separate the IDs with commas (,).
        self.rule_ids = rule_ids  # type: str
        # The ID of the protection rule template to which the protection rule that you want to delete belongs.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteDefenseRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, instance_id=None, region_id=None, resource_manager_resource_group_id=None, template_id=None):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The ID of the protection rule template that you want to delete.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteDefenseTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, access_type=None, domain=None, domain_id=None, instance_id=None, region_id=None,
                 source_ip=None):
        # The mode in which the domain name is added to WAF. Valid values:
        # 
        # *   **share:** CNAME record mode. This is the default value.
        # *   **hybrid_cloud_cname:** hybrid cloud reverse proxy mode.
        self.access_type = access_type  # type: str
        # The domain name that you want to delete.
        self.domain = domain  # type: str
        # The ID of the domain name.
        self.domain_id = domain_id  # type: str
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The source IP address of the request. The value of this parameter is specified by the system.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, instance_id=None, ip_list=None, region_id=None, resource_manager_resource_group_id=None,
                 rule_id=None, template_id=None):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The IP address blacklist for major event protection that you want to delete. You can specify multiple CIDR blocks or IP addresses. IPv4 and IPv6 addresses are supported. Separate the CIDR blocks or IP addresses with commas (,). For more information, see [Protection for major events](~~425591~~).
        self.ip_list = ip_list  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The ID of the IP address blacklist rule for major event protection.
        self.rule_id = rule_id  # type: long
        # The ID of the IP address blacklist rule template for major event protection.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteMajorProtectionBlackIpResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, group_name=None, instance_id=None, region_id=None, resource_manager_resource_group_id=None):
        # The name of the protected object group whose information you want to query.
        self.group_name = group_name  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        return self


class DescribeDefenseResourceGroupResponseBodyGroup(TeaModel):
    def __init__(self, description=None, gmt_create=None, gmt_modified=None, group_name=None, resource_list=None):
        # The description of the protected object group.
        self.description = description  # type: str
        # The time when the protected object group was created.
        self.gmt_create = gmt_create  # type: long
        # The most recent time when the protected object group was modified.
        self.gmt_modified = gmt_modified  # type: long
        # The name of the protected object group.
        self.group_name = group_name  # type: str
        # The protected objects in the protected object group. The protected objects are separated with commas (,).
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
        # The information about the protected object group.
        self.group = group  # type: DescribeDefenseResourceGroupResponseBodyGroup
        # The ID of the request.
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


class DescribeDefenseResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefenseResourcesRequestTag, self).to_map()
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


class DescribeDefenseResourcesRequest(TeaModel):
    def __init__(self, instance_id=None, page_number=None, page_size=None, query=None, region_id=None,
                 resource_manager_resource_group_id=None, source_ip=None, tag=None):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size  # type: int
        # The query conditions. Specify the value of this parameter as a string in the JSON format.
        # 
        # >  The results vary based on the query condition. For more information, see the "**Query parameters**" section in this topic.
        self.query = query  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The source IP address of the request. The value of this parameter is specified by the system.
        self.source_ip = source_ip  # type: str
        # The tags of the resources that you want to query. You can specify up to 20 tags.
        self.tag = tag  # type: list[DescribeDefenseResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDefenseResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDefenseResourcesResponseBodyResources(TeaModel):
    def __init__(self, acw_cookie_status=None, acw_secure_status=None, acw_v3secure_status=None,
                 custom_headers=None, description=None, detail=None, gmt_create=None, gmt_modified=None, pattern=None, product=None,
                 resource=None, resource_group=None, resource_manager_resource_group_id=None, resource_origin=None,
                 xff_status=None):
        # The status of the tracking cookie.
        # 
        # *   **0:** disabled.
        # *   **1:** enabled.
        self.acw_cookie_status = acw_cookie_status  # type: int
        # The status of the secure attribute of the tracking cookie.
        # 
        # *   **0:** disabled.
        # *   **1:** enabled.
        self.acw_secure_status = acw_secure_status  # type: int
        # The status of the secure attribute of the slider verification cookie.
        # 
        # *   **0:** disabled.
        # *   **1:** enabled.
        self.acw_v3secure_status = acw_v3secure_status  # type: int
        # The custom XFF headers that are used to identify the originating IP addresses of clients. If the value of XffStatus is 1 and CustomHeaders is left empty, the first IP address in the XFF header is the originating IP address of the client.
        self.custom_headers = custom_headers  # type: list[str]
        # The description of the protected object.
        self.description = description  # type: str
        # The details of the protected object. Different key-value pairs in a map indicate different properties of the protected object.
        self.detail = detail  # type: dict[str, any]
        # The creation time of the protected object. Unit: seconds.
        self.gmt_create = gmt_create  # type: long
        # The most recent modification time of the protected object. Unit: seconds.
        self.gmt_modified = gmt_modified  # type: long
        # The protection pattern.
        self.pattern = pattern  # type: str
        # The name of the cloud service.
        self.product = product  # type: str
        # The name of the protected object.
        self.resource = resource  # type: str
        # The name of the protected object group to which the protected object belongs.
        self.resource_group = resource_group  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The origin of the protected object.
        self.resource_origin = resource_origin  # type: str
        # Indicates whether the X-Forwarded-For (XFF) header is used.
        self.xff_status = xff_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefenseResourcesResponseBodyResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acw_cookie_status is not None:
            result['AcwCookieStatus'] = self.acw_cookie_status
        if self.acw_secure_status is not None:
            result['AcwSecureStatus'] = self.acw_secure_status
        if self.acw_v3secure_status is not None:
            result['AcwV3SecureStatus'] = self.acw_v3secure_status
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
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.resource_origin is not None:
            result['ResourceOrigin'] = self.resource_origin
        if self.xff_status is not None:
            result['XffStatus'] = self.xff_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcwCookieStatus') is not None:
            self.acw_cookie_status = m.get('AcwCookieStatus')
        if m.get('AcwSecureStatus') is not None:
            self.acw_secure_status = m.get('AcwSecureStatus')
        if m.get('AcwV3SecureStatus') is not None:
            self.acw_v3secure_status = m.get('AcwV3SecureStatus')
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
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('ResourceOrigin') is not None:
            self.resource_origin = m.get('ResourceOrigin')
        if m.get('XffStatus') is not None:
            self.xff_status = m.get('XffStatus')
        return self


class DescribeDefenseResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, resources=None, total_count=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The protected objects.
        self.resources = resources  # type: list[DescribeDefenseResourcesResponseBodyResources]
        # The total number of entries that are returned.
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
    def __init__(self, instance_id=None, region_id=None, resource_manager_resource_group_id=None, rule_id=None,
                 template_id=None):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The ID of the protection rule that you want to query.
        self.rule_id = rule_id  # type: long
        # The ID of the protection rule template to which the protection rule that you want to query belongs.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeDefenseRuleResponseBodyRule(TeaModel):
    def __init__(self, config=None, defense_origin=None, defense_scene=None, gmt_modified=None, rule_id=None,
                 rule_name=None, status=None, template_id=None):
        # The details of the protection rule. The value is a JSON string that contains multiple parameters. For more information, see the "**Protection rule parameters**" section of the [CreateDefenseRule](~~CreateDefenseRule~~) topic.
        self.config = config  # type: str
        # The origin of the protection rule. Valid values:
        # 
        # *   **custom:** The protection rule is created by the user.
        # *   **system:** The protection rule is automatically generated by the system.
        self.defense_origin = defense_origin  # type: str
        # The scenario in which the protection rule is used. For more information, see the description of **DefenseScene** in the [CreateDefenseRule](~~CreateDefenseRule~~) topic.
        self.defense_scene = defense_scene  # type: str
        # The most recent time when the protection rule was modified.
        self.gmt_modified = gmt_modified  # type: long
        # The ID of the protection rule.
        self.rule_id = rule_id  # type: long
        # The name of the protection rule.
        self.rule_name = rule_name  # type: str
        # The status of the protection rule. Valid values:
        # 
        # *   **0:** disabled.
        # *   **1:** enabled.
        self.status = status  # type: int
        # The ID of the protection rule template.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The configurations of the protection rule. The value is a JSON string that contains multiple parameters.
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
    def __init__(self, instance_id=None, page_number=None, page_size=None, query=None, region_id=None,
                 resource_manager_resource_group_id=None, rule_type=None):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size  # type: int
        # The query conditions. Specify a string that contains multiple parameters in the JSON format.
        # 
        # >  The results vary based on the query conditions. For more information, see the "**Query parameters**" section in this topic.
        self.query = query  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The type of protection rule that you want to query. Valid values:
        # 
        # *   **whitelist:** whitelist rule.
        # *   **defense:** defense rule. This is the default value.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class DescribeDefenseRulesResponseBodyRules(TeaModel):
    def __init__(self, config=None, defense_origin=None, defense_scene=None, gmt_modified=None, rule_id=None,
                 rule_name=None, status=None, template_id=None):
        # The details of the protection rule. The value is a string that contains multiple parameters in the JSON format. For more information, see the "**Rule parameters**" section in the [CreateDefenseRule](~~CreateDefenseRule~~) topic.
        self.config = config  # type: str
        # The origin of the protection rule. Valid values:
        # 
        # *   **custom:** The protection rule is created by the user.
        # *   **system:** The protection rule is automatically generated by the system.
        self.defense_origin = defense_origin  # type: str
        # The scenario in which the protection rule is used. For more information, see the description of the **DefenseScene** parameter in the [CreateDefenseRule](~~CreateDefenseRule~~) topic.
        self.defense_scene = defense_scene  # type: str
        # The most recent time when the protection rule was modified.
        self.gmt_modified = gmt_modified  # type: long
        # The ID of the protection rule.
        self.rule_id = rule_id  # type: long
        # The name of the protection rule.
        self.rule_name = rule_name  # type: str
        # The status of the protection rule. Valid values:
        # 
        # *   **0:** disabled.
        # *   **1:** enabled.
        self.status = status  # type: int
        # The ID of the protection rule template.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array of protection rules.
        self.rules = rules  # type: list[DescribeDefenseRulesResponseBodyRules]
        # The total number of returned entries.
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
    def __init__(self, instance_id=None, region_id=None, resource_manager_resource_group_id=None, template_id=None):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The ID of the protection rule template.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeDefenseTemplateResponseBodyTemplate(TeaModel):
    def __init__(self, defense_scene=None, defense_sub_scene=None, description=None, gmt_modified=None,
                 template_id=None, template_name=None, template_origin=None, template_status=None, template_type=None):
        # The scenario in which the template is used. For more information, see the description of the **DefenseScene** parameter in the [CreateDefenseRule](~~CreateDefenseRule~~) topic.
        self.defense_scene = defense_scene  # type: str
        self.defense_sub_scene = defense_sub_scene  # type: str
        # The description of the protection rule template.
        self.description = description  # type: str
        # The most recent time when the protection rule template was modified.
        self.gmt_modified = gmt_modified  # type: long
        # The ID of the protection rule template.
        self.template_id = template_id  # type: long
        # The name of the protection rule template.
        self.template_name = template_name  # type: str
        # The origin of the protection rule template. If the value of this parameter is custom, the protection rule template is created by the user.
        self.template_origin = template_origin  # type: str
        # The status of the protection rule template. Valid values:
        # 
        # *   **0:** disabled.
        # *   **1:** enabled.
        self.template_status = template_status  # type: int
        # The type of the protection rule template. Valid values:
        # 
        # *   **user_default:** default template.
        # *   **user_custom:** custom template.
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
        if self.defense_sub_scene is not None:
            result['DefenseSubScene'] = self.defense_sub_scene
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
        if m.get('DefenseSubScene') is not None:
            self.defense_sub_scene = m.get('DefenseSubScene')
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the template.
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
    def __init__(self, domain=None, instance_id=None, region_id=None, source_ip=None):
        # The domain name that you want to query.
        self.domain = domain  # type: str
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The source IP address of the request. The value of this parameter is specified by the system.
        self.source_ip = source_ip  # type: str

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeDomainDetailResponseBodyCertDetail(TeaModel):
    def __init__(self, common_name=None, end_time=None, id=None, name=None, sans=None, start_time=None):
        # The domain name of your website.
        self.common_name = common_name  # type: str
        # The end of the validity period of the SSL certificate. The value is in the UNIX timestamp format. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The ID of the SSL certificate.
        self.id = id  # type: str
        # The name of the SSL certificate.
        self.name = name  # type: str
        # All domain names that are bound to the certificate.
        self.sans = sans  # type: list[str]
        # The beginning of the validity period of the SSL certificate. The value is in the UNIX timestamp format. Unit: milliseconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainDetailResponseBodyCertDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainDetailResponseBodyListen(TeaModel):
    def __init__(self, cert_id=None, cipher_suite=None, custom_ciphers=None, enable_tlsv_3=None, exclusive_ip=None,
                 focus_https=None, http_2enabled=None, http_ports=None, https_ports=None, ipv_6enabled=None,
                 protection_resource=None, sm2access_only=None, sm2cert_id=None, sm2enabled=None, tlsversion=None, xff_header_mode=None,
                 xff_headers=None):
        # The ID of the certificate.
        self.cert_id = cert_id  # type: long
        # The type of the cipher suites. Valid values:
        # 
        # *   **1:** all cipher suites.
        # *   **2:** strong cipher suites.
        # *   **99:** custom cipher suites.
        self.cipher_suite = cipher_suite  # type: long
        # An array of custom cipher suites.
        self.custom_ciphers = custom_ciphers  # type: list[str]
        # Indicates whether TLS 1.3 is supported. Valid values:
        # 
        # *   **true:** TLS 1.3 is supported.
        # *   **false:** TLS 1.3 is not supported.
        self.enable_tlsv_3 = enable_tlsv_3  # type: bool
        # Indicates whether an exclusive IP address is enabled. Valid values:
        # 
        # *   **true:** An exclusive IP address is enabled for the domain name.
        # *   **false:** No exclusive IP addresses are enabled for the domain name.
        self.exclusive_ip = exclusive_ip  # type: bool
        # Indicates whether HTTP to HTTPS redirection is enabled for the domain name. Valid values:
        # 
        # *   **true:** HTTP to HTTPS redirection is enabled.
        # *   **false:** HTTP to HTTPS redirection is disabled.
        self.focus_https = focus_https  # type: bool
        # Indicates whether HTTP/2 is enabled. Valid values:
        # 
        # *   **true:** HTTP/2 is enabled.
        # *   **false:** HTTP/2 is disabled.
        self.http_2enabled = http_2enabled  # type: bool
        # An array of HTTP listener ports.
        self.http_ports = http_ports  # type: list[long]
        # An array of HTTPS listener ports.
        self.https_ports = https_ports  # type: list[long]
        # Indicates whether IPv6 is enabled. Valid values:
        # 
        # *   **true:** IPv6 is enabled.
        # *   **false:** IPv6 is disabled.
        self.ipv_6enabled = ipv_6enabled  # type: bool
        # The type of protection resource that is used. Valid values:
        # 
        # *   **share:** shared cluster.
        # *   **gslb:** shared cluster-based intelligent load balancing.
        self.protection_resource = protection_resource  # type: str
        self.sm2access_only = sm2access_only  # type: bool
        self.sm2cert_id = sm2cert_id  # type: bool
        self.sm2enabled = sm2enabled  # type: bool
        # The version of the Transport Layer Security (TLS) protocol. Valid values:
        # 
        # *   **tlsv1**\
        # *   **tlsv1.1**\
        # *   **tlsv1.2**\
        self.tlsversion = tlsversion  # type: str
        # The method that WAF uses to obtain the actual IP address of a client. Valid values:
        # 
        # *   **0:** No Layer 7 proxies are deployed in front of WAF.
        # *   **1:** WAF reads the first value of the X-Forwarded-For (XFF) header field as the actual IP address of the client.
        # *   **2:** WAF reads the value of a custom header field as the actual IP address of the client.
        self.xff_header_mode = xff_header_mode  # type: long
        # An array of custom header fields that are used to obtain the actual IP address of a client.
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
        if self.sm2access_only is not None:
            result['SM2AccessOnly'] = self.sm2access_only
        if self.sm2cert_id is not None:
            result['SM2CertId'] = self.sm2cert_id
        if self.sm2enabled is not None:
            result['SM2Enabled'] = self.sm2enabled
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
        if m.get('SM2AccessOnly') is not None:
            self.sm2access_only = m.get('SM2AccessOnly')
        if m.get('SM2CertId') is not None:
            self.sm2cert_id = m.get('SM2CertId')
        if m.get('SM2Enabled') is not None:
            self.sm2enabled = m.get('SM2Enabled')
        if m.get('TLSVersion') is not None:
            self.tlsversion = m.get('TLSVersion')
        if m.get('XffHeaderMode') is not None:
            self.xff_header_mode = m.get('XffHeaderMode')
        if m.get('XffHeaders') is not None:
            self.xff_headers = m.get('XffHeaders')
        return self


class DescribeDomainDetailResponseBodyRedirectBackends(TeaModel):
    def __init__(self, backend=None):
        # The IP address or domain name of the origin server.
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
        # The key of the custom header field.
        self.key = key  # type: str
        # The value of the custom header field.
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
    def __init__(self, backends=None, connect_timeout=None, focus_http_backend=None, keepalive=None,
                 keepalive_requests=None, keepalive_timeout=None, loadbalance=None, read_timeout=None, request_headers=None,
                 retry=None, sni_enabled=None, sni_host=None, write_timeout=None):
        # An array of addresses of origin servers.
        self.backends = backends  # type: list[DescribeDomainDetailResponseBodyRedirectBackends]
        # The timeout period of the connection. Unit: seconds. Valid values: 5 to 120.
        self.connect_timeout = connect_timeout  # type: int
        # Indicates whether HTTPS to HTTP redirection is enabled for back-to-origin requests of the domain name. Valid values:
        # 
        # *   **true:** HTTPS to HTTP redirection for back-to-origin requests of the domain name is enabled.
        # *   **false:** HTTPS to HTTP redirection for back-to-origin requests of the domain name is disabled.
        self.focus_http_backend = focus_http_backend  # type: bool
        # Indicates whether the persistent connection feature is enabled. Valid values:
        # 
        # *   **true:** The persistent connection feature is enabled. This is the default value.
        # *   **false:** The persistent connection feature is disabled.
        self.keepalive = keepalive  # type: bool
        # The number of reused persistent connections. Valid values: 60 to 1000.
        # 
        # >  This parameter specifies the number of reused persistent connections when you enable the persistent connection feature.
        self.keepalive_requests = keepalive_requests  # type: int
        # The timeout period of persistent connections that are in the Idle state. Valid values: 1 to 60. Default value: 15. Unit: seconds.
        # 
        # >  This parameter specifies the period of time during which a reused persistent connection is allowed to remain in the Idle state before the persistent connection is released.
        self.keepalive_timeout = keepalive_timeout  # type: int
        # The load balancing algorithm that is used when WAF forwards requests to the origin server. Valid values:
        # 
        # *   **ip_hash:** the IP hash algorithm.
        # *   **roundRobin:** the round-robin algorithm.
        # *   **leastTime:** the least response time algorithm.
        self.loadbalance = loadbalance  # type: str
        # The read timeout period. Unit: seconds. Valid values: 5 to 1800.
        self.read_timeout = read_timeout  # type: int
        # An array of key-value pairs that are used to mark the requests that pass through the WAF instance.
        self.request_headers = request_headers  # type: list[DescribeDomainDetailResponseBodyRedirectRequestHeaders]
        # Indicates whether WAF retries to forward requests when requests fail to be forwarded to the origin server. Valid values:
        # 
        # *   **true:** WAF retries to forward requests. This is the default value.
        # *   **false:** WAF does not retry to forward requests.
        self.retry = retry  # type: bool
        # Indicates whether origin Server Name Indication (SNI) is enabled. Valid values:
        # 
        # *   **true:** Origin SNI is enabled.
        # *   **false:** Origin SNI is disabled. This is the default value.
        self.sni_enabled = sni_enabled  # type: bool
        # The value of the custom SNI field.
        self.sni_host = sni_host  # type: str
        # The write timeout period. Unit: seconds. Valid values: 5 to 1800.
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
        if self.keepalive is not None:
            result['Keepalive'] = self.keepalive
        if self.keepalive_requests is not None:
            result['KeepaliveRequests'] = self.keepalive_requests
        if self.keepalive_timeout is not None:
            result['KeepaliveTimeout'] = self.keepalive_timeout
        if self.loadbalance is not None:
            result['Loadbalance'] = self.loadbalance
        if self.read_timeout is not None:
            result['ReadTimeout'] = self.read_timeout
        result['RequestHeaders'] = []
        if self.request_headers is not None:
            for k in self.request_headers:
                result['RequestHeaders'].append(k.to_map() if k else None)
        if self.retry is not None:
            result['Retry'] = self.retry
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
        if m.get('Keepalive') is not None:
            self.keepalive = m.get('Keepalive')
        if m.get('KeepaliveRequests') is not None:
            self.keepalive_requests = m.get('KeepaliveRequests')
        if m.get('KeepaliveTimeout') is not None:
            self.keepalive_timeout = m.get('KeepaliveTimeout')
        if m.get('Loadbalance') is not None:
            self.loadbalance = m.get('Loadbalance')
        if m.get('ReadTimeout') is not None:
            self.read_timeout = m.get('ReadTimeout')
        self.request_headers = []
        if m.get('RequestHeaders') is not None:
            for k in m.get('RequestHeaders'):
                temp_model = DescribeDomainDetailResponseBodyRedirectRequestHeaders()
                self.request_headers.append(temp_model.from_map(k))
        if m.get('Retry') is not None:
            self.retry = m.get('Retry')
        if m.get('SniEnabled') is not None:
            self.sni_enabled = m.get('SniEnabled')
        if m.get('SniHost') is not None:
            self.sni_host = m.get('SniHost')
        if m.get('WriteTimeout') is not None:
            self.write_timeout = m.get('WriteTimeout')
        return self


class DescribeDomainDetailResponseBodySM2CertDetail(TeaModel):
    def __init__(self, common_name=None, end_time=None, id=None, name=None, sans=None, start_time=None):
        # The domain name of your website.
        self.common_name = common_name  # type: str
        # The end of the validity period of the SSL certificate. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_time = end_time  # type: long
        # The ID of the SSL certificate.
        self.id = id  # type: str
        # The name of the SSL certificate.
        self.name = name  # type: str
        # All domain names that are bound to the certificate.
        self.sans = sans  # type: list[str]
        # The beginning of the validity period of the SSL certificate. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainDetailResponseBodySM2CertDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainDetailResponseBody(TeaModel):
    def __init__(self, cert_detail=None, cname=None, domain=None, listen=None, redirect=None, request_id=None,
                 resource_manager_resource_group_id=None, sm2cert_detail=None, status=None):
        # The details of the SSL certificate.
        self.cert_detail = cert_detail  # type: DescribeDomainDetailResponseBodyCertDetail
        # The CNAME that is assigned by WAF to the domain name.
        self.cname = cname  # type: str
        # The domain name.
        self.domain = domain  # type: str
        # The configurations of the listeners.
        self.listen = listen  # type: DescribeDomainDetailResponseBodyListen
        # The configurations of the forwarding rule.
        self.redirect = redirect  # type: DescribeDomainDetailResponseBodyRedirect
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The information about the SM certificate.
        self.sm2cert_detail = sm2cert_detail  # type: DescribeDomainDetailResponseBodySM2CertDetail
        # The status of the domain name. Valid values:
        # 
        # *   **1:** The domain name is in a normal state.
        # *   **2:** The domain name is being created.
        # *   **3:** The domain name is being modified.
        # *   **4:** The domain name is being released.
        # *   **5:** WAF no longer forwards traffic of the domain name.
        self.status = status  # type: long

    def validate(self):
        if self.cert_detail:
            self.cert_detail.validate()
        if self.listen:
            self.listen.validate()
        if self.redirect:
            self.redirect.validate()
        if self.sm2cert_detail:
            self.sm2cert_detail.validate()

    def to_map(self):
        _map = super(DescribeDomainDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_detail is not None:
            result['CertDetail'] = self.cert_detail.to_map()
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
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.sm2cert_detail is not None:
            result['SM2CertDetail'] = self.sm2cert_detail.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertDetail') is not None:
            temp_model = DescribeDomainDetailResponseBodyCertDetail()
            self.cert_detail = temp_model.from_map(m['CertDetail'])
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
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('SM2CertDetail') is not None:
            temp_model = DescribeDomainDetailResponseBodySM2CertDetail()
            self.sm2cert_detail = temp_model.from_map(m['SM2CertDetail'])
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


class DescribeDomainsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainsRequestTag, self).to_map()
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


class DescribeDomainsRequest(TeaModel):
    def __init__(self, backend=None, domain=None, instance_id=None, page_number=None, page_size=None, region_id=None,
                 resource_manager_resource_group_id=None, source_ip=None, tag=None):
        # An array of HTTPS listener ports.
        self.backend = backend  # type: str
        # The ID of the request.
        self.domain = domain  # type: str
        # The page number of the page to return. Default value: 1.
        self.instance_id = instance_id  # type: str
        # The HTTPS address of the origin server.
        self.page_number = page_number  # type: long
        # Queries the list of a domain name that is added to Web Application Firewall (WAF).
        self.page_size = page_size  # type: long
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The source IP address. The value of this parameter is specified by the system.
        self.source_ip = source_ip  # type: str
        # The tag of the resource. You can specify up to 20 tags.
        self.tag = tag  # type: list[DescribeDomainsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDomainsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDomainsResponseBodyDomainsBackedsHttp(TeaModel):
    def __init__(self, backend=None):
        # The HTTP address of the origin server.
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
        # The HTTPS address of the origin server.
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
        # The HTTP addresses of the origin server.
        self.http = http  # type: list[DescribeDomainsResponseBodyDomainsBackedsHttp]
        # The HTTPS addresses of the origin server.
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
        # The HTTP listener ports.
        self.http = http  # type: list[long]
        # The HTTPS listener ports.
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
    def __init__(self, backeds=None, cname=None, domain=None, listen_ports=None,
                 resource_manager_resource_group_id=None, status=None):
        # The back-to-origin settings.
        self.backeds = backeds  # type: DescribeDomainsResponseBodyDomainsBackeds
        # The CNAME assigned by WAF to the domain name.
        self.cname = cname  # type: str
        # The domain name that is added to WAF in CNAME record mode.
        self.domain = domain  # type: str
        # The configurations of the listeners.
        self.listen_ports = listen_ports  # type: DescribeDomainsResponseBodyDomainsListenPorts
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The status of the domain name. Valid values:
        # 
        # *   **1:** The domain name is in a normal state.
        # *   **2:** The domain name is being created.
        # *   **3:** The domain name is being modified.
        # *   **4:** The domain name is being released.
        # *   **5:** WAF no longer forwards traffic that is sent to the domain name.
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
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDomainsResponseBody(TeaModel):
    def __init__(self, domains=None, request_id=None, total_count=None):
        # The domain names that are added to WAF in CNAME record mode.
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
    def __init__(self, end_timestamp=None, instance_id=None, interval=None, region_id=None, resource=None,
                 resource_manager_resource_group_id=None, start_timestamp=None):
        # The end of the time range to query. Unit: seconds. If you do not specify this parameter, the current time is used.
        self.end_timestamp = end_timestamp  # type: str
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The time interval. Unit: seconds. The value must be an integral multiple of 60.
        self.interval = interval  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The protected object.
        self.resource = resource  # type: str
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The beginning of the time range to query. Unit: seconds.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeFlowChartResponseBodyFlowChart(TeaModel):
    def __init__(self, acl_custom_block_sum=None, acl_custom_reports_sum=None, anti_scan_block_sum=None,
                 antibot_block_sum=None, antibot_report_sum=None, antiscan_reports_sum=None, blacklist_block_sum=None,
                 blacklist_reports_sum=None, cc_custom_block_sum=None, cc_custom_reports_sum=None, cc_system_blocks_sum=None,
                 cc_system_reports_sum=None, count=None, in_bytes=None, index=None, max_pv=None, out_bytes=None, ratelimit_block_sum=None,
                 ratelimit_report_sum=None, region_block_blocks_sum=None, region_block_reports_sum=None, robot_count=None,
                 waf_block_sum=None, waf_report_sum=None):
        # The number of requests that are blocked by custom access control rules.
        self.acl_custom_block_sum = acl_custom_block_sum  # type: long
        # The number of requests that are monitored by custom access control rules.
        self.acl_custom_reports_sum = acl_custom_reports_sum  # type: long
        # The number of requests that are blocked by scan protection rules.
        self.anti_scan_block_sum = anti_scan_block_sum  # type: long
        # The number of requests that are blocked by bot management rules.
        self.antibot_block_sum = antibot_block_sum  # type: long
        # The number of requests that are monitored by bot management rules.
        self.antibot_report_sum = antibot_report_sum  # type: str
        # The number of requests that are monitored by scan protection rules.
        self.antiscan_reports_sum = antiscan_reports_sum  # type: long
        # The number of requests that are blocked by IP address blacklist rules.
        self.blacklist_block_sum = blacklist_block_sum  # type: str
        # The number of requests that are monitored by IP address blacklist rules.
        self.blacklist_reports_sum = blacklist_reports_sum  # type: long
        # The number of requests that are blocked by custom HTTP flood protection rules.
        self.cc_custom_block_sum = cc_custom_block_sum  # type: long
        # The number of requests that are monitored by custom HTTP flood protection rules.
        self.cc_custom_reports_sum = cc_custom_reports_sum  # type: long
        # The number of requests that are blocked by HTTP flood protection rules generated by the system.
        self.cc_system_blocks_sum = cc_system_blocks_sum  # type: long
        # The number of requests that are monitored by HTTP flood protection rules generated by the system.
        self.cc_system_reports_sum = cc_system_reports_sum  # type: long
        # The total number of requests.
        self.count = count  # type: long
        # The total number of requests that are forwarded to WAF.
        self.in_bytes = in_bytes  # type: long
        # The serial number of the time interval. The serial numbers are arranged in chronological order.
        self.index = index  # type: long
        # The maximum number of requests.
        self.max_pv = max_pv  # type: long
        # The total number of requests that are sent from WAF.
        self.out_bytes = out_bytes  # type: long
        self.ratelimit_block_sum = ratelimit_block_sum  # type: long
        self.ratelimit_report_sum = ratelimit_report_sum  # type: long
        # The number of requests that are blocked by region blacklist rules.
        self.region_block_blocks_sum = region_block_blocks_sum  # type: long
        # The number of requests that are monitored by region blacklist rules.
        self.region_block_reports_sum = region_block_reports_sum  # type: long
        self.robot_count = robot_count  # type: long
        # The number of requests that are blocked by basic protection rules.
        self.waf_block_sum = waf_block_sum  # type: long
        # The number of requests that are monitored by basic protection rules.
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
        if self.ratelimit_block_sum is not None:
            result['RatelimitBlockSum'] = self.ratelimit_block_sum
        if self.ratelimit_report_sum is not None:
            result['RatelimitReportSum'] = self.ratelimit_report_sum
        if self.region_block_blocks_sum is not None:
            result['RegionBlockBlocksSum'] = self.region_block_blocks_sum
        if self.region_block_reports_sum is not None:
            result['RegionBlockReportsSum'] = self.region_block_reports_sum
        if self.robot_count is not None:
            result['RobotCount'] = self.robot_count
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
        if m.get('RatelimitBlockSum') is not None:
            self.ratelimit_block_sum = m.get('RatelimitBlockSum')
        if m.get('RatelimitReportSum') is not None:
            self.ratelimit_report_sum = m.get('RatelimitReportSum')
        if m.get('RegionBlockBlocksSum') is not None:
            self.region_block_blocks_sum = m.get('RegionBlockBlocksSum')
        if m.get('RegionBlockReportsSum') is not None:
            self.region_block_reports_sum = m.get('RegionBlockReportsSum')
        if m.get('RobotCount') is not None:
            self.robot_count = m.get('RobotCount')
        if m.get('WafBlockSum') is not None:
            self.waf_block_sum = m.get('WafBlockSum')
        if m.get('WafReportSum') is not None:
            self.waf_report_sum = m.get('WafReportSum')
        return self


class DescribeFlowChartResponseBody(TeaModel):
    def __init__(self, flow_chart=None, request_id=None):
        # The traffic statistics.
        self.flow_chart = flow_chart  # type: list[DescribeFlowChartResponseBodyFlowChart]
        # The ID of the request.
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
    def __init__(self, end_timestamp=None, instance_id=None, region_id=None,
                 resource_manager_resource_group_id=None, start_timestamp=None):
        # The end of the time range to query. Unit: seconds. If you do not specify this parameter, the current time is used.
        self.end_timestamp = end_timestamp  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The beginning of the time range to query. Unit: seconds.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeFlowTopResourceResponseBodyRuleHitsTopResource(TeaModel):
    def __init__(self, count=None, resource=None):
        # The total number of requests received by the protected object in a specified time range.
        self.count = count  # type: long
        # The protected object.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The array of the top 10 protected objects that receive requests.
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
    def __init__(self, end_timestamp=None, instance_id=None, region_id=None, resource=None,
                 resource_manager_resource_group_id=None, start_timestamp=None):
        # The end of the time range to query. Unit: seconds. If you do not specify this parameter, the current time is used.
        self.end_timestamp = end_timestamp  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The protected object.
        self.resource = resource  # type: str
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The beginning of the time range to query. Unit: seconds.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeFlowTopUrlResponseBodyRuleHitsTopUrl(TeaModel):
    def __init__(self, count=None, url=None):
        # The total number of requests that are initiated by using the URL.
        self.count = count  # type: long
        # The URL that is used to initiate requests.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The array of the top 10 URLs that are used to initiate requests.
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


class DescribeHybridCloudGroupsRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_proxy_type=None, group_name=None, group_type=None, instance_id=None,
                 page_number=None, page_size=None, region_id=None, resource_manager_resource_group_id=None):
        # The ID of the hybrid cloud cluster.
        self.cluster_id = cluster_id  # type: long
        # The type of proxy cluster that is used. Valid values:
        # 
        # *   **service**: service-based traffic mirroring.
        # *   **cname**: reverse proxy.
        self.cluster_proxy_type = cluster_proxy_type  # type: str
        # The name of the hybrid cloud node group that you want to query.
        self.group_name = group_name  # type: int
        # The type of the node group. Valid values:
        # 
        # *   **protect**\
        # *   **control**\
        # *   **storage**\
        # *   **controlStorage**\
        self.group_type = group_type  # type: str
        # The ID of the WAF instance.
        # 
        # > You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The page number. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries per page. Default value: **10**.
        self.page_size = page_size  # type: int
        # The region ID of the WAF instance. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHybridCloudGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_proxy_type is not None:
            result['ClusterProxyType'] = self.cluster_proxy_type
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterProxyType') is not None:
            self.cluster_proxy_type = m.get('ClusterProxyType')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        return self


class DescribeHybridCloudGroupsResponseBodyGroups(TeaModel):
    def __init__(self, back_source_mark=None, continents_value=None, group_id=None, group_name=None,
                 group_type=None, load_balance_ip=None, location_id=None, operator_value=None, ports=None,
                 region_code_value=None, remark=None):
        self.back_source_mark = back_source_mark  # type: str
        self.continents_value = continents_value  # type: int
        # The ID of the hybrid cloud node group.
        self.group_id = group_id  # type: int
        # The name of the hybrid cloud node group.
        self.group_name = group_name  # type: str
        # The type of the hybrid cloud node group. Valid values:
        # 
        # *   **protect**\
        # *   **control**\
        # *   **storage**\
        # *   **controlStorage**\
        self.group_type = group_type  # type: str
        # The IP address of the server for load balancing.
        self.load_balance_ip = load_balance_ip  # type: str
        # The ID of the protection node.
        self.location_id = location_id  # type: long
        self.operator_value = operator_value  # type: int
        # The port that is used by the hybrid cloud cluster. The value of this parameter is a string. If multiple ports are returned, the value is in the **port1,port2,port3** format.
        self.ports = ports  # type: str
        self.region_code_value = region_code_value  # type: int
        # The description of the hybrid cloud node group.
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHybridCloudGroupsResponseBodyGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.back_source_mark is not None:
            result['BackSourceMark'] = self.back_source_mark
        if self.continents_value is not None:
            result['ContinentsValue'] = self.continents_value
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.load_balance_ip is not None:
            result['LoadBalanceIp'] = self.load_balance_ip
        if self.location_id is not None:
            result['LocationId'] = self.location_id
        if self.operator_value is not None:
            result['OperatorValue'] = self.operator_value
        if self.ports is not None:
            result['Ports'] = self.ports
        if self.region_code_value is not None:
            result['RegionCodeValue'] = self.region_code_value
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackSourceMark') is not None:
            self.back_source_mark = m.get('BackSourceMark')
        if m.get('ContinentsValue') is not None:
            self.continents_value = m.get('ContinentsValue')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('LoadBalanceIp') is not None:
            self.load_balance_ip = m.get('LoadBalanceIp')
        if m.get('LocationId') is not None:
            self.location_id = m.get('LocationId')
        if m.get('OperatorValue') is not None:
            self.operator_value = m.get('OperatorValue')
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        if m.get('RegionCodeValue') is not None:
            self.region_code_value = m.get('RegionCodeValue')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class DescribeHybridCloudGroupsResponseBody(TeaModel):
    def __init__(self, groups=None, request_id=None, total_count=None):
        # The hybrid cloud node groups.
        self.groups = groups  # type: list[DescribeHybridCloudGroupsResponseBodyGroups]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHybridCloudGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = DescribeHybridCloudGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeHybridCloudGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHybridCloudGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHybridCloudGroupsResponse, self).to_map()
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
            temp_model = DescribeHybridCloudGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHybridCloudResourcesRequest(TeaModel):
    def __init__(self, backend=None, cname_enabled=None, domain=None, instance_id=None, page_number=None,
                 page_size=None, region_id=None, resource_manager_resource_group_id=None, source_ip=None):
        # The back-to-origin IP address or domain name.
        self.backend = backend  # type: str
        # Specifies whether the public cloud disaster recovery feature is enabled for the domain name. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.cname_enabled = cname_enabled  # type: bool
        # The domain name that you want to query.
        self.domain = domain  # type: str
        # The ID of the WAF instance.
        # 
        # > You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The page number. Default value: **1**.
        self.page_number = page_number  # type: long
        # The number of entries per page. Default value: **10**.
        self.page_size = page_size  # type: long
        # The region ID of the WAF instance. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The source IP address of the request. The system specifies this parameter.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHybridCloudResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend is not None:
            result['Backend'] = self.backend
        if self.cname_enabled is not None:
            result['CnameEnabled'] = self.cname_enabled
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Backend') is not None:
            self.backend = m.get('Backend')
        if m.get('CnameEnabled') is not None:
            self.cname_enabled = m.get('CnameEnabled')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeHybridCloudResourcesResponseBodyDomainsListen(TeaModel):
    def __init__(self, cert_id=None, cipher_suite=None, custom_ciphers=None, enable_tlsv_3=None, exclusive_ip=None,
                 focus_https=None, http_2enabled=None, http_ports=None, https_ports=None, ipv_6enabled=None,
                 protection_resource=None, tlsversion=None, xff_header_mode=None, xff_headers=None):
        # The ID of the certificate.
        self.cert_id = cert_id  # type: str
        # The types of cipher suites that are added. Valid values:
        # 
        # *   **1:** all cipher suites.
        # *   **2:** strong cipher suites.
        # *   **99:** custom cipher suites.
        self.cipher_suite = cipher_suite  # type: int
        # The custom cipher suites.
        # 
        # > This parameter is returned only if the value of **CipherSuite** is **99**.
        self.custom_ciphers = custom_ciphers  # type: list[str]
        # Indicates whether TLS 1.3 is supported. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable_tlsv_3 = enable_tlsv_3  # type: bool
        # Indicates whether exclusive IP addresses are supported. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.exclusive_ip = exclusive_ip  # type: bool
        # Indicates whether the HTTP to HTTPS redirection feature is enabled for the domain name. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.focus_https = focus_https  # type: bool
        # Indicates whether HTTP/2 is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.http_2enabled = http_2enabled  # type: bool
        # The HTTP listener ports.
        self.http_ports = http_ports  # type: list[long]
        # The HTTPS listener ports.
        self.https_ports = https_ports  # type: list[long]
        # Indicates whether IPv6 is supported. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.ipv_6enabled = ipv_6enabled  # type: bool
        # The type of the protection resource. Valid values:
        # 
        # *   **share:** shared cluster.
        # *   **gslb:** shared cluster-based intelligent load balancing.
        self.protection_resource = protection_resource  # type: str
        # The version of the Transport Layer Security (TLS) protocol. Valid values:
        # 
        # *   **tlsv1**\
        # *   **tlsv1.1**\
        # *   **tlsv1.2**\
        self.tlsversion = tlsversion  # type: str
        # The method that is used to obtain the actual IP address of a client. Valid values:
        # 
        # *   **0:** No Layer 7 proxies are deployed in front of WAF.
        # *   **1:** WAF reads the first value of the X-Forwarded-For (XFF) header field as the actual IP address of the client.
        # *   **2:** WAF reads the value of a custom header field as the actual IP address of the client.
        self.xff_header_mode = xff_header_mode  # type: int
        # The custom header fields that are used to obtain the actual IP address of a client. The value is in the \["header1","header2",...] format.
        # 
        # > This parameter is returned only if the value of **XffHeaderMode** is 2.
        self.xff_headers = xff_headers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHybridCloudResourcesResponseBodyDomainsListen, self).to_map()
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
            result['Ipv6Enabled'] = self.ipv_6enabled
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
        if m.get('Ipv6Enabled') is not None:
            self.ipv_6enabled = m.get('Ipv6Enabled')
        if m.get('ProtectionResource') is not None:
            self.protection_resource = m.get('ProtectionResource')
        if m.get('TLSVersion') is not None:
            self.tlsversion = m.get('TLSVersion')
        if m.get('XffHeaderMode') is not None:
            self.xff_header_mode = m.get('XffHeaderMode')
        if m.get('XffHeaders') is not None:
            self.xff_headers = m.get('XffHeaders')
        return self


class DescribeHybridCloudResourcesResponseBodyDomainsRedirectRequestHeaders(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the custom header field.
        self.key = key  # type: str
        # The value of the custom header field.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHybridCloudResourcesResponseBodyDomainsRedirectRequestHeaders, self).to_map()
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


class DescribeHybridCloudResourcesResponseBodyDomainsRedirect(TeaModel):
    def __init__(self, backends=None, cname_enabled=None, connect_timeout=None, focus_http_backend=None,
                 keepalive=None, keepalive_requests=None, keepalive_timeout=None, loadbalance=None, read_timeout=None,
                 request_headers=None, retry=None, routing_rules=None, sni_enabled=None, sni_host=None, write_timeout=None):
        # The back-to-origin IP addresses or domain names.
        self.backends = backends  # type: list[str]
        # Indicates whether the public cloud disaster recovery feature is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.cname_enabled = cname_enabled  # type: bool
        # The connection timeout period. Unit: seconds. Valid values: 5 to 120.
        self.connect_timeout = connect_timeout  # type: long
        # Indicates whether the HTTPS to HTTP redirection feature is enabled for back-to-origin requests. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.focus_http_backend = focus_http_backend  # type: bool
        # Indicates whether the persistent connection feature is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.keepalive = keepalive  # type: bool
        # The number of reused persistent connections. Valid values: 60 to 1000.
        # 
        # > This parameter indicates the number of reused persistent connections after you enable the persistent connection feature.
        self.keepalive_requests = keepalive_requests  # type: long
        # The timeout period of persistent connections that are in the Idle state. Unit: seconds. Valid values: 1 to 60. Default value: 15.
        # 
        # > This parameter indicates the period of time during which a reused persistent connection is allowed to remain in the Idle state before the persistent connection is released.
        self.keepalive_timeout = keepalive_timeout  # type: long
        # The load balancing algorithm that WAF uses to forward requests to the origin server. Valid values:
        # 
        # *   **ip_hash**\
        # *   **roundRobin**\
        # *   **leastTime**\
        self.loadbalance = loadbalance  # type: str
        # The read timeout period. Unit: seconds. Valid values: 5 to 1800.
        self.read_timeout = read_timeout  # type: long
        # The key-value pair that is used to mark the requests that pass through the WAF instance.
        self.request_headers = request_headers  # type: list[DescribeHybridCloudResourcesResponseBodyDomainsRedirectRequestHeaders]
        # Indicates whether WAF retries to forward requests when requests fail to be forwarded to the origin server. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.retry = retry  # type: bool
        # The forwarding rules that you configured for the domain name that you added to WAF in hybrid cloud mode. The value is a string that consists of JSON arrays. Each element in a JSON array is a JSON struct that contains the following fields:
        # 
        # *   **rs:** The back-to-origin IP addresses or CNAMEs. The value is of the ARRAY type.
        # *   **location:** The name of the protection node. The value is of the STRING type.
        # *   **locationId:** The ID of the protection node. The value is of the LONG type.
        self.routing_rules = routing_rules  # type: str
        # Indicates whether the origin Server Name Indication (SNI) feature is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.sni_enabled = sni_enabled  # type: bool
        # The value of the custom Server Name Indication (SNI) field. If the parameter is left empty, the value of the **Host** field in the request header is automatically used as the value of the SNI field.
        # 
        # > This parameter is returned only if the value of **SniEnabled** is **true**.
        self.sni_host = sni_host  # type: str
        # The write timeout period. Unit: seconds. Valid values: 5 to 1800.
        self.write_timeout = write_timeout  # type: long

    def validate(self):
        if self.request_headers:
            for k in self.request_headers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHybridCloudResourcesResponseBodyDomainsRedirect, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backends is not None:
            result['Backends'] = self.backends
        if self.cname_enabled is not None:
            result['CnameEnabled'] = self.cname_enabled
        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout
        if self.focus_http_backend is not None:
            result['FocusHttpBackend'] = self.focus_http_backend
        if self.keepalive is not None:
            result['Keepalive'] = self.keepalive
        if self.keepalive_requests is not None:
            result['KeepaliveRequests'] = self.keepalive_requests
        if self.keepalive_timeout is not None:
            result['KeepaliveTimeout'] = self.keepalive_timeout
        if self.loadbalance is not None:
            result['Loadbalance'] = self.loadbalance
        if self.read_timeout is not None:
            result['ReadTimeout'] = self.read_timeout
        result['RequestHeaders'] = []
        if self.request_headers is not None:
            for k in self.request_headers:
                result['RequestHeaders'].append(k.to_map() if k else None)
        if self.retry is not None:
            result['Retry'] = self.retry
        if self.routing_rules is not None:
            result['RoutingRules'] = self.routing_rules
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
        if m.get('CnameEnabled') is not None:
            self.cname_enabled = m.get('CnameEnabled')
        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')
        if m.get('FocusHttpBackend') is not None:
            self.focus_http_backend = m.get('FocusHttpBackend')
        if m.get('Keepalive') is not None:
            self.keepalive = m.get('Keepalive')
        if m.get('KeepaliveRequests') is not None:
            self.keepalive_requests = m.get('KeepaliveRequests')
        if m.get('KeepaliveTimeout') is not None:
            self.keepalive_timeout = m.get('KeepaliveTimeout')
        if m.get('Loadbalance') is not None:
            self.loadbalance = m.get('Loadbalance')
        if m.get('ReadTimeout') is not None:
            self.read_timeout = m.get('ReadTimeout')
        self.request_headers = []
        if m.get('RequestHeaders') is not None:
            for k in m.get('RequestHeaders'):
                temp_model = DescribeHybridCloudResourcesResponseBodyDomainsRedirectRequestHeaders()
                self.request_headers.append(temp_model.from_map(k))
        if m.get('Retry') is not None:
            self.retry = m.get('Retry')
        if m.get('RoutingRules') is not None:
            self.routing_rules = m.get('RoutingRules')
        if m.get('SniEnabled') is not None:
            self.sni_enabled = m.get('SniEnabled')
        if m.get('SniHost') is not None:
            self.sni_host = m.get('SniHost')
        if m.get('WriteTimeout') is not None:
            self.write_timeout = m.get('WriteTimeout')
        return self


class DescribeHybridCloudResourcesResponseBodyDomains(TeaModel):
    def __init__(self, cname=None, domain=None, id=None, listen=None, redirect=None,
                 resource_manager_resource_group_id=None, status=None, uid=None):
        # The CNAME that is assigned by WAF to the domain name.
        # 
        # > This parameter is returned only if you set **CnameEnabled** to true.
        self.cname = cname  # type: str
        # The domain name.
        self.domain = domain  # type: str
        # The access ID.
        self.id = id  # type: long
        # The configurations of the listeners.
        self.listen = listen  # type: DescribeHybridCloudResourcesResponseBodyDomainsListen
        # The configurations of the forwarding rule.
        self.redirect = redirect  # type: DescribeHybridCloudResourcesResponseBodyDomainsRedirect
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The status of the domain name. Valid values:
        # 
        # *   **1:** The domain name is normal.
        # *   **2:** The domain name is being created.
        # *   **3:** The domain name is being modified.
        # *   **4:** The domain name is being released.
        # *   **5:** WAF no longer forwards traffic of the domain name.
        self.status = status  # type: int
        # The user ID.
        self.uid = uid  # type: str

    def validate(self):
        if self.listen:
            self.listen.validate()
        if self.redirect:
            self.redirect.validate()

    def to_map(self):
        _map = super(DescribeHybridCloudResourcesResponseBodyDomains, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.id is not None:
            result['Id'] = self.id
        if self.listen is not None:
            result['Listen'] = self.listen.to_map()
        if self.redirect is not None:
            result['Redirect'] = self.redirect.to_map()
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Listen') is not None:
            temp_model = DescribeHybridCloudResourcesResponseBodyDomainsListen()
            self.listen = temp_model.from_map(m['Listen'])
        if m.get('Redirect') is not None:
            temp_model = DescribeHybridCloudResourcesResponseBodyDomainsRedirect()
            self.redirect = temp_model.from_map(m['Redirect'])
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeHybridCloudResourcesResponseBody(TeaModel):
    def __init__(self, domains=None, request_id=None, total_count=None):
        # The domain names.
        self.domains = domains  # type: list[DescribeHybridCloudResourcesResponseBodyDomains]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries that are returned.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHybridCloudResourcesResponseBody, self).to_map()
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
                temp_model = DescribeHybridCloudResourcesResponseBodyDomains()
                self.domains.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeHybridCloudResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHybridCloudResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHybridCloudResourcesResponse, self).to_map()
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
            temp_model = DescribeHybridCloudResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHybridCloudUserRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, resource_manager_resource_group_id=None):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # > You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHybridCloudUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        return self


class DescribeHybridCloudUserResponseBodyUserInfo(TeaModel):
    def __init__(self, http_ports=None, https_ports=None):
        # The HTTP ports. The value is a string. If multiple ports are returned, the value is in the **port1,port2,port3** format.
        self.http_ports = http_ports  # type: str
        # The HTTPS ports. The value is a string. If multiple ports are returned, the value is in the **port1,port2,port3** format.
        self.https_ports = https_ports  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHybridCloudUserResponseBodyUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_ports is not None:
            result['HttpPorts'] = self.http_ports
        if self.https_ports is not None:
            result['HttpsPorts'] = self.https_ports
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpPorts') is not None:
            self.http_ports = m.get('HttpPorts')
        if m.get('HttpsPorts') is not None:
            self.https_ports = m.get('HttpsPorts')
        return self


class DescribeHybridCloudUserResponseBody(TeaModel):
    def __init__(self, request_id=None, user_info=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the ports that can be used by a hybrid cloud cluster.
        self.user_info = user_info  # type: DescribeHybridCloudUserResponseBodyUserInfo

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(DescribeHybridCloudUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserInfo') is not None:
            temp_model = DescribeHybridCloudUserResponseBodyUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class DescribeHybridCloudUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHybridCloudUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHybridCloudUserResponse, self).to_map()
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
            temp_model = DescribeHybridCloudUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(self, region_id=None, resource_manager_resource_group_id=None):
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
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
        # The maximum number of IP addresses that can be added to the match content of a match condition. For more information, see [Match conditions](~~374354~~).
        self.acl_rule_max_ip_count = acl_rule_max_ip_count  # type: long
        # Indicates whether the scan protection module is supported. Valid values:
        # 
        # *   **true:** The scan protection module is supported.
        # *   **false:** The scan protection module is not supported.
        self.anti_scan = anti_scan  # type: bool
        # The maximum number of scan protection rule templates that can be configured.
        self.anti_scan_template_max_count = anti_scan_template_max_count  # type: long
        # The maximum number of back-to-origin IP addresses that can be configured.
        self.backend_max_count = backend_max_count  # type: long
        # Indicates whether the basic protection rule module is supported. Valid values:
        # 
        # *   **true:** The basic protection rule module is supported.
        # *   **false:** The basic protection rule module is not supported.
        self.base_waf_group = base_waf_group  # type: bool
        # The maximum number of protection rules that can be included in a basic protection rule template.
        self.base_waf_group_rule_in_template_max_count = base_waf_group_rule_in_template_max_count  # type: long
        # The maximum number of basic protection rule templates that can be configured.
        self.base_waf_group_rule_template_max_count = base_waf_group_rule_template_max_count  # type: long
        # Indicates whether the bot management module is supported. Valid values:
        # 
        # *   **true:** The bot management module is supported.
        # *   **false:** The bot management module is not supported.
        self.bot = bot  # type: bool
        # Indicates whether bot management for app protection is supported. Valid values:
        # 
        # *   **true:** Bot management for app protection is supported.
        # *   **false:** Bot management for app protection is not supported.
        self.bot_app = bot_app  # type: str
        # The maximum number of bot management rule templates that can be configured.
        self.bot_template_max_count = bot_template_max_count  # type: long
        # Indicates whether bot management for website protection is supported. Valid values:
        # 
        # *   **true:** Bot management for website protection is supported.
        # *   **false:** Bot management for website protection is not supported.
        self.bot_web = bot_web  # type: str
        # The maximum number of CNAMEs that can be added.
        self.cname_resource_max_count = cname_resource_max_count  # type: long
        # Indicates whether the custom response module is supported. Valid values:
        # 
        # *   **true:** The custom response module is supported.
        # *   **false:** The custom response module is not supported.
        self.custom_response = custom_response  # type: bool
        # The maximum number of rules that can be included in a custom response rule template.
        self.custom_response_rule_in_template_max_count = custom_response_rule_in_template_max_count  # type: long
        # The maximum number of custom response rule templates that can be configured.
        self.custom_response_template_max_count = custom_response_template_max_count  # type: long
        # Indicates whether the custom rule module is supported. Valid values:
        # 
        # *   **true:** The custom rule module is supported.
        # *   **false:** The custom rule module is not supported.
        self.custom_rule = custom_rule  # type: bool
        # The action that can be included in a custom rule.
        self.custom_rule_action = custom_rule_action  # type: str
        # The match conditions that can be used in a custom rule. For more information, see **Match condition parameters** in the "**Parameters of custom rules (custom_acl)**" section in the [CreateDefenseRule](~~CreateDefenseRule~~) topic.
        self.custom_rule_condition = custom_rule_condition  # type: str
        # The maximum number of rules that can be included in a custom rule template.
        self.custom_rule_in_template_max_count = custom_rule_in_template_max_count  # type: long
        # The statistical object for rate limiting in a custom rule.
        self.custom_rule_ratelimitor = custom_rule_ratelimitor  # type: str
        # The maximum number of custom rule templates that can be configured.
        self.custom_rule_template_max_count = custom_rule_template_max_count  # type: long
        # The maximum number of protected object groups that can be configured.
        self.defense_group_max_count = defense_group_max_count  # type: long
        # The maximum number of protected objects that can be included in a protected object group.
        self.defense_object_in_group_max_count = defense_object_in_group_max_count  # type: long
        # The maximum number of protected objects to which a protection rule template can be applied.
        self.defense_object_in_template_max_count = defense_object_in_template_max_count  # type: long
        # The maximum number of protected objects that can be configured.
        self.defense_object_max_count = defense_object_max_count  # type: long
        # Indicates whether the data leakage prevention module is supported. Valid values:
        # 
        # *   **true:** The data leakage prevention module is supported.
        # *   **false:** The data leakage prevention module is not supported.
        self.dlp = dlp  # type: bool
        # The maximum number of rules that can be included in a data leakage prevention rule template.
        self.dlp_rule_in_template_max_count = dlp_rule_in_template_max_count  # type: long
        # The maximum number of data leakage prevention rule templates that can be configured.
        self.dlp_template_max_count = dlp_template_max_count  # type: long
        # Indicates whether exclusive IP addresses are supported. Valid values:
        # 
        # *   **true:** Exclusive IP addresses are supported.
        # *   **false:** Exclusive IP addresses are not supported.
        self.exclusive_ip = exclusive_ip  # type: bool
        # Indicates whether global server load balancing (GSLB) is supported. Valid values:
        # 
        # *   **true:** GSLB is supported.
        # *   **false:** GSLB is not supported.
        self.gslb = gslb  # type: bool
        # The HTTP port range that is supported. For more information, see [View supported ports](~~385578~~).
        self.http_ports = http_ports  # type: str
        # The HTTPS port range that is supported. For more information, see [View supported ports](~~385578~~).
        self.https_ports = https_ports  # type: str
        # Indicates whether the IP address blacklist module is supported. Valid values:
        # 
        # *   **true:** The IP address blacklist module is supported.
        # *   **false:** The IP address blacklist module is not supported.
        self.ip_blacklist = ip_blacklist  # type: bool
        # The maximum number of IP addresses that can be added to an IP address blacklist rule.
        self.ip_blacklist_ip_in_rule_max_count = ip_blacklist_ip_in_rule_max_count  # type: long
        # The maximum number of rules that can be included in an IP address blacklist rule template.
        self.ip_blacklist_rule_in_template_max_count = ip_blacklist_rule_in_template_max_count  # type: long
        # The maximum number of IP address blacklist rule templates that can be configured.
        self.ip_blacklist_template_max_count = ip_blacklist_template_max_count  # type: long
        # Indicates whether IPv6 is supported. Valid values:
        # 
        # *   **true:** IPv6 is supported.
        # *   **false:** IPv6 is not supported.
        self.ipv_6 = ipv_6  # type: bool
        # Indicates whether the log collection feature is supported. Valid values:
        # 
        # *   **true:** The log collection feature is supported.
        # *   **false:** The log collection feature is not supported.
        self.log_service = log_service  # type: bool
        # Indicates whether major event protection is supported. Valid values:
        # 
        # *   **true:** Major event protection is supported.
        # *   **false:** Major event protection is not supported.
        self.major_protection = major_protection  # type: bool
        # The maximum number of major event protection rule templates that can be configured.
        self.major_protection_template_max_count = major_protection_template_max_count  # type: long
        # Indicates whether the website tamper-proofing module is supported. Valid values:
        # 
        # *   **true:** The website tamper-proofing module is supported.
        # *   **false:** The website tamper-proofing module is not supported.
        self.tamperproof = tamperproof  # type: bool
        # The maximum number of rules that can be included in a website tamper-proofing rule template.
        self.tamperproof_rule_in_template_max_count = tamperproof_rule_in_template_max_count  # type: long
        # The maximum number of website tamper-proofing rule templates that can be configured.
        self.tamperproof_template_max_count = tamperproof_template_max_count  # type: long
        # The maximum number of IP addresses or CIDR blocks that can be added to an IP address blacklist in a batch.
        self.vast_ip_blacklist_in_file_max_count = vast_ip_blacklist_in_file_max_count  # type: long
        # The maximum number of IP addresses or CIDR blocks that can be added to an IP address blacklist on a page.
        self.vast_ip_blacklist_in_operation_max_count = vast_ip_blacklist_in_operation_max_count  # type: long
        # The maximum number of IP addresses or CIDR blocks that can be added to an IP address blacklist per Alibaba Cloud account.
        self.vast_ip_blacklist_max_count = vast_ip_blacklist_max_count  # type: long
        # Indicates whether the whitelist module is supported. Valid values:
        # 
        # *   **true:** The whitelist module is supported.
        # *   **false:** The whitelist module is not supported.
        self.whitelist = whitelist  # type: bool
        # The logical operators that can be used in a whitelist rule. For more information, see **Match condition parameters** in the "**Parameters of whitelist rules (whitelist)**" section in the [CreateDefenseRule](~~CreateDefenseRule~~) topic.
        self.whitelist_logical = whitelist_logical  # type: str
        # The match fields that can be used in a whitelist rule. For more information, see **Match condition parameters** in the "**Parameters of whitelist rules (whitelist)**" section in the [CreateDefenseRule](~~CreateDefenseRule~~) topic.
        self.whitelist_rule_condition = whitelist_rule_condition  # type: str
        # The maximum number of rules that can be included in a whitelist rule template.
        self.whitelist_rule_in_template_max_count = whitelist_rule_in_template_max_count  # type: long
        # The maximum number of whitelist rule templates that can be configured.
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
        # The details of the WAF instance.
        self.details = details  # type: DescribeInstanceResponseBodyDetails
        # The edition of the WAF instance.
        self.edition = edition  # type: str
        # The expiration time of the WAF instance.
        self.end_time = end_time  # type: long
        # Indicates whether the WAF instance has overdue payments. Valid values:
        # 
        # *   **0**: The WAF instance does not have overdue payments.
        # *   **1**: The WAF instance has overdue payments.
        self.in_debt = in_debt  # type: str
        # The ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The billing method of the WAF instance. Valid values:
        # 
        # *   **POSTPAY:** The WAF instance uses the pay-as-you-go billing method.
        # *   **PREPAY:** The WAF instance uses the subscription billing method.
        self.pay_type = pay_type  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The purchase time of the WAF instance. The time is in the UNIX timestamp format. The time is displayed in UTC. Unit: milliseconds.
        self.start_time = start_time  # type: long
        # The status of the WAF instance. Valid values:
        # 
        # *   **1:** The WAF instance is in a normal state.
        # *   **2:** The WAF instance has expired.
        # *   **3:** The WAF instance has been released.
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
    def __init__(self, instance_id=None, ip_like=None, order_by=None, page_number=None, page_size=None,
                 region_id=None, resource_manager_resource_group_id=None, rule_id=None, template_id=None):
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The IP address that you want to query. You can specify this parameter to query an IP address in the IP address blacklist for major event protection by using fuzzy matching.
        self.ip_like = ip_like  # type: str
        # The method that you want to use to sort the IP addresses **in descending order**. Valid values:
        # 
        # *   **gmtModified:** sorts the IP addresses by most recent modification time.
        # *   **ip:** sorts the IP addresses by IP address.
        # *   **templateId:** sorts the IP addresses by template ID.
        # *   **id:** sorts the IP addresses by primary key.
        self.order_by = order_by  # type: str
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size  # type: int
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The ID of the IP address blacklist rule for major event protection.
        self.rule_id = rule_id  # type: long
        # The ID of the rule template for major event protection.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeMajorProtectionBlackIpsResponseBodyIpList(TeaModel):
    def __init__(self, description=None, expired_time=None, gmt_modified=None, ip=None, rule_id=None,
                 template_id=None):
        # The description of the IP address in the blacklist.
        self.description = description  # type: str
        # The time after which the IP address blacklist becomes invalid. Unit: seconds.
        # 
        # >  If the value of this parameter is **0**, the blacklist is permanently valid.
        self.expired_time = expired_time  # type: long
        # The most recent time when the IP address blacklist was modified.
        self.gmt_modified = gmt_modified  # type: long
        # The IP address in the IP address blacklist.
        self.ip = ip  # type: str
        # The ID of the IP address blacklist rule for major event protection.
        self.rule_id = rule_id  # type: long
        # The ID of the rule template for major event protection.
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
        # An array of IP addresses in the IP address blacklist.
        self.ip_list = ip_list  # type: list[DescribeMajorProtectionBlackIpsResponseBodyIpList]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of IP addresses in the blacklist.
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
    def __init__(self, end_timestamp=None, instance_id=None, interval=None, region_id=None, resource=None,
                 resource_manager_resource_group_id=None, start_timestamp=None):
        # The end of the time range to query. Unit: seconds. If you do not specify this parameter, the current time is used.
        self.end_timestamp = end_timestamp  # type: str
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The time interval. Unit: seconds. The value must be an integral multiple of 60.
        self.interval = interval  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The protected object.
        self.resource = resource  # type: str
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The beginning of the time range to query. Unit: seconds.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribePeakTrendResponseBodyFlowChart(TeaModel):
    def __init__(self, acl_sum=None, anti_scan_sum=None, cc_sum=None, count=None, index=None, waf_sum=None):
        # The number of requests that are monitored or blocked by the custom rule (access control) module.
        self.acl_sum = acl_sum  # type: long
        # The number of requests that are monitored or blocked by the scan protection module.
        self.anti_scan_sum = anti_scan_sum  # type: long
        # The number of requests that are monitored or blocked by the HTTP flood protection module.
        self.cc_sum = cc_sum  # type: long
        # The total number of requests.
        self.count = count  # type: long
        # The serial number of the time interval. The serial numbers are arranged in chronological order.
        self.index = index  # type: long
        # The number of requests that are monitored or blocked by the regular expression protection engine.
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
        # An array of the QPS statistics of the WAF instance.
        self.flow_chart = flow_chart  # type: list[DescribePeakTrendResponseBodyFlowChart]
        # The ID of the request.
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
    def __init__(self, instance_id=None, region_id=None, resource_manager_resource_group_id=None, resources=None):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The protected object that you want to query. You can specify multiple protected objects. Separate the protected objects with commas (,).
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class DescribeResourceLogStatusResponseBodyResult(TeaModel):
    def __init__(self, resource=None, status=None):
        # The protected object.
        self.resource = resource  # type: str
        # Indicates whether the log collection feature is enabled for the protected object. Valid values:
        # 
        # *   **true:** The log collection feature is enabled.
        # *   **false:** The log collection feature is disabled.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The returned result.
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
    def __init__(self, instance_id=None, region_id=None, resource_instance_id=None,
                 resource_manager_resource_group_id=None):
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the cloud service instance.
        self.resource_instance_id = resource_instance_id  # type: str
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeResourcePortRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        return self


class DescribeResourcePortResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_ports=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array of HTTP and HTTPS listener ports that are added to the WAF instance.
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
    def __init__(self, end_timestamp=None, instance_id=None, interval=None, region_id=None, resource=None,
                 resource_manager_resource_group_id=None, start_timestamp=None, type=None):
        # The end of the time range to query. Unit: seconds. If you do not specify this parameter, the current time is used.
        self.end_timestamp = end_timestamp  # type: str
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The time interval. Unit: seconds. The value must be an integral multiple of 60.
        self.interval = interval  # type: str
        # The ID of the region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The protected object.
        self.resource = resource  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The beginning of the time range to query. Unit: seconds.
        self.start_timestamp = start_timestamp  # type: str
        # The type of the error codes. Valid values:
        # 
        # *   **waf:** error codes that are returned to clients from WAF.
        # *   **upstream:** error codes that are returned to WAF from the origin server.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeResponseCodeTrendGraphResponseBodyResponseCodes(TeaModel):
    def __init__(self, code_302pv=None, code_405pv=None, code_499pv=None, code_5xx_pv=None, index=None):
        # The number of 302 error codes that are returned.
        self.code_302pv = code_302pv  # type: long
        # The number of 405 error codes that are returned.
        self.code_405pv = code_405pv  # type: long
        # The number of 499 error codes that are returned.
        self.code_499pv = code_499pv  # type: long
        # The number of 5xx error codes that are returned.
        self.code_5xx_pv = code_5xx_pv  # type: long
        # The serial number of the time interval. The serial numbers are arranged in chronological order.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The array of the statistics of the error codes.
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
    def __init__(self, instance_id=None, page_number=None, page_size=None, region_id=None,
                 resource_manager_resource_group_id=None, search_type=None, search_value=None):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size  # type: int
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The type of the query condition. Valid values:
        # 
        # *   **id:** queries regular expression rule groups by ID.
        # *   **name:** queries regular expression rule groups by name.
        self.search_type = search_type  # type: str
        # The query condition.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        return self


class DescribeRuleGroupsResponseBodyRuleGroups(TeaModel):
    def __init__(self, gmt_modified=None, is_subscribe=None, parent_rule_group_id=None, rule_group_id=None,
                 rule_group_name=None, rule_total_count=None):
        # The most recent time when the rule group was modified.
        self.gmt_modified = gmt_modified  # type: long
        # Indicates whether the automatic update feature is enabled for the rule group.
        # 
        # *   1: The automatic update feature is enabled for the rule group.
        # *   2: The automatic update feature is disabled for the rule group.
        self.is_subscribe = is_subscribe  # type: int
        # The ID of the rule group.
        # 
        # *   0: The rule group is created from scratch.
        # *   1011: The rule group is a strict rule group.
        # *   1012: The rule group is a medium rule group.
        # *   1013: The rue group is a loose rule group.
        self.parent_rule_group_id = parent_rule_group_id  # type: long
        # The ID of the regular expression rule group.
        self.rule_group_id = rule_group_id  # type: long
        # The name of the rule group.
        self.rule_group_name = rule_group_name  # type: str
        # The number of built-in rules in the rule group.
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
        if self.is_subscribe is not None:
            result['IsSubscribe'] = self.is_subscribe
        if self.parent_rule_group_id is not None:
            result['ParentRuleGroupId'] = self.parent_rule_group_id
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
        if m.get('IsSubscribe') is not None:
            self.is_subscribe = m.get('IsSubscribe')
        if m.get('ParentRuleGroupId') is not None:
            self.parent_rule_group_id = m.get('ParentRuleGroupId')
        if m.get('RuleGroupId') is not None:
            self.rule_group_id = m.get('RuleGroupId')
        if m.get('RuleGroupName') is not None:
            self.rule_group_name = m.get('RuleGroupName')
        if m.get('RuleTotalCount') is not None:
            self.rule_total_count = m.get('RuleTotalCount')
        return self


class DescribeRuleGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, rule_groups=None, total_count=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array of regular expression rule groups.
        self.rule_groups = rule_groups  # type: list[DescribeRuleGroupsResponseBodyRuleGroups]
        # The total number of entries that are returned.
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
    def __init__(self, end_timestamp=None, instance_id=None, region_id=None, resource=None,
                 resource_manager_resource_group_id=None, rule_type=None, start_timestamp=None):
        # The end of the time range to query. Unit: seconds. If you do not specify this parameter, the current time is used.
        self.end_timestamp = end_timestamp  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The protected object.
        self.resource = resource  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The type of rules that are triggered by the protected object. By default, this parameter is not specified and all types of rules are queried.
        # 
        # *   **blacklist:** IP address blacklist rules.
        # *   **custom:** custom rules.
        # *   **antiscan:** scan protection rules.
        # *   **cc_system:** HTTP flood protection rules.
        # *   **region_block:** region blacklist rules.
        self.rule_type = rule_type  # type: str
        # The beginning of the time range to query. Unit: seconds.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeRuleHitsTopClientIpResponseBodyRuleHitsTopClientIp(TeaModel):
    def __init__(self, client_ip=None, count=None):
        # The IP address of the service client.
        self.client_ip = client_ip  # type: str
        # The number of attacks that are initiated from the IP address.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The array of the top 10 IP addresses from which attacks are initiated.
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
    def __init__(self, end_timestamp=None, instance_id=None, region_id=None,
                 resource_manager_resource_group_id=None, rule_type=None, start_timestamp=None):
        # The end of the time range to query. Unit: seconds. If you do not specify this parameter, the current time is used.
        self.end_timestamp = end_timestamp  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The type of rules that are triggered by the protected object. By default, this parameter is not specified and all types of rules are queried.
        # 
        # *   **blacklist:** IP address blacklist rules.
        # *   **custom:** custom rules.
        # *   **antiscan:** scan protection rules.
        # *   **cc_system:** HTTP flood protection rules.
        # *   **region_block:** region blacklist rules.
        self.rule_type = rule_type  # type: str
        # The beginning of the time range to query. Unit: seconds.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeRuleHitsTopResourceResponseBodyRuleHitsTopResource(TeaModel):
    def __init__(self, count=None, resource=None):
        # The number of requests that match protection rules.
        self.count = count  # type: long
        # The protected object.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The array of the top 10 protected objects that trigger protection rules.
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
    def __init__(self, end_timestamp=None, instance_id=None, is_group_resource=None, region_id=None, resource=None,
                 resource_manager_resource_group_id=None, rule_type=None, start_timestamp=None):
        # The end of the time range to query. Unit: seconds. If you do not specify this parameter, the current time is used.
        self.end_timestamp = end_timestamp  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to query the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        self.is_group_resource = is_group_resource  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The protected object.
        self.resource = resource  # type: str
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The type of rules that are triggered by the protected object. By default, this parameter is not specified and all types of rules are queried.
        # 
        # *   **blacklist:** IP address blacklist rules.
        # *   **custom:** custom rules.
        # *   **antiscan:** scan protection rules.
        # *   **cc_system:** HTTP flood protection rules.
        # *   **region_block:** region blacklist rules.
        self.rule_type = rule_type  # type: str
        # The beginning of the time range to query. Unit: seconds.
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
        if self.is_group_resource is not None:
            result['IsGroupResource'] = self.is_group_resource
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('IsGroupResource') is not None:
            self.is_group_resource = m.get('IsGroupResource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeRuleHitsTopRuleIdResponseBodyRuleHitsTopRuleId(TeaModel):
    def __init__(self, count=None, resource=None, rule_id=None):
        # The number of requests that match the rule.
        self.count = count  # type: long
        # The protected object.
        self.resource = resource  # type: str
        # The ID of the rule.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The array of the IDs of the top 10 rules that are matched by requests.
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
    def __init__(self, end_timestamp=None, instance_id=None, region_id=None, resource=None, start_timestamp=None):
        # The end point of the time period for which to query. Unit: seconds. If you do not specify this parameter, the current time is used.
        self.end_timestamp = end_timestamp  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to query the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The ID of the region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou**: the Chinese mainland.
        # *   **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The protected object.
        self.resource = resource  # type: str
        # The start point of the time period for which to query. Unit: seconds.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeRuleHitsTopTuleTypeResponseBodyRuleHitsTopTuleType(TeaModel):
    def __init__(self, count=None, rule_type=None):
        # The number of requests that match protection rules.
        self.count = count  # type: long
        # The type of rule that is matched. By default, this parameter is not returned. This indicates that all types of rules that are matched are returned.
        # 
        # *   **waf:** basic protection rules.
        # *   **blacklist:** IP address blacklist rules.
        # *   **custom:** custom rules.
        # *   **antiscan:** scan protection rules.
        # *   **cc_system:** HTTP flood protection rules.
        # *   **region_block:** region blacklist rules.
        # *   **scene:** bot management rules.
        # *   **dlp:** data leakage prevention rules.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The top 10 protection modules that are matched.
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
    def __init__(self, end_timestamp=None, instance_id=None, region_id=None, resource=None,
                 resource_manager_resource_group_id=None, start_timestamp=None):
        # The end of the time range to query. Unit: seconds. If you do not specify this parameter, the current time is used.
        self.end_timestamp = end_timestamp  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The protected object.
        self.resource = resource  # type: str
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The beginning of the time range to query. Unit: seconds.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeRuleHitsTopUaResponseBodyRuleHitsTopUa(TeaModel):
    def __init__(self, count=None, ua=None):
        # The number of attacks that are initiated from the IP address.
        self.count = count  # type: long
        # The user agent.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The array of the top 10 user agents that are used to initiate attacks.
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
    def __init__(self, end_timestamp=None, instance_id=None, region_id=None, resource=None,
                 resource_manager_resource_group_id=None, rule_type=None, start_timestamp=None):
        # The end of the time range to query. Unit: seconds. If you do not specify this parameter, the current time is used.
        self.end_timestamp = end_timestamp  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The protected object.
        self.resource = resource  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The type of rules that are triggered by the protected object. By default, this parameter is not specified and all types of rules are queried.
        # 
        # *   **blacklist:** IP address blacklist rules.
        # *   **custom:** custom rules.
        # *   **antiscan:** scan protection rules.
        # *   **cc_system:** HTTP flood protection rules.
        # *   **region_block:** region blacklist rules.
        self.rule_type = rule_type  # type: str
        # The beginning of the time range to query. Unit: seconds.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeRuleHitsTopUrlResponseBodyRuleHitsTopUrl(TeaModel):
    def __init__(self, count=None, url=None):
        # The number of requests from the URL that match protection rules.
        self.count = count  # type: long
        # The request URL.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The array of the top 10 URLs that trigger protection rules.
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
    def __init__(self, instance_id=None, region_id=None, resource_manager_resource_group_id=None,
                 resource_type=None, template_id=None):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The type of the protected resource. Valid values:
        # 
        # *   **single:** protected object.
        # *   **group:** protected object group.
        self.resource_type = resource_type  # type: str
        # The ID of the protection rule template.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeTemplateResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, resources=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array of protected objects or protected object groups that are associated to the protection rule template.
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
    def __init__(self, end_timestamp=None, instance_id=None, region_id=None, resource=None,
                 resource_manager_resource_group_id=None, start_timestamp=None):
        # The end of the time range to query. Unit: seconds. If you do not specify this parameter, the current time is used.
        self.end_timestamp = end_timestamp  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The protected object.
        self.resource = resource  # type: str
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The beginning of the time range to query. Unit: seconds.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeVisitTopIpResponseBodyTopIp(TeaModel):
    def __init__(self, area=None, count=None, ip=None, isp=None):
        # The ordinal number of the area to which the IP address belongs.
        self.area = area  # type: str
        # The total number of requests that are sent from the IP address.
        self.count = count  # type: long
        # The IP address.
        self.ip = ip  # type: str
        # The ISP.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The array of the top 10 IP addresses from which requests are sent.
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
    def __init__(self, end_timestamp=None, instance_id=None, region_id=None, resource=None, start_timestamp=None):
        # The end of the time range to query. Unit: seconds. If you do not specify this parameter, the current time is used.
        self.end_timestamp = end_timestamp  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        # The protected object.
        self.resource = resource  # type: str
        # The beginning of the time range to query. Unit: seconds.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeVisitUasResponseBodyUas(TeaModel):
    def __init__(self, count=None, ua=None):
        # The number of requests that use the user agent.
        self.count = count  # type: long
        # The user agent.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The array of the top 10 user agents that are used to initiate requests.
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
    def __init__(self, instance_id=None, region_id=None, resource_manager_resource_group_id=None):
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWafSourceIpSegmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        return self


class DescribeWafSourceIpSegmentResponseBodyWafSourceIp(TeaModel):
    def __init__(self, ipv_4=None, ipv_6=None):
        # An array of back-to-origin IPv4 CIDR blocks.
        self.ipv_4 = ipv_4  # type: list[str]
        # An array of back-to-origin IPv6 CIDR blocks.
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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The back-to-origin CIDR blocks that are used by the protection cluster.
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
    def __init__(self, add_list=None, delete_list=None, description=None, group_name=None, instance_id=None,
                 region_id=None, resource_manager_resource_group_id=None):
        # The protected objects that you want to add to the protected object group. Separate the protected objects with commas (,). If you leave this parameter empty, no protected objects are added to the protected object group.
        self.add_list = add_list  # type: str
        # The protected objects that you want to remove from the protected object group. Separate the protected objects with commas (,). If you leave this parameter empty, no protected objects are removed from the protected object group.
        self.delete_list = delete_list  # type: str
        # The description of the protected object group.
        self.description = description  # type: str
        # The name of the protected object group whose configurations you want to modify.
        self.group_name = group_name  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        return self


class ModifyDefenseResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, defense_scene=None, instance_id=None, region_id=None,
                 resource_manager_resource_group_id=None, rules=None, template_id=None):
        self.defense_scene = defense_scene  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
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
    def __init__(self, instance_id=None, region_id=None, resource_manager_resource_group_id=None, rule_id=None,
                 rule_status=None, template_id=None):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The ID of the protection rule whose status you want to change.
        self.rule_id = rule_id  # type: long
        # The new status of the protection rule. Valid values:
        # 
        # *   **0:** disabled.
        # *   **1:** enabled.
        self.rule_status = rule_status  # type: int
        # The ID of the protection rule template to which the protection rule whose status you want to change belongs.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ModifyDefenseRuleStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, description=None, instance_id=None, region_id=None, resource_manager_resource_group_id=None,
                 template_id=None, template_name=None):
        # The description of the protection rule template whose configurations you want to modify.
        self.description = description  # type: str
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The ID of the protection rule template whose configurations you want to modify.
        self.template_id = template_id  # type: long
        # The name of the protection rule template whose configurations you want to modify.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ModifyDefenseTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, instance_id=None, region_id=None, resource_manager_resource_group_id=None, template_id=None,
                 template_status=None):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The ID of the protection rule template whose status you want to change.
        self.template_id = template_id  # type: long
        # The new status of the protection rule template. Valid values:
        # 
        # *   **0:** disabled.
        # *   **1:** enabled.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')
        return self


class ModifyDefenseTemplateStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
                 protection_resource=None, sm2access_only=None, sm2cert_id=None, sm2enabled=None, tlsversion=None, xff_header_mode=None,
                 xff_headers=None):
        # The ID of the certificate that you want to add.
        self.cert_id = cert_id  # type: str
        # The type of cipher suite that you want to add. This parameter is available only when you specify the **HttpsPorts** parameter. Valid values:
        # 
        # *   **1:** all cipher suites.
        # *   **2:** strong cipher suites. You can select this value only when you set the **TLSVersion** parameter to **tlsv1.2**.
        # *   **99:** custom cipher suites.
        self.cipher_suite = cipher_suite  # type: int
        # The custom cipher suites that you want to add. This parameter is available only when you set the **CipherSuite** parameter to **99**.
        self.custom_ciphers = custom_ciphers  # type: list[str]
        # Specifies whether to support TLS 1.3. This parameter is available only when you specify the **HttpsPorts** parameter. Valid values:
        # 
        # *   **true:** supports TLS 1.3.
        # *   **false:** does not support TLS 1.3.
        self.enable_tlsv_3 = enable_tlsv_3  # type: bool
        # Specifies whether to enable an exclusive IP address for the domain name. This parameter is available only when you set the **IPv6Enabled** parameter to false and the **ProtectionResource** parameter to **share**. Valid values:
        # 
        # *   **true:** enables an exclusive IP address for the domain name.
        # *   **false:** does not enable an exclusive IP address for the domain name. This is the default value.
        self.exclusive_ip = exclusive_ip  # type: bool
        # Specifies whether to enable HTTP to HTTPS redirection for the domain name. This parameter is available only when you specify the **HttpsPorts** parameter and leave the **HttpPorts** parameter empty. Valid values:
        # 
        # *   **true:** enables HTTP to HTTPS redirection.
        # *   **false:** disables HTTP to HTTPS redirection.
        self.focus_https = focus_https  # type: bool
        # Specifies whether to enable HTTP/2. This parameter is available only when you specify the **HttpsPorts** parameter. Valid values:
        # 
        # *   **true:** enables HTTP/2.
        # *   **false:** disables HTTP/2. This is the default value.
        self.http_2enabled = http_2enabled  # type: bool
        # An array of HTTP listener ports. Specify the value of this parameter in the \[port1,port2,...] format.
        self.http_ports = http_ports  # type: list[int]
        # An array of HTTPS listener ports. Specify the value of this parameter in the \[port1,port2,...] format.
        self.https_ports = https_ports  # type: list[int]
        # Specifies whether to enable IPv6. Valid values:
        # 
        # *   **true:** enables IPv6.
        # *   **false:** disables IPv6. This is the default value.
        self.ipv_6enabled = ipv_6enabled  # type: bool
        # The type of the protection resource that you want to use. Valid values:
        # 
        # *   **share:** shared cluster. This is the default value.
        # *   **gslb:** shared cluster-based intelligent load balancing.
        self.protection_resource = protection_resource  # type: str
        # 是否仅客端访问。仅SM2Enable取值为true时，使用该参数。
        # 
        # - true：仅国密客户端才可以访问。
        # 
        # - false：国密和非国密均可以访问。
        self.sm2access_only = sm2access_only  # type: bool
        # 要添加的国密证书的ID。仅SM2Enable取值为true时，使用该参数。
        self.sm2cert_id = sm2cert_id  # type: str
        # 是否开启国密证书
        self.sm2enabled = sm2enabled  # type: bool
        # The version of the Transport Layer Security (TLS) protocol. This parameter is available only when you specify the **HttpsPorts** parameter. Valid values:
        # 
        # *   **tlsv1**\
        # *   **tlsv1.1**\
        # *   **tlsv1.2**\
        self.tlsversion = tlsversion  # type: str
        # The method that you want WAF to use to obtain the actual IP address of a client. Valid values:
        # 
        # *   **0:** No Layer 7 proxies are deployed in front of WAF. This is the default value.
        # *   **1:** WAF reads the first value of the X-Forwarded-For (XFF) header field as the actual IP address of the client.
        # *   **2:** WAF reads the value of a custom header field as the actual IP address of the client.
        self.xff_header_mode = xff_header_mode  # type: int
        # The custom header fields that you want to use to obtain the actual IP address of a client. Specify the value of this parameter in the \["header1","header2",...] format.
        # 
        # >  If you set the **XffHeaderMode** parameter to 2, this parameter is required.
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
        if self.sm2access_only is not None:
            result['SM2AccessOnly'] = self.sm2access_only
        if self.sm2cert_id is not None:
            result['SM2CertId'] = self.sm2cert_id
        if self.sm2enabled is not None:
            result['SM2Enabled'] = self.sm2enabled
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
        if m.get('SM2AccessOnly') is not None:
            self.sm2access_only = m.get('SM2AccessOnly')
        if m.get('SM2CertId') is not None:
            self.sm2cert_id = m.get('SM2CertId')
        if m.get('SM2Enabled') is not None:
            self.sm2enabled = m.get('SM2Enabled')
        if m.get('TLSVersion') is not None:
            self.tlsversion = m.get('TLSVersion')
        if m.get('XffHeaderMode') is not None:
            self.xff_header_mode = m.get('XffHeaderMode')
        if m.get('XffHeaders') is not None:
            self.xff_headers = m.get('XffHeaders')
        return self


class ModifyDomainRequestRedirectRequestHeaders(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the custom header field.
        self.key = key  # type: str
        # The value of the custom header field.
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
    def __init__(self, backends=None, cname_enabled=None, connect_timeout=None, focus_http_backend=None,
                 keepalive=None, keepalive_requests=None, keepalive_timeout=None, loadbalance=None, read_timeout=None,
                 request_headers=None, retry=None, routing_rules=None, sni_enabled=None, sni_host=None, write_timeout=None):
        # The back-to-origin IP addresses or domain names. You can specify only one type of address. If you use the domain name type, only IPv4 is supported.
        # 
        # *   If you use the IP address type, specify the value of this parameter in the \["ip1","ip2",...] format. You can specify up to 20 IP addresses.
        # *   If you use the domain name type, specify the value of this parameter in the \["domain"] format. You can specify up to 20 domain names.
        self.backends = backends  # type: list[str]
        # Specifies whether to enable the public cloud disaster recovery feature. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.cname_enabled = cname_enabled  # type: bool
        # The connection timeout period. Unit: seconds. Valid values: 1 to 3600.
        self.connect_timeout = connect_timeout  # type: int
        # Specifies whether to enable HTTPS to HTTP redirection for back-to-origin requests. This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.focus_http_backend = focus_http_backend  # type: bool
        # Specifies whether to enable the persistent connection feature. Valid values:
        # 
        # *   **true** (default)
        # *   **false**\
        self.keepalive = keepalive  # type: bool
        # The number of reused persistent connections. Valid values: 60 to 1000.
        # 
        # > This parameter specifies the number of reused persistent connections after you enable the persistent connection feature.
        self.keepalive_requests = keepalive_requests  # type: int
        # The timeout period of persistent connections that are in the Idle state. Valid values: 1 to 60. Default value: 15. Unit: seconds.
        # 
        # > This parameter specifies the period of time during which a reused persistent connection remains in the Idle state before the persistent connection is released.
        self.keepalive_timeout = keepalive_timeout  # type: int
        # The load balancing algorithm that you want WAF to use to forward requests to the origin server. Valid values:
        # 
        # *   **ip_hash**\
        # *   **roundRobin**\
        # *   **leastTime**. You can select this value only if you set **ProtectionResource** to **gslb**.
        self.loadbalance = loadbalance  # type: str
        # The read timeout period. Unit: seconds. Valid values: 1 to 3600.
        self.read_timeout = read_timeout  # type: int
        # The key-value pairs that you want to use to mark the requests that are processed by WAF.
        # 
        # WAF automatically adds the key-value pairs to the request headers. This way, the backend service can identify the requests that are processed by WAF.
        self.request_headers = request_headers  # type: list[ModifyDomainRequestRedirectRequestHeaders]
        # Specifies whether WAF retries to forward requests when requests fail to be forwarded to the origin server. Valid values:
        # 
        # *   **true** (default)
        # *   **false**\
        self.retry = retry  # type: bool
        # The forwarding rules that you want to configure for the domain name that you want to add to WAF in hybrid cloud mode. Set the value to a string that consists of JSON arrays. Each element in a JSON array must be a JSON struct that contains the following fields:
        # 
        # *   **rs:** The back-to-origin IP addresses or CNAMEs. The value must be of the ARRAY type.
        # *   **location:** The name of the protection node. The value must be of the STRING type.
        # *   **locationId:** The ID of the protection node. The value must be of the LONG type.
        self.routing_rules = routing_rules  # type: str
        # Specifies whether to enable origin Server Name Indication (SNI). This parameter is available only if you specify **HttpsPorts**. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.sni_enabled = sni_enabled  # type: bool
        # The value of the custom SNI field. If you do not specify this parameter, the value of the **Host** field in the request header is automatically used. If you want WAF to use an SNI field value that is different from the value of the Host field in back-to-origin requests, you can specify a custom value for the SNI field.
        # 
        # > This parameter is required only if you set **SniEnabled** to true.
        self.sni_host = sni_host  # type: str
        # The write timeout period. Unit: seconds. Valid values: 1 to 3600.
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
        if self.cname_enabled is not None:
            result['CnameEnabled'] = self.cname_enabled
        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout
        if self.focus_http_backend is not None:
            result['FocusHttpBackend'] = self.focus_http_backend
        if self.keepalive is not None:
            result['Keepalive'] = self.keepalive
        if self.keepalive_requests is not None:
            result['KeepaliveRequests'] = self.keepalive_requests
        if self.keepalive_timeout is not None:
            result['KeepaliveTimeout'] = self.keepalive_timeout
        if self.loadbalance is not None:
            result['Loadbalance'] = self.loadbalance
        if self.read_timeout is not None:
            result['ReadTimeout'] = self.read_timeout
        result['RequestHeaders'] = []
        if self.request_headers is not None:
            for k in self.request_headers:
                result['RequestHeaders'].append(k.to_map() if k else None)
        if self.retry is not None:
            result['Retry'] = self.retry
        if self.routing_rules is not None:
            result['RoutingRules'] = self.routing_rules
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
        if m.get('CnameEnabled') is not None:
            self.cname_enabled = m.get('CnameEnabled')
        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')
        if m.get('FocusHttpBackend') is not None:
            self.focus_http_backend = m.get('FocusHttpBackend')
        if m.get('Keepalive') is not None:
            self.keepalive = m.get('Keepalive')
        if m.get('KeepaliveRequests') is not None:
            self.keepalive_requests = m.get('KeepaliveRequests')
        if m.get('KeepaliveTimeout') is not None:
            self.keepalive_timeout = m.get('KeepaliveTimeout')
        if m.get('Loadbalance') is not None:
            self.loadbalance = m.get('Loadbalance')
        if m.get('ReadTimeout') is not None:
            self.read_timeout = m.get('ReadTimeout')
        self.request_headers = []
        if m.get('RequestHeaders') is not None:
            for k in m.get('RequestHeaders'):
                temp_model = ModifyDomainRequestRedirectRequestHeaders()
                self.request_headers.append(temp_model.from_map(k))
        if m.get('Retry') is not None:
            self.retry = m.get('Retry')
        if m.get('RoutingRules') is not None:
            self.routing_rules = m.get('RoutingRules')
        if m.get('SniEnabled') is not None:
            self.sni_enabled = m.get('SniEnabled')
        if m.get('SniHost') is not None:
            self.sni_host = m.get('SniHost')
        if m.get('WriteTimeout') is not None:
            self.write_timeout = m.get('WriteTimeout')
        return self


class ModifyDomainRequest(TeaModel):
    def __init__(self, access_type=None, domain=None, instance_id=None, listen=None, redirect=None, region_id=None,
                 source_ip=None):
        # The mode in which you want to add the domain name to WAF. Valid values:
        # 
        # *   **share:** adds the domain name to WAF in CNAME record mode. This is the default value.
        # *   **hybrid_cloud_cname:** adds the domain name to WAF in hybrid cloud reverse proxy mode.
        self.access_type = access_type  # type: str
        # The domain name whose access configurations you want to modify.
        self.domain = domain  # type: str
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The configurations of the listeners.
        self.listen = listen  # type: ModifyDomainRequestListen
        # The configurations of the forwarding rule.
        self.redirect = redirect  # type: ModifyDomainRequestRedirect
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The source IP address of the request. The value of this parameter is specified by the system.
        self.source_ip = source_ip  # type: str

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
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
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
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class ModifyDomainShrinkRequest(TeaModel):
    def __init__(self, access_type=None, domain=None, instance_id=None, listen_shrink=None, redirect_shrink=None,
                 region_id=None, source_ip=None):
        # The mode in which you want to add the domain name to WAF. Valid values:
        # 
        # *   **share:** adds the domain name to WAF in CNAME record mode. This is the default value.
        # *   **hybrid_cloud_cname:** adds the domain name to WAF in hybrid cloud reverse proxy mode.
        self.access_type = access_type  # type: str
        # The domain name whose access configurations you want to modify.
        self.domain = domain  # type: str
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The configurations of the listeners.
        self.listen_shrink = listen_shrink  # type: str
        # The configurations of the forwarding rule.
        self.redirect_shrink = redirect_shrink  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The source IP address of the request. The value of this parameter is specified by the system.
        self.source_ip = source_ip  # type: str

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
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
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
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class ModifyDomainResponseBodyDomainInfo(TeaModel):
    def __init__(self, cname=None, domain=None, domain_id=None):
        # The CNAME that is assigned by WAF to the domain name.
        self.cname = cname  # type: str
        # The domain name whose access configurations you modified.
        self.domain = domain  # type: str
        # The ID of the domain name.
        self.domain_id = domain_id  # type: str

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
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        return self


class ModifyDomainResponseBody(TeaModel):
    def __init__(self, domain_info=None, request_id=None):
        # The information about the domain name.
        self.domain_info = domain_info  # type: ModifyDomainResponseBodyDomainInfo
        # The ID of the request.
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


class ModifyHybridCloudClusterBypassStatusRequest(TeaModel):
    def __init__(self, cluster_resource_id=None, instance_id=None, rule_status=None):
        # The ID of the hybrid cloud cluster.
        self.cluster_resource_id = cluster_resource_id  # type: str
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # **\
        # 
        # **You can call the **DescribeInstanceInfo[ operation to obtain the ID of the WAF instance.](~~140857~~)
        self.instance_id = instance_id  # type: str
        # The status of manual bypass. Valid values:
        # 
        # *   **on**: enabled.
        # *   **off**: disabled. This is the default value.
        self.rule_status = rule_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHybridCloudClusterBypassStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_resource_id is not None:
            result['ClusterResourceId'] = self.cluster_resource_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterResourceId') is not None:
            self.cluster_resource_id = m.get('ClusterResourceId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')
        return self


class ModifyHybridCloudClusterBypassStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHybridCloudClusterBypassStatusResponseBody, self).to_map()
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


class ModifyHybridCloudClusterBypassStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyHybridCloudClusterBypassStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyHybridCloudClusterBypassStatusResponse, self).to_map()
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
            temp_model = ModifyHybridCloudClusterBypassStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMajorProtectionBlackIpRequest(TeaModel):
    def __init__(self, description=None, expired_time=None, instance_id=None, ip_list=None, region_id=None,
                 resource_manager_resource_group_id=None, rule_id=None, template_id=None):
        # The description of the IP address blacklist.
        self.description = description  # type: str
        # The time after which the IP address blacklist becomes invalid. Unit: seconds.
        # 
        # >  If you set this parameter to **0**, the blacklist is permanently valid.
        self.expired_time = expired_time  # type: long
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The IP addresses that you want to add to the IP address blacklist. You can specify multiple CIDR blocks or IP addresses. IPv4 and IPv6 addresses are supported. Separate the CIDR blocks or IP addresses with commas (,). For more information, see [Protection for major events](~~425591~~).
        self.ip_list = ip_list  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The ID of the IP address blacklist rule for major event protection.
        self.rule_id = rule_id  # type: long
        # The ID of the IP address blacklist rule template for major event protection.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ModifyMajorProtectionBlackIpResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, instance_id=None, region_id=None, resource=None, resource_manager_resource_group_id=None,
                 status=None):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The protected object on which you want to manage the log collection feature.
        self.resource = resource  # type: str
        # The ID of the resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # Specifies whether to enable the log collection feature for the protected object. Valid values:
        # 
        # *   **true:** enables the log collection feature.
        # *   **false:** disables the log collection feature.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyResourceLogStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, status=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the log collection feature is enabled for the protected object. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
    def __init__(self, bind_resource_groups=None, bind_resources=None, instance_id=None, region_id=None,
                 resource_manager_resource_group_id=None, template_id=None, unbind_resource_groups=None, unbind_resources=None):
        # The protected object groups that you want to associate with the protection rule template. Specify the value of this parameter in the \["group1","group2",...] format.
        self.bind_resource_groups = bind_resource_groups  # type: list[str]
        # The protected objects that you want to associate with the protection rule template. Specify the value of this parameter in the \["XX1","XX2",...] format.
        self.bind_resources = bind_resources  # type: list[str]
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](~~433756~~) operation to obtain the ID of the WAF instance.
        self.instance_id = instance_id  # type: str
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id  # type: str
        # The ID of the protection rule template.
        self.template_id = template_id  # type: long
        # The protected object groups that you want to disassociate from the protection rule template. Specify the value of this parameter in the \["group1","group2",...] format.
        self.unbind_resource_groups = unbind_resource_groups  # type: list[str]
        # The protected objects that you want to disassociate from the protection rule template. Specify the value of this parameter in the \["XX1","XX2",...] format.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UnbindResourceGroups') is not None:
            self.unbind_resource_groups = m.get('UnbindResourceGroups')
        if m.get('UnbindResources') is not None:
            self.unbind_resources = m.get('UnbindResources')
        return self


class ModifyTemplateResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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


