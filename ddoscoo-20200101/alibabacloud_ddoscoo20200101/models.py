# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddAutoCcBlacklistRequest(TeaModel):
    def __init__(self, blacklist=None, expire_time=None, instance_id=None):
        self.blacklist = blacklist  # type: str
        self.expire_time = expire_time  # type: int
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAutoCcBlacklistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blacklist is not None:
            result['Blacklist'] = self.blacklist
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Blacklist') is not None:
            self.blacklist = m.get('Blacklist')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class AddAutoCcBlacklistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAutoCcBlacklistResponseBody, self).to_map()
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


class AddAutoCcBlacklistResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddAutoCcBlacklistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddAutoCcBlacklistResponse, self).to_map()
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
            temp_model = AddAutoCcBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddAutoCcWhitelistRequest(TeaModel):
    def __init__(self, expire_time=None, instance_id=None, whitelist=None):
        # This parameter is deprecated.
        # 
        # > This parameter indicates the validity period of the IP address blacklist. By default, the traffic from the IP addresses that you add to the whitelist is always allowed. You do not need to set this parameter.
        self.expire_time = expire_time  # type: int
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # The configuration of the IP addresses that you want to add to the whitelist. The value is a string that consists of JSON arrays. Each element in a JSON array is a JSON struct that contains the following fields:
        # 
        # *   **src**: the IP address that you want to add. This parameter is required. Data type: string.
        self.whitelist = whitelist  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAutoCcWhitelistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class AddAutoCcWhitelistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAutoCcWhitelistResponseBody, self).to_map()
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


class AddAutoCcWhitelistResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddAutoCcWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddAutoCcWhitelistResponse, self).to_map()
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
            temp_model = AddAutoCcWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateWebCertRequest(TeaModel):
    def __init__(self, cert=None, cert_id=None, cert_identifier=None, cert_name=None, cert_region=None, domain=None,
                 key=None, resource_group_id=None):
        # The public key of the certificate that you want to associate. This parameter must be used together with **CertName** and **Key**.
        # 
        # > If you specify **CertName**, **Cert**, and **Key**, you do not need to specify **CertId**.
        self.cert = cert  # type: str
        # The ID of the certificate that you want to associate. If the certificate that you want to associate has been issued in Certificate Management Service, you can specify the certificate ID to associate the certificate.
        # 
        # > If you specify the certificate ID, you do not need to specify a value for the **CertName**, **Cert**, and **Key** parameters.
        self.cert_id = cert_id  # type: int
        self.cert_identifier = cert_identifier  # type: str
        # The name of the certificate that you want to associate. This parameter must be used together with the **Cert** and **Key** parameters.
        # 
        # > If you specify a value for the **CertName**, **Cert**, and **Key** parameters, you do not need to specify a value for the **CertId** parameter.
        self.cert_name = cert_name  # type: str
        self.cert_region = cert_region  # type: str
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The private key of the certificate that you want to associate. This parameter must be used together with **CertName** and **Cert**.
        # 
        # > If you specify **CertName**, **Cert**, and **Key**, you do not need to specify **CertId**.
        self.key = key  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateWebCertRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_region is not None:
            result['CertRegion'] = self.cert_region
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.key is not None:
            result['Key'] = self.key
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertRegion') is not None:
            self.cert_region = m.get('CertRegion')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class AssociateWebCertResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateWebCertResponseBody, self).to_map()
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


class AssociateWebCertResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociateWebCertResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateWebCertResponse, self).to_map()
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
            temp_model = AssociateWebCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachSceneDefenseObjectRequest(TeaModel):
    def __init__(self, object_type=None, objects=None, policy_id=None):
        # The type of the object. Set the value to **Domain**, which indicates a domain name.
        self.object_type = object_type  # type: str
        # The object that you want to add to the policy. Separate multiple objects with commas (,).
        self.objects = objects  # type: str
        # The ID of the policy.
        # 
        # > You can call the [DescribeSceneDefensePolicies](~~159382~~) operation to query the IDs of all policies.
        self.policy_id = policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachSceneDefenseObjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.objects is not None:
            result['Objects'] = self.objects
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Objects') is not None:
            self.objects = m.get('Objects')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class AttachSceneDefenseObjectResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachSceneDefenseObjectResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachSceneDefenseObjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachSceneDefenseObjectResponse, self).to_map()
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
            temp_model = AttachSceneDefenseObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigL7RsPolicyRequest(TeaModel):
    def __init__(self, domain=None, policy=None, resource_group_id=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query the domain names for which forwarding rules are configured.
        self.domain = domain  # type: str
        # The back-to-origin policy. The value is a string that consists of a JSON struct. The JSON struct contains the following fields:
        # 
        # *   **ProxyMode**: The load balancing algorithm for back-to-origin traffic. This field is required and must be a string. Valid values:
        # 
        #     *   **ip_hash**: the IP hash algorithm. This algorithm is used to redirect the requests from the same IP address to the same origin server.
        #     *   **rr**: the round-robin algorithm. This algorithm is used to redirect requests to origin servers in turn. If you use this algorithm, you can specify a weight for each server based on server performance.
        #     *   **least_time**: the least response time algorithm. This algorithm is used to minimize the latency when requests are forwarded from Anti-DDoS Pro or Anti-DDoS Premium instances to origin servers based on the intelligent DNS resolution feature.
        # 
        # *   **Attributes**: the parameters for back-to-origin. This field is optional and must be a JSON array. Each element in the array contains the following fields:
        # 
        #     *   **RealServer**: the address of the origin server. This field is optional and must be a string.
        # 
        #     *   **Attribute**: the parameter for back-to-origin. This field is optional and must be a JSON object. The value contains the following field:
        # 
        #         *   **Weight**: the weight of the server. This field is optional and must be an integer. This field takes effect only when **ProxyMode** is set to **rr**. Valid values: **1** to **100**. Default value: **100**. An origin server with a higher weight receives more requests.
        self.policy = policy  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](~~94485~~).
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigL7RsPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ConfigL7RsPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigL7RsPolicyResponseBody, self).to_map()
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


class ConfigL7RsPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigL7RsPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigL7RsPolicyResponse, self).to_map()
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
            temp_model = ConfigL7RsPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigLayer4RealLimitRequest(TeaModel):
    def __init__(self, instance_id=None, limit_value=None):
        # The ID of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # Specifies the threshold of the clean bandwidth. Valid values: 0 to 15360. The value 0 indicates that rate limiting is never triggered. Unit: Mbit/s
        self.limit_value = limit_value  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigLayer4RealLimitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.limit_value is not None:
            result['LimitValue'] = self.limit_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LimitValue') is not None:
            self.limit_value = m.get('LimitValue')
        return self


class ConfigLayer4RealLimitResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigLayer4RealLimitResponseBody, self).to_map()
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


class ConfigLayer4RealLimitResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigLayer4RealLimitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigLayer4RealLimitResponse, self).to_map()
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
            temp_model = ConfigLayer4RealLimitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigLayer4RemarkRequest(TeaModel):
    def __init__(self, listeners=None):
        # The port forwarding rule that you want to manage.
        # 
        # This parameter is a string that consists of JSON arrays. Each element in a JSON array indicates a port forwarding rule. You can perform this operation only on one port forwarding rule at a time.
        # 
        # > You can call the [DescribeNetworkRules](~~157484~~) to query existing port forwarding rules.
        # 
        # Each port forwarding rule contains the following fields:
        # 
        # *   **InstanceId**: the ID of the instance. This field is required and must be of the STRING type.
        # *   **Protocol**: the forwarding protocol. This field is required and must be of the STRING type. Valid values: **tcp** and **udp**.
        # *   **FrontendPort**: the forwarding port. This field is required and must be of the INTEGER type.
        # *   **Remark**: the remarks of the port forwarding rule. This field is required and must be of the STRING type. The value can contain letters, digits, and some special characters, such as `, . + - * / _`. The value can be up to 200 characters in length.
        self.listeners = listeners  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigLayer4RemarkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        return self


class ConfigLayer4RemarkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigLayer4RemarkResponseBody, self).to_map()
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


class ConfigLayer4RemarkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigLayer4RemarkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigLayer4RemarkResponse, self).to_map()
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
            temp_model = ConfigLayer4RemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigLayer4RuleBakModeRequest(TeaModel):
    def __init__(self, bak_mode=None, listeners=None):
        # The mode that you want to use to forward service traffic. Valid values:
        # 
        # *   **0**: the default mode. In this mode, Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the origin IP address that you specified when you created the port forwarding rule. You can call the [CreateNetworkRules](~~157482~~) operation to create a port forwarding rule.
        # *   **1**: the origin redundancy mode. In this mode, Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the primary or secondary origin servers. You can call the [ConfigLayer4RulePolicy](~~312684~~) operation to configure IP addresses.
        self.bak_mode = bak_mode  # type: str
        # The port forwarding rule that you want to manage.
        # 
        # This parameter is a string that consists of JSON arrays. Each element in a JSON array indicates a port forwarding rule. You can perform this operation only on one port forwarding rule at a time.
        # 
        # > You can call the [DescribeNetworkRules](~~157484~~) to query existing port forwarding rules.
        # 
        # Each port forwarding rule contains the following fields:
        # 
        # *   **InstanceId**: the ID of the instance. This field is required and must be of the STRING type.
        # *   **Protocol**: the forwarding protocol. This field is required and must be of the STRING type. Valid values: **tcp** and **udp**.
        # *   **FrontendPort**: the forwarding port. This field is required and must be of the INTEGER type.
        self.listeners = listeners  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigLayer4RuleBakModeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bak_mode is not None:
            result['BakMode'] = self.bak_mode
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BakMode') is not None:
            self.bak_mode = m.get('BakMode')
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        return self


class ConfigLayer4RuleBakModeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigLayer4RuleBakModeResponseBody, self).to_map()
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


class ConfigLayer4RuleBakModeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigLayer4RuleBakModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigLayer4RuleBakModeResponse, self).to_map()
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
            temp_model = ConfigLayer4RuleBakModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigLayer4RulePolicyRequest(TeaModel):
    def __init__(self, listeners=None):
        # The port forwarding rule that you want to manage.
        # 
        # This parameter is a string that consists of JSON arrays. Each element in a JSON array indicates a port forwarding rule. You can perform this operation only on one port forwarding rule at a time.
        # 
        # > You can call the [DescribeNetworkRules](~~157484~~) to query existing port forwarding rules.
        # 
        # Each port forwarding rule contains the following fields:
        # 
        # *   **InstanceId**: the ID of the instance. This field is required and must be of the STRING type.
        # 
        # *   **Protocol**: the forwarding protocol. This field is required and must be of the STRING type. Valid values: **tcp** and **udp**.
        # 
        # *   **FrontendPort**: the forwarding port. This field is required and must be of the INTEGER type.
        # 
        # *   **BackendPort**: the port of the origin server. This field is required and must be of the INTEGER type.
        # 
        # *   **PriRealServers**: the IP addresses of the primary origin server. This field is required and must be a JSON array. Each element in a JSON array indicates an IP address of the primary origin server. You can configure a maximum of 20 IP addresses.
        # 
        #     Each element in the JSON array contains the following field:
        # 
        #     *   **RealServer**: the IP address of the primary origin server. This field is required and must be of the STRING type.
        # 
        # *   **SecRealServers**: the IP addresses of the secondary origin server. This field is required and must be a JSON array. Each element in a JSON array indicates an IP address of the secondary origin server. You can configure a maximum of 20 IP addresses.
        # 
        #     Each element in the JSON array contains the following field:
        # 
        #     *   **RealServer**: the IP address of the secondary origin server. This field is required and must be of the STRING type.
        # 
        # *   **CurrentRsIndex**: the origin server that you want to use to receive service traffic. This field is required and must be of the INTEGER type. Valid values:
        # 
        #     *   **1**: the primary origin server, which indicates that Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the primary origin server.
        #     *   **2**: the secondary origin server, which indicates that Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the secondary origin server.
        self.listeners = listeners  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigLayer4RulePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        return self


class ConfigLayer4RulePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigLayer4RulePolicyResponseBody, self).to_map()
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


class ConfigLayer4RulePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigLayer4RulePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigLayer4RulePolicyResponse, self).to_map()
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
            temp_model = ConfigLayer4RulePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigNetworkRegionBlockRequest(TeaModel):
    def __init__(self, config=None, instance_id=None):
        # The details of the configurations of blocked locations. This parameter is a JSON string. The value consists of the following fields:
        # 
        # *   **RegionBlockSwitch**: the status of the Location Blacklist policy. This field is required and must be of the string type. Valid values:
        # 
        #     *   **on**: enables the policy.
        #     *   **off**: disables the policy.
        # 
        # *   **Countries**: the codes of the countries or areas from which you want to block requests. This field is optional and must be of the array type.
        # 
        #     **\
        # 
        #     **Note**For more information, see the **Codes of countries and areas** section of the [Codes of administrative regions in China and codes of countries and areas](~~167926~~) topic.
        # 
        #     For example, `[1,2]` specifies China and Australia.
        # 
        # *   **Provinces**: the codes of the administrative regions in China from which you want to block requests. This field is optional and must be of the array type.
        # 
        #     **\
        # 
        #     **Note**For more information, see the **Codes of administrative regions in China** section of the [Codes of administrative regions in China and codes of countries and areas](~~167926~~) topic.
        # 
        #     For example, `[11,12]` specifies Beijing and Tianjin.
        self.config = config  # type: str
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigNetworkRegionBlockRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ConfigNetworkRegionBlockResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigNetworkRegionBlockResponseBody, self).to_map()
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


class ConfigNetworkRegionBlockResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigNetworkRegionBlockResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigNetworkRegionBlockResponse, self).to_map()
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
            temp_model = ConfigNetworkRegionBlockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigNetworkRulesRequest(TeaModel):
    def __init__(self, network_rules=None):
        # The details of the port forwarding rule. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **InstanceId**: the ID of the instance. This field is required and must be of the STRING type.
        # *   **Protocol**: the forwarding protocol. This field is required and must be of the STRING type. Valid values: **tcp** and **udp**.
        # *   **FrontendPort**: the forwarding port. This field is required and must be of the INTEGER type.
        # *   **BackendPort**: the port of the origin server. This field is required and must be of the INTEGER type.
        # *   **RealServers**: the IP addresses of the origin server. This field is required and must be a JSON array. You can specify up to 20 IP addresses.
        # 
        # > You can modify only the value of **RealServers** when you modify a port forwarding rule.
        self.network_rules = network_rules  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigNetworkRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkRules') is not None:
            self.network_rules = m.get('NetworkRules')
        return self


class ConfigNetworkRulesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigNetworkRulesResponseBody, self).to_map()
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


class ConfigNetworkRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigNetworkRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigNetworkRulesResponse, self).to_map()
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
            temp_model = ConfigNetworkRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigUdpReflectRequest(TeaModel):
    def __init__(self, config=None, instance_id=None, region_id=None):
        # The configuration of the filtering policy for UDP reflection attacks.
        # 
        # The value is a string that consists of a JSON struct. The JSON struct contains the following field:
        # 
        # *   **UdpSports**: the source ports of the UDP traffic that you want to block. This field is required and must be of the ARRAY type. Example: `[17,19]`.
        # 
        #     We recommend that you block the following source ports of UDP traffic:
        # 
        #     *   UDP 17: QOTD reflection attacks
        #     *   UDP 19: CharGEN reflection attacks
        #     *   UDP 69: TFTP reflection attacks
        #     *   UDP 111: Portmap reflection attacks
        #     *   UDP 123: NTP reflection attacks
        #     *   UDP 137: NetBIOS reflection attacks
        #     *   UDP 161: SNMPv2 reflection attacks
        #     *   UDP 389: CLDAP reflection attacks
        #     *   UDP 1194: OpenVPN reflection attacks
        #     *   UDP 1900: SSDP reflection attacks
        #     *   UDP 3389: RDP reflection attacks
        #     *   UDP 11211: memcached reflection attacks
        self.config = config  # type: str
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # The region ID of the instance. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland, which indicates Anti-DDoS Pro instances. This is the default value.
        # *   **ap-southeast-1**: outside the Chinese mainland, which indicates Anti-DDoS Premium instances.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigUdpReflectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConfigUdpReflectResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigUdpReflectResponseBody, self).to_map()
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


class ConfigUdpReflectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigUdpReflectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigUdpReflectResponse, self).to_map()
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
            temp_model = ConfigUdpReflectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigWebCCTemplateRequest(TeaModel):
    def __init__(self, domain=None, resource_group_id=None, template=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The mode of the Frequency Control policy. Valid values:
        # 
        # *   **default**: Normal
        # *   **gf_under_attack**: Emergency
        # *   **gf_sos_verify**: Strict
        # *   **gf_sos_enhance**: Super Strict
        self.template = template  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigWebCCTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class ConfigWebCCTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigWebCCTemplateResponseBody, self).to_map()
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


class ConfigWebCCTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigWebCCTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigWebCCTemplateResponse, self).to_map()
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
            temp_model = ConfigWebCCTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigWebIpSetRequest(TeaModel):
    def __init__(self, black_list=None, domain=None, resource_group_id=None, white_list=None):
        # IP address N or CIDR block N that you want to add to the blacklist. The maximum value of N is 200. You can add up to 200 IP addresses or CIDR blocks to the blacklist.
        self.black_list = black_list  # type: list[str]
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # IP address N or CIDR block N that you want to add to the whitelist. The maximum value of N is 200. You can add up to 200 IP addresses or CIDR blocks to the whitelist.
        self.white_list = white_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigWebIpSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_list is not None:
            result['BlackList'] = self.black_list
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class ConfigWebIpSetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigWebIpSetResponseBody, self).to_map()
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


class ConfigWebIpSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigWebIpSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigWebIpSetResponse, self).to_map()
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
            temp_model = ConfigWebIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAsyncTaskRequest(TeaModel):
    def __init__(self, resource_group_id=None, task_params=None, task_type=None):
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The details of the asynchronous export task. The value is a JSON string. The field in the value varies with **TaskType**.
        # 
        # If **TaskType** is set to **1**, **3**, **4**, **5**, or **6**, the following filed is returned:
        # 
        # *   **instanceId**: the ID of the instance. This field is required and must be of the STRING type.
        # 
        # If **TaskType** is set to **2**, the following field is returned:
        # 
        # *   **domain**: the domain name of the website, which must be of the STRING type. If you do not specify this field, the forwarding rules of all websites are exported.
        self.task_params = task_params  # type: str
        # The type of the asynchronous export task that you want to create. Valid values:
        # 
        # *   **1**: the task to export the port forwarding rules of an instance
        # *   **2**: the task to export the forwarding rules of a website protected by an instance
        # *   **3**: the task to export the session persistence and health check settings of an instance
        # *   **4**: the task to export the anti-DDoS mitigation policies of an instance
        # *   **5**: the task to download the blacklist for destination IP addresses of an instance
        # *   **6**: the task to download the whitelist for destination IP addresses of an instance
        self.task_type = task_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAsyncTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class CreateAsyncTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAsyncTaskResponseBody, self).to_map()
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


class CreateAsyncTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAsyncTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAsyncTaskResponse, self).to_map()
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
            temp_model = CreateAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainResourceRequestProxyTypes(TeaModel):
    def __init__(self, proxy_ports=None, proxy_type=None):
        # An array that consists of port numbers.
        self.proxy_ports = proxy_ports  # type: list[int]
        # The type of the protocol. Valid values:
        # 
        # *   **http**\
        # *   **https**\
        # *   **websocket**\
        # *   **websockets**\
        self.proxy_type = proxy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDomainResourceRequestProxyTypes, self).to_map()
        if _map is not None:
            return _map

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


class CreateDomainResourceRequest(TeaModel):
    def __init__(self, domain=None, https_ext=None, instance_ids=None, proxy_types=None, real_servers=None,
                 rs_type=None):
        # The domain name of the website that you want to add to the Anti-DDoS Pro or Anti-DDoS Premium instance.
        self.domain = domain  # type: str
        # The advanced HTTPS settings. This parameter takes effect only when the value of the **ProxyType** parameter includes **https**. The value is a string that consists of a JSON struct. The JSON struct contains the following fields:
        # 
        # *   **Http2https**: specifies whether to turn on Enforce HTTPS Routing. This field is optional and must be an integer. Valid values: **0** and **1**. The value 0 indicates that Enforce HTTPS Routing is turned off. The value 1 indicates that Enforce HTTPS Routing is turned on. The default value is 0.
        # 
        #     If your website supports both HTTP and HTTPS, this feature meets your business requirements. If you enable this feature, all HTTP requests to access the website are redirected to HTTPS requests on the standard port 443.
        # 
        # *   **Https2http**: specifies whether to turn on Enable HTTP. This field is optional and must be an integer. Valid values: **0** and **1**. The value 0 indicates that Enable HTTP is turned off. The value 1 indicates that Enable HTTP is turned on. The default value is 0.
        # 
        #     If your website does not support HTTPS, this feature meets your business requirements If this feature is enabled, all HTTPS requests are redirected to HTTP requests and forwarded to origin servers. This feature can redirect WebSockets requests to WebSocket requests. Requests are redirected over the standard port 80.
        # 
        # *   **Http2**: specifies whether to turn on Enable HTTP/2. This field is optional. Data type: integer. Valid values: **0** and **1**. The value 0 indicates that Enable HTTP/2 is turned off. The value 1 indicates that Enable HTTP/2 is turned on. The default value is 0.
        # 
        #     After you turn on the switch, HTTP/2 is used.
        self.https_ext = https_ext  # type: str
        # An array consisting of the IDs of instances that you want to associate.
        self.instance_ids = instance_ids  # type: list[str]
        # An array that consists of the details of the protocol type and port number.
        self.proxy_types = proxy_types  # type: list[CreateDomainResourceRequestProxyTypes]
        # An array that consists of the addresses of origin servers.
        self.real_servers = real_servers  # type: list[str]
        # The address type of the origin server. Valid values:
        # 
        # *   **0**: IP address
        # 
        # *   **1**: domain name
        # 
        #     If you deploy proxies, such as a Web Application Firewall (WAF) instance, between the origin server and the Anti-DDoS Pro or Anti-DDoS Premium instance, set the value to 1. If you use the domain name, you must enter the address of the proxy, such as the CNAME of WAF.
        self.rs_type = rs_type  # type: int

    def validate(self):
        if self.proxy_types:
            for k in self.proxy_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateDomainResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.https_ext is not None:
            result['HttpsExt'] = self.https_ext
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        result['ProxyTypes'] = []
        if self.proxy_types is not None:
            for k in self.proxy_types:
                result['ProxyTypes'].append(k.to_map() if k else None)
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('HttpsExt') is not None:
            self.https_ext = m.get('HttpsExt')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        self.proxy_types = []
        if m.get('ProxyTypes') is not None:
            for k in m.get('ProxyTypes'):
                temp_model = CreateDomainResourceRequestProxyTypes()
                self.proxy_types.append(temp_model.from_map(k))
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        return self


class CreateDomainResourceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDomainResourceResponseBody, self).to_map()
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


class CreateDomainResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDomainResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDomainResourceResponse, self).to_map()
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
            temp_model = CreateDomainResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNetworkRulesRequest(TeaModel):
    def __init__(self, network_rules=None):
        # The details of the port forwarding rule. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **InstanceId**: the ID of the instance. This field is required and must be of the STRING type.
        # *   **Protocol**: the forwarding protocol. This field is required and must be of the STRING type. Valid values: **tcp** and **udp**.
        # *   **FrontendPort**: the forwarding port. This field is required and must be of the INTEGER type.
        # *   **BackendPort**: the port of the origin server. This field is required and must be of the INTEGER type.
        # *   **RealServers**: the IP addresses of the origin server. This field is required and must be a JSON array. You can specify up to 20 IP addresses.
        self.network_rules = network_rules  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNetworkRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkRules') is not None:
            self.network_rules = m.get('NetworkRules')
        return self


class CreateNetworkRulesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNetworkRulesResponseBody, self).to_map()
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


class CreateNetworkRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateNetworkRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNetworkRulesResponse, self).to_map()
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
            temp_model = CreateNetworkRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePortRequest(TeaModel):
    def __init__(self, backend_port=None, frontend_port=None, frontend_protocol=None, instance_id=None,
                 real_servers=None):
        # The port of the origin server. Valid values: **0** to **65535**.
        self.backend_port = backend_port  # type: str
        # The forwarding port. Valid values: **0** to **65535**.
        self.frontend_port = frontend_port  # type: str
        # The type of the protocol. Valid values:
        # 
        # *   **tcp**\
        # *   **udp**\
        self.frontend_protocol = frontend_protocol  # type: str
        # The ID of the Anti-DDoS Pro or Anti-DDoS Premium instance to which the port forwarding rule belongs.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # An array that consists of the IP addresses of origin servers.
        self.real_servers = real_servers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePortRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_port is not None:
            result['BackendPort'] = self.backend_port
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.frontend_protocol is not None:
            result['FrontendProtocol'] = self.frontend_protocol
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackendPort') is not None:
            self.backend_port = m.get('BackendPort')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('FrontendProtocol') is not None:
            self.frontend_protocol = m.get('FrontendProtocol')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        return self


class CreatePortResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePortResponseBody, self).to_map()
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


class CreatePortResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePortResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePortResponse, self).to_map()
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
            temp_model = CreatePortResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSceneDefensePolicyRequest(TeaModel):
    def __init__(self, end_time=None, name=None, start_time=None, template=None):
        # The end time of the policy. This value is a UNIX timestamp. Units: milliseconds.
        self.end_time = end_time  # type: long
        # The name of the policy.
        self.name = name  # type: str
        # The start time of the policy. This value is a UNIX timestamp. Units: milliseconds.
        self.start_time = start_time  # type: long
        # The template of the policy. Valid values:
        # 
        # *   **promotion**: important activity
        # *   **bypass**: all traffic forwarded
        self.template = template  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSceneDefensePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.name is not None:
            result['Name'] = self.name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class CreateSceneDefensePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSceneDefensePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSceneDefensePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSceneDefensePolicyResponse, self).to_map()
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
            temp_model = CreateSceneDefensePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSchedulerRuleRequest(TeaModel):
    def __init__(self, param=None, resource_group_id=None, rule_name=None, rule_type=None, rules=None):
        # The details of the CDN interaction rule. This parameter is a JSON string. The following list describes the fields in the value of the parameter:
        # 
        # *   **ParamType**: the type of the scheduling rule. This field is required and must be of the string type. Set the value to **cdn**. This indicates that you want to modify a CDN interaction rule.
        # 
        # *   **ParamData**: the values of parameters that you want to modify for the CDN interaction rule. This field is required and must be of the map type. ParamData contains the following parameters:
        # 
        #     *   **Domain**: the accelerated domain in CDN. This parameter is required and must be of the string type.
        #     *   **Cname**: the CNAME that is assigned to the accelerated domain. This parameter is required and must be of the string type.
        #     *   **AccessQps**: the queries per second (QPS) threshold that is used to switch service traffic to Anti-DDoS Pro or Anti-DDoS Premium. This parameter is required and must be of the integer type.
        #     *   **UpstreamQps**: the QPS threshold that is used to switch service traffic to CDN. This parameter is optional and must be of the integer type.
        self.param = param  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The name of the rule.
        self.rule_name = rule_name  # type: str
        # The type of the custom defense rule. Valid values:
        # 
        # *   **2**: tiered protection
        # *   **3**: network acceleration
        # *   **5**: CDN interaction
        # *   **6**: cloud service interaction
        self.rule_type = rule_type  # type: int
        # The details of the scheduling rule. This parameter is a JSON string. The following list describes the fields in the value of the parameter:
        # 
        # *   **Type**: the address type of the interaction resource that you want to use in the scheduling rule. This field is required and must be of the string type. Valid values:
        # 
        #     *   **A**: IP address
        #     *   **CNAME**: domain name
        # 
        # *   **Value**: the address of the interaction resource that you want to use in the scheduling rule. This field is required and must be of the string type.
        # 
        # *   **Priority**: the priority of the scheduling rule. This field is required and must be of the integer type. Valid values: **0** to **100**. A larger value indicates a higher priority.
        # 
        # *   **ValueType**: the type of the interaction resource that you want to use in the scheduling rule. This field is required and must be of the integer type. Valid values:
        # 
        #     *   **1**: the IP address of the Anti-DDoS Pro or Anti-DDoS Premium instance
        #     *   **2**: the IP address of the interaction resource in the tiered protection scenario
        #     *   **3**: the IP address that is used to accelerate access in the network acceleration scenario
        #     *   **5**: the domain name that is configured in Alibaba Cloud CDN (CDN) in the CDN interaction scenario
        #     *   **6** the IP address of the interaction resource in the cloud service interaction scenario
        # 
        # *   **RegionId**: the region where the interaction resource is deployed. This parameter must be specified when **ValueType** is set to **2**. The value must be of the string type.
        self.rules = rules  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSchedulerRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param is not None:
            result['Param'] = self.param
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.rules is not None:
            result['Rules'] = self.rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        return self


class CreateSchedulerRuleResponseBody(TeaModel):
    def __init__(self, cname=None, request_id=None, rule_name=None):
        # The CNAME that is assigned by Sec-Traffic Manager for the scheduling rule.
        # 
        # > To enable the scheduling rule, you must map the domain name of the service to the CNAME.
        self.cname = cname  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The name of the rule.
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSchedulerRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class CreateSchedulerRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSchedulerRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSchedulerRuleResponse, self).to_map()
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
            temp_model = CreateSchedulerRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTagResourcesRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag to add.
        self.key = key  # type: str
        # The value of the tag to add.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTagResourcesRequestTags, self).to_map()
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


class CreateTagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_group_id=None, resource_ids=None, resource_type=None, tags=None):
        # The region ID of the instance. Set the value to **cn-hangzhou**, which indicates an Anti-DDoS Pro instance in the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # An array consisting of the IDs of the Anti-DDoS Pro instances to which you want to add the tag.
        self.resource_ids = resource_ids  # type: list[str]
        # The type of the resource to which the tag belongs. Set the value to **INSTANCE**, which indicates an Anti-DDoS Pro instance.
        self.resource_type = resource_type  # type: str
        # An array that consists of the tags to add.
        self.tags = tags  # type: list[CreateTagResourcesRequestTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateTagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateTagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTagResourcesResponseBody, self).to_map()
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


class CreateTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTagResourcesResponse, self).to_map()
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
            temp_model = CreateTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWebCCRuleRequest(TeaModel):
    def __init__(self, act=None, count=None, domain=None, interval=None, mode=None, name=None, resource_group_id=None,
                 ttl=None, uri=None):
        self.act = act  # type: str
        self.count = count  # type: int
        self.domain = domain  # type: str
        self.interval = interval  # type: int
        self.mode = mode  # type: str
        self.name = name  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.ttl = ttl  # type: int
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWebCCRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.act is not None:
            result['Act'] = self.act
        if self.count is not None:
            result['Count'] = self.count
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CreateWebCCRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWebCCRuleResponseBody, self).to_map()
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


class CreateWebCCRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateWebCCRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateWebCCRuleResponse, self).to_map()
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
            temp_model = CreateWebCCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWebRuleRequest(TeaModel):
    def __init__(self, defense_id=None, domain=None, https_ext=None, instance_ids=None, resource_group_id=None,
                 rs_type=None, rules=None):
        # The ID of the associated defense. This parameter applies to scenarios in which other cloud services, such as Object Storage Service (OSS), are integrated with Anti-DDoS Pro or Anti-DDoS Premium.
        # 
        # > This parameter is in internal preview. Do not use this parameter.
        # 
        # For example, if you integrate OSS with Anti-DDoS Pro or Anti-DDoS Premium, Anti-DDoS Pro or Anti-DDoS Premium allocates an IP address pool for the OSS production account. Each IP address corresponds to a unique defense ID. A defense ID is a CNAME, which is automatically resolved to the IP address of the required Anti-DDoS Pro or Anti-DDoS Premium instance. A defense ID can be resolved to the same IP address to facilitate scheduling.
        # 
        # > You can specify only one of the following parameters: **InstanceIds** and **DefenseId**.
        self.defense_id = defense_id  # type: str
        # The domain name of the website that you want to add to the instance.
        self.domain = domain  # type: str
        # The advanced HTTPS settings. This parameter takes effect only when the value of the **ProxyType** parameter includes **https**. The value is a string that consists of a JSON struct. The JSON struct contains the following fields:
        # 
        # *   **Http2https**: specifies whether to turn on Enforce HTTPS Routing. This field is optional and must be an integer. Valid values: **0** and **1**. The value 0 indicates that Enforce HTTPS Routing is turned off. The value 1 indicates that Enforce HTTPS Routing is turned on. The default value is 0.
        # 
        #     If your website supports both HTTP and HTTPS, this feature meets your business requirements. If you enable this feature, all HTTP requests to access the website are redirected to HTTPS requests on the standard port 443.
        # 
        # *   **Https2http**: specifies whether to turn on Enable HTTP. This field is optional and must be an integer. Valid values: **0** and **1**. The value 0 indicates that Enable HTTP is turned off. The value 1 indicates that Enable HTTP is turned on. The default value is 0.
        # 
        #     If your website does not support HTTPS, this feature meets your business requirements If this feature is enabled, all HTTPS requests are redirected to HTTP requests and forwarded to origin servers. This feature can redirect WebSockets requests to WebSocket requests. Requests are redirected over the standard port 80.
        # 
        # *   **Http2**: specifies whether to turn on Enable HTTP/2. This field is optional and must be an integer. Valid values: **0** and **1**. The value 0 indicates that Enable HTTP/2 is turned off. The value 1 indicates that Enable HTTP/2 is turned on. The default value is 0.
        # 
        #     After you turn on Enable HTTP/2, the protocol type is HTTP/2.
        self.https_ext = https_ext  # type: str
        # An array consisting of the IDs of instances that you want to associate.
        self.instance_ids = instance_ids  # type: list[str]
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](~~94485~~).
        self.resource_group_id = resource_group_id  # type: str
        # The address type of the origin server. Valid values:
        # 
        # *   **0**: IP address
        # *   **1**: domain name The domain name of the origin server is returned if you deploy proxies, such as Web Application Firewall (WAF), between the origin server and the instance. In this case, the address of the proxy, such as the CNAME provided by WAF, is returned.
        self.rs_type = rs_type  # type: int
        # The details of the forwarding rule. The value is a string that consists of JSON arrays. Each element in a JSON array is a JSON struct that contains the following fields:
        # 
        # *   **ProxyRules**: the information about the origin server. The information includes the port number and IP address. This field is required and must be a JSON array. Each element in a JSON array is a JSON struct that contains the following fields:
        # 
        #     *   **ProxyPort**: the port number. This field is required and must be an integer.
        #     *   **RealServers**: the IP address. This field is required and must be a string array.
        # 
        # *   **ProxyType**: the protocol type. This field is required and must be a string. Valid values: **http**, **https**, **websocket**, and **websockets**.
        self.rules = rules  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWebRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_id is not None:
            result['DefenseId'] = self.defense_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.https_ext is not None:
            result['HttpsExt'] = self.https_ext
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.rules is not None:
            result['Rules'] = self.rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefenseId') is not None:
            self.defense_id = m.get('DefenseId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('HttpsExt') is not None:
            self.https_ext = m.get('HttpsExt')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        return self


class CreateWebRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWebRuleResponseBody, self).to_map()
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


class CreateWebRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateWebRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateWebRuleResponse, self).to_map()
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
            temp_model = CreateWebRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAsyncTaskRequest(TeaModel):
    def __init__(self, resource_group_id=None, task_id=None):
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the task that you want to delete.
        # 
        # > You can call the [DescribeAsyncTasks](~~159405~~) operation to query the IDs of all asynchronous export tasks.
        self.task_id = task_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAsyncTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteAsyncTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAsyncTaskResponseBody, self).to_map()
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


class DeleteAsyncTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAsyncTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAsyncTaskResponse, self).to_map()
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
            temp_model = DeleteAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutoCcBlacklistRequest(TeaModel):
    def __init__(self, blacklist=None, instance_id=None):
        # The IP addresses that you want to manage. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **src**: the IP address. This field is required and must be of the STRING type.
        self.blacklist = blacklist  # type: str
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAutoCcBlacklistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blacklist is not None:
            result['Blacklist'] = self.blacklist
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Blacklist') is not None:
            self.blacklist = m.get('Blacklist')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteAutoCcBlacklistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAutoCcBlacklistResponseBody, self).to_map()
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


class DeleteAutoCcBlacklistResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAutoCcBlacklistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAutoCcBlacklistResponse, self).to_map()
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
            temp_model = DeleteAutoCcBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAutoCcWhitelistRequest(TeaModel):
    def __init__(self, instance_id=None, whitelist=None):
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # The IP addresses that you want to manage. This parameter is a JSON string. This parameter is a JSON string. The string contains the following field:
        # 
        # *   **src**: the IP address. This field is required and must be of the string type.
        self.whitelist = whitelist  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAutoCcWhitelistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class DeleteAutoCcWhitelistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAutoCcWhitelistResponseBody, self).to_map()
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


class DeleteAutoCcWhitelistResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAutoCcWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAutoCcWhitelistResponse, self).to_map()
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
            temp_model = DeleteAutoCcWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainResourceRequest(TeaModel):
    def __init__(self, domain=None):
        # The domain name for which the forwarding rule is configured.
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainResourceRequest, self).to_map()
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


class DeleteDomainResourceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDomainResourceResponseBody, self).to_map()
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


class DeleteDomainResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDomainResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDomainResourceResponse, self).to_map()
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
            temp_model = DeleteDomainResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNetworkRuleRequest(TeaModel):
    def __init__(self, network_rule=None):
        # An array that consists of the information about the port forwarding rule. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **InstanceId**: the ID of the instance. This field is required and must be of the STRING type.
        # *   **Protocol**: the forwarding protocol. This field is required and must be of the STRING type. Valid values: **tcp** and **udp**.
        # *   **FrontendPort**: the forwarding port. This field is required and must be of the INTEGER type.
        self.network_rule = network_rule  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNetworkRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_rule is not None:
            result['NetworkRule'] = self.network_rule
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkRule') is not None:
            self.network_rule = m.get('NetworkRule')
        return self


class DeleteNetworkRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNetworkRuleResponseBody, self).to_map()
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


class DeleteNetworkRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteNetworkRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNetworkRuleResponse, self).to_map()
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
            temp_model = DeleteNetworkRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePortRequest(TeaModel):
    def __init__(self, backend_port=None, frontend_port=None, frontend_protocol=None, instance_id=None,
                 real_servers=None):
        # The port of the origin server. Valid values: **0** to **65535**.
        self.backend_port = backend_port  # type: str
        # The forwarding port. Valid values: **0** to **65535**.
        self.frontend_port = frontend_port  # type: str
        # The type of the protocol. Valid values:
        # 
        # *   **tcp**\
        # *   **udp**\
        self.frontend_protocol = frontend_protocol  # type: str
        # The ID of the Anti-DDoS Pro or Anti-DDoS Premium instance to which the port forwarding rule belongs.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # An array that consists of the IP addresses of origin servers.
        self.real_servers = real_servers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePortRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_port is not None:
            result['BackendPort'] = self.backend_port
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.frontend_protocol is not None:
            result['FrontendProtocol'] = self.frontend_protocol
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackendPort') is not None:
            self.backend_port = m.get('BackendPort')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('FrontendProtocol') is not None:
            self.frontend_protocol = m.get('FrontendProtocol')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        return self


class DeletePortResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePortResponseBody, self).to_map()
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


class DeletePortResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePortResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePortResponse, self).to_map()
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
            temp_model = DeletePortResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSceneDefensePolicyRequest(TeaModel):
    def __init__(self, policy_id=None):
        # The ID of the policy that you want to delete.
        # 
        # > You can call the [DescribeSceneDefensePolicies](~~159382~~) operation to query the IDs of all policies.
        self.policy_id = policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSceneDefensePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DeleteSceneDefensePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSceneDefensePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSceneDefensePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSceneDefensePolicyResponse, self).to_map()
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
            temp_model = DeleteSceneDefensePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSchedulerRuleRequest(TeaModel):
    def __init__(self, resource_group_id=None, rule_name=None):
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The name of the scheduling rule that you want to delete.
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSchedulerRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DeleteSchedulerRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSchedulerRuleResponseBody, self).to_map()
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


class DeleteSchedulerRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSchedulerRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSchedulerRuleResponse, self).to_map()
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
            temp_model = DeleteSchedulerRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTagResourcesRequest(TeaModel):
    def __init__(self, all=None, region_id=None, resource_group_id=None, resource_ids=None, resource_type=None,
                 tag_key=None):
        # Specifies whether to remove all tags from the specified resource. Valid values:
        # 
        # *   **true**: yes.
        # *   **false** no. This is the default value.
        self.all = all  # type: bool
        # The region ID of the instance. Set the value to **cn-hangzhou**, which indicates an Anti-DDoS Pro instance in the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # An array consisting of the IDs of instances from which you want to remove tags.
        self.resource_ids = resource_ids  # type: list[str]
        # The type of the resource to which the tag belongs. Set the value to **INSTANCE**, which indicates an Anti-DDoS Pro instance.
        self.resource_type = resource_type  # type: str
        # An array consisting of the keys of the tags that you want to remove.
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class DeleteTagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTagResourcesResponseBody, self).to_map()
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


class DeleteTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTagResourcesResponse, self).to_map()
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
            temp_model = DeleteTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebCCRuleRequest(TeaModel):
    def __init__(self, domain=None, name=None, resource_group_id=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for a domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The name of the custom frequency control rule that you want to delete.
        self.name = name  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWebCCRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteWebCCRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWebCCRuleResponseBody, self).to_map()
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


class DeleteWebCCRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteWebCCRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWebCCRuleResponse, self).to_map()
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
            temp_model = DeleteWebCCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebCacheCustomRuleRequest(TeaModel):
    def __init__(self, domain=None, resource_group_id=None, rule_names=None):
        # The domain name for which you want to delete the custom rules of the Static Page Caching policy.
        # 
        # > You can call the [DescribeDomains](~~91724~~) operation to query all the domain names that are added to Anti-DDoS Pro or Anti-DDoS Premium.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # An array consisting of the names of the rules that you want to delete.
        self.rule_names = rule_names  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWebCacheCustomRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rule_names is not None:
            result['RuleNames'] = self.rule_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RuleNames') is not None:
            self.rule_names = m.get('RuleNames')
        return self


class DeleteWebCacheCustomRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWebCacheCustomRuleResponseBody, self).to_map()
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


class DeleteWebCacheCustomRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteWebCacheCustomRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWebCacheCustomRuleResponse, self).to_map()
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
            temp_model = DeleteWebCacheCustomRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebPreciseAccessRuleRequest(TeaModel):
    def __init__(self, domain=None, resource_group_id=None, rule_names=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # An array that consists of the names of rules to delete.
        self.rule_names = rule_names  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWebPreciseAccessRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rule_names is not None:
            result['RuleNames'] = self.rule_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RuleNames') is not None:
            self.rule_names = m.get('RuleNames')
        return self


class DeleteWebPreciseAccessRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWebPreciseAccessRuleResponseBody, self).to_map()
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


class DeleteWebPreciseAccessRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteWebPreciseAccessRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWebPreciseAccessRuleResponse, self).to_map()
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
            temp_model = DeleteWebPreciseAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebRuleRequest(TeaModel):
    def __init__(self, domain=None, resource_group_id=None):
        # The domain name of the website from which you want to delete the forwarding rule.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query the domain names for which forwarding rules are configured.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](~~94485~~).
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWebRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteWebRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWebRuleResponseBody, self).to_map()
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


class DeleteWebRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteWebRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWebRuleResponse, self).to_map()
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
            temp_model = DeleteWebRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAsyncTasksRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, resource_group_id=None):
        # The number of the page to return.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAsyncTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeAsyncTasksResponseBodyAsyncTasks(TeaModel):
    def __init__(self, end_time=None, start_time=None, task_id=None, task_params=None, task_result=None,
                 task_status=None, task_type=None):
        # The end time of the task. This value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The start time of the task. The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time  # type: long
        # The ID of the job.
        self.task_id = task_id  # type: long
        # The task parameter. The value is a JSON string. The returned field in the value varies based on the value of **TaskType**.
        # 
        # If **TaskType** is set to **1**, **3**, **4**, **5**, or **6**, the following filed is returned:
        # 
        # *   **instanceId**: the ID of the instance. Data type: string.
        # 
        # If **TaskType** is set to **2**, the following field is returned:
        # 
        # *   **domain**: the domain name of the website. Data type: string.
        self.task_params = task_params  # type: str
        # The execution result of the task. The value is a JSON string. The returned fields in the value vary based on the value of **TaskType**.
        # 
        # If **TaskType** is set to **1**, **3**, **4**, **5**, or **6**, the following fields are returned:
        # 
        # *   **instanceId**: the ID of the instance. Data type: string.
        # *   **url**: the URL to download the exported file from Object Storage Service (OSS). Data type: string.
        # 
        # If **TaskType** is set to **2**, the following fields are returned:
        # 
        # *   **domain**: the domain name of the website. Data type: string.
        # *   **url**: the URL to download the exported file from OSS. Data type: string.
        self.task_result = task_result  # type: str
        # The status of the task. Valid values:
        # 
        # *   **0**: indicates that the task is being initialized.
        # *   **1**: indicates that the task is in progress.
        # *   **2**: indicates that the task is successful.
        # *   **3**: indicates that the task failed.
        self.task_status = task_status  # type: int
        # The type of the task. Valid values:
        # 
        # *   **1**: the task to export the port forwarding rules of an instance
        # *   **2**: the task to export the forwarding rules of a website protected by an instance
        # *   **3**: the task to export the sessions and health check settings of an instance
        # *   **4**: the task to export the mitigation policies of an instance
        # *   **5**: the task to download the blacklist for destination IP addresses of an instance
        # *   **6**: the task to download the whitelist for destination IP addresses of an instance
        self.task_type = task_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAsyncTasksResponseBodyAsyncTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_result is not None:
            result['TaskResult'] = self.task_result
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeAsyncTasksResponseBody(TeaModel):
    def __init__(self, async_tasks=None, request_id=None, total_count=None):
        # An array that consists of the details of the asynchronous export tasks.
        self.async_tasks = async_tasks  # type: list[DescribeAsyncTasksResponseBodyAsyncTasks]
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The total number of asynchronous export tasks that are returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.async_tasks:
            for k in self.async_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAsyncTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AsyncTasks'] = []
        if self.async_tasks is not None:
            for k in self.async_tasks:
                result['AsyncTasks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.async_tasks = []
        if m.get('AsyncTasks') is not None:
            for k in m.get('AsyncTasks'):
                temp_model = DescribeAsyncTasksResponseBodyAsyncTasks()
                self.async_tasks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAsyncTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAsyncTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAsyncTasksResponse, self).to_map()
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
            temp_model = DescribeAsyncTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAttackAnalysisMaxQpsRequest(TeaModel):
    def __init__(self, end_time=None, start_time=None):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: long
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAttackAnalysisMaxQpsRequest, self).to_map()
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


class DescribeAttackAnalysisMaxQpsResponseBody(TeaModel):
    def __init__(self, qps=None, request_id=None):
        # The peak queries per second (QPS) of DDoS attacks. Units: QPS.
        self.qps = qps  # type: long
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAttackAnalysisMaxQpsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAttackAnalysisMaxQpsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAttackAnalysisMaxQpsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAttackAnalysisMaxQpsResponse, self).to_map()
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
            temp_model = DescribeAttackAnalysisMaxQpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoCcBlacklistRequest(TeaModel):
    def __init__(self, instance_id=None, key_word=None, page_number=None, page_size=None):
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # The keyword for the query. This keyword is used to specify the prefix of the source IP address that you want to query.
        # 
        # > The keyword must be greater than three characters in length.
        self.key_word = key_word  # type: str
        # The number of the page to return. For example, to query the returned results on the first page, set the value to **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutoCcBlacklistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
    def __init__(self, dest_ip=None, end_time=None, source_ip=None, type=None):
        # The IP address of the instance.
        self.dest_ip = dest_ip  # type: str
        # The validity period of the IP address in the blacklist. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: long
        # The IP address in the blacklist.
        self.source_ip = source_ip  # type: str
        # The mode of how the IP address is added to the blacklist. Valid values:
        # 
        # *   **manual**: manually added
        # *   **auto**: automatically added
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutoCcBlacklistResponseBodyAutoCcBlacklist, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_ip is not None:
            result['DestIp'] = self.dest_ip
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestIp') is not None:
            self.dest_ip = m.get('DestIp')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAutoCcBlacklistResponseBody(TeaModel):
    def __init__(self, auto_cc_blacklist=None, request_id=None, total_count=None):
        # An array that consists of the details of the IP addresses in the blacklist of the instance.
        self.auto_cc_blacklist = auto_cc_blacklist  # type: list[DescribeAutoCcBlacklistResponseBodyAutoCcBlacklist]
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The total number of returned IP addresses in the blacklist.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.auto_cc_blacklist:
            for k in self.auto_cc_blacklist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAutoCcBlacklistResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AutoCcBlacklist'] = []
        if self.auto_cc_blacklist is not None:
            for k in self.auto_cc_blacklist:
                result['AutoCcBlacklist'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.auto_cc_blacklist = []
        if m.get('AutoCcBlacklist') is not None:
            for k in m.get('AutoCcBlacklist'):
                temp_model = DescribeAutoCcBlacklistResponseBodyAutoCcBlacklist()
                self.auto_cc_blacklist.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAutoCcBlacklistResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAutoCcBlacklistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAutoCcBlacklistResponse, self).to_map()
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
            temp_model = DescribeAutoCcBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoCcListCountRequest(TeaModel):
    def __init__(self, instance_id=None, query_type=None):
        # The ID of the instance.
        # 
        # > You can call the **DescribeInstanceIds** operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # The mode of how an IP address is added to the whitelist or blacklist. Valid values:
        # 
        # *   **manual**: manually added
        # *   **auto**: automatically added
        self.query_type = query_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutoCcListCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        return self


class DescribeAutoCcListCountResponseBody(TeaModel):
    def __init__(self, black_count=None, request_id=None, white_count=None):
        # The total number of IP addresses in the blacklist.
        self.black_count = black_count  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of IP addresses in the whitelist.
        self.white_count = white_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutoCcListCountResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAutoCcListCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAutoCcListCountResponse, self).to_map()
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
            temp_model = DescribeAutoCcListCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoCcWhitelistRequest(TeaModel):
    def __init__(self, instance_id=None, key_word=None, page_number=None, page_size=None):
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # The keyword for the query. This keyword is used to specify the prefix of the source IP address that you want to query.
        # 
        # > The keyword must be greater than three characters in length.
        self.key_word = key_word  # type: str
        # The number of the page to return. For example, to query the returned results on the first page, set the value to **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutoCcWhitelistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
    def __init__(self, dest_ip=None, end_time=None, source_ip=None, type=None):
        # The IP address of the instance.
        self.dest_ip = dest_ip  # type: str
        # The validity period of the IP address in the whitelist. Unit: seconds. **0** indicates that the IP address in the whitelist never expires.
        self.end_time = end_time  # type: long
        # The IP addresses that is contained in the IP address whitelist.
        self.source_ip = source_ip  # type: str
        # The mode of how an IP address is added to the whitelist. Valid values:
        # 
        # *   **manual**: manually added
        # *   **auto**: automatically added
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutoCcWhitelistResponseBodyAutoCcWhitelist, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_ip is not None:
            result['DestIp'] = self.dest_ip
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestIp') is not None:
            self.dest_ip = m.get('DestIp')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAutoCcWhitelistResponseBody(TeaModel):
    def __init__(self, auto_cc_whitelist=None, request_id=None, total_count=None):
        # An array that consists of details of the IP address in the whitelist of the instance.
        self.auto_cc_whitelist = auto_cc_whitelist  # type: list[DescribeAutoCcWhitelistResponseBodyAutoCcWhitelist]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned IP addresses in the whitelist.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.auto_cc_whitelist:
            for k in self.auto_cc_whitelist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAutoCcWhitelistResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AutoCcWhitelist'] = []
        if self.auto_cc_whitelist is not None:
            for k in self.auto_cc_whitelist:
                result['AutoCcWhitelist'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.auto_cc_whitelist = []
        if m.get('AutoCcWhitelist') is not None:
            for k in m.get('AutoCcWhitelist'):
                temp_model = DescribeAutoCcWhitelistResponseBodyAutoCcWhitelist()
                self.auto_cc_whitelist.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAutoCcWhitelistResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAutoCcWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAutoCcWhitelistResponse, self).to_map()
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
            temp_model = DescribeAutoCcWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackSourceCidrRequest(TeaModel):
    def __init__(self, ip_version=None, line=None, resource_group_id=None):
        # The IP version of the back-to-origin CIDR block.
        # 
        # *   **Ipv4**\
        # *   **Ipv6**\
        self.ip_version = ip_version  # type: str
        # The Internet service provider (ISP) line that you want to query.
        self.line = line  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackSourceCidrRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.line is not None:
            result['Line'] = self.line
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeBackSourceCidrResponseBody(TeaModel):
    def __init__(self, cidrs=None, request_id=None):
        # An array that consists of the back-to-origin CIDR blocks of the instance.
        self.cidrs = cidrs  # type: list[str]
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBackSourceCidrResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBackSourceCidrResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBackSourceCidrResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBackSourceCidrResponse, self).to_map()
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
            temp_model = DescribeBackSourceCidrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBlackholeStatusRequest(TeaModel):
    def __init__(self, instance_ids=None):
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_ids = instance_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBlackholeStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeBlackholeStatusResponseBodyBlackholeStatus(TeaModel):
    def __init__(self, black_status=None, end_time=None, ip=None, start_time=None):
        # Indicates whether blackhole filtering is triggered for the instance. Valid values:
        # 
        # *   **blackhole**: yes
        # *   **normal**: no
        self.black_status = black_status  # type: str
        # The end time of blackhole filtering. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: long
        # The IP address of the instance.
        self.ip = ip  # type: str
        # The start time of blackhole filtering. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBlackholeStatusResponseBodyBlackholeStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_status is not None:
            result['BlackStatus'] = self.black_status
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackStatus') is not None:
            self.black_status = m.get('BlackStatus')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeBlackholeStatusResponseBody(TeaModel):
    def __init__(self, blackhole_status=None, request_id=None):
        # An array that consists of the blackhole filtering status of the instance.
        self.blackhole_status = blackhole_status  # type: list[DescribeBlackholeStatusResponseBodyBlackholeStatus]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.blackhole_status:
            for k in self.blackhole_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBlackholeStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlackholeStatus'] = []
        if self.blackhole_status is not None:
            for k in self.blackhole_status:
                result['BlackholeStatus'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.blackhole_status = []
        if m.get('BlackholeStatus') is not None:
            for k in m.get('BlackholeStatus'):
                temp_model = DescribeBlackholeStatusResponseBodyBlackholeStatus()
                self.blackhole_status.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBlackholeStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBlackholeStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBlackholeStatusResponse, self).to_map()
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
            temp_model = DescribeBlackholeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBlockStatusRequest(TeaModel):
    def __init__(self, instance_ids=None, resource_group_id=None):
        # An array consisting of information about the IDs of the instances that you want to query.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_ids = instance_ids  # type: list[str]
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBlockStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeBlockStatusResponseBodyStatusListBlockStatusList(TeaModel):
    def __init__(self, block_status=None, end_time=None, line=None, start_time=None):
        # The blocking status of the network traffic. Valid values:
        # 
        # *   **areablock**: Network traffic is blocked.
        # *   **normal**: Network traffic is not blocked.
        self.block_status = block_status  # type: str
        # The end time of the blocking. This value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: long
        # The Internet service provider (ISP) line from which the traffic is blocked. Valid values:
        # 
        # *   **ct**: China Telecom (International)
        # *   **cut**: China Unicom (International)
        self.line = line  # type: str
        # The start time of the blocking. This value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBlockStatusResponseBodyStatusListBlockStatusList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_status is not None:
            result['BlockStatus'] = self.block_status
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.line is not None:
            result['Line'] = self.line
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockStatus') is not None:
            self.block_status = m.get('BlockStatus')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeBlockStatusResponseBodyStatusList(TeaModel):
    def __init__(self, block_status_list=None, ip=None):
        # An array that consists of details of the Diversion from Origin Server configuration.
        self.block_status_list = block_status_list  # type: list[DescribeBlockStatusResponseBodyStatusListBlockStatusList]
        # The IP address of the instance.
        self.ip = ip  # type: str

    def validate(self):
        if self.block_status_list:
            for k in self.block_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBlockStatusResponseBodyStatusList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlockStatusList'] = []
        if self.block_status_list is not None:
            for k in self.block_status_list:
                result['BlockStatusList'].append(k.to_map() if k else None)
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.block_status_list = []
        if m.get('BlockStatusList') is not None:
            for k in m.get('BlockStatusList'):
                temp_model = DescribeBlockStatusResponseBodyStatusListBlockStatusList()
                self.block_status_list.append(temp_model.from_map(k))
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeBlockStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, status_list=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array that consists of details of the Diversion from Origin Server configurations of the instance.
        self.status_list = status_list  # type: list[DescribeBlockStatusResponseBodyStatusList]

    def validate(self):
        if self.status_list:
            for k in self.status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBlockStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeBlockStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBlockStatusResponse, self).to_map()
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
            temp_model = DescribeBlockStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCertsRequest(TeaModel):
    def __init__(self, domain=None, resource_group_id=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCertsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeCertsResponseBodyCerts(TeaModel):
    def __init__(self, cert_identifier=None, common=None, domain_related=None, end_date=None, id=None, issuer=None,
                 name=None, start_date=None):
        self.cert_identifier = cert_identifier  # type: str
        # The domain name that is associated with the certificate.
        self.common = common  # type: str
        # Indicates whether the certificate is associated with the domain name. Valid values:
        # 
        # *   **true**: The certificate is associated with the domain name.
        # *   **false**: The certificate is not associated with the domain name.
        self.domain_related = domain_related  # type: bool
        # The expiration date of the certificate. string
        self.end_date = end_date  # type: str
        # The ID of the certificate.
        self.id = id  # type: int
        # The certificate authority (CA) that issued the certificate.
        self.issuer = issuer  # type: str
        # The name of the certificate.
        self.name = name  # type: str
        # The issuance date of the certificate. string
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCertsResponseBodyCerts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.common is not None:
            result['Common'] = self.common
        if self.domain_related is not None:
            result['DomainRelated'] = self.domain_related
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.id is not None:
            result['Id'] = self.id
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.name is not None:
            result['Name'] = self.name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('DomainRelated') is not None:
            self.domain_related = m.get('DomainRelated')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeCertsResponseBody(TeaModel):
    def __init__(self, certs=None, request_id=None):
        # The certificate information about the website.
        self.certs = certs  # type: list[DescribeCertsResponseBodyCerts]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.certs:
            for k in self.certs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCertsResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCertsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCertsResponse, self).to_map()
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
            temp_model = DescribeCertsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCnameReusesRequest(TeaModel):
    def __init__(self, domains=None, resource_group_id=None):
        self.domains = domains  # type: list[str]
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCnameReusesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeCnameReusesResponseBodyCnameReuses(TeaModel):
    def __init__(self, cname=None, domain=None, enable=None):
        self.cname = cname  # type: str
        self.domain = domain  # type: str
        self.enable = enable  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCnameReusesResponseBodyCnameReuses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DescribeCnameReusesResponseBody(TeaModel):
    def __init__(self, cname_reuses=None, request_id=None):
        self.cname_reuses = cname_reuses  # type: list[DescribeCnameReusesResponseBodyCnameReuses]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cname_reuses:
            for k in self.cname_reuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCnameReusesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CnameReuses'] = []
        if self.cname_reuses is not None:
            for k in self.cname_reuses:
                result['CnameReuses'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cname_reuses = []
        if m.get('CnameReuses') is not None:
            for k in m.get('CnameReuses'):
                temp_model = DescribeCnameReusesResponseBodyCnameReuses()
                self.cname_reuses.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCnameReusesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeCnameReusesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCnameReusesResponse, self).to_map()
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
            temp_model = DescribeCnameReusesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDoSEventsRequest(TeaModel):
    def __init__(self, end_time=None, instance_ids=None, page_number=None, page_size=None, resource_group_id=None,
                 start_time=None):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_ids = instance_ids  # type: list[str]
        # The number of the page to return. For example, to query the returned results on the first page, set the value to **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDDoSEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDDoSEventsResponseBodyDDoSEvents(TeaModel):
    def __init__(self, bps=None, end_time=None, event_type=None, ip=None, port=None, pps=None, region=None,
                 start_time=None):
        # The bandwidth of attack traffic. Unit: bit/s.
        self.bps = bps  # type: long
        # The time when the DDoS attack stopped. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: long
        # The type of the attack event. Valid values:
        # 
        # *   **defense**: traffic scrubbing events
        # *   **blackhole**: blackhole filtering events
        self.event_type = event_type  # type: str
        # The attacked IP address.
        self.ip = ip  # type: str
        # The attacked port.
        self.port = port  # type: str
        # The packet forwarding rate of attack traffic. Unit: packets per second (pps).
        self.pps = pps  # type: long
        # The region from which the attack was launched. Valid values:
        # 
        # *   **cn**: a region in the Chinese mainland
        # *   **alb-ap-northeast-1-gf-x**: Japan (Tokyo)
        # *   **alb-ap-southeast-gf-x**: Singapore
        # *   **alb-cn-hongkong-gf-x**: Hong Kong (China)
        # *   **alb-eu-central-1-gf-x**: Germany (Frankfurt)
        # *   **alb-us-west-1-gf-x**: US (Silicon Valley)
        # 
        # > The values except **cn** are returned only when **RegionId** is set to **ap-southeast-1**.
        self.region = region  # type: str
        # The time when the DDoS attack started. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDDoSEventsResponseBodyDDoSEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.region is not None:
            result['Region'] = self.region
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDDoSEventsResponseBody(TeaModel):
    def __init__(self, ddo_sevents=None, request_id=None, total=None):
        # The DDoS attack events.
        self.ddo_sevents = ddo_sevents  # type: list[DescribeDDoSEventsResponseBodyDDoSEvents]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned attack events.
        self.total = total  # type: long

    def validate(self):
        if self.ddo_sevents:
            for k in self.ddo_sevents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDDoSEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DDoSEvents'] = []
        if self.ddo_sevents is not None:
            for k in self.ddo_sevents:
                result['DDoSEvents'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ddo_sevents = []
        if m.get('DDoSEvents') is not None:
            for k in m.get('DDoSEvents'):
                temp_model = DescribeDDoSEventsResponseBodyDDoSEvents()
                self.ddo_sevents.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeDDoSEventsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDDoSEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDDoSEventsResponse, self).to_map()
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
            temp_model = DescribeDDoSEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosAllEventListRequest(TeaModel):
    def __init__(self, end_time=None, event_type=None, page_number=None, page_size=None, start_time=None):
        # The end of the time range to query. The DDoS attack events occur before **EndTime** are queried. This value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: long
        # The type of the DDoS attack events you want to query. Valid values:
        # 
        # *   **web-cc**: resource exhaustion attacks
        # *   **cc**: connection flood attacks
        # *   **defense**: DDoS attacks that trigger traffic scrubbing
        # *   **blackhole**: DDoS attacks that trigger blackhole filtering
        # 
        # If you want to query multiple types of DDoS attack events, separate them with commas (,).
        # 
        # If you do not configure this parameter, DDoS attack events of all types are queried.
        self.event_type = event_type  # type: str
        # The number of the page to return.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The beginning of the time range to query. The DDoS attack events occur after **StartTime** are queried. This value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDDosAllEventListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDDosAllEventListResponseBodyAttackEvents(TeaModel):
    def __init__(self, area=None, end_time=None, event_type=None, ip=None, mbps=None, port=None, pps=None,
                 start_time=None):
        # The source location or region from which the attack was initiated. Valid values:
        # 
        # *   **cn**: Chinese mainland
        # *   **alb-cn-hongkong-gf-2**: China (Hongkong)
        # *   **alb-us-west-1-gf-2**: US (Silicon Valley)
        # *   **alb-ap-northeast-1-gf-1**: Japan (Tokyo)
        # *   **alb-ap-southeast-gf-1**: Singapore
        # *   **alb-eu-central-1-gf-1**: Germany (Frankfurt)
        # *   **alb-eu-central-1-gf-1** or **selb-eu-west-1-gf-1a**: UK (London)
        # *   **alb-us-east-gf-1**: US (Virginia)
        # *   **CT-yundi**: China (Hongkong) This value is returned only for Anti-DDoS Premium instances of the Secure Chinese Mainland Acceleration (Sec-CMA) mitigation plan.
        self.area = area  # type: str
        # The time when the DDoS attack stopped. This value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: long
        # The type of the DDoS attack event. Valid values:
        # 
        # *   **web-cc**: resource exhaustion attacks
        # *   **cc**: connection flood attacks
        # *   **defense**: DDoS attacks that trigger traffic scrubbing
        # *   **blackhole**: DDoS attacks that trigger blackhole filtering
        self.event_type = event_type  # type: str
        # The attacked object. The attacked object varies based on the attack event type. The following list describes different attacked objects of different attack event types:
        # 
        # *   If **EventType** is set to **web-cc**, the value of this parameter indicates the domain name of the attacked website.
        # *   If **EventType** is set to **cc**, the value of this parameter indicates the IP address of the attacked Anti-DDoS Pro or Anti-DDoS Premium instance.
        # *   If **EventType** is set to **defense** or **blackhole**, the value of this parameter indicates the IP address of the attacked Anti-DDoS Pro or Anti-DDoS Premium instance.
        self.ip = ip  # type: str
        # The peak bandwidth of the attack traffic. Unit: Mbit/s.
        self.mbps = mbps  # type: long
        # The attacked port.
        # 
        # > If **EventType** is set to **web-cc**, this parameter is not returned.
        self.port = port  # type: str
        # The peak packet forwarding rate of attack traffic. Unit: packets per second (pps).
        self.pps = pps  # type: long
        # The time when the DDoS attack started. This value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDDosAllEventListResponseBodyAttackEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.mbps is not None:
            result['Mbps'] = self.mbps
        if self.port is not None:
            result['Port'] = self.port
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDDosAllEventListResponseBody(TeaModel):
    def __init__(self, attack_events=None, request_id=None, total=None):
        # An array that consists of attack events.
        self.attack_events = attack_events  # type: list[DescribeDDosAllEventListResponseBodyAttackEvents]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of DDoS attack events.
        self.total = total  # type: long

    def validate(self):
        if self.attack_events:
            for k in self.attack_events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDDosAllEventListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AttackEvents'] = []
        if self.attack_events is not None:
            for k in self.attack_events:
                result['AttackEvents'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.attack_events = []
        if m.get('AttackEvents') is not None:
            for k in m.get('AttackEvents'):
                temp_model = DescribeDDosAllEventListResponseBodyAttackEvents()
                self.attack_events.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeDDosAllEventListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDDosAllEventListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDDosAllEventListResponse, self).to_map()
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
            temp_model = DescribeDDosAllEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosEventAreaRequest(TeaModel):
    def __init__(self, event_type=None, ip=None, start_time=None):
        # The type of the attack event that you want to query. Valid values:
        # 
        # *   **defense**: attack events that trigger traffic scrubbing
        # *   **blackhole**: attack events that trigger blackhole filtering
        self.event_type = event_type  # type: str
        # The IP address of the attacked Anti-DDoS Pro or Anti-DDoS Premium instance.
        self.ip = ip  # type: str
        # The UNIX timestamp when the query starts. Unit: seconds.
        # 
        # > You can call the [DescribeDDosAllEventList](~~188604~~) operation to query the beginning time of all attack events.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDDosEventAreaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDDosEventAreaResponseBodyAreas(TeaModel):
    def __init__(self, area=None, in_pkts=None):
        # The code or ID of the source region. For more information, see [Codes of administrative regions in China and codes of countries and areas](~~167926~~). For example, **110000** indicates Beijing, China, and **us** indicates the United States.
        self.area = area  # type: str
        # The number of request packets that were sent from the source region.
        self.in_pkts = in_pkts  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDDosEventAreaResponseBodyAreas, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.in_pkts is not None:
            result['InPkts'] = self.in_pkts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('InPkts') is not None:
            self.in_pkts = m.get('InPkts')
        return self


class DescribeDDosEventAreaResponseBody(TeaModel):
    def __init__(self, areas=None, request_id=None):
        # The information about the source region from which the volumetric attack was initiated.
        self.areas = areas  # type: list[DescribeDDosEventAreaResponseBodyAreas]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.areas:
            for k in self.areas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDDosEventAreaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Areas'] = []
        if self.areas is not None:
            for k in self.areas:
                result['Areas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.areas = []
        if m.get('Areas') is not None:
            for k in m.get('Areas'):
                temp_model = DescribeDDosEventAreaResponseBodyAreas()
                self.areas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDDosEventAreaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDDosEventAreaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDDosEventAreaResponse, self).to_map()
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
            temp_model = DescribeDDosEventAreaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosEventAttackTypeRequest(TeaModel):
    def __init__(self, event_type=None, ip=None, start_time=None):
        # The type of the attack event that you want to query. Valid values:
        # 
        # *   **defense**: attack events that trigger traffic scrubbing
        # *   **blackhole**: attack events that trigger blackhole filtering
        self.event_type = event_type  # type: str
        # The IP address of the attacked Anti-DDoS Pro or Anti-DDoS Premium instance.
        self.ip = ip  # type: str
        # The UNIX timestamp when the query starts. Unit: seconds.
        # 
        # > You can call the [DescribeDDosAllEventList](~~188604~~) operation to query the beginning time of all attack events.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDDosEventAttackTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDDosEventAttackTypeResponseBodyAttackTypes(TeaModel):
    def __init__(self, attack_type=None, in_pkts=None):
        # The type of the attack Valid values:
        # 
        # *   **QOTD-Reflect-Flood**: QOTD reflection attacks
        # *   **CharGEN-Reflect-Flood**: CHARGEN reflection attacks
        # *   **DNS-Reflect-Flood**: DNS reflection attacks
        # *   **TFTP-Reflect-Flood**: TFTP reflection attacks
        # *   **Portmap-Reflect-Flood**: Portmap reflection attacks
        # *   **NTP-Reflect-Flood**: NTP reflection attacks
        # *   **NetBIOS-Reflect-Flood**: NetBIOS reflection attacks
        # *   **SNMPv2-Reflect-Flood**: SNMPv2 reflection attacks
        # *   **CLDAP-Reflect-Flood**: CLDAP reflection attacks
        # *   **Ripv1-Reflect-Flood**: RIPv1 reflection attacks
        # *   **OpenVPN-Reflect-Flood**: OpenVPN reflection attacks
        # *   **SSDP-Reflect-Flood**: SSDP reflection attacks
        # *   **NetAssistant-Reflect-Flood**: NetAssistant reflection attacks
        # *   **WSDiscovery-Reflect-Flood**: WS-Discovery reflection attacks
        # *   **Kad-Reflect-Flood**: Kad reflection attacks
        # *   **mDNS-Reflect-Flood**: mDNS reflection attacks
        # *   **10001-Reflect-Flood**: reflection attacks over port 10001
        # *   **Memcached-Reflect-Flood**: Memcached reflection attacks
        # *   **QNP-Reflect-Flood**: QNP reflection attacks
        # *   **DVR-Reflect-Flood**: DVR reflection attacks
        # *   **CoAP-Reflect-Flood**: CoAP reflection attacks
        # *   **ADDP-Reflect-Flood**: ADDP reflection attacks
        # *   **Tcp-Syn**: TCP SYN flood attacks
        # *   **Tcp-Fin**: TCP FIN flood attacks
        # *   **Tcp-Ack**: TCP ACK flood attacks
        # *   **Tcp-Rst**: TCP RST flood attacks
        # *   **Tcp-Pushack**: TCP PSH-ACK flood attacks
        # *   **Tcp-Synack**: TCP SYN-ACK flood attacks
        # *   **Udp-None**: UDP attacks
        # *   **Udp-Ssh**: UDP-based SSH attacks
        # *   **Udp-Dns**: UDP-based DNS attacks
        # *   **Udp-Http**: UDP-based HTTP attacks
        # *   **Udp-Https**: UDP-based HTTPS attacks
        # *   **Udp-Ntp**: UDP-based NTP attacks
        # *   **Udp-Ldap**: UDP-based LDAP attacks
        # *   **Udp-Ssdp**: UDP-based SSDP attacks
        # *   **Udp-Memcached**: Memcached UDP reflection attacks
        # *   **Tcp-Other**: other TCP attacks
        # *   **Icmp**: ICMP flood attacks
        # *   **Igmp**: IGMP flood attacks
        # *   **Ipv6**: IPv6 attacks
        self.attack_type = attack_type  # type: str
        # The number of request packets of the attack type.
        self.in_pkts = in_pkts  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDDosEventAttackTypeResponseBodyAttackTypes, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, attack_types=None, request_id=None):
        # The information about the attack types.
        self.attack_types = attack_types  # type: list[DescribeDDosEventAttackTypeResponseBodyAttackTypes]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.attack_types:
            for k in self.attack_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDDosEventAttackTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AttackTypes'] = []
        if self.attack_types is not None:
            for k in self.attack_types:
                result['AttackTypes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.attack_types = []
        if m.get('AttackTypes') is not None:
            for k in m.get('AttackTypes'):
                temp_model = DescribeDDosEventAttackTypeResponseBodyAttackTypes()
                self.attack_types.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDDosEventAttackTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDDosEventAttackTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDDosEventAttackTypeResponse, self).to_map()
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
            temp_model = DescribeDDosEventAttackTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosEventIspRequest(TeaModel):
    def __init__(self, event_type=None, ip=None, start_time=None):
        # The type of the attack event that you want to query. Valid values:
        # 
        # *   **defense**: attack events that trigger traffic scrubbing
        # *   **blackhole**: attack events that trigger blackhole filtering
        self.event_type = event_type  # type: str
        # The IP address of the attacked Anti-DDoS Pro or Anti-DDoS Premium instance.
        self.ip = ip  # type: str
        # The UNIX timestamp when the query starts. Unit: seconds.
        # 
        # > You can call the [DescribeDDosAllEventList](~~188604~~) operation to query the beginning time of all attack events.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDDosEventIspRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDDosEventIspResponseBodyIsps(TeaModel):
    def __init__(self, in_pkts=None, isp=None):
        # The number of request packets that were sent from the ISP.
        self.in_pkts = in_pkts  # type: long
        # The code of the ISP. Valid values:
        # 
        # *   **100017**: China Telecom
        # *   **100026**: China Unicom
        # *   **100025**: China Mobile
        # *   **100027**: China Education and Research Network
        # *   **100020**: China Mobile Tietong
        # *   **1000143**: Dr.Peng Telecom & Media Group
        # *   **100080**: Beijing Gehua CATV Network
        # *   **1000139**: National Radio and Television Administration
        # *   **100023**: Oriental Cable Network
        # *   **100063**: Founder Broadband
        # *   **1000337**: China Internet Exchange
        # *   **100021**: 21Vianet Group
        # *   **1000333**: Wasu Media Holding
        # *   **100093**: Wangsu Science & Technology
        # *   **1000401**: Tencent
        # *   **100099**: Baidu
        # *   **1000323**: Alibaba Cloud
        # *   **100098**: Alibaba
        self.isp = isp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDDosEventIspResponseBodyIsps, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, isps=None, request_id=None):
        # An array that consists of the ISPs for the volumetric attack.
        self.isps = isps  # type: list[DescribeDDosEventIspResponseBodyIsps]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.isps:
            for k in self.isps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDDosEventIspResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Isps'] = []
        if self.isps is not None:
            for k in self.isps:
                result['Isps'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.isps = []
        if m.get('Isps') is not None:
            for k in m.get('Isps'):
                temp_model = DescribeDDosEventIspResponseBodyIsps()
                self.isps.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDDosEventIspResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDDosEventIspResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDDosEventIspResponse, self).to_map()
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
            temp_model = DescribeDDosEventIspResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosEventMaxRequest(TeaModel):
    def __init__(self, end_time=None, start_time=None):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: long
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDDosEventMaxRequest, self).to_map()
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


