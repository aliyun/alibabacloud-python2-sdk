# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateCertificateRequest(TeaModel):
    def __init__(self, domain=None, certificate=None, private_key=None, certificate_name=None, instance_id=None):
        self.domain = domain  # type: str
        self.certificate = certificate  # type: str
        self.private_key = private_key  # type: str
        self.certificate_name = certificate_name  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None, certificate_id=None):
        self.request_id = request_id  # type: str
        self.certificate_id = certificate_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class CreateCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertificateByCertificateIdRequest(TeaModel):
    def __init__(self, domain=None, certificate_id=None, instance_id=None):
        self.domain = domain  # type: str
        self.certificate_id = certificate_id  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCertificateByCertificateIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateCertificateByCertificateIdResponseBody(TeaModel):
    def __init__(self, request_id=None, certificate_id=None):
        self.request_id = request_id  # type: str
        self.certificate_id = certificate_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCertificateByCertificateIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class CreateCertificateByCertificateIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateCertificateByCertificateIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCertificateByCertificateIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateCertificateByCertificateIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainRequest(TeaModel):
    def __init__(self, instance_id=None, domain=None, source_ips=None, is_access_product=None,
                 access_header_mode=None, access_headers=None, load_balancing=None, log_headers=None, http_port=None, https_port=None,
                 http_2port=None, http_to_user_ip=None, https_redirect=None, cluster_type=None, resource_group_id=None,
                 connection_time=None, read_time=None, write_time=None, access_type=None, cloud_native_instances=None,
                 ip_follow_status=None):
        self.instance_id = instance_id  # type: str
        self.domain = domain  # type: str
        self.source_ips = source_ips  # type: str
        self.is_access_product = is_access_product  # type: int
        self.access_header_mode = access_header_mode  # type: int
        self.access_headers = access_headers  # type: str
        self.load_balancing = load_balancing  # type: int
        self.log_headers = log_headers  # type: str
        self.http_port = http_port  # type: str
        self.https_port = https_port  # type: str
        self.http_2port = http_2port  # type: str
        self.http_to_user_ip = http_to_user_ip  # type: int
        self.https_redirect = https_redirect  # type: int
        self.cluster_type = cluster_type  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.connection_time = connection_time  # type: int
        self.read_time = read_time  # type: int
        self.write_time = write_time  # type: int
        self.access_type = access_type  # type: str
        self.cloud_native_instances = cloud_native_instances  # type: str
        self.ip_follow_status = ip_follow_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.source_ips is not None:
            result['SourceIps'] = self.source_ips
        if self.is_access_product is not None:
            result['IsAccessProduct'] = self.is_access_product
        if self.access_header_mode is not None:
            result['AccessHeaderMode'] = self.access_header_mode
        if self.access_headers is not None:
            result['AccessHeaders'] = self.access_headers
        if self.load_balancing is not None:
            result['LoadBalancing'] = self.load_balancing
        if self.log_headers is not None:
            result['LogHeaders'] = self.log_headers
        if self.http_port is not None:
            result['HttpPort'] = self.http_port
        if self.https_port is not None:
            result['HttpsPort'] = self.https_port
        if self.http_2port is not None:
            result['Http2Port'] = self.http_2port
        if self.http_to_user_ip is not None:
            result['HttpToUserIp'] = self.http_to_user_ip
        if self.https_redirect is not None:
            result['HttpsRedirect'] = self.https_redirect
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.connection_time is not None:
            result['ConnectionTime'] = self.connection_time
        if self.read_time is not None:
            result['ReadTime'] = self.read_time
        if self.write_time is not None:
            result['WriteTime'] = self.write_time
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.cloud_native_instances is not None:
            result['CloudNativeInstances'] = self.cloud_native_instances
        if self.ip_follow_status is not None:
            result['IpFollowStatus'] = self.ip_follow_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('SourceIps') is not None:
            self.source_ips = m.get('SourceIps')
        if m.get('IsAccessProduct') is not None:
            self.is_access_product = m.get('IsAccessProduct')
        if m.get('AccessHeaderMode') is not None:
            self.access_header_mode = m.get('AccessHeaderMode')
        if m.get('AccessHeaders') is not None:
            self.access_headers = m.get('AccessHeaders')
        if m.get('LoadBalancing') is not None:
            self.load_balancing = m.get('LoadBalancing')
        if m.get('LogHeaders') is not None:
            self.log_headers = m.get('LogHeaders')
        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')
        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')
        if m.get('Http2Port') is not None:
            self.http_2port = m.get('Http2Port')
        if m.get('HttpToUserIp') is not None:
            self.http_to_user_ip = m.get('HttpToUserIp')
        if m.get('HttpsRedirect') is not None:
            self.https_redirect = m.get('HttpsRedirect')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ConnectionTime') is not None:
            self.connection_time = m.get('ConnectionTime')
        if m.get('ReadTime') is not None:
            self.read_time = m.get('ReadTime')
        if m.get('WriteTime') is not None:
            self.write_time = m.get('WriteTime')
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('CloudNativeInstances') is not None:
            self.cloud_native_instances = m.get('CloudNativeInstances')
        if m.get('IpFollowStatus') is not None:
            self.ip_follow_status = m.get('IpFollowStatus')
        return self


class CreateDomainResponseBody(TeaModel):
    def __init__(self, request_id=None, cname=None):
        self.request_id = request_id  # type: str
        self.cname = cname  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cname is not None:
            result['Cname'] = self.cname
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        return self


class CreateDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProtectionModuleRuleRequest(TeaModel):
    def __init__(self, domain=None, defense_type=None, rule=None, instance_id=None):
        self.domain = domain  # type: str
        self.defense_type = defense_type  # type: str
        self.rule = rule  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProtectionModuleRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.rule is not None:
            result['Rule'] = self.rule
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateProtectionModuleRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProtectionModuleRuleResponseBody, self).to_map()
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


class CreateProtectionModuleRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateProtectionModuleRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProtectionModuleRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateProtectionModuleRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(self, instance_id=None, domain=None):
        self.instance_id = instance_id  # type: str
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
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


class DeleteInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, resource_group_id=None):
        self.instance_id = instance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceResponseBody, self).to_map()
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


class DeleteInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProtectionModuleRuleRequest(TeaModel):
    def __init__(self, domain=None, defense_type=None, rule_id=None, instance_id=None):
        self.domain = domain  # type: str
        self.defense_type = defense_type  # type: str
        self.rule_id = rule_id  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProtectionModuleRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteProtectionModuleRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProtectionModuleRuleResponseBody, self).to_map()
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


class DeleteProtectionModuleRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteProtectionModuleRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProtectionModuleRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteProtectionModuleRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertificatesRequest(TeaModel):
    def __init__(self, instance_id=None, domain=None):
        self.instance_id = instance_id  # type: str
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCertificatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeCertificatesResponseBodyCertificates(TeaModel):
    def __init__(self, certificate_name=None, common_name=None, sans=None, is_using=None, certificate_id=None):
        self.certificate_name = certificate_name  # type: str
        self.common_name = common_name  # type: str
        self.sans = sans  # type: list[str]
        self.is_using = is_using  # type: bool
        self.certificate_id = certificate_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCertificatesResponseBodyCertificates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.common_name is not None:
            result['CommonName'] = self.common_name
        if self.sans is not None:
            result['Sans'] = self.sans
        if self.is_using is not None:
            result['IsUsing'] = self.is_using
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')
        if m.get('Sans') is not None:
            self.sans = m.get('Sans')
        if m.get('IsUsing') is not None:
            self.is_using = m.get('IsUsing')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        return self


class DescribeCertificatesResponseBody(TeaModel):
    def __init__(self, request_id=None, certificates=None):
        self.request_id = request_id  # type: str
        self.certificates = certificates  # type: list[DescribeCertificatesResponseBodyCertificates]

    def validate(self):
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCertificatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = DescribeCertificatesResponseBodyCertificates()
                self.certificates.append(temp_model.from_map(k))
        return self


class DescribeCertificatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCertificatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCertificatesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCertificatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertMatchStatusRequest(TeaModel):
    def __init__(self, domain=None, certificate=None, private_key=None, instance_id=None):
        self.domain = domain  # type: str
        self.certificate = certificate  # type: str
        self.private_key = private_key  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCertMatchStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeCertMatchStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, match_status=None):
        self.request_id = request_id  # type: str
        self.match_status = match_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCertMatchStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.match_status is not None:
            result['MatchStatus'] = self.match_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MatchStatus') is not None:
            self.match_status = m.get('MatchStatus')
        return self


class DescribeCertMatchStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCertMatchStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCertMatchStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCertMatchStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRequest(TeaModel):
    def __init__(self, instance_id=None, domain=None):
        self.instance_id = instance_id  # type: str
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainResponseBodyDomainCloudNativeInstancesProtocolPortConfigs(TeaModel):
    def __init__(self, protocol=None, ports=None):
        self.protocol = protocol  # type: str
        self.ports = ports  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainResponseBodyDomainCloudNativeInstancesProtocolPortConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.ports is not None:
            result['Ports'] = self.ports
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        return self


class DescribeDomainResponseBodyDomainCloudNativeInstances(TeaModel):
    def __init__(self, protocol_port_configs=None, redirection_type_name=None, cloud_native_product_name=None,
                 instance_id=None, ipaddress_list=None):
        self.protocol_port_configs = protocol_port_configs  # type: list[DescribeDomainResponseBodyDomainCloudNativeInstancesProtocolPortConfigs]
        self.redirection_type_name = redirection_type_name  # type: str
        self.cloud_native_product_name = cloud_native_product_name  # type: str
        self.instance_id = instance_id  # type: str
        self.ipaddress_list = ipaddress_list  # type: str

    def validate(self):
        if self.protocol_port_configs:
            for k in self.protocol_port_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainResponseBodyDomainCloudNativeInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProtocolPortConfigs'] = []
        if self.protocol_port_configs is not None:
            for k in self.protocol_port_configs:
                result['ProtocolPortConfigs'].append(k.to_map() if k else None)
        if self.redirection_type_name is not None:
            result['RedirectionTypeName'] = self.redirection_type_name
        if self.cloud_native_product_name is not None:
            result['CloudNativeProductName'] = self.cloud_native_product_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ipaddress_list is not None:
            result['IPAddressList'] = self.ipaddress_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.protocol_port_configs = []
        if m.get('ProtocolPortConfigs') is not None:
            for k in m.get('ProtocolPortConfigs'):
                temp_model = DescribeDomainResponseBodyDomainCloudNativeInstancesProtocolPortConfigs()
                self.protocol_port_configs.append(temp_model.from_map(k))
        if m.get('RedirectionTypeName') is not None:
            self.redirection_type_name = m.get('RedirectionTypeName')
        if m.get('CloudNativeProductName') is not None:
            self.cloud_native_product_name = m.get('CloudNativeProductName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IPAddressList') is not None:
            self.ipaddress_list = m.get('IPAddressList')
        return self


class DescribeDomainResponseBodyDomainLogHeaders(TeaModel):
    def __init__(self, k=None, v=None):
        self.k = k  # type: str
        self.v = v  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainResponseBodyDomainLogHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.k is not None:
            result['k'] = self.k
        if self.v is not None:
            result['v'] = self.v
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('k') is not None:
            self.k = m.get('k')
        if m.get('v') is not None:
            self.v = m.get('v')
        return self