class DescribeDDosEventMaxResponseBody(TeaModel):
    def __init__(self, cps=None, mbps=None, qps=None, request_id=None):
        # The peak of connection flood attacks. Unit: connections per seconds (CPS).
        self.cps = cps  # type: long
        # The peak of volumetric attacks. Unit: Mbit/s.
        self.mbps = mbps  # type: long
        # The peak of resource exhaustion attacks. Unit: queries per second (QPS).
        self.qps = qps  # type: long
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDDosEventMaxResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.mbps is not None:
            result['Mbps'] = self.mbps
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDDosEventMaxResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDDosEventMaxResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDDosEventMaxResponse, self).to_map()
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
            temp_model = DescribeDDosEventMaxResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDosEventSrcIpRequest(TeaModel):
    def __init__(self, event_type=None, ip=None, range=None, start_time=None):
        # The type of the attack event that you want to query. Valid values:
        # 
        # *   **defense**: attack events that trigger traffic scrubbing
        # *   **blackhole**: attack events that trigger blackhole filtering
        self.event_type = event_type  # type: str
        # The IP address of the attacked Anti-DDoS Pro or Anti-DDoS Premium instance.
        self.ip = ip  # type: str
        # The number of source IP addresses that you want to return. The source IP addresses are returned in descending order of attack traffic. By default, the top **five** source IP addresses are returned.
        self.range = range  # type: long
        # The UNIX timestamp when the query starts. Unit: seconds.
        # 
        # > You can call the [DescribeDDosAllEventList](~~188604~~) operation to query the beginning time of all attack events.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDDosEventSrcIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.range is not None:
            result['Range'] = self.range
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Range') is not None:
            self.range = m.get('Range')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDDosEventSrcIpResponseBodyIps(TeaModel):
    def __init__(self, area_id=None, isp=None, src_ip=None):
        # The code or ID of the source region. For more information, see [Codes of administrative regions in China and codes of countries and areas](~~167926~~). For example, **110000** indicates Beijing, China, and **us** indicates the United States.
        self.area_id = area_id  # type: str
        # The Internet service provider (ISP) for the volumetric attack. Valid values:
        # 
        # *   **100017**: China Telecom
        # *   **100026**: China Unicom
        # *   **100025**: China Mobile
        # *   **100027**: China Education and Research Network
        # *   **100020**: China Mobile Tietong
        # *   **1000143**: Dr.Peng Telecom & Media Group
        # *   **100080**: Beijing Gehua CATV Network
        # *   **1000139**: National Radio and Television Administration
        # *   **100023**: Oriental Cable Network
        # *   **100063**: Founder Broadband
        # *   **1000337**: China Internet Exchange
        # *   **100021**: 21Vianet Group
        # *   **1000333**: Wasu Media Holding
        # *   **100093**: Wangsu Science & Technology
        # *   **1000401**: Tencent
        # *   **100099**: Baidu
        # *   **1000323**: Alibaba Cloud
        # *   **100098**: Alibaba
        self.isp = isp  # type: str
        # The source IP address of the volumetric attack.
        self.src_ip = src_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDDosEventSrcIpResponseBodyIps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')
        return self


class DescribeDDosEventSrcIpResponseBody(TeaModel):
    def __init__(self, ips=None, request_id=None):
        # An array that consists of information about the source IP address of the volumetric attack.
        self.ips = ips  # type: list[DescribeDDosEventSrcIpResponseBodyIps]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.ips:
            for k in self.ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDDosEventSrcIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Ips'] = []
        if self.ips is not None:
            for k in self.ips:
                result['Ips'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ips = []
        if m.get('Ips') is not None:
            for k in m.get('Ips'):
                temp_model = DescribeDDosEventSrcIpResponseBodyIps()
                self.ips.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDDosEventSrcIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDDosEventSrcIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDDosEventSrcIpResponse, self).to_map()
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
            temp_model = DescribeDDosEventSrcIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDefenseCountStatisticsRequest(TeaModel):
    def __init__(self, resource_group_id=None):
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefenseCountStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDefenseCountStatisticsResponseBodyDefenseCountStatistics(TeaModel):
    def __init__(self, defense_count_total_usage_of_current_month=None, flow_pack_count_remain=None,
                 max_usable_defense_count_current_month=None, sec_high_speed_count_remain=None):
        # The number of advanced mitigation sessions that are used within the current calendar month.
        self.defense_count_total_usage_of_current_month = defense_count_total_usage_of_current_month  # type: int
        # The number of available global advanced mitigation sessions for the Insurance mitigation plan.
        self.flow_pack_count_remain = flow_pack_count_remain  # type: int
        # The maximum number of advanced mitigation sessions available for the current calendar month. The advanced mitigation sessions include the advanced mitigation sessions that are provided free of charge and the global advanced mitigation sessions that you purchase.
        self.max_usable_defense_count_current_month = max_usable_defense_count_current_month  # type: int
        # The number of available global advanced mitigation sessions for the Secure Chinese Mainland Acceleration (Sec-CMA) mitigation plan.
        self.sec_high_speed_count_remain = sec_high_speed_count_remain  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefenseCountStatisticsResponseBodyDefenseCountStatistics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_count_total_usage_of_current_month is not None:
            result['DefenseCountTotalUsageOfCurrentMonth'] = self.defense_count_total_usage_of_current_month
        if self.flow_pack_count_remain is not None:
            result['FlowPackCountRemain'] = self.flow_pack_count_remain
        if self.max_usable_defense_count_current_month is not None:
            result['MaxUsableDefenseCountCurrentMonth'] = self.max_usable_defense_count_current_month
        if self.sec_high_speed_count_remain is not None:
            result['SecHighSpeedCountRemain'] = self.sec_high_speed_count_remain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefenseCountTotalUsageOfCurrentMonth') is not None:
            self.defense_count_total_usage_of_current_month = m.get('DefenseCountTotalUsageOfCurrentMonth')
        if m.get('FlowPackCountRemain') is not None:
            self.flow_pack_count_remain = m.get('FlowPackCountRemain')
        if m.get('MaxUsableDefenseCountCurrentMonth') is not None:
            self.max_usable_defense_count_current_month = m.get('MaxUsableDefenseCountCurrentMonth')
        if m.get('SecHighSpeedCountRemain') is not None:
            self.sec_high_speed_count_remain = m.get('SecHighSpeedCountRemain')
        return self


class DescribeDefenseCountStatisticsResponseBody(TeaModel):
    def __init__(self, defense_count_statistics=None, request_id=None):
        # The statistics on the number of advanced mitigation sessions.
        self.defense_count_statistics = defense_count_statistics  # type: DescribeDefenseCountStatisticsResponseBodyDefenseCountStatistics
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.defense_count_statistics:
            self.defense_count_statistics.validate()

    def to_map(self):
        _map = super(DescribeDefenseCountStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_count_statistics is not None:
            result['DefenseCountStatistics'] = self.defense_count_statistics.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefenseCountStatistics') is not None:
            temp_model = DescribeDefenseCountStatisticsResponseBodyDefenseCountStatistics()
            self.defense_count_statistics = temp_model.from_map(m['DefenseCountStatistics'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDefenseCountStatisticsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDefenseCountStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDefenseCountStatisticsResponse, self).to_map()
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
            temp_model = DescribeDefenseCountStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDefenseRecordsRequest(TeaModel):
    def __init__(self, end_time=None, instance_id=None, page_number=None, page_size=None, resource_group_id=None,
                 start_time=None):
        # The end of the time range to query. This value is a UNIX timestamp. Units: miliseconds.
        # 
        # > The time must be in the latest 90 days.
        self.end_time = end_time  # type: long
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # The number of the page to return. For example, to query the returned results on the first page, set the value to **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Maximum value: **50**.
        self.page_size = page_size  # type: int
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. This value is a UNIX timestamp. Units: miliseconds.
        # 
        # > The time must be in the latest 90 days.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefenseRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDefenseRecordsResponseBodyDefenseRecords(TeaModel):
    def __init__(self, attack_peak=None, end_time=None, event_count=None, instance_id=None, start_time=None,
                 status=None):
        # The peak attack traffic. Unit: bit/s.
        self.attack_peak = attack_peak  # type: long
        # The end time of the advanced mitigation session. This value is a UNIX timestamp. Units: miliseconds.
        self.end_time = end_time  # type: long
        # The number of attacks.
        self.event_count = event_count  # type: int
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The start time of the advanced mitigation session. This value is a UNIX timestamp. Units: miliseconds.
        self.start_time = start_time  # type: long
        # The status of the advanced mitigation session. Valid values:
        # 
        # *   **0**: The advanced mitigation session is being used.
        # *   **1**: The advanced mitigation session is used.
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDefenseRecordsResponseBodyDefenseRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_peak is not None:
            result['AttackPeak'] = self.attack_peak
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_count is not None:
            result['EventCount'] = self.event_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttackPeak') is not None:
            self.attack_peak = m.get('AttackPeak')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventCount') is not None:
            self.event_count = m.get('EventCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDefenseRecordsResponseBody(TeaModel):
    def __init__(self, defense_records=None, request_id=None, total_count=None):
        # An array that consists of details of the log of an advanced mitigation session.
        self.defense_records = defense_records  # type: list[DescribeDefenseRecordsResponseBodyDefenseRecords]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of advanced mitigation sessions.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.defense_records:
            for k in self.defense_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDefenseRecordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DefenseRecords'] = []
        if self.defense_records is not None:
            for k in self.defense_records:
                result['DefenseRecords'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.defense_records = []
        if m.get('DefenseRecords') is not None:
            for k in m.get('DefenseRecords'):
                temp_model = DescribeDefenseRecordsResponseBodyDefenseRecords()
                self.defense_records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDefenseRecordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDefenseRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDefenseRecordsResponse, self).to_map()
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
            temp_model = DescribeDefenseRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainAttackEventsRequest(TeaModel):
    def __init__(self, domain=None, end_time=None, page_number=None, page_size=None, resource_group_id=None,
                 start_time=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # The number of the page to return. For example, to query the returned results on the first page, set the value to **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainAttackEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainAttackEventsResponseBodyDomainAttackEvents(TeaModel):
    def __init__(self, domain=None, end_time=None, max_qps=None, start_time=None):
        # The attacked domain name.
        self.domain = domain  # type: str
        # The time when the DDoS attack stopped. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: long
        # The peak attack QPS.
        self.max_qps = max_qps  # type: long
        # The time when the DDoS attack started. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainAttackEventsResponseBodyDomainAttackEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainAttackEventsResponseBody(TeaModel):
    def __init__(self, domain_attack_events=None, request_id=None, total_count=None):
        # An array that consists of the details of the DDoS attack event.
        self.domain_attack_events = domain_attack_events  # type: list[DescribeDomainAttackEventsResponseBodyDomainAttackEvents]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned DDoS attack events.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.domain_attack_events:
            for k in self.domain_attack_events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainAttackEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainAttackEvents'] = []
        if self.domain_attack_events is not None:
            for k in self.domain_attack_events:
                result['DomainAttackEvents'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_attack_events = []
        if m.get('DomainAttackEvents') is not None:
            for k in m.get('DomainAttackEvents'):
                temp_model = DescribeDomainAttackEventsResponseBodyDomainAttackEvents()
                self.domain_attack_events.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDomainAttackEventsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainAttackEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainAttackEventsResponse, self).to_map()
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
            temp_model = DescribeDomainAttackEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainOverviewRequest(TeaModel):
    def __init__(self, domain=None, end_time=None, resource_group_id=None, start_time=None):
        # The domain name of the website that you want to query. If you leave this parameter unspecified, the statistics on all domain names are queried.
        # 
        # > The domain name must be added to Anti-DDoS Pro or Anti-DDoS Premium. You can call the [DescribeDomains](~~91724~~) operation to query all the domain names that are added to Anti-DDoS Pro or Anti-DDoS Premium.
        self.domain = domain  # type: str
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds. If you leave this parameter unspecified, the current system time is used as the end time.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](~~94485~~).
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainOverviewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainOverviewResponseBody(TeaModel):
    def __init__(self, max_http=None, max_https=None, request_id=None):
        # The peak queries per second (QPS) during HTTP traffic scrubbing. Unit: QPS.
        self.max_http = max_http  # type: long
        # The peak QPS during HTTPS traffic scrubbing. Unit: QPS.
        self.max_https = max_https  # type: long
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainOverviewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_http is not None:
            result['MaxHttp'] = self.max_http
        if self.max_https is not None:
            result['MaxHttps'] = self.max_https
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxHttp') is not None:
            self.max_http = m.get('MaxHttp')
        if m.get('MaxHttps') is not None:
            self.max_https = m.get('MaxHttps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainOverviewResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainOverviewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainOverviewResponse, self).to_map()
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
            temp_model = DescribeDomainOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainQPSListRequest(TeaModel):
    def __init__(self, domain=None, end_time=None, interval=None, resource_group_id=None, start_time=None):
        # The domain name of the website. If you do not specify this parameter, the statistics on the QPS of all domain names are queried.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # The interval for returning data. Unit: seconds.
        self.interval = interval  # type: long
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainQPSListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainQPSListResponseBodyDomainQPSList(TeaModel):
    def __init__(self, attack_qps=None, cache_hits=None, index=None, max_attack_qps=None, max_normal_qps=None,
                 max_qps=None, time=None, total_count=None, total_qps=None):
        # The attack QPS.
        self.attack_qps = attack_qps  # type: long
        # The number of cache hits.
        self.cache_hits = cache_hits  # type: long
        # The index number of the returned data.
        self.index = index  # type: long
        # The peak attack QPS.
        self.max_attack_qps = max_attack_qps  # type: long
        # The peak of normal QPS.
        self.max_normal_qps = max_normal_qps  # type: long
        # The peak of total QPS.
        self.max_qps = max_qps  # type: long
        # The time when the data was collected. The value is a UNIX timestamp. Unit: seconds.
        self.time = time  # type: long
        # The total number of requests.
        self.total_count = total_count  # type: long
        # The total QPS.
        self.total_qps = total_qps  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainQPSListResponseBodyDomainQPSList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_qps is not None:
            result['AttackQps'] = self.attack_qps
        if self.cache_hits is not None:
            result['CacheHits'] = self.cache_hits
        if self.index is not None:
            result['Index'] = self.index
        if self.max_attack_qps is not None:
            result['MaxAttackQps'] = self.max_attack_qps
        if self.max_normal_qps is not None:
            result['MaxNormalQps'] = self.max_normal_qps
        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps
        if self.time is not None:
            result['Time'] = self.time
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_qps is not None:
            result['TotalQps'] = self.total_qps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttackQps') is not None:
            self.attack_qps = m.get('AttackQps')
        if m.get('CacheHits') is not None:
            self.cache_hits = m.get('CacheHits')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('MaxAttackQps') is not None:
            self.max_attack_qps = m.get('MaxAttackQps')
        if m.get('MaxNormalQps') is not None:
            self.max_normal_qps = m.get('MaxNormalQps')
        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalQps') is not None:
            self.total_qps = m.get('TotalQps')
        return self


class DescribeDomainQPSListResponseBody(TeaModel):
    def __init__(self, domain_qpslist=None, request_id=None):
        # An array that consists of the statistics on the QPS of the website.
        self.domain_qpslist = domain_qpslist  # type: list[DescribeDomainQPSListResponseBodyDomainQPSList]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_qpslist:
            for k in self.domain_qpslist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainQPSListResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainQPSListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainQPSListResponse, self).to_map()
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
            temp_model = DescribeDomainQPSListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainQpsWithCacheRequest(TeaModel):
    def __init__(self, domain=None, end_time=None, resource_group_id=None, start_time=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainQpsWithCacheRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainQpsWithCacheResponseBody(TeaModel):
    def __init__(self, blocks=None, cache_hits=None, cc_block_qps=None, cc_js_qps=None, interval=None,
                 ip_block_qps=None, precise_blocks=None, precise_js_qps=None, region_blocks=None, request_id=None,
                 start_time=None, totals=None):
        # An array that consists of the attack QPS.
        self.blocks = blocks  # type: list[str]
        # An array consisting of cache hit ratios.
        self.cache_hits = cache_hits  # type: list[str]
        # An array consisting of the QPS that is blocked by the Frequency Control policy.
        self.cc_block_qps = cc_block_qps  # type: list[str]
        # An array consisting of the QPS for which the Frequency Control policy triggers Completely Automated Public Turing test to tell Computers and Humans Apart (CAPTCHA).
        self.cc_js_qps = cc_js_qps  # type: list[str]
        # The intervals between every two adjacent records. Unit: seconds.
        self.interval = interval  # type: int
        # An array consisting of the QPS that is blocked by the blacklist for domain names.
        self.ip_block_qps = ip_block_qps  # type: list[str]
        # An array consisting of the QPS that is blocked by the Accurate Access Control policy.
        self.precise_blocks = precise_blocks  # type: list[str]
        # An array consisting of the QPS for which the Accurate Access Control policy triggers the JavaScript challenge.
        self.precise_js_qps = precise_js_qps  # type: list[str]
        # An array consisting of the QPS that is blocked by the Location Blacklist policy.
        self.region_blocks = region_blocks  # type: list[str]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The start time. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: long
        # An array consisting of the total QPS.
        self.totals = totals  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainQpsWithCacheResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blocks is not None:
            result['Blocks'] = self.blocks
        if self.cache_hits is not None:
            result['CacheHits'] = self.cache_hits
        if self.cc_block_qps is not None:
            result['CcBlockQps'] = self.cc_block_qps
        if self.cc_js_qps is not None:
            result['CcJsQps'] = self.cc_js_qps
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.ip_block_qps is not None:
            result['IpBlockQps'] = self.ip_block_qps
        if self.precise_blocks is not None:
            result['PreciseBlocks'] = self.precise_blocks
        if self.precise_js_qps is not None:
            result['PreciseJsQps'] = self.precise_js_qps
        if self.region_blocks is not None:
            result['RegionBlocks'] = self.region_blocks
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.totals is not None:
            result['Totals'] = self.totals
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Blocks') is not None:
            self.blocks = m.get('Blocks')
        if m.get('CacheHits') is not None:
            self.cache_hits = m.get('CacheHits')
        if m.get('CcBlockQps') is not None:
            self.cc_block_qps = m.get('CcBlockQps')
        if m.get('CcJsQps') is not None:
            self.cc_js_qps = m.get('CcJsQps')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IpBlockQps') is not None:
            self.ip_block_qps = m.get('IpBlockQps')
        if m.get('PreciseBlocks') is not None:
            self.precise_blocks = m.get('PreciseBlocks')
        if m.get('PreciseJsQps') is not None:
            self.precise_js_qps = m.get('PreciseJsQps')
        if m.get('RegionBlocks') is not None:
            self.region_blocks = m.get('RegionBlocks')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Totals') is not None:
            self.totals = m.get('Totals')
        return self


class DescribeDomainQpsWithCacheResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainQpsWithCacheResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainQpsWithCacheResponse, self).to_map()
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
            temp_model = DescribeDomainQpsWithCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainResourceRequest(TeaModel):
    def __init__(self, domain=None, instance_ids=None, page_number=None, page_size=None, query_domain_pattern=None):
        # The domain name of the website that you want to query.
        self.domain = domain  # type: str
        # An array that consists of the IDs of instances to query.
        self.instance_ids = instance_ids  # type: list[str]
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The match mode. Valid values:
        # 
        # *   **fuzzy**: fuzzy match. This is the default value.
        # *   **exact**: exact match.
        self.query_domain_pattern = query_domain_pattern  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_domain_pattern is not None:
            result['QueryDomainPattern'] = self.query_domain_pattern
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryDomainPattern') is not None:
            self.query_domain_pattern = m.get('QueryDomainPattern')
        return self


class DescribeDomainResourceResponseBodyWebRulesProxyTypes(TeaModel):
    def __init__(self, proxy_ports=None, proxy_type=None):
        # The port numbers.
        self.proxy_ports = proxy_ports  # type: list[str]
        # The type of the protocol. Valid values:
        # 
        # *   **http**\
        # *   **https**\
        # *   **websocket**\
        # *   **websockets**\
        self.proxy_type = proxy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainResourceResponseBodyWebRulesProxyTypes, self).to_map()
        if _map is not None:
            return _map

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


class DescribeDomainResourceResponseBodyWebRules(TeaModel):
    def __init__(self, black_list=None, cc_enabled=None, cc_rule_enabled=None, cc_template=None, cert_name=None,
                 cname=None, custom_ciphers=None, domain=None, http_2enable=None, http_2https_enable=None,
                 https_2http_enable=None, https_ext=None, instance_ids=None, ocsp_enabled=None, policy_mode=None, proxy_enabled=None,
                 proxy_types=None, punish_reason=None, punish_status=None, real_servers=None, rs_type=None, ssl_13enabled=None,
                 ssl_ciphers=None, ssl_protocols=None, white_list=None):
        # The IP addresses that are included in the blacklist of the domain name.
        self.black_list = black_list  # type: list[str]
        # Indicates whether the Frequency Control policy is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.cc_enabled = cc_enabled  # type: bool
        # Indicates whether the Custom Rule switch of the Frequency Control policy is turned on. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.cc_rule_enabled = cc_rule_enabled  # type: bool
        # The mode of the Frequency Control policy. Valid values:
        # 
        # *   **default**: the Normal mode
        # *   **gf_under_attack**: the Emergency mode
        # *   **gf_sos_verify**: the Strict mode
        # *   **gf_sos_verify**: the Super Strict mode
        self.cc_template = cc_template  # type: str
        # The name of the SSL certificate used by the domain name.
        self.cert_name = cert_name  # type: str
        # The CNAME provided by the instance to which the domain name is added.
        self.cname = cname  # type: str
        # The custom cipher suites.
        self.custom_ciphers = custom_ciphers  # type: list[str]
        # The domain name of the website.
        self.domain = domain  # type: str
        # Indicates whether Enable HTTP/2 is turned on. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.http_2enable = http_2enable  # type: bool
        # Indicates whether Enforce HTTPS Routing is turned on. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.http_2https_enable = http_2https_enable  # type: bool
        # Indicates whether Enable HTTP is turned on. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.https_2http_enable = https_2http_enable  # type: bool
        # The advanced HTTPS settings. This parameter takes effect only when the value of the **ProxyType** parameter includes **https**. The value is a string that consists of a JSON struct. The JSON struct contains the following fields:
        # 
        # *   **Http2https**: indicates whether the feature of redirecting HTTP requests to HTTPS requests is enabled. Data type: integer. Valid values: **0** and **1**. The value 0 indicates that the feature is disabled. The value 1 indicates that the feature is enabled.
        # *   **Https2http**: indicates whether the feature of redirecting HTTPS requests to HTTP requests is enabled. Data type: integer. Valid values: **0** and **1**. The value 0 indicates that the feature is disabled. The value 1 indicates that the feature is enabled.
        # *   **Http2**: indicates whether HTTP/2 is supported. Data type: integer. Valid values: **0** and **1**. The value 0 indicates that HTTP/2 is not supported. The value 1 indicates that HTTP/2 is supported.
        self.https_ext = https_ext  # type: str
        # The IDs of the instances to which the domain name is added.
        self.instance_ids = instance_ids  # type: list[str]
        # Indicates whether the Online Certificate Status Protocol (OCSP) feature is enabled. Valid values:
        # - **true**: yes
        # - **false**: no
        self.ocsp_enabled = ocsp_enabled  # type: bool
        # The load balancing algorithm for back-to-origin traffic. Valid values:
        # 
        # *   **ip_hash**: the IP hash algorithm. This algorithm is used to redirect the requests from the same IP address to the same origin server.
        # *   **rr**: the round-robin algorithm. This algorithm is used to redirect requests to origin servers in turn.
        # *   **least_time**: the least response time algorithm. This algorithm is used to minimize the latency when requests are forwarded from Anti-DDoS Pro or Anti-DDoS Premium instances to origin servers based on the intelligent DNS resolution feature.
        self.policy_mode = policy_mode  # type: str
        # Indicates whether the instance forwards the traffic that is destined for the website. Valid values:
        # 
        # *   **true**: Anti-DDoS Pro or Anti-DDoS Premium forwards the traffic that is destined for the website.
        # *   **false**: no
        self.proxy_enabled = proxy_enabled  # type: bool
        # The details about the protocol type and port number.
        self.proxy_types = proxy_types  # type: list[DescribeDomainResourceResponseBodyWebRulesProxyTypes]
        # The reason why the domain name is invalid. Valid values:
        # 
        # *   **1**: No Content Provider (ICP) filing is completed for the domain name.
        # *   **2**: The business for which you registered the domain name does not meet regulatory requirements.
        # 
        # If the two reasons are both involved, the value **2** is returned.
        self.punish_reason = punish_reason  # type: int
        # Indicates whether the domain name is invalid. Valid values:
        # 
        # *   **true**: The domain name is invalid. You can view the specific reasons from the **PunishReason** parameter.
        # *   **false**: The domain name is valid.
        self.punish_status = punish_status  # type: bool
        # The addresses of origin servers.
        self.real_servers = real_servers  # type: list[str]
        # The address type of the origin server. Valid values:
        # 
        # *   **0**: IP address
        # *   **1**: domain name
        self.rs_type = rs_type  # type: int
        # Indicates whether TLS 1.3 is supported. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.ssl_13enabled = ssl_13enabled  # type: bool
        # The type of the cipher suite. Valid values:
        # 
        # *   **default**: custom cipher suite
        # *   **all**: all cipher suites
        # *   **strong**: strong cipher suites
        self.ssl_ciphers = ssl_ciphers  # type: str
        # The version of the TLS protocol. Valid values:
        # 
        # *   **tls1.0**: TLS 1.0 or later
        # *   **tls1.1**: TLS 1.1 or later
        # *   **tls1.2**: TLS 1.2 or later
        self.ssl_protocols = ssl_protocols  # type: str
        # The IP addresses that are included in the whitelist of the domain name.
        self.white_list = white_list  # type: list[str]

    def validate(self):
        if self.proxy_types:
            for k in self.proxy_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainResourceResponseBodyWebRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_list is not None:
            result['BlackList'] = self.black_list
        if self.cc_enabled is not None:
            result['CcEnabled'] = self.cc_enabled
        if self.cc_rule_enabled is not None:
            result['CcRuleEnabled'] = self.cc_rule_enabled
        if self.cc_template is not None:
            result['CcTemplate'] = self.cc_template
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.custom_ciphers is not None:
            result['CustomCiphers'] = self.custom_ciphers
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.http_2enable is not None:
            result['Http2Enable'] = self.http_2enable
        if self.http_2https_enable is not None:
            result['Http2HttpsEnable'] = self.http_2https_enable
        if self.https_2http_enable is not None:
            result['Https2HttpEnable'] = self.https_2http_enable
        if self.https_ext is not None:
            result['HttpsExt'] = self.https_ext
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.ocsp_enabled is not None:
            result['OcspEnabled'] = self.ocsp_enabled
        if self.policy_mode is not None:
            result['PolicyMode'] = self.policy_mode
        if self.proxy_enabled is not None:
            result['ProxyEnabled'] = self.proxy_enabled
        result['ProxyTypes'] = []
        if self.proxy_types is not None:
            for k in self.proxy_types:
                result['ProxyTypes'].append(k.to_map() if k else None)
        if self.punish_reason is not None:
            result['PunishReason'] = self.punish_reason
        if self.punish_status is not None:
            result['PunishStatus'] = self.punish_status
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.ssl_13enabled is not None:
            result['Ssl13Enabled'] = self.ssl_13enabled
        if self.ssl_ciphers is not None:
            result['SslCiphers'] = self.ssl_ciphers
        if self.ssl_protocols is not None:
            result['SslProtocols'] = self.ssl_protocols
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')
        if m.get('CcEnabled') is not None:
            self.cc_enabled = m.get('CcEnabled')
        if m.get('CcRuleEnabled') is not None:
            self.cc_rule_enabled = m.get('CcRuleEnabled')
        if m.get('CcTemplate') is not None:
            self.cc_template = m.get('CcTemplate')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('CustomCiphers') is not None:
            self.custom_ciphers = m.get('CustomCiphers')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Http2Enable') is not None:
            self.http_2enable = m.get('Http2Enable')
        if m.get('Http2HttpsEnable') is not None:
            self.http_2https_enable = m.get('Http2HttpsEnable')
        if m.get('Https2HttpEnable') is not None:
            self.https_2http_enable = m.get('Https2HttpEnable')
        if m.get('HttpsExt') is not None:
            self.https_ext = m.get('HttpsExt')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OcspEnabled') is not None:
            self.ocsp_enabled = m.get('OcspEnabled')
        if m.get('PolicyMode') is not None:
            self.policy_mode = m.get('PolicyMode')
        if m.get('ProxyEnabled') is not None:
            self.proxy_enabled = m.get('ProxyEnabled')
        self.proxy_types = []
        if m.get('ProxyTypes') is not None:
            for k in m.get('ProxyTypes'):
                temp_model = DescribeDomainResourceResponseBodyWebRulesProxyTypes()
                self.proxy_types.append(temp_model.from_map(k))
        if m.get('PunishReason') is not None:
            self.punish_reason = m.get('PunishReason')
        if m.get('PunishStatus') is not None:
            self.punish_status = m.get('PunishStatus')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        if m.get('Ssl13Enabled') is not None:
            self.ssl_13enabled = m.get('Ssl13Enabled')
        if m.get('SslCiphers') is not None:
            self.ssl_ciphers = m.get('SslCiphers')
        if m.get('SslProtocols') is not None:
            self.ssl_protocols = m.get('SslProtocols')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class DescribeDomainResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, web_rules=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of forwarding rules.
        self.total_count = total_count  # type: long
        # The configurations of the forwarding rule.
        self.web_rules = web_rules  # type: list[DescribeDomainResourceResponseBodyWebRules]

    def validate(self):
        if self.web_rules:
            for k in self.web_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['WebRules'] = []
        if self.web_rules is not None:
            for k in self.web_rules:
                result['WebRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.web_rules = []
        if m.get('WebRules') is not None:
            for k in m.get('WebRules'):
                temp_model = DescribeDomainResourceResponseBodyWebRules()
                self.web_rules.append(temp_model.from_map(k))
        return self


class DescribeDomainResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainResourceResponse, self).to_map()
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
            temp_model = DescribeDomainResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSecurityProfileRequest(TeaModel):
    def __init__(self, domain=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSecurityProfileRequest, self).to_map()
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


class DescribeDomainSecurityProfileResponseBodyResult(TeaModel):
    def __init__(self, global_enable=None, global_mode=None):
        # Indicates whether the global mitigation policy is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.global_enable = global_enable  # type: bool
        # The mode of the global mitigation policy. Valid values:
        # 
        # *   **weak**: the Low mode
        # *   **default**: the Normal mode
        # *   **hard**: the Strict mode
        self.global_mode = global_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainSecurityProfileResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_enable is not None:
            result['GlobalEnable'] = self.global_enable
        if self.global_mode is not None:
            result['GlobalMode'] = self.global_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GlobalEnable') is not None:
            self.global_enable = m.get('GlobalEnable')
        if m.get('GlobalMode') is not None:
            self.global_mode = m.get('GlobalMode')
        return self


class DescribeDomainSecurityProfileResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The returned results.
        self.result = result  # type: list[DescribeDomainSecurityProfileResponseBodyResult]

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainSecurityProfileResponseBody, self).to_map()
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
                temp_model = DescribeDomainSecurityProfileResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeDomainSecurityProfileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainSecurityProfileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainSecurityProfileResponse, self).to_map()
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
            temp_model = DescribeDomainSecurityProfileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainStatusCodeCountRequest(TeaModel):
    def __init__(self, domain=None, end_time=None, resource_group_id=None, start_time=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainStatusCodeCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainStatusCodeCountResponseBody(TeaModel):
    def __init__(self, request_id=None, status_200=None, status_2xx=None, status_3xx=None, status_403=None,
                 status_404=None, status_405=None, status_4xx=None, status_501=None, status_502=None, status_503=None,
                 status_504=None, status_5xx=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The number of 200 status codes within the specified period of time.
        self.status_200 = status_200  # type: long
        # The number of 2xx status codes within the specified period of time.
        self.status_2xx = status_2xx  # type: long
        # The number of 3xx status codes within the specified period of time.
        self.status_3xx = status_3xx  # type: long
        # The number of 403 status codes within the specified period of time.
        self.status_403 = status_403  # type: long
        # The number of 404 status codes within the specified period of time.
        self.status_404 = status_404  # type: long
        # The number of 405 status codes within the specified period of time.
        self.status_405 = status_405  # type: long
        # The number of 4xx status codes within the specified period of time.
        self.status_4xx = status_4xx  # type: long
        # The number of 501 status codes within the specified period of time.
        self.status_501 = status_501  # type: long
        # The number of 502 status codes within the specified period of time.
        self.status_502 = status_502  # type: long
        # The number of 503 status codes within the specified period of time.
        self.status_503 = status_503  # type: long
        # The number of 504 status codes within the specified period of time.
        self.status_504 = status_504  # type: long
        # The number of 5xx status codes within the specified period of time.
        self.status_5xx = status_5xx  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainStatusCodeCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status_200 is not None:
            result['Status200'] = self.status_200
        if self.status_2xx is not None:
            result['Status2XX'] = self.status_2xx
        if self.status_3xx is not None:
            result['Status3XX'] = self.status_3xx
        if self.status_403 is not None:
            result['Status403'] = self.status_403
        if self.status_404 is not None:
            result['Status404'] = self.status_404
        if self.status_405 is not None:
            result['Status405'] = self.status_405
        if self.status_4xx is not None:
            result['Status4XX'] = self.status_4xx
        if self.status_501 is not None:
            result['Status501'] = self.status_501
        if self.status_502 is not None:
            result['Status502'] = self.status_502
        if self.status_503 is not None:
            result['Status503'] = self.status_503
        if self.status_504 is not None:
            result['Status504'] = self.status_504
        if self.status_5xx is not None:
            result['Status5XX'] = self.status_5xx
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status200') is not None:
            self.status_200 = m.get('Status200')
        if m.get('Status2XX') is not None:
            self.status_2xx = m.get('Status2XX')
        if m.get('Status3XX') is not None:
            self.status_3xx = m.get('Status3XX')
        if m.get('Status403') is not None:
            self.status_403 = m.get('Status403')
        if m.get('Status404') is not None:
            self.status_404 = m.get('Status404')
        if m.get('Status405') is not None:
            self.status_405 = m.get('Status405')
        if m.get('Status4XX') is not None:
            self.status_4xx = m.get('Status4XX')
        if m.get('Status501') is not None:
            self.status_501 = m.get('Status501')
        if m.get('Status502') is not None:
            self.status_502 = m.get('Status502')
        if m.get('Status503') is not None:
            self.status_503 = m.get('Status503')
        if m.get('Status504') is not None:
            self.status_504 = m.get('Status504')
        if m.get('Status5XX') is not None:
            self.status_5xx = m.get('Status5XX')
        return self


class DescribeDomainStatusCodeCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainStatusCodeCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainStatusCodeCountResponse, self).to_map()
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
            temp_model = DescribeDomainStatusCodeCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainStatusCodeListRequest(TeaModel):
    def __init__(self, domain=None, end_time=None, interval=None, query_type=None, resource_group_id=None,
                 start_time=None):
        # The domain name of the website. If you do not specify this parameter, the statistics on response status codes of all domain names are queried.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # The interval for returning data. Unit: seconds.
        self.interval = interval  # type: long
        # The source of the statistics. Valid values:
        # 
        # *   **gf**: Anti-DDoS Pro or Anti-DDoS Premium
        # *   **upstrem**: origin server
        self.query_type = query_type  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The start time of the event. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainStatusCodeListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainStatusCodeListResponseBodyStatusCodeList(TeaModel):
    def __init__(self, index=None, status_200=None, status_2xx=None, status_3xx=None, status_403=None,
                 status_404=None, status_405=None, status_4xx=None, status_501=None, status_502=None, status_503=None,
                 status_504=None, status_5xx=None, time=None):
        # The index number of the returned data.
        self.index = index  # type: int
        # The number of 200 status codes.
        self.status_200 = status_200  # type: long
        # The number of 2xx status codes.
        self.status_2xx = status_2xx  # type: long
        # The number of 3xx status codes.
        self.status_3xx = status_3xx  # type: long
        # The number of 403 status codes.
        self.status_403 = status_403  # type: long
        # The number of 404 status codes.
        self.status_404 = status_404  # type: long
        # The number of 405 status codes.
        self.status_405 = status_405  # type: long
        # The number of 4xx status codes.
        self.status_4xx = status_4xx  # type: long
        # The number of 501 status codes.
        self.status_501 = status_501  # type: long
        # The number of 502 status codes.
        self.status_502 = status_502  # type: long
        # The number of 503 status codes.
        self.status_503 = status_503  # type: long
        # The number of 504 status codes.
        self.status_504 = status_504  # type: long
        # The number of 5xx status codes.
        self.status_5xx = status_5xx  # type: long
        # The time when the data was collected. The value is a UNIX timestamp. Unit: seconds.
        self.time = time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainStatusCodeListResponseBodyStatusCodeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.status_200 is not None:
            result['Status200'] = self.status_200
        if self.status_2xx is not None:
            result['Status2XX'] = self.status_2xx
        if self.status_3xx is not None:
            result['Status3XX'] = self.status_3xx
        if self.status_403 is not None:
            result['Status403'] = self.status_403
        if self.status_404 is not None:
            result['Status404'] = self.status_404
        if self.status_405 is not None:
            result['Status405'] = self.status_405
        if self.status_4xx is not None:
            result['Status4XX'] = self.status_4xx
        if self.status_501 is not None:
            result['Status501'] = self.status_501
        if self.status_502 is not None:
            result['Status502'] = self.status_502
        if self.status_503 is not None:
            result['Status503'] = self.status_503
        if self.status_504 is not None:
            result['Status504'] = self.status_504
        if self.status_5xx is not None:
            result['Status5XX'] = self.status_5xx
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Status200') is not None:
            self.status_200 = m.get('Status200')
        if m.get('Status2XX') is not None:
            self.status_2xx = m.get('Status2XX')
        if m.get('Status3XX') is not None:
            self.status_3xx = m.get('Status3XX')
        if m.get('Status403') is not None:
            self.status_403 = m.get('Status403')
        if m.get('Status404') is not None:
            self.status_404 = m.get('Status404')
        if m.get('Status405') is not None:
            self.status_405 = m.get('Status405')
        if m.get('Status4XX') is not None:
            self.status_4xx = m.get('Status4XX')
        if m.get('Status501') is not None:
            self.status_501 = m.get('Status501')
        if m.get('Status502') is not None:
            self.status_502 = m.get('Status502')
        if m.get('Status503') is not None:
            self.status_503 = m.get('Status503')
        if m.get('Status504') is not None:
            self.status_504 = m.get('Status504')
        if m.get('Status5XX') is not None:
            self.status_5xx = m.get('Status5XX')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeDomainStatusCodeListResponseBody(TeaModel):
    def __init__(self, request_id=None, status_code_list=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The statistics on response status codes.
        self.status_code_list = status_code_list  # type: list[DescribeDomainStatusCodeListResponseBodyStatusCodeList]

    def validate(self):
        if self.status_code_list:
            for k in self.status_code_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainStatusCodeListResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainStatusCodeListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainStatusCodeListResponse, self).to_map()
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
            temp_model = DescribeDomainStatusCodeListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainTopAttackListRequest(TeaModel):
    def __init__(self, end_time=None, resource_group_id=None, start_time=None):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainTopAttackListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainTopAttackListResponseBodyAttackList(TeaModel):
    def __init__(self, attack=None, count=None, domain=None):
        # The attack QPS. Unit: QPS
        self.attack = attack  # type: long
        # The number of all QPS, which includes normal and attack QPS. Unit: QPS.
        self.count = count  # type: long
        # The domain name of the website.
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainTopAttackListResponseBodyAttackList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack is not None:
            result['Attack'] = self.attack
        if self.count is not None:
            result['Count'] = self.count
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attack') is not None:
            self.attack = m.get('Attack')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainTopAttackListResponseBody(TeaModel):
    def __init__(self, attack_list=None, request_id=None):
        # The peak QPS of the website.
        self.attack_list = attack_list  # type: list[DescribeDomainTopAttackListResponseBodyAttackList]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.attack_list:
            for k in self.attack_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainTopAttackListResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainTopAttackListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainTopAttackListResponse, self).to_map()
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
            temp_model = DescribeDomainTopAttackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainViewSourceCountriesRequest(TeaModel):
    def __init__(self, domain=None, end_time=None, resource_group_id=None, start_time=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainViewSourceCountriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainViewSourceCountriesResponseBodySourceCountrys(TeaModel):
    def __init__(self, count=None, country_id=None):
        # The total number of requests.
        self.count = count  # type: long
        # The abbreviation of the country or area. For more information, see the **Codes of countries and areas** section of the [Codes of administrative regions in China and codes of countries and areas](~~167926~~) topic. For example, **cn** indicates China, and **us** indicates the United States.
        self.country_id = country_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainViewSourceCountriesResponseBodySourceCountrys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        return self


class DescribeDomainViewSourceCountriesResponseBody(TeaModel):
    def __init__(self, request_id=None, source_countrys=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array consisting of the country or area from which the requests are sent.
        self.source_countrys = source_countrys  # type: list[DescribeDomainViewSourceCountriesResponseBodySourceCountrys]

    def validate(self):
        if self.source_countrys:
            for k in self.source_countrys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainViewSourceCountriesResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainViewSourceCountriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainViewSourceCountriesResponse, self).to_map()
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
            temp_model = DescribeDomainViewSourceCountriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainViewSourceProvincesRequest(TeaModel):
    def __init__(self, domain=None, end_time=None, resource_group_id=None, start_time=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainViewSourceProvincesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainViewSourceProvincesResponseBodySourceProvinces(TeaModel):
    def __init__(self, count=None, province_id=None):
        # The total number of requests.
        self.count = count  # type: long
        # The ID of the region inside China. For more information, see the **Codes of administrative regions in China** section of the [Codes of administrative regions in China and codes of countries and areas](~~167926~~) topic. For example, **110000** indicates Beijing, and **120000** indicates Tianjin.
        self.province_id = province_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainViewSourceProvincesResponseBodySourceProvinces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.province_id is not None:
            result['ProvinceId'] = self.province_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('ProvinceId') is not None:
            self.province_id = m.get('ProvinceId')
        return self


class DescribeDomainViewSourceProvincesResponseBody(TeaModel):
    def __init__(self, request_id=None, source_provinces=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array consisting of the details of the administrative region in China from which the requests are sent.
        self.source_provinces = source_provinces  # type: list[DescribeDomainViewSourceProvincesResponseBodySourceProvinces]

    def validate(self):
        if self.source_provinces:
            for k in self.source_provinces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainViewSourceProvincesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SourceProvinces'] = []
        if self.source_provinces is not None:
            for k in self.source_provinces:
                result['SourceProvinces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.source_provinces = []
        if m.get('SourceProvinces') is not None:
            for k in m.get('SourceProvinces'):
                temp_model = DescribeDomainViewSourceProvincesResponseBodySourceProvinces()
                self.source_provinces.append(temp_model.from_map(k))
        return self


class DescribeDomainViewSourceProvincesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainViewSourceProvincesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainViewSourceProvincesResponse, self).to_map()
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
            temp_model = DescribeDomainViewSourceProvincesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainViewTopCostTimeRequest(TeaModel):
    def __init__(self, domain=None, end_time=None, resource_group_id=None, start_time=None, top=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long
        # The number of URLs to query. Valid values: **1** to **100**.
        self.top = top  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainViewTopCostTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.top is not None:
            result['Top'] = self.top
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        return self


class DescribeDomainViewTopCostTimeResponseBodyUrlList(TeaModel):
    def __init__(self, cost_time=None, domain=None, url=None):
        # The response duration. Unit: milliseconds.
        self.cost_time = cost_time  # type: float
        # The domain name of the website.
        self.domain = domain  # type: str
        # The URL that is Base64-encoded.
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainViewTopCostTimeResponseBodyUrlList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeDomainViewTopCostTimeResponseBody(TeaModel):
    def __init__(self, request_id=None, url_list=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The URLs which require the longest time to respond to requests.
        self.url_list = url_list  # type: list[DescribeDomainViewTopCostTimeResponseBodyUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainViewTopCostTimeResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainViewTopCostTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainViewTopCostTimeResponse, self).to_map()
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
            temp_model = DescribeDomainViewTopCostTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainViewTopUrlRequest(TeaModel):
    def __init__(self, domain=None, end_time=None, resource_group_id=None, start_time=None, top=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long
        # The number of URLs to query. Valid values: **1** to **100**.
        self.top = top  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainViewTopUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.top is not None:
            result['Top'] = self.top
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        return self


class DescribeDomainViewTopUrlResponseBodyUrlList(TeaModel):
    def __init__(self, count=None, domain=None, url=None):
        # The total number of requests.
        self.count = count  # type: long
        # The domain name of the website.
        self.domain = domain  # type: str
        # The URL that is Base64-encoded.
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainViewTopUrlResponseBodyUrlList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeDomainViewTopUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, url_list=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array consisting of the URLs that receive the most requests.
        self.url_list = url_list  # type: list[DescribeDomainViewTopUrlResponseBodyUrlList]

    def validate(self):
        if self.url_list:
            for k in self.url_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDomainViewTopUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDomainViewTopUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDomainViewTopUrlResponse, self).to_map()
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
            temp_model = DescribeDomainViewTopUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainsRequest(TeaModel):
    def __init__(self, instance_ids=None, resource_group_id=None):
        # The ID of the instance that you want to query.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_ids = instance_ids  # type: list[str]
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](~~94485~~).
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDomainsResponseBody(TeaModel):
    def __init__(self, domains=None, request_id=None):
        # An array consisting of details of the domain name for which the forwarding rules are configured.
        self.domains = domains  # type: list[str]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDomainsResponseBody, self).to_map()
        if _map is not None:
            return _map

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


class DescribeElasticBandwidthSpecRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeElasticBandwidthSpecRequest, self).to_map()
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


class DescribeElasticBandwidthSpecResponseBody(TeaModel):
    def __init__(self, elastic_bandwidth_spec=None, request_id=None):
        # An array that consists of the available burstable protection bandwidths. Unit: Gbit/s.
        self.elastic_bandwidth_spec = elastic_bandwidth_spec  # type: list[str]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeElasticBandwidthSpecResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_bandwidth_spec is not None:
            result['ElasticBandwidthSpec'] = self.elastic_bandwidth_spec
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ElasticBandwidthSpec') is not None:
            self.elastic_bandwidth_spec = m.get('ElasticBandwidthSpec')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeElasticBandwidthSpecResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeElasticBandwidthSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeElasticBandwidthSpecResponse, self).to_map()
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
            temp_model = DescribeElasticBandwidthSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHeadersRequest(TeaModel):
    def __init__(self, domain=None, resource_group_id=None):
        # The domain name that you want to query.
        # 
        # > You can call the [DescribeDomains](~~91724~~) operation to query all the domain names that are added to Anti-DDoS Pro or Anti-DDoS Premium.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHeadersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeHeadersResponseBodyCustomHeader(TeaModel):
    def __init__(self, domain=None, headers=None):
        # The domain name of the website.
        self.domain = domain  # type: str
        # The header of the response.
        self.headers = headers  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHeadersResponseBodyCustomHeader, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.headers is not None:
            result['Headers'] = self.headers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')
        return self


class DescribeHeadersResponseBody(TeaModel):
    def __init__(self, custom_header=None, request_id=None):
        # The information about the custom header.
        self.custom_header = custom_header  # type: DescribeHeadersResponseBodyCustomHeader
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.custom_header:
            self.custom_header.validate()

    def to_map(self):
        _map = super(DescribeHeadersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_header is not None:
            result['CustomHeader'] = self.custom_header.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomHeader') is not None:
            temp_model = DescribeHeadersResponseBodyCustomHeader()
            self.custom_header = temp_model.from_map(m['CustomHeader'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHeadersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHeadersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHeadersResponse, self).to_map()
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
            temp_model = DescribeHeadersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHealthCheckListRequest(TeaModel):
    def __init__(self, network_rules=None):
        # The information about the port forwarding rule. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **InstanceId**: the ID of the instance. This field is required and must be of the STRING type.
        # *   **Protocol**: the forwarding protocol. This field is required and must be of the STRING type. Valid values: **tcp** and **udp**.
        # *   **FrontendPort**: the forwarding port. This field is required and must be of the INTEGER type.
        self.network_rules = network_rules  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthCheckListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkRules') is not None:
            self.network_rules = m.get('NetworkRules')
        return self


class DescribeHealthCheckListResponseBodyHealthCheckListHealthCheck(TeaModel):
    def __init__(self, domain=None, down=None, interval=None, port=None, timeout=None, type=None, up=None, uri=None):
        # The domain name.
        # 
        # > This parameter is returned only when the Layer 7 health check configuration is queried.
        self.domain = domain  # type: str
        # The number of consecutive failed health checks that must occur before a port is declared unhealthy. Valid values: **1** to **10**.
        self.down = down  # type: int
        # The interval at which checks are performed. Valid values: **1** to **30**. Unit: seconds.
        self.interval = interval  # type: int
        # The port that was checked.
        self.port = port  # type: int
        # The response timeout period. Valid values: **1** to **30**. Unit: seconds.
        self.timeout = timeout  # type: int
        # The type of the protocol. Valid values:
        # 
        # *   **tcp**: The Layer 4 health check configuration was queried.
        # *   **http**: The Layer 7 health check configuration was queried.
        self.type = type  # type: str
        # The number of consecutive successful health checks that must occur before a port is declared healthy. Valid values: **1** to **10**.
        self.up = up  # type: int
        # The check path.
        # 
        # > This parameter is returned only when the Layer 7 health check configuration is queried.
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthCheckListResponseBodyHealthCheckListHealthCheck, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.down is not None:
            result['Down'] = self.down
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.port is not None:
            result['Port'] = self.port
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.type is not None:
            result['Type'] = self.type
        if self.up is not None:
            result['Up'] = self.up
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Down') is not None:
            self.down = m.get('Down')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Up') is not None:
            self.up = m.get('Up')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DescribeHealthCheckListResponseBodyHealthCheckList(TeaModel):
    def __init__(self, frontend_port=None, health_check=None, instance_id=None, protocol=None):
        # The forwarding port.
        self.frontend_port = frontend_port  # type: int
        # The health check configuration.
        self.health_check = health_check  # type: DescribeHealthCheckListResponseBodyHealthCheckListHealthCheck
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The forwarding protocol. Valid values:
        # 
        # *   **tcp**\
        # *   **udp**\
        self.protocol = protocol  # type: str

    def validate(self):
        if self.health_check:
            self.health_check.validate()

    def to_map(self):
        _map = super(DescribeHealthCheckListResponseBodyHealthCheckList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('HealthCheck') is not None:
            temp_model = DescribeHealthCheckListResponseBodyHealthCheckListHealthCheck()
            self.health_check = temp_model.from_map(m['HealthCheck'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeHealthCheckListResponseBody(TeaModel):
    def __init__(self, health_check_list=None, request_id=None):
        # An array that consists of information about the health check configuration.
        self.health_check_list = health_check_list  # type: list[DescribeHealthCheckListResponseBodyHealthCheckList]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.health_check_list:
            for k in self.health_check_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHealthCheckListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HealthCheckList'] = []
        if self.health_check_list is not None:
            for k in self.health_check_list:
                result['HealthCheckList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.health_check_list = []
        if m.get('HealthCheckList') is not None:
            for k in m.get('HealthCheckList'):
                temp_model = DescribeHealthCheckListResponseBodyHealthCheckList()
                self.health_check_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHealthCheckListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHealthCheckListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHealthCheckListResponse, self).to_map()
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
            temp_model = DescribeHealthCheckListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHealthCheckStatusRequest(TeaModel):
    def __init__(self, network_rules=None):
        # An array that consists of the details of the port forwarding rule. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **InstanceId**: the ID of the instance. This field is required and must be of the STRING type.
        # *   **Protocol**: the forwarding protocol. This field is required and must be of the STRING type. Valid values: **tcp** and **udp**.
        # *   **FrontendPort**: the forwarding port. This field is required and must be of the INTEGER type.
        self.network_rules = network_rules  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthCheckStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkRules') is not None:
            self.network_rules = m.get('NetworkRules')
        return self


class DescribeHealthCheckStatusResponseBodyHealthCheckStatusRealServerStatusList(TeaModel):
    def __init__(self, address=None, status=None):
        # The IP address of the origin server.
        self.address = address  # type: str
        # The health state of the IP address. Valid values:
        # 
        # *   **normal**: healthy
        # *   **abnormal**: unhealthy
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHealthCheckStatusResponseBodyHealthCheckStatusRealServerStatusList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeHealthCheckStatusResponseBodyHealthCheckStatus(TeaModel):
    def __init__(self, frontend_port=None, instance_id=None, protocol=None, real_server_status_list=None,
                 status=None):
        # The forwarding port.
        self.frontend_port = frontend_port  # type: int
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The forwarding protocol. Valid values:
        # 
        # *   **tcp**\
        # *   **udp**\
        self.protocol = protocol  # type: str
        # An array that consists of the health states of the IP addresses of the origin server.
        self.real_server_status_list = real_server_status_list  # type: list[DescribeHealthCheckStatusResponseBodyHealthCheckStatusRealServerStatusList]
        # The health status of the origin server. Valid values:
        # 
        # *   **normal**: healthy
        # *   **abnormal**: unhealthy
        self.status = status  # type: str

    def validate(self):
        if self.real_server_status_list:
            for k in self.real_server_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHealthCheckStatusResponseBodyHealthCheckStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        result['RealServerStatusList'] = []
        if self.real_server_status_list is not None:
            for k in self.real_server_status_list:
                result['RealServerStatusList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        self.real_server_status_list = []
        if m.get('RealServerStatusList') is not None:
            for k in m.get('RealServerStatusList'):
                temp_model = DescribeHealthCheckStatusResponseBodyHealthCheckStatusRealServerStatusList()
                self.real_server_status_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeHealthCheckStatusResponseBody(TeaModel):
    def __init__(self, health_check_status=None, request_id=None):
        # An array that consists of the details of the health status of the origin server.
        self.health_check_status = health_check_status  # type: list[DescribeHealthCheckStatusResponseBodyHealthCheckStatus]
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.health_check_status:
            for k in self.health_check_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHealthCheckStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HealthCheckStatus'] = []
        if self.health_check_status is not None:
            for k in self.health_check_status:
                result['HealthCheckStatus'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.health_check_status = []
        if m.get('HealthCheckStatus') is not None:
            for k in m.get('HealthCheckStatus'):
                temp_model = DescribeHealthCheckStatusResponseBodyHealthCheckStatus()
                self.health_check_status.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHealthCheckStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHealthCheckStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHealthCheckStatusResponse, self).to_map()
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
            temp_model = DescribeHealthCheckStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceDetailsRequest(TeaModel):
    def __init__(self, instance_ids=None):
        # An array that consists of the IDs of instances to query.
        self.instance_ids = instance_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceDetailsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfos(TeaModel):
    def __init__(self, eip=None, ip_mode=None, ip_version=None, status=None):
        # The IP address of the instance.
        self.eip = eip  # type: str
        # The IP address-based forwarding mode of the instance. Valid values:
        # 
        # *   **fnat**: Requests from IPv4 addresses are forwarded to origin servers that use IPv4 addresses and requests from IPv6 addresses are forwarded to origin servers that use IPv6 addresses.
        # *   **v6tov4**: All requests are forwarded to origin servers that use IPv4 addresses.
        self.ip_mode = ip_mode  # type: str
        # The IP version of the protocol. Valid values:
        # 
        # *   **Ipv4**: IPv4
        # *   **Ipv6**: IPv6
        self.ip_version = ip_version  # type: str
        # The status of the instance. Valid values:
        # 
        # *   **normal**: indicates that the instance is normal.
        # *   **expired**: indicates that the instance expired.
        # *   **defense**: indicates that traffic scrubbing is performed on the asset that is protected by the instance.
        # *   **blackhole**: indicates that blackhole filtering is triggered for the asset that is protected by the instance.
        # *   **punished**: indicates that the instance is in penalty.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.ip_mode is not None:
            result['IpMode'] = self.ip_mode
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('IpMode') is not None:
            self.ip_mode = m.get('IpMode')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeInstanceDetailsResponseBodyInstanceDetails(TeaModel):
    def __init__(self, eip_infos=None, instance_id=None, line=None):
        # The information about the IP address of the instance.
        self.eip_infos = eip_infos  # type: list[DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfos]
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The protection line of the instance.
        self.line = line  # type: str

    def validate(self):
        if self.eip_infos:
            for k in self.eip_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceDetailsResponseBodyInstanceDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EipInfos'] = []
        if self.eip_infos is not None:
            for k in self.eip_infos:
                result['EipInfos'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.eip_infos = []
        if m.get('EipInfos') is not None:
            for k in m.get('EipInfos'):
                temp_model = DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfos()
                self.eip_infos.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        return self


class DescribeInstanceDetailsResponseBody(TeaModel):
    def __init__(self, instance_details=None, request_id=None):
        # The IP address and ISP line information about the instance.
        self.instance_details = instance_details  # type: list[DescribeInstanceDetailsResponseBodyInstanceDetails]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_details:
            for k in self.instance_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceDetailsResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceDetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceDetailsResponse, self).to_map()
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
            temp_model = DescribeInstanceDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceIdsRequest(TeaModel):
    def __init__(self, edition=None, instance_ids=None, resource_group_id=None):
        self.edition = edition  # type: int
        self.instance_ids = instance_ids  # type: list[str]
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceIdsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeInstanceIdsResponseBodyInstanceIds(TeaModel):
    def __init__(self, edition=None, instance_id=None, ip_mode=None, ip_version=None, remark=None):
        self.edition = edition  # type: int
        self.instance_id = instance_id  # type: str
        self.ip_mode = ip_mode  # type: str
        self.ip_version = ip_version  # type: str
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceIdsResponseBodyInstanceIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_mode is not None:
            result['IpMode'] = self.ip_mode
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpMode') is not None:
            self.ip_mode = m.get('IpMode')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class DescribeInstanceIdsResponseBody(TeaModel):
    def __init__(self, instance_ids=None, request_id=None):
        self.instance_ids = instance_ids  # type: list[DescribeInstanceIdsResponseBodyInstanceIds]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_ids:
            for k in self.instance_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceIdsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceIds'] = []
        if self.instance_ids is not None:
            for k in self.instance_ids:
                result['InstanceIds'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_ids = []
        if m.get('InstanceIds') is not None:
            for k in m.get('InstanceIds'):
                temp_model = DescribeInstanceIdsResponseBodyInstanceIds()
                self.instance_ids.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceIdsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceIdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceIdsResponse, self).to_map()
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
            temp_model = DescribeInstanceIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSpecsRequest(TeaModel):
    def __init__(self, instance_ids=None):
        # An array that consists of the IDs of instances to query.
        self.instance_ids = instance_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceSpecsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeInstanceSpecsResponseBodyInstanceSpecs(TeaModel):
    def __init__(self, bandwidth_mbps=None, base_bandwidth=None, conn_limit=None, cps_limit=None,
                 defense_count=None, domain_limit=None, elastic_bandwidth=None, elastic_bw=None, elastic_bw_model=None,
                 elastic_qps=None, elastic_qps_mode=None, function_version=None, instance_id=None, port_limit=None,
                 qps_limit=None, real_limit_bw=None, site_limit=None):
        # The clean bandwidth of normal services. Unit: Mbit/s.
        self.bandwidth_mbps = bandwidth_mbps  # type: int
        # The basic protection bandwidth. Unit: Gbit/s.
        self.base_bandwidth = base_bandwidth  # type: int
        # The specification of concurrent connections of the instance.
        self.conn_limit = conn_limit  # type: long
        # The specification of new connections of the instance.
        self.cps_limit = cps_limit  # type: long
        # The number of available advanced mitigation sessions for this month. If **-1** is returned, advanced mitigation capabilities are unlimited.
        # 
        # > This parameter is returned only when **RegionId** is set to **ap-southeast-1**. If RegionId is set to ap-southeast-1, the specifications of Anti-DDoS Premium instances are queried.
        self.defense_count = defense_count  # type: int
        # The number of domain names that can be protected by the instance.
        self.domain_limit = domain_limit  # type: int
        # The burstable protection bandwidth. Unit: Gbit/s.
        self.elastic_bandwidth = elastic_bandwidth  # type: int
        # The burstable clean bandwidth. Unit: Mbit/s.
        self.elastic_bw = elastic_bw  # type: int
        # The metering method of the burstable clean bandwidth. Valid values:
        # 
        # *   **day**: the metering method of daily 95th percentile
        # *   **month**: the metering method of monthly 95th percentile
        self.elastic_bw_model = elastic_bw_model  # type: str
        self.elastic_qps = elastic_qps  # type: long
        self.elastic_qps_mode = elastic_qps_mode  # type: str
        # The function plan of the instance. Valid values:
        # 
        # *   **default**: Standard
        # *   **enhance**: Enhanced
        # *   **cnhk**: Chinese Mainland Acceleration (CMA)
        # *   **cnhk_default**: Secure Chinese Mainland Acceleration (Sec-CMA) standard function plan
        # *   **cnhk_enhance**: Sec-CMA enhanced function plan
        self.function_version = function_version  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The number of ports that can be protected by the instance.
        self.port_limit = port_limit  # type: int
        # The clean queries per second (QPS) of normal services.
        self.qps_limit = qps_limit  # type: int
        # 实例业务带宽限速值。取值：0～15360，0表示不限速。单位：mbps。
        self.real_limit_bw = real_limit_bw  # type: long
        # The number of sites that can be protected by the instance.
        self.site_limit = site_limit  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceSpecsResponseBodyInstanceSpecs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_mbps is not None:
            result['BandwidthMbps'] = self.bandwidth_mbps
        if self.base_bandwidth is not None:
            result['BaseBandwidth'] = self.base_bandwidth
        if self.conn_limit is not None:
            result['ConnLimit'] = self.conn_limit
        if self.cps_limit is not None:
            result['CpsLimit'] = self.cps_limit
        if self.defense_count is not None:
            result['DefenseCount'] = self.defense_count
        if self.domain_limit is not None:
            result['DomainLimit'] = self.domain_limit
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth
        if self.elastic_bw is not None:
            result['ElasticBw'] = self.elastic_bw
        if self.elastic_bw_model is not None:
            result['ElasticBwModel'] = self.elastic_bw_model
        if self.elastic_qps is not None:
            result['ElasticQps'] = self.elastic_qps
        if self.elastic_qps_mode is not None:
            result['ElasticQpsMode'] = self.elastic_qps_mode
        if self.function_version is not None:
            result['FunctionVersion'] = self.function_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port_limit is not None:
            result['PortLimit'] = self.port_limit
        if self.qps_limit is not None:
            result['QpsLimit'] = self.qps_limit
        if self.real_limit_bw is not None:
            result['RealLimitBw'] = self.real_limit_bw
        if self.site_limit is not None:
            result['SiteLimit'] = self.site_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandwidthMbps') is not None:
            self.bandwidth_mbps = m.get('BandwidthMbps')
        if m.get('BaseBandwidth') is not None:
            self.base_bandwidth = m.get('BaseBandwidth')
        if m.get('ConnLimit') is not None:
            self.conn_limit = m.get('ConnLimit')
        if m.get('CpsLimit') is not None:
            self.cps_limit = m.get('CpsLimit')
        if m.get('DefenseCount') is not None:
            self.defense_count = m.get('DefenseCount')
        if m.get('DomainLimit') is not None:
            self.domain_limit = m.get('DomainLimit')
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')
        if m.get('ElasticBw') is not None:
            self.elastic_bw = m.get('ElasticBw')
        if m.get('ElasticBwModel') is not None:
            self.elastic_bw_model = m.get('ElasticBwModel')
        if m.get('ElasticQps') is not None:
            self.elastic_qps = m.get('ElasticQps')
        if m.get('ElasticQpsMode') is not None:
            self.elastic_qps_mode = m.get('ElasticQpsMode')
        if m.get('FunctionVersion') is not None:
            self.function_version = m.get('FunctionVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PortLimit') is not None:
            self.port_limit = m.get('PortLimit')
        if m.get('QpsLimit') is not None:
            self.qps_limit = m.get('QpsLimit')
        if m.get('RealLimitBw') is not None:
            self.real_limit_bw = m.get('RealLimitBw')
        if m.get('SiteLimit') is not None:
            self.site_limit = m.get('SiteLimit')
        return self


class DescribeInstanceSpecsResponseBody(TeaModel):
    def __init__(self, instance_specs=None, request_id=None):
        # An array that consists of the specifications of instances.
        self.instance_specs = instance_specs  # type: list[DescribeInstanceSpecsResponseBodyInstanceSpecs]
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_specs:
            for k in self.instance_specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceSpecsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceSpecs'] = []
        if self.instance_specs is not None:
            for k in self.instance_specs:
                result['InstanceSpecs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_specs = []
        if m.get('InstanceSpecs') is not None:
            for k in m.get('InstanceSpecs'):
                temp_model = DescribeInstanceSpecsResponseBodyInstanceSpecs()
                self.instance_specs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceSpecsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceSpecsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceSpecsResponse, self).to_map()
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
            temp_model = DescribeInstanceSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceStatisticsRequest(TeaModel):
    def __init__(self, instance_ids=None):
        # The ID of the instance that you want to query.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_ids = instance_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribeInstanceStatisticsResponseBodyInstanceStatistics(TeaModel):
    def __init__(self, defense_count_usage=None, domain_usage=None, instance_id=None, port_usage=None,
                 site_usage=None):
        # The number of advanced mitigation sessions that are used in this month.
        # 
        # > This parameter is returned only if Anti-DDoS Premium instances are queried.
        self.defense_count_usage = defense_count_usage  # type: int
        # The number of domain names that are protected by the instance.
        self.domain_usage = domain_usage  # type: int
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The number of ports that are protected by the instance.
        self.port_usage = port_usage  # type: int
        # The number of websites that are protected by the instance.
        self.site_usage = site_usage  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceStatisticsResponseBodyInstanceStatistics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_count_usage is not None:
            result['DefenseCountUsage'] = self.defense_count_usage
        if self.domain_usage is not None:
            result['DomainUsage'] = self.domain_usage
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port_usage is not None:
            result['PortUsage'] = self.port_usage
        if self.site_usage is not None:
            result['SiteUsage'] = self.site_usage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DefenseCountUsage') is not None:
            self.defense_count_usage = m.get('DefenseCountUsage')
        if m.get('DomainUsage') is not None:
            self.domain_usage = m.get('DomainUsage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PortUsage') is not None:
            self.port_usage = m.get('PortUsage')
        if m.get('SiteUsage') is not None:
            self.site_usage = m.get('SiteUsage')
        return self


class DescribeInstanceStatisticsResponseBody(TeaModel):
    def __init__(self, instance_statistics=None, request_id=None):
        # The statistics on the instances.
        self.instance_statistics = instance_statistics  # type: list[DescribeInstanceStatisticsResponseBodyInstanceStatistics]
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_statistics:
            for k in self.instance_statistics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceStatisticsResponse, self).to_map()
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
            temp_model = DescribeInstanceStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceStatusRequest(TeaModel):
    def __init__(self, instance_id=None, product_type=None):
        # The ID of the instance to query.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all Anti-DDoS Pro or Anti-DDoS Premium instances.
        self.instance_id = instance_id  # type: str
        # The type of the instance to query. Valid values:
        # 
        # *   **1**: an Anti-DDoS Pro instance
        # *   **2**: an Anti-DDoS Premium instance
        self.product_type = product_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class DescribeInstanceStatusResponseBody(TeaModel):
    def __init__(self, instance_id=None, instance_status=None, request_id=None):
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The status of the instance. Valid values:
        # 
        # *   **1**: normal
        # *   **2**: expired
        # *   **3**: overdue
        # *   **4**: released
        self.instance_status = instance_status  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceStatusResponse, self).to_map()
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
            temp_model = DescribeInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N that is added to the instance to query. The maximum value of N is 200. You can specify up to 200 tags. When you specify tags, take note of the following rules:
        # 
        # *   Each tag consists of a key (**Key**) and a value (**Value**), which are separated by a comma (,).
        # *   Separate multiple tags with commas (,).
        # 
        # >  The tag key (**Key**) and tag value (**Value**) must be specified in pairs.
        self.key = key  # type: str
        # The value of tag N that is added to the instance to query. The maximum value of N is 200. You can specify up to 200 tags. When you specify tags, take note of the following rules:
        # 
        # *   Each tag consists of a key (**Key**) and a value (**Value**), which are separated by a comma (,).
        # *   Separate multiple tags with commas (,).
        # 
        # >  The tag key (**Key**) and tag value (**Value**) must be specified in pairs.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesRequestTag, self).to_map()
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


class DescribeInstancesRequest(TeaModel):
    def __init__(self, edition=None, enabled=None, expire_end_time=None, expire_start_time=None, instance_ids=None,
                 ip=None, page_number=None, page_size=None, remark=None, resource_group_id=None, status=None, tag=None):
        # The mitigation plan of the instance to query. Valid values:
        # 
        # *   **0**: Anti-DDoS Premium instance of the Insurance mitigation plan
        # *   **1**: Anti-DDoS Premium instance of the Unlimited mitigation plan
        # *   **2**: Anti-DDoS Premium instance of the Mainland China Acceleration (MCA) mitigation plan
        # *   **9**: Anti-DDoS Pro instance of the Profession mitigation plan
        self.edition = edition  # type: int
        # The traffic forwarding status of the instance to query. Valid values:
        # 
        # *   **0**: The instance no longer forwards service traffic.
        # *   **1**: The instance forwards service traffic as expected.
        self.enabled = enabled  # type: int
        # The end of the time range to query. Instances whose expiration time is earlier than the point in time are queried. This value is a UNIX timestamp. Unit: milliseconds.
        self.expire_end_time = expire_end_time  # type: long
        # The beginning of the time range to query. Instances whose expiration time is later than the point in time are queried. This value is a UNIX timestamp. Unit: milliseconds.
        self.expire_start_time = expire_start_time  # type: long
        self.instance_ids = instance_ids  # type: list[str]
        # The IP address of the instance to query.
        self.ip = ip  # type: str
        # The number of the page to return.
        self.page_number = page_number  # type: str
        # The number of entries to return on each page.
        self.page_size = page_size  # type: str
        # The remarks of the instance to query. Fuzzy match is supported.
        self.remark = remark  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: list[int]
        self.tag = tag  # type: list[DescribeInstancesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.expire_end_time is not None:
            result['ExpireEndTime'] = self.expire_end_time
        if self.expire_start_time is not None:
            result['ExpireStartTime'] = self.expire_start_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('ExpireEndTime') is not None:
            self.expire_end_time = m.get('ExpireEndTime')
        if m.get('ExpireStartTime') is not None:
            self.expire_start_time = m.get('ExpireStartTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(self, create_time=None, debt_status=None, edition=None, enabled=None, expire_time=None,
                 instance_id=None, ip=None, ip_mode=None, ip_version=None, is_first_open_bw=None, is_first_open_qps=None,
                 remark=None, status=None):
        # The time when the instance is created. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time  # type: long
        # The overdue status of the instance. The value is fixed as **0**, which indicates that your Alibaba Cloud account does not have overdue payments. The instance supports only the subscription billing method.
        self.debt_status = debt_status  # type: int
        # The mitigation plan of the instance. Valid values:
        # 
        # *   **0**: Anti-DDoS Premium instance of the Insurance mitigation plan
        # *   **1**: Anti-DDoS Premium instance of the Unlimited mitigation plan
        # *   **2**: Anti-DDoS Premium instance of the MCA mitigation plan
        # *   **9**: Anti-DDoS Pro instance of the Profession mitigation plan
        self.edition = edition  # type: int
        # The forwarding status of the instance. Valid values:
        # 
        # *   **0**: The instance no longer forwards service traffic.
        # *   **1**: The instance forwards service traffic as expected.
        self.enabled = enabled  # type: int
        # The time when the instance expires. This value is a UNIX timestamp. Unit: milliseconds.
        self.expire_time = expire_time  # type: long
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The IP address of the instance.
        self.ip = ip  # type: str
        # The IP address-based forwarding mode of the instance. Valid values:
        # 
        # *   **fnat**: Requests from IPv4 addresses are forwarded to origin servers that use IPv4 addresses and requests from IPv6 addresses are forwarded to origin servers that use IPv6 addresses.
        # *   **v6tov4**: All requests are forwarded to origin servers that use IPv4 addresses.
        self.ip_mode = ip_mode  # type: str
        # The IP version of the instance. Valid values:
        # 
        # *   **Ipv4**: IPv4
        # *   **Ipv6**: IPv6
        self.ip_version = ip_version  # type: str
        # Indicates whether the 95th percentile metering method has been enabled for the instance. Valid values:
        # 
        # *   0: The 95th percentile metering method has not been enabled for the instance.
        # *   1: The 95th percentile metering method has been enabled for the instance.
        self.is_first_open_bw = is_first_open_bw  # type: long
        # Indicates whether the metering method of the 95th percentile burstable QPS is enabled for the instance. Valid values:
        # 
        # - 0: no
        # - 1: yes
        self.is_first_open_qps = is_first_open_qps  # type: long
        # The remarks of the instance.
        self.remark = remark  # type: str
        # The status of the instance. Valid values:
        # 
        # *   **1**: normal
        # *   **2**: expired
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.debt_status is not None:
            result['DebtStatus'] = self.debt_status
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.ip_mode is not None:
            result['IpMode'] = self.ip_mode
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.is_first_open_bw is not None:
            result['IsFirstOpenBw'] = self.is_first_open_bw
        if self.is_first_open_qps is not None:
            result['IsFirstOpenQps'] = self.is_first_open_qps
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DebtStatus') is not None:
            self.debt_status = m.get('DebtStatus')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IpMode') is not None:
            self.ip_mode = m.get('IpMode')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('IsFirstOpenBw') is not None:
            self.is_first_open_bw = m.get('IsFirstOpenBw')
        if m.get('IsFirstOpenQps') is not None:
            self.is_first_open_qps = m.get('IsFirstOpenQps')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(self, instances=None, request_id=None, total_count=None):
        # An array that consists of the details of the instances.
        self.instances = instances  # type: list[DescribeInstancesResponseBodyInstances]
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The total number of the instances.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponse, self).to_map()
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
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeL7RsPolicyRequest(TeaModel):
    def __init__(self, domain=None, real_servers=None, resource_group_id=None):
        # The domain name of the website to query.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query the domain names for which forwarding rules are configured.
        self.domain = domain  # type: str
        # An array that consists of N addresses of origin servers to query. The maximum value of N is 200. You can specify up to 200 addresses.
        self.real_servers = real_servers  # type: list[str]
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](~~94485~~).
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeL7RsPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeL7RsPolicyResponseBodyAttributesAttribute(TeaModel):
    def __init__(self, weight=None):
        # The weight of the origin server. This parameter takes effect only when **ProxyMode** is set to **rr**.
        # 
        # Valid values: **1** to **100**. Default value: **100**. A server with a higher weight receives more requests.
        self.weight = weight  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeL7RsPolicyResponseBodyAttributesAttribute, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, attribute=None, real_server=None, rs_type=None):
        # The parameter for back-to-origin.
        self.attribute = attribute  # type: DescribeL7RsPolicyResponseBodyAttributesAttribute
        # The address of the origin server.
        self.real_server = real_server  # type: str
        # The address type of the origin server. Valid values:
        # 
        # *   **0**: IP address
        # *   **1**: domain name
        self.rs_type = rs_type  # type: int

    def validate(self):
        if self.attribute:
            self.attribute.validate()

    def to_map(self):
        _map = super(DescribeL7RsPolicyResponseBodyAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute is not None:
            result['Attribute'] = self.attribute.to_map()
        if self.real_server is not None:
            result['RealServer'] = self.real_server
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Attribute') is not None:
            temp_model = DescribeL7RsPolicyResponseBodyAttributesAttribute()
            self.attribute = temp_model.from_map(m['Attribute'])
        if m.get('RealServer') is not None:
            self.real_server = m.get('RealServer')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        return self


class DescribeL7RsPolicyResponseBody(TeaModel):
    def __init__(self, attributes=None, proxy_mode=None, request_id=None):
        # The details of the parameters for back-to-origin.
        self.attributes = attributes  # type: list[DescribeL7RsPolicyResponseBodyAttributes]
        # The scheduling algorithm for back-to-origin traffic. Valid values:
        # 
        # *   **ip_hash**: the IP hash algorithm. This algorithm is used to redirect the requests from the same IP address to the same origin server.
        # *   **rr**: the round-robin algorithm. This algorithm is used to redirect requests to origin servers in turn.
        # *   **least_time**: the least response time algorithm. This algorithm is used to minimize the latency when requests are forwarded from Anti-DDoS Pro or Anti-DDoS Premium instances to origin servers based on the intelligent DNS resolution feature.
        self.proxy_mode = proxy_mode  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeL7RsPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.proxy_mode is not None:
            result['ProxyMode'] = self.proxy_mode
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = DescribeL7RsPolicyResponseBodyAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('ProxyMode') is not None:
            self.proxy_mode = m.get('ProxyMode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeL7RsPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeL7RsPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeL7RsPolicyResponse, self).to_map()
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
            temp_model = DescribeL7RsPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLayer4RulePolicyRequest(TeaModel):
    def __init__(self, listeners=None):
        # The port forwarding rule that you want to query.
        # 
        # This parameter is a string that consists of JSON arrays. Each element in a JSON array indicates a port forwarding rule. You can query only one port forwarding rule at a time.
        # 
        # > You can call the [DescribeNetworkRules](~~157484~~) to query existing port forwarding rules.
        # 
        # Each port forwarding rule contains the following fields:
        # 
        # *   **InstanceId**: the ID of the instance. This field is required and must be of the string type.
        # *   **Protocol**: the forwarding protocol. This field is required and must be of the string type. Valid values: **tcp** and **udp**.
        # *   **FrontendPort**: the forwarding port. This field is required and must be of the integer type.
        self.listeners = listeners  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLayer4RulePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        return self


class DescribeLayer4RulePolicyResponseBodyPriRealServers(TeaModel):
    def __init__(self, current_index=None, eip=None, frontend_port=None, instance_id=None, protocol=None,
                 real_server=None):
        # The origin server that is used to receive service traffic. Valid values:
        # 
        # *   **1**: the primary origin server, which indicates that Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the primary origin server.
        # *   **2**: the secondary origin server, which indicates that Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the secondary origin server.
        self.current_index = current_index  # type: int
        # The IP address of the instance.
        self.eip = eip  # type: str
        # The forwarding port.
        self.frontend_port = frontend_port  # type: int
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The type of the protocol.
        self.protocol = protocol  # type: str
        # The IP address of the primary origin server.
        self.real_server = real_server  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLayer4RulePolicyResponseBodyPriRealServers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_index is not None:
            result['CurrentIndex'] = self.current_index
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.real_server is not None:
            result['RealServer'] = self.real_server
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentIndex') is not None:
            self.current_index = m.get('CurrentIndex')
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RealServer') is not None:
            self.real_server = m.get('RealServer')
        return self


class DescribeLayer4RulePolicyResponseBodySecRealServers(TeaModel):
    def __init__(self, current_index=None, eip=None, frontend_port=None, instance_id=None, protocol=None,
                 real_server=None):
        # The origin server that is used to receive service traffic. Valid values:
        # 
        # *   **1**: the primary origin server, which indicates that Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the primary origin server.
        # *   **2**: the secondary origin server, which indicates that Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the secondary origin server.
        self.current_index = current_index  # type: int
        # The IP address of the instance.
        self.eip = eip  # type: str
        # The forwarding port.
        self.frontend_port = frontend_port  # type: int
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The type of the protocol.
        self.protocol = protocol  # type: str
        # The IP address of the secondary origin server.
        self.real_server = real_server  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLayer4RulePolicyResponseBodySecRealServers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_index is not None:
            result['CurrentIndex'] = self.current_index
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.real_server is not None:
            result['RealServer'] = self.real_server
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentIndex') is not None:
            self.current_index = m.get('CurrentIndex')
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RealServer') is not None:
            self.real_server = m.get('RealServer')
        return self


class DescribeLayer4RulePolicyResponseBody(TeaModel):
    def __init__(self, backend_port=None, bak_mode=None, current_index=None, forward_protocol=None,
                 frontend_port=None, instance_id=None, pri_real_servers=None, request_id=None, sec_real_servers=None):
        # The port of the origin server.
        self.backend_port = backend_port  # type: int
        # The mode that is used to forward service traffic. Valid values:
        # 
        # *   0: the default mode. In this mode, Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the origin IP address that you specified when you created the port forwarding rule. You can call the [CreateNetworkRules](~~157482~~) operation to create a port forwarding rule.
        # *   1: the origin redundancy mode. In this mode, Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the primary or secondary origin servers. You can call the [ConfigLayer4RulePolicy](~~312684~~) operation to configure IP addresses.
        self.bak_mode = bak_mode  # type: str
        # The origin server that is used to receive service traffic. Valid values:
        # 
        # *   **1**: the primary origin server, which indicates that Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the primary origin server.
        # *   **2**: the secondary origin server, which indicates that Anti-DDoS Pro or Anti-DDoS Premium forwards service traffic to the IP addresses of the secondary origin server.
        self.current_index = current_index  # type: int
        # The type of the protocol.
        self.forward_protocol = forward_protocol  # type: str
        # The forwarding port.
        self.frontend_port = frontend_port  # type: int
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # An array that consists of the information about the primary origin server, including the IP addresses, forwarding protocol, and forwarding port.
        self.pri_real_servers = pri_real_servers  # type: list[DescribeLayer4RulePolicyResponseBodyPriRealServers]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array that consists of the information about the secondary origin server, including the IP addresses, forwarding protocol, and forwarding port.
        self.sec_real_servers = sec_real_servers  # type: list[DescribeLayer4RulePolicyResponseBodySecRealServers]

    def validate(self):
        if self.pri_real_servers:
            for k in self.pri_real_servers:
                if k:
                    k.validate()
        if self.sec_real_servers:
            for k in self.sec_real_servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLayer4RulePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_port is not None:
            result['BackendPort'] = self.backend_port
        if self.bak_mode is not None:
            result['BakMode'] = self.bak_mode
        if self.current_index is not None:
            result['CurrentIndex'] = self.current_index
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['PriRealServers'] = []
        if self.pri_real_servers is not None:
            for k in self.pri_real_servers:
                result['PriRealServers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecRealServers'] = []
        if self.sec_real_servers is not None:
            for k in self.sec_real_servers:
                result['SecRealServers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackendPort') is not None:
            self.backend_port = m.get('BackendPort')
        if m.get('BakMode') is not None:
            self.bak_mode = m.get('BakMode')
        if m.get('CurrentIndex') is not None:
            self.current_index = m.get('CurrentIndex')
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.pri_real_servers = []
        if m.get('PriRealServers') is not None:
            for k in m.get('PriRealServers'):
                temp_model = DescribeLayer4RulePolicyResponseBodyPriRealServers()
                self.pri_real_servers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sec_real_servers = []
        if m.get('SecRealServers') is not None:
            for k in m.get('SecRealServers'):
                temp_model = DescribeLayer4RulePolicyResponseBodySecRealServers()
                self.sec_real_servers.append(temp_model.from_map(k))
        return self


class DescribeLayer4RulePolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLayer4RulePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLayer4RulePolicyResponse, self).to_map()
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
            temp_model = DescribeLayer4RulePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogStoreExistStatusRequest(TeaModel):
    def __init__(self, resource_group_id=None):
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogStoreExistStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeLogStoreExistStatusResponseBody(TeaModel):
    def __init__(self, exist_status=None, request_id=None):
        # Indicates whether a Logstore is created for Anti-DDoS Pro or Anti-DDoS Premium. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.exist_status = exist_status  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLogStoreExistStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist_status is not None:
            result['ExistStatus'] = self.exist_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExistStatus') is not None:
            self.exist_status = m.get('ExistStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLogStoreExistStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLogStoreExistStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLogStoreExistStatusResponse, self).to_map()
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
            temp_model = DescribeLogStoreExistStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNetworkRegionBlockRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNetworkRegionBlockRequest, self).to_map()
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


class DescribeNetworkRegionBlockResponseBodyConfig(TeaModel):
    def __init__(self, countries=None, provinces=None, region_block_switch=None):
        # An array consisting of the codes of the countries or areas from which the requests are blocked.
        self.countries = countries  # type: list[str]
        # An array consisting of the codes of the administrative regions in China from which the requests are blocked.
        self.provinces = provinces  # type: list[str]
        # The status of the Location Blacklist policy. Valid values:
        # 
        # *   **on**: enabled
        # *   **off**: disabled
        self.region_block_switch = region_block_switch  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNetworkRegionBlockResponseBodyConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.countries is not None:
            result['Countries'] = self.countries
        if self.provinces is not None:
            result['Provinces'] = self.provinces
        if self.region_block_switch is not None:
            result['RegionBlockSwitch'] = self.region_block_switch
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Countries') is not None:
            self.countries = m.get('Countries')
        if m.get('Provinces') is not None:
            self.provinces = m.get('Provinces')
        if m.get('RegionBlockSwitch') is not None:
            self.region_block_switch = m.get('RegionBlockSwitch')
        return self


class DescribeNetworkRegionBlockResponseBody(TeaModel):
    def __init__(self, config=None, request_id=None):
        # The configuration of blocked locations.
        self.config = config  # type: DescribeNetworkRegionBlockResponseBodyConfig
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super(DescribeNetworkRegionBlockResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = DescribeNetworkRegionBlockResponseBodyConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNetworkRegionBlockResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNetworkRegionBlockResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNetworkRegionBlockResponse, self).to_map()
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
            temp_model = DescribeNetworkRegionBlockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNetworkRuleAttributesRequest(TeaModel):
    def __init__(self, network_rules=None):
        # The details of the port forwarding rule. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **InstanceId**: the ID of the instance. This field is required and must be of the STRING type.
        # *   **Protocol**: the forwarding protocol. This field is required and must be of the STRING type. Valid values: **tcp** and **udp**.
        # *   **FrontendPort**: the forwarding port. This field is required and must be of the INTEGER type.
        self.network_rules = network_rules  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNetworkRuleAttributesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_rules is not None:
            result['NetworkRules'] = self.network_rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkRules') is not None:
            self.network_rules = m.get('NetworkRules')
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCcSblack(TeaModel):
    def __init__(self, cnt=None, during=None, expires=None, type=None):
        # The threshold that the number of connections initiated from a source IP address can exceed the limit. Set the value to **5**. If the number of connections initiated from a source IP address exceeds the limit five times during the check, the source IP address is added to the blacklist.
        self.cnt = cnt  # type: int
        # The interval at which checks are performed. Set the value to **60**. Unit: seconds.
        self.during = during  # type: int
        # The validity period of the IP address in the blacklist. Valid values: **60** to **604800**. Unit: seconds.
        self.expires = expires  # type: int
        # The type of the limit that causes a source IP address to be added to the blacklist. Valid values:
        # 
        # *   **1**: Source New Connection Rate Limit
        # *   **2**: Source Concurrent Connection Rate Limit
        # *   **3**: PPS Limit for Source
        # *   **4**: Bandwidth Limit for Source
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCcSblack, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cnt is not None:
            result['Cnt'] = self.cnt
        if self.during is not None:
            result['During'] = self.during
        if self.expires is not None:
            result['Expires'] = self.expires
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cnt') is not None:
            self.cnt = m.get('Cnt')
        if m.get('During') is not None:
            self.during = m.get('During')
        if m.get('Expires') is not None:
            self.expires = m.get('Expires')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCc(TeaModel):
    def __init__(self, sblack=None):
        # The protection policy that a source IP address is added to the blacklist when the number of connections initiated from the IP address frequently exceeds the limit.
        self.sblack = sblack  # type: list[DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCcSblack]

    def validate(self):
        if self.sblack:
            for k in self.sblack:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCc, self).to_map()
        if _map is not None:
            return _map

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
        # The maximum length of a packet. Valid values: **0** to **6000**. Unit: bytes.
        self.max = max  # type: int
        # The minimum length of a packet. Valid values: **0** to **6000**. Unit: bytes.
        self.min = min  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigPayloadLen, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, cps=None, cps_enable=None, maxconn=None, maxconn_enable=None):
        # The maximum number of new connections per second that can be established over the port of the destination instance. Valid values: **100** to **100000**.
        self.cps = cps  # type: int
        # The status of the Destination New Connection Rate Limit switch. Valid values:
        # 
        # *   **0**: The switch is turned off.
        # *   **1**: The switch is turned on.
        self.cps_enable = cps_enable  # type: int
        # The maximum number of concurrent connections that can be established over the port of the destination instance. Valid values: **1000** to **1000000**.
        self.maxconn = maxconn  # type: int
        # The status of the Destination Concurrent Connection Rate Limit switch. Valid values:
        # 
        # *   **0**: The switch is turned off.
        # *   **1**: The switch is turned on.
        self.maxconn_enable = maxconn_enable  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSla, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.cps_enable is not None:
            result['CpsEnable'] = self.cps_enable
        if self.maxconn is not None:
            result['Maxconn'] = self.maxconn
        if self.maxconn_enable is not None:
            result['MaxconnEnable'] = self.maxconn_enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('CpsEnable') is not None:
            self.cps_enable = m.get('CpsEnable')
        if m.get('Maxconn') is not None:
            self.maxconn = m.get('Maxconn')
        if m.get('MaxconnEnable') is not None:
            self.maxconn_enable = m.get('MaxconnEnable')
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSlimit(TeaModel):
    def __init__(self, bps=None, cps=None, cps_enable=None, cps_mode=None, maxconn=None, maxconn_enable=None,
                 pps=None):
        # The bandwidth limit for a source IP address. Valid values: **1024** to **268435456**. Unit: bytes/s. Default value: **0**, which indicates that the bandwidth for a source IP address is unlimited.
        self.bps = bps  # type: long
        # The maximum number of new connections per second that can be initiated from a source IP address. Valid values: **1** to **500000**.
        self.cps = cps  # type: int
        # The status of the Source New Connection Rate Limit switch. Valid values:
        # 
        # *   **0**: The switch is turned off.
        # *   **1**: The switch is turned on.
        self.cps_enable = cps_enable  # type: int
        # The mode of the Source New Connection Rate Limit switch. Valid values:
        # 
        # *   **1**: the manual mode
        # *   **2**: the automatic mode
        self.cps_mode = cps_mode  # type: int
        # The maximum number of concurrent connections initiated from a source IP address. Valid values: **1** to **500000**.
        self.maxconn = maxconn  # type: int
        # The status of the Source Concurrent Connection Rate Limit switch. Valid values:
        # 
        # *   **0**: The switch is turned off.
        # *   **1**: The switch is turned on.
        self.maxconn_enable = maxconn_enable  # type: int
        # The packets per second (pps) limit for a source IP address. Valid values: **1** to **100000**. Unit: packets/s. Default value: **0**, which indicates that the pps for a source IP address is unlimited.
        self.pps = pps  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSlimit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.cps_enable is not None:
            result['CpsEnable'] = self.cps_enable
        if self.cps_mode is not None:
            result['CpsMode'] = self.cps_mode
        if self.maxconn is not None:
            result['Maxconn'] = self.maxconn
        if self.maxconn_enable is not None:
            result['MaxconnEnable'] = self.maxconn_enable
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('CpsEnable') is not None:
            self.cps_enable = m.get('CpsEnable')
        if m.get('CpsMode') is not None:
            self.cps_mode = m.get('CpsMode')
        if m.get('Maxconn') is not None:
            self.maxconn = m.get('Maxconn')
        if m.get('MaxconnEnable') is not None:
            self.maxconn_enable = m.get('MaxconnEnable')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfig(TeaModel):
    def __init__(self, cc=None, nodata_conn=None, payload_len=None, persistence_timeout=None, sla=None, slimit=None,
                 synproxy=None):
        # The protection policy applied when the number of connections initiated from a source IP address frequently exceeds the limit.
        self.cc = cc  # type: DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCc
        # The status of the Empty Connection switch. Valid values:
        # 
        # *   **on**: The switch is turned on.
        # *   **off**: The switch is turned off.
        self.nodata_conn = nodata_conn  # type: str
        # The settings of the Packet Length Limit policy.
        self.payload_len = payload_len  # type: DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigPayloadLen
        # The timeout period of session persistence. Valid values: **30** to **3600**. Unit: seconds. Default value: **0**, which indicates that session persistence is disabled.
        self.persistence_timeout = persistence_timeout  # type: int
        # The settings of the Speed Limit for Destination policy.
        self.sla = sla  # type: DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSla
        # The settings of the Speed Limit for Source policy.
        self.slimit = slimit  # type: DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSlimit
        # The status of the False Source switch. Valid values:
        # 
        # *   **on**: The switch is turned on.
        # *   **off**: The switch is turned off.
        self.synproxy = synproxy  # type: str

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
        _map = super(DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cc is not None:
            result['Cc'] = self.cc.to_map()
        if self.nodata_conn is not None:
            result['NodataConn'] = self.nodata_conn
        if self.payload_len is not None:
            result['PayloadLen'] = self.payload_len.to_map()
        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout
        if self.sla is not None:
            result['Sla'] = self.sla.to_map()
        if self.slimit is not None:
            result['Slimit'] = self.slimit.to_map()
        if self.synproxy is not None:
            result['Synproxy'] = self.synproxy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cc') is not None:
            temp_model = DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCc()
            self.cc = temp_model.from_map(m['Cc'])
        if m.get('NodataConn') is not None:
            self.nodata_conn = m.get('NodataConn')
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
        if m.get('Synproxy') is not None:
            self.synproxy = m.get('Synproxy')
        return self


class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributes(TeaModel):
    def __init__(self, config=None, frontend_port=None, instance_id=None, protocol=None):
        # The mitigation settings of the port forwarding rule.
        self.config = config  # type: DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfig
        # The forwarding port.
        self.frontend_port = frontend_port  # type: int
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The forwarding protocol. Valid values:
        # 
        # *   **tcp**\
        # *   **udp**\
        self.protocol = protocol  # type: str

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super(DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeNetworkRuleAttributesResponseBody(TeaModel):
    def __init__(self, network_rule_attributes=None, request_id=None):
        # An array that consists of the mitigation settings of the port forwarding rule for a non-website service. The mitigation settings include session persistence and DDoS mitigation policies.
        self.network_rule_attributes = network_rule_attributes  # type: list[DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributes]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.network_rule_attributes:
            for k in self.network_rule_attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeNetworkRuleAttributesResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNetworkRuleAttributesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNetworkRuleAttributesResponse, self).to_map()
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
            temp_model = DescribeNetworkRuleAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNetworkRulesRequest(TeaModel):
    def __init__(self, forward_protocol=None, frontend_port=None, instance_id=None, page_number=None,
                 page_size=None):
        # The forwarding protocol. Valid values:
        # 
        # *   **tcp**\
        # *   **udp**\
        self.forward_protocol = forward_protocol  # type: str
        # The forwarding port.
        self.frontend_port = frontend_port  # type: int
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # The number of the page to return. For example, to query the returned results on the first page, set the value to **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNetworkRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeNetworkRulesResponseBodyNetworkRules(TeaModel):
    def __init__(self, backend_port=None, frontend_port=None, instance_id=None, is_auto_create=None, protocol=None,
                 real_servers=None):
        # The port of the origin server.
        self.backend_port = backend_port  # type: int
        # The forwarding port.
        self.frontend_port = frontend_port  # type: int
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # Indicates whether the port forwarding rule is automatically created. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.is_auto_create = is_auto_create  # type: bool
        # The forwarding protocol. Valid values:
        # 
        # *   **tcp**\
        # *   **udp**\
        self.protocol = protocol  # type: str
        # An array that consists of IP addresses of origin servers.
        self.real_servers = real_servers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNetworkRulesResponseBodyNetworkRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_port is not None:
            result['BackendPort'] = self.backend_port
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_auto_create is not None:
            result['IsAutoCreate'] = self.is_auto_create
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackendPort') is not None:
            self.backend_port = m.get('BackendPort')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsAutoCreate') is not None:
            self.is_auto_create = m.get('IsAutoCreate')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        return self


class DescribeNetworkRulesResponseBody(TeaModel):
    def __init__(self, network_rules=None, request_id=None, total_count=None):
        # An array that consists of the details of a port forwarding rule.
        self.network_rules = network_rules  # type: list[DescribeNetworkRulesResponseBodyNetworkRules]
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The total number of returned port forwarding rules.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.network_rules:
            for k in self.network_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeNetworkRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NetworkRules'] = []
        if self.network_rules is not None:
            for k in self.network_rules:
                result['NetworkRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.network_rules = []
        if m.get('NetworkRules') is not None:
            for k in m.get('NetworkRules'):
                temp_model = DescribeNetworkRulesResponseBodyNetworkRules()
                self.network_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeNetworkRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNetworkRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNetworkRulesResponse, self).to_map()
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
            temp_model = DescribeNetworkRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOpEntitiesRequest(TeaModel):
    def __init__(self, end_time=None, entity_object=None, entity_type=None, page_number=None, page_size=None,
                 resource_group_id=None, start_time=None):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # > The time must be in the latest 30 days.
        self.end_time = end_time  # type: long
        # The operation object that you want to query.
        self.entity_object = entity_object  # type: str
        # The type of the operation object that you want to query. Valid values:
        # 
        # *   **1**: the IP address of the Anti-DDoS Pro or Anti-DDoS Premium instance
        # *   **2**: Anti-DDoS plans
        # *   **3**: ECS instances
        # *   **4**: all logs
        self.entity_type = entity_type  # type: int
        # The number of the page to return. For example, to query the returned results on the first page, set the value to **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Maximum value: **50**.
        self.page_size = page_size  # type: int
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # > The time must be in the latest 30 days.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOpEntitiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.entity_object is not None:
            result['EntityObject'] = self.entity_object
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeOpEntitiesResponseBodyOpEntities(TeaModel):
    def __init__(self, entity_object=None, entity_type=None, gmt_create=None, op_account=None, op_action=None,
                 op_desc=None):
        # The operation object.
        self.entity_object = entity_object  # type: str
        # The type of the operation object. Valid values:
        # 
        # *   **1**: the IP address of the Anti-DDoS Pro or Anti-DDoS Premium instance
        # *   **2**: Anti-DDoS plans
        # *   **3**: ECS instances
        # *   **4**: all logs
        self.entity_type = entity_type  # type: int
        # The time when the operation was performed. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create  # type: long
        # The ID of the Alibaba Cloud account that is used to call the API operation.
        self.op_account = op_account  # type: str
        # The type of the operation. Valid values:
        # 
        # *   **1**: configuring burstable protection bandwidth.
        # *   **5**: using Anti-DDoS plans.
        # *   **8**: changing IP addresses of ECS instances.
        # *   **9**: deactivating blackhole filtering.
        # *   **10**: configuring the Diversion from Origin Server policy.
        # *   **11**: clearing all logs.
        # *   **12**: downgrading the specifications of instances. If the instance expires or the account has overdue payments, this operation is performed to downgrade the burstable protection bandwidth.
        # *   **13**: restoring the specifications of instances. If the instance is renewed or you have paid the overdue payments within your account, this operation is performed to restore the burstable protection bandwidth.
        self.op_action = op_action  # type: int
        # The details of the operation. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **newEntity**: the values of the parameters after the operation. This field must be of the STRING type.
        # *   **oldEntity**: the values of the parameters before the operation. This field must be of the STRING type.
        # 
        # Both **newEntity** and **oldEntity** are JSON strings. The returned parameters vary with **OpAtion**.
        # 
        # If **OpAction** is **1**, **12**, or **13**, the following parameter is returned:
        # 
        # *   **elasticBandwidth**: the burstable protection bandwidth. The value is of the INTEGER type.
        # 
        #     For example: `{"newEntity":{"elasticBandwidth":300},"oldEntity":{"elasticBandwidth":300}}`
        # 
        # If **OpAction** is **5**, the following parameters are returned:
        # 
        # *   **bandwidth**: the burstable protection bandwidth. The value is of the INTEGER type. Unit: Gbit/s.
        # 
        # *   **count**: the number of Anti-DDoS plans. The value is of the INTEGER type.
        # 
        # *   **deductCount**: the number of used Anti-DDoS plans. The value is of the INTEGER type.
        # 
        # *   **expireTime**: the expiration time of the Anti-DDoS plans. The value is of the LONG type. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # *   **instanceId**: the ID of the instance. The value is of the STRING type.
        # 
        # *   **peakFlow**: the peak throughput on the instance. The value is of the INTEGER type. Unit: bit/s.
        # 
        #     For example: `{"newEntity":{"bandwidth":100,"count":4,"deductCount":1,"expireTime":1616299196000,"instanceId":"ddoscoo-cn-v641kpmq****","peakFlow":751427000}}`
        # 
        # If **OpAction** is **8**, the following parameter is returned:
        # 
        # *   **instanceId**: the ID of the ECS instance whose IP address is changed. The value is of the STRING type.
        # 
        #     For example: `{"newEntity":{"instanceId":"i-wz9h6nc313zptbqn****"}}`
        # 
        # If **OpAction** is **9**, the following parameter is returned:
        # 
        # *   **actionMethod**: the operation method. The value is of the STRING type. Valid value: **undo**, which indicates that you deactivated blackhole filtering.
        # 
        #     For example: `{"newEntity":{"actionMethod":"undo"}}`
        # 
        # If **OpAction** is **10**, the following parameters are returned:
        # 
        # *   **actionMethod**: the operation method. The value is of the STRING type. Valid values:
        # 
        #     *   **do**: The Diversion from Origin Server policy is enabled.
        #     *   **undo**: The Diversion from Origin Server policy is disabled.
        # 
        # *   **lines**: The Internet service provider (ISP) line from which the traffic is blocked. Valid values:
        # 
        #     *   **ct**: China Telecom (International)
        #     *   **cut**: China Unicom (International)
        # 
        #     For example: `{"newEntity":{"actionMethod":"undo","lines":["ct"]}}`
        # 
        # If **OpAction** is **11**, no parameter is returned, and the description is empty.
        self.op_desc = op_desc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOpEntitiesResponseBodyOpEntities, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_object is not None:
            result['EntityObject'] = self.entity_object
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.op_account is not None:
            result['OpAccount'] = self.op_account
        if self.op_action is not None:
            result['OpAction'] = self.op_action
        if self.op_desc is not None:
            result['OpDesc'] = self.op_desc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OpAccount') is not None:
            self.op_account = m.get('OpAccount')
        if m.get('OpAction') is not None:
            self.op_action = m.get('OpAction')
        if m.get('OpDesc') is not None:
            self.op_desc = m.get('OpDesc')
        return self


class DescribeOpEntitiesResponseBody(TeaModel):
    def __init__(self, op_entities=None, request_id=None, total_count=None):
        # An array that consists of the details of the operation log.
        self.op_entities = op_entities  # type: list[DescribeOpEntitiesResponseBodyOpEntities]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned operation records.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.op_entities:
            for k in self.op_entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOpEntitiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OpEntities'] = []
        if self.op_entities is not None:
            for k in self.op_entities:
                result['OpEntities'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.op_entities = []
        if m.get('OpEntities') is not None:
            for k in m.get('OpEntities'):
                temp_model = DescribeOpEntitiesResponseBodyOpEntities()
                self.op_entities.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOpEntitiesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOpEntitiesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOpEntitiesResponse, self).to_map()
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
            temp_model = DescribeOpEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortRequest(TeaModel):
    def __init__(self, frontend_port=None, frontend_protocol=None, instance_id=None, page_number=None,
                 page_size=None):
        # The forwarding port to query. Valid values: **0** to **65535**.
        self.frontend_port = frontend_port  # type: int
        # The type of the forwarding protocol to query. Valid values:
        # 
        # *   **tcp**\
        # *   **udp**\
        self.frontend_protocol = frontend_protocol  # type: str
        # The ID of the instance to query.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # The number of the page to return. For example, if you want to obtain results on the first page, set the value to **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.frontend_protocol is not None:
            result['FrontendProtocol'] = self.frontend_protocol
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('FrontendProtocol') is not None:
            self.frontend_protocol = m.get('FrontendProtocol')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribePortResponseBodyNetworkRules(TeaModel):
    def __init__(self, backend_port=None, frontend_port=None, frontend_protocol=None, instance_id=None,
                 is_auto_create=None, real_servers=None):
        # The port of the origin server.
        self.backend_port = backend_port  # type: int
        # The forwarding port.
        self.frontend_port = frontend_port  # type: int
        # The type of the protocol. Valid values:
        # 
        # *   **tcp**\
        # *   **udp**\
        self.frontend_protocol = frontend_protocol  # type: str
        # The ID of the instance to which the port forwarding rule is applied.
        self.instance_id = instance_id  # type: str
        # Indicates whether the port forwarding rule is automatically created by the instance. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.is_auto_create = is_auto_create  # type: bool
        # An array that consists of IP addresses of origin servers.
        self.real_servers = real_servers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortResponseBodyNetworkRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_port is not None:
            result['BackendPort'] = self.backend_port
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.frontend_protocol is not None:
            result['FrontendProtocol'] = self.frontend_protocol
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_auto_create is not None:
            result['IsAutoCreate'] = self.is_auto_create
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackendPort') is not None:
            self.backend_port = m.get('BackendPort')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('FrontendProtocol') is not None:
            self.frontend_protocol = m.get('FrontendProtocol')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsAutoCreate') is not None:
            self.is_auto_create = m.get('IsAutoCreate')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        return self


class DescribePortResponseBody(TeaModel):
    def __init__(self, network_rules=None, request_id=None, total_count=None):
        # An array that consists of port forwarding rules.
        self.network_rules = network_rules  # type: list[DescribePortResponseBodyNetworkRules]
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The number of port forwarding rules returned.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.network_rules:
            for k in self.network_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePortResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NetworkRules'] = []
        if self.network_rules is not None:
            for k in self.network_rules:
                result['NetworkRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.network_rules = []
        if m.get('NetworkRules') is not None:
            for k in m.get('NetworkRules'):
                temp_model = DescribePortResponseBodyNetworkRules()
                self.network_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePortResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePortResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePortResponse, self).to_map()
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
            temp_model = DescribePortResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortAttackMaxFlowRequest(TeaModel):
    def __init__(self, end_time=None, instance_ids=None, resource_group_id=None, start_time=None):
        # The end of the time range to query. This value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # An array that consists of the IDs of instances to query.
        self.instance_ids = instance_ids  # type: list[str]
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. This value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortAttackMaxFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePortAttackMaxFlowResponseBody(TeaModel):
    def __init__(self, bps=None, pps=None, request_id=None):
        # The peak bandwidth of attack traffic. Unit: bit/s.
        self.bps = bps  # type: long
        # The peak packet rate of attack traffic . Unit: packets per second (pps).
        self.pps = pps  # type: long
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortAttackMaxFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePortAttackMaxFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePortAttackMaxFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePortAttackMaxFlowResponse, self).to_map()
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
            temp_model = DescribePortAttackMaxFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortAutoCcStatusRequest(TeaModel):
    def __init__(self, instance_ids=None):
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_ids = instance_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortAutoCcStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DescribePortAutoCcStatusResponseBodyPortAutoCcStatus(TeaModel):
    def __init__(self, mode=None, switch=None, web_mode=None, web_switch=None):
        # The mode of the Intelligent Protection policy. Valid values:
        # 
        # *   **normal**\
        # *   **loose**\
        # *   **strict**\
        self.mode = mode  # type: str
        # The status of the Intelligent Protection policy. Valid values:
        # 
        # *   **on**: enabled
        # *   **off**: disabled
        self.switch = switch  # type: str
        # The protection mode for ports 80 and 443. Valid values:
        # 
        # *   **normal**\
        # *   **loose**\
        # *   **strict**\
        self.web_mode = web_mode  # type: str
        # The status of the Intelligent Protection policy for ports 80 and 443. Valid values:
        # 
        # *   **on**: enabled
        # *   **off**: disabled
        self.web_switch = web_switch  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortAutoCcStatusResponseBodyPortAutoCcStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.switch is not None:
            result['Switch'] = self.switch
        if self.web_mode is not None:
            result['WebMode'] = self.web_mode
        if self.web_switch is not None:
            result['WebSwitch'] = self.web_switch
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Switch') is not None:
            self.switch = m.get('Switch')
        if m.get('WebMode') is not None:
            self.web_mode = m.get('WebMode')
        if m.get('WebSwitch') is not None:
            self.web_switch = m.get('WebSwitch')
        return self


class DescribePortAutoCcStatusResponseBody(TeaModel):
    def __init__(self, port_auto_cc_status=None, request_id=None):
        # An array that consists of the configurations of the Intelligent Protection policy.
        self.port_auto_cc_status = port_auto_cc_status  # type: list[DescribePortAutoCcStatusResponseBodyPortAutoCcStatus]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.port_auto_cc_status:
            for k in self.port_auto_cc_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePortAutoCcStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PortAutoCcStatus'] = []
        if self.port_auto_cc_status is not None:
            for k in self.port_auto_cc_status:
                result['PortAutoCcStatus'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.port_auto_cc_status = []
        if m.get('PortAutoCcStatus') is not None:
            for k in m.get('PortAutoCcStatus'):
                temp_model = DescribePortAutoCcStatusResponseBodyPortAutoCcStatus()
                self.port_auto_cc_status.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePortAutoCcStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePortAutoCcStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePortAutoCcStatusResponse, self).to_map()
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
            temp_model = DescribePortAutoCcStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortConnsCountRequest(TeaModel):
    def __init__(self, end_time=None, instance_ids=None, port=None, resource_group_id=None, start_time=None):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # An array that consists of the IDs of instances.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_ids = instance_ids  # type: list[str]
        # The number of port that you want to query. If you do not specify this parameter, all ports are queried.
        self.port = port  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortConnsCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.port is not None:
            result['Port'] = self.port
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePortConnsCountResponseBody(TeaModel):
    def __init__(self, act_conns=None, conns=None, cps=None, in_act_conns=None, request_id=None):
        # The number of active connections.
        self.act_conns = act_conns  # type: long
        # The number of concurrent connections.
        self.conns = conns  # type: long
        # The number of new connections.
        self.cps = cps  # type: long
        # The number of inactive connections.
        self.in_act_conns = in_act_conns  # type: long
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortConnsCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.act_conns is not None:
            result['ActConns'] = self.act_conns
        if self.conns is not None:
            result['Conns'] = self.conns
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.in_act_conns is not None:
            result['InActConns'] = self.in_act_conns
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActConns') is not None:
            self.act_conns = m.get('ActConns')
        if m.get('Conns') is not None:
            self.conns = m.get('Conns')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('InActConns') is not None:
            self.in_act_conns = m.get('InActConns')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePortConnsCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePortConnsCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePortConnsCountResponse, self).to_map()
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
            temp_model = DescribePortConnsCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortConnsListRequest(TeaModel):
    def __init__(self, end_time=None, instance_ids=None, interval=None, port=None, resource_group_id=None,
                 start_time=None):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_ids = instance_ids  # type: list[str]
        # The interval for returning data. Unit: seconds.
        self.interval = interval  # type: int
        # The number of port that you want to query. If you do not specify this parameter, all ports are queried.
        self.port = port  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortConnsListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.port is not None:
            result['Port'] = self.port
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePortConnsListResponseBodyConnsList(TeaModel):
    def __init__(self, act_conns=None, conns=None, cps=None, in_act_conns=None, index=None):
        # The number of active connections.
        self.act_conns = act_conns  # type: long
        # The number of concurrent connections.
        self.conns = conns  # type: long
        # The new connection creation rate.
        self.cps = cps  # type: long
        # The number of inactive connections.
        self.in_act_conns = in_act_conns  # type: long
        # The index number of the returned data.
        self.index = index  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortConnsListResponseBodyConnsList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.act_conns is not None:
            result['ActConns'] = self.act_conns
        if self.conns is not None:
            result['Conns'] = self.conns
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.in_act_conns is not None:
            result['InActConns'] = self.in_act_conns
        if self.index is not None:
            result['Index'] = self.index
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActConns') is not None:
            self.act_conns = m.get('ActConns')
        if m.get('Conns') is not None:
            self.conns = m.get('Conns')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('InActConns') is not None:
            self.in_act_conns = m.get('InActConns')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        return self


class DescribePortConnsListResponseBody(TeaModel):
    def __init__(self, conns_list=None, request_id=None):
        # An array that consists of the connections established over the port.
        self.conns_list = conns_list  # type: list[DescribePortConnsListResponseBodyConnsList]
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.conns_list:
            for k in self.conns_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePortConnsListResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePortConnsListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePortConnsListResponse, self).to_map()
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
            temp_model = DescribePortConnsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortFlowListRequest(TeaModel):
    def __init__(self, end_time=None, instance_ids=None, interval=None, resource_group_id=None, start_time=None):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # **\
        # 
        # **This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # An array that consists of the IDs of instances.
        self.instance_ids = instance_ids  # type: list[str]
        # The interval for returning data. Unit: seconds. The interval that you can specify varies based on the time range to query. The time range to query is determined by the values of **StartTime** and **EndTime**.
        # 
        # *   If the time range to query is no greater than 1 hour, we recommend that you specify the interval from 60 seconds to the time range to query.
        # *   If the time range to query is greater than 1 hour but no greater than 6 hours, we recommend that you specify the interval from 600 seconds to the time range to query.
        # *   If the time range to query is greater than 6 hours but no greater than 24 hours, we recommend that you specify the interval from 1,800 seconds to the time range to query.
        # *   If the time range to query is greater than 24 hours but no greater than 7 days, we recommend that you specify the interval from 3,600 seconds to the time range to query.
        # *   If the time range to query is greater than 7 days but no greater than 15 days, we recommend that you specify the interval from 14,400 seconds to the time range to query.
        # *   If the time range to query is greater than 15 days, we recommend that you specify the interval from 43,200 seconds to the time range to query.
        self.interval = interval  # type: int
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](~~94485~~).
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # **\
        # 
        # **This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortFlowListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePortFlowListResponseBodyPortFlowList(TeaModel):
    def __init__(self, attack_bps=None, attack_pps=None, in_bps=None, in_pps=None, index=None, out_bps=None,
                 out_pps=None, region=None, sla_bps_drop_bps=None, sla_bps_drop_pps=None, sla_conn_drop_bps=None,
                 sla_conn_drop_pps=None, sla_cps_drop_bps=None, sla_cps_drop_pps=None, sla_pps_drop_bps=None, sla_pps_drop_pps=None,
                 time=None):
        # The bandwidth of attack traffic. Unit: bit/s.
        self.attack_bps = attack_bps  # type: long
        # The packet forwarding rate of attack traffic. Unit: pps.
        self.attack_pps = attack_pps  # type: long
        # The inbound bandwidth. Unit: bit/s.
        self.in_bps = in_bps  # type: long
        # The packet forwarding rate of inbound traffic. Unit: packets per second.
        self.in_pps = in_pps  # type: long
        # The index number of the returned data.
        self.index = index  # type: long
        # The outbound bandwidth. Unit: bit/s.
        self.out_bps = out_bps  # type: long
        # The packet forwarding rate of outbound traffic. Unit: packets per second (pps).
        self.out_pps = out_pps  # type: long
        # The source region of the traffic. Valid values:
        # 
        # *   **cn**: mainland China
        # *   **alb-ap-northeast-1-gf-x**: Japan (Tokyo)
        # *   **alb-ap-southeast-gf-x**: Singapore
        # *   **alb-cn-hongkong-gf-x**: Hong Kong (China)
        # *   **alb-eu-central-1-gf-x**: Germany (Frankfurt)
        # *   **alb-us-west-1-gf-x**: US (Silicon Valley)
        # 
        # > The values except **cn** are returned only when **RegionId** is set to **ap-southeast-1**.
        self.region = region  # type: str
        self.sla_bps_drop_bps = sla_bps_drop_bps  # type: long
        self.sla_bps_drop_pps = sla_bps_drop_pps  # type: long
        self.sla_conn_drop_bps = sla_conn_drop_bps  # type: long
        self.sla_conn_drop_pps = sla_conn_drop_pps  # type: long
        self.sla_cps_drop_bps = sla_cps_drop_bps  # type: long
        self.sla_cps_drop_pps = sla_cps_drop_pps  # type: long
        self.sla_pps_drop_bps = sla_pps_drop_bps  # type: long
        self.sla_pps_drop_pps = sla_pps_drop_pps  # type: long
        # The time when the data was collected. The value is a UNIX timestamp. Unit: seconds.
        self.time = time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortFlowListResponseBodyPortFlowList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_bps is not None:
            result['AttackBps'] = self.attack_bps
        if self.attack_pps is not None:
            result['AttackPps'] = self.attack_pps
        if self.in_bps is not None:
            result['InBps'] = self.in_bps
        if self.in_pps is not None:
            result['InPps'] = self.in_pps
        if self.index is not None:
            result['Index'] = self.index
        if self.out_bps is not None:
            result['OutBps'] = self.out_bps
        if self.out_pps is not None:
            result['OutPps'] = self.out_pps
        if self.region is not None:
            result['Region'] = self.region
        if self.sla_bps_drop_bps is not None:
            result['SlaBpsDropBps'] = self.sla_bps_drop_bps
        if self.sla_bps_drop_pps is not None:
            result['SlaBpsDropPps'] = self.sla_bps_drop_pps
        if self.sla_conn_drop_bps is not None:
            result['SlaConnDropBps'] = self.sla_conn_drop_bps
        if self.sla_conn_drop_pps is not None:
            result['SlaConnDropPps'] = self.sla_conn_drop_pps
        if self.sla_cps_drop_bps is not None:
            result['SlaCpsDropBps'] = self.sla_cps_drop_bps
        if self.sla_cps_drop_pps is not None:
            result['SlaCpsDropPps'] = self.sla_cps_drop_pps
        if self.sla_pps_drop_bps is not None:
            result['SlaPpsDropBps'] = self.sla_pps_drop_bps
        if self.sla_pps_drop_pps is not None:
            result['SlaPpsDropPps'] = self.sla_pps_drop_pps
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttackBps') is not None:
            self.attack_bps = m.get('AttackBps')
        if m.get('AttackPps') is not None:
            self.attack_pps = m.get('AttackPps')
        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')
        if m.get('InPps') is not None:
            self.in_pps = m.get('InPps')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('OutBps') is not None:
            self.out_bps = m.get('OutBps')
        if m.get('OutPps') is not None:
            self.out_pps = m.get('OutPps')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SlaBpsDropBps') is not None:
            self.sla_bps_drop_bps = m.get('SlaBpsDropBps')
        if m.get('SlaBpsDropPps') is not None:
            self.sla_bps_drop_pps = m.get('SlaBpsDropPps')
        if m.get('SlaConnDropBps') is not None:
            self.sla_conn_drop_bps = m.get('SlaConnDropBps')
        if m.get('SlaConnDropPps') is not None:
            self.sla_conn_drop_pps = m.get('SlaConnDropPps')
        if m.get('SlaCpsDropBps') is not None:
            self.sla_cps_drop_bps = m.get('SlaCpsDropBps')
        if m.get('SlaCpsDropPps') is not None:
            self.sla_cps_drop_pps = m.get('SlaCpsDropPps')
        if m.get('SlaPpsDropBps') is not None:
            self.sla_pps_drop_bps = m.get('SlaPpsDropBps')
        if m.get('SlaPpsDropPps') is not None:
            self.sla_pps_drop_pps = m.get('SlaPpsDropPps')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribePortFlowListResponseBody(TeaModel):
    def __init__(self, port_flow_list=None, request_id=None):
        # The returned traffic data.
        self.port_flow_list = port_flow_list  # type: list[DescribePortFlowListResponseBodyPortFlowList]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.port_flow_list:
            for k in self.port_flow_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePortFlowListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PortFlowList'] = []
        if self.port_flow_list is not None:
            for k in self.port_flow_list:
                result['PortFlowList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.port_flow_list = []
        if m.get('PortFlowList') is not None:
            for k in m.get('PortFlowList'):
                temp_model = DescribePortFlowListResponseBodyPortFlowList()
                self.port_flow_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePortFlowListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePortFlowListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePortFlowListResponse, self).to_map()
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
            temp_model = DescribePortFlowListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortMaxConnsRequest(TeaModel):
    def __init__(self, end_time=None, instance_ids=None, resource_group_id=None, start_time=None):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_ids = instance_ids  # type: list[str]
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortMaxConnsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePortMaxConnsResponseBodyPortMaxConns(TeaModel):
    def __init__(self, cps=None, ip=None, port=None):
        # The maximum number of connections per second (CPS).
        self.cps = cps  # type: long
        # The IP address of the instance.
        self.ip = ip  # type: str
        # The port of the instance.
        self.port = port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortMaxConnsResponseBodyPortMaxConns, self).to_map()
        if _map is not None:
            return _map

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
        # An array consisting of the details of the maximum number of connections that are established over a port of the instance.
        self.port_max_conns = port_max_conns  # type: list[DescribePortMaxConnsResponseBodyPortMaxConns]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.port_max_conns:
            for k in self.port_max_conns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePortMaxConnsResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePortMaxConnsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePortMaxConnsResponse, self).to_map()
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
            temp_model = DescribePortMaxConnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortViewSourceCountriesRequest(TeaModel):
    def __init__(self, end_time=None, instance_ids=None, resource_group_id=None, start_time=None):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # An array that consists of the IDs of instances to query.
        self.instance_ids = instance_ids  # type: list[str]
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](~~94485~~).
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortViewSourceCountriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePortViewSourceCountriesResponseBodySourceCountrys(TeaModel):
    def __init__(self, count=None, country_id=None):
        # The number of requests.
        self.count = count  # type: long
        # The abbreviation of the country or area. For example, **cn** indicates China and **us** indicates the United States.
        # 
        # > For more information, see [Location parameters](~~167926~~).
        self.country_id = country_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortViewSourceCountriesResponseBodySourceCountrys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        return self