class DescribeDomainResponseBodyDomain(TeaModel):
    def __init__(self, http_2port=None, cloud_native_instances=None, http_to_user_ip=None, http_port=None,
                 log_headers=None, is_access_product=None, access_headers=None, access_header_mode=None, https_redirect=None,
                 load_balancing=None, ip_follow_status=None, access_type=None, version=None, cluster_type=None, read_time=None,
                 write_time=None, resource_group_id=None, cname=None, source_ips=None, connection_time=None, https_port=None):
        self.http_2port = http_2port  # type: list[str]
        self.cloud_native_instances = cloud_native_instances  # type: list[DescribeDomainResponseBodyDomainCloudNativeInstances]
        self.http_to_user_ip = http_to_user_ip  # type: int
        self.http_port = http_port  # type: list[str]
        self.log_headers = log_headers  # type: list[DescribeDomainResponseBodyDomainLogHeaders]
        self.is_access_product = is_access_product  # type: int
        self.access_headers = access_headers  # type: list[str]
        self.access_header_mode = access_header_mode  # type: int
        self.https_redirect = https_redirect  # type: int
        self.load_balancing = load_balancing  # type: int
        self.ip_follow_status = ip_follow_status  # type: int
        self.access_type = access_type  # type: str
        self.version = version  # type: long
        self.cluster_type = cluster_type  # type: int
        self.read_time = read_time  # type: int
        self.write_time = write_time  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.cname = cname  # type: str
        self.source_ips = source_ips  # type: list[str]
        self.connection_time = connection_time  # type: int
        self.https_port = https_port  # type: list[str]

    def validate(self):
        if self.cloud_native_instances:
            for k in self.cloud_native_instances:
                if k:
                    k.validate()
        if self.log_headers:
            for k in self.log_headers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainResponseBodyDomain, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_2port is not None:
            result['Http2Port'] = self.http_2port
        result['CloudNativeInstances'] = []
        if self.cloud_native_instances is not None:
            for k in self.cloud_native_instances:
                result['CloudNativeInstances'].append(k.to_map() if k else None)
        if self.http_to_user_ip is not None:
            result['HttpToUserIp'] = self.http_to_user_ip
        if self.http_port is not None:
            result['HttpPort'] = self.http_port
        result['LogHeaders'] = []
        if self.log_headers is not None:
            for k in self.log_headers:
                result['LogHeaders'].append(k.to_map() if k else None)
        if self.is_access_product is not None:
            result['IsAccessProduct'] = self.is_access_product
        if self.access_headers is not None:
            result['AccessHeaders'] = self.access_headers
        if self.access_header_mode is not None:
            result['AccessHeaderMode'] = self.access_header_mode
        if self.https_redirect is not None:
            result['HttpsRedirect'] = self.https_redirect
        if self.load_balancing is not None:
            result['LoadBalancing'] = self.load_balancing
        if self.ip_follow_status is not None:
            result['IpFollowStatus'] = self.ip_follow_status
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.version is not None:
            result['Version'] = self.version
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.read_time is not None:
            result['ReadTime'] = self.read_time
        if self.write_time is not None:
            result['WriteTime'] = self.write_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.source_ips is not None:
            result['SourceIps'] = self.source_ips
        if self.connection_time is not None:
            result['ConnectionTime'] = self.connection_time
        if self.https_port is not None:
            result['HttpsPort'] = self.https_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Http2Port') is not None:
            self.http_2port = m.get('Http2Port')
        self.cloud_native_instances = []
        if m.get('CloudNativeInstances') is not None:
            for k in m.get('CloudNativeInstances'):
                temp_model = DescribeDomainResponseBodyDomainCloudNativeInstances()
                self.cloud_native_instances.append(temp_model.from_map(k))
        if m.get('HttpToUserIp') is not None:
            self.http_to_user_ip = m.get('HttpToUserIp')
        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')
        self.log_headers = []
        if m.get('LogHeaders') is not None:
            for k in m.get('LogHeaders'):
                temp_model = DescribeDomainResponseBodyDomainLogHeaders()
                self.log_headers.append(temp_model.from_map(k))
        if m.get('IsAccessProduct') is not None:
            self.is_access_product = m.get('IsAccessProduct')
        if m.get('AccessHeaders') is not None:
            self.access_headers = m.get('AccessHeaders')
        if m.get('AccessHeaderMode') is not None:
            self.access_header_mode = m.get('AccessHeaderMode')
        if m.get('HttpsRedirect') is not None:
            self.https_redirect = m.get('HttpsRedirect')
        if m.get('LoadBalancing') is not None:
            self.load_balancing = m.get('LoadBalancing')
        if m.get('IpFollowStatus') is not None:
            self.ip_follow_status = m.get('IpFollowStatus')
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ReadTime') is not None:
            self.read_time = m.get('ReadTime')
        if m.get('WriteTime') is not None:
            self.write_time = m.get('WriteTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('SourceIps') is not None:
            self.source_ips = m.get('SourceIps')
        if m.get('ConnectionTime') is not None:
            self.connection_time = m.get('ConnectionTime')
        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')
        return self


class DescribeDomainResponseBody(TeaModel):
    def __init__(self, request_id=None, domain=None):
        self.request_id = request_id  # type: str
        self.domain = domain  # type: DescribeDomainResponseBodyDomain

    def validate(self):
        if self.domain:
            self.domain.validate()

    def to_map(self):
        _map = super(DescribeDomainResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain is not None:
            result['Domain'] = self.domain.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Domain') is not None:
            temp_model = DescribeDomainResponseBodyDomain()
            self.domain = temp_model.from_map(m['Domain'])
        return self


class DescribeDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainAdvanceConfigsRequest(TeaModel):
    def __init__(self, instance_id=None, domain_list=None, resource_group_id=None):
        self.instance_id = instance_id  # type: str
        self.domain_list = domain_list  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainAdvanceConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDomainAdvanceConfigsResponseBodyDomainConfigsProfile(TeaModel):
    def __init__(self, http_2port=None, ipv_6status=None, http_port=None, gslbstatus=None, rs=None,
                 vip_service_status=None, cluster_type=None, exclusive_vip_status=None, cname=None, cert_status=None, https_port=None,
                 resolved_type=None):
        self.http_2port = http_2port  # type: str
        self.ipv_6status = ipv_6status  # type: int
        self.http_port = http_port  # type: str
        self.gslbstatus = gslbstatus  # type: str
        self.rs = rs  # type: str
        self.vip_service_status = vip_service_status  # type: int
        self.cluster_type = cluster_type  # type: int
        self.exclusive_vip_status = exclusive_vip_status  # type: int
        self.cname = cname  # type: str
        self.cert_status = cert_status  # type: int
        self.https_port = https_port  # type: str
        self.resolved_type = resolved_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainAdvanceConfigsResponseBodyDomainConfigsProfile, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_2port is not None:
            result['Http2Port'] = self.http_2port
        if self.ipv_6status is not None:
            result['Ipv6Status'] = self.ipv_6status
        if self.http_port is not None:
            result['HttpPort'] = self.http_port
        if self.gslbstatus is not None:
            result['GSLBStatus'] = self.gslbstatus
        if self.rs is not None:
            result['Rs'] = self.rs
        if self.vip_service_status is not None:
            result['VipServiceStatus'] = self.vip_service_status
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.exclusive_vip_status is not None:
            result['ExclusiveVipStatus'] = self.exclusive_vip_status
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.cert_status is not None:
            result['CertStatus'] = self.cert_status
        if self.https_port is not None:
            result['HttpsPort'] = self.https_port
        if self.resolved_type is not None:
            result['ResolvedType'] = self.resolved_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Http2Port') is not None:
            self.http_2port = m.get('Http2Port')
        if m.get('Ipv6Status') is not None:
            self.ipv_6status = m.get('Ipv6Status')
        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')
        if m.get('GSLBStatus') is not None:
            self.gslbstatus = m.get('GSLBStatus')
        if m.get('Rs') is not None:
            self.rs = m.get('Rs')
        if m.get('VipServiceStatus') is not None:
            self.vip_service_status = m.get('VipServiceStatus')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ExclusiveVipStatus') is not None:
            self.exclusive_vip_status = m.get('ExclusiveVipStatus')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('CertStatus') is not None:
            self.cert_status = m.get('CertStatus')
        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')
        if m.get('ResolvedType') is not None:
            self.resolved_type = m.get('ResolvedType')
        return self


class DescribeDomainAdvanceConfigsResponseBodyDomainConfigs(TeaModel):
    def __init__(self, profile=None, domain=None):
        self.profile = profile  # type: DescribeDomainAdvanceConfigsResponseBodyDomainConfigsProfile
        self.domain = domain  # type: str

    def validate(self):
        if self.profile:
            self.profile.validate()

    def to_map(self):
        _map = super(DescribeDomainAdvanceConfigsResponseBodyDomainConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.profile is not None:
            result['Profile'] = self.profile.to_map()
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Profile') is not None:
            temp_model = DescribeDomainAdvanceConfigsResponseBodyDomainConfigsProfile()
            self.profile = temp_model.from_map(m['Profile'])
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainAdvanceConfigsResponseBody(TeaModel):
    def __init__(self, request_id=None, domain_configs=None):
        self.request_id = request_id  # type: str
        self.domain_configs = domain_configs  # type: list[DescribeDomainAdvanceConfigsResponseBodyDomainConfigs]

    def validate(self):
        if self.domain_configs:
            for k in self.domain_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainAdvanceConfigsResponseBody, self).to_map()
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
                temp_model = DescribeDomainAdvanceConfigsResponseBodyDomainConfigs()
                self.domain_configs.append(temp_model.from_map(k))
        return self


class DescribeDomainAdvanceConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainAdvanceConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainAdvanceConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainAdvanceConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainBasicConfigsRequest(TeaModel):
    def __init__(self, instance_id=None, domain_key=None, access_type=None, cloud_native_product_id=None,
                 page_number=None, page_size=None, resource_group_id=None):
        self.instance_id = instance_id  # type: str
        self.domain_key = domain_key  # type: str
        self.access_type = access_type  # type: str
        self.cloud_native_product_id = cloud_native_product_id  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainBasicConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain_key is not None:
            result['DomainKey'] = self.domain_key
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.cloud_native_product_id is not None:
            result['CloudNativeProductId'] = self.cloud_native_product_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DomainKey') is not None:
            self.domain_key = m.get('DomainKey')
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('CloudNativeProductId') is not None:
            self.cloud_native_product_id = m.get('CloudNativeProductId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDomainBasicConfigsResponseBodyDomainConfigs(TeaModel):
    def __init__(self, status=None, domain=None, owner=None, cc_mode=None, cc_status=None, access_type=None,
                 version=None, acl_status=None, waf_status=None, waf_mode=None):
        self.status = status  # type: int
        self.domain = domain  # type: str
        self.owner = owner  # type: str
        self.cc_mode = cc_mode  # type: int
        self.cc_status = cc_status  # type: int
        self.access_type = access_type  # type: str
        self.version = version  # type: long
        self.acl_status = acl_status  # type: int
        self.waf_status = waf_status  # type: int
        self.waf_mode = waf_mode  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainBasicConfigsResponseBodyDomainConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.cc_mode is not None:
            result['CcMode'] = self.cc_mode
        if self.cc_status is not None:
            result['CcStatus'] = self.cc_status
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.version is not None:
            result['Version'] = self.version
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.waf_status is not None:
            result['WafStatus'] = self.waf_status
        if self.waf_mode is not None:
            result['WafMode'] = self.waf_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('CcMode') is not None:
            self.cc_mode = m.get('CcMode')
        if m.get('CcStatus') is not None:
            self.cc_status = m.get('CcStatus')
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('WafStatus') is not None:
            self.waf_status = m.get('WafStatus')
        if m.get('WafMode') is not None:
            self.waf_mode = m.get('WafMode')
        return self


class DescribeDomainBasicConfigsResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, domain_configs=None):
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.domain_configs = domain_configs  # type: list[DescribeDomainBasicConfigsResponseBodyDomainConfigs]

    def validate(self):
        if self.domain_configs:
            for k in self.domain_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainBasicConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DomainConfigs'] = []
        if self.domain_configs is not None:
            for k in self.domain_configs:
                result['DomainConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.domain_configs = []
        if m.get('DomainConfigs') is not None:
            for k in m.get('DomainConfigs'):
                temp_model = DescribeDomainBasicConfigsResponseBodyDomainConfigs()
                self.domain_configs.append(temp_model.from_map(k))
        return self


class DescribeDomainBasicConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainBasicConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainBasicConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainBasicConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainListRequest(TeaModel):
    def __init__(self, resource_group_id=None, instance_id=None, domain_name=None, page_number=None, page_size=None,
                 is_sub=None, domain_names=None):
        self.resource_group_id = resource_group_id  # type: str
        self.instance_id = instance_id  # type: str
        self.domain_name = domain_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.is_sub = is_sub  # type: int
        self.domain_names = domain_names  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.is_sub is not None:
            result['IsSub'] = self.is_sub
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('IsSub') is not None:
            self.is_sub = m.get('IsSub')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        return self


class DescribeDomainListResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, domain_names=None):
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.domain_names = domain_names  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        return self


class DescribeDomainListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainNamesRequest(TeaModel):
    def __init__(self, instance_id=None, resource_group_id=None):
        self.instance_id = instance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainNamesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDomainNamesResponseBody(TeaModel):
    def __init__(self, request_id=None, domain_names=None):
        self.request_id = request_id  # type: str
        self.domain_names = domain_names  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainNamesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        return self


class DescribeDomainNamesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainNamesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainNamesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRuleGroupRequest(TeaModel):
    def __init__(self, domain=None, instance_id=None):
        self.domain = domain  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRuleGroupRequest, self).to_map()
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


class DescribeDomainRuleGroupResponseBody(TeaModel):
    def __init__(self, rule_group_id=None, request_id=None):
        self.rule_group_id = rule_group_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainRuleGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_group_id is not None:
            result['RuleGroupId'] = self.rule_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleGroupId') is not None:
            self.rule_group_id = m.get('RuleGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainRuleGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDomainRuleGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainRuleGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainRuleGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceInfoRequest(TeaModel):
    def __init__(self, instance_id=None, resource_group_id=None):
        self.instance_id = instance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeInstanceInfoResponseBodyInstanceInfo(TeaModel):
    def __init__(self, status=None, end_date=None, version=None, remain_day=None, region=None, pay_type=None,
                 in_debt=None, instance_id=None, subscription_type=None, trial=None):
        self.status = status  # type: int
        self.end_date = end_date  # type: long
        self.version = version  # type: str
        self.remain_day = remain_day  # type: int
        self.region = region  # type: str
        self.pay_type = pay_type  # type: int
        self.in_debt = in_debt  # type: int
        self.instance_id = instance_id  # type: str
        self.subscription_type = subscription_type  # type: str
        self.trial = trial  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceInfoResponseBodyInstanceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.version is not None:
            result['Version'] = self.version
        if self.remain_day is not None:
            result['RemainDay'] = self.remain_day
        if self.region is not None:
            result['Region'] = self.region
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.trial is not None:
            result['Trial'] = self.trial
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('RemainDay') is not None:
            self.remain_day = m.get('RemainDay')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Trial') is not None:
            self.trial = m.get('Trial')
        return self


class DescribeInstanceInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_info=None):
        self.request_id = request_id  # type: str
        self.instance_info = instance_info  # type: DescribeInstanceInfoResponseBodyInstanceInfo

    def validate(self):
        if self.instance_info:
            self.instance_info.validate()

    def to_map(self):
        _map = super(DescribeInstanceInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_info is not None:
            result['InstanceInfo'] = self.instance_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceInfo') is not None:
            temp_model = DescribeInstanceInfoResponseBodyInstanceInfo()
            self.instance_info = temp_model.from_map(m['InstanceInfo'])
        return self


class DescribeInstanceInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstanceInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceInfosRequest(TeaModel):
    def __init__(self, instance_source=None, instance_id=None, resource_group_id=None):
        self.instance_source = instance_source  # type: str
        self.instance_id = instance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeInstanceInfosResponseBodyInstanceInfos(TeaModel):
    def __init__(self, status=None, end_date=None, remain_day=None, region=None, pay_type=None, in_debt=None,
                 instance_id=None, subscription_type=None, trial=None):
        self.status = status  # type: int
        self.end_date = end_date  # type: long
        self.remain_day = remain_day  # type: int
        self.region = region  # type: str
        self.pay_type = pay_type  # type: int
        self.in_debt = in_debt  # type: int
        self.instance_id = instance_id  # type: str
        self.subscription_type = subscription_type  # type: str
        self.trial = trial  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceInfosResponseBodyInstanceInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.remain_day is not None:
            result['RemainDay'] = self.remain_day
        if self.region is not None:
            result['Region'] = self.region
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.in_debt is not None:
            result['InDebt'] = self.in_debt
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.trial is not None:
            result['Trial'] = self.trial
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('RemainDay') is not None:
            self.remain_day = m.get('RemainDay')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('InDebt') is not None:
            self.in_debt = m.get('InDebt')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Trial') is not None:
            self.trial = m.get('Trial')
        return self


class DescribeInstanceInfosResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_infos=None):
        self.request_id = request_id  # type: str
        self.instance_infos = instance_infos  # type: list[DescribeInstanceInfosResponseBodyInstanceInfos]

    def validate(self):
        if self.instance_infos:
            for k in self.instance_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['InstanceInfos'] = []
        if self.instance_infos is not None:
            for k in self.instance_infos:
                result['InstanceInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instance_infos = []
        if m.get('InstanceInfos') is not None:
            for k in m.get('InstanceInfos'):
                temp_model = DescribeInstanceInfosResponseBodyInstanceInfos()
                self.instance_infos.append(temp_model.from_map(k))
        return self


class DescribeInstanceInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstanceInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceInfosResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSpecInfoRequest(TeaModel):
    def __init__(self, instance_id=None, resource_group_id=None):
        self.instance_id = instance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceSpecInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeInstanceSpecInfoResponseBodyInstanceSpecInfos(TeaModel):
    def __init__(self, value=None, code=None):
        self.value = value  # type: str
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceSpecInfoResponseBodyInstanceSpecInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeInstanceSpecInfoResponseBody(TeaModel):
    def __init__(self, instance_spec_infos=None, request_id=None, instance_id=None, version=None, expire_time=None):
        self.instance_spec_infos = instance_spec_infos  # type: list[DescribeInstanceSpecInfoResponseBodyInstanceSpecInfos]
        self.request_id = request_id  # type: str
        self.instance_id = instance_id  # type: str
        self.version = version  # type: str
        self.expire_time = expire_time  # type: long

    def validate(self):
        if self.instance_spec_infos:
            for k in self.instance_spec_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceSpecInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceSpecInfos'] = []
        if self.instance_spec_infos is not None:
            for k in self.instance_spec_infos:
                result['InstanceSpecInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.version is not None:
            result['Version'] = self.version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_spec_infos = []
        if m.get('InstanceSpecInfos') is not None:
            for k in m.get('InstanceSpecInfos'):
                temp_model = DescribeInstanceSpecInfoResponseBodyInstanceSpecInfos()
                self.instance_spec_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class DescribeInstanceSpecInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstanceSpecInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceSpecInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceSpecInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogServiceStatusRequest(TeaModel):
    def __init__(self, instance_id=None, region=None, resource_group_id=None, page_number=None, page_size=None,
                 domain_names=None):
        self.instance_id = instance_id  # type: str
        self.region = region  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.domain_names = domain_names  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogServiceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        return self


class DescribeLogServiceStatusResponseBodyDomainStatus(TeaModel):
    def __init__(self, domain=None, sls_log_active=None):
        self.domain = domain  # type: str
        self.sls_log_active = sls_log_active  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogServiceStatusResponseBodyDomainStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.sls_log_active is not None:
            result['SlsLogActive'] = self.sls_log_active
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('SlsLogActive') is not None:
            self.sls_log_active = m.get('SlsLogActive')
        return self


class DescribeLogServiceStatusResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, domain_status=None):
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.domain_status = domain_status  # type: list[DescribeLogServiceStatusResponseBodyDomainStatus]

    def validate(self):
        if self.domain_status:
            for k in self.domain_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLogServiceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DomainStatus'] = []
        if self.domain_status is not None:
            for k in self.domain_status:
                result['DomainStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.domain_status = []
        if m.get('DomainStatus') is not None:
            for k in m.get('DomainStatus'):
                temp_model = DescribeLogServiceStatusResponseBodyDomainStatus()
                self.domain_status.append(temp_model.from_map(k))
        return self


class DescribeLogServiceStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeLogServiceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogServiceStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLogServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProtectionModuleCodeConfigRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, code_type=None, code_value=None, instance_id=None,
                 resource_group_id=None):
        self.source_ip = source_ip  # type: str
        self.lang = lang  # type: str
        self.code_type = code_type  # type: int
        self.code_value = code_value  # type: int
        self.instance_id = instance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProtectionModuleCodeConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.code_type is not None:
            result['CodeType'] = self.code_type
        if self.code_value is not None:
            result['CodeValue'] = self.code_value
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('CodeType') is not None:
            self.code_type = m.get('CodeType')
        if m.get('CodeValue') is not None:
            self.code_value = m.get('CodeValue')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeProtectionModuleCodeConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, code_configs=None):
        self.request_id = request_id  # type: str
        self.code_configs = code_configs  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProtectionModuleCodeConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code_configs is not None:
            result['CodeConfigs'] = self.code_configs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CodeConfigs') is not None:
            self.code_configs = m.get('CodeConfigs')
        return self


class DescribeProtectionModuleCodeConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeProtectionModuleCodeConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProtectionModuleCodeConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeProtectionModuleCodeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProtectionModuleModeRequest(TeaModel):
    def __init__(self, domain=None, defense_type=None, instance_id=None, resource_group_id=None):
        self.domain = domain  # type: str
        self.defense_type = defense_type  # type: str
        self.instance_id = instance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProtectionModuleModeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeProtectionModuleModeResponseBody(TeaModel):
    def __init__(self, learn_status=None, request_id=None, mode=None):
        self.learn_status = learn_status  # type: int
        self.request_id = request_id  # type: str
        self.mode = mode  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProtectionModuleModeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.learn_status is not None:
            result['LearnStatus'] = self.learn_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LearnStatus') is not None:
            self.learn_status = m.get('LearnStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class DescribeProtectionModuleModeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeProtectionModuleModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProtectionModuleModeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeProtectionModuleModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProtectionModuleRulesRequest(TeaModel):
    def __init__(self, page_size=None, page_number=None, domain=None, defense_type=None, query=None, lang=None,
                 instance_id=None, resource_group_id=None):
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.domain = domain  # type: str
        self.defense_type = defense_type  # type: str
        self.query = query  # type: str
        self.lang = lang  # type: str
        self.instance_id = instance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProtectionModuleRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.query is not None:
            result['Query'] = self.query
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeProtectionModuleRulesResponseBodyRules(TeaModel):
    def __init__(self, status=None, time=None, version=None, content=None, rule_id=None):
        self.status = status  # type: long
        self.time = time  # type: long
        self.version = version  # type: long
        self.content = content  # type: dict[str, any]
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProtectionModuleRulesResponseBodyRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.time is not None:
            result['Time'] = self.time
        if self.version is not None:
            result['Version'] = self.version
        if self.content is not None:
            result['Content'] = self.content
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeProtectionModuleRulesResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, rules=None):
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.rules = rules  # type: list[DescribeProtectionModuleRulesResponseBodyRules]

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeProtectionModuleRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeProtectionModuleRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        return self


class DescribeProtectionModuleRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeProtectionModuleRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProtectionModuleRulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeProtectionModuleRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProtectionModuleStatusRequest(TeaModel):
    def __init__(self, domain=None, defense_type=None, instance_id=None):
        self.domain = domain  # type: str
        self.defense_type = defense_type  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProtectionModuleStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeProtectionModuleStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, module_status=None):
        self.request_id = request_id  # type: str
        self.module_status = module_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeProtectionModuleStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.module_status is not None:
            result['ModuleStatus'] = self.module_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ModuleStatus') is not None:
            self.module_status = m.get('ModuleStatus')
        return self


class DescribeProtectionModuleStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeProtectionModuleStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeProtectionModuleStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeProtectionModuleStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWafSourceIpSegmentRequest(TeaModel):
    def __init__(self, instance_id=None, resource_group_id=None):
        self.instance_id = instance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWafSourceIpSegmentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeWafSourceIpSegmentResponseBody(TeaModel):
    def __init__(self, request_id=None, ip_v6s=None, ips=None):
        self.request_id = request_id  # type: str
        self.ip_v6s = ip_v6s  # type: str
        self.ips = ips  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWafSourceIpSegmentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ip_v6s is not None:
            result['IpV6s'] = self.ip_v6s
        if self.ips is not None:
            result['Ips'] = self.ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IpV6s') is not None:
            self.ip_v6s = m.get('IpV6s')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        return self


class DescribeWafSourceIpSegmentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeWafSourceIpSegmentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWafSourceIpSegmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDomainRequest(TeaModel):
    def __init__(self, instance_id=None, domain=None, source_ips=None, load_balancing=None, http_port=None,
                 https_port=None, http_2port=None, https_redirect=None, http_to_user_ip=None, is_access_product=None,
                 log_headers=None, cluster_type=None, connection_time=None, read_time=None, write_time=None, access_type=None,
                 cloud_native_instances=None, ip_follow_status=None):
        self.instance_id = instance_id  # type: str
        self.domain = domain  # type: str
        self.source_ips = source_ips  # type: str
        self.load_balancing = load_balancing  # type: int
        self.http_port = http_port  # type: str
        self.https_port = https_port  # type: str
        self.http_2port = http_2port  # type: str
        self.https_redirect = https_redirect  # type: int
        self.http_to_user_ip = http_to_user_ip  # type: int
        self.is_access_product = is_access_product  # type: int
        self.log_headers = log_headers  # type: str
        self.cluster_type = cluster_type  # type: int
        self.connection_time = connection_time  # type: int
        self.read_time = read_time  # type: int
        self.write_time = write_time  # type: int
        self.access_type = access_type  # type: str
        self.cloud_native_instances = cloud_native_instances  # type: str
        self.ip_follow_status = ip_follow_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.source_ips is not None:
            result['SourceIps'] = self.source_ips
        if self.load_balancing is not None:
            result['LoadBalancing'] = self.load_balancing
        if self.http_port is not None:
            result['HttpPort'] = self.http_port
        if self.https_port is not None:
            result['HttpsPort'] = self.https_port
        if self.http_2port is not None:
            result['Http2Port'] = self.http_2port
        if self.https_redirect is not None:
            result['HttpsRedirect'] = self.https_redirect
        if self.http_to_user_ip is not None:
            result['HttpToUserIp'] = self.http_to_user_ip
        if self.is_access_product is not None:
            result['IsAccessProduct'] = self.is_access_product
        if self.log_headers is not None:
            result['LogHeaders'] = self.log_headers
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.connection_time is not None:
            result['ConnectionTime'] = self.connection_time
        if self.read_time is not None:
            result['ReadTime'] = self.read_time
        if self.write_time is not None:
            result['WriteTime'] = self.write_time
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.cloud_native_instances is not None:
            result['CloudNativeInstances'] = self.cloud_native_instances
        if self.ip_follow_status is not None:
            result['IpFollowStatus'] = self.ip_follow_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('SourceIps') is not None:
            self.source_ips = m.get('SourceIps')
        if m.get('LoadBalancing') is not None:
            self.load_balancing = m.get('LoadBalancing')
        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')
        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')
        if m.get('Http2Port') is not None:
            self.http_2port = m.get('Http2Port')
        if m.get('HttpsRedirect') is not None:
            self.https_redirect = m.get('HttpsRedirect')
        if m.get('HttpToUserIp') is not None:
            self.http_to_user_ip = m.get('HttpToUserIp')
        if m.get('IsAccessProduct') is not None:
            self.is_access_product = m.get('IsAccessProduct')
        if m.get('LogHeaders') is not None:
            self.log_headers = m.get('LogHeaders')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ConnectionTime') is not None:
            self.connection_time = m.get('ConnectionTime')
        if m.get('ReadTime') is not None:
            self.read_time = m.get('ReadTime')
        if m.get('WriteTime') is not None:
            self.write_time = m.get('WriteTime')
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('CloudNativeInstances') is not None:
            self.cloud_native_instances = m.get('CloudNativeInstances')
        if m.get('IpFollowStatus') is not None:
            self.ip_follow_status = m.get('IpFollowStatus')
        return self


class ModifyDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDomainResponseBody, self).to_map()
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


class ModifyDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDomainIpv6StatusRequest(TeaModel):
    def __init__(self, instance_id=None, domain=None, enabled=None):
        self.instance_id = instance_id  # type: str
        self.domain = domain  # type: str
        self.enabled = enabled  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDomainIpv6StatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class ModifyDomainIpv6StatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDomainIpv6StatusResponseBody, self).to_map()
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


class ModifyDomainIpv6StatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDomainIpv6StatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDomainIpv6StatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDomainIpv6StatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLogRetrievalStatusRequest(TeaModel):
    def __init__(self, instance_id=None, domain=None, enabled=None):
        self.instance_id = instance_id  # type: str
        self.domain = domain  # type: str
        self.enabled = enabled  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyLogRetrievalStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class ModifyLogRetrievalStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyLogRetrievalStatusResponseBody, self).to_map()
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


class ModifyLogRetrievalStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyLogRetrievalStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyLogRetrievalStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyLogRetrievalStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLogServiceStatusRequest(TeaModel):
    def __init__(self, instance_id=None, domain=None, enabled=None):
        self.instance_id = instance_id  # type: str
        self.domain = domain  # type: str
        self.enabled = enabled  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyLogServiceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class ModifyLogServiceStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyLogServiceStatusResponseBody, self).to_map()
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


class ModifyLogServiceStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyLogServiceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyLogServiceStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyLogServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProtectionModuleModeRequest(TeaModel):
    def __init__(self, domain=None, defense_type=None, mode=None, instance_id=None):
        self.domain = domain  # type: str
        self.defense_type = defense_type  # type: str
        self.mode = mode  # type: int
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProtectionModuleModeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyProtectionModuleModeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProtectionModuleModeResponseBody, self).to_map()
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


class ModifyProtectionModuleModeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyProtectionModuleModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyProtectionModuleModeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyProtectionModuleModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProtectionModuleRuleRequest(TeaModel):
    def __init__(self, domain=None, defense_type=None, rule=None, rule_id=None, lock_version=None, instance_id=None):
        self.domain = domain  # type: str
        self.defense_type = defense_type  # type: str
        self.rule = rule  # type: str
        self.rule_id = rule_id  # type: long
        self.lock_version = lock_version  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProtectionModuleRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.rule is not None:
            result['Rule'] = self.rule
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.lock_version is not None:
            result['LockVersion'] = self.lock_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('LockVersion') is not None:
            self.lock_version = m.get('LockVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyProtectionModuleRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProtectionModuleRuleResponseBody, self).to_map()
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


class ModifyProtectionModuleRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyProtectionModuleRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyProtectionModuleRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyProtectionModuleRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProtectionModuleStatusRequest(TeaModel):
    def __init__(self, domain=None, defense_type=None, module_status=None, instance_id=None):
        self.domain = domain  # type: str
        self.defense_type = defense_type  # type: str
        self.module_status = module_status  # type: int
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProtectionModuleStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.module_status is not None:
            result['ModuleStatus'] = self.module_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('ModuleStatus') is not None:
            self.module_status = m.get('ModuleStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyProtectionModuleStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProtectionModuleStatusResponseBody, self).to_map()
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


class ModifyProtectionModuleStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyProtectionModuleStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyProtectionModuleStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyProtectionModuleStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProtectionRuleCacheStatusRequest(TeaModel):
    def __init__(self, domain=None, rule_id=None, defense_type=None, instance_id=None):
        self.domain = domain  # type: str
        self.rule_id = rule_id  # type: long
        self.defense_type = defense_type  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProtectionRuleCacheStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyProtectionRuleCacheStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProtectionRuleCacheStatusResponseBody, self).to_map()
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


class ModifyProtectionRuleCacheStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyProtectionRuleCacheStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyProtectionRuleCacheStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyProtectionRuleCacheStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProtectionRuleStatusRequest(TeaModel):
    def __init__(self, domain=None, defense_type=None, rule_id=None, rule_status=None, lock_version=None,
                 instance_id=None):
        self.domain = domain  # type: str
        self.defense_type = defense_type  # type: str
        self.rule_id = rule_id  # type: long
        self.rule_status = rule_status  # type: int
        self.lock_version = lock_version  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProtectionRuleStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.defense_type is not None:
            result['DefenseType'] = self.defense_type
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status
        if self.lock_version is not None:
            result['LockVersion'] = self.lock_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DefenseType') is not None:
            self.defense_type = m.get('DefenseType')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')
        if m.get('LockVersion') is not None:
            self.lock_version = m.get('LockVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyProtectionRuleStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProtectionRuleStatusResponseBody, self).to_map()
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


class ModifyProtectionRuleStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyProtectionRuleStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyProtectionRuleStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyProtectionRuleStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainRuleGroupRequest(TeaModel):
    def __init__(self, domains=None, rule_group_id=None, waf_version=None, instance_id=None, resource_group_id=None):
        self.domains = domains  # type: str
        self.rule_group_id = rule_group_id  # type: long
        self.waf_version = waf_version  # type: long
        self.instance_id = instance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDomainRuleGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.rule_group_id is not None:
            result['RuleGroupId'] = self.rule_group_id
        if self.waf_version is not None:
            result['WafVersion'] = self.waf_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('RuleGroupId') is not None:
            self.rule_group_id = m.get('RuleGroupId')
        if m.get('WafVersion') is not None:
            self.waf_version = m.get('WafVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class SetDomainRuleGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDomainRuleGroupResponseBody, self).to_map()
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


class SetDomainRuleGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDomainRuleGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDomainRuleGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetDomainRuleGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