class DescribePortViewSourceCountriesResponseBody(TeaModel):
    def __init__(self, request_id=None, source_countrys=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array consisting of countries or areas from which the requests are sent.
        self.source_countrys = source_countrys  # type: list[DescribePortViewSourceCountriesResponseBodySourceCountrys]

    def validate(self):
        if self.source_countrys:
            for k in self.source_countrys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePortViewSourceCountriesResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePortViewSourceCountriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePortViewSourceCountriesResponse, self).to_map()
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
            temp_model = DescribePortViewSourceCountriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortViewSourceIspsRequest(TeaModel):
    def __init__(self, end_time=None, instance_ids=None, resource_group_id=None, start_time=None):
        # The end of the time range to query. This value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # An array that consists of the IDs of instances to query.
        self.instance_ids = instance_ids  # type: list[str]
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. This value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortViewSourceIspsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePortViewSourceIspsResponseBodyIsps(TeaModel):
    def __init__(self, count=None, isp_id=None):
        # The total number of requests that are sent from the ISP.
        # 
        # > This parameter does not indicate the accurate number of requests. You can use this parameter to calculate the proportion of requests from different ISPs.
        self.count = count  # type: long
        # The ID of the ISP. For more information, see the ISP codes table.
        self.isp_id = isp_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortViewSourceIspsResponseBodyIsps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.isp_id is not None:
            result['IspId'] = self.isp_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('IspId') is not None:
            self.isp_id = m.get('IspId')
        return self


class DescribePortViewSourceIspsResponseBody(TeaModel):
    def __init__(self, isps=None, request_id=None):
        # An array that consists of the details of the ISP.
        self.isps = isps  # type: list[DescribePortViewSourceIspsResponseBodyIsps]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.isps:
            for k in self.isps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePortViewSourceIspsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Isps'] = []
        if self.isps is not None:
            for k in self.isps:
                result['Isps'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.isps = []
        if m.get('Isps') is not None:
            for k in m.get('Isps'):
                temp_model = DescribePortViewSourceIspsResponseBodyIsps()
                self.isps.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePortViewSourceIspsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePortViewSourceIspsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePortViewSourceIspsResponse, self).to_map()
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
            temp_model = DescribePortViewSourceIspsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortViewSourceProvincesRequest(TeaModel):
    def __init__(self, end_time=None, instance_ids=None, resource_group_id=None, start_time=None):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds. If you do not configure this parameter, the current system time is used as the end time.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # The IDs of instances to query.
        self.instance_ids = instance_ids  # type: list[str]
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](~~94485~~).
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortViewSourceProvincesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePortViewSourceProvincesResponseBodySourceProvinces(TeaModel):
    def __init__(self, count=None, province_id=None):
        # The total number of requests that are sent from the ISP.
        # 
        # > This parameter does not indicate the accurate number of requests. You can use this parameter to calculate the proportion of requests from different administrative regions in China.
        self.count = count  # type: long
        # The ID of the administrative region in China from which the requests are sent. For example, **110000** indicates Beijing, and **120000** indicates Tianjin.
        # 
        # > For more information, see [Location parameters](~~167926~~).
        self.province_id = province_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePortViewSourceProvincesResponseBodySourceProvinces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.province_id is not None:
            result['ProvinceId'] = self.province_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('ProvinceId') is not None:
            self.province_id = m.get('ProvinceId')
        return self


class DescribePortViewSourceProvincesResponseBody(TeaModel):
    def __init__(self, request_id=None, source_provinces=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Details about the administrative region in China from which the requests are sent.
        self.source_provinces = source_provinces  # type: list[DescribePortViewSourceProvincesResponseBodySourceProvinces]

    def validate(self):
        if self.source_provinces:
            for k in self.source_provinces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePortViewSourceProvincesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SourceProvinces'] = []
        if self.source_provinces is not None:
            for k in self.source_provinces:
                result['SourceProvinces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.source_provinces = []
        if m.get('SourceProvinces') is not None:
            for k in m.get('SourceProvinces'):
                temp_model = DescribePortViewSourceProvincesResponseBodySourceProvinces()
                self.source_provinces.append(temp_model.from_map(k))
        return self


class DescribePortViewSourceProvincesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePortViewSourceProvincesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePortViewSourceProvincesResponse, self).to_map()
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
            temp_model = DescribePortViewSourceProvincesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSceneDefenseObjectsRequest(TeaModel):
    def __init__(self, policy_id=None, resource_group_id=None):
        # The ID of the policy that you want to query.
        # 
        # > You can call the [DescribeSceneDefensePolicies](~~159382~~) operation to query the IDs of all policies.
        self.policy_id = policy_id  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSceneDefenseObjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSceneDefenseObjectsResponseBodyObjects(TeaModel):
    def __init__(self, domain=None, policy_id=None, vip=None):
        # The domain name that is protected by the policy.
        self.domain = domain  # type: str
        # The ID of the policy.
        self.policy_id = policy_id  # type: str
        # The IP address of the Anti-DDoS Pro or Anti-DDoS Premium instance that is protected by the policy.
        self.vip = vip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSceneDefenseObjectsResponseBodyObjects, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, objects=None, request_id=None, success=None):
        # The information about the protected assets.
        self.objects = objects  # type: list[DescribeSceneDefenseObjectsResponseBodyObjects]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success  # type: bool

    def validate(self):
        if self.objects:
            for k in self.objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSceneDefenseObjectsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Objects'] = []
        if self.objects is not None:
            for k in self.objects:
                result['Objects'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.objects = []
        if m.get('Objects') is not None:
            for k in m.get('Objects'):
                temp_model = DescribeSceneDefenseObjectsResponseBodyObjects()
                self.objects.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSceneDefenseObjectsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSceneDefenseObjectsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSceneDefenseObjectsResponse, self).to_map()
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
            temp_model = DescribeSceneDefenseObjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSceneDefensePoliciesRequest(TeaModel):
    def __init__(self, resource_group_id=None, status=None, template=None):
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The status of the policy. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: pending enabling
        # *   **2**: enabled
        # *   **3**: expired
        self.status = status  # type: str
        # The type of the template that is used to create the policy. Valid values:
        # 
        # *   **promotion**: the Important Activity template
        # *   **bypass**: the Forward All template
        self.template = template  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSceneDefensePoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class DescribeSceneDefensePoliciesResponseBodyPoliciesRuntimePolicies(TeaModel):
    def __init__(self, new_value=None, policy_type=None, status=None, old_value=None):
        # The protection rule that is applied when the policy takes effect.
        # 
        # If you set **PolicyType** to **1**, the value is **{"cc_rule_enable": false }**. The value indicates that the Frequency Control policy is disabled.
        # 
        # If you set **PolicyType** to **2**, the value is **{"ai_rule_enable": 0}**. The value indicates that the Intelligent Protection policy is disabled.
        self.new_value = new_value  # type: str
        # The protection policy whose status is changed when the policy takes effect. Valid values:
        # 
        # *   **1**: indicates that the Frequency Control policy is changed.
        # *   **2**: indicates that the Intelligent Protection policy is changed.
        self.policy_type = policy_type  # type: int
        # The running status of the policy. Valid values:
        # 
        # *   **0**: The policy has not been issued or is restored.
        # *   **1**: The policy is pending.
        # *   **2**: The policy is being restored.
        # *   **3**: The policy takes effect.
        # *   **4**: The policy fails to take effect.
        # *   **5**:The policy fails to be restored.
        # *   **6**: The configurations of the protected objects for the policy does not exist because the configurations may be deleted.
        self.status = status  # type: int
        # The protection rule that is applied before the policy takes effect.
        # 
        # If you set **PolicyType** to **1**, the value is **{"cc_rule_enable": true}**. The value indicates that the Frequency Control policy is enabled.
        # 
        # If you set **PolicyType** to **2**, the value is **{"ai_rule_enable": 1}**. The value indicates that the Intelligent Protection policy is enabled.
        self.old_value = old_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSceneDefensePoliciesResponseBodyPoliciesRuntimePolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_value is not None:
            result['NewValue'] = self.new_value
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.status is not None:
            result['Status'] = self.status
        if self.old_value is not None:
            result['oldValue'] = self.old_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('oldValue') is not None:
            self.old_value = m.get('oldValue')
        return self


class DescribeSceneDefensePoliciesResponseBodyPolicies(TeaModel):
    def __init__(self, done=None, end_time=None, name=None, object_count=None, policy_id=None, runtime_policies=None,
                 start_time=None, status=None, template=None):
        # The execution status of the policy. Valid values:
        # 
        # *   **1**: not executed or execution completed
        # *   **0**: being executed
        # *   **-1**: execution failed
        self.done = done  # type: int
        # The time at which the policy expires. The value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The name of the policy.
        self.name = name  # type: str
        # The number of objects that are protected by the policy.
        self.object_count = object_count  # type: int
        # The ID of the policy.
        self.policy_id = policy_id  # type: str
        # The running rules of the policy.
        self.runtime_policies = runtime_policies  # type: list[DescribeSceneDefensePoliciesResponseBodyPoliciesRuntimePolicies]
        # The time at which the policy takes effect. The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time  # type: long
        # The status of the policy. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: pending enabling
        # *   **2**: enabled
        # *   **3**: expired
        self.status = status  # type: int
        # The type of the template that is used to create the policy. Valid values:
        # 
        # *   **promotion**: the Important Activity template
        # *   **bypass**: the Forward All template
        self.template = template  # type: str

    def validate(self):
        if self.runtime_policies:
            for k in self.runtime_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSceneDefensePoliciesResponseBodyPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.done is not None:
            result['Done'] = self.done
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.name is not None:
            result['Name'] = self.name
        if self.object_count is not None:
            result['ObjectCount'] = self.object_count
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        result['RuntimePolicies'] = []
        if self.runtime_policies is not None:
            for k in self.runtime_policies:
                result['RuntimePolicies'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Done') is not None:
            self.done = m.get('Done')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ObjectCount') is not None:
            self.object_count = m.get('ObjectCount')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        self.runtime_policies = []
        if m.get('RuntimePolicies') is not None:
            for k in m.get('RuntimePolicies'):
                temp_model = DescribeSceneDefensePoliciesResponseBodyPoliciesRuntimePolicies()
                self.runtime_policies.append(temp_model.from_map(k))
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class DescribeSceneDefensePoliciesResponseBody(TeaModel):
    def __init__(self, policies=None, request_id=None, success=None):
        # An array that consists of the configurations of the scenario-specific custom policy.
        self.policies = policies  # type: list[DescribeSceneDefensePoliciesResponseBodyPolicies]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success  # type: bool

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSceneDefensePoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSceneDefensePoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSceneDefensePoliciesResponse, self).to_map()
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
            temp_model = DescribeSceneDefensePoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSchedulerRulesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, resource_group_id=None, rule_name=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSchedulerRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DescribeSchedulerRulesResponseBodySchedulerRulesParamParamData(TeaModel):
    def __init__(self, cloud_instance_id=None):
        self.cloud_instance_id = cloud_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSchedulerRulesResponseBodySchedulerRulesParamParamData, self).to_map()
        if _map is not None:
            return _map

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
        self.param_type = param_type  # type: str

    def validate(self):
        if self.param_data:
            self.param_data.validate()

    def to_map(self):
        _map = super(DescribeSchedulerRulesResponseBodySchedulerRulesParam, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, priority=None, region_id=None, restore_delay=None, status=None, type=None, value=None,
                 value_type=None):
        self.priority = priority  # type: int
        self.region_id = region_id  # type: str
        self.restore_delay = restore_delay  # type: int
        self.status = status  # type: int
        self.type = type  # type: str
        self.value = value  # type: str
        self.value_type = value_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSchedulerRulesResponseBodySchedulerRulesRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.restore_delay is not None:
            result['RestoreDelay'] = self.restore_delay
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RestoreDelay') is not None:
            self.restore_delay = m.get('RestoreDelay')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class DescribeSchedulerRulesResponseBodySchedulerRules(TeaModel):
    def __init__(self, cname=None, param=None, rule_name=None, rule_type=None, rules=None):
        self.cname = cname  # type: str
        self.param = param  # type: DescribeSchedulerRulesResponseBodySchedulerRulesParam
        self.rule_name = rule_name  # type: str
        self.rule_type = rule_type  # type: str
        self.rules = rules  # type: list[DescribeSchedulerRulesResponseBodySchedulerRulesRules]

    def validate(self):
        if self.param:
            self.param.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSchedulerRulesResponseBodySchedulerRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.param is not None:
            result['Param'] = self.param.to_map()
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Param') is not None:
            temp_model = DescribeSchedulerRulesResponseBodySchedulerRulesParam()
            self.param = temp_model.from_map(m['Param'])
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeSchedulerRulesResponseBodySchedulerRulesRules()
                self.rules.append(temp_model.from_map(k))
        return self


class DescribeSchedulerRulesResponseBody(TeaModel):
    def __init__(self, request_id=None, scheduler_rules=None, total_count=None):
        self.request_id = request_id  # type: str
        self.scheduler_rules = scheduler_rules  # type: list[DescribeSchedulerRulesResponseBodySchedulerRules]
        self.total_count = total_count  # type: str

    def validate(self):
        if self.scheduler_rules:
            for k in self.scheduler_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSchedulerRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SchedulerRules'] = []
        if self.scheduler_rules is not None:
            for k in self.scheduler_rules:
                result['SchedulerRules'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scheduler_rules = []
        if m.get('SchedulerRules') is not None:
            for k in m.get('SchedulerRules'):
                temp_model = DescribeSchedulerRulesResponseBodySchedulerRules()
                self.scheduler_rules.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSchedulerRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSchedulerRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSchedulerRulesResponse, self).to_map()
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
            temp_model = DescribeSchedulerRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlaEventListRequest(TeaModel):
    def __init__(self, end_time=None, ip=None, page=None, page_size=None, region=None, start_time=None):
        self.end_time = end_time  # type: long
        self.ip = ip  # type: str
        self.page = page  # type: long
        self.page_size = page_size  # type: long
        self.region = region  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlaEventListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region is not None:
            result['Region'] = self.region
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSlaEventListResponseBodySlaEvent(TeaModel):
    def __init__(self, end_time=None, ip=None, region=None, start_time=None):
        self.end_time = end_time  # type: long
        self.ip = ip  # type: str
        self.region = region  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlaEventListResponseBodySlaEvent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.region is not None:
            result['Region'] = self.region
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSlaEventListResponseBody(TeaModel):
    def __init__(self, request_id=None, sla_event=None, total=None):
        self.request_id = request_id  # type: str
        self.sla_event = sla_event  # type: list[DescribeSlaEventListResponseBodySlaEvent]
        self.total = total  # type: long

    def validate(self):
        if self.sla_event:
            for k in self.sla_event:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSlaEventListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SlaEvent'] = []
        if self.sla_event is not None:
            for k in self.sla_event:
                result['SlaEvent'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sla_event = []
        if m.get('SlaEvent') is not None:
            for k in m.get('SlaEvent'):
                temp_model = DescribeSlaEventListResponseBodySlaEvent()
                self.sla_event.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeSlaEventListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSlaEventListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSlaEventListResponse, self).to_map()
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
            temp_model = DescribeSlaEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlsAuthStatusRequest(TeaModel):
    def __init__(self, resource_group_id=None):
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlsAuthStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSlsAuthStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, sls_auth_status=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether Anti-DDoS Pro or Anti-DDoS Premium is authorized to access Log Service. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.sls_auth_status = sls_auth_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlsAuthStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSlsAuthStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSlsAuthStatusResponse, self).to_map()
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
            temp_model = DescribeSlsAuthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlsLogstoreInfoRequest(TeaModel):
    def __init__(self, resource_group_id=None):
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlsLogstoreInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSlsLogstoreInfoResponseBody(TeaModel):
    def __init__(self, log_store=None, project=None, quota=None, request_id=None, ttl=None, used=None):
        # The Logstore of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        self.log_store = log_store  # type: str
        # The Logstore project of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        self.project = project  # type: str
        # The available log storage capacity. Unit: bytes.
        self.quota = quota  # type: long
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The log storage duration. Unit: days.
        self.ttl = ttl  # type: int
        # The used log storage capacity. Unit: bytes.
        # 
        # > The statistics on Log Service are delayed for about two hours.
        self.used = used  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlsLogstoreInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.used is not None:
            result['Used'] = self.used
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Used') is not None:
            self.used = m.get('Used')
        return self


class DescribeSlsLogstoreInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSlsLogstoreInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSlsLogstoreInfoResponse, self).to_map()
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
            temp_model = DescribeSlsLogstoreInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlsOpenStatusRequest(TeaModel):
    def __init__(self, resource_group_id=None):
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlsOpenStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeSlsOpenStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, sls_open_status=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether Log Service is activated. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.sls_open_status = sls_open_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlsOpenStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSlsOpenStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSlsOpenStatusResponse, self).to_map()
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
            temp_model = DescribeSlsOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStsGrantStatusRequest(TeaModel):
    def __init__(self, resource_group_id=None, role=None):
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The name of the RAM role to query. Set the value to **AliyunDDoSCOODefaultRole**, which indicates the default role of Anti-DDoS Pro or Anti-DDoS Premium.
        # 
        # > Anti-DDoS Pro or Anti-DDoS Premium uses the default role to access other cloud services.
        self.role = role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStsGrantStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class DescribeStsGrantStatusResponseBodyStsGrant(TeaModel):
    def __init__(self, status=None):
        # The authorization status. Valid values:
        # 
        # *   **0**: Anti-DDoS Pro or Anti-DDoS Premium is not authorized to access other cloud services.
        # *   **1**: Anti-DDoS Pro or Anti-DDoS Premium is authorized to access other cloud services.
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeStsGrantStatusResponseBodyStsGrant, self).to_map()
        if _map is not None:
            return _map

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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The authorization status of Anti-DDoS Pro or Anti-DDoS Premium.
        self.sts_grant = sts_grant  # type: DescribeStsGrantStatusResponseBodyStsGrant

    def validate(self):
        if self.sts_grant:
            self.sts_grant.validate()

    def to_map(self):
        _map = super(DescribeStsGrantStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeStsGrantStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeStsGrantStatusResponse, self).to_map()
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
            temp_model = DescribeStsGrantStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSystemLogRequest(TeaModel):
    def __init__(self, end_time=None, entity_object=None, entity_type=None, page_number=None, page_size=None,
                 start_time=None):
        # The end of the time range to query. The bills of the burstable clean bandwidth that are issued before this point in time are queried. The value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The IP address of the instance.
        # 
        # > You can call the [DescribeInstanceDetails](~~91490~~) operation to query the IP addresses of all instances.
        self.entity_object = entity_object  # type: str
        # The type of the system log. Set the value to **20**, which indicates the billing logs for the burstable clean bandwidth.
        # 
        # > You must specify this parameter. Otherwise, the call fails.
        self.entity_type = entity_type  # type: int
        # The number of the page to return.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The beginning of the time range to query. The bills of the burstable clean bandwidth that are issued after this point in time are queried. The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSystemLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.entity_object is not None:
            result['EntityObject'] = self.entity_object
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSystemLogResponseBodySystemLog(TeaModel):
    def __init__(self, entity_object=None, entity_type=None, gmt_create=None, gmt_modified=None, op_account=None,
                 op_action=None, op_desc=None, status=None):
        # The IP address of the instance.
        self.entity_object = entity_object  # type: str
        # The type of the system log. The value is fixed as **20**, which indicates the billing logs for burstable clean bandwidth.
        self.entity_type = entity_type  # type: int
        # The time when the bill was generated. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create  # type: long
        # The time when the bill was last modified. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_modified = gmt_modified  # type: long
        # The ID of the Alibaba Cloud account to which the bill belongs.
        self.op_account = op_account  # type: str
        # The operation type. The value is fixed as **100**, which indicates the billing logs for the burstable clean bandwidth that you increased.
        self.op_action = op_action  # type: int
        # The details of the bill. The value is a string that consists of a JSON struct. The JSON struct contains the following fields:
        # 
        # *   **newEntity**: the bill record, which contains the following fields. Data type: object.
        # 
        #     *   **billValue**: the usage of the burstable clean bandwidth within a month. Unit: Mbit/s. Data type: integer.
        #     *   **instanceId**: the ID of the instance. Data type: string.
        #     *   **ip**: the IP address of the instance. Data type: string.
        #     *   **maxBw**: the peak service traffic (monthly 95th percentile bandwidth) within a month. Unit: Mbit/s. Data type: string.
        #     *   **month**: the month in which the bill of the previous calendar month is issued. This value is a UNIX timestamp. Unit: milliseconds. Data type: long.
        #     *   **overBandwidth**: the peak service traffic minus the clean bandwidth of the instance. Unit: Mbit/s. Data type: integer.
        #     *   **peakTime**: the time in point of the peak service traffic that is measured for billing. This value is a UNIX timestamp. Unit: seconds. Data type: long.
        #     *   **startTimestamp**: the beginning of the time range for the peak service traffic range. This value is a UNIX timestamp. Unit: seconds. Data type: long.
        self.op_desc = op_desc  # type: str
        # The status of the bill. Valid values:
        # 
        # *   **0**: to be billed
        # *   **1**: billed
        # *   **2**: terminated
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSystemLogResponseBodySystemLog, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_object is not None:
            result['EntityObject'] = self.entity_object
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.op_account is not None:
            result['OpAccount'] = self.op_account
        if self.op_action is not None:
            result['OpAction'] = self.op_action
        if self.op_desc is not None:
            result['OpDesc'] = self.op_desc
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('OpAccount') is not None:
            self.op_account = m.get('OpAccount')
        if m.get('OpAction') is not None:
            self.op_action = m.get('OpAction')
        if m.get('OpDesc') is not None:
            self.op_desc = m.get('OpDesc')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSystemLogResponseBody(TeaModel):
    def __init__(self, request_id=None, system_log=None, total=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array that consists of details of the billing logs for the burstable clean bandwidth.
        self.system_log = system_log  # type: list[DescribeSystemLogResponseBodySystemLog]
        # The total number of billing logs for the burstable clean bandwidth.
        self.total = total  # type: long

    def validate(self):
        if self.system_log:
            for k in self.system_log:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSystemLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SystemLog'] = []
        if self.system_log is not None:
            for k in self.system_log:
                result['SystemLog'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.system_log = []
        if m.get('SystemLog') is not None:
            for k in m.get('SystemLog'):
                temp_model = DescribeSystemLogResponseBodySystemLog()
                self.system_log.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeSystemLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSystemLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSystemLogResponse, self).to_map()
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
            temp_model = DescribeSystemLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagKeysRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None, resource_group_id=None, resource_type=None):
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size  # type: int
        # The region ID of the instance. Set the value to **cn-hangzhou**, which indicates an Anti-DDoS Pro instance in the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The type of the resource to which the tag belongs. Set the value to **INSTANCE**, which indicates an Anti-DDoS Pro instance.
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTagKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeTagKeysResponseBodyTagKeys(TeaModel):
    def __init__(self, tag_count=None, tag_key=None):
        # The number of Anti-DDoS Pro instances to which the tag key is added.
        self.tag_count = tag_count  # type: int
        # The tag key.
        self.tag_key = tag_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTagKeysResponseBodyTagKeys, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, page_number=None, page_size=None, request_id=None, tag_keys=None, total_count=None):
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned on each page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array that consists of the details of the tag key.
        self.tag_keys = tag_keys  # type: list[DescribeTagKeysResponseBodyTagKeys]
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.tag_keys:
            for k in self.tag_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTagKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k in self.tag_keys:
                result['TagKeys'].append(k.to_map() if k else None)
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
        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k in m.get('TagKeys'):
                temp_model = DescribeTagKeysResponseBodyTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTagKeysResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTagKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTagKeysResponse, self).to_map()
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
            temp_model = DescribeTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagResourcesRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag that you want to query.
        # 
        # > 
        # 
        # *   You must specify at least one of the **ResourceIds.N** and **Tags.N.Key** parameters.
        # 
        # *   You can call the [DescribeTagKeys](~~159785~~) operation to query all tag keys.
        self.key = key  # type: str
        # The value of the tag that you want to query.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTagResourcesRequestTags, self).to_map()
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
    def __init__(self, next_token=None, region_id=None, resource_group_id=None, resource_ids=None,
                 resource_type=None, tags=None):
        # The query token. Set the value to the value of **NextToken** that is returned in the last call.
        # 
        # > You do not need to configure this parameter if you call this operation for the first time.
        self.next_token = next_token  # type: str
        # The region ID of the instance. Set the value to **cn-hangzhou**, which indicates an Anti-DDoS Pro instance in the Chinese mainland.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # An array consisting of IDs of the Anti-DDoS Pro instances that you want to query.
        self.resource_ids = resource_ids  # type: list[str]
        # The type of the resource to which the tag belongs. Set the value to **INSTANCE**, which indicates an Anti-DDoS Pro instance.
        self.resource_type = resource_type  # type: str
        # An array consisting of tags that you want to query. Each tag consists of a tag **key** and a tag **value**.
        self.tags = tags  # type: list[DescribeTagResourcesRequestTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeTagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        # The ID of the Anti-DDoS Pro instance.
        self.resource_id = resource_id  # type: str
        # The type of the resource. The value is fixed as **INSTANCE**, which indicates an Anti-DDoS Pro instance.
        self.resource_type = resource_type  # type: str
        # The key of the tag that is added to the Anti-DDoS Pro instance.
        self.tag_key = tag_key  # type: str
        # The value of the tag that is added to the Anti-DDoS Pro instance.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTagResourcesResponseBodyTagResourcesTagResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
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
        _map = super(DescribeTagResourcesResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

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
        # The query token that is returned in this call.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array consisting of the details of the tags that are added to the Anti-DDoS Pro instance.
        self.tag_resources = tag_resources  # type: DescribeTagResourcesResponseBodyTagResources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super(DescribeTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTotalAttackMaxFlowRequest(TeaModel):
    def __init__(self, end_time=None, instance_ids=None, resource_group_id=None, start_time=None):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time  # type: long
        # The IDs of the instances. Separate multiple instance IDs with commas (,). Example: InstanceIds.1, InstanceIds.2, InstanceIds.3.
        self.instance_ids = instance_ids  # type: list[str]
        # The ID of the resource group to which the instance belongs in Resource Management. If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTotalAttackMaxFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeTotalAttackMaxFlowResponseBody(TeaModel):
    def __init__(self, bps=None, pps=None, request_id=None):
        # The peak bandwidth of attack traffic. Unit: bit/s.
        self.bps = bps  # type: long
        # The peak packet rate of attack traffic . Unit: packets per second (pps).
        self.pps = pps  # type: long
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTotalAttackMaxFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTotalAttackMaxFlowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTotalAttackMaxFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTotalAttackMaxFlowResponse, self).to_map()
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
            temp_model = DescribeTotalAttackMaxFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUdpReflectRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        # The ID of the instance to query.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # The region ID of the instance. Valid values:
        # 
        # *   **cn-hangzhou**: Chinese mainland, which indicates an Anti-DDoS Pro instance. This is the default value.
        # *   **ap-southeast-1**: outside the Chinese mainland, which indicates an Anti-DDoS Premium instance.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUdpReflectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeUdpReflectResponseBody(TeaModel):
    def __init__(self, request_id=None, udp_sports=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array consisting of the source ports of the UDP traffic that are filtered out by the filtering policies for UDP reflection attacks.
        self.udp_sports = udp_sports  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUdpReflectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.udp_sports is not None:
            result['UdpSports'] = self.udp_sports
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UdpSports') is not None:
            self.udp_sports = m.get('UdpSports')
        return self


class DescribeUdpReflectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUdpReflectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUdpReflectResponse, self).to_map()
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
            temp_model = DescribeUdpReflectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUnBlackholeCountRequest(TeaModel):
    def __init__(self, resource_group_id=None):
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUnBlackholeCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeUnBlackholeCountResponseBody(TeaModel):
    def __init__(self, remain_count=None, request_id=None, total_count=None):
        # The remaining quota that you can deactivate blackhole filtering.
        self.remain_count = remain_count  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total quota that you can deactivate blackhole filtering.
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUnBlackholeCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remain_count is not None:
            result['RemainCount'] = self.remain_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RemainCount') is not None:
            self.remain_count = m.get('RemainCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeUnBlackholeCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUnBlackholeCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUnBlackholeCountResponse, self).to_map()
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
            temp_model = DescribeUnBlackholeCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUnBlockCountRequest(TeaModel):
    def __init__(self, resource_group_id=None):
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUnBlockCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeUnBlockCountResponseBody(TeaModel):
    def __init__(self, remain_count=None, request_id=None, total_count=None):
        # The remaining quota that you can use the Diversion from Origin Server policy.
        self.remain_count = remain_count  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total quota that you can use the Diversion from Origin Server policy.
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUnBlockCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remain_count is not None:
            result['RemainCount'] = self.remain_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RemainCount') is not None:
            self.remain_count = m.get('RemainCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeUnBlockCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUnBlockCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUnBlockCountResponse, self).to_map()
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
            temp_model = DescribeUnBlockCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebAccessLogDispatchStatusRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, resource_group_id=None):
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size  # type: int
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebAccessLogDispatchStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeWebAccessLogDispatchStatusResponseBodySlsConfigStatus(TeaModel):
    def __init__(self, domain=None, enable=None):
        # The domain name.
        self.domain = domain  # type: str
        # Indicates whether the log analysis feature is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.enable = enable  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebAccessLogDispatchStatusResponseBodySlsConfigStatus, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, request_id=None, sls_config_status=None, total_count=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the log analysis feature is enabled for domain names.
        self.sls_config_status = sls_config_status  # type: list[DescribeWebAccessLogDispatchStatusResponseBodySlsConfigStatus]
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.sls_config_status:
            for k in self.sls_config_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebAccessLogDispatchStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SlsConfigStatus'] = []
        if self.sls_config_status is not None:
            for k in self.sls_config_status:
                result['SlsConfigStatus'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sls_config_status = []
        if m.get('SlsConfigStatus') is not None:
            for k in m.get('SlsConfigStatus'):
                temp_model = DescribeWebAccessLogDispatchStatusResponseBodySlsConfigStatus()
                self.sls_config_status.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeWebAccessLogDispatchStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebAccessLogDispatchStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebAccessLogDispatchStatusResponse, self).to_map()
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
            temp_model = DescribeWebAccessLogDispatchStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebAccessLogEmptyCountRequest(TeaModel):
    def __init__(self, resource_group_id=None):
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebAccessLogEmptyCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeWebAccessLogEmptyCountResponseBody(TeaModel):
    def __init__(self, available_count=None, request_id=None):
        # The remaining quota that you can clear the Logstore.
        self.available_count = available_count  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebAccessLogEmptyCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_count is not None:
            result['AvailableCount'] = self.available_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableCount') is not None:
            self.available_count = m.get('AvailableCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWebAccessLogEmptyCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebAccessLogEmptyCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebAccessLogEmptyCountResponse, self).to_map()
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
            temp_model = DescribeWebAccessLogEmptyCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebAccessLogStatusRequest(TeaModel):
    def __init__(self, domain=None, resource_group_id=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebAccessLogStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeWebAccessLogStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, sls_logstore=None, sls_project=None, sls_status=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The Logstore of the instance.
        self.sls_logstore = sls_logstore  # type: str
        # The Log Service project of the instance.
        self.sls_project = sls_project  # type: str
        # Indicates whether the Log Analysis feature is enabled for the website. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.sls_status = sls_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebAccessLogStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_logstore is not None:
            result['SlsLogstore'] = self.sls_logstore
        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project
        if self.sls_status is not None:
            result['SlsStatus'] = self.sls_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsLogstore') is not None:
            self.sls_logstore = m.get('SlsLogstore')
        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')
        if m.get('SlsStatus') is not None:
            self.sls_status = m.get('SlsStatus')
        return self


class DescribeWebAccessLogStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebAccessLogStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebAccessLogStatusResponse, self).to_map()
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
            temp_model = DescribeWebAccessLogStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebAccessModeRequest(TeaModel):
    def __init__(self, domains=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for a domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domains = domains  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebAccessModeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class DescribeWebAccessModeResponseBodyDomainModes(TeaModel):
    def __init__(self, access_mode=None, domain=None):
        # The mode in which the website service is added. Valid values:
        # 
        # *   **0**: A record
        # *   **1**: anti-DDoS mode
        # *   **2**: origin redundancy mode
        self.access_mode = access_mode  # type: int
        # The domain name of the website.
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebAccessModeResponseBodyDomainModes, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, domain_modes=None, request_id=None):
        # An array consisting of the modes in which the website service is added.
        self.domain_modes = domain_modes  # type: list[DescribeWebAccessModeResponseBodyDomainModes]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_modes:
            for k in self.domain_modes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebAccessModeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainModes'] = []
        if self.domain_modes is not None:
            for k in self.domain_modes:
                result['DomainModes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_modes = []
        if m.get('DomainModes') is not None:
            for k in m.get('DomainModes'):
                temp_model = DescribeWebAccessModeResponseBodyDomainModes()
                self.domain_modes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWebAccessModeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebAccessModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebAccessModeResponse, self).to_map()
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
            temp_model = DescribeWebAccessModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebAreaBlockConfigsRequest(TeaModel):
    def __init__(self, domains=None, resource_group_id=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domains = domains  # type: list[str]
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebAreaBlockConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigsRegionList(TeaModel):
    def __init__(self, block=None, region=None):
        # Indicates whether the location is blocked. Valid values:
        # 
        # *   **0**: yes
        # *   **1**: no
        self.block = block  # type: int
        # The name of the location.
        self.region = region  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigsRegionList, self).to_map()
        if _map is not None:
            return _map

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
        # The domain name of the website.
        self.domain = domain  # type: str
        # The configuration of the blocked locations.
        self.region_list = region_list  # type: list[DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigsRegionList]

    def validate(self):
        if self.region_list:
            for k in self.region_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigs, self).to_map()
        if _map is not None:
            return _map

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
        # An array that consists of the configurations of the Location Blacklist (Domain Names) policy.
        self.area_block_configs = area_block_configs  # type: list[DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigs]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.area_block_configs:
            for k in self.area_block_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebAreaBlockConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebAreaBlockConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebAreaBlockConfigsResponse, self).to_map()
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
            temp_model = DescribeWebAreaBlockConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebCCRulesRequest(TeaModel):
    def __init__(self, domain=None, page_number=None, page_size=None, resource_group_id=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The number of the page to return. For example, to query the returned results on the first page, set the value to **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebCCRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeWebCCRulesResponseBodyWebCCRules(TeaModel):
    def __init__(self, act=None, count=None, interval=None, mode=None, name=None, ttl=None, uri=None):
        # The blocking type. Valid values:
        # 
        # *   **close**: blocks requests.
        # *   **captcha**: enables Completely Automated Public Turing test to tell Computers and Humans Apart (CAPTCHA) verification.
        self.act = act  # type: str
        # The number of requests that are allowed from an individual IP address. Valid values: **2** to **2000**.
        self.count = count  # type: int
        # The check intervals. Valid values: **5** to **10800**. Unit: seconds.
        self.interval = interval  # type: int
        # The match mode. Valid values:
        # 
        # *   **prefix**: prefix match
        # *   **match**: exact match
        self.mode = mode  # type: str
        # The name of the rule.
        self.name = name  # type: str
        # The blocking duration. Valid values: **1** to **1440**. Unit: minutes.
        self.ttl = ttl  # type: int
        # The check path.
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebCCRulesResponseBodyWebCCRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.act is not None:
            result['Act'] = self.act
        if self.count is not None:
            result['Count'] = self.count
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.name is not None:
            result['Name'] = self.name
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DescribeWebCCRulesResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, web_ccrules=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of returned custom frequency control rules.
        self.total_count = total_count  # type: long
        # An array that consists of the details of the custom frequency control rule.
        self.web_ccrules = web_ccrules  # type: list[DescribeWebCCRulesResponseBodyWebCCRules]

    def validate(self):
        if self.web_ccrules:
            for k in self.web_ccrules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebCCRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['WebCCRules'] = []
        if self.web_ccrules is not None:
            for k in self.web_ccrules:
                result['WebCCRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.web_ccrules = []
        if m.get('WebCCRules') is not None:
            for k in m.get('WebCCRules'):
                temp_model = DescribeWebCCRulesResponseBodyWebCCRules()
                self.web_ccrules.append(temp_model.from_map(k))
        return self


class DescribeWebCCRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebCCRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebCCRulesResponse, self).to_map()
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
            temp_model = DescribeWebCCRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebCacheConfigsRequest(TeaModel):
    def __init__(self, domains=None, resource_group_id=None):
        # An array consisting of domain names for which you want to query the Static Page Caching configurations.
        self.domains = domains  # type: list[str]
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebCacheConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeWebCacheConfigsResponseBodyDomainCacheConfigsCustomRules(TeaModel):
    def __init__(self, cache_ttl=None, mode=None, name=None, uri=None):
        # The expiration time of the page cache. Unit: seconds.
        self.cache_ttl = cache_ttl  # type: long
        # The cache mode. Valid values:
        # 
        # *   **standard**: The standard cache mode is used.
        # *   **aggressive**: The enhanced cache mode is used.
        # *   **bypass**: No data is cached.
        self.mode = mode  # type: str
        # The name of the rule.
        self.name = name  # type: str
        # The path to the cached page.
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebCacheConfigsResponseBodyDomainCacheConfigsCustomRules, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, custom_rules=None, domain=None, enable=None, mode=None):
        # An array that consists of custom caching rules.
        self.custom_rules = custom_rules  # type: list[DescribeWebCacheConfigsResponseBodyDomainCacheConfigsCustomRules]
        # The domain name of the website.
        self.domain = domain  # type: str
        # The status of the Static Page Caching policy. Valid values:
        # 
        # *   **1**: enabled
        # *   **0**: disabled
        self.enable = enable  # type: int
        # The cache mode. Valid values:
        # 
        # *   **standard**: The standard cache mode is used.
        # *   **aggressive**: The enhanced cache mode is used.
        # *   **bypass**: No data is cached.
        self.mode = mode  # type: str

    def validate(self):
        if self.custom_rules:
            for k in self.custom_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebCacheConfigsResponseBodyDomainCacheConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomRules'] = []
        if self.custom_rules is not None:
            for k in self.custom_rules:
                result['CustomRules'].append(k.to_map() if k else None)
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.custom_rules = []
        if m.get('CustomRules') is not None:
            for k in m.get('CustomRules'):
                temp_model = DescribeWebCacheConfigsResponseBodyDomainCacheConfigsCustomRules()
                self.custom_rules.append(temp_model.from_map(k))
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class DescribeWebCacheConfigsResponseBody(TeaModel):
    def __init__(self, domain_cache_configs=None, request_id=None):
        # An array that consists of Static Page Caching configurations.
        self.domain_cache_configs = domain_cache_configs  # type: list[DescribeWebCacheConfigsResponseBodyDomainCacheConfigs]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_cache_configs:
            for k in self.domain_cache_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebCacheConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainCacheConfigs'] = []
        if self.domain_cache_configs is not None:
            for k in self.domain_cache_configs:
                result['DomainCacheConfigs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_cache_configs = []
        if m.get('DomainCacheConfigs') is not None:
            for k in m.get('DomainCacheConfigs'):
                temp_model = DescribeWebCacheConfigsResponseBodyDomainCacheConfigs()
                self.domain_cache_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWebCacheConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebCacheConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebCacheConfigsResponse, self).to_map()
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
            temp_model = DescribeWebCacheConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebCcProtectSwitchRequest(TeaModel):
    def __init__(self, domains=None, resource_group_id=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domains = domains  # type: list[str]
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebCcProtectSwitchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeWebCcProtectSwitchResponseBodyProtectSwitchList(TeaModel):
    def __init__(self, ai_mode=None, ai_rule_enable=None, ai_template=None, black_white_list_enable=None,
                 cc_custom_rule_enable=None, cc_enable=None, cc_template=None, domain=None, precise_rule_enable=None,
                 region_block_enable=None):
        # The mode of the Intelligent Protection policy. Valid values:
        # 
        # *   **watch**: the Warning mode
        # *   **defense**: the Defense mode
        self.ai_mode = ai_mode  # type: str
        # The status of the Intelligent Protection policy. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.ai_rule_enable = ai_rule_enable  # type: int
        # The level of the Intelligent Protection policy. Valid values:
        # 
        # *   **level30**: the Low level
        # *   **level60**: the Normal level
        # *   **level90**: the Strict level
        self.ai_template = ai_template  # type: str
        # The status of the Black Lists and White Lists (Domain Names) policy. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.black_white_list_enable = black_white_list_enable  # type: int
        # The status of the Custom Rule switch for the Frequency Control policy. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.cc_custom_rule_enable = cc_custom_rule_enable  # type: int
        # The status of the Frequency Control policy. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.cc_enable = cc_enable  # type: int
        # The mode of the Frequency Control policy. Valid values:
        # 
        # *   **default**: Normal
        # *   **gf_under_attack**: Emergency
        # *   **gf_sos_verify**: Strict
        # *   **gf_sos_enhance**: Super Strict
        self.cc_template = cc_template  # type: str
        # The domain name of the website.
        self.domain = domain  # type: str
        # The status of the Accurate Access Control policy. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.precise_rule_enable = precise_rule_enable  # type: int
        # The status of the Location Blacklist (Domain Names) policy. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.region_block_enable = region_block_enable  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebCcProtectSwitchResponseBodyProtectSwitchList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_mode is not None:
            result['AiMode'] = self.ai_mode
        if self.ai_rule_enable is not None:
            result['AiRuleEnable'] = self.ai_rule_enable
        if self.ai_template is not None:
            result['AiTemplate'] = self.ai_template
        if self.black_white_list_enable is not None:
            result['BlackWhiteListEnable'] = self.black_white_list_enable
        if self.cc_custom_rule_enable is not None:
            result['CcCustomRuleEnable'] = self.cc_custom_rule_enable
        if self.cc_enable is not None:
            result['CcEnable'] = self.cc_enable
        if self.cc_template is not None:
            result['CcTemplate'] = self.cc_template
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.precise_rule_enable is not None:
            result['PreciseRuleEnable'] = self.precise_rule_enable
        if self.region_block_enable is not None:
            result['RegionBlockEnable'] = self.region_block_enable
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AiMode') is not None:
            self.ai_mode = m.get('AiMode')
        if m.get('AiRuleEnable') is not None:
            self.ai_rule_enable = m.get('AiRuleEnable')
        if m.get('AiTemplate') is not None:
            self.ai_template = m.get('AiTemplate')
        if m.get('BlackWhiteListEnable') is not None:
            self.black_white_list_enable = m.get('BlackWhiteListEnable')
        if m.get('CcCustomRuleEnable') is not None:
            self.cc_custom_rule_enable = m.get('CcCustomRuleEnable')
        if m.get('CcEnable') is not None:
            self.cc_enable = m.get('CcEnable')
        if m.get('CcTemplate') is not None:
            self.cc_template = m.get('CcTemplate')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PreciseRuleEnable') is not None:
            self.precise_rule_enable = m.get('PreciseRuleEnable')
        if m.get('RegionBlockEnable') is not None:
            self.region_block_enable = m.get('RegionBlockEnable')
        return self


class DescribeWebCcProtectSwitchResponseBody(TeaModel):
    def __init__(self, protect_switch_list=None, request_id=None):
        # The status of each protection policy for a website.
        self.protect_switch_list = protect_switch_list  # type: list[DescribeWebCcProtectSwitchResponseBodyProtectSwitchList]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.protect_switch_list:
            for k in self.protect_switch_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebCcProtectSwitchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProtectSwitchList'] = []
        if self.protect_switch_list is not None:
            for k in self.protect_switch_list:
                result['ProtectSwitchList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.protect_switch_list = []
        if m.get('ProtectSwitchList') is not None:
            for k in m.get('ProtectSwitchList'):
                temp_model = DescribeWebCcProtectSwitchResponseBodyProtectSwitchList()
                self.protect_switch_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWebCcProtectSwitchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebCcProtectSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebCcProtectSwitchResponse, self).to_map()
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
            temp_model = DescribeWebCcProtectSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebCustomPortsRequest(TeaModel):
    def __init__(self, resource_group_id=None):
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebCustomPortsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeWebCustomPortsResponseBodyWebCustomPorts(TeaModel):
    def __init__(self, proxy_ports=None, proxy_type=None):
        # An array that consists of supported custom ports.
        self.proxy_ports = proxy_ports  # type: list[str]
        # The type of the protocol. Valid values:
        # 
        # *   **http**\
        # *   **https**\
        self.proxy_type = proxy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebCustomPortsResponseBodyWebCustomPorts, self).to_map()
        if _map is not None:
            return _map

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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array consisting of information about supported custom ports that are used by a website.
        self.web_custom_ports = web_custom_ports  # type: list[DescribeWebCustomPortsResponseBodyWebCustomPorts]

    def validate(self):
        if self.web_custom_ports:
            for k in self.web_custom_ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebCustomPortsResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebCustomPortsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebCustomPortsResponse, self).to_map()
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
            temp_model = DescribeWebCustomPortsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebInstanceRelationsRequest(TeaModel):
    def __init__(self, domains=None, resource_group_id=None):
        # The domain names of the website. list
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domains = domains  # type: list[str]
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebInstanceRelationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeWebInstanceRelationsResponseBodyWebInstanceRelationsInstanceDetails(TeaModel):
    def __init__(self, eip_list=None, function_version=None, instance_id=None):
        # The IP addresses of the instance.
        self.eip_list = eip_list  # type: list[str]
        # The function plan of the instance. Valid values:
        # 
        # *   **default**: Standard function plan
        # *   **enhance**: Enhanced function plan
        self.function_version = function_version  # type: str
        # The ID of the instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebInstanceRelationsResponseBodyWebInstanceRelationsInstanceDetails, self).to_map()
        if _map is not None:
            return _map

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
        # The domain name of the website.
        self.domain = domain  # type: str
        # The information about the instance to which a website service is added.
        self.instance_details = instance_details  # type: list[DescribeWebInstanceRelationsResponseBodyWebInstanceRelationsInstanceDetails]

    def validate(self):
        if self.instance_details:
            for k in self.instance_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebInstanceRelationsResponseBodyWebInstanceRelations, self).to_map()
        if _map is not None:
            return _map

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
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information about the instances to which a website service is added.
        self.web_instance_relations = web_instance_relations  # type: list[DescribeWebInstanceRelationsResponseBodyWebInstanceRelations]

    def validate(self):
        if self.web_instance_relations:
            for k in self.web_instance_relations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebInstanceRelationsResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebInstanceRelationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebInstanceRelationsResponse, self).to_map()
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
            temp_model = DescribeWebInstanceRelationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebPreciseAccessRuleRequest(TeaModel):
    def __init__(self, domains=None, resource_group_id=None):
        # An array that consists of the domain names of websites.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domains = domains  # type: list[str]
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebPreciseAccessRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleListConditionList(TeaModel):
    def __init__(self, content=None, field=None, header_name=None, match_method=None):
        # The match content.
        self.content = content  # type: str
        # The match field.
        self.field = field  # type: str
        # The custom HTTP header.
        # 
        # > This parameter takes effect only when **Field** is set to **header**.
        self.header_name = header_name  # type: str
        # The logical operator.
        self.match_method = match_method  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleListConditionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.field is not None:
            result['Field'] = self.field
        if self.header_name is not None:
            result['HeaderName'] = self.header_name
        if self.match_method is not None:
            result['MatchMethod'] = self.match_method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('HeaderName') is not None:
            self.header_name = m.get('HeaderName')
        if m.get('MatchMethod') is not None:
            self.match_method = m.get('MatchMethod')
        return self


class DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleList(TeaModel):
    def __init__(self, action=None, condition_list=None, expires=None, name=None, owner=None):
        # The action triggered if the rule is matched. Valid values:
        # 
        # *   **accept**: allows the requests that match the rule.
        # *   **block**: blocks the requests that match the rule.
        # *   **challenge**: implements Completely Automated Public Turing test to tell Computers and Humans Apart (CAPTCHA) verification for the requests that match the rule.
        self.action = action  # type: str
        # The match conditions.
        self.condition_list = condition_list  # type: list[DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleListConditionList]
        # The validity period of the rule. Unit: seconds. This parameter takes effect only when **action** of a rule is **block**. Access requests that match the rule are blocked within the specified validity period of the rule. **0** indicates that the rule takes effect all the time.
        self.expires = expires  # type: long
        # The name of the rule.
        self.name = name  # type: str
        # The source of the rule. Valid values:
        # 
        # *   **manual**: manually created. This is the default value.
        # *   **auto**: automatically generated.
        self.owner = owner  # type: str

    def validate(self):
        if self.condition_list:
            for k in self.condition_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        result['ConditionList'] = []
        if self.condition_list is not None:
            for k in self.condition_list:
                result['ConditionList'].append(k.to_map() if k else None)
        if self.expires is not None:
            result['Expires'] = self.expires
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        self.condition_list = []
        if m.get('ConditionList') is not None:
            for k in m.get('ConditionList'):
                temp_model = DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleListConditionList()
                self.condition_list.append(temp_model.from_map(k))
        if m.get('Expires') is not None:
            self.expires = m.get('Expires')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        return self


class DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigList(TeaModel):
    def __init__(self, domain=None, rule_list=None):
        # The domain name of the website.
        self.domain = domain  # type: str
        # An array that consists of the rules.
        self.rule_list = rule_list  # type: list[DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigListRuleList]

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigList, self).to_map()
        if _map is not None:
            return _map

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
        # An array consisting of the configuration of the accurate access control rule that is created for the website.
        self.precise_access_config_list = precise_access_config_list  # type: list[DescribeWebPreciseAccessRuleResponseBodyPreciseAccessConfigList]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.precise_access_config_list:
            for k in self.precise_access_config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebPreciseAccessRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebPreciseAccessRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebPreciseAccessRuleResponse, self).to_map()
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
            temp_model = DescribeWebPreciseAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebRulesRequest(TeaModel):
    def __init__(self, cname=None, domain=None, instance_ids=None, page_number=None, page_size=None,
                 query_domain_pattern=None, resource_group_id=None):
        self.cname = cname  # type: str
        self.domain = domain  # type: str
        self.instance_ids = instance_ids  # type: list[str]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.query_domain_pattern = query_domain_pattern  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_domain_pattern is not None:
            result['QueryDomainPattern'] = self.query_domain_pattern
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryDomainPattern') is not None:
            self.query_domain_pattern = m.get('QueryDomainPattern')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeWebRulesResponseBodyWebRulesGmCert(TeaModel):
    def __init__(self, cert_id=None, gm_enable=None, gm_only=None):
        self.cert_id = cert_id  # type: str
        self.gm_enable = gm_enable  # type: long
        self.gm_only = gm_only  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebRulesResponseBodyWebRulesGmCert, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.gm_enable is not None:
            result['GmEnable'] = self.gm_enable
        if self.gm_only is not None:
            result['GmOnly'] = self.gm_only
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('GmEnable') is not None:
            self.gm_enable = m.get('GmEnable')
        if m.get('GmOnly') is not None:
            self.gm_only = m.get('GmOnly')
        return self


class DescribeWebRulesResponseBodyWebRulesProxyTypes(TeaModel):
    def __init__(self, proxy_ports=None, proxy_type=None):
        self.proxy_ports = proxy_ports  # type: list[str]
        self.proxy_type = proxy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebRulesResponseBodyWebRulesProxyTypes, self).to_map()
        if _map is not None:
            return _map

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


class DescribeWebRulesResponseBodyWebRulesRealServers(TeaModel):
    def __init__(self, real_server=None, rs_type=None):
        self.real_server = real_server  # type: str
        self.rs_type = rs_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeWebRulesResponseBodyWebRulesRealServers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.real_server is not None:
            result['RealServer'] = self.real_server
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RealServer') is not None:
            self.real_server = m.get('RealServer')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        return self


class DescribeWebRulesResponseBodyWebRules(TeaModel):
    def __init__(self, black_list=None, cc_enabled=None, cc_rule_enabled=None, cc_template=None, cert_name=None,
                 cert_region=None, cname=None, custom_ciphers=None, domain=None, gm_cert=None, http_2enable=None,
                 http_2https_enable=None, https_2http_enable=None, ocsp_enabled=None, policy_mode=None, proxy_enabled=None,
                 proxy_types=None, punish_reason=None, punish_status=None, real_servers=None, ssl_13enabled=None,
                 ssl_ciphers=None, ssl_protocols=None, white_list=None):
        self.black_list = black_list  # type: list[str]
        self.cc_enabled = cc_enabled  # type: bool
        self.cc_rule_enabled = cc_rule_enabled  # type: bool
        self.cc_template = cc_template  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_region = cert_region  # type: str
        self.cname = cname  # type: str
        self.custom_ciphers = custom_ciphers  # type: list[str]
        self.domain = domain  # type: str
        self.gm_cert = gm_cert  # type: DescribeWebRulesResponseBodyWebRulesGmCert
        self.http_2enable = http_2enable  # type: bool
        self.http_2https_enable = http_2https_enable  # type: bool
        self.https_2http_enable = https_2http_enable  # type: bool
        self.ocsp_enabled = ocsp_enabled  # type: bool
        self.policy_mode = policy_mode  # type: str
        self.proxy_enabled = proxy_enabled  # type: bool
        self.proxy_types = proxy_types  # type: list[DescribeWebRulesResponseBodyWebRulesProxyTypes]
        self.punish_reason = punish_reason  # type: int
        self.punish_status = punish_status  # type: bool
        self.real_servers = real_servers  # type: list[DescribeWebRulesResponseBodyWebRulesRealServers]
        self.ssl_13enabled = ssl_13enabled  # type: bool
        self.ssl_ciphers = ssl_ciphers  # type: str
        self.ssl_protocols = ssl_protocols  # type: str
        self.white_list = white_list  # type: list[str]

    def validate(self):
        if self.gm_cert:
            self.gm_cert.validate()
        if self.proxy_types:
            for k in self.proxy_types:
                if k:
                    k.validate()
        if self.real_servers:
            for k in self.real_servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebRulesResponseBodyWebRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_list is not None:
            result['BlackList'] = self.black_list
        if self.cc_enabled is not None:
            result['CcEnabled'] = self.cc_enabled
        if self.cc_rule_enabled is not None:
            result['CcRuleEnabled'] = self.cc_rule_enabled
        if self.cc_template is not None:
            result['CcTemplate'] = self.cc_template
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_region is not None:
            result['CertRegion'] = self.cert_region
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.custom_ciphers is not None:
            result['CustomCiphers'] = self.custom_ciphers
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.gm_cert is not None:
            result['GmCert'] = self.gm_cert.to_map()
        if self.http_2enable is not None:
            result['Http2Enable'] = self.http_2enable
        if self.http_2https_enable is not None:
            result['Http2HttpsEnable'] = self.http_2https_enable
        if self.https_2http_enable is not None:
            result['Https2HttpEnable'] = self.https_2http_enable
        if self.ocsp_enabled is not None:
            result['OcspEnabled'] = self.ocsp_enabled
        if self.policy_mode is not None:
            result['PolicyMode'] = self.policy_mode
        if self.proxy_enabled is not None:
            result['ProxyEnabled'] = self.proxy_enabled
        result['ProxyTypes'] = []
        if self.proxy_types is not None:
            for k in self.proxy_types:
                result['ProxyTypes'].append(k.to_map() if k else None)
        if self.punish_reason is not None:
            result['PunishReason'] = self.punish_reason
        if self.punish_status is not None:
            result['PunishStatus'] = self.punish_status
        result['RealServers'] = []
        if self.real_servers is not None:
            for k in self.real_servers:
                result['RealServers'].append(k.to_map() if k else None)
        if self.ssl_13enabled is not None:
            result['Ssl13Enabled'] = self.ssl_13enabled
        if self.ssl_ciphers is not None:
            result['SslCiphers'] = self.ssl_ciphers
        if self.ssl_protocols is not None:
            result['SslProtocols'] = self.ssl_protocols
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')
        if m.get('CcEnabled') is not None:
            self.cc_enabled = m.get('CcEnabled')
        if m.get('CcRuleEnabled') is not None:
            self.cc_rule_enabled = m.get('CcRuleEnabled')
        if m.get('CcTemplate') is not None:
            self.cc_template = m.get('CcTemplate')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertRegion') is not None:
            self.cert_region = m.get('CertRegion')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('CustomCiphers') is not None:
            self.custom_ciphers = m.get('CustomCiphers')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('GmCert') is not None:
            temp_model = DescribeWebRulesResponseBodyWebRulesGmCert()
            self.gm_cert = temp_model.from_map(m['GmCert'])
        if m.get('Http2Enable') is not None:
            self.http_2enable = m.get('Http2Enable')
        if m.get('Http2HttpsEnable') is not None:
            self.http_2https_enable = m.get('Http2HttpsEnable')
        if m.get('Https2HttpEnable') is not None:
            self.https_2http_enable = m.get('Https2HttpEnable')
        if m.get('OcspEnabled') is not None:
            self.ocsp_enabled = m.get('OcspEnabled')
        if m.get('PolicyMode') is not None:
            self.policy_mode = m.get('PolicyMode')
        if m.get('ProxyEnabled') is not None:
            self.proxy_enabled = m.get('ProxyEnabled')
        self.proxy_types = []
        if m.get('ProxyTypes') is not None:
            for k in m.get('ProxyTypes'):
                temp_model = DescribeWebRulesResponseBodyWebRulesProxyTypes()
                self.proxy_types.append(temp_model.from_map(k))
        if m.get('PunishReason') is not None:
            self.punish_reason = m.get('PunishReason')
        if m.get('PunishStatus') is not None:
            self.punish_status = m.get('PunishStatus')
        self.real_servers = []
        if m.get('RealServers') is not None:
            for k in m.get('RealServers'):
                temp_model = DescribeWebRulesResponseBodyWebRulesRealServers()
                self.real_servers.append(temp_model.from_map(k))
        if m.get('Ssl13Enabled') is not None:
            self.ssl_13enabled = m.get('Ssl13Enabled')
        if m.get('SslCiphers') is not None:
            self.ssl_ciphers = m.get('SslCiphers')
        if m.get('SslProtocols') is not None:
            self.ssl_protocols = m.get('SslProtocols')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class DescribeWebRulesResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, web_rules=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long
        self.web_rules = web_rules  # type: list[DescribeWebRulesResponseBodyWebRules]

    def validate(self):
        if self.web_rules:
            for k in self.web_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeWebRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['WebRules'] = []
        if self.web_rules is not None:
            for k in self.web_rules:
                result['WebRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.web_rules = []
        if m.get('WebRules') is not None:
            for k in m.get('WebRules'):
                temp_model = DescribeWebRulesResponseBodyWebRules()
                self.web_rules.append(temp_model.from_map(k))
        return self


class DescribeWebRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeWebRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeWebRulesResponse, self).to_map()
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
            temp_model = DescribeWebRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachSceneDefenseObjectRequest(TeaModel):
    def __init__(self, object_type=None, objects=None, policy_id=None):
        # The type of the object. Set the value to **Domain**, which indicates a domain name.
        self.object_type = object_type  # type: str
        # The protection asset that you want to remove from a policy. Separate multiple protection assets with commas (,).
        self.objects = objects  # type: str
        # The ID of the policy.
        # 
        # > You can call the [DescribeSceneDefensePolicies](~~159382~~) operation to query the IDs of all policies.
        self.policy_id = policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachSceneDefenseObjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.objects is not None:
            result['Objects'] = self.objects
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Objects') is not None:
            self.objects = m.get('Objects')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DetachSceneDefenseObjectResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachSceneDefenseObjectResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachSceneDefenseObjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachSceneDefenseObjectResponse, self).to_map()
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
            temp_model = DetachSceneDefenseObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableSceneDefensePolicyRequest(TeaModel):
    def __init__(self, policy_id=None):
        # The ID of the policy that you want to disable.
        # 
        # > You can call the [DescribeSceneDefensePolicies](~~159382~~) operation to query the IDs of all policies.
        self.policy_id = policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableSceneDefensePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class DisableSceneDefensePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableSceneDefensePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableSceneDefensePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableSceneDefensePolicyResponse, self).to_map()
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
            temp_model = DisableSceneDefensePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableWebAccessLogConfigRequest(TeaModel):
    def __init__(self, domain=None, resource_group_id=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableWebAccessLogConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DisableWebAccessLogConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableWebAccessLogConfigResponseBody, self).to_map()
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


class DisableWebAccessLogConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableWebAccessLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableWebAccessLogConfigResponse, self).to_map()
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
            temp_model = DisableWebAccessLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableWebCCRequest(TeaModel):
    def __init__(self, domain=None, resource_group_id=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for a domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableWebCCRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DisableWebCCResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableWebCCResponseBody, self).to_map()
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


class DisableWebCCResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableWebCCResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableWebCCResponse, self).to_map()
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
            temp_model = DisableWebCCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableWebCCRuleRequest(TeaModel):
    def __init__(self, domain=None, resource_group_id=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for a domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableWebCCRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DisableWebCCRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableWebCCRuleResponseBody, self).to_map()
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


class DisableWebCCRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableWebCCRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableWebCCRuleResponse, self).to_map()
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
            temp_model = DisableWebCCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EmptyAutoCcBlacklistRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EmptyAutoCcBlacklistRequest, self).to_map()
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


class EmptyAutoCcBlacklistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EmptyAutoCcBlacklistResponseBody, self).to_map()
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


class EmptyAutoCcBlacklistResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EmptyAutoCcBlacklistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EmptyAutoCcBlacklistResponse, self).to_map()
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
            temp_model = EmptyAutoCcBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EmptyAutoCcWhitelistRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EmptyAutoCcWhitelistRequest, self).to_map()
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


class EmptyAutoCcWhitelistResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EmptyAutoCcWhitelistResponseBody, self).to_map()
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


class EmptyAutoCcWhitelistResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EmptyAutoCcWhitelistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EmptyAutoCcWhitelistResponse, self).to_map()
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
            temp_model = EmptyAutoCcWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EmptySlsLogstoreRequest(TeaModel):
    def __init__(self, resource_group_id=None):
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EmptySlsLogstoreRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class EmptySlsLogstoreResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EmptySlsLogstoreResponseBody, self).to_map()
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


class EmptySlsLogstoreResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EmptySlsLogstoreResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EmptySlsLogstoreResponse, self).to_map()
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
            temp_model = EmptySlsLogstoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableSceneDefensePolicyRequest(TeaModel):
    def __init__(self, policy_id=None):
        # The ID of the policy that you want to enable.
        # 
        # > You can call the [DescribeSceneDefensePolicies](~~159382~~) operation to query the IDs of all policies.
        self.policy_id = policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableSceneDefensePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        return self


class EnableSceneDefensePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableSceneDefensePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableSceneDefensePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableSceneDefensePolicyResponse, self).to_map()
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
            temp_model = EnableSceneDefensePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableWebAccessLogConfigRequest(TeaModel):
    def __init__(self, domain=None, resource_group_id=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableWebAccessLogConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class EnableWebAccessLogConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableWebAccessLogConfigResponseBody, self).to_map()
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


class EnableWebAccessLogConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableWebAccessLogConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableWebAccessLogConfigResponse, self).to_map()
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
            temp_model = EnableWebAccessLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableWebCCRequest(TeaModel):
    def __init__(self, domain=None, resource_group_id=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableWebCCRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class EnableWebCCResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableWebCCResponseBody, self).to_map()
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


class EnableWebCCResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableWebCCResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableWebCCResponse, self).to_map()
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
            temp_model = EnableWebCCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableWebCCRuleRequest(TeaModel):
    def __init__(self, domain=None, resource_group_id=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableWebCCRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class EnableWebCCRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableWebCCRuleResponseBody, self).to_map()
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


class EnableWebCCRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableWebCCRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableWebCCRuleResponse, self).to_map()
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
            temp_model = EnableWebCCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBizBandWidthModeRequest(TeaModel):
    def __init__(self, instance_id=None, mode=None):
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # The metering method of the burstable clean bandwidth feature. Valid values:
        # 
        # *   **month**: the metering method of monthly 95th percentile
        # *   **day**: the metering method of daily 95th percentile
        self.mode = mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBizBandWidthModeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class ModifyBizBandWidthModeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBizBandWidthModeResponseBody, self).to_map()
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


class ModifyBizBandWidthModeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyBizBandWidthModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyBizBandWidthModeResponse, self).to_map()
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
            temp_model = ModifyBizBandWidthModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBlackholeStatusRequest(TeaModel):
    def __init__(self, blackhole_status=None, instance_id=None):
        # The action that you want to perform on the instance. Set the value to **undo**, which indicates that you want to deactivate blackhole filtering.
        self.blackhole_status = blackhole_status  # type: str
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBlackholeStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blackhole_status is not None:
            result['BlackholeStatus'] = self.blackhole_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlackholeStatus') is not None:
            self.blackhole_status = m.get('BlackholeStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyBlackholeStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBlackholeStatusResponseBody, self).to_map()
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


class ModifyBlackholeStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyBlackholeStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyBlackholeStatusResponse, self).to_map()
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
            temp_model = ModifyBlackholeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBlockStatusRequest(TeaModel):
    def __init__(self, duration=None, instance_id=None, lines=None, status=None):
        # The blocking period. Valid values: **15** to **43200**. Unit: minutes.
        # 
        # > If you set **Status** to **do**, you must also specify this parameter.
        self.duration = duration  # type: int
        # The ID of the Anti-DDoS Pro instance to manage.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # An array consisting of the Internet service provider (ISP) lines from which traffic is blocked.
        self.lines = lines  # type: list[str]
        # Specifies the status of the Diversion from Origin Server policy. Valid values:
        # 
        # *   **do**: enables the policy.
        # *   **undo**: disables the policy.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBlockStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lines is not None:
            result['Lines'] = self.lines
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lines') is not None:
            self.lines = m.get('Lines')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyBlockStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBlockStatusResponseBody, self).to_map()
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


class ModifyBlockStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyBlockStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyBlockStatusResponse, self).to_map()
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
            temp_model = ModifyBlockStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCnameReuseRequest(TeaModel):
    def __init__(self, cname=None, domain=None, enable=None, resource_group_id=None):
        # The CNAME record that you want to reuse for the website.
        self.cname = cname  # type: str
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # Specifies whether to enable CNAME reuse. Valid values:
        # 
        # *   **1**: enables CNAME reuse.
        # *   **2**: disables CNAME reuse.
        self.enable = enable  # type: int
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyCnameReuseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyCnameReuseResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyCnameReuseResponseBody, self).to_map()
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


class ModifyCnameReuseResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyCnameReuseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyCnameReuseResponse, self).to_map()
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
            temp_model = ModifyCnameReuseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDomainResourceRequestProxyTypes(TeaModel):
    def __init__(self, proxy_ports=None, proxy_type=None):
        # An array that consists of port numbers.
        self.proxy_ports = proxy_ports  # type: list[int]
        # The type of the protocol. Valid values:
        # 
        # *   **http**\
        # *   **https**\
        # *   **websocket**\
        # *   **websockets**\
        self.proxy_type = proxy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDomainResourceRequestProxyTypes, self).to_map()
        if _map is not None:
            return _map

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


class ModifyDomainResourceRequest(TeaModel):
    def __init__(self, domain=None, https_ext=None, instance_ids=None, proxy_types=None, real_servers=None,
                 rs_type=None):
        # The domain name that is added to the Anti-DDoS Pro or Anti-DDoS Premium instance.
        self.domain = domain  # type: str
        # The advanced HTTPS settings. This parameter takes effect only when the value of the **ProxyType** parameter includes **https**. The value is a string that consists of a JSON struct. The JSON struct contains the following fields:
        # 
        # *   **Http2https**: specifies whether to turn on Enforce HTTPS Routing. This field is optional and must be an integer. Valid values: **0** and **1**. The value 0 indicates that Enforce HTTPS Routing is turned off. The value 1 indicates that Enforce HTTPS Routing is turned on. The default value is 0.
        # 
        #     If your website supports both HTTP and HTTPS, this feature meets your business requirements. If you enable this feature, all HTTP requests to access the website are redirected to HTTPS requests on the standard port 443.
        # 
        # *   **Https2http**: specifies whether to turn on Enable HTTP. This field is optional and must be an integer. Valid values: **0** and **1**. The value 0 indicates that Enable HTTP is turned off. The value 1 indicates that Enable HTTP is turned on. The default value is 0.
        # 
        #     If your website does not support HTTPS, this feature meets your business requirements If this feature is enabled, all HTTPS requests are redirected to HTTP requests and forwarded to origin servers. This feature can redirect WebSockets requests to WebSocket requests. Requests are redirected over the standard port 80.
        # 
        # *   **Http2**: specifies whether to turn on Enable HTTP/2. This field is optional. Data type: integer. Valid values: **0** and **1**. The value 0 indicates that Enable HTTP/2 is turned off. The value 1 indicates that Enable HTTP/2 is turned on. The default value is 0.
        # 
        #     After you turn on the switch, HTTP/2 is used.
        self.https_ext = https_ext  # type: str
        # An array consisting of the IDs of instances that you want to associate.
        self.instance_ids = instance_ids  # type: list[str]
        # An array that consists of the details of the protocol type and port number.
        self.proxy_types = proxy_types  # type: list[ModifyDomainResourceRequestProxyTypes]
        # An array that consists of the addresses of origin servers.
        self.real_servers = real_servers  # type: list[str]
        # The address type of the origin server. Valid values:
        # 
        # *   **0**: IP address
        # 
        # *   **1**: domain name
        # 
        #     If you deploy proxies, such as a Web Application Firewall (WAF) instance, between the origin server and the Anti-DDoS Pro or Anti-DDoS Premium instance, set the value to 1. If you use the domain name, you must enter the address of the proxy, such as the CNAME of WAF.
        self.rs_type = rs_type  # type: int

    def validate(self):
        if self.proxy_types:
            for k in self.proxy_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyDomainResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.https_ext is not None:
            result['HttpsExt'] = self.https_ext
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        result['ProxyTypes'] = []
        if self.proxy_types is not None:
            for k in self.proxy_types:
                result['ProxyTypes'].append(k.to_map() if k else None)
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('HttpsExt') is not None:
            self.https_ext = m.get('HttpsExt')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        self.proxy_types = []
        if m.get('ProxyTypes') is not None:
            for k in m.get('ProxyTypes'):
                temp_model = ModifyDomainResourceRequestProxyTypes()
                self.proxy_types.append(temp_model.from_map(k))
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        return self


class ModifyDomainResourceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDomainResourceResponseBody, self).to_map()
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


class ModifyDomainResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDomainResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDomainResourceResponse, self).to_map()
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
            temp_model = ModifyDomainResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyElasticBandWidthRequest(TeaModel):
    def __init__(self, elastic_bandwidth=None, instance_id=None):
        # The new burstable protection bandwidth that you want to use. Unit: Gbit/s.
        # 
        # > You can call the [DescribeElasticBandwidthSpec](~~91502~~) operation to query the available burstable protection bandwidth of the instance.
        self.elastic_bandwidth = elastic_bandwidth  # type: int
        # The ID of the instance.
        # 
        # >  The instance must be in a normal state. You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyElasticBandWidthRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyElasticBandWidthResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyElasticBandWidthResponseBody, self).to_map()
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


class ModifyElasticBandWidthResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyElasticBandWidthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyElasticBandWidthResponse, self).to_map()
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
            temp_model = ModifyElasticBandWidthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyElasticBizBandWidthRequest(TeaModel):
    def __init__(self, elastic_biz_bandwidth=None, instance_id=None, mode=None):
        # The burstable clean bandwidth. Unit: Mbit/s. The burstable clean bandwidth cannot exceed nine times the clean bandwidth of your Anti-DDoS Pro or Anti-DDoS Premium instance, and the sum of the clean bandwidth and the burstable clean bandwidth cannot exceed the maximum clean bandwidth that is supported by your instance. The value 0 indicates that the burstable clean bandwidth feature is disabled. You can disable the burstable clean bandwidth feature once a month.
        self.elastic_biz_bandwidth = elastic_biz_bandwidth  # type: int
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # The metering method of the burstable clean bandwidth feature. Valid values:
        # 
        # *   **month**: the metering method of monthly 95th percentile
        # *   **day**: the metering method of daily 95th percentile
        self.mode = mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyElasticBizBandWidthRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_biz_bandwidth is not None:
            result['ElasticBizBandwidth'] = self.elastic_biz_bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ElasticBizBandwidth') is not None:
            self.elastic_biz_bandwidth = m.get('ElasticBizBandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class ModifyElasticBizBandWidthResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyElasticBizBandWidthResponseBody, self).to_map()
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


class ModifyElasticBizBandWidthResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyElasticBizBandWidthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyElasticBizBandWidthResponse, self).to_map()
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
            temp_model = ModifyElasticBizBandWidthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFullLogTtlRequest(TeaModel):
    def __init__(self, resource_group_id=None, ttl=None):
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The log storage duration of a website. Valid values: **30** to **180**. Unit: days.
        self.ttl = ttl  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFullLogTtlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class ModifyFullLogTtlResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFullLogTtlResponseBody, self).to_map()
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


class ModifyFullLogTtlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyFullLogTtlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFullLogTtlResponse, self).to_map()
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
            temp_model = ModifyFullLogTtlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHeadersRequest(TeaModel):
    def __init__(self, custom_headers=None, domain=None, resource_group_id=None):
        # The key-value pair of the custom header. Key indicates the header name and Value indicates the header value. You can specify up to five key-value pairs. The key-value pairs can be up to 200 characters in length.
        # 
        # Take note of the following items:
        # 
        # *   Do not use X-Forwarded-ClientSrcPort as a custom header.
        # *   Do not use a standard HTTP header such as User-Agent. If you use a standard HTTP header, the original header may be overwritten.
        # 
        # > If you set Key to X-Forwarded-ClientSrcPort, the actual source port of the client that accesses Anti-DDoS Pro or Anti-DDoS Premium (a Layer 7 proxy) is obtained. In this case, the Value is "".
        self.custom_headers = custom_headers  # type: str
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs.
        # 
        # > 
        # 
        # *   You can query resource group IDs in the Anti-DDoS Pro or Anti-DDoS Premium console or by calling the [ListResourceGroups](~~158855~~) operation. For more information, see [View basic information of a resource group](~~151181~~).
        # 
        # *   Before you modify the resource group to which an instance belongs, you can call the [ListResources](~~158866~~) operation to view the current resource group of the instance.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHeadersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_headers is not None:
            result['CustomHeaders'] = self.custom_headers
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomHeaders') is not None:
            self.custom_headers = m.get('CustomHeaders')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyHeadersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The unique ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHeadersResponseBody, self).to_map()
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


class ModifyHeadersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyHeadersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyHeadersResponse, self).to_map()
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
            temp_model = ModifyHeadersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHealthCheckConfigRequest(TeaModel):
    def __init__(self, forward_protocol=None, frontend_port=None, health_check=None, instance_id=None):
        # The forwarding protocol. Valid values:
        # 
        # *   **tcp**\
        # *   **udp**\
        self.forward_protocol = forward_protocol  # type: str
        # The forwarding port.
        self.frontend_port = frontend_port  # type: int
        # The details of the health check configuration. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **Type**: the protocol type. This field is required and must be of the STRING type. Valid values: **tcp** (Layer 4) and **http** (Layer 7).
        # 
        # *   **Domain**: the domain name, which must be of the STRING type.
        # 
        #     **\
        # 
        #     **Note**This parameter is returned only when the Layer 7 health check configuration is queried.
        # 
        # *   **Uri**: the check path, which must be of the STRING type.
        # 
        #     **\
        # 
        #     **Note**This parameter is returned only when the Layer 7 health check configuration is queried.
        # 
        # *   **Timeout**: the response timeout period, which must be of the INTEGER type. Valid values: **1** to **30**. Unit: seconds.
        # 
        # *   **Port**: the port on which you want to perform the health check, which must be of the INTEGER type.
        # 
        # *   **Interval**: the health check interval, which must be of the INTEGER type. Valid values: **1** to **30**. Unit: seconds.
        # 
        # *   **Up**: the number of consecutive successful health checks that must occur before declaring a port healthy, which must be of the INTEGER type. Valid values: **1** to **10**.
        # 
        # *   **Down**: the number of consecutive failed health checks that must occur before declaring a port unhealthy, which must be of the INTEGER type. Valid values: **1** to **10**.
        self.health_check = health_check  # type: str
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHealthCheckConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyHealthCheckConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHealthCheckConfigResponseBody, self).to_map()
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


class ModifyHealthCheckConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyHealthCheckConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyHealthCheckConfigResponse, self).to_map()
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
            temp_model = ModifyHealthCheckConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHttp2EnableRequest(TeaModel):
    def __init__(self, domain=None, enable=None, resource_group_id=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name, and the domain name must be associated with an instance that uses the Enhanced function plan. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # Specifies whether to enable HTTP/2. Valid values:
        # 
        # *   **0**: disables HTTP/2.
        # *   **1**: enables HTTP/2.
        self.enable = enable  # type: int
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHttp2EnableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyHttp2EnableResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHttp2EnableResponseBody, self).to_map()
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


class ModifyHttp2EnableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyHttp2EnableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyHttp2EnableResponse, self).to_map()
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
            temp_model = ModifyHttp2EnableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceRemarkRequest(TeaModel):
    def __init__(self, instance_id=None, remark=None):
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # The description of the instance.
        # 
        # The value can contain letters, digits, and some special characters, such as`, . + - * / _` The value can be up to 500 characters in length.
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceRemarkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ModifyInstanceRemarkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceRemarkResponseBody, self).to_map()
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


class ModifyInstanceRemarkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceRemarkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceRemarkResponse, self).to_map()
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
            temp_model = ModifyInstanceRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNetworkRuleAttributeRequest(TeaModel):
    def __init__(self, config=None, forward_protocol=None, frontend_port=None, instance_id=None):
        # The session persistence settings of the port forwarding rule. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **PersistenceTimeout**: The timeout period of session persistence. This field is required and must be of the integer type. Valid values: **30** to **3600**. Unit: seconds. Default value: **0**. A value of 0 indicates that session persistence is disabled.
        self.config = config  # type: str
        # The forwarding protocol. Valid values:
        # 
        # *   **tcp**\
        # *   **udp**\
        self.forward_protocol = forward_protocol  # type: str
        # The forwarding port.
        self.frontend_port = frontend_port  # type: int
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNetworkRuleAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyNetworkRuleAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNetworkRuleAttributeResponseBody, self).to_map()
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


class ModifyNetworkRuleAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyNetworkRuleAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyNetworkRuleAttributeResponse, self).to_map()
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
            temp_model = ModifyNetworkRuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOcspStatusRequest(TeaModel):
    def __init__(self, domain=None, enable=None):
        # The domain name for which you want to configure the Static Page Caching policy.
        # 
        # > You can call the [DescribeDomains](~~91724~~) operation to query all the domain names that are added to Anti-DDoS Pro or Anti-DDoS Premium.
        self.domain = domain  # type: str
        # Specifies whether to enable the OCSP feature. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable = enable  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyOcspStatusRequest, self).to_map()
        if _map is not None:
            return _map

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


class ModifyOcspStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyOcspStatusResponseBody, self).to_map()
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


class ModifyOcspStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyOcspStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyOcspStatusResponse, self).to_map()
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
            temp_model = ModifyOcspStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPortRequest(TeaModel):
    def __init__(self, backend_port=None, frontend_port=None, frontend_protocol=None, instance_id=None,
                 real_servers=None):
        # The port of the origin server. Valid values: **0** to **65535**.
        self.backend_port = backend_port  # type: str
        # The forwarding port. Valid values: **0** to **65535**.
        self.frontend_port = frontend_port  # type: str
        # The type of the protocol. Valid values:
        # 
        # *   **tcp**\
        # *   **udp**\
        self.frontend_protocol = frontend_protocol  # type: str
        # The ID of the Anti-DDoS Pro or Anti-DDoS Premium instance to which the port forwarding rule belongs.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # An array that consists of the IP addresses of origin servers.
        self.real_servers = real_servers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPortRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_port is not None:
            result['BackendPort'] = self.backend_port
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.frontend_protocol is not None:
            result['FrontendProtocol'] = self.frontend_protocol
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackendPort') is not None:
            self.backend_port = m.get('BackendPort')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('FrontendProtocol') is not None:
            self.frontend_protocol = m.get('FrontendProtocol')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        return self


class ModifyPortResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPortResponseBody, self).to_map()
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


class ModifyPortResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyPortResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPortResponse, self).to_map()
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
            temp_model = ModifyPortResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPortAutoCcStatusRequest(TeaModel):
    def __init__(self, instance_id=None, mode=None, switch=None):
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](~~157459~~) operation to query the IDs of all instances.
        self.instance_id = instance_id  # type: str
        # The mode of the Intelligent Protection policy. Valid values:
        # 
        # *   **normal**\
        # *   **loose**\
        # *   **strict**\
        self.mode = mode  # type: str
        # Specifies the status of the Intelligent Protection policy. Valid values:
        # 
        # *   **on**: enables the policy.
        # *   **off**: disables the policy.
        self.switch = switch  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPortAutoCcStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.switch is not None:
            result['Switch'] = self.switch
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Switch') is not None:
            self.switch = m.get('Switch')
        return self


class ModifyPortAutoCcStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPortAutoCcStatusResponseBody, self).to_map()
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


class ModifyPortAutoCcStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyPortAutoCcStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPortAutoCcStatusResponse, self).to_map()
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
            temp_model = ModifyPortAutoCcStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySceneDefensePolicyRequest(TeaModel):
    def __init__(self, end_time=None, name=None, policy_id=None, start_time=None, template=None):
        # The end time of the policy. The value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time  # type: long
        # The name of the policy.
        self.name = name  # type: str
        # The ID of the policy that you want to modify.
        # 
        # > You can call the [DescribeSceneDefensePolicies](~~159382~~) operation to query the IDs of all policies.
        self.policy_id = policy_id  # type: str
        # The start time of the policy. The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time  # type: long
        # The template of the policy. Valid values:
        # 
        # *   **promotion**: important activity
        # *   **bypass**: all traffic forwarded
        self.template = template  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySceneDefensePolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class ModifySceneDefensePolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySceneDefensePolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifySceneDefensePolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySceneDefensePolicyResponse, self).to_map()
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
            temp_model = ModifySceneDefensePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySchedulerRuleRequest(TeaModel):
    def __init__(self, param=None, resource_group_id=None, rule_name=None, rule_type=None, rules=None):
        # The details of the CDN interaction rule. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **ParamType**: the type of the scheduling rule. This field is required and must be of the string type. Set the value to **cdn**. This indicates that you want to modify a CDN interaction rule.
        # 
        # *   **ParamData**: the values of parameters that you want to modify for the CDN interaction rule. This field is required and must be of the map type. The ParamData parameter contains the following parameters:
        # 
        #     *   **Domain**: the accelerated domain in CDN. This parameter is required and must be of the string type.
        #     *   **Cname**: the CNAME that is assigned to the accelerated domain. This parameter is required and must be of the string type.
        #     *   **AccessQps**: the queries per second (QPS) threshold that is used to switch service traffic to Anti-DDoS Pro or Anti-DDoS Premium. This parameter is required and must be of the integer type.
        #     *   **UpstreamQps**: the QPS threshold that is used to switch service traffic to CDN. This parameter is optional and must be of the integer type.
        self.param = param  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The name of the rule that you want to modify.
        self.rule_name = rule_name  # type: str
        # The type of the rule. Valid values:
        # 
        # *   **2**: tiered protection
        # *   **3**: network acceleration
        # *   **5**: Alibaba Cloud CDN (CDN) interaction
        # *   **6**: cloud service interaction
        self.rule_type = rule_type  # type: int
        # The details of the scheduling rule. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **Type**: the address type of the interaction resource that you want to use in the scheduling rule. This field is required and must be of the string type. Valid values:
        # 
        #     *   **A**: IP address
        #     *   **CNAME**: domain name
        # 
        # *   **Value**: the address of the interaction resource that you want to use in the scheduling rule. This field is required and must be of the string type.
        # 
        # *   **Priority**: the priority of the scheduling rule. This field is required and must be of the integer type. Valid values: **0** to **100**. A larger value indicates a higher priority.
        # 
        # *   **ValueType**: the type of the interaction resource that you want to use in the scheduling rule. This field is required and must be of the integer type. Valid values:
        # 
        #     *   **1**: the IP address of the Anti-DDoS Pro or Anti-DDoS Premium instance
        #     *   **2**: the IP address of the interaction resource in the tiered protection scenario
        #     *   **3**: the IP address that is used to accelerate access in the network acceleration scenario
        #     *   **5**: the domain name that is configured in Alibaba Cloud CDN (CDN) in the CDN interaction scenario
        #     *   **6** the IP address of the interaction resource in the cloud service interaction scenario
        # 
        # *   **RegionId**: the region where the interaction resource is deployed. This parameter must be specified when **ValueType** is set to **2**. The value must be of the string type.
        self.rules = rules  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySchedulerRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param is not None:
            result['Param'] = self.param
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.rules is not None:
            result['Rules'] = self.rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        return self


class ModifySchedulerRuleResponseBody(TeaModel):
    def __init__(self, cname=None, request_id=None, rule_name=None):
        # The CNAME that is assigned by Sec-Traffic Manager for the scheduling rule.
        # 
        # > To enable the scheduling rule, you must map the domain name of the service to the CNAME.
        self.cname = cname  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The name of the rule.
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySchedulerRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ModifySchedulerRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifySchedulerRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySchedulerRuleResponse, self).to_map()
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
            temp_model = ModifySchedulerRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTlsConfigRequest(TeaModel):
    def __init__(self, config=None, domain=None, resource_group_id=None):
        # The details of the TLS policy. The value is a JSON string that contains the following fields:
        # 
        # *   **ssl_protocols**: the version of TLS. This field is required. Data type: string. Valid values:
        # 
        #     *   **tls1.0**: TLS 1.0 and later
        #     *   **tls1.1**: TLS 1.1 and later
        #     *   **tls1.2**: TLS 1.2 and later
        # 
        # *   **ssl_ciphers**: the type of the cipher suite. This field is required. Data type: string. Valid values:
        # 
        #     *   **all**: all cipher suites, which include strong and weak cipher suites
        #     *   **improved**: enhanced cipher suites
        #     *   **strong**: strong cipher suites
        #     *   **default**: default cipher suites, which include only strong cipher suites
        self.config = config  # type: str
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTlsConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyTlsConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTlsConfigResponseBody, self).to_map()
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


class ModifyTlsConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyTlsConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTlsConfigResponse, self).to_map()
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
            temp_model = ModifyTlsConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebAIProtectModeRequest(TeaModel):
    def __init__(self, config=None, domain=None, resource_group_id=None):
        # The details of the Intelligent Protection policy. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **AiTemplate**: the level of the Intelligent Protection policy. This field is required and must be of the STRING type. Valid values:
        # 
        #     *   **level30**: the Low level
        #     *   **level60**: the Normal level
        #     *   **level90**: the Strict level
        # 
        # *   **AiMode**: the mode of the Intelligent Protection policy. This field is required and must be of the string type. Valid values:
        # 
        #     *   **watch**: the Warning mode
        #     *   **defense**: the Defense mode
        self.config = config  # type: str
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for a domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebAIProtectModeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyWebAIProtectModeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebAIProtectModeResponseBody, self).to_map()
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


class ModifyWebAIProtectModeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyWebAIProtectModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyWebAIProtectModeResponse, self).to_map()
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
            temp_model = ModifyWebAIProtectModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebAIProtectSwitchRequest(TeaModel):
    def __init__(self, config=None, domain=None, resource_group_id=None):
        # The details of the Intelligent Protection policy. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **AiRuleEnable**: the status of the Intelligent Protection policy. This field is required and must be of the integer type. Valid values:
        # 
        #     *   **0**: disabled
        #     *   **1**: enabled
        self.config = config  # type: str
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for a domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebAIProtectSwitchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyWebAIProtectSwitchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebAIProtectSwitchResponseBody, self).to_map()
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


class ModifyWebAIProtectSwitchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyWebAIProtectSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyWebAIProtectSwitchResponse, self).to_map()
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
            temp_model = ModifyWebAIProtectSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebAccessModeRequest(TeaModel):
    def __init__(self, access_mode=None, domain=None):
        # The mode in which a website service is added to Anti-DDoS Pro or Anti-DDoS Premium. Valid values:
        # 
        # *   **0**: A record mode
        # *   **1**: anti-DDoS mode
        # *   **2**: origin redundancy mode
        self.access_mode = access_mode  # type: int
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebAccessModeRequest, self).to_map()
        if _map is not None:
            return _map

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


class ModifyWebAccessModeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebAccessModeResponseBody, self).to_map()
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


class ModifyWebAccessModeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyWebAccessModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyWebAccessModeResponse, self).to_map()
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
            temp_model = ModifyWebAccessModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebAreaBlockRequest(TeaModel):
    def __init__(self, domain=None, regions=None, resource_group_id=None):
        # The domain name whose configurations you want to modify.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The regions from which you block requests.
        # 
        # > If you do not configure this parameter, the Blocked Regions (Domain Names) policy is disabled.
        self.regions = regions  # type: list[str]
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](~~94485~~).
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebAreaBlockRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.regions is not None:
            result['Regions'] = self.regions
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyWebAreaBlockResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebAreaBlockResponseBody, self).to_map()
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


class ModifyWebAreaBlockResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyWebAreaBlockResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyWebAreaBlockResponse, self).to_map()
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
            temp_model = ModifyWebAreaBlockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebAreaBlockSwitchRequest(TeaModel):
    def __init__(self, config=None, domain=None, resource_group_id=None):
        # Specifies whether to enable or disable the Location Blacklist (Domain Names) policy for a domain name. The value is a string that consists of a JSON struct. The JSON struct contains the following parameters:
        # 
        # *   **RegionblockEnable**: the status of the Location Blacklist (Domain Names) policy. This parameter is required and must be of the INTEGER type. Valid values:
        # 
        #     *   **1**: enables the policy.
        #     *   **0**: disables the policy.
        self.config = config  # type: str
        # The domain name for which you want to enable or disable the Location Blacklist policy.
        # 
        # > You can call the [DescribeDomains](~~91724~~) operation to query all the domain names that are added to Anti-DDoS Pro or Anti-DDoS Premium.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebAreaBlockSwitchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyWebAreaBlockSwitchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebAreaBlockSwitchResponseBody, self).to_map()
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


class ModifyWebAreaBlockSwitchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyWebAreaBlockSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyWebAreaBlockSwitchResponse, self).to_map()
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
            temp_model = ModifyWebAreaBlockSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebCCRuleRequest(TeaModel):
    def __init__(self, act=None, count=None, domain=None, interval=None, mode=None, name=None, resource_group_id=None,
                 ttl=None, uri=None):
        self.act = act  # type: str
        self.count = count  # type: int
        self.domain = domain  # type: str
        self.interval = interval  # type: int
        self.mode = mode  # type: str
        self.name = name  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.ttl = ttl  # type: int
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebCCRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.act is not None:
            result['Act'] = self.act
        if self.count is not None:
            result['Count'] = self.count
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class ModifyWebCCRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebCCRuleResponseBody, self).to_map()
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


class ModifyWebCCRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyWebCCRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyWebCCRuleResponse, self).to_map()
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
            temp_model = ModifyWebCCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebCacheCustomRuleRequest(TeaModel):
    def __init__(self, domain=None, resource_group_id=None, rules=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name, and the domain name must be associated with an instance that uses the Enhanced function plan. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The details of the custom rule. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **Name**: the name of the rule. This field is required and must be of the string type.
        # 
        # *   **Uri**: the path to the cached page. This field is required and must be of the STRING type.
        # 
        # *   **Mode**: the cache mode. This field is required and must be of the STRING type. Valid values:
        # 
        #     *   **standard**: uses the standard mode.
        #     *   **aggressive**: uses the enhanced mode.
        #     *   **bypass**: No data is cached.
        # 
        # *   **CacheTtl**: the expiration time of the page cache. This field is required and must be of the INTEGER type. Unit: seconds.
        self.rules = rules  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebCacheCustomRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rules is not None:
            result['Rules'] = self.rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        return self


class ModifyWebCacheCustomRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebCacheCustomRuleResponseBody, self).to_map()
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


class ModifyWebCacheCustomRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyWebCacheCustomRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyWebCacheCustomRuleResponse, self).to_map()
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
            temp_model = ModifyWebCacheCustomRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebCacheModeRequest(TeaModel):
    def __init__(self, domain=None, mode=None, resource_group_id=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name, and the domain name must be associated with an instance that uses the Enhanced function plan. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The cache mode of the Static Page Caching policy. Valid values:
        # 
        # *   **standard**: uses the standard cache mode.
        # *   **aggressive**: uses the enhanced cache mode.
        # *   **bypass**: caches no data.
        self.mode = mode  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebCacheModeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyWebCacheModeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebCacheModeResponseBody, self).to_map()
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


class ModifyWebCacheModeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyWebCacheModeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyWebCacheModeResponse, self).to_map()
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
            temp_model = ModifyWebCacheModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebCacheSwitchRequest(TeaModel):
    def __init__(self, domain=None, enable=None, resource_group_id=None):
        # The domain name for which you want to configure the Static Page Caching policy.
        # 
        # > You can call the [DescribeDomains](~~91724~~) operation to query all the domain names that are added to Anti-DDoS Pro or Anti-DDoS Premium.
        self.domain = domain  # type: str
        # Specifies whether to enable or disable the Static Page Caching policy for a website. Valid values:
        # 
        # *   **1**: enables the policy.
        # *   **0**: disables the policy.
        self.enable = enable  # type: int
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebCacheSwitchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyWebCacheSwitchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebCacheSwitchResponseBody, self).to_map()
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


class ModifyWebCacheSwitchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyWebCacheSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyWebCacheSwitchResponse, self).to_map()
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
            temp_model = ModifyWebCacheSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebIpSetSwitchRequest(TeaModel):
    def __init__(self, config=None, domain=None, resource_group_id=None):
        # The details of the Black Lists and White Lists (Domain Names) policy. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **Bwlist_Enable**: the status of the Black Lists and White Lists (Domain Names) policy. This field is required and must be of the integer type. Valid values:
        # 
        #     *   **0**: disabled
        #     *   **1**: enabled
        self.config = config  # type: str
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebIpSetSwitchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyWebIpSetSwitchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebIpSetSwitchResponseBody, self).to_map()
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


class ModifyWebIpSetSwitchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyWebIpSetSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyWebIpSetSwitchResponse, self).to_map()
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
            temp_model = ModifyWebIpSetSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebPreciseAccessRuleRequest(TeaModel):
    def __init__(self, domain=None, expires=None, resource_group_id=None, rules=None):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The validity period of the rule. Unit: seconds. This parameter takes effect only when **action** of a rule is **block**. Access requests that match the rule are blocked within the specified validity period of the rule. If you do not specify this parameter, this rule takes effect all the time.
        self.expires = expires  # type: int
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The settings of the accurate access control rule. This parameter is a JSON string. The following list describes the fields in the value of the parameter:
        # 
        # *   **action**: the action that is performed if the rule is matched. This field is required and must be of the string type. Valid values:
        # 
        #     *   **accept**: allows the requests that match the rule.
        #     *   **block**: blocks the requests that match the rule.
        #     *   **challenge**: implements a CAPTCHA for the requests that match the rule.
        # 
        # *   **name**: the name of the rule. This field is required and must be of the string type.
        # 
        # *   **condition**: the match conditions. This field is required and must be of the map type. A match condition contains the following parameters.
        # 
        #     **\
        # 
        #     **Note**The AND logical operator is used to define the relationship among multiple match conditions.
        # 
        #     *   **field**: the match field. This parameter is required and must be of the string type.
        # 
        #     *   **match_method**: the logical relation. This parameter is required and must be of the string type.
        # 
        #         **\
        # 
        #         **Note**For information about the mappings between the **field** and **match_method** parameters, see the Mappings between the field and match_method parameters table in this topic.
        # 
        #     *   **content**: the match content. This parameter is required and must be of the string type.
        # 
        # *   **header_name**: the HTTP header. This parameter is optional and must be of the string type. This parameter takes effect only when **field** is **header**.
        self.rules = rules  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebPreciseAccessRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.expires is not None:
            result['Expires'] = self.expires
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rules is not None:
            result['Rules'] = self.rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Expires') is not None:
            self.expires = m.get('Expires')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        return self


class ModifyWebPreciseAccessRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebPreciseAccessRuleResponseBody, self).to_map()
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


class ModifyWebPreciseAccessRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyWebPreciseAccessRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyWebPreciseAccessRuleResponse, self).to_map()
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
            temp_model = ModifyWebPreciseAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebPreciseAccessSwitchRequest(TeaModel):
    def __init__(self, config=None, domain=None, resource_group_id=None):
        # The configuration of the Accurate Access Control policy. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **PreciseRuleEnable**: the status of the Accurate Access Control policy. This field is required and must be of the INTEGER type. Valid values:
        # 
        #     *   **0**: disables the policy.
        #     *   **1**: enables the policy.
        self.config = config  # type: str
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for a domain name. You can call the [DescribeDomains](~~91724~~) operation to query all domain names.
        self.domain = domain  # type: str
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebPreciseAccessSwitchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyWebPreciseAccessSwitchResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebPreciseAccessSwitchResponseBody, self).to_map()
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


class ModifyWebPreciseAccessSwitchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyWebPreciseAccessSwitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyWebPreciseAccessSwitchResponse, self).to_map()
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
            temp_model = ModifyWebPreciseAccessSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebRuleRequest(TeaModel):
    def __init__(self, domain=None, https_ext=None, instance_ids=None, proxy_types=None, real_servers=None,
                 resource_group_id=None, rs_type=None):
        self.domain = domain  # type: str
        self.https_ext = https_ext  # type: str
        self.instance_ids = instance_ids  # type: list[str]
        self.proxy_types = proxy_types  # type: str
        self.real_servers = real_servers  # type: list[str]
        self.resource_group_id = resource_group_id  # type: str
        self.rs_type = rs_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.https_ext is not None:
            result['HttpsExt'] = self.https_ext
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.proxy_types is not None:
            result['ProxyTypes'] = self.proxy_types
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('HttpsExt') is not None:
            self.https_ext = m.get('HttpsExt')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('ProxyTypes') is not None:
            self.proxy_types = m.get('ProxyTypes')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        return self


class ModifyWebRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyWebRuleResponseBody, self).to_map()
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


class ModifyWebRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyWebRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyWebRuleResponse, self).to_map()
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
            temp_model = ModifyWebRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstanceRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseInstanceRequest, self).to_map()
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


class ReleaseInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseInstanceResponseBody, self).to_map()
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


class ReleaseInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleaseInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseInstanceResponse, self).to_map()
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
            temp_model = ReleaseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchSchedulerRuleRequest(TeaModel):
    def __init__(self, rule_name=None, rule_type=None, switch_data=None):
        # The name of the scheduling rule to manage.
        # 
        # > You can call the [DescribeSchedulerRules](~~157481~~) operation to query the names of all scheduling rules.
        self.rule_name = rule_name  # type: str
        # The type of the scheduling rule. Valid values:
        # 
        # *   **2**: tiered protection rule
        # *   **3**: network acceleration rule
        # *   **5**: Alibaba Cloud CDN (CDN) interaction rule
        # *   **6**: cloud service interaction rule
        self.rule_type = rule_type  # type: int
        # The configuration that is used to switch service traffic. This parameter is a string that consists of JSON arrays. Each element in a JSON array is a JSON struct that includes the following parameters:
        # 
        # *   **Value**: required. The IP address of the associated resource. Data type: string.
        # 
        # *   **State**: required. The operation type. Data type: integer. Valid values:
        # 
        #     *   **0**: switches service traffic from the associated resource to your Anti-DDoS Pro or Anti-DDoS Premium instance for scrubbing.
        #     *   **1**: switches service traffic back to the associated cloud resource.
        # 
        # *   **Interval**: optional. The waiting time that is required before the service traffic is switched back. Unit: minutes. Data type: integer. Usage notes:
        # 
        #     *   If the **State** parameter is set to **0**, you must set this parameter to \*\*-1\*\*. Otherwise, the call fails.
        #     *   If the **State** parameter is set to **1**, you do not need to set this parameter.
        self.switch_data = switch_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchSchedulerRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.switch_data is not None:
            result['SwitchData'] = self.switch_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('SwitchData') is not None:
            self.switch_data = m.get('SwitchData')
        return self


class SwitchSchedulerRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SwitchSchedulerRuleResponseBody, self).to_map()
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


class SwitchSchedulerRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SwitchSchedulerRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SwitchSchedulerRuleResponse, self).to_map()
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
            temp_model = SwitchSchedulerRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


