# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddUserToDesktopGroupRequest(TeaModel):
    def __init__(self, region_id=None, desktop_group_id=None, client_token=None, end_user_ids=None):
        self.region_id = region_id  # type: str
        self.desktop_group_id = desktop_group_id  # type: str
        self.client_token = client_token  # type: str
        self.end_user_ids = end_user_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserToDesktopGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        return self


class AddUserToDesktopGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserToDesktopGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddUserToDesktopGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddUserToDesktopGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddUserToDesktopGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddUserToDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserToSecurityCenterWhiteListRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserToSecurityCenterWhiteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddUserToSecurityCenterWhiteListResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserToSecurityCenterWhiteListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddUserToSecurityCenterWhiteListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddUserToSecurityCenterWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddUserToSecurityCenterWhiteListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddUserToSecurityCenterWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachCenRequest(TeaModel):
    def __init__(self, region_id=None, cen_id=None, office_site_id=None):
        self.region_id = region_id  # type: str
        self.cen_id = cen_id  # type: str
        self.office_site_id = office_site_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachCenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class AttachCenResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachCenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachCenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AttachCenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachCenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckUserInSecurityCenterWhiteListRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckUserInSecurityCenterWhiteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CheckUserInSecurityCenterWhiteListResponseBody(TeaModel):
    def __init__(self, in_white_list=None, request_id=None):
        self.in_white_list = in_white_list  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckUserInSecurityCenterWhiteListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_white_list is not None:
            result['InWhiteList'] = self.in_white_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InWhiteList') is not None:
            self.in_white_list = m.get('InWhiteList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckUserInSecurityCenterWhiteListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckUserInSecurityCenterWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckUserInSecurityCenterWhiteListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckUserInSecurityCenterWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClonePolicyGroupRequest(TeaModel):
    def __init__(self, region_id=None, policy_group_id=None, name=None):
        self.region_id = region_id  # type: str
        self.policy_group_id = policy_group_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClonePolicyGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ClonePolicyGroupResponseBody(TeaModel):
    def __init__(self, policy_group_id=None, request_id=None):
        self.policy_group_id = policy_group_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClonePolicyGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ClonePolicyGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ClonePolicyGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ClonePolicyGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ClonePolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateADConnectorDirectoryRequest(TeaModel):
    def __init__(self, region_id=None, domain_name=None, domain_user_name=None, domain_password=None,
                 directory_name=None, enable_admin_access=None, desktop_access_type=None, sub_domain_name=None, mfa_enabled=None,
                 dns_address=None, v_switch_id=None, sub_domain_dns_address=None):
        self.region_id = region_id  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_user_name = domain_user_name  # type: str
        self.domain_password = domain_password  # type: str
        self.directory_name = directory_name  # type: str
        self.enable_admin_access = enable_admin_access  # type: bool
        self.desktop_access_type = desktop_access_type  # type: str
        self.sub_domain_name = sub_domain_name  # type: str
        self.mfa_enabled = mfa_enabled  # type: bool
        self.dns_address = dns_address  # type: list[str]
        self.v_switch_id = v_switch_id  # type: list[str]
        self.sub_domain_dns_address = sub_domain_dns_address  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateADConnectorDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.sub_domain_dns_address is not None:
            result['SubDomainDnsAddress'] = self.sub_domain_dns_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('SubDomainDnsAddress') is not None:
            self.sub_domain_dns_address = m.get('SubDomainDnsAddress')
        return self


class CreateADConnectorDirectoryResponseBodyAdConnectors(TeaModel):
    def __init__(self, address=None):
        self.address = address  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateADConnectorDirectoryResponseBodyAdConnectors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        return self


class CreateADConnectorDirectoryResponseBody(TeaModel):
    def __init__(self, trust_password=None, request_id=None, directory_id=None, ad_connectors=None):
        self.trust_password = trust_password  # type: str
        self.request_id = request_id  # type: str
        self.directory_id = directory_id  # type: str
        self.ad_connectors = ad_connectors  # type: list[CreateADConnectorDirectoryResponseBodyAdConnectors]

    def validate(self):
        if self.ad_connectors:
            for k in self.ad_connectors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateADConnectorDirectoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trust_password is not None:
            result['TrustPassword'] = self.trust_password
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        result['AdConnectors'] = []
        if self.ad_connectors is not None:
            for k in self.ad_connectors:
                result['AdConnectors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TrustPassword') is not None:
            self.trust_password = m.get('TrustPassword')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        self.ad_connectors = []
        if m.get('AdConnectors') is not None:
            for k in m.get('AdConnectors'):
                temp_model = CreateADConnectorDirectoryResponseBodyAdConnectors()
                self.ad_connectors.append(temp_model.from_map(k))
        return self


class CreateADConnectorDirectoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateADConnectorDirectoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateADConnectorDirectoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateADConnectorDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateADConnectorOfficeSiteRequest(TeaModel):
    def __init__(self, region_id=None, cidr_block=None, cen_id=None, bandwidth=None, domain_name=None,
                 domain_user_name=None, domain_password=None, office_site_name=None, enable_admin_access=None,
                 desktop_access_type=None, enable_internet_access=None, sub_domain_name=None, mfa_enabled=None, dns_address=None,
                 sub_domain_dns_address=None):
        self.region_id = region_id  # type: str
        self.cidr_block = cidr_block  # type: str
        self.cen_id = cen_id  # type: str
        self.bandwidth = bandwidth  # type: int
        self.domain_name = domain_name  # type: str
        self.domain_user_name = domain_user_name  # type: str
        self.domain_password = domain_password  # type: str
        self.office_site_name = office_site_name  # type: str
        self.enable_admin_access = enable_admin_access  # type: bool
        self.desktop_access_type = desktop_access_type  # type: str
        self.enable_internet_access = enable_internet_access  # type: bool
        self.sub_domain_name = sub_domain_name  # type: str
        self.mfa_enabled = mfa_enabled  # type: bool
        self.dns_address = dns_address  # type: list[str]
        self.sub_domain_dns_address = sub_domain_dns_address  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateADConnectorOfficeSiteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.sub_domain_dns_address is not None:
            result['SubDomainDnsAddress'] = self.sub_domain_dns_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('SubDomainDnsAddress') is not None:
            self.sub_domain_dns_address = m.get('SubDomainDnsAddress')
        return self


class CreateADConnectorOfficeSiteResponseBody(TeaModel):
    def __init__(self, request_id=None, office_site_id=None):
        self.request_id = request_id  # type: str
        self.office_site_id = office_site_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateADConnectorOfficeSiteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class CreateADConnectorOfficeSiteResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateADConnectorOfficeSiteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateADConnectorOfficeSiteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateADConnectorOfficeSiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBundleRequest(TeaModel):
    def __init__(self, region_id=None, image_id=None, desktop_type=None, root_disk_size_gib=None, bundle_name=None,
                 description=None, user_disk_size_gib=None):
        self.region_id = region_id  # type: str
        self.image_id = image_id  # type: str
        self.desktop_type = desktop_type  # type: str
        self.root_disk_size_gib = root_disk_size_gib  # type: int
        self.bundle_name = bundle_name  # type: str
        self.description = description  # type: str
        self.user_disk_size_gib = user_disk_size_gib  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBundleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.root_disk_size_gib is not None:
            result['RootDiskSizeGib'] = self.root_disk_size_gib
        if self.bundle_name is not None:
            result['BundleName'] = self.bundle_name
        if self.description is not None:
            result['Description'] = self.description
        if self.user_disk_size_gib is not None:
            result['UserDiskSizeGib'] = self.user_disk_size_gib
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('RootDiskSizeGib') is not None:
            self.root_disk_size_gib = m.get('RootDiskSizeGib')
        if m.get('BundleName') is not None:
            self.bundle_name = m.get('BundleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UserDiskSizeGib') is not None:
            self.user_disk_size_gib = m.get('UserDiskSizeGib')
        return self


class CreateBundleResponseBody(TeaModel):
    def __init__(self, bundle_id=None, request_id=None):
        self.bundle_id = bundle_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateBundleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBundleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateBundleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateBundleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateBundleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDesktopGroupRequest(TeaModel):
    def __init__(self, region_id=None, bundle_id=None, office_site_id=None, policy_group_id=None,
                 desktop_group_name=None, directory_id=None, scale_strategy_id=None, vpc_id=None, default_init_desktop_count=None,
                 keep_duration=None, charge_type=None, period=None, period_unit=None, own_type=None, auto_pay=None, comments=None,
                 min_desktops_count=None, max_desktops_count=None, allow_auto_setup=None, allow_buffer_count=None, client_token=None,
                 end_user_ids=None):
        self.region_id = region_id  # type: str
        self.bundle_id = bundle_id  # type: str
        self.office_site_id = office_site_id  # type: str
        self.policy_group_id = policy_group_id  # type: str
        self.desktop_group_name = desktop_group_name  # type: str
        self.directory_id = directory_id  # type: str
        self.scale_strategy_id = scale_strategy_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.default_init_desktop_count = default_init_desktop_count  # type: int
        self.keep_duration = keep_duration  # type: long
        self.charge_type = charge_type  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.own_type = own_type  # type: int
        self.auto_pay = auto_pay  # type: bool
        self.comments = comments  # type: str
        self.min_desktops_count = min_desktops_count  # type: int
        self.max_desktops_count = max_desktops_count  # type: int
        self.allow_auto_setup = allow_auto_setup  # type: int
        self.allow_buffer_count = allow_buffer_count  # type: int
        self.client_token = client_token  # type: str
        self.end_user_ids = end_user_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDesktopGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.scale_strategy_id is not None:
            result['ScaleStrategyId'] = self.scale_strategy_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.default_init_desktop_count is not None:
            result['DefaultInitDesktopCount'] = self.default_init_desktop_count
        if self.keep_duration is not None:
            result['KeepDuration'] = self.keep_duration
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.own_type is not None:
            result['OwnType'] = self.own_type
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count
        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count
        if self.allow_auto_setup is not None:
            result['AllowAutoSetup'] = self.allow_auto_setup
        if self.allow_buffer_count is not None:
            result['AllowBufferCount'] = self.allow_buffer_count
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('ScaleStrategyId') is not None:
            self.scale_strategy_id = m.get('ScaleStrategyId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('DefaultInitDesktopCount') is not None:
            self.default_init_desktop_count = m.get('DefaultInitDesktopCount')
        if m.get('KeepDuration') is not None:
            self.keep_duration = m.get('KeepDuration')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')
        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')
        if m.get('AllowAutoSetup') is not None:
            self.allow_auto_setup = m.get('AllowAutoSetup')
        if m.get('AllowBufferCount') is not None:
            self.allow_buffer_count = m.get('AllowBufferCount')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        return self


class CreateDesktopGroupResponseBody(TeaModel):
    def __init__(self, desktop_group_id=None, request_id=None, order_ids=None):
        self.desktop_group_id = desktop_group_id  # type: str
        self.request_id = request_id  # type: str
        self.order_ids = order_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDesktopGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class CreateDesktopGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDesktopGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDesktopGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDesktopsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDesktopsRequestTag, self).to_map()
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


class CreateDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, group_id=None, bundle_id=None, desktop_name=None, user_name=None, vpc_id=None,
                 amount=None, directory_id=None, office_site_id=None, policy_group_id=None, charge_type=None, period=None,
                 period_unit=None, auto_pay=None, auto_renew=None, promotion_id=None, user_assign_mode=None, end_user_id=None,
                 tag=None):
        self.region_id = region_id  # type: str
        self.group_id = group_id  # type: str
        self.bundle_id = bundle_id  # type: str
        self.desktop_name = desktop_name  # type: str
        self.user_name = user_name  # type: str
        self.vpc_id = vpc_id  # type: str
        self.amount = amount  # type: int
        self.directory_id = directory_id  # type: str
        self.office_site_id = office_site_id  # type: str
        self.policy_group_id = policy_group_id  # type: str
        self.charge_type = charge_type  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.auto_renew = auto_renew  # type: bool
        self.promotion_id = promotion_id  # type: str
        self.user_assign_mode = user_assign_mode  # type: str
        self.end_user_id = end_user_id  # type: list[str]
        self.tag = tag  # type: list[CreateDesktopsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateDesktopsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.user_assign_mode is not None:
            result['UserAssignMode'] = self.user_assign_mode
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('UserAssignMode') is not None:
            self.user_assign_mode = m.get('UserAssignMode')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateDesktopsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateDesktopsResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None, desktop_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str
        self.desktop_id = desktop_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDesktopsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class CreateDesktopsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDesktopsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDesktopsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDesktopsLiteRequest(TeaModel):
    def __init__(self, region_id=None, bundle_id=None, user_assign_mode=None, amount=None,
                 enable_internet_access=None, bandwidth=None, period_unit=None, period=None, end_user_id=None):
        self.region_id = region_id  # type: str
        self.bundle_id = bundle_id  # type: str
        self.user_assign_mode = user_assign_mode  # type: str
        self.amount = amount  # type: int
        self.enable_internet_access = enable_internet_access  # type: bool
        self.bandwidth = bandwidth  # type: int
        self.period_unit = period_unit  # type: str
        self.period = period  # type: int
        self.end_user_id = end_user_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDesktopsLiteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.user_assign_mode is not None:
            result['UserAssignMode'] = self.user_assign_mode
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period is not None:
            result['Period'] = self.period
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('UserAssignMode') is not None:
            self.user_assign_mode = m.get('UserAssignMode')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        return self


class CreateDesktopsLiteResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None, desktop_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str
        self.desktop_id = desktop_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDesktopsLiteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class CreateDesktopsLiteResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDesktopsLiteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDesktopsLiteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDesktopsLiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None, image_name=None, description=None, snapshot_id=None,
                 image_resource_type=None, snapshot_ids=None):
        self.region_id = region_id  # type: str
        self.desktop_id = desktop_id  # type: str
        self.image_name = image_name  # type: str
        self.description = description  # type: str
        self.snapshot_id = snapshot_id  # type: str
        self.image_resource_type = image_resource_type  # type: str
        self.snapshot_ids = snapshot_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.description is not None:
            result['Description'] = self.description
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.image_resource_type is not None:
            result['ImageResourceType'] = self.image_resource_type
        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('ImageResourceType') is not None:
            self.image_resource_type = m.get('ImageResourceType')
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')
        return self


class CreateImageResponseBody(TeaModel):
    def __init__(self, image_id=None, request_id=None):
        self.image_id = image_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateImageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNASFileSystemRequest(TeaModel):
    def __init__(self, region_id=None, office_site_id=None, name=None, description=None):
        self.region_id = region_id  # type: str
        self.office_site_id = office_site_id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNASFileSystemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateNASFileSystemResponseBody(TeaModel):
    def __init__(self, file_system_id=None, file_system_name=None, mount_target_domain=None, request_id=None,
                 office_site_id=None):
        self.file_system_id = file_system_id  # type: str
        self.file_system_name = file_system_name  # type: str
        self.mount_target_domain = mount_target_domain  # type: str
        self.request_id = request_id  # type: str
        self.office_site_id = office_site_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNASFileSystemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class CreateNASFileSystemResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateNASFileSystemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNASFileSystemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateNASFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNetworkPackageRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth=None, office_site_id=None, internet_charge_type=None, period=None,
                 period_unit=None, auto_pay=None, auto_renew=None):
        self.region_id = region_id  # type: str
        self.bandwidth = bandwidth  # type: int
        self.office_site_id = office_site_id  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.auto_renew = auto_renew  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNetworkPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        return self


class CreateNetworkPackageResponseBody(TeaModel):
    def __init__(self, network_package_id=None, request_id=None, order_id=None):
        self.network_package_id = network_package_id  # type: str
        self.request_id = request_id  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNetworkPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateNetworkPackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateNetworkPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNetworkPackageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateNetworkPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyGroupRequestAuthorizeSecurityPolicyRule(TeaModel):
    def __init__(self, type=None, policy=None, port_range=None, description=None, ip_protocol=None, priority=None,
                 cidr_ip=None):
        self.type = type  # type: str
        self.policy = policy  # type: str
        self.port_range = port_range  # type: str
        self.description = description  # type: str
        self.ip_protocol = ip_protocol  # type: str
        self.priority = priority  # type: str
        self.cidr_ip = cidr_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyGroupRequestAuthorizeSecurityPolicyRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.description is not None:
            result['Description'] = self.description
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        return self


class CreatePolicyGroupRequestAuthorizeAccessPolicyRule(TeaModel):
    def __init__(self, description=None, cidr_ip=None):
        self.description = description  # type: str
        self.cidr_ip = cidr_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyGroupRequestAuthorizeAccessPolicyRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        return self


class CreatePolicyGroupRequest(TeaModel):
    def __init__(self, region_id=None, clipboard=None, local_drive=None, usb_redirect=None, visual_quality=None,
                 html_5access=None, html_5file_transfer=None, watermark=None, name=None, watermark_type=None,
                 watermark_custom_text=None, watermark_transparency=None, preempt_login=None, domain_list=None, preempt_login_user=None,
                 authorize_security_policy_rule=None, authorize_access_policy_rule=None):
        self.region_id = region_id  # type: str
        self.clipboard = clipboard  # type: str
        self.local_drive = local_drive  # type: str
        self.usb_redirect = usb_redirect  # type: str
        self.visual_quality = visual_quality  # type: str
        self.html_5access = html_5access  # type: str
        self.html_5file_transfer = html_5file_transfer  # type: str
        self.watermark = watermark  # type: str
        self.name = name  # type: str
        self.watermark_type = watermark_type  # type: str
        self.watermark_custom_text = watermark_custom_text  # type: str
        self.watermark_transparency = watermark_transparency  # type: str
        self.preempt_login = preempt_login  # type: str
        self.domain_list = domain_list  # type: str
        self.preempt_login_user = preempt_login_user  # type: list[str]
        self.authorize_security_policy_rule = authorize_security_policy_rule  # type: list[CreatePolicyGroupRequestAuthorizeSecurityPolicyRule]
        self.authorize_access_policy_rule = authorize_access_policy_rule  # type: list[CreatePolicyGroupRequestAuthorizeAccessPolicyRule]

    def validate(self):
        if self.authorize_security_policy_rule:
            for k in self.authorize_security_policy_rule:
                if k:
                    k.validate()
        if self.authorize_access_policy_rule:
            for k in self.authorize_access_policy_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreatePolicyGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.visual_quality is not None:
            result['VisualQuality'] = self.visual_quality
        if self.html_5access is not None:
            result['Html5Access'] = self.html_5access
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.name is not None:
            result['Name'] = self.name
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        if self.watermark_custom_text is not None:
            result['WatermarkCustomText'] = self.watermark_custom_text
        if self.watermark_transparency is not None:
            result['WatermarkTransparency'] = self.watermark_transparency
        if self.preempt_login is not None:
            result['PreemptLogin'] = self.preempt_login
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.preempt_login_user is not None:
            result['PreemptLoginUser'] = self.preempt_login_user
        result['AuthorizeSecurityPolicyRule'] = []
        if self.authorize_security_policy_rule is not None:
            for k in self.authorize_security_policy_rule:
                result['AuthorizeSecurityPolicyRule'].append(k.to_map() if k else None)
        result['AuthorizeAccessPolicyRule'] = []
        if self.authorize_access_policy_rule is not None:
            for k in self.authorize_access_policy_rule:
                result['AuthorizeAccessPolicyRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('VisualQuality') is not None:
            self.visual_quality = m.get('VisualQuality')
        if m.get('Html5Access') is not None:
            self.html_5access = m.get('Html5Access')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        if m.get('WatermarkCustomText') is not None:
            self.watermark_custom_text = m.get('WatermarkCustomText')
        if m.get('WatermarkTransparency') is not None:
            self.watermark_transparency = m.get('WatermarkTransparency')
        if m.get('PreemptLogin') is not None:
            self.preempt_login = m.get('PreemptLogin')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('PreemptLoginUser') is not None:
            self.preempt_login_user = m.get('PreemptLoginUser')
        self.authorize_security_policy_rule = []
        if m.get('AuthorizeSecurityPolicyRule') is not None:
            for k in m.get('AuthorizeSecurityPolicyRule'):
                temp_model = CreatePolicyGroupRequestAuthorizeSecurityPolicyRule()
                self.authorize_security_policy_rule.append(temp_model.from_map(k))
        self.authorize_access_policy_rule = []
        if m.get('AuthorizeAccessPolicyRule') is not None:
            for k in m.get('AuthorizeAccessPolicyRule'):
                temp_model = CreatePolicyGroupRequestAuthorizeAccessPolicyRule()
                self.authorize_access_policy_rule.append(temp_model.from_map(k))
        return self


class CreatePolicyGroupResponseBody(TeaModel):
    def __init__(self, policy_group_id=None, request_id=None):
        self.policy_group_id = policy_group_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePolicyGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePolicyGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreatePolicyGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePolicyGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRAMDirectoryRequest(TeaModel):
    def __init__(self, region_id=None, directory_name=None, enable_internet_access=None, enable_admin_access=None,
                 desktop_access_type=None, v_switch_id=None):
        self.region_id = region_id  # type: str
        self.directory_name = directory_name  # type: str
        self.enable_internet_access = enable_internet_access  # type: bool
        self.enable_admin_access = enable_admin_access  # type: bool
        self.desktop_access_type = desktop_access_type  # type: str
        self.v_switch_id = v_switch_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRAMDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateRAMDirectoryResponseBody(TeaModel):
    def __init__(self, directory_id=None, request_id=None):
        self.directory_id = directory_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRAMDirectoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRAMDirectoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateRAMDirectoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRAMDirectoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRAMDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScaleStrategyRequest(TeaModel):
    def __init__(self, region_id=None, scale_strategy_name=None, scale_strategy_type=None, pay_type=None,
                 min_desktops_count=None, max_desktops_count=None, min_available_desktops_count=None,
                 max_available_desktops_count=None, scale_step=None, client_token=None):
        self.region_id = region_id  # type: str
        self.scale_strategy_name = scale_strategy_name  # type: str
        self.scale_strategy_type = scale_strategy_type  # type: str
        self.pay_type = pay_type  # type: str
        self.min_desktops_count = min_desktops_count  # type: int
        self.max_desktops_count = max_desktops_count  # type: int
        self.min_available_desktops_count = min_available_desktops_count  # type: int
        self.max_available_desktops_count = max_available_desktops_count  # type: int
        self.scale_step = scale_step  # type: int
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScaleStrategyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scale_strategy_name is not None:
            result['ScaleStrategyName'] = self.scale_strategy_name
        if self.scale_strategy_type is not None:
            result['ScaleStrategyType'] = self.scale_strategy_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count
        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count
        if self.min_available_desktops_count is not None:
            result['MinAvailableDesktopsCount'] = self.min_available_desktops_count
        if self.max_available_desktops_count is not None:
            result['MaxAvailableDesktopsCount'] = self.max_available_desktops_count
        if self.scale_step is not None:
            result['ScaleStep'] = self.scale_step
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScaleStrategyName') is not None:
            self.scale_strategy_name = m.get('ScaleStrategyName')
        if m.get('ScaleStrategyType') is not None:
            self.scale_strategy_type = m.get('ScaleStrategyType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')
        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')
        if m.get('MinAvailableDesktopsCount') is not None:
            self.min_available_desktops_count = m.get('MinAvailableDesktopsCount')
        if m.get('MaxAvailableDesktopsCount') is not None:
            self.max_available_desktops_count = m.get('MaxAvailableDesktopsCount')
        if m.get('ScaleStep') is not None:
            self.scale_step = m.get('ScaleStep')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateScaleStrategyResponseBody(TeaModel):
    def __init__(self, scale_strategy_id=None, request_id=None):
        self.scale_strategy_id = scale_strategy_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateScaleStrategyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_strategy_id is not None:
            result['ScaleStrategyId'] = self.scale_strategy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScaleStrategyId') is not None:
            self.scale_strategy_id = m.get('ScaleStrategyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateScaleStrategyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateScaleStrategyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateScaleStrategyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateScaleStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceLinkedRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateServiceLinkedRoleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceLinkedRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateServiceLinkedRoleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateServiceLinkedRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceLinkedRoleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSimpleOfficeSiteRequest(TeaModel):
    def __init__(self, region_id=None, cidr_block=None, cen_id=None, bandwidth=None, office_site_name=None,
                 enable_internet_access=None, enable_admin_access=None, desktop_access_type=None):
        self.region_id = region_id  # type: str
        self.cidr_block = cidr_block  # type: str
        self.cen_id = cen_id  # type: str
        self.bandwidth = bandwidth  # type: int
        self.office_site_name = office_site_name  # type: str
        self.enable_internet_access = enable_internet_access  # type: bool
        self.enable_admin_access = enable_admin_access  # type: bool
        self.desktop_access_type = desktop_access_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSimpleOfficeSiteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        return self


class CreateSimpleOfficeSiteResponseBody(TeaModel):
    def __init__(self, office_site_id=None, request_id=None):
        self.office_site_id = office_site_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSimpleOfficeSiteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSimpleOfficeSiteResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSimpleOfficeSiteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSimpleOfficeSiteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSimpleOfficeSiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSnapshotRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None, snapshot_name=None, description=None, source_disk_type=None):
        self.region_id = region_id  # type: str
        self.desktop_id = desktop_id  # type: str
        self.snapshot_name = snapshot_name  # type: str
        self.description = description  # type: str
        self.source_disk_type = source_disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.description is not None:
            result['Description'] = self.description
        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')
        return self


class CreateSnapshotResponseBody(TeaModel):
    def __init__(self, snapshot_id=None, request_id=None):
        self.snapshot_id = snapshot_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSnapshotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBundlesRequest(TeaModel):
    def __init__(self, region_id=None, bundle_id=None):
        self.region_id = region_id  # type: str
        self.bundle_id = bundle_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBundlesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        return self


class DeleteBundlesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBundlesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBundlesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteBundlesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBundlesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteBundlesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDesktopGroupRequest(TeaModel):
    def __init__(self, region_id=None, desktop_group_id=None):
        self.region_id = region_id  # type: str
        self.desktop_group_id = desktop_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDesktopGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        return self


class DeleteDesktopGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDesktopGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDesktopGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDesktopGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDesktopGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None):
        self.region_id = region_id  # type: str
        self.desktop_id = desktop_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDesktopsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class DeleteDesktopsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDesktopsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDesktopsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDesktopsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDesktopsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDirectoriesRequest(TeaModel):
    def __init__(self, region_id=None, directory_id=None):
        self.region_id = region_id  # type: str
        self.directory_id = directory_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDirectoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class DeleteDirectoriesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDirectoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDirectoriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDirectoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDirectoriesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImagesRequest(TeaModel):
    def __init__(self, region_id=None, image_id=None):
        self.region_id = region_id  # type: str
        self.image_id = image_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class DeleteImagesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteImagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteImagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteImagesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNASFileSystemsRequest(TeaModel):
    def __init__(self, region_id=None, file_system_id=None):
        self.region_id = region_id  # type: str
        self.file_system_id = file_system_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNASFileSystemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DeleteNASFileSystemsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNASFileSystemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNASFileSystemsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteNASFileSystemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNASFileSystemsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNASFileSystemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNetworkPackagesRequest(TeaModel):
    def __init__(self, region_id=None, network_package_id=None):
        self.region_id = region_id  # type: str
        self.network_package_id = network_package_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNetworkPackagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        return self


class DeleteNetworkPackagesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNetworkPackagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNetworkPackagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteNetworkPackagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNetworkPackagesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNetworkPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOfficeSitesRequest(TeaModel):
    def __init__(self, region_id=None, office_site_id=None):
        self.region_id = region_id  # type: str
        self.office_site_id = office_site_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteOfficeSitesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class DeleteOfficeSitesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteOfficeSitesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteOfficeSitesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteOfficeSitesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteOfficeSitesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteOfficeSitesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyGroupsRequest(TeaModel):
    def __init__(self, region_id=None, policy_group_id=None):
        self.region_id = region_id  # type: str
        self.policy_group_id = policy_group_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        return self


class DeletePolicyGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePolicyGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeletePolicyGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePolicyGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeletePolicyGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScaleStrategyRequest(TeaModel):
    def __init__(self, region_id=None, scale_strategy_id=None):
        self.region_id = region_id  # type: str
        self.scale_strategy_id = scale_strategy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteScaleStrategyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scale_strategy_id is not None:
            result['ScaleStrategyId'] = self.scale_strategy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScaleStrategyId') is not None:
            self.scale_strategy_id = m.get('ScaleStrategyId')
        return self


class DeleteScaleStrategyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteScaleStrategyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteScaleStrategyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteScaleStrategyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteScaleStrategyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteScaleStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotRequest(TeaModel):
    def __init__(self, region_id=None, snapshot_id=None):
        self.region_id = region_id  # type: str
        self.snapshot_id = snapshot_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class DeleteSnapshotResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSnapshotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVirtualMFADeviceRequest(TeaModel):
    def __init__(self, region_id=None, serial_number=None):
        self.region_id = region_id  # type: str
        self.serial_number = serial_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVirtualMFADeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class DeleteVirtualMFADeviceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVirtualMFADeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVirtualMFADeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteVirtualMFADeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVirtualMFADeviceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlarmEventStackInfoRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None, event_name=None, unique_info=None, lang=None):
        self.region_id = region_id  # type: str
        self.desktop_id = desktop_id  # type: str
        self.event_name = event_name  # type: str
        self.unique_info = unique_info  # type: str
        self.lang = lang  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlarmEventStackInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.unique_info is not None:
            result['UniqueInfo'] = self.unique_info
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('UniqueInfo') is not None:
            self.unique_info = m.get('UniqueInfo')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeAlarmEventStackInfoResponseBody(TeaModel):
    def __init__(self, stack_info=None, request_id=None):
        self.stack_info = stack_info  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAlarmEventStackInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_info is not None:
            result['StackInfo'] = self.stack_info
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StackInfo') is not None:
            self.stack_info = m.get('StackInfo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAlarmEventStackInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAlarmEventStackInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAlarmEventStackInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAlarmEventStackInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBundlesRequest(TeaModel):
    def __init__(self, region_id=None, max_results=None, next_token=None, bundle_type=None,
                 desktop_type_family=None, cpu_count=None, memory_size=None, gpu_count=None, check_stock=None, from_desktop_group=None,
                 protocol_type=None, bundle_id=None):
        self.region_id = region_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.bundle_type = bundle_type  # type: str
        self.desktop_type_family = desktop_type_family  # type: str
        self.cpu_count = cpu_count  # type: int
        self.memory_size = memory_size  # type: int
        self.gpu_count = gpu_count  # type: float
        self.check_stock = check_stock  # type: bool
        self.from_desktop_group = from_desktop_group  # type: bool
        self.protocol_type = protocol_type  # type: str
        self.bundle_id = bundle_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBundlesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.bundle_type is not None:
            result['BundleType'] = self.bundle_type
        if self.desktop_type_family is not None:
            result['DesktopTypeFamily'] = self.desktop_type_family
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.check_stock is not None:
            result['CheckStock'] = self.check_stock
        if self.from_desktop_group is not None:
            result['FromDesktopGroup'] = self.from_desktop_group
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('BundleType') is not None:
            self.bundle_type = m.get('BundleType')
        if m.get('DesktopTypeFamily') is not None:
            self.desktop_type_family = m.get('DesktopTypeFamily')
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('CheckStock') is not None:
            self.check_stock = m.get('CheckStock')
        if m.get('FromDesktopGroup') is not None:
            self.from_desktop_group = m.get('FromDesktopGroup')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        return self


class DescribeBundlesResponseBodyBundlesDisks(TeaModel):
    def __init__(self, disk_type=None, disk_size=None):
        self.disk_type = disk_type  # type: str
        self.disk_size = disk_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBundlesResponseBodyBundlesDisks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        return self


class DescribeBundlesResponseBodyBundlesDesktopTypeAttribute(TeaModel):
    def __init__(self, cpu_count=None, gpu_count=None, gpu_spec=None, memory_size=None):
        self.cpu_count = cpu_count  # type: int
        self.gpu_count = gpu_count  # type: float
        self.gpu_spec = gpu_spec  # type: str
        self.memory_size = memory_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeBundlesResponseBodyBundlesDesktopTypeAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        return self


class DescribeBundlesResponseBodyBundles(TeaModel):
    def __init__(self, description=None, bundle_type=None, os_type=None, stock_state=None, desktop_type=None,
                 protocol_type=None, bundle_id=None, image_id=None, bundle_name=None, disks=None, desktop_type_attribute=None):
        self.description = description  # type: str
        self.bundle_type = bundle_type  # type: str
        self.os_type = os_type  # type: str
        self.stock_state = stock_state  # type: str
        self.desktop_type = desktop_type  # type: str
        self.protocol_type = protocol_type  # type: str
        self.bundle_id = bundle_id  # type: str
        self.image_id = image_id  # type: str
        self.bundle_name = bundle_name  # type: str
        self.disks = disks  # type: list[DescribeBundlesResponseBodyBundlesDisks]
        self.desktop_type_attribute = desktop_type_attribute  # type: DescribeBundlesResponseBodyBundlesDesktopTypeAttribute

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()
        if self.desktop_type_attribute:
            self.desktop_type_attribute.validate()

    def to_map(self):
        _map = super(DescribeBundlesResponseBodyBundles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.bundle_type is not None:
            result['BundleType'] = self.bundle_type
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.stock_state is not None:
            result['StockState'] = self.stock_state
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.bundle_name is not None:
            result['BundleName'] = self.bundle_name
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.desktop_type_attribute is not None:
            result['DesktopTypeAttribute'] = self.desktop_type_attribute.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('BundleType') is not None:
            self.bundle_type = m.get('BundleType')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('StockState') is not None:
            self.stock_state = m.get('StockState')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('BundleName') is not None:
            self.bundle_name = m.get('BundleName')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeBundlesResponseBodyBundlesDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('DesktopTypeAttribute') is not None:
            temp_model = DescribeBundlesResponseBodyBundlesDesktopTypeAttribute()
            self.desktop_type_attribute = temp_model.from_map(m['DesktopTypeAttribute'])
        return self


class DescribeBundlesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, bundles=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.bundles = bundles  # type: list[DescribeBundlesResponseBodyBundles]

    def validate(self):
        if self.bundles:
            for k in self.bundles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeBundlesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Bundles'] = []
        if self.bundles is not None:
            for k in self.bundles:
                result['Bundles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.bundles = []
        if m.get('Bundles') is not None:
            for k in m.get('Bundles'):
                temp_model = DescribeBundlesResponseBodyBundles()
                self.bundles.append(temp_model.from_map(k))
        return self


class DescribeBundlesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeBundlesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeBundlesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBundlesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCensRequest(TeaModel):
    def __init__(self, region_id=None, page_size=None, page_number=None):
        self.region_id = region_id  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCensRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeCensResponseBodyCensTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCensResponseBodyCensTags, self).to_map()
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


class DescribeCensResponseBodyCensPackageIds(TeaModel):
    def __init__(self, package_id=None):
        self.package_id = package_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCensResponseBodyCensPackageIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        return self


class DescribeCensResponseBodyCens(TeaModel):
    def __init__(self, status=None, creation_time=None, ipv_6level=None, description=None, cen_id=None,
                 protection_level=None, name=None, tags=None, package_ids=None):
        self.status = status  # type: str
        self.creation_time = creation_time  # type: str
        self.ipv_6level = ipv_6level  # type: str
        self.description = description  # type: str
        self.cen_id = cen_id  # type: str
        self.protection_level = protection_level  # type: str
        self.name = name  # type: str
        self.tags = tags  # type: list[DescribeCensResponseBodyCensTags]
        self.package_ids = package_ids  # type: list[DescribeCensResponseBodyCensPackageIds]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.package_ids:
            for k in self.package_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCensResponseBodyCens, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.ipv_6level is not None:
            result['Ipv6Level'] = self.ipv_6level
        if self.description is not None:
            result['Description'] = self.description
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.name is not None:
            result['Name'] = self.name
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['PackageIds'] = []
        if self.package_ids is not None:
            for k in self.package_ids:
                result['PackageIds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Ipv6Level') is not None:
            self.ipv_6level = m.get('Ipv6Level')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeCensResponseBodyCensTags()
                self.tags.append(temp_model.from_map(k))
        self.package_ids = []
        if m.get('PackageIds') is not None:
            for k in m.get('PackageIds'):
                temp_model = DescribeCensResponseBodyCensPackageIds()
                self.package_ids.append(temp_model.from_map(k))
        return self


class DescribeCensResponseBody(TeaModel):
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, cens=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.cens = cens  # type: list[DescribeCensResponseBodyCens]

    def validate(self):
        if self.cens:
            for k in self.cens:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeCensResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Cens'] = []
        if self.cens is not None:
            for k in self.cens:
                result['Cens'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.cens = []
        if m.get('Cens') is not None:
            for k in m.get('Cens'):
                temp_model = DescribeCensResponseBodyCens()
                self.cens.append(temp_model.from_map(k))
        return self


class DescribeCensResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCensResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCensResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCensResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClientEventsRequest(TeaModel):
    def __init__(self, region_id=None, end_user_id=None, desktop_id=None, desktop_ip=None, directory_id=None,
                 office_site_id=None, event_type=None, start_time=None, end_time=None, max_results=None, next_token=None):
        self.region_id = region_id  # type: str
        self.end_user_id = end_user_id  # type: str
        self.desktop_id = desktop_id  # type: str
        self.desktop_ip = desktop_ip  # type: str
        self.directory_id = directory_id  # type: str
        self.office_site_id = office_site_id  # type: str
        self.event_type = event_type  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClientEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_ip is not None:
            result['DesktopIp'] = self.desktop_ip
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopIp') is not None:
            self.desktop_ip = m.get('DesktopIp')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeClientEventsResponseBodyEvents(TeaModel):
    def __init__(self, status=None, bytes_received=None, desktop_ip=None, event_time=None, bytes_send=None,
                 office_site_id=None, ali_uid=None, desktop_id=None, region_id=None, event_id=None, directory_type=None,
                 event_type=None, end_user_id=None, client_ip=None, client_os=None, office_site_type=None, directory_id=None,
                 client_version=None):
        self.status = status  # type: str
        self.bytes_received = bytes_received  # type: str
        self.desktop_ip = desktop_ip  # type: str
        self.event_time = event_time  # type: str
        self.bytes_send = bytes_send  # type: str
        self.office_site_id = office_site_id  # type: str
        self.ali_uid = ali_uid  # type: str
        self.desktop_id = desktop_id  # type: str
        self.region_id = region_id  # type: str
        self.event_id = event_id  # type: str
        self.directory_type = directory_type  # type: str
        self.event_type = event_type  # type: str
        self.end_user_id = end_user_id  # type: str
        self.client_ip = client_ip  # type: str
        self.client_os = client_os  # type: str
        self.office_site_type = office_site_type  # type: str
        self.directory_id = directory_id  # type: str
        self.client_version = client_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClientEventsResponseBodyEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.bytes_received is not None:
            result['BytesReceived'] = self.bytes_received
        if self.desktop_ip is not None:
            result['DesktopIp'] = self.desktop_ip
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.bytes_send is not None:
            result['BytesSend'] = self.bytes_send
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('BytesReceived') is not None:
            self.bytes_received = m.get('BytesReceived')
        if m.get('DesktopIp') is not None:
            self.desktop_ip = m.get('DesktopIp')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('BytesSend') is not None:
            self.bytes_send = m.get('BytesSend')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        return self


class DescribeClientEventsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, events=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.events = events  # type: list[DescribeClientEventsResponseBodyEvents]

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClientEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeClientEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        return self


class DescribeClientEventsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClientEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClientEventsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeClientEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopIdsByVulNamesRequest(TeaModel):
    def __init__(self, region_id=None, type=None, office_site_id=None, necessity=None, vul_name=None):
        self.region_id = region_id  # type: str
        self.type = type  # type: str
        self.office_site_id = office_site_id  # type: str
        self.necessity = necessity  # type: str
        self.vul_name = vul_name  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDesktopIdsByVulNamesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.vul_name is not None:
            result['VulName'] = self.vul_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('VulName') is not None:
            self.vul_name = m.get('VulName')
        return self


class DescribeDesktopIdsByVulNamesResponseBodyDesktopItems(TeaModel):
    def __init__(self, desktop_name=None, desktop_id=None):
        self.desktop_name = desktop_name  # type: str
        self.desktop_id = desktop_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDesktopIdsByVulNamesResponseBodyDesktopItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class DescribeDesktopIdsByVulNamesResponseBody(TeaModel):
    def __init__(self, request_id=None, desktop_items=None):
        self.request_id = request_id  # type: str
        self.desktop_items = desktop_items  # type: list[DescribeDesktopIdsByVulNamesResponseBodyDesktopItems]

    def validate(self):
        if self.desktop_items:
            for k in self.desktop_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDesktopIdsByVulNamesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DesktopItems'] = []
        if self.desktop_items is not None:
            for k in self.desktop_items:
                result['DesktopItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.desktop_items = []
        if m.get('DesktopItems') is not None:
            for k in m.get('DesktopItems'):
                temp_model = DescribeDesktopIdsByVulNamesResponseBodyDesktopItems()
                self.desktop_items.append(temp_model.from_map(k))
        return self


class DescribeDesktopIdsByVulNamesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDesktopIdsByVulNamesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDesktopIdsByVulNamesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDesktopIdsByVulNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopPolicysRequest(TeaModel):
    def __init__(self, region_id=None, next_token=None, max_results=None, desktop_id=None):
        self.region_id = region_id  # type: str
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int
        self.desktop_id = desktop_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDesktopPolicysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class DescribeDesktopPolicysResponseBodyDescribeDesktopPolicys(TeaModel):
    def __init__(self, usb_redirect=None, desktop_id=None, watermark=None, clipboard=None, local_drive=None):
        self.usb_redirect = usb_redirect  # type: str
        self.desktop_id = desktop_id  # type: str
        self.watermark = watermark  # type: str
        self.clipboard = clipboard  # type: str
        self.local_drive = local_drive  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDesktopPolicysResponseBodyDescribeDesktopPolicys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        return self


class DescribeDesktopPolicysResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, describe_desktop_policys=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.describe_desktop_policys = describe_desktop_policys  # type: list[DescribeDesktopPolicysResponseBodyDescribeDesktopPolicys]

    def validate(self):
        if self.describe_desktop_policys:
            for k in self.describe_desktop_policys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDesktopPolicysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DescribeDesktopPolicys'] = []
        if self.describe_desktop_policys is not None:
            for k in self.describe_desktop_policys:
                result['DescribeDesktopPolicys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.describe_desktop_policys = []
        if m.get('DescribeDesktopPolicys') is not None:
            for k in m.get('DescribeDesktopPolicys'):
                temp_model = DescribeDesktopPolicysResponseBodyDescribeDesktopPolicys()
                self.describe_desktop_policys.append(temp_model.from_map(k))
        return self


class DescribeDesktopPolicysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDesktopPolicysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDesktopPolicysResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDesktopPolicysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, group_id=None, desktop_status=None, max_results=None, next_token=None,
                 user_name=None, desktop_name=None, directory_id=None, office_site_id=None, policy_group_id=None,
                 charge_type=None, expired_time=None, desktop_id=None, end_user_id=None):
        self.region_id = region_id  # type: str
        self.group_id = group_id  # type: str
        self.desktop_status = desktop_status  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.user_name = user_name  # type: str
        self.desktop_name = desktop_name  # type: str
        self.directory_id = directory_id  # type: str
        self.office_site_id = office_site_id  # type: str
        self.policy_group_id = policy_group_id  # type: str
        self.charge_type = charge_type  # type: str
        self.expired_time = expired_time  # type: str
        self.desktop_id = desktop_id  # type: list[str]
        self.end_user_id = end_user_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDesktopsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        return self


class DescribeDesktopsResponseBodyDesktopsDisks(TeaModel):
    def __init__(self, disk_type=None, disk_id=None, disk_size=None):
        self.disk_type = disk_type  # type: str
        self.disk_id = disk_id  # type: str
        self.disk_size = disk_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDesktopsResponseBodyDesktopsDisks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        return self


class DescribeDesktopsResponseBodyDesktopsTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDesktopsResponseBodyDesktopsTags, self).to_map()
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


class DescribeDesktopsResponseBodyDesktopsSessions(TeaModel):
    def __init__(self, end_user_id=None, establishment_time=None):
        self.end_user_id = end_user_id  # type: str
        self.establishment_time = establishment_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDesktopsResponseBodyDesktopsSessions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.establishment_time is not None:
            result['EstablishmentTime'] = self.establishment_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EstablishmentTime') is not None:
            self.establishment_time = m.get('EstablishmentTime')
        return self


class DescribeDesktopsResponseBodyDesktops(TeaModel):
    def __init__(self, creation_time=None, charge_type=None, desktop_name=None, policy_group_name=None,
                 system_disk_size=None, policy_group_id=None, desktop_status=None, desktop_type=None, gpu_count=None, memory=None,
                 gpu_spec=None, directory_id=None, image_id=None, management_flag=None, data_disk_category=None,
                 system_disk_category=None, office_site_id=None, network_interface_id=None, data_disk_size=None, desktop_id=None,
                 office_site_name=None, start_time=None, directory_type=None, cpu=None, network_interface_ip=None, expired_time=None,
                 os_type=None, connection_status=None, bundle_id=None, office_site_type=None, disks=None, tags=None,
                 sessions=None, end_user_ids=None):
        self.creation_time = creation_time  # type: str
        self.charge_type = charge_type  # type: str
        self.desktop_name = desktop_name  # type: str
        self.policy_group_name = policy_group_name  # type: str
        self.system_disk_size = system_disk_size  # type: int
        self.policy_group_id = policy_group_id  # type: str
        self.desktop_status = desktop_status  # type: str
        self.desktop_type = desktop_type  # type: str
        self.gpu_count = gpu_count  # type: float
        self.memory = memory  # type: long
        self.gpu_spec = gpu_spec  # type: str
        self.directory_id = directory_id  # type: str
        self.image_id = image_id  # type: str
        self.management_flag = management_flag  # type: str
        self.data_disk_category = data_disk_category  # type: str
        self.system_disk_category = system_disk_category  # type: str
        self.office_site_id = office_site_id  # type: str
        self.network_interface_id = network_interface_id  # type: str
        self.data_disk_size = data_disk_size  # type: str
        self.desktop_id = desktop_id  # type: str
        self.office_site_name = office_site_name  # type: str
        self.start_time = start_time  # type: str
        self.directory_type = directory_type  # type: str
        self.cpu = cpu  # type: int
        self.network_interface_ip = network_interface_ip  # type: str
        self.expired_time = expired_time  # type: str
        self.os_type = os_type  # type: str
        self.connection_status = connection_status  # type: str
        self.bundle_id = bundle_id  # type: str
        self.office_site_type = office_site_type  # type: str
        self.disks = disks  # type: list[DescribeDesktopsResponseBodyDesktopsDisks]
        self.tags = tags  # type: list[DescribeDesktopsResponseBodyDesktopsTags]
        self.sessions = sessions  # type: list[DescribeDesktopsResponseBodyDesktopsSessions]
        self.end_user_ids = end_user_ids  # type: list[str]

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.sessions:
            for k in self.sessions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDesktopsResponseBodyDesktops, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.management_flag is not None:
            result['ManagementFlag'] = self.management_flag
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.network_interface_ip is not None:
            result['NetworkInterfaceIp'] = self.network_interface_ip
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['Sessions'] = []
        if self.sessions is not None:
            for k in self.sessions:
                result['Sessions'].append(k.to_map() if k else None)
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ManagementFlag') is not None:
            self.management_flag = m.get('ManagementFlag')
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('NetworkInterfaceIp') is not None:
            self.network_interface_ip = m.get('NetworkInterfaceIp')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeDesktopsResponseBodyDesktopsDisks()
                self.disks.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDesktopsResponseBodyDesktopsTags()
                self.tags.append(temp_model.from_map(k))
        self.sessions = []
        if m.get('Sessions') is not None:
            for k in m.get('Sessions'):
                temp_model = DescribeDesktopsResponseBodyDesktopsSessions()
                self.sessions.append(temp_model.from_map(k))
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        return self


class DescribeDesktopsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, desktops=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.desktops = desktops  # type: list[DescribeDesktopsResponseBodyDesktops]

    def validate(self):
        if self.desktops:
            for k in self.desktops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDesktopsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Desktops'] = []
        if self.desktops is not None:
            for k in self.desktops:
                result['Desktops'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.desktops = []
        if m.get('Desktops') is not None:
            for k in m.get('Desktops'):
                temp_model = DescribeDesktopsResponseBodyDesktops()
                self.desktops.append(temp_model.from_map(k))
        return self


class DescribeDesktopsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDesktopsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDesktopsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopsInGroupRequest(TeaModel):
    def __init__(self, region_id=None, desktop_group_id=None, pay_type=None, max_results=None, next_token=None):
        self.region_id = region_id  # type: str
        self.desktop_group_id = desktop_group_id  # type: str
        self.pay_type = pay_type  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDesktopsInGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeDesktopsInGroupResponseBodyPaidDesktops(TeaModel):
    def __init__(self, end_user_id=None, desktop_status=None, desktop_name=None, connection_status=None,
                 desktop_id=None, end_user_name=None):
        self.end_user_id = end_user_id  # type: str
        self.desktop_status = desktop_status  # type: str
        self.desktop_name = desktop_name  # type: str
        self.connection_status = connection_status  # type: str
        self.desktop_id = desktop_id  # type: str
        self.end_user_name = end_user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDesktopsInGroupResponseBodyPaidDesktops, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.end_user_name is not None:
            result['EndUserName'] = self.end_user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EndUserName') is not None:
            self.end_user_name = m.get('EndUserName')
        return self


class DescribeDesktopsInGroupResponseBodyPostPaidDesktops(TeaModel):
    def __init__(self, create_duration=None, end_user_id=None, desktop_status=None, create_time=None,
                 release_time=None, desktop_name=None, connection_status=None, desktop_id=None, end_user_name=None):
        self.create_duration = create_duration  # type: str
        self.end_user_id = end_user_id  # type: str
        self.desktop_status = desktop_status  # type: str
        self.create_time = create_time  # type: str
        self.release_time = release_time  # type: str
        self.desktop_name = desktop_name  # type: str
        self.connection_status = connection_status  # type: str
        self.desktop_id = desktop_id  # type: str
        self.end_user_name = end_user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDesktopsInGroupResponseBodyPostPaidDesktops, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_duration is not None:
            result['CreateDuration'] = self.create_duration
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.end_user_name is not None:
            result['EndUserName'] = self.end_user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateDuration') is not None:
            self.create_duration = m.get('CreateDuration')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EndUserName') is not None:
            self.end_user_name = m.get('EndUserName')
        return self


class DescribeDesktopsInGroupResponseBody(TeaModel):
    def __init__(self, post_paid_desktops_count=None, next_token=None, paid_desktops_count=None, request_id=None,
                 post_paid_desktops_total_amount=None, paid_desktops=None, post_paid_desktops=None):
        self.post_paid_desktops_count = post_paid_desktops_count  # type: int
        self.next_token = next_token  # type: str
        self.paid_desktops_count = paid_desktops_count  # type: int
        self.request_id = request_id  # type: str
        self.post_paid_desktops_total_amount = post_paid_desktops_total_amount  # type: int
        self.paid_desktops = paid_desktops  # type: list[DescribeDesktopsInGroupResponseBodyPaidDesktops]
        self.post_paid_desktops = post_paid_desktops  # type: list[DescribeDesktopsInGroupResponseBodyPostPaidDesktops]

    def validate(self):
        if self.paid_desktops:
            for k in self.paid_desktops:
                if k:
                    k.validate()
        if self.post_paid_desktops:
            for k in self.post_paid_desktops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDesktopsInGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.post_paid_desktops_count is not None:
            result['PostPaidDesktopsCount'] = self.post_paid_desktops_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.paid_desktops_count is not None:
            result['PaidDesktopsCount'] = self.paid_desktops_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.post_paid_desktops_total_amount is not None:
            result['PostPaidDesktopsTotalAmount'] = self.post_paid_desktops_total_amount
        result['PaidDesktops'] = []
        if self.paid_desktops is not None:
            for k in self.paid_desktops:
                result['PaidDesktops'].append(k.to_map() if k else None)
        result['PostPaidDesktops'] = []
        if self.post_paid_desktops is not None:
            for k in self.post_paid_desktops:
                result['PostPaidDesktops'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PostPaidDesktopsCount') is not None:
            self.post_paid_desktops_count = m.get('PostPaidDesktopsCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PaidDesktopsCount') is not None:
            self.paid_desktops_count = m.get('PaidDesktopsCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PostPaidDesktopsTotalAmount') is not None:
            self.post_paid_desktops_total_amount = m.get('PostPaidDesktopsTotalAmount')
        self.paid_desktops = []
        if m.get('PaidDesktops') is not None:
            for k in m.get('PaidDesktops'):
                temp_model = DescribeDesktopsInGroupResponseBodyPaidDesktops()
                self.paid_desktops.append(temp_model.from_map(k))
        self.post_paid_desktops = []
        if m.get('PostPaidDesktops') is not None:
            for k in m.get('PostPaidDesktops'):
                temp_model = DescribeDesktopsInGroupResponseBodyPostPaidDesktops()
                self.post_paid_desktops.append(temp_model.from_map(k))
        return self


class DescribeDesktopsInGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDesktopsInGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDesktopsInGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDesktopsInGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopTypesRequest(TeaModel):
    def __init__(self, region_id=None, desktop_type_id=None, instance_type_family=None, cpu_count=None,
                 memory_size=None, gpu_count=None):
        self.region_id = region_id  # type: str
        self.desktop_type_id = desktop_type_id  # type: str
        self.instance_type_family = instance_type_family  # type: str
        self.cpu_count = cpu_count  # type: int
        self.memory_size = memory_size  # type: int
        self.gpu_count = gpu_count  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDesktopTypesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_type_id is not None:
            result['DesktopTypeId'] = self.desktop_type_id
        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopTypeId') is not None:
            self.desktop_type_id = m.get('DesktopTypeId')
        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        return self


class DescribeDesktopTypesResponseBodyDesktopTypesAllowDiskSize(TeaModel):
    def __init__(self, data_disk_size=None, system_disk_size=None):
        self.data_disk_size = data_disk_size  # type: int
        self.system_disk_size = system_disk_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDesktopTypesResponseBodyDesktopTypesAllowDiskSize, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class DescribeDesktopTypesResponseBodyDesktopTypes(TeaModel):
    def __init__(self, system_disk_size=None, desktop_type_id=None, data_disk_size=None, cpu_count=None,
                 gpu_count=None, gpu_spec=None, instance_type_family=None, memory_size=None, allow_disk_size=None):
        self.system_disk_size = system_disk_size  # type: str
        self.desktop_type_id = desktop_type_id  # type: str
        self.data_disk_size = data_disk_size  # type: str
        self.cpu_count = cpu_count  # type: str
        self.gpu_count = gpu_count  # type: float
        self.gpu_spec = gpu_spec  # type: str
        self.instance_type_family = instance_type_family  # type: str
        self.memory_size = memory_size  # type: str
        self.allow_disk_size = allow_disk_size  # type: list[DescribeDesktopTypesResponseBodyDesktopTypesAllowDiskSize]

    def validate(self):
        if self.allow_disk_size:
            for k in self.allow_disk_size:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDesktopTypesResponseBodyDesktopTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.desktop_type_id is not None:
            result['DesktopTypeId'] = self.desktop_type_id
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec
        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        result['AllowDiskSize'] = []
        if self.allow_disk_size is not None:
            for k in self.allow_disk_size:
                result['AllowDiskSize'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('DesktopTypeId') is not None:
            self.desktop_type_id = m.get('DesktopTypeId')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')
        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        self.allow_disk_size = []
        if m.get('AllowDiskSize') is not None:
            for k in m.get('AllowDiskSize'):
                temp_model = DescribeDesktopTypesResponseBodyDesktopTypesAllowDiskSize()
                self.allow_disk_size.append(temp_model.from_map(k))
        return self


class DescribeDesktopTypesResponseBody(TeaModel):
    def __init__(self, request_id=None, desktop_types=None):
        self.request_id = request_id  # type: str
        self.desktop_types = desktop_types  # type: list[DescribeDesktopTypesResponseBodyDesktopTypes]

    def validate(self):
        if self.desktop_types:
            for k in self.desktop_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDesktopTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DesktopTypes'] = []
        if self.desktop_types is not None:
            for k in self.desktop_types:
                result['DesktopTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.desktop_types = []
        if m.get('DesktopTypes') is not None:
            for k in m.get('DesktopTypes'):
                temp_model = DescribeDesktopTypesResponseBodyDesktopTypes()
                self.desktop_types.append(temp_model.from_map(k))
        return self


class DescribeDesktopTypesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDesktopTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDesktopTypesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDesktopTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDirectoriesRequest(TeaModel):
    def __init__(self, region_id=None, directory_type=None, directory_status=None, max_results=None,
                 next_token=None, directory_id=None):
        self.region_id = region_id  # type: str
        self.directory_type = directory_type  # type: str
        self.directory_status = directory_status  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.directory_id = directory_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDirectoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.directory_status is not None:
            result['DirectoryStatus'] = self.directory_status
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('DirectoryStatus') is not None:
            self.directory_status = m.get('DirectoryStatus')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class DescribeDirectoriesResponseBodyDirectoriesADConnectors(TeaModel):
    def __init__(self, connector_status=None, v_switch_id=None, adconnector_address=None,
                 network_interface_id=None):
        self.connector_status = connector_status  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.adconnector_address = adconnector_address  # type: str
        self.network_interface_id = network_interface_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDirectoriesResponseBodyDirectoriesADConnectors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connector_status is not None:
            result['ConnectorStatus'] = self.connector_status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.adconnector_address is not None:
            result['ADConnectorAddress'] = self.adconnector_address
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectorStatus') is not None:
            self.connector_status = m.get('ConnectorStatus')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ADConnectorAddress') is not None:
            self.adconnector_address = m.get('ADConnectorAddress')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        return self


class DescribeDirectoriesResponseBodyDirectoriesLogs(TeaModel):
    def __init__(self, step=None, message=None, time_stamp=None, level=None):
        self.step = step  # type: str
        self.message = message  # type: str
        self.time_stamp = time_stamp  # type: str
        self.level = level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDirectoriesResponseBodyDirectoriesLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.step is not None:
            result['Step'] = self.step
        if self.message is not None:
            result['Message'] = self.message
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class DescribeDirectoriesResponseBodyDirectories(TeaModel):
    def __init__(self, enable_internet_access=None, vpc_id=None, creation_time=None, status=None,
                 domain_password=None, enable_admin_access=None, sub_domain_name=None, domain_user_name=None,
                 enable_cross_desktop_access=None, custom_security_group_id=None, desktop_vpc_endpoint=None, sso_enabled=None,
                 domain_name=None, desktop_access_type=None, mfa_enabled=None, directory_type=None, dns_user_name=None,
                 trust_password=None, name=None, directory_id=None, adconnectors=None, logs=None, v_switch_ids=None,
                 file_system_ids=None, sub_dns_address=None, dns_address=None):
        self.enable_internet_access = enable_internet_access  # type: bool
        self.vpc_id = vpc_id  # type: str
        self.creation_time = creation_time  # type: str
        self.status = status  # type: str
        self.domain_password = domain_password  # type: str
        self.enable_admin_access = enable_admin_access  # type: bool
        self.sub_domain_name = sub_domain_name  # type: str
        self.domain_user_name = domain_user_name  # type: str
        self.enable_cross_desktop_access = enable_cross_desktop_access  # type: bool
        self.custom_security_group_id = custom_security_group_id  # type: str
        self.desktop_vpc_endpoint = desktop_vpc_endpoint  # type: str
        self.sso_enabled = sso_enabled  # type: bool
        self.domain_name = domain_name  # type: str
        self.desktop_access_type = desktop_access_type  # type: str
        self.mfa_enabled = mfa_enabled  # type: bool
        self.directory_type = directory_type  # type: str
        self.dns_user_name = dns_user_name  # type: str
        self.trust_password = trust_password  # type: str
        self.name = name  # type: str
        self.directory_id = directory_id  # type: str
        self.adconnectors = adconnectors  # type: list[DescribeDirectoriesResponseBodyDirectoriesADConnectors]
        self.logs = logs  # type: list[DescribeDirectoriesResponseBodyDirectoriesLogs]
        self.v_switch_ids = v_switch_ids  # type: list[str]
        self.file_system_ids = file_system_ids  # type: list[str]
        self.sub_dns_address = sub_dns_address  # type: list[str]
        self.dns_address = dns_address  # type: list[str]

    def validate(self):
        if self.adconnectors:
            for k in self.adconnectors:
                if k:
                    k.validate()
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDirectoriesResponseBodyDirectories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.enable_cross_desktop_access is not None:
            result['EnableCrossDesktopAccess'] = self.enable_cross_desktop_access
        if self.custom_security_group_id is not None:
            result['CustomSecurityGroupId'] = self.custom_security_group_id
        if self.desktop_vpc_endpoint is not None:
            result['DesktopVpcEndpoint'] = self.desktop_vpc_endpoint
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.dns_user_name is not None:
            result['DnsUserName'] = self.dns_user_name
        if self.trust_password is not None:
            result['TrustPassword'] = self.trust_password
        if self.name is not None:
            result['Name'] = self.name
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        result['ADConnectors'] = []
        if self.adconnectors is not None:
            for k in self.adconnectors:
                result['ADConnectors'].append(k.to_map() if k else None)
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids
        if self.sub_dns_address is not None:
            result['SubDnsAddress'] = self.sub_dns_address
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('EnableCrossDesktopAccess') is not None:
            self.enable_cross_desktop_access = m.get('EnableCrossDesktopAccess')
        if m.get('CustomSecurityGroupId') is not None:
            self.custom_security_group_id = m.get('CustomSecurityGroupId')
        if m.get('DesktopVpcEndpoint') is not None:
            self.desktop_vpc_endpoint = m.get('DesktopVpcEndpoint')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('DnsUserName') is not None:
            self.dns_user_name = m.get('DnsUserName')
        if m.get('TrustPassword') is not None:
            self.trust_password = m.get('TrustPassword')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        self.adconnectors = []
        if m.get('ADConnectors') is not None:
            for k in m.get('ADConnectors'):
                temp_model = DescribeDirectoriesResponseBodyDirectoriesADConnectors()
                self.adconnectors.append(temp_model.from_map(k))
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = DescribeDirectoriesResponseBodyDirectoriesLogs()
                self.logs.append(temp_model.from_map(k))
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')
        if m.get('SubDnsAddress') is not None:
            self.sub_dns_address = m.get('SubDnsAddress')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        return self


class DescribeDirectoriesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, directories=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.directories = directories  # type: list[DescribeDirectoriesResponseBodyDirectories]

    def validate(self):
        if self.directories:
            for k in self.directories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDirectoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Directories'] = []
        if self.directories is not None:
            for k in self.directories:
                result['Directories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.directories = []
        if m.get('Directories') is not None:
            for k in m.get('Directories'):
                temp_model = DescribeDirectoriesResponseBodyDirectories()
                self.directories.append(temp_model.from_map(k))
        return self


class DescribeDirectoriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeDirectoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDirectoriesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFrontVulPatchListRequestVulInfo(TeaModel):
    def __init__(self, desktop_id=None, tag=None, name=None):
        self.desktop_id = desktop_id  # type: str
        self.tag = tag  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFrontVulPatchListRequestVulInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeFrontVulPatchListRequest(TeaModel):
    def __init__(self, region_id=None, operate_type=None, type=None, vul_info=None):
        self.region_id = region_id  # type: str
        self.operate_type = operate_type  # type: str
        self.type = type  # type: str
        self.vul_info = vul_info  # type: list[DescribeFrontVulPatchListRequestVulInfo]

    def validate(self):
        if self.vul_info:
            for k in self.vul_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFrontVulPatchListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.type is not None:
            result['Type'] = self.type
        result['VulInfo'] = []
        if self.vul_info is not None:
            for k in self.vul_info:
                result['VulInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        self.vul_info = []
        if m.get('VulInfo') is not None:
            for k in m.get('VulInfo'):
                temp_model = DescribeFrontVulPatchListRequestVulInfo()
                self.vul_info.append(temp_model.from_map(k))
        return self


class DescribeFrontVulPatchListResponseBodyFrontPatchListPatchList(TeaModel):
    def __init__(self, name=None, alias_name=None):
        self.name = name  # type: str
        self.alias_name = alias_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFrontVulPatchListResponseBodyFrontPatchListPatchList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        return self


class DescribeFrontVulPatchListResponseBodyFrontPatchList(TeaModel):
    def __init__(self, desktop_id=None, patch_list=None):
        self.desktop_id = desktop_id  # type: str
        self.patch_list = patch_list  # type: list[DescribeFrontVulPatchListResponseBodyFrontPatchListPatchList]

    def validate(self):
        if self.patch_list:
            for k in self.patch_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFrontVulPatchListResponseBodyFrontPatchList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        result['PatchList'] = []
        if self.patch_list is not None:
            for k in self.patch_list:
                result['PatchList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        self.patch_list = []
        if m.get('PatchList') is not None:
            for k in m.get('PatchList'):
                temp_model = DescribeFrontVulPatchListResponseBodyFrontPatchListPatchList()
                self.patch_list.append(temp_model.from_map(k))
        return self


class DescribeFrontVulPatchListResponseBody(TeaModel):
    def __init__(self, request_id=None, front_patch_list=None):
        self.request_id = request_id  # type: str
        self.front_patch_list = front_patch_list  # type: list[DescribeFrontVulPatchListResponseBodyFrontPatchList]

    def validate(self):
        if self.front_patch_list:
            for k in self.front_patch_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFrontVulPatchListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['FrontPatchList'] = []
        if self.front_patch_list is not None:
            for k in self.front_patch_list:
                result['FrontPatchList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.front_patch_list = []
        if m.get('FrontPatchList') is not None:
            for k in m.get('FrontPatchList'):
                temp_model = DescribeFrontVulPatchListResponseBodyFrontPatchList()
                self.front_patch_list.append(temp_model.from_map(k))
        return self


class DescribeFrontVulPatchListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeFrontVulPatchListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFrontVulPatchListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFrontVulPatchListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupedVulRequest(TeaModel):
    def __init__(self, region_id=None, lang=None, type=None, office_site_id=None, necessity=None, dealed=None,
                 current_page=None, page_size=None):
        self.region_id = region_id  # type: str
        self.lang = lang  # type: str
        self.type = type  # type: str
        self.office_site_id = office_site_id  # type: str
        self.necessity = necessity  # type: str
        self.dealed = dealed  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGroupedVulRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.type is not None:
            result['Type'] = self.type
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeGroupedVulResponseBodyGroupedVulItems(TeaModel):
    def __init__(self, type=None, nntf_count=None, handled_count=None, gmt_last=None, tags=None, later_count=None,
                 alias_name=None, name=None, asap_count=None):
        self.type = type  # type: str
        self.nntf_count = nntf_count  # type: int
        self.handled_count = handled_count  # type: int
        self.gmt_last = gmt_last  # type: str
        self.tags = tags  # type: str
        self.later_count = later_count  # type: int
        self.alias_name = alias_name  # type: str
        self.name = name  # type: str
        self.asap_count = asap_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGroupedVulResponseBodyGroupedVulItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.nntf_count is not None:
            result['NntfCount'] = self.nntf_count
        if self.handled_count is not None:
            result['HandledCount'] = self.handled_count
        if self.gmt_last is not None:
            result['GmtLast'] = self.gmt_last
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.later_count is not None:
            result['LaterCount'] = self.later_count
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.name is not None:
            result['Name'] = self.name
        if self.asap_count is not None:
            result['AsapCount'] = self.asap_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('NntfCount') is not None:
            self.nntf_count = m.get('NntfCount')
        if m.get('HandledCount') is not None:
            self.handled_count = m.get('HandledCount')
        if m.get('GmtLast') is not None:
            self.gmt_last = m.get('GmtLast')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('LaterCount') is not None:
            self.later_count = m.get('LaterCount')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AsapCount') is not None:
            self.asap_count = m.get('AsapCount')
        return self


class DescribeGroupedVulResponseBody(TeaModel):
    def __init__(self, current_page=None, request_id=None, page_size=None, total_count=None, grouped_vul_items=None):
        self.current_page = current_page  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.grouped_vul_items = grouped_vul_items  # type: list[DescribeGroupedVulResponseBodyGroupedVulItems]

    def validate(self):
        if self.grouped_vul_items:
            for k in self.grouped_vul_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGroupedVulResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['GroupedVulItems'] = []
        if self.grouped_vul_items is not None:
            for k in self.grouped_vul_items:
                result['GroupedVulItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.grouped_vul_items = []
        if m.get('GroupedVulItems') is not None:
            for k in m.get('GroupedVulItems'):
                temp_model = DescribeGroupedVulResponseBodyGroupedVulItems()
                self.grouped_vul_items.append(temp_model.from_map(k))
        return self


class DescribeGroupedVulResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeGroupedVulResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGroupedVulResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeGroupedVulResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImagesRequest(TeaModel):
    def __init__(self, region_id=None, max_results=None, next_token=None, image_type=None, image_status=None,
                 gpu_category=None, protocol_type=None, image_id=None):
        self.region_id = region_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.image_type = image_type  # type: str
        self.image_status = image_status  # type: str
        self.gpu_category = gpu_category  # type: bool
        self.protocol_type = protocol_type  # type: str
        self.image_id = image_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_status is not None:
            result['ImageStatus'] = self.image_status
        if self.gpu_category is not None:
            result['GpuCategory'] = self.gpu_category
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageStatus') is not None:
            self.image_status = m.get('ImageStatus')
        if m.get('GpuCategory') is not None:
            self.gpu_category = m.get('GpuCategory')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class DescribeImagesResponseBodyImages(TeaModel):
    def __init__(self, creation_time=None, status=None, progress=None, data_disk_size=None, image_type=None,
                 description=None, size=None, os_type=None, protocol_type=None, name=None, image_id=None, gpu_category=None):
        self.creation_time = creation_time  # type: str
        self.status = status  # type: str
        self.progress = progress  # type: str
        self.data_disk_size = data_disk_size  # type: int
        self.image_type = image_type  # type: str
        self.description = description  # type: str
        self.size = size  # type: int
        self.os_type = os_type  # type: str
        self.protocol_type = protocol_type  # type: str
        self.name = name  # type: str
        self.image_id = image_id  # type: str
        self.gpu_category = gpu_category  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImagesResponseBodyImages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.description is not None:
            result['Description'] = self.description
        if self.size is not None:
            result['Size'] = self.size
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.name is not None:
            result['Name'] = self.name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.gpu_category is not None:
            result['GpuCategory'] = self.gpu_category
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('GpuCategory') is not None:
            self.gpu_category = m.get('GpuCategory')
        return self


class DescribeImagesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, images=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.images = images  # type: list[DescribeImagesResponseBodyImages]

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeImagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = DescribeImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        return self


class DescribeImagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeImagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeImagesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInvocationsRequest(TeaModel):
    def __init__(self, region_id=None, invoke_id=None, command_type=None, invoke_status=None, desktop_id=None,
                 include_output=None, content_encoding=None, max_results=None, next_token=None):
        self.region_id = region_id  # type: str
        self.invoke_id = invoke_id  # type: str
        self.command_type = command_type  # type: str
        self.invoke_status = invoke_status  # type: str
        self.desktop_id = desktop_id  # type: str
        self.include_output = include_output  # type: bool
        self.content_encoding = content_encoding  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInvocationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.command_type is not None:
            result['CommandType'] = self.command_type
        if self.invoke_status is not None:
            result['InvokeStatus'] = self.invoke_status
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.include_output is not None:
            result['IncludeOutput'] = self.include_output
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')
        if m.get('InvokeStatus') is not None:
            self.invoke_status = m.get('InvokeStatus')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('IncludeOutput') is not None:
            self.include_output = m.get('IncludeOutput')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeInvocationsResponseBodyInvocationsInvokeDesktops(TeaModel):
    def __init__(self, creation_time=None, invocation_status=None, finish_time=None, update_time=None, repeats=None,
                 desktop_id=None, output=None, dropped=None, stop_time=None, exit_code=None, start_time=None, error_info=None,
                 error_code=None):
        self.creation_time = creation_time  # type: str
        self.invocation_status = invocation_status  # type: str
        self.finish_time = finish_time  # type: str
        self.update_time = update_time  # type: str
        self.repeats = repeats  # type: int
        self.desktop_id = desktop_id  # type: str
        self.output = output  # type: str
        self.dropped = dropped  # type: int
        self.stop_time = stop_time  # type: str
        self.exit_code = exit_code  # type: long
        self.start_time = start_time  # type: str
        self.error_info = error_info  # type: str
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInvocationsResponseBodyInvocationsInvokeDesktops, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.repeats is not None:
            result['Repeats'] = self.repeats
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.output is not None:
            result['Output'] = self.output
        if self.dropped is not None:
            result['Dropped'] = self.dropped
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Repeats') is not None:
            self.repeats = m.get('Repeats')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Dropped') is not None:
            self.dropped = m.get('Dropped')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DescribeInvocationsResponseBodyInvocations(TeaModel):
    def __init__(self, creation_time=None, invocation_status=None, invoke_id=None, command_type=None,
                 command_content=None, invoke_desktops=None):
        self.creation_time = creation_time  # type: str
        self.invocation_status = invocation_status  # type: str
        self.invoke_id = invoke_id  # type: str
        self.command_type = command_type  # type: str
        self.command_content = command_content  # type: str
        self.invoke_desktops = invoke_desktops  # type: list[DescribeInvocationsResponseBodyInvocationsInvokeDesktops]

    def validate(self):
        if self.invoke_desktops:
            for k in self.invoke_desktops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInvocationsResponseBodyInvocations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.command_type is not None:
            result['CommandType'] = self.command_type
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        result['InvokeDesktops'] = []
        if self.invoke_desktops is not None:
            for k in self.invoke_desktops:
                result['InvokeDesktops'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        self.invoke_desktops = []
        if m.get('InvokeDesktops') is not None:
            for k in m.get('InvokeDesktops'):
                temp_model = DescribeInvocationsResponseBodyInvocationsInvokeDesktops()
                self.invoke_desktops.append(temp_model.from_map(k))
        return self


class DescribeInvocationsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, invocations=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.invocations = invocations  # type: list[DescribeInvocationsResponseBodyInvocations]

    def validate(self):
        if self.invocations:
            for k in self.invocations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInvocationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Invocations'] = []
        if self.invocations is not None:
            for k in self.invocations:
                result['Invocations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.invocations = []
        if m.get('Invocations') is not None:
            for k in m.get('Invocations'):
                temp_model = DescribeInvocationsResponseBodyInvocations()
                self.invocations.append(temp_model.from_map(k))
        return self


class DescribeInvocationsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInvocationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInvocationsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInvocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeModificationPriceRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, instance_type=None, root_disk_size_gib=None,
                 user_disk_size_gib=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.root_disk_size_gib = root_disk_size_gib  # type: int
        self.user_disk_size_gib = user_disk_size_gib  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeModificationPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.root_disk_size_gib is not None:
            result['RootDiskSizeGib'] = self.root_disk_size_gib
        if self.user_disk_size_gib is not None:
            result['UserDiskSizeGib'] = self.user_disk_size_gib
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RootDiskSizeGib') is not None:
            self.root_disk_size_gib = m.get('RootDiskSizeGib')
        if m.get('UserDiskSizeGib') is not None:
            self.user_disk_size_gib = m.get('UserDiskSizeGib')
        return self


class DescribeModificationPriceResponseBodyPriceInfoRules(TeaModel):
    def __init__(self, description=None, rule_id=None):
        self.description = description  # type: str
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeModificationPriceResponseBodyPriceInfoRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeModificationPriceResponseBodyPriceInfoPricePromotions(TeaModel):
    def __init__(self, promotion_desc=None, option_code=None, selected=None, promotion_id=None, promotion_name=None):
        self.promotion_desc = promotion_desc  # type: str
        self.option_code = option_code  # type: str
        self.selected = selected  # type: bool
        self.promotion_id = promotion_id  # type: str
        self.promotion_name = promotion_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeModificationPriceResponseBodyPriceInfoPricePromotions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.option_code is not None:
            result['OptionCode'] = self.option_code
        if self.selected is not None:
            result['Selected'] = self.selected
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        return self


class DescribeModificationPriceResponseBodyPriceInfoPrice(TeaModel):
    def __init__(self, original_price=None, discount_price=None, currency=None, trade_price=None, promotions=None):
        self.original_price = original_price  # type: float
        self.discount_price = discount_price  # type: float
        self.currency = currency  # type: str
        self.trade_price = trade_price  # type: float
        self.promotions = promotions  # type: list[DescribeModificationPriceResponseBodyPriceInfoPricePromotions]

    def validate(self):
        if self.promotions:
            for k in self.promotions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeModificationPriceResponseBodyPriceInfoPrice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        result['Promotions'] = []
        if self.promotions is not None:
            for k in self.promotions:
                result['Promotions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        self.promotions = []
        if m.get('Promotions') is not None:
            for k in m.get('Promotions'):
                temp_model = DescribeModificationPriceResponseBodyPriceInfoPricePromotions()
                self.promotions.append(temp_model.from_map(k))
        return self


class DescribeModificationPriceResponseBodyPriceInfo(TeaModel):
    def __init__(self, rules=None, price=None):
        self.rules = rules  # type: list[DescribeModificationPriceResponseBodyPriceInfoRules]
        self.price = price  # type: DescribeModificationPriceResponseBodyPriceInfoPrice

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()
        if self.price:
            self.price.validate()

    def to_map(self):
        _map = super(DescribeModificationPriceResponseBodyPriceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.price is not None:
            result['Price'] = self.price.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeModificationPriceResponseBodyPriceInfoRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('Price') is not None:
            temp_model = DescribeModificationPriceResponseBodyPriceInfoPrice()
            self.price = temp_model.from_map(m['Price'])
        return self


class DescribeModificationPriceResponseBody(TeaModel):
    def __init__(self, request_id=None, price_info=None):
        self.request_id = request_id  # type: str
        self.price_info = price_info  # type: DescribeModificationPriceResponseBodyPriceInfo

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        _map = super(DescribeModificationPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PriceInfo') is not None:
            temp_model = DescribeModificationPriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m['PriceInfo'])
        return self


class DescribeModificationPriceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeModificationPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeModificationPriceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeModificationPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNASFileSystemsRequest(TeaModel):
    def __init__(self, region_id=None, office_site_id=None, max_results=None, next_token=None, file_system_id=None):
        self.region_id = region_id  # type: str
        self.office_site_id = office_site_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.file_system_id = file_system_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNASFileSystemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DescribeNASFileSystemsResponseBodyFileSystems(TeaModel):
    def __init__(self, capacity=None, mount_target_status=None, create_time=None, office_site_id=None,
                 support_acl=None, storage_type=None, office_site_name=None, region_id=None, file_system_id=None,
                 file_system_type=None, file_system_name=None, metered_size=None, mount_target_domain=None, description=None,
                 zone_id=None, file_system_status=None):
        self.capacity = capacity  # type: long
        self.mount_target_status = mount_target_status  # type: str
        self.create_time = create_time  # type: str
        self.office_site_id = office_site_id  # type: str
        self.support_acl = support_acl  # type: bool
        self.storage_type = storage_type  # type: str
        self.office_site_name = office_site_name  # type: str
        self.region_id = region_id  # type: str
        self.file_system_id = file_system_id  # type: str
        self.file_system_type = file_system_type  # type: str
        self.file_system_name = file_system_name  # type: str
        self.metered_size = metered_size  # type: long
        self.mount_target_domain = mount_target_domain  # type: str
        self.description = description  # type: str
        self.zone_id = zone_id  # type: str
        self.file_system_status = file_system_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNASFileSystemsResponseBodyFileSystems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.mount_target_status is not None:
            result['MountTargetStatus'] = self.mount_target_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.support_acl is not None:
            result['SupportAcl'] = self.support_acl
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name
        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.description is not None:
            result['Description'] = self.description
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.file_system_status is not None:
            result['FileSystemStatus'] = self.file_system_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('MountTargetStatus') is not None:
            self.mount_target_status = m.get('MountTargetStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('SupportAcl') is not None:
            self.support_acl = m.get('SupportAcl')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')
        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('FileSystemStatus') is not None:
            self.file_system_status = m.get('FileSystemStatus')
        return self


class DescribeNASFileSystemsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, file_systems=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.file_systems = file_systems  # type: list[DescribeNASFileSystemsResponseBodyFileSystems]

    def validate(self):
        if self.file_systems:
            for k in self.file_systems:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeNASFileSystemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['FileSystems'] = []
        if self.file_systems is not None:
            for k in self.file_systems:
                result['FileSystems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.file_systems = []
        if m.get('FileSystems') is not None:
            for k in m.get('FileSystems'):
                temp_model = DescribeNASFileSystemsResponseBodyFileSystems()
                self.file_systems.append(temp_model.from_map(k))
        return self


class DescribeNASFileSystemsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeNASFileSystemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNASFileSystemsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNASFileSystemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNetworkPackagesRequest(TeaModel):
    def __init__(self, region_id=None, max_results=None, next_token=None, network_package_id=None):
        self.region_id = region_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.network_package_id = network_package_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNetworkPackagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        return self


class DescribeNetworkPackagesResponseBodyNetworkPackages(TeaModel):
    def __init__(self, network_package_id=None, bandwidth=None, expired_time=None, create_time=None,
                 office_site_id=None, internet_charge_type=None, network_package_status=None, office_site_name=None,
                 eip_addresses=None):
        self.network_package_id = network_package_id  # type: str
        self.bandwidth = bandwidth  # type: int
        self.expired_time = expired_time  # type: str
        self.create_time = create_time  # type: str
        self.office_site_id = office_site_id  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.network_package_status = network_package_status  # type: str
        self.office_site_name = office_site_name  # type: str
        self.eip_addresses = eip_addresses  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNetworkPackagesResponseBodyNetworkPackages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.network_package_status is not None:
            result['NetworkPackageStatus'] = self.network_package_status
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.eip_addresses is not None:
            result['EipAddresses'] = self.eip_addresses
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('NetworkPackageStatus') is not None:
            self.network_package_status = m.get('NetworkPackageStatus')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('EipAddresses') is not None:
            self.eip_addresses = m.get('EipAddresses')
        return self


class DescribeNetworkPackagesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, network_packages=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.network_packages = network_packages  # type: list[DescribeNetworkPackagesResponseBodyNetworkPackages]

    def validate(self):
        if self.network_packages:
            for k in self.network_packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeNetworkPackagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['NetworkPackages'] = []
        if self.network_packages is not None:
            for k in self.network_packages:
                result['NetworkPackages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.network_packages = []
        if m.get('NetworkPackages') is not None:
            for k in m.get('NetworkPackages'):
                temp_model = DescribeNetworkPackagesResponseBodyNetworkPackages()
                self.network_packages.append(temp_model.from_map(k))
        return self


class DescribeNetworkPackagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeNetworkPackagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNetworkPackagesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNetworkPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOfficeSitesRequest(TeaModel):
    def __init__(self, region_id=None, office_site_type=None, max_results=None, next_token=None,
                 office_site_id=None):
        self.region_id = region_id  # type: str
        self.office_site_type = office_site_type  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.office_site_id = office_site_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOfficeSitesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class DescribeOfficeSitesResponseBodyOfficeSitesADConnectors(TeaModel):
    def __init__(self, connector_status=None, v_switch_id=None, adconnector_address=None,
                 network_interface_id=None):
        self.connector_status = connector_status  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.adconnector_address = adconnector_address  # type: str
        self.network_interface_id = network_interface_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOfficeSitesResponseBodyOfficeSitesADConnectors, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connector_status is not None:
            result['ConnectorStatus'] = self.connector_status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.adconnector_address is not None:
            result['ADConnectorAddress'] = self.adconnector_address
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectorStatus') is not None:
            self.connector_status = m.get('ConnectorStatus')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ADConnectorAddress') is not None:
            self.adconnector_address = m.get('ADConnectorAddress')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        return self


class DescribeOfficeSitesResponseBodyOfficeSitesLogs(TeaModel):
    def __init__(self, step=None, message=None, time_stamp=None, level=None):
        self.step = step  # type: str
        self.message = message  # type: str
        self.time_stamp = time_stamp  # type: str
        self.level = level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOfficeSitesResponseBodyOfficeSitesLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.step is not None:
            result['Step'] = self.step
        if self.message is not None:
            result['Message'] = self.message
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class DescribeOfficeSitesResponseBodyOfficeSites(TeaModel):
    def __init__(self, status=None, creation_time=None, vpc_id=None, enable_admin_access=None,
                 enable_cross_desktop_access=None, desktop_vpc_endpoint=None, desktop_access_type=None, domain_name=None, sso_enabled=None,
                 cidr_block=None, bandwidth=None, trust_password=None, name=None, enable_internet_access=None,
                 domain_password=None, custom_security_group_id=None, domain_user_name=None, sub_domain_name=None,
                 office_site_id=None, cen_id=None, mfa_enabled=None, network_package_id=None, dns_user_name=None,
                 office_site_type=None, adconnectors=None, logs=None, v_switch_ids=None, file_system_ids=None, sub_dns_address=None,
                 dns_address=None):
        self.status = status  # type: str
        self.creation_time = creation_time  # type: str
        self.vpc_id = vpc_id  # type: str
        self.enable_admin_access = enable_admin_access  # type: bool
        self.enable_cross_desktop_access = enable_cross_desktop_access  # type: bool
        self.desktop_vpc_endpoint = desktop_vpc_endpoint  # type: str
        self.desktop_access_type = desktop_access_type  # type: str
        self.domain_name = domain_name  # type: str
        self.sso_enabled = sso_enabled  # type: bool
        self.cidr_block = cidr_block  # type: str
        self.bandwidth = bandwidth  # type: int
        self.trust_password = trust_password  # type: str
        self.name = name  # type: str
        self.enable_internet_access = enable_internet_access  # type: bool
        self.domain_password = domain_password  # type: str
        self.custom_security_group_id = custom_security_group_id  # type: str
        self.domain_user_name = domain_user_name  # type: str
        self.sub_domain_name = sub_domain_name  # type: str
        self.office_site_id = office_site_id  # type: str
        self.cen_id = cen_id  # type: str
        self.mfa_enabled = mfa_enabled  # type: bool
        self.network_package_id = network_package_id  # type: str
        self.dns_user_name = dns_user_name  # type: str
        self.office_site_type = office_site_type  # type: str
        self.adconnectors = adconnectors  # type: list[DescribeOfficeSitesResponseBodyOfficeSitesADConnectors]
        self.logs = logs  # type: list[DescribeOfficeSitesResponseBodyOfficeSitesLogs]
        self.v_switch_ids = v_switch_ids  # type: list[str]
        self.file_system_ids = file_system_ids  # type: list[str]
        self.sub_dns_address = sub_dns_address  # type: list[str]
        self.dns_address = dns_address  # type: list[str]

    def validate(self):
        if self.adconnectors:
            for k in self.adconnectors:
                if k:
                    k.validate()
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOfficeSitesResponseBodyOfficeSites, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.enable_cross_desktop_access is not None:
            result['EnableCrossDesktopAccess'] = self.enable_cross_desktop_access
        if self.desktop_vpc_endpoint is not None:
            result['DesktopVpcEndpoint'] = self.desktop_vpc_endpoint
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.trust_password is not None:
            result['TrustPassword'] = self.trust_password
        if self.name is not None:
            result['Name'] = self.name
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.custom_security_group_id is not None:
            result['CustomSecurityGroupId'] = self.custom_security_group_id
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.dns_user_name is not None:
            result['DnsUserName'] = self.dns_user_name
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        result['ADConnectors'] = []
        if self.adconnectors is not None:
            for k in self.adconnectors:
                result['ADConnectors'].append(k.to_map() if k else None)
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids
        if self.sub_dns_address is not None:
            result['SubDnsAddress'] = self.sub_dns_address
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('EnableCrossDesktopAccess') is not None:
            self.enable_cross_desktop_access = m.get('EnableCrossDesktopAccess')
        if m.get('DesktopVpcEndpoint') is not None:
            self.desktop_vpc_endpoint = m.get('DesktopVpcEndpoint')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('TrustPassword') is not None:
            self.trust_password = m.get('TrustPassword')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('CustomSecurityGroupId') is not None:
            self.custom_security_group_id = m.get('CustomSecurityGroupId')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('DnsUserName') is not None:
            self.dns_user_name = m.get('DnsUserName')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        self.adconnectors = []
        if m.get('ADConnectors') is not None:
            for k in m.get('ADConnectors'):
                temp_model = DescribeOfficeSitesResponseBodyOfficeSitesADConnectors()
                self.adconnectors.append(temp_model.from_map(k))
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = DescribeOfficeSitesResponseBodyOfficeSitesLogs()
                self.logs.append(temp_model.from_map(k))
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')
        if m.get('SubDnsAddress') is not None:
            self.sub_dns_address = m.get('SubDnsAddress')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        return self


class DescribeOfficeSitesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, office_sites=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.office_sites = office_sites  # type: list[DescribeOfficeSitesResponseBodyOfficeSites]

    def validate(self):
        if self.office_sites:
            for k in self.office_sites:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOfficeSitesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['OfficeSites'] = []
        if self.office_sites is not None:
            for k in self.office_sites:
                result['OfficeSites'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.office_sites = []
        if m.get('OfficeSites') is not None:
            for k in m.get('OfficeSites'):
                temp_model = DescribeOfficeSitesResponseBodyOfficeSites()
                self.office_sites.append(temp_model.from_map(k))
        return self


class DescribeOfficeSitesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeOfficeSitesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOfficeSitesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeOfficeSitesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyGroupsRequest(TeaModel):
    def __init__(self, region_id=None, max_results=None, next_token=None, policy_group_id=None):
        self.region_id = region_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.policy_group_id = policy_group_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        return self


class DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeSecurityPolicyRules(TeaModel):
    def __init__(self, type=None, policy=None, description=None, port_range=None, ip_protocol=None, priority=None,
                 cidr_ip=None):
        self.type = type  # type: str
        self.policy = policy  # type: str
        self.description = description  # type: str
        self.port_range = port_range  # type: str
        self.ip_protocol = ip_protocol  # type: str
        self.priority = priority  # type: str
        self.cidr_ip = cidr_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeSecurityPolicyRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.description is not None:
            result['Description'] = self.description
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        return self


class DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeAccessPolicyRules(TeaModel):
    def __init__(self, description=None, cidr_ip=None):
        self.description = description  # type: str
        self.cidr_ip = cidr_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeAccessPolicyRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        return self


class DescribePolicyGroupsResponseBodyDescribePolicyGroups(TeaModel):
    def __init__(self, policy_status=None, html_5access=None, watermark_type=None, preempt_login=None,
                 watermark_custom_text=None, clipboard=None, domain_list=None, policy_group_id=None, watermark_transparency=None,
                 html_5file_transfer=None, usb_redirect=None, policy_group_type=None, watermark=None, visual_quality=None,
                 eds_count=None, name=None, local_drive=None, authorize_security_policy_rules=None,
                 authorize_access_policy_rules=None, preempt_login_users=None):
        self.policy_status = policy_status  # type: str
        self.html_5access = html_5access  # type: str
        self.watermark_type = watermark_type  # type: str
        self.preempt_login = preempt_login  # type: str
        self.watermark_custom_text = watermark_custom_text  # type: str
        self.clipboard = clipboard  # type: str
        self.domain_list = domain_list  # type: str
        self.policy_group_id = policy_group_id  # type: str
        self.watermark_transparency = watermark_transparency  # type: str
        self.html_5file_transfer = html_5file_transfer  # type: str
        self.usb_redirect = usb_redirect  # type: str
        self.policy_group_type = policy_group_type  # type: str
        self.watermark = watermark  # type: str
        self.visual_quality = visual_quality  # type: str
        self.eds_count = eds_count  # type: int
        self.name = name  # type: str
        self.local_drive = local_drive  # type: str
        self.authorize_security_policy_rules = authorize_security_policy_rules  # type: list[DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeSecurityPolicyRules]
        self.authorize_access_policy_rules = authorize_access_policy_rules  # type: list[DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeAccessPolicyRules]
        self.preempt_login_users = preempt_login_users  # type: list[str]

    def validate(self):
        if self.authorize_security_policy_rules:
            for k in self.authorize_security_policy_rules:
                if k:
                    k.validate()
        if self.authorize_access_policy_rules:
            for k in self.authorize_access_policy_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePolicyGroupsResponseBodyDescribePolicyGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status
        if self.html_5access is not None:
            result['Html5Access'] = self.html_5access
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        if self.preempt_login is not None:
            result['PreemptLogin'] = self.preempt_login
        if self.watermark_custom_text is not None:
            result['WatermarkCustomText'] = self.watermark_custom_text
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.watermark_transparency is not None:
            result['WatermarkTransparency'] = self.watermark_transparency
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.policy_group_type is not None:
            result['PolicyGroupType'] = self.policy_group_type
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.visual_quality is not None:
            result['VisualQuality'] = self.visual_quality
        if self.eds_count is not None:
            result['EdsCount'] = self.eds_count
        if self.name is not None:
            result['Name'] = self.name
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        result['AuthorizeSecurityPolicyRules'] = []
        if self.authorize_security_policy_rules is not None:
            for k in self.authorize_security_policy_rules:
                result['AuthorizeSecurityPolicyRules'].append(k.to_map() if k else None)
        result['AuthorizeAccessPolicyRules'] = []
        if self.authorize_access_policy_rules is not None:
            for k in self.authorize_access_policy_rules:
                result['AuthorizeAccessPolicyRules'].append(k.to_map() if k else None)
        if self.preempt_login_users is not None:
            result['PreemptLoginUsers'] = self.preempt_login_users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')
        if m.get('Html5Access') is not None:
            self.html_5access = m.get('Html5Access')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        if m.get('PreemptLogin') is not None:
            self.preempt_login = m.get('PreemptLogin')
        if m.get('WatermarkCustomText') is not None:
            self.watermark_custom_text = m.get('WatermarkCustomText')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('WatermarkTransparency') is not None:
            self.watermark_transparency = m.get('WatermarkTransparency')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('PolicyGroupType') is not None:
            self.policy_group_type = m.get('PolicyGroupType')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('VisualQuality') is not None:
            self.visual_quality = m.get('VisualQuality')
        if m.get('EdsCount') is not None:
            self.eds_count = m.get('EdsCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        self.authorize_security_policy_rules = []
        if m.get('AuthorizeSecurityPolicyRules') is not None:
            for k in m.get('AuthorizeSecurityPolicyRules'):
                temp_model = DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeSecurityPolicyRules()
                self.authorize_security_policy_rules.append(temp_model.from_map(k))
        self.authorize_access_policy_rules = []
        if m.get('AuthorizeAccessPolicyRules') is not None:
            for k in m.get('AuthorizeAccessPolicyRules'):
                temp_model = DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeAccessPolicyRules()
                self.authorize_access_policy_rules.append(temp_model.from_map(k))
        if m.get('PreemptLoginUsers') is not None:
            self.preempt_login_users = m.get('PreemptLoginUsers')
        return self


class DescribePolicyGroupsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, describe_policy_groups=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.describe_policy_groups = describe_policy_groups  # type: list[DescribePolicyGroupsResponseBodyDescribePolicyGroups]

    def validate(self):
        if self.describe_policy_groups:
            for k in self.describe_policy_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePolicyGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DescribePolicyGroups'] = []
        if self.describe_policy_groups is not None:
            for k in self.describe_policy_groups:
                result['DescribePolicyGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.describe_policy_groups = []
        if m.get('DescribePolicyGroups') is not None:
            for k in m.get('DescribePolicyGroups'):
                temp_model = DescribePolicyGroupsResponseBodyDescribePolicyGroups()
                self.describe_policy_groups.append(temp_model.from_map(k))
        return self


class DescribePolicyGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePolicyGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePolicyGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePolicyGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePostPaidDesktopBillsRequest(TeaModel):
    def __init__(self, region_id=None, desktop_group_id=None, bill_start_time=None, bill_end_time=None,
                 max_results=None, next_token=None):
        self.region_id = region_id  # type: str
        self.desktop_group_id = desktop_group_id  # type: str
        self.bill_start_time = bill_start_time  # type: str
        self.bill_end_time = bill_end_time  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePostPaidDesktopBillsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.bill_start_time is not None:
            result['BillStartTime'] = self.bill_start_time
        if self.bill_end_time is not None:
            result['BillEndTime'] = self.bill_end_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('BillStartTime') is not None:
            self.bill_start_time = m.get('BillStartTime')
        if m.get('BillEndTime') is not None:
            self.bill_end_time = m.get('BillEndTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribePostPaidDesktopBillsResponseBodyBills(TeaModel):
    def __init__(self, bill_id=None, discount_price=None, product=None, price_unit=None, cash_payment=None,
                 payment=None, original_price=None, instance_id=None, product_detail=None, usage=None, gold_note=None,
                 usage_unit=None, price=None, bill_start_time=None, bill_type=None, resource_group_id=None, charge_item=None,
                 resource_group_name=None, consume_time=None, consume_type=None, bill_end_time=None):
        self.bill_id = bill_id  # type: str
        self.discount_price = discount_price  # type: str
        self.product = product  # type: str
        self.price_unit = price_unit  # type: str
        self.cash_payment = cash_payment  # type: str
        self.payment = payment  # type: str
        self.original_price = original_price  # type: str
        self.instance_id = instance_id  # type: str
        self.product_detail = product_detail  # type: str
        self.usage = usage  # type: str
        self.gold_note = gold_note  # type: str
        self.usage_unit = usage_unit  # type: str
        self.price = price  # type: str
        self.bill_start_time = bill_start_time  # type: str
        self.bill_type = bill_type  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.charge_item = charge_item  # type: str
        self.resource_group_name = resource_group_name  # type: str
        self.consume_time = consume_time  # type: str
        self.consume_type = consume_type  # type: str
        self.bill_end_time = bill_end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePostPaidDesktopBillsResponseBodyBills, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.product is not None:
            result['Product'] = self.product
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.cash_payment is not None:
            result['CashPayment'] = self.cash_payment
        if self.payment is not None:
            result['Payment'] = self.payment
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail
        if self.usage is not None:
            result['Usage'] = self.usage
        if self.gold_note is not None:
            result['GoldNote'] = self.gold_note
        if self.usage_unit is not None:
            result['UsageUnit'] = self.usage_unit
        if self.price is not None:
            result['Price'] = self.price
        if self.bill_start_time is not None:
            result['BillStartTime'] = self.bill_start_time
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.charge_item is not None:
            result['ChargeItem'] = self.charge_item
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        if self.consume_time is not None:
            result['ConsumeTime'] = self.consume_time
        if self.consume_type is not None:
            result['ConsumeType'] = self.consume_type
        if self.bill_end_time is not None:
            result['BillEndTime'] = self.bill_end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('CashPayment') is not None:
            self.cash_payment = m.get('CashPayment')
        if m.get('Payment') is not None:
            self.payment = m.get('Payment')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        if m.get('GoldNote') is not None:
            self.gold_note = m.get('GoldNote')
        if m.get('UsageUnit') is not None:
            self.usage_unit = m.get('UsageUnit')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('BillStartTime') is not None:
            self.bill_start_time = m.get('BillStartTime')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ChargeItem') is not None:
            self.charge_item = m.get('ChargeItem')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        if m.get('ConsumeTime') is not None:
            self.consume_time = m.get('ConsumeTime')
        if m.get('ConsumeType') is not None:
            self.consume_type = m.get('ConsumeType')
        if m.get('BillEndTime') is not None:
            self.bill_end_time = m.get('BillEndTime')
        return self


class DescribePostPaidDesktopBillsResponseBody(TeaModel):
    def __init__(self, post_paid_desktops_bills_url=None, post_paid_desktops_count=None, next_token=None,
                 request_id=None, post_paid_desktops_total_amount=None, bills=None):
        self.post_paid_desktops_bills_url = post_paid_desktops_bills_url  # type: str
        self.post_paid_desktops_count = post_paid_desktops_count  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.post_paid_desktops_total_amount = post_paid_desktops_total_amount  # type: float
        self.bills = bills  # type: list[DescribePostPaidDesktopBillsResponseBodyBills]

    def validate(self):
        if self.bills:
            for k in self.bills:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePostPaidDesktopBillsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.post_paid_desktops_bills_url is not None:
            result['PostPaidDesktopsBillsUrl'] = self.post_paid_desktops_bills_url
        if self.post_paid_desktops_count is not None:
            result['PostPaidDesktopsCount'] = self.post_paid_desktops_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.post_paid_desktops_total_amount is not None:
            result['PostPaidDesktopsTotalAmount'] = self.post_paid_desktops_total_amount
        result['Bills'] = []
        if self.bills is not None:
            for k in self.bills:
                result['Bills'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PostPaidDesktopsBillsUrl') is not None:
            self.post_paid_desktops_bills_url = m.get('PostPaidDesktopsBillsUrl')
        if m.get('PostPaidDesktopsCount') is not None:
            self.post_paid_desktops_count = m.get('PostPaidDesktopsCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PostPaidDesktopsTotalAmount') is not None:
            self.post_paid_desktops_total_amount = m.get('PostPaidDesktopsTotalAmount')
        self.bills = []
        if m.get('Bills') is not None:
            for k in m.get('Bills'):
                temp_model = DescribePostPaidDesktopBillsResponseBodyBills()
                self.bills.append(temp_model.from_map(k))
        return self


class DescribePostPaidDesktopBillsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePostPaidDesktopBillsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePostPaidDesktopBillsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePostPaidDesktopBillsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePriceRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, instance_type=None, root_disk_size_gib=None,
                 user_disk_size_gib=None, os_type=None, period_unit=None, period=None, amount=None, promotion_id=None,
                 internet_charge_type=None, bandwidth=None):
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.instance_type = instance_type  # type: str
        self.root_disk_size_gib = root_disk_size_gib  # type: int
        self.user_disk_size_gib = user_disk_size_gib  # type: int
        self.os_type = os_type  # type: str
        self.period_unit = period_unit  # type: str
        self.period = period  # type: int
        self.amount = amount  # type: int
        self.promotion_id = promotion_id  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.bandwidth = bandwidth  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.root_disk_size_gib is not None:
            result['RootDiskSizeGib'] = self.root_disk_size_gib
        if self.user_disk_size_gib is not None:
            result['UserDiskSizeGib'] = self.user_disk_size_gib
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period is not None:
            result['Period'] = self.period
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RootDiskSizeGib') is not None:
            self.root_disk_size_gib = m.get('RootDiskSizeGib')
        if m.get('UserDiskSizeGib') is not None:
            self.user_disk_size_gib = m.get('UserDiskSizeGib')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        return self


class DescribePriceResponseBodyPriceInfoRules(TeaModel):
    def __init__(self, description=None, rule_id=None):
        self.description = description  # type: str
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePriceResponseBodyPriceInfoRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribePriceResponseBodyPriceInfoPricePromotions(TeaModel):
    def __init__(self, promotion_desc=None, option_code=None, selected=None, promotion_id=None, promotion_name=None):
        self.promotion_desc = promotion_desc  # type: str
        self.option_code = option_code  # type: str
        self.selected = selected  # type: bool
        self.promotion_id = promotion_id  # type: str
        self.promotion_name = promotion_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePriceResponseBodyPriceInfoPricePromotions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.option_code is not None:
            result['OptionCode'] = self.option_code
        if self.selected is not None:
            result['Selected'] = self.selected
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        return self


class DescribePriceResponseBodyPriceInfoPrice(TeaModel):
    def __init__(self, original_price=None, discount_price=None, currency=None, trade_price=None, promotions=None):
        self.original_price = original_price  # type: float
        self.discount_price = discount_price  # type: float
        self.currency = currency  # type: str
        self.trade_price = trade_price  # type: float
        self.promotions = promotions  # type: list[DescribePriceResponseBodyPriceInfoPricePromotions]

    def validate(self):
        if self.promotions:
            for k in self.promotions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePriceResponseBodyPriceInfoPrice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        result['Promotions'] = []
        if self.promotions is not None:
            for k in self.promotions:
                result['Promotions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        self.promotions = []
        if m.get('Promotions') is not None:
            for k in m.get('Promotions'):
                temp_model = DescribePriceResponseBodyPriceInfoPricePromotions()
                self.promotions.append(temp_model.from_map(k))
        return self


class DescribePriceResponseBodyPriceInfo(TeaModel):
    def __init__(self, rules=None, price=None):
        self.rules = rules  # type: list[DescribePriceResponseBodyPriceInfoRules]
        self.price = price  # type: DescribePriceResponseBodyPriceInfoPrice

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()
        if self.price:
            self.price.validate()

    def to_map(self):
        _map = super(DescribePriceResponseBodyPriceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.price is not None:
            result['Price'] = self.price.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribePriceResponseBodyPriceInfoRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('Price') is not None:
            temp_model = DescribePriceResponseBodyPriceInfoPrice()
            self.price = temp_model.from_map(m['Price'])
        return self


class DescribePriceResponseBody(TeaModel):
    def __init__(self, request_id=None, price_info=None):
        self.request_id = request_id  # type: str
        self.price_info = price_info  # type: DescribePriceResponseBodyPriceInfo

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        _map = super(DescribePriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PriceInfo') is not None:
            temp_model = DescribePriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m['PriceInfo'])
        return self


class DescribePriceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribePriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePriceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region_endpoint=None, region_id=None):
        self.region_endpoint = region_endpoint  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, request_id=None, regions=None):
        self.request_id = request_id  # type: str
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScaleStrategysRequest(TeaModel):
    def __init__(self, region_id=None, scale_strategy_name=None, max_results=None, next_token=None):
        self.region_id = region_id  # type: str
        self.scale_strategy_name = scale_strategy_name  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeScaleStrategysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scale_strategy_name is not None:
            result['ScaleStrategyName'] = self.scale_strategy_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScaleStrategyName') is not None:
            self.scale_strategy_name = m.get('ScaleStrategyName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeScaleStrategysResponseBodyScaleStrategys(TeaModel):
    def __init__(self, scale_strategy_id=None, max_desktops_count=None, max_available_desktops_count=None,
                 scale_strategy_name=None, scale_strategy_type=None, min_desktops_count=None, min_available_desktops_count=None,
                 scale_step=None):
        self.scale_strategy_id = scale_strategy_id  # type: str
        self.max_desktops_count = max_desktops_count  # type: int
        self.max_available_desktops_count = max_available_desktops_count  # type: int
        self.scale_strategy_name = scale_strategy_name  # type: str
        self.scale_strategy_type = scale_strategy_type  # type: str
        self.min_desktops_count = min_desktops_count  # type: int
        self.min_available_desktops_count = min_available_desktops_count  # type: int
        self.scale_step = scale_step  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeScaleStrategysResponseBodyScaleStrategys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_strategy_id is not None:
            result['ScaleStrategyId'] = self.scale_strategy_id
        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count
        if self.max_available_desktops_count is not None:
            result['MaxAvailableDesktopsCount'] = self.max_available_desktops_count
        if self.scale_strategy_name is not None:
            result['ScaleStrategyName'] = self.scale_strategy_name
        if self.scale_strategy_type is not None:
            result['ScaleStrategyType'] = self.scale_strategy_type
        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count
        if self.min_available_desktops_count is not None:
            result['MinAvailableDesktopsCount'] = self.min_available_desktops_count
        if self.scale_step is not None:
            result['ScaleStep'] = self.scale_step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScaleStrategyId') is not None:
            self.scale_strategy_id = m.get('ScaleStrategyId')
        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')
        if m.get('MaxAvailableDesktopsCount') is not None:
            self.max_available_desktops_count = m.get('MaxAvailableDesktopsCount')
        if m.get('ScaleStrategyName') is not None:
            self.scale_strategy_name = m.get('ScaleStrategyName')
        if m.get('ScaleStrategyType') is not None:
            self.scale_strategy_type = m.get('ScaleStrategyType')
        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')
        if m.get('MinAvailableDesktopsCount') is not None:
            self.min_available_desktops_count = m.get('MinAvailableDesktopsCount')
        if m.get('ScaleStep') is not None:
            self.scale_step = m.get('ScaleStep')
        return self


class DescribeScaleStrategysResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, scale_strategys=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.scale_strategys = scale_strategys  # type: list[DescribeScaleStrategysResponseBodyScaleStrategys]

    def validate(self):
        if self.scale_strategys:
            for k in self.scale_strategys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeScaleStrategysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ScaleStrategys'] = []
        if self.scale_strategys is not None:
            for k in self.scale_strategys:
                result['ScaleStrategys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scale_strategys = []
        if m.get('ScaleStrategys') is not None:
            for k in m.get('ScaleStrategys'):
                temp_model = DescribeScaleStrategysResponseBodyScaleStrategys()
                self.scale_strategys.append(temp_model.from_map(k))
        return self


class DescribeScaleStrategysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeScaleStrategysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeScaleStrategysResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeScaleStrategysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScanTaskProgressRequest(TeaModel):
    def __init__(self, region_id=None, task_id=None):
        self.region_id = region_id  # type: str
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeScanTaskProgressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeScanTaskProgressResponseBody(TeaModel):
    def __init__(self, request_id=None, task_status=None, create_time=None):
        self.request_id = request_id  # type: str
        self.task_status = task_status  # type: str
        self.create_time = create_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeScanTaskProgressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class DescribeScanTaskProgressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeScanTaskProgressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeScanTaskProgressResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeScanTaskProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityEventOperationsRequest(TeaModel):
    def __init__(self, region_id=None, security_event_id=None):
        self.region_id = region_id  # type: str
        self.security_event_id = security_event_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityEventOperationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')
        return self


class DescribeSecurityEventOperationsResponseBodySecurityEventOperations(TeaModel):
    def __init__(self, operation_params=None, operation_code=None, user_can_operate=None):
        self.operation_params = operation_params  # type: str
        self.operation_code = operation_code  # type: str
        self.user_can_operate = user_can_operate  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityEventOperationsResponseBodySecurityEventOperations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_params is not None:
            result['OperationParams'] = self.operation_params
        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code
        if self.user_can_operate is not None:
            result['UserCanOperate'] = self.user_can_operate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperationParams') is not None:
            self.operation_params = m.get('OperationParams')
        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')
        if m.get('UserCanOperate') is not None:
            self.user_can_operate = m.get('UserCanOperate')
        return self


class DescribeSecurityEventOperationsResponseBody(TeaModel):
    def __init__(self, request_id=None, security_event_operations=None):
        self.request_id = request_id  # type: str
        self.security_event_operations = security_event_operations  # type: list[DescribeSecurityEventOperationsResponseBodySecurityEventOperations]

    def validate(self):
        if self.security_event_operations:
            for k in self.security_event_operations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSecurityEventOperationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityEventOperations'] = []
        if self.security_event_operations is not None:
            for k in self.security_event_operations:
                result['SecurityEventOperations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_event_operations = []
        if m.get('SecurityEventOperations') is not None:
            for k in m.get('SecurityEventOperations'):
                temp_model = DescribeSecurityEventOperationsResponseBodySecurityEventOperations()
                self.security_event_operations.append(temp_model.from_map(k))
        return self


class DescribeSecurityEventOperationsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSecurityEventOperationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSecurityEventOperationsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSecurityEventOperationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityEventOperationStatusRequest(TeaModel):
    def __init__(self, region_id=None, task_id=None, security_event_id=None):
        self.region_id = region_id  # type: str
        self.task_id = task_id  # type: long
        self.security_event_id = security_event_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityEventOperationStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')
        return self


class DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatuses(TeaModel):
    def __init__(self, status=None, security_event_id=None, error_code=None):
        self.status = status  # type: str
        self.security_event_id = security_event_id  # type: long
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatuses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DescribeSecurityEventOperationStatusResponseBody(TeaModel):
    def __init__(self, task_status=None, request_id=None, security_event_operation_statuses=None):
        self.task_status = task_status  # type: str
        self.request_id = request_id  # type: str
        self.security_event_operation_statuses = security_event_operation_statuses  # type: list[DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatuses]

    def validate(self):
        if self.security_event_operation_statuses:
            for k in self.security_event_operation_statuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSecurityEventOperationStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityEventOperationStatuses'] = []
        if self.security_event_operation_statuses is not None:
            for k in self.security_event_operation_statuses:
                result['SecurityEventOperationStatuses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_event_operation_statuses = []
        if m.get('SecurityEventOperationStatuses') is not None:
            for k in m.get('SecurityEventOperationStatuses'):
                temp_model = DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatuses()
                self.security_event_operation_statuses.append(temp_model.from_map(k))
        return self


class DescribeSecurityEventOperationStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSecurityEventOperationStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSecurityEventOperationStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSecurityEventOperationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSnapshotsRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None, snapshot_id=None, max_results=None, next_token=None):
        self.region_id = region_id  # type: str
        self.desktop_id = desktop_id  # type: str
        self.snapshot_id = snapshot_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSnapshotsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeSnapshotsResponseBodySnapshots(TeaModel):
    def __init__(self, creation_time=None, status=None, snapshot_type=None, snapshot_name=None, progress=None,
                 description=None, snapshot_id=None, remain_time=None, source_disk_size=None, source_disk_type=None,
                 desktop_id=None):
        self.creation_time = creation_time  # type: str
        self.status = status  # type: str
        self.snapshot_type = snapshot_type  # type: str
        self.snapshot_name = snapshot_name  # type: str
        self.progress = progress  # type: str
        self.description = description  # type: str
        self.snapshot_id = snapshot_id  # type: str
        self.remain_time = remain_time  # type: int
        self.source_disk_size = source_disk_size  # type: str
        self.source_disk_type = source_disk_type  # type: str
        self.desktop_id = desktop_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSnapshotsResponseBodySnapshots, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.description is not None:
            result['Description'] = self.description
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time
        if self.source_disk_size is not None:
            result['SourceDiskSize'] = self.source_disk_size
        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')
        if m.get('SourceDiskSize') is not None:
            self.source_disk_size = m.get('SourceDiskSize')
        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class DescribeSnapshotsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, snapshots=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.snapshots = snapshots  # type: list[DescribeSnapshotsResponseBodySnapshots]

    def validate(self):
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSnapshotsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = DescribeSnapshotsResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
        return self


class DescribeSnapshotsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSnapshotsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSnapshotsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSuspEventOverviewRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSuspEventOverviewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSuspEventOverviewResponseBody(TeaModel):
    def __init__(self, suspicious_count=None, remind_count=None, serious_count=None, request_id=None):
        self.suspicious_count = suspicious_count  # type: int
        self.remind_count = remind_count  # type: int
        self.serious_count = serious_count  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSuspEventOverviewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.suspicious_count is not None:
            result['SuspiciousCount'] = self.suspicious_count
        if self.remind_count is not None:
            result['RemindCount'] = self.remind_count
        if self.serious_count is not None:
            result['SeriousCount'] = self.serious_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SuspiciousCount') is not None:
            self.suspicious_count = m.get('SuspiciousCount')
        if m.get('RemindCount') is not None:
            self.remind_count = m.get('RemindCount')
        if m.get('SeriousCount') is not None:
            self.serious_count = m.get('SeriousCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSuspEventOverviewResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSuspEventOverviewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSuspEventOverviewResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSuspEventOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSuspEventQuaraFilesRequest(TeaModel):
    def __init__(self, region_id=None, status=None, office_site_id=None, current_page=None, page_size=None):
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.office_site_id = office_site_id  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSuspEventQuaraFilesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeSuspEventQuaraFilesResponseBodyQuaraFiles(TeaModel):
    def __init__(self, status=None, event_name=None, event_type=None, path=None, desktop_name=None, md_5=None,
                 tag=None, desktop_id=None, id=None, modify_time=None):
        self.status = status  # type: str
        self.event_name = event_name  # type: str
        self.event_type = event_type  # type: str
        self.path = path  # type: str
        self.desktop_name = desktop_name  # type: str
        self.md_5 = md_5  # type: str
        self.tag = tag  # type: str
        self.desktop_id = desktop_id  # type: str
        self.id = id  # type: int
        self.modify_time = modify_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSuspEventQuaraFilesResponseBodyQuaraFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.path is not None:
            result['Path'] = self.path
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class DescribeSuspEventQuaraFilesResponseBody(TeaModel):
    def __init__(self, current_page=None, request_id=None, page_size=None, total_count=None, quara_files=None):
        self.current_page = current_page  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.quara_files = quara_files  # type: list[DescribeSuspEventQuaraFilesResponseBodyQuaraFiles]

    def validate(self):
        if self.quara_files:
            for k in self.quara_files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSuspEventQuaraFilesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['QuaraFiles'] = []
        if self.quara_files is not None:
            for k in self.quara_files:
                result['QuaraFiles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.quara_files = []
        if m.get('QuaraFiles') is not None:
            for k in m.get('QuaraFiles'):
                temp_model = DescribeSuspEventQuaraFilesResponseBodyQuaraFiles()
                self.quara_files.append(temp_model.from_map(k))
        return self


class DescribeSuspEventQuaraFilesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSuspEventQuaraFilesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSuspEventQuaraFilesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSuspEventQuaraFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSuspEventsRequest(TeaModel):
    def __init__(self, region_id=None, lang=None, office_site_id=None, dealed=None, levels=None,
                 parent_event_type=None, alarm_unique_info=None, current_page=None, page_size=None):
        self.region_id = region_id  # type: str
        self.lang = lang  # type: str
        self.office_site_id = office_site_id  # type: str
        self.dealed = dealed  # type: str
        self.levels = levels  # type: str
        self.parent_event_type = parent_event_type  # type: str
        self.alarm_unique_info = alarm_unique_info  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSuspEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.levels is not None:
            result['Levels'] = self.levels
        if self.parent_event_type is not None:
            result['ParentEventType'] = self.parent_event_type
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('Levels') is not None:
            self.levels = m.get('Levels')
        if m.get('ParentEventType') is not None:
            self.parent_event_type = m.get('ParentEventType')
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeSuspEventsResponseBodySuspEventsDetails(TeaModel):
    def __init__(self, type=None, value=None, name_display=None, name=None, value_display=None):
        self.type = type  # type: str
        self.value = value  # type: str
        self.name_display = name_display  # type: str
        self.name = name  # type: str
        self.value_display = value_display  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSuspEventsResponseBodySuspEventsDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.name_display is not None:
            result['NameDisplay'] = self.name_display
        if self.name is not None:
            result['Name'] = self.name
        if self.value_display is not None:
            result['ValueDisplay'] = self.value_display
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('NameDisplay') is not None:
            self.name_display = m.get('NameDisplay')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ValueDisplay') is not None:
            self.value_display = m.get('ValueDisplay')
        return self


class DescribeSuspEventsResponseBodySuspEvents(TeaModel):
    def __init__(self, data_source=None, event_sub_type=None, desktop_name=None, desktop_id=None,
                 occurrence_time=None, alarm_event_type_display=None, alarm_unique_info=None, desc=None,
                 alarm_event_name_display=None, can_cancel_fault=None, last_time=None, operate_msg=None, can_be_deal_on_line=None,
                 alarm_event_type=None, event_status=None, operate_error_code=None, alarm_event_name=None, name=None,
                 unique_info=None, level=None, id=None, details=None):
        self.data_source = data_source  # type: str
        self.event_sub_type = event_sub_type  # type: str
        self.desktop_name = desktop_name  # type: str
        self.desktop_id = desktop_id  # type: str
        self.occurrence_time = occurrence_time  # type: str
        self.alarm_event_type_display = alarm_event_type_display  # type: str
        self.alarm_unique_info = alarm_unique_info  # type: str
        self.desc = desc  # type: str
        self.alarm_event_name_display = alarm_event_name_display  # type: str
        self.can_cancel_fault = can_cancel_fault  # type: bool
        self.last_time = last_time  # type: str
        self.operate_msg = operate_msg  # type: str
        self.can_be_deal_on_line = can_be_deal_on_line  # type: str
        self.alarm_event_type = alarm_event_type  # type: str
        self.event_status = event_status  # type: int
        self.operate_error_code = operate_error_code  # type: str
        self.alarm_event_name = alarm_event_name  # type: str
        self.name = name  # type: str
        self.unique_info = unique_info  # type: str
        self.level = level  # type: str
        self.id = id  # type: long
        self.details = details  # type: list[DescribeSuspEventsResponseBodySuspEventsDetails]

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSuspEventsResponseBodySuspEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.event_sub_type is not None:
            result['EventSubType'] = self.event_sub_type
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.occurrence_time is not None:
            result['OccurrenceTime'] = self.occurrence_time
        if self.alarm_event_type_display is not None:
            result['AlarmEventTypeDisplay'] = self.alarm_event_type_display
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.alarm_event_name_display is not None:
            result['AlarmEventNameDisplay'] = self.alarm_event_name_display
        if self.can_cancel_fault is not None:
            result['CanCancelFault'] = self.can_cancel_fault
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.operate_msg is not None:
            result['OperateMsg'] = self.operate_msg
        if self.can_be_deal_on_line is not None:
            result['CanBeDealOnLine'] = self.can_be_deal_on_line
        if self.alarm_event_type is not None:
            result['AlarmEventType'] = self.alarm_event_type
        if self.event_status is not None:
            result['EventStatus'] = self.event_status
        if self.operate_error_code is not None:
            result['OperateErrorCode'] = self.operate_error_code
        if self.alarm_event_name is not None:
            result['AlarmEventName'] = self.alarm_event_name
        if self.name is not None:
            result['Name'] = self.name
        if self.unique_info is not None:
            result['UniqueInfo'] = self.unique_info
        if self.level is not None:
            result['Level'] = self.level
        if self.id is not None:
            result['Id'] = self.id
        result['Details'] = []
        if self.details is not None:
            for k in self.details:
                result['Details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('EventSubType') is not None:
            self.event_sub_type = m.get('EventSubType')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('OccurrenceTime') is not None:
            self.occurrence_time = m.get('OccurrenceTime')
        if m.get('AlarmEventTypeDisplay') is not None:
            self.alarm_event_type_display = m.get('AlarmEventTypeDisplay')
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('AlarmEventNameDisplay') is not None:
            self.alarm_event_name_display = m.get('AlarmEventNameDisplay')
        if m.get('CanCancelFault') is not None:
            self.can_cancel_fault = m.get('CanCancelFault')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('OperateMsg') is not None:
            self.operate_msg = m.get('OperateMsg')
        if m.get('CanBeDealOnLine') is not None:
            self.can_be_deal_on_line = m.get('CanBeDealOnLine')
        if m.get('AlarmEventType') is not None:
            self.alarm_event_type = m.get('AlarmEventType')
        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')
        if m.get('OperateErrorCode') is not None:
            self.operate_error_code = m.get('OperateErrorCode')
        if m.get('AlarmEventName') is not None:
            self.alarm_event_name = m.get('AlarmEventName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UniqueInfo') is not None:
            self.unique_info = m.get('UniqueInfo')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.details = []
        if m.get('Details') is not None:
            for k in m.get('Details'):
                temp_model = DescribeSuspEventsResponseBodySuspEventsDetails()
                self.details.append(temp_model.from_map(k))
        return self


class DescribeSuspEventsResponseBody(TeaModel):
    def __init__(self, current_page=None, request_id=None, page_size=None, total_count=None, susp_events=None):
        self.current_page = current_page  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: str
        self.total_count = total_count  # type: int
        self.susp_events = susp_events  # type: list[DescribeSuspEventsResponseBodySuspEvents]

    def validate(self):
        if self.susp_events:
            for k in self.susp_events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSuspEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['SuspEvents'] = []
        if self.susp_events is not None:
            for k in self.susp_events:
                result['SuspEvents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.susp_events = []
        if m.get('SuspEvents') is not None:
            for k in m.get('SuspEvents'):
                temp_model = DescribeSuspEventsResponseBodySuspEvents()
                self.susp_events.append(temp_model.from_map(k))
        return self


class DescribeSuspEventsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSuspEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSuspEventsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSuspEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserConnectionRecordsRequest(TeaModel):
    def __init__(self, region_id=None, desktop_group_id=None, end_user_id=None, end_user_type=None,
                 max_results=None, next_token=None):
        self.region_id = region_id  # type: str
        self.desktop_group_id = desktop_group_id  # type: str
        self.end_user_id = end_user_id  # type: str
        self.end_user_type = end_user_type  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserConnectionRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.end_user_type is not None:
            result['EndUserType'] = self.end_user_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EndUserType') is not None:
            self.end_user_type = m.get('EndUserType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeUserConnectionRecordsResponseBodyConnectionRecords(TeaModel):
    def __init__(self, connection_record_id=None, connect_start_time=None, desktop_name=None,
                 connect_duration=None, connect_end_time=None, desktop_id=None):
        self.connection_record_id = connection_record_id  # type: str
        self.connect_start_time = connect_start_time  # type: str
        self.desktop_name = desktop_name  # type: str
        self.connect_duration = connect_duration  # type: str
        self.connect_end_time = connect_end_time  # type: str
        self.desktop_id = desktop_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserConnectionRecordsResponseBodyConnectionRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_record_id is not None:
            result['ConnectionRecordId'] = self.connection_record_id
        if self.connect_start_time is not None:
            result['ConnectStartTime'] = self.connect_start_time
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.connect_duration is not None:
            result['ConnectDuration'] = self.connect_duration
        if self.connect_end_time is not None:
            result['ConnectEndTime'] = self.connect_end_time
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionRecordId') is not None:
            self.connection_record_id = m.get('ConnectionRecordId')
        if m.get('ConnectStartTime') is not None:
            self.connect_start_time = m.get('ConnectStartTime')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('ConnectDuration') is not None:
            self.connect_duration = m.get('ConnectDuration')
        if m.get('ConnectEndTime') is not None:
            self.connect_end_time = m.get('ConnectEndTime')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class DescribeUserConnectionRecordsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, connection_records=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.connection_records = connection_records  # type: list[DescribeUserConnectionRecordsResponseBodyConnectionRecords]

    def validate(self):
        if self.connection_records:
            for k in self.connection_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUserConnectionRecordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ConnectionRecords'] = []
        if self.connection_records is not None:
            for k in self.connection_records:
                result['ConnectionRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.connection_records = []
        if m.get('ConnectionRecords') is not None:
            for k in m.get('ConnectionRecords'):
                temp_model = DescribeUserConnectionRecordsResponseBodyConnectionRecords()
                self.connection_records.append(temp_model.from_map(k))
        return self


class DescribeUserConnectionRecordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUserConnectionRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserConnectionRecordsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserConnectionRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsersInGroupRequest(TeaModel):
    def __init__(self, region_id=None, desktop_group_id=None, max_results=None, next_token=None):
        self.region_id = region_id  # type: str
        self.desktop_group_id = desktop_group_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUsersInGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeUsersInGroupResponseBodyEndUsers(TeaModel):
    def __init__(self, end_user_id=None, end_user_email=None, desktop_name=None, connection_status=None,
                 desktop_id=None, end_user_type=None, end_user_phone=None, end_user_name=None):
        self.end_user_id = end_user_id  # type: str
        self.end_user_email = end_user_email  # type: str
        self.desktop_name = desktop_name  # type: str
        self.connection_status = connection_status  # type: str
        self.desktop_id = desktop_id  # type: str
        self.end_user_type = end_user_type  # type: str
        self.end_user_phone = end_user_phone  # type: str
        self.end_user_name = end_user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUsersInGroupResponseBodyEndUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.end_user_email is not None:
            result['EndUserEmail'] = self.end_user_email
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.end_user_type is not None:
            result['EndUserType'] = self.end_user_type
        if self.end_user_phone is not None:
            result['EndUserPhone'] = self.end_user_phone
        if self.end_user_name is not None:
            result['EndUserName'] = self.end_user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EndUserEmail') is not None:
            self.end_user_email = m.get('EndUserEmail')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EndUserType') is not None:
            self.end_user_type = m.get('EndUserType')
        if m.get('EndUserPhone') is not None:
            self.end_user_phone = m.get('EndUserPhone')
        if m.get('EndUserName') is not None:
            self.end_user_name = m.get('EndUserName')
        return self


class DescribeUsersInGroupResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, users_count=None, online_users_count=None, end_users=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.users_count = users_count  # type: int
        self.online_users_count = online_users_count  # type: int
        self.end_users = end_users  # type: list[DescribeUsersInGroupResponseBodyEndUsers]

    def validate(self):
        if self.end_users:
            for k in self.end_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUsersInGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.users_count is not None:
            result['UsersCount'] = self.users_count
        if self.online_users_count is not None:
            result['OnlineUsersCount'] = self.online_users_count
        result['EndUsers'] = []
        if self.end_users is not None:
            for k in self.end_users:
                result['EndUsers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UsersCount') is not None:
            self.users_count = m.get('UsersCount')
        if m.get('OnlineUsersCount') is not None:
            self.online_users_count = m.get('OnlineUsersCount')
        self.end_users = []
        if m.get('EndUsers') is not None:
            for k in m.get('EndUsers'):
                temp_model = DescribeUsersInGroupResponseBodyEndUsers()
                self.end_users.append(temp_model.from_map(k))
        return self


class DescribeUsersInGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUsersInGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUsersInGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUsersInGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVirtualMFADevicesRequest(TeaModel):
    def __init__(self, region_id=None, max_results=None, next_token=None, directory_id=None, office_site_id=None,
                 end_user_id=None):
        self.region_id = region_id  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.directory_id = directory_id  # type: str
        self.office_site_id = office_site_id  # type: str
        self.end_user_id = end_user_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVirtualMFADevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        return self


class DescribeVirtualMFADevicesResponseBodyVirtualMFADevices(TeaModel):
    def __init__(self, serial_number=None, gmt_unlock=None, end_user_id=None, consecutive_fails=None,
                 office_site_id=None, status=None, directory_id=None, gmt_enabled=None):
        self.serial_number = serial_number  # type: str
        self.gmt_unlock = gmt_unlock  # type: str
        self.end_user_id = end_user_id  # type: str
        self.consecutive_fails = consecutive_fails  # type: int
        self.office_site_id = office_site_id  # type: str
        self.status = status  # type: str
        self.directory_id = directory_id  # type: str
        self.gmt_enabled = gmt_enabled  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVirtualMFADevicesResponseBodyVirtualMFADevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.gmt_unlock is not None:
            result['GmtUnlock'] = self.gmt_unlock
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.consecutive_fails is not None:
            result['ConsecutiveFails'] = self.consecutive_fails
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.status is not None:
            result['status'] = self.status
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.gmt_enabled is not None:
            result['GmtEnabled'] = self.gmt_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('GmtUnlock') is not None:
            self.gmt_unlock = m.get('GmtUnlock')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ConsecutiveFails') is not None:
            self.consecutive_fails = m.get('ConsecutiveFails')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('GmtEnabled') is not None:
            self.gmt_enabled = m.get('GmtEnabled')
        return self


class DescribeVirtualMFADevicesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, virtual_mfadevices=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.virtual_mfadevices = virtual_mfadevices  # type: list[DescribeVirtualMFADevicesResponseBodyVirtualMFADevices]

    def validate(self):
        if self.virtual_mfadevices:
            for k in self.virtual_mfadevices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVirtualMFADevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VirtualMFADevices'] = []
        if self.virtual_mfadevices is not None:
            for k in self.virtual_mfadevices:
                result['VirtualMFADevices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.virtual_mfadevices = []
        if m.get('VirtualMFADevices') is not None:
            for k in m.get('VirtualMFADevices'):
                temp_model = DescribeVirtualMFADevicesResponseBodyVirtualMFADevices()
                self.virtual_mfadevices.append(temp_model.from_map(k))
        return self


class DescribeVirtualMFADevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVirtualMFADevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVirtualMFADevicesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVirtualMFADevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVulDetailsRequest(TeaModel):
    def __init__(self, region_id=None, lang=None, type=None, name=None, alias_name=None):
        self.region_id = region_id  # type: str
        self.lang = lang  # type: str
        self.type = type  # type: str
        self.name = name  # type: str
        self.alias_name = alias_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVulDetailsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.type is not None:
            result['Type'] = self.type
        if self.name is not None:
            result['Name'] = self.name
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        return self


class DescribeVulDetailsResponseBodyCves(TeaModel):
    def __init__(self, cve_id=None, summary=None, title=None, cvss_score=None):
        self.cve_id = cve_id  # type: str
        self.summary = summary  # type: str
        self.title = title  # type: str
        self.cvss_score = cvss_score  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVulDetailsResponseBodyCves, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cve_id is not None:
            result['CveId'] = self.cve_id
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.title is not None:
            result['Title'] = self.title
        if self.cvss_score is not None:
            result['CvssScore'] = self.cvss_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('CvssScore') is not None:
            self.cvss_score = m.get('CvssScore')
        return self


class DescribeVulDetailsResponseBody(TeaModel):
    def __init__(self, request_id=None, cves=None):
        self.request_id = request_id  # type: str
        self.cves = cves  # type: list[DescribeVulDetailsResponseBodyCves]

    def validate(self):
        if self.cves:
            for k in self.cves:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVulDetailsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Cves'] = []
        if self.cves is not None:
            for k in self.cves:
                result['Cves'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.cves = []
        if m.get('Cves') is not None:
            for k in m.get('Cves'):
                temp_model = DescribeVulDetailsResponseBodyCves()
                self.cves.append(temp_model.from_map(k))
        return self


class DescribeVulDetailsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVulDetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVulDetailsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVulDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVulListRequest(TeaModel):
    def __init__(self, region_id=None, lang=None, type=None, office_site_id=None, necessity=None, alias_name=None,
                 dealed=None, current_page=None, page_size=None):
        self.region_id = region_id  # type: str
        self.lang = lang  # type: str
        self.type = type  # type: str
        self.office_site_id = office_site_id  # type: str
        self.necessity = necessity  # type: str
        self.alias_name = alias_name  # type: str
        self.dealed = dealed  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVulListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.type is not None:
            result['Type'] = self.type
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList(TeaModel):
    def __init__(self, path=None, update_cmd=None, name=None, full_version=None, match_detail=None):
        self.path = path  # type: str
        self.update_cmd = update_cmd  # type: str
        self.name = name  # type: str
        self.full_version = full_version  # type: str
        self.match_detail = match_detail  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.update_cmd is not None:
            result['UpdateCmd'] = self.update_cmd
        if self.name is not None:
            result['Name'] = self.name
        if self.full_version is not None:
            result['FullVersion'] = self.full_version
        if self.match_detail is not None:
            result['MatchDetail'] = self.match_detail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('UpdateCmd') is not None:
            self.update_cmd = m.get('UpdateCmd')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('FullVersion') is not None:
            self.full_version = m.get('FullVersion')
        if m.get('MatchDetail') is not None:
            self.match_detail = m.get('MatchDetail')
        return self


class DescribeVulListResponseBodyVulRecordsExtendContentJson(TeaModel):
    def __init__(self, rpm_entity_list=None):
        self.rpm_entity_list = rpm_entity_list  # type: list[DescribeVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList]

    def validate(self):
        if self.rpm_entity_list:
            for k in self.rpm_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVulListResponseBodyVulRecordsExtendContentJson, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RpmEntityList'] = []
        if self.rpm_entity_list is not None:
            for k in self.rpm_entity_list:
                result['RpmEntityList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.rpm_entity_list = []
        if m.get('RpmEntityList') is not None:
            for k in m.get('RpmEntityList'):
                temp_model = DescribeVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList()
                self.rpm_entity_list.append(temp_model.from_map(k))
        return self


class DescribeVulListResponseBodyVulRecords(TeaModel):
    def __init__(self, status=None, type=None, modify_ts=None, desktop_name=None, result_code=None, tag=None,
                 desktop_id=None, related=None, last_ts=None, first_ts=None, necessity=None, repair_ts=None, online=None,
                 result_message=None, os_version=None, alias_name=None, name=None, extend_content_json=None):
        self.status = status  # type: int
        self.type = type  # type: str
        self.modify_ts = modify_ts  # type: long
        self.desktop_name = desktop_name  # type: str
        self.result_code = result_code  # type: str
        self.tag = tag  # type: str
        self.desktop_id = desktop_id  # type: str
        self.related = related  # type: str
        self.last_ts = last_ts  # type: long
        self.first_ts = first_ts  # type: long
        self.necessity = necessity  # type: str
        self.repair_ts = repair_ts  # type: long
        self.online = online  # type: bool
        self.result_message = result_message  # type: str
        self.os_version = os_version  # type: str
        self.alias_name = alias_name  # type: str
        self.name = name  # type: str
        self.extend_content_json = extend_content_json  # type: DescribeVulListResponseBodyVulRecordsExtendContentJson

    def validate(self):
        if self.extend_content_json:
            self.extend_content_json.validate()

    def to_map(self):
        _map = super(DescribeVulListResponseBodyVulRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.modify_ts is not None:
            result['ModifyTs'] = self.modify_ts
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.related is not None:
            result['Related'] = self.related
        if self.last_ts is not None:
            result['LastTs'] = self.last_ts
        if self.first_ts is not None:
            result['FirstTs'] = self.first_ts
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.repair_ts is not None:
            result['RepairTs'] = self.repair_ts
        if self.online is not None:
            result['Online'] = self.online
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.os_version is not None:
            result['OsVersion'] = self.os_version
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.name is not None:
            result['Name'] = self.name
        if self.extend_content_json is not None:
            result['ExtendContentJson'] = self.extend_content_json.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ModifyTs') is not None:
            self.modify_ts = m.get('ModifyTs')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Related') is not None:
            self.related = m.get('Related')
        if m.get('LastTs') is not None:
            self.last_ts = m.get('LastTs')
        if m.get('FirstTs') is not None:
            self.first_ts = m.get('FirstTs')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('RepairTs') is not None:
            self.repair_ts = m.get('RepairTs')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ExtendContentJson') is not None:
            temp_model = DescribeVulListResponseBodyVulRecordsExtendContentJson()
            self.extend_content_json = temp_model.from_map(m['ExtendContentJson'])
        return self


class DescribeVulListResponseBody(TeaModel):
    def __init__(self, current_page=None, request_id=None, page_size=None, total_count=None, vul_records=None):
        self.current_page = current_page  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.vul_records = vul_records  # type: list[DescribeVulListResponseBodyVulRecords]

    def validate(self):
        if self.vul_records:
            for k in self.vul_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVulListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VulRecords'] = []
        if self.vul_records is not None:
            for k in self.vul_records:
                result['VulRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vul_records = []
        if m.get('VulRecords') is not None:
            for k in m.get('VulRecords'):
                temp_model = DescribeVulListResponseBodyVulRecords()
                self.vul_records.append(temp_model.from_map(k))
        return self


class DescribeVulListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVulListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVulListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVulListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVulOverviewRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVulOverviewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeVulOverviewResponseBody(TeaModel):
    def __init__(self, nntf_count=None, later_count=None, request_id=None, asap_count=None):
        self.nntf_count = nntf_count  # type: int
        self.later_count = later_count  # type: int
        self.request_id = request_id  # type: str
        self.asap_count = asap_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVulOverviewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nntf_count is not None:
            result['NntfCount'] = self.nntf_count
        if self.later_count is not None:
            result['LaterCount'] = self.later_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.asap_count is not None:
            result['AsapCount'] = self.asap_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NntfCount') is not None:
            self.nntf_count = m.get('NntfCount')
        if m.get('LaterCount') is not None:
            self.later_count = m.get('LaterCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AsapCount') is not None:
            self.asap_count = m.get('AsapCount')
        return self


class DescribeVulOverviewResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVulOverviewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVulOverviewResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVulOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(self, zone_id=None):
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeZonesResponseBodyZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(self, request_id=None, zones=None):
        self.request_id = request_id  # type: str
        self.zones = zones  # type: list[DescribeZonesResponseBodyZones]

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = DescribeZonesResponseBodyZones()
                self.zones.append(temp_model.from_map(k))
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeZonesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachCenRequest(TeaModel):
    def __init__(self, region_id=None, office_site_id=None):
        self.region_id = region_id  # type: str
        self.office_site_id = office_site_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachCenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class DetachCenResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachCenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachCenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetachCenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachCenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoCheckResourceRequest(TeaModel):
    def __init__(self, invoker=None, pk=None, bid=None, hid=None, country=None, task_identifier=None,
                 task_extra_data=None, gmt_wakeup=None, region_id=None):
        self.invoker = invoker  # type: str
        self.pk = pk  # type: str
        self.bid = bid  # type: str
        self.hid = hid  # type: long
        self.country = country  # type: str
        self.task_identifier = task_identifier  # type: str
        self.task_extra_data = task_extra_data  # type: str
        self.gmt_wakeup = gmt_wakeup  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoCheckResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.country is not None:
            result['Country'] = self.country
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DoCheckResourceResponseBody(TeaModel):
    def __init__(self, gmt_wakeup=None, hid=None, message=None, task_identifier=None, request_id=None, success=None,
                 url=None, interrupt=None, invoker=None, task_extra_data=None, country=None, prompt=None, level=None,
                 pk=None, bid=None):
        self.gmt_wakeup = gmt_wakeup  # type: str
        self.hid = hid  # type: long
        self.message = message  # type: str
        self.task_identifier = task_identifier  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.url = url  # type: str
        self.interrupt = interrupt  # type: bool
        self.invoker = invoker  # type: str
        self.task_extra_data = task_extra_data  # type: str
        self.country = country  # type: str
        self.prompt = prompt  # type: str
        self.level = level  # type: long
        self.pk = pk  # type: str
        self.bid = bid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoCheckResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.message is not None:
            result['Message'] = self.message
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.url is not None:
            result['Url'] = self.url
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.country is not None:
            result['Country'] = self.country
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.level is not None:
            result['Level'] = self.level
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.bid is not None:
            result['Bid'] = self.bid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        return self


class DoCheckResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DoCheckResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DoCheckResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DoCheckResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoLogicalDeleteResourceRequest(TeaModel):
    def __init__(self, invoker=None, pk=None, bid=None, hid=None, country=None, task_identifier=None,
                 task_extra_data=None, gmt_wakeup=None, region_id=None):
        self.invoker = invoker  # type: str
        self.pk = pk  # type: str
        self.bid = bid  # type: str
        self.hid = hid  # type: long
        self.country = country  # type: str
        self.task_identifier = task_identifier  # type: str
        self.task_extra_data = task_extra_data  # type: str
        self.gmt_wakeup = gmt_wakeup  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoLogicalDeleteResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.country is not None:
            result['Country'] = self.country
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DoLogicalDeleteResourceResponseBody(TeaModel):
    def __init__(self, gmt_wakeup=None, hid=None, message=None, task_identifier=None, request_id=None, invoker=None,
                 task_extra_data=None, country=None, pk=None, bid=None, success=None, interrupt=None):
        self.gmt_wakeup = gmt_wakeup  # type: str
        self.hid = hid  # type: long
        self.message = message  # type: str
        self.task_identifier = task_identifier  # type: str
        self.request_id = request_id  # type: str
        self.invoker = invoker  # type: str
        self.task_extra_data = task_extra_data  # type: str
        self.country = country  # type: str
        self.pk = pk  # type: str
        self.bid = bid  # type: str
        self.success = success  # type: bool
        self.interrupt = interrupt  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoLogicalDeleteResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.message is not None:
            result['Message'] = self.message
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.country is not None:
            result['Country'] = self.country
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.success is not None:
            result['Success'] = self.success
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        return self


class DoLogicalDeleteResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DoLogicalDeleteResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DoLogicalDeleteResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DoLogicalDeleteResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoPhysicalDeleteResourceRequest(TeaModel):
    def __init__(self, invoker=None, pk=None, bid=None, hid=None, country=None, task_identifier=None,
                 task_extra_data=None, gmt_wakeup=None, region_id=None):
        self.invoker = invoker  # type: str
        self.pk = pk  # type: str
        self.bid = bid  # type: str
        self.hid = hid  # type: long
        self.country = country  # type: str
        self.task_identifier = task_identifier  # type: str
        self.task_extra_data = task_extra_data  # type: str
        self.gmt_wakeup = gmt_wakeup  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoPhysicalDeleteResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.country is not None:
            result['Country'] = self.country
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DoPhysicalDeleteResourceResponseBody(TeaModel):
    def __init__(self, gmt_wakeup=None, hid=None, message=None, task_identifier=None, request_id=None, invoker=None,
                 task_extra_data=None, country=None, pk=None, bid=None, success=None, interrupt=None):
        self.gmt_wakeup = gmt_wakeup  # type: str
        self.hid = hid  # type: long
        self.message = message  # type: str
        self.task_identifier = task_identifier  # type: str
        self.request_id = request_id  # type: str
        self.invoker = invoker  # type: str
        self.task_extra_data = task_extra_data  # type: str
        self.country = country  # type: str
        self.pk = pk  # type: str
        self.bid = bid  # type: str
        self.success = success  # type: bool
        self.interrupt = interrupt  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoPhysicalDeleteResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.message is not None:
            result['Message'] = self.message
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.country is not None:
            result['Country'] = self.country
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.success is not None:
            result['Success'] = self.success
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        return self


class DoPhysicalDeleteResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DoPhysicalDeleteResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DoPhysicalDeleteResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DoPhysicalDeleteResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConnectionTicketRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, region_id=None,
                 instance_id=None, user_name=None, password=None, task_id=None, desktop_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.user_name = user_name  # type: str
        self.password = password  # type: str
        self.task_id = task_id  # type: str
        self.desktop_id = desktop_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnectionTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.password is not None:
            result['Password'] = self.password
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class GetConnectionTicketResponseBody(TeaModel):
    def __init__(self, ticket=None, task_id=None, request_id=None, task_status=None):
        self.ticket = ticket  # type: str
        self.task_id = task_id  # type: str
        self.request_id = request_id  # type: str
        self.task_status = task_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnectionTicketResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GetConnectionTicketResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetConnectionTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetConnectionTicketResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetConnectionTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDesktopGroupDetailRequest(TeaModel):
    def __init__(self, region_id=None, desktop_group_id=None):
        self.region_id = region_id  # type: str
        self.desktop_group_id = desktop_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDesktopGroupDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        return self


class GetDesktopGroupDetailResponseBodyDesktops(TeaModel):
    def __init__(self, creation_time=None, pay_type=None, policy_group_name=None, creator=None,
                 max_desktops_count=None, allow_auto_setup=None, res_type=None, system_disk_size=None, policy_group_id=None,
                 own_bundle_id=None, gpu_count=None, allow_buffer_count=None, memory=None, gpu_spec=None, directory_id=None,
                 own_bundle_name=None, data_disk_category=None, desktop_group_name=None, system_disk_category=None,
                 office_site_id=None, keep_duration=None, min_desktops_count=None, data_disk_size=None, desktop_group_id=None,
                 office_site_name=None, directory_type=None, cpu=None, expired_time=None, comments=None, office_site_type=None):
        self.creation_time = creation_time  # type: str
        self.pay_type = pay_type  # type: str
        self.policy_group_name = policy_group_name  # type: str
        self.creator = creator  # type: str
        self.max_desktops_count = max_desktops_count  # type: int
        self.allow_auto_setup = allow_auto_setup  # type: int
        self.res_type = res_type  # type: int
        self.system_disk_size = system_disk_size  # type: int
        self.policy_group_id = policy_group_id  # type: str
        self.own_bundle_id = own_bundle_id  # type: str
        self.gpu_count = gpu_count  # type: float
        self.allow_buffer_count = allow_buffer_count  # type: int
        self.memory = memory  # type: long
        self.gpu_spec = gpu_spec  # type: str
        self.directory_id = directory_id  # type: str
        self.own_bundle_name = own_bundle_name  # type: str
        self.data_disk_category = data_disk_category  # type: str
        self.desktop_group_name = desktop_group_name  # type: str
        self.system_disk_category = system_disk_category  # type: str
        self.office_site_id = office_site_id  # type: str
        self.keep_duration = keep_duration  # type: long
        self.min_desktops_count = min_desktops_count  # type: int
        self.data_disk_size = data_disk_size  # type: str
        self.desktop_group_id = desktop_group_id  # type: str
        self.office_site_name = office_site_name  # type: str
        self.directory_type = directory_type  # type: str
        self.cpu = cpu  # type: int
        self.expired_time = expired_time  # type: str
        self.comments = comments  # type: str
        self.office_site_type = office_site_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDesktopGroupDetailResponseBodyDesktops, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count
        if self.allow_auto_setup is not None:
            result['AllowAutoSetup'] = self.allow_auto_setup
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.own_bundle_id is not None:
            result['OwnBundleId'] = self.own_bundle_id
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.allow_buffer_count is not None:
            result['AllowBufferCount'] = self.allow_buffer_count
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.own_bundle_name is not None:
            result['OwnBundleName'] = self.own_bundle_name
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category
        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.keep_duration is not None:
            result['KeepDuration'] = self.keep_duration
        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')
        if m.get('AllowAutoSetup') is not None:
            self.allow_auto_setup = m.get('AllowAutoSetup')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('OwnBundleId') is not None:
            self.own_bundle_id = m.get('OwnBundleId')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('AllowBufferCount') is not None:
            self.allow_buffer_count = m.get('AllowBufferCount')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OwnBundleName') is not None:
            self.own_bundle_name = m.get('OwnBundleName')
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')
        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('KeepDuration') is not None:
            self.keep_duration = m.get('KeepDuration')
        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        return self


class GetDesktopGroupDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, desktops=None):
        self.request_id = request_id  # type: str
        self.desktops = desktops  # type: list[GetDesktopGroupDetailResponseBodyDesktops]

    def validate(self):
        if self.desktops:
            for k in self.desktops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDesktopGroupDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Desktops'] = []
        if self.desktops is not None:
            for k in self.desktops:
                result['Desktops'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.desktops = []
        if m.get('Desktops') is not None:
            for k in m.get('Desktops'):
                temp_model = GetDesktopGroupDetailResponseBodyDesktops()
                self.desktops.append(temp_model.from_map(k))
        return self


class GetDesktopGroupDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDesktopGroupDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDesktopGroupDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDesktopGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDesktopUsersRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None):
        self.region_id = region_id  # type: str
        self.desktop_id = desktop_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDesktopUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class GetDesktopUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, end_user_ids=None):
        self.request_id = request_id  # type: str
        self.end_user_ids = end_user_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDesktopUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        return self


class GetDesktopUsersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDesktopUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDesktopUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDesktopUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDirectorySsoStatusRequest(TeaModel):
    def __init__(self, region_id=None, directory_id=None):
        self.region_id = region_id  # type: str
        self.directory_id = directory_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDirectorySsoStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class GetDirectorySsoStatusResponseBody(TeaModel):
    def __init__(self, sso_status=None, request_id=None):
        self.sso_status = sso_status  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDirectorySsoStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sso_status is not None:
            result['SsoStatus'] = self.sso_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SsoStatus') is not None:
            self.sso_status = m.get('SsoStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDirectorySsoStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDirectorySsoStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDirectorySsoStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDirectorySsoStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOfficeSiteSsoStatusRequest(TeaModel):
    def __init__(self, region_id=None, office_site_id=None):
        self.region_id = region_id  # type: str
        self.office_site_id = office_site_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOfficeSiteSsoStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class GetOfficeSiteSsoStatusResponseBody(TeaModel):
    def __init__(self, sso_status=None, request_id=None):
        self.sso_status = sso_status  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOfficeSiteSsoStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sso_status is not None:
            result['SsoStatus'] = self.sso_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SsoStatus') is not None:
            self.sso_status = m.get('SsoStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOfficeSiteSsoStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetOfficeSiteSsoStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOfficeSiteSsoStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetOfficeSiteSsoStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSpMetadataRequest(TeaModel):
    def __init__(self, region_id=None, directory_id=None, office_site_id=None):
        self.region_id = region_id  # type: str
        self.directory_id = directory_id  # type: str
        self.office_site_id = office_site_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSpMetadataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class GetSpMetadataResponseBody(TeaModel):
    def __init__(self, sp_metadata=None, request_id=None):
        self.sp_metadata = sp_metadata  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSpMetadataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sp_metadata is not None:
            result['SpMetadata'] = self.sp_metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpMetadata') is not None:
            self.sp_metadata = m.get('SpMetadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSpMetadataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSpMetadataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSpMetadataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSpMetadataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HandleSecurityEventsRequestSecurityEvent(TeaModel):
    def __init__(self, security_event_id=None, desktop_id=None):
        self.security_event_id = security_event_id  # type: str
        self.desktop_id = desktop_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HandleSecurityEventsRequestSecurityEvent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class HandleSecurityEventsRequest(TeaModel):
    def __init__(self, region_id=None, operation_code=None, operation_params=None, security_event=None):
        self.region_id = region_id  # type: str
        self.operation_code = operation_code  # type: str
        self.operation_params = operation_params  # type: str
        self.security_event = security_event  # type: list[HandleSecurityEventsRequestSecurityEvent]

    def validate(self):
        if self.security_event:
            for k in self.security_event:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(HandleSecurityEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code
        if self.operation_params is not None:
            result['OperationParams'] = self.operation_params
        result['SecurityEvent'] = []
        if self.security_event is not None:
            for k in self.security_event:
                result['SecurityEvent'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')
        if m.get('OperationParams') is not None:
            self.operation_params = m.get('OperationParams')
        self.security_event = []
        if m.get('SecurityEvent') is not None:
            for k in m.get('SecurityEvent'):
                temp_model = HandleSecurityEventsRequestSecurityEvent()
                self.security_event.append(temp_model.from_map(k))
        return self


class HandleSecurityEventsResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None):
        self.task_id = task_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HandleSecurityEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class HandleSecurityEventsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: HandleSecurityEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(HandleSecurityEventsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = HandleSecurityEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDirectoryUsersRequest(TeaModel):
    def __init__(self, region_id=None, filter=None, directory_id=None, next_token=None, max_results=None):
        self.region_id = region_id  # type: str
        self.filter = filter  # type: str
        self.directory_id = directory_id  # type: str
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDirectoryUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListDirectoryUsersResponseBodyUsers(TeaModel):
    def __init__(self, end_user=None):
        self.end_user = end_user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDirectoryUsersResponseBodyUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user is not None:
            result['EndUser'] = self.end_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndUser') is not None:
            self.end_user = m.get('EndUser')
        return self


class ListDirectoryUsersResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, users=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.users = users  # type: list[ListDirectoryUsersResponseBodyUsers]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDirectoryUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = ListDirectoryUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListDirectoryUsersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDirectoryUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDirectoryUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDirectoryUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOfficeSiteOverviewRequest(TeaModel):
    def __init__(self, region_id=None, force_refresh=None, max_results=None, next_token=None, office_site_id=None):
        self.region_id = region_id  # type: str
        self.force_refresh = force_refresh  # type: bool
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.office_site_id = office_site_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOfficeSiteOverviewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.force_refresh is not None:
            result['ForceRefresh'] = self.force_refresh
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ForceRefresh') is not None:
            self.force_refresh = m.get('ForceRefresh')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class ListOfficeSiteOverviewResponseBodyOfficeSiteOverviewResults(TeaModel):
    def __init__(self, office_site_status=None, total_eds_count=None, will_expired_eds_count=None,
                 office_site_id=None, running_eds_count=None, office_site_name=None, has_expired_eds_count=None, region_id=None):
        self.office_site_status = office_site_status  # type: str
        self.total_eds_count = total_eds_count  # type: int
        self.will_expired_eds_count = will_expired_eds_count  # type: int
        self.office_site_id = office_site_id  # type: str
        self.running_eds_count = running_eds_count  # type: int
        self.office_site_name = office_site_name  # type: str
        self.has_expired_eds_count = has_expired_eds_count  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOfficeSiteOverviewResponseBodyOfficeSiteOverviewResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.office_site_status is not None:
            result['OfficeSiteStatus'] = self.office_site_status
        if self.total_eds_count is not None:
            result['TotalEdsCount'] = self.total_eds_count
        if self.will_expired_eds_count is not None:
            result['WillExpiredEdsCount'] = self.will_expired_eds_count
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.running_eds_count is not None:
            result['RunningEdsCount'] = self.running_eds_count
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.has_expired_eds_count is not None:
            result['HasExpiredEdsCount'] = self.has_expired_eds_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OfficeSiteStatus') is not None:
            self.office_site_status = m.get('OfficeSiteStatus')
        if m.get('TotalEdsCount') is not None:
            self.total_eds_count = m.get('TotalEdsCount')
        if m.get('WillExpiredEdsCount') is not None:
            self.will_expired_eds_count = m.get('WillExpiredEdsCount')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RunningEdsCount') is not None:
            self.running_eds_count = m.get('RunningEdsCount')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('HasExpiredEdsCount') is not None:
            self.has_expired_eds_count = m.get('HasExpiredEdsCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListOfficeSiteOverviewResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, office_site_overview_results=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.office_site_overview_results = office_site_overview_results  # type: list[ListOfficeSiteOverviewResponseBodyOfficeSiteOverviewResults]

    def validate(self):
        if self.office_site_overview_results:
            for k in self.office_site_overview_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOfficeSiteOverviewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['OfficeSiteOverviewResults'] = []
        if self.office_site_overview_results is not None:
            for k in self.office_site_overview_results:
                result['OfficeSiteOverviewResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.office_site_overview_results = []
        if m.get('OfficeSiteOverviewResults') is not None:
            for k in m.get('OfficeSiteOverviewResults'):
                temp_model = ListOfficeSiteOverviewResponseBodyOfficeSiteOverviewResults()
                self.office_site_overview_results.append(temp_model.from_map(k))
        return self


class ListOfficeSiteOverviewResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListOfficeSiteOverviewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOfficeSiteOverviewResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListOfficeSiteOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOfficeSiteUsersRequest(TeaModel):
    def __init__(self, region_id=None, filter=None, office_site_id=None, next_token=None, max_results=None):
        self.region_id = region_id  # type: str
        self.filter = filter  # type: str
        self.office_site_id = office_site_id  # type: str
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOfficeSiteUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListOfficeSiteUsersResponseBodyUsers(TeaModel):
    def __init__(self, end_user=None):
        self.end_user = end_user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOfficeSiteUsersResponseBodyUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user is not None:
            result['EndUser'] = self.end_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndUser') is not None:
            self.end_user = m.get('EndUser')
        return self


class ListOfficeSiteUsersResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, users=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.users = users  # type: list[ListOfficeSiteUsersResponseBodyUsers]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOfficeSiteUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = ListOfficeSiteUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListOfficeSiteUsersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListOfficeSiteUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOfficeSiteUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListOfficeSiteUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesRequestTag, self).to_map()
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


class ListTagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, max_results=None, next_token=None, resource_id=None,
                 tag=None):
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.tag = tag  # type: list[ListTagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, tag_value=None, resource_type=None, resource_id=None, tag_key=None):
        self.tag_value = tag_value  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: str
        self.tag_key = tag_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.tag_resources = tag_resources  # type: list[ListTagResourcesResponseBodyTagResources]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockVirtualMFADeviceRequest(TeaModel):
    def __init__(self, region_id=None, serial_number=None):
        self.region_id = region_id  # type: str
        self.serial_number = serial_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LockVirtualMFADeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class LockVirtualMFADeviceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LockVirtualMFADeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LockVirtualMFADeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: LockVirtualMFADeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LockVirtualMFADeviceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = LockVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyADConnectorDirectoryRequest(TeaModel):
    def __init__(self, region_id=None, directory_id=None, domain_name=None, domain_user_name=None,
                 domain_password=None, directory_name=None, sub_domain_name=None, mfa_enabled=None, dns_address=None,
                 sub_domain_dns_address=None):
        self.region_id = region_id  # type: str
        self.directory_id = directory_id  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_user_name = domain_user_name  # type: str
        self.domain_password = domain_password  # type: str
        self.directory_name = directory_name  # type: str
        self.sub_domain_name = sub_domain_name  # type: str
        self.mfa_enabled = mfa_enabled  # type: bool
        self.dns_address = dns_address  # type: list[str]
        self.sub_domain_dns_address = sub_domain_dns_address  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyADConnectorDirectoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.sub_domain_dns_address is not None:
            result['SubDomainDnsAddress'] = self.sub_domain_dns_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('SubDomainDnsAddress') is not None:
            self.sub_domain_dns_address = m.get('SubDomainDnsAddress')
        return self


class ModifyADConnectorDirectoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyADConnectorDirectoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyADConnectorDirectoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyADConnectorDirectoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyADConnectorDirectoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyADConnectorDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyADConnectorOfficeSiteRequest(TeaModel):
    def __init__(self, region_id=None, office_site_id=None, domain_name=None, domain_user_name=None,
                 domain_password=None, office_site_name=None, sub_domain_name=None, mfa_enabled=None, dns_address=None,
                 sub_domain_dns_address=None):
        self.region_id = region_id  # type: str
        self.office_site_id = office_site_id  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_user_name = domain_user_name  # type: str
        self.domain_password = domain_password  # type: str
        self.office_site_name = office_site_name  # type: str
        self.sub_domain_name = sub_domain_name  # type: str
        self.mfa_enabled = mfa_enabled  # type: bool
        self.dns_address = dns_address  # type: list[str]
        self.sub_domain_dns_address = sub_domain_dns_address  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyADConnectorOfficeSiteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.sub_domain_dns_address is not None:
            result['SubDomainDnsAddress'] = self.sub_domain_dns_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('SubDomainDnsAddress') is not None:
            self.sub_domain_dns_address = m.get('SubDomainDnsAddress')
        return self


class ModifyADConnectorOfficeSiteResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyADConnectorOfficeSiteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyADConnectorOfficeSiteResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyADConnectorOfficeSiteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyADConnectorOfficeSiteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyADConnectorOfficeSiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBundleRequest(TeaModel):
    def __init__(self, region_id=None, bundle_id=None, image_id=None, bundle_name=None, description=None):
        self.region_id = region_id  # type: str
        self.bundle_id = bundle_id  # type: str
        self.image_id = image_id  # type: str
        self.bundle_name = bundle_name  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBundleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.bundle_name is not None:
            result['BundleName'] = self.bundle_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('BundleName') is not None:
            self.bundle_name = m.get('BundleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifyBundleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBundleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyBundleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyBundleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyBundleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyBundleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopGroupRequest(TeaModel):
    def __init__(self, region_id=None, desktop_group_id=None, own_bundle_id=None, policy_group_id=None,
                 desktop_group_name=None, scale_strategy_id=None, keep_duration=None, comments=None, min_desktops_count=None,
                 max_desktops_count=None, allow_auto_setup=None, allow_buffer_count=None):
        self.region_id = region_id  # type: str
        self.desktop_group_id = desktop_group_id  # type: str
        self.own_bundle_id = own_bundle_id  # type: str
        self.policy_group_id = policy_group_id  # type: str
        self.desktop_group_name = desktop_group_name  # type: str
        self.scale_strategy_id = scale_strategy_id  # type: str
        self.keep_duration = keep_duration  # type: long
        self.comments = comments  # type: str
        self.min_desktops_count = min_desktops_count  # type: int
        self.max_desktops_count = max_desktops_count  # type: int
        self.allow_auto_setup = allow_auto_setup  # type: int
        self.allow_buffer_count = allow_buffer_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDesktopGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.own_bundle_id is not None:
            result['OwnBundleId'] = self.own_bundle_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name
        if self.scale_strategy_id is not None:
            result['ScaleStrategyId'] = self.scale_strategy_id
        if self.keep_duration is not None:
            result['KeepDuration'] = self.keep_duration
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count
        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count
        if self.allow_auto_setup is not None:
            result['AllowAutoSetup'] = self.allow_auto_setup
        if self.allow_buffer_count is not None:
            result['AllowBufferCount'] = self.allow_buffer_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('OwnBundleId') is not None:
            self.own_bundle_id = m.get('OwnBundleId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')
        if m.get('ScaleStrategyId') is not None:
            self.scale_strategy_id = m.get('ScaleStrategyId')
        if m.get('KeepDuration') is not None:
            self.keep_duration = m.get('KeepDuration')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')
        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')
        if m.get('AllowAutoSetup') is not None:
            self.allow_auto_setup = m.get('AllowAutoSetup')
        if m.get('AllowBufferCount') is not None:
            self.allow_buffer_count = m.get('AllowBufferCount')
        return self


class ModifyDesktopGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDesktopGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDesktopGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDesktopGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDesktopGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopNameRequest(TeaModel):
    def __init__(self, region_id=None, new_desktop_name=None, desktop_id=None):
        self.region_id = region_id  # type: str
        self.new_desktop_name = new_desktop_name  # type: str
        self.desktop_id = desktop_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDesktopNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.new_desktop_name is not None:
            result['NewDesktopName'] = self.new_desktop_name
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NewDesktopName') is not None:
            self.new_desktop_name = m.get('NewDesktopName')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class ModifyDesktopNameResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDesktopNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDesktopNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDesktopNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDesktopNameResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDesktopNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopPolicysRequest(TeaModel):
    def __init__(self, region_id=None, clipboard=None, local_drive=None, usb_redirect=None, watermark=None,
                 desktop_id=None):
        self.region_id = region_id  # type: str
        self.clipboard = clipboard  # type: str
        self.local_drive = local_drive  # type: str
        self.usb_redirect = usb_redirect  # type: str
        self.watermark = watermark  # type: str
        self.desktop_id = desktop_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDesktopPolicysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class ModifyDesktopPolicysResponseBodyResults(TeaModel):
    def __init__(self, success=None, code=None, message=None, desktop_id=None):
        self.success = success  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.desktop_id = desktop_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDesktopPolicysResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class ModifyDesktopPolicysResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        self.request_id = request_id  # type: str
        self.results = results  # type: list[ModifyDesktopPolicysResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyDesktopPolicysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ModifyDesktopPolicysResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class ModifyDesktopPolicysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDesktopPolicysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDesktopPolicysResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDesktopPolicysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopSpecRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None, desktop_type=None, root_disk_size_gib=None,
                 user_disk_size_gib=None, auto_pay=None):
        self.region_id = region_id  # type: str
        self.desktop_id = desktop_id  # type: str
        self.desktop_type = desktop_type  # type: str
        self.root_disk_size_gib = root_disk_size_gib  # type: int
        self.user_disk_size_gib = user_disk_size_gib  # type: int
        self.auto_pay = auto_pay  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDesktopSpecRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.root_disk_size_gib is not None:
            result['RootDiskSizeGib'] = self.root_disk_size_gib
        if self.user_disk_size_gib is not None:
            result['UserDiskSizeGib'] = self.user_disk_size_gib
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('RootDiskSizeGib') is not None:
            self.root_disk_size_gib = m.get('RootDiskSizeGib')
        if m.get('UserDiskSizeGib') is not None:
            self.user_disk_size_gib = m.get('UserDiskSizeGib')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        return self


class ModifyDesktopSpecResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDesktopSpecResponseBody, self).to_map()
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


class ModifyDesktopSpecResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDesktopSpecResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDesktopSpecResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDesktopSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopsPolicyGroupRequest(TeaModel):
    def __init__(self, region_id=None, policy_group_id=None, desktop_id=None):
        self.region_id = region_id  # type: str
        self.policy_group_id = policy_group_id  # type: str
        self.desktop_id = desktop_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDesktopsPolicyGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class ModifyDesktopsPolicyGroupResponseBodyModifyResults(TeaModel):
    def __init__(self, code=None, message=None, desktop_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.desktop_id = desktop_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDesktopsPolicyGroupResponseBodyModifyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class ModifyDesktopsPolicyGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, modify_results=None):
        self.request_id = request_id  # type: str
        self.modify_results = modify_results  # type: list[ModifyDesktopsPolicyGroupResponseBodyModifyResults]

    def validate(self):
        if self.modify_results:
            for k in self.modify_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyDesktopsPolicyGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ModifyResults'] = []
        if self.modify_results is not None:
            for k in self.modify_results:
                result['ModifyResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.modify_results = []
        if m.get('ModifyResults') is not None:
            for k in m.get('ModifyResults'):
                temp_model = ModifyDesktopsPolicyGroupResponseBodyModifyResults()
                self.modify_results.append(temp_model.from_map(k))
        return self


class ModifyDesktopsPolicyGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDesktopsPolicyGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDesktopsPolicyGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDesktopsPolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyEntitlementRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None, end_user_id=None):
        self.region_id = region_id  # type: str
        self.desktop_id = desktop_id  # type: str
        self.end_user_id = end_user_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyEntitlementRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        return self


class ModifyEntitlementResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyEntitlementResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyEntitlementResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyEntitlementResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyEntitlementResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyEntitlementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyImageAttributeRequest(TeaModel):
    def __init__(self, region_id=None, image_id=None, name=None, description=None):
        self.region_id = region_id  # type: str
        self.image_id = image_id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyImageAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifyImageAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyImageAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyImageAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyImageAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyImageAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyImageAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNASDefaultMountTargetRequest(TeaModel):
    def __init__(self, region_id=None, file_system_id=None, mount_target_domain=None):
        self.region_id = region_id  # type: str
        self.file_system_id = file_system_id  # type: str
        self.mount_target_domain = mount_target_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNASDefaultMountTargetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        return self


class ModifyNASDefaultMountTargetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNASDefaultMountTargetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyNASDefaultMountTargetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyNASDefaultMountTargetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyNASDefaultMountTargetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyNASDefaultMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNetworkPackageRequest(TeaModel):
    def __init__(self, region_id=None, network_package_id=None, bandwidth=None):
        self.region_id = region_id  # type: str
        self.network_package_id = network_package_id  # type: str
        self.bandwidth = bandwidth  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNetworkPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        return self


class ModifyNetworkPackageResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNetworkPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyNetworkPackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyNetworkPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyNetworkPackageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyNetworkPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNetworkPackageEnabledRequest(TeaModel):
    def __init__(self, region_id=None, network_package_id=None, enabled=None):
        self.region_id = region_id  # type: str
        self.network_package_id = network_package_id  # type: str
        self.enabled = enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNetworkPackageEnabledRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class ModifyNetworkPackageEnabledResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNetworkPackageEnabledResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyNetworkPackageEnabledResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyNetworkPackageEnabledResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyNetworkPackageEnabledResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyNetworkPackageEnabledResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOfficeSiteAttributeRequest(TeaModel):
    def __init__(self, region_id=None, office_site_id=None, desktop_access_type=None, office_site_name=None):
        self.region_id = region_id  # type: str
        self.office_site_id = office_site_id  # type: str
        self.desktop_access_type = desktop_access_type  # type: str
        self.office_site_name = office_site_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyOfficeSiteAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        return self


class ModifyOfficeSiteAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyOfficeSiteAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyOfficeSiteAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyOfficeSiteAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyOfficeSiteAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyOfficeSiteAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOfficeSiteCrossDesktopAccessRequest(TeaModel):
    def __init__(self, region_id=None, office_site_id=None, enable_cross_desktop_access=None):
        self.region_id = region_id  # type: str
        self.office_site_id = office_site_id  # type: str
        self.enable_cross_desktop_access = enable_cross_desktop_access  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyOfficeSiteCrossDesktopAccessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.enable_cross_desktop_access is not None:
            result['EnableCrossDesktopAccess'] = self.enable_cross_desktop_access
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('EnableCrossDesktopAccess') is not None:
            self.enable_cross_desktop_access = m.get('EnableCrossDesktopAccess')
        return self


class ModifyOfficeSiteCrossDesktopAccessResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyOfficeSiteCrossDesktopAccessResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyOfficeSiteCrossDesktopAccessResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyOfficeSiteCrossDesktopAccessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyOfficeSiteCrossDesktopAccessResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyOfficeSiteCrossDesktopAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOfficeSiteMfaEnabledRequest(TeaModel):
    def __init__(self, region_id=None, office_site_id=None, mfa_enabled=None):
        self.region_id = region_id  # type: str
        self.office_site_id = office_site_id  # type: str
        self.mfa_enabled = mfa_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyOfficeSiteMfaEnabledRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        return self


class ModifyOfficeSiteMfaEnabledResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyOfficeSiteMfaEnabledResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyOfficeSiteMfaEnabledResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyOfficeSiteMfaEnabledResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyOfficeSiteMfaEnabledResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyOfficeSiteMfaEnabledResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOperateVulRequestVulInfo(TeaModel):
    def __init__(self, desktop_id=None, tag=None, name=None):
        self.desktop_id = desktop_id  # type: str
        self.tag = tag  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyOperateVulRequestVulInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyOperateVulRequest(TeaModel):
    def __init__(self, region_id=None, type=None, operate_type=None, reason=None, vul_info=None):
        self.region_id = region_id  # type: str
        self.type = type  # type: str
        self.operate_type = operate_type  # type: str
        self.reason = reason  # type: str
        self.vul_info = vul_info  # type: list[ModifyOperateVulRequestVulInfo]

    def validate(self):
        if self.vul_info:
            for k in self.vul_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyOperateVulRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.reason is not None:
            result['Reason'] = self.reason
        result['VulInfo'] = []
        if self.vul_info is not None:
            for k in self.vul_info:
                result['VulInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        self.vul_info = []
        if m.get('VulInfo') is not None:
            for k in m.get('VulInfo'):
                temp_model = ModifyOperateVulRequestVulInfo()
                self.vul_info.append(temp_model.from_map(k))
        return self


class ModifyOperateVulResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyOperateVulResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyOperateVulResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyOperateVulResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyOperateVulResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyOperateVulResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPolicyGroupRequestAuthorizeSecurityPolicyRule(TeaModel):
    def __init__(self, type=None, policy=None, port_range=None, description=None, ip_protocol=None, priority=None,
                 cidr_ip=None):
        self.type = type  # type: str
        self.policy = policy  # type: str
        self.port_range = port_range  # type: str
        self.description = description  # type: str
        self.ip_protocol = ip_protocol  # type: str
        self.priority = priority  # type: str
        self.cidr_ip = cidr_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPolicyGroupRequestAuthorizeSecurityPolicyRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.description is not None:
            result['Description'] = self.description
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        return self


class ModifyPolicyGroupRequestRevokeSecurityPolicyRule(TeaModel):
    def __init__(self, type=None, policy=None, port_range=None, description=None, ip_protocol=None, priority=None,
                 cidr_ip=None):
        self.type = type  # type: str
        self.policy = policy  # type: str
        self.port_range = port_range  # type: str
        self.description = description  # type: str
        self.ip_protocol = ip_protocol  # type: str
        self.priority = priority  # type: str
        self.cidr_ip = cidr_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPolicyGroupRequestRevokeSecurityPolicyRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.description is not None:
            result['Description'] = self.description
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        return self


class ModifyPolicyGroupRequestAuthorizeAccessPolicyRule(TeaModel):
    def __init__(self, description=None, cidr_ip=None):
        self.description = description  # type: str
        self.cidr_ip = cidr_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPolicyGroupRequestAuthorizeAccessPolicyRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        return self


class ModifyPolicyGroupRequestRevokeAccessPolicyRule(TeaModel):
    def __init__(self, description=None, cidr_ip=None):
        self.description = description  # type: str
        self.cidr_ip = cidr_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPolicyGroupRequestRevokeAccessPolicyRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        return self


class ModifyPolicyGroupRequest(TeaModel):
    def __init__(self, region_id=None, policy_group_id=None, name=None, clipboard=None, local_drive=None,
                 usb_redirect=None, visual_quality=None, html_5access=None, html_5file_transfer=None, watermark=None,
                 watermark_type=None, watermark_custom_text=None, watermark_transparency=None, preempt_login=None,
                 domain_list=None, preempt_login_user=None, authorize_security_policy_rule=None,
                 revoke_security_policy_rule=None, authorize_access_policy_rule=None, revoke_access_policy_rule=None):
        self.region_id = region_id  # type: str
        self.policy_group_id = policy_group_id  # type: str
        self.name = name  # type: str
        self.clipboard = clipboard  # type: str
        self.local_drive = local_drive  # type: str
        self.usb_redirect = usb_redirect  # type: str
        self.visual_quality = visual_quality  # type: str
        self.html_5access = html_5access  # type: str
        self.html_5file_transfer = html_5file_transfer  # type: str
        self.watermark = watermark  # type: str
        self.watermark_type = watermark_type  # type: str
        self.watermark_custom_text = watermark_custom_text  # type: str
        self.watermark_transparency = watermark_transparency  # type: str
        self.preempt_login = preempt_login  # type: str
        self.domain_list = domain_list  # type: str
        self.preempt_login_user = preempt_login_user  # type: list[str]
        self.authorize_security_policy_rule = authorize_security_policy_rule  # type: list[ModifyPolicyGroupRequestAuthorizeSecurityPolicyRule]
        self.revoke_security_policy_rule = revoke_security_policy_rule  # type: list[ModifyPolicyGroupRequestRevokeSecurityPolicyRule]
        self.authorize_access_policy_rule = authorize_access_policy_rule  # type: list[ModifyPolicyGroupRequestAuthorizeAccessPolicyRule]
        self.revoke_access_policy_rule = revoke_access_policy_rule  # type: list[ModifyPolicyGroupRequestRevokeAccessPolicyRule]

    def validate(self):
        if self.authorize_security_policy_rule:
            for k in self.authorize_security_policy_rule:
                if k:
                    k.validate()
        if self.revoke_security_policy_rule:
            for k in self.revoke_security_policy_rule:
                if k:
                    k.validate()
        if self.authorize_access_policy_rule:
            for k in self.authorize_access_policy_rule:
                if k:
                    k.validate()
        if self.revoke_access_policy_rule:
            for k in self.revoke_access_policy_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyPolicyGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.visual_quality is not None:
            result['VisualQuality'] = self.visual_quality
        if self.html_5access is not None:
            result['Html5Access'] = self.html_5access
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        if self.watermark_custom_text is not None:
            result['WatermarkCustomText'] = self.watermark_custom_text
        if self.watermark_transparency is not None:
            result['WatermarkTransparency'] = self.watermark_transparency
        if self.preempt_login is not None:
            result['PreemptLogin'] = self.preempt_login
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.preempt_login_user is not None:
            result['PreemptLoginUser'] = self.preempt_login_user
        result['AuthorizeSecurityPolicyRule'] = []
        if self.authorize_security_policy_rule is not None:
            for k in self.authorize_security_policy_rule:
                result['AuthorizeSecurityPolicyRule'].append(k.to_map() if k else None)
        result['RevokeSecurityPolicyRule'] = []
        if self.revoke_security_policy_rule is not None:
            for k in self.revoke_security_policy_rule:
                result['RevokeSecurityPolicyRule'].append(k.to_map() if k else None)
        result['AuthorizeAccessPolicyRule'] = []
        if self.authorize_access_policy_rule is not None:
            for k in self.authorize_access_policy_rule:
                result['AuthorizeAccessPolicyRule'].append(k.to_map() if k else None)
        result['RevokeAccessPolicyRule'] = []
        if self.revoke_access_policy_rule is not None:
            for k in self.revoke_access_policy_rule:
                result['RevokeAccessPolicyRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('VisualQuality') is not None:
            self.visual_quality = m.get('VisualQuality')
        if m.get('Html5Access') is not None:
            self.html_5access = m.get('Html5Access')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        if m.get('WatermarkCustomText') is not None:
            self.watermark_custom_text = m.get('WatermarkCustomText')
        if m.get('WatermarkTransparency') is not None:
            self.watermark_transparency = m.get('WatermarkTransparency')
        if m.get('PreemptLogin') is not None:
            self.preempt_login = m.get('PreemptLogin')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('PreemptLoginUser') is not None:
            self.preempt_login_user = m.get('PreemptLoginUser')
        self.authorize_security_policy_rule = []
        if m.get('AuthorizeSecurityPolicyRule') is not None:
            for k in m.get('AuthorizeSecurityPolicyRule'):
                temp_model = ModifyPolicyGroupRequestAuthorizeSecurityPolicyRule()
                self.authorize_security_policy_rule.append(temp_model.from_map(k))
        self.revoke_security_policy_rule = []
        if m.get('RevokeSecurityPolicyRule') is not None:
            for k in m.get('RevokeSecurityPolicyRule'):
                temp_model = ModifyPolicyGroupRequestRevokeSecurityPolicyRule()
                self.revoke_security_policy_rule.append(temp_model.from_map(k))
        self.authorize_access_policy_rule = []
        if m.get('AuthorizeAccessPolicyRule') is not None:
            for k in m.get('AuthorizeAccessPolicyRule'):
                temp_model = ModifyPolicyGroupRequestAuthorizeAccessPolicyRule()
                self.authorize_access_policy_rule.append(temp_model.from_map(k))
        self.revoke_access_policy_rule = []
        if m.get('RevokeAccessPolicyRule') is not None:
            for k in m.get('RevokeAccessPolicyRule'):
                temp_model = ModifyPolicyGroupRequestRevokeAccessPolicyRule()
                self.revoke_access_policy_rule.append(temp_model.from_map(k))
        return self


class ModifyPolicyGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPolicyGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyPolicyGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyPolicyGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPolicyGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyPolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScaleStrategyRequest(TeaModel):
    def __init__(self, region_id=None, scale_strategy_id=None, scale_strategy_name=None, scale_strategy_type=None,
                 min_desktops_count=None, max_desktops_count=None, min_available_desktops_count=None,
                 max_available_desktops_count=None, scale_step=None):
        self.region_id = region_id  # type: str
        self.scale_strategy_id = scale_strategy_id  # type: str
        self.scale_strategy_name = scale_strategy_name  # type: str
        self.scale_strategy_type = scale_strategy_type  # type: str
        self.min_desktops_count = min_desktops_count  # type: int
        self.max_desktops_count = max_desktops_count  # type: int
        self.min_available_desktops_count = min_available_desktops_count  # type: int
        self.max_available_desktops_count = max_available_desktops_count  # type: int
        self.scale_step = scale_step  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyScaleStrategyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scale_strategy_id is not None:
            result['ScaleStrategyId'] = self.scale_strategy_id
        if self.scale_strategy_name is not None:
            result['ScaleStrategyName'] = self.scale_strategy_name
        if self.scale_strategy_type is not None:
            result['ScaleStrategyType'] = self.scale_strategy_type
        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count
        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count
        if self.min_available_desktops_count is not None:
            result['MinAvailableDesktopsCount'] = self.min_available_desktops_count
        if self.max_available_desktops_count is not None:
            result['MaxAvailableDesktopsCount'] = self.max_available_desktops_count
        if self.scale_step is not None:
            result['ScaleStep'] = self.scale_step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScaleStrategyId') is not None:
            self.scale_strategy_id = m.get('ScaleStrategyId')
        if m.get('ScaleStrategyName') is not None:
            self.scale_strategy_name = m.get('ScaleStrategyName')
        if m.get('ScaleStrategyType') is not None:
            self.scale_strategy_type = m.get('ScaleStrategyType')
        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')
        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')
        if m.get('MinAvailableDesktopsCount') is not None:
            self.min_available_desktops_count = m.get('MinAvailableDesktopsCount')
        if m.get('MaxAvailableDesktopsCount') is not None:
            self.max_available_desktops_count = m.get('MaxAvailableDesktopsCount')
        if m.get('ScaleStep') is not None:
            self.scale_step = m.get('ScaleStep')
        return self


class ModifyScaleStrategyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyScaleStrategyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyScaleStrategyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyScaleStrategyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyScaleStrategyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyScaleStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserToDesktopGroupRequest(TeaModel):
    def __init__(self, region_id=None, desktop_group_id=None, old_end_user_ids=None, new_end_user_ids=None):
        self.region_id = region_id  # type: str
        self.desktop_group_id = desktop_group_id  # type: str
        self.old_end_user_ids = old_end_user_ids  # type: list[str]
        self.new_end_user_ids = new_end_user_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserToDesktopGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.old_end_user_ids is not None:
            result['OldEndUserIds'] = self.old_end_user_ids
        if self.new_end_user_ids is not None:
            result['NewEndUserIds'] = self.new_end_user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('OldEndUserIds') is not None:
            self.old_end_user_ids = m.get('OldEndUserIds')
        if m.get('NewEndUserIds') is not None:
            self.new_end_user_ids = m.get('NewEndUserIds')
        return self


class ModifyUserToDesktopGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserToDesktopGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyUserToDesktopGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyUserToDesktopGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyUserToDesktopGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyUserToDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateVulsRequest(TeaModel):
    def __init__(self, region_id=None, type=None, operate_type=None, reason=None, precondition=None, vul_name=None,
                 desktop_id=None):
        self.region_id = region_id  # type: str
        self.type = type  # type: str
        self.operate_type = operate_type  # type: str
        self.reason = reason  # type: str
        self.precondition = precondition  # type: int
        self.vul_name = vul_name  # type: list[str]
        self.desktop_id = desktop_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateVulsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.precondition is not None:
            result['Precondition'] = self.precondition
        if self.vul_name is not None:
            result['VulName'] = self.vul_name
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Precondition') is not None:
            self.precondition = m.get('Precondition')
        if m.get('VulName') is not None:
            self.vul_name = m.get('VulName')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class OperateVulsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OperateVulsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OperateVulsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: OperateVulsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OperateVulsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OperateVulsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PayOrderCallbackRequest(TeaModel):
    def __init__(self, data=None):
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PayOrderCallbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class PayOrderCallbackResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PayOrderCallbackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PayOrderCallbackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PayOrderCallbackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PayOrderCallbackResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PayOrderCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None):
        self.region_id = region_id  # type: str
        self.desktop_id = desktop_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebootDesktopsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class RebootDesktopsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebootDesktopsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RebootDesktopsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RebootDesktopsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RebootDesktopsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RebootDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebuildDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None):
        self.region_id = region_id  # type: str
        self.desktop_id = desktop_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebuildDesktopsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class RebuildDesktopsResponseBodyRebuildResults(TeaModel):
    def __init__(self, code=None, message=None, desktop_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.desktop_id = desktop_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebuildDesktopsResponseBodyRebuildResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class RebuildDesktopsResponseBody(TeaModel):
    def __init__(self, request_id=None, rebuild_results=None):
        self.request_id = request_id  # type: str
        self.rebuild_results = rebuild_results  # type: list[RebuildDesktopsResponseBodyRebuildResults]

    def validate(self):
        if self.rebuild_results:
            for k in self.rebuild_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RebuildDesktopsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RebuildResults'] = []
        if self.rebuild_results is not None:
            for k in self.rebuild_results:
                result['RebuildResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rebuild_results = []
        if m.get('RebuildResults') is not None:
            for k in m.get('RebuildResults'):
                temp_model = RebuildDesktopsResponseBodyRebuildResults()
                self.rebuild_results.append(temp_model.from_map(k))
        return self


class RebuildDesktopsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RebuildDesktopsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RebuildDesktopsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RebuildDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecreateDesktopGroupRequest(TeaModel):
    def __init__(self, region_id=None, desktop_group_id=None, own_bundle_id=None):
        self.region_id = region_id  # type: str
        self.desktop_group_id = desktop_group_id  # type: str
        self.own_bundle_id = own_bundle_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecreateDesktopGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.own_bundle_id is not None:
            result['OwnBundleId'] = self.own_bundle_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('OwnBundleId') is not None:
            self.own_bundle_id = m.get('OwnBundleId')
        return self


class RecreateDesktopGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecreateDesktopGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecreateDesktopGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecreateDesktopGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecreateDesktopGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RecreateDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserFromDesktopGroupRequest(TeaModel):
    def __init__(self, region_id=None, desktop_group_id=None, end_user_ids=None):
        self.region_id = region_id  # type: str
        self.desktop_group_id = desktop_group_id  # type: str
        self.end_user_ids = end_user_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUserFromDesktopGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        return self


class RemoveUserFromDesktopGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUserFromDesktopGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveUserFromDesktopGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveUserFromDesktopGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveUserFromDesktopGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveUserFromDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, period=None, period_unit=None, auto_pay=None, desktop_id=None):
        self.region_id = region_id  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.desktop_id = desktop_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewDesktopsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class RenewDesktopsResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewDesktopsResponseBody, self).to_map()
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


class RenewDesktopsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RenewDesktopsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenewDesktopsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenewDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetNASDefaultMountTargetRequest(TeaModel):
    def __init__(self, region_id=None, file_system_id=None):
        self.region_id = region_id  # type: str
        self.file_system_id = file_system_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetNASDefaultMountTargetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class ResetNASDefaultMountTargetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetNASDefaultMountTargetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetNASDefaultMountTargetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResetNASDefaultMountTargetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetNASDefaultMountTargetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetNASDefaultMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetSnapshotRequest(TeaModel):
    def __init__(self, region_id=None, snapshot_id=None):
        self.region_id = region_id  # type: str
        self.snapshot_id = snapshot_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetSnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class ResetSnapshotResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetSnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResetSnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetSnapshotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackSuspEventQuaraFileRequest(TeaModel):
    def __init__(self, region_id=None, quara_field_id=None, desktop_id=None):
        self.region_id = region_id  # type: str
        self.quara_field_id = quara_field_id  # type: int
        self.desktop_id = desktop_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RollbackSuspEventQuaraFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.quara_field_id is not None:
            result['QuaraFieldId'] = self.quara_field_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('QuaraFieldId') is not None:
            self.quara_field_id = m.get('QuaraFieldId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class RollbackSuspEventQuaraFileResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RollbackSuspEventQuaraFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RollbackSuspEventQuaraFileResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RollbackSuspEventQuaraFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RollbackSuspEventQuaraFileResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RollbackSuspEventQuaraFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCommandRequest(TeaModel):
    def __init__(self, region_id=None, type=None, command_content=None, timeout=None, content_encoding=None,
                 desktop_id=None):
        self.region_id = region_id  # type: str
        self.type = type  # type: str
        self.command_content = command_content  # type: str
        self.timeout = timeout  # type: long
        self.content_encoding = content_encoding  # type: str
        self.desktop_id = desktop_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunCommandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class RunCommandResponseBody(TeaModel):
    def __init__(self, invoke_id=None, request_id=None):
        self.invoke_id = invoke_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunCommandResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunCommandResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RunCommandResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RunCommandResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RunCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDirectorySsoStatusRequest(TeaModel):
    def __init__(self, region_id=None, directory_id=None, enable_sso=None):
        self.region_id = region_id  # type: str
        self.directory_id = directory_id  # type: str
        self.enable_sso = enable_sso  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDirectorySsoStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.enable_sso is not None:
            result['EnableSso'] = self.enable_sso
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EnableSso') is not None:
            self.enable_sso = m.get('EnableSso')
        return self


class SetDirectorySsoStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDirectorySsoStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDirectorySsoStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetDirectorySsoStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDirectorySsoStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetDirectorySsoStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetIdpMetadataRequest(TeaModel):
    def __init__(self, region_id=None, directory_id=None, office_site_id=None, idp_metadata=None):
        self.region_id = region_id  # type: str
        self.directory_id = directory_id  # type: str
        self.office_site_id = office_site_id  # type: str
        self.idp_metadata = idp_metadata  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetIdpMetadataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.idp_metadata is not None:
            result['IdpMetadata'] = self.idp_metadata
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('IdpMetadata') is not None:
            self.idp_metadata = m.get('IdpMetadata')
        return self


class SetIdpMetadataResponseBody(TeaModel):
    def __init__(self, idp_entity_id=None, request_id=None):
        self.idp_entity_id = idp_entity_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetIdpMetadataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_entity_id is not None:
            result['IdpEntityId'] = self.idp_entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdpEntityId') is not None:
            self.idp_entity_id = m.get('IdpEntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetIdpMetadataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetIdpMetadataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetIdpMetadataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetIdpMetadataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetOfficeSiteSsoStatusRequest(TeaModel):
    def __init__(self, region_id=None, office_site_id=None, enable_sso=None):
        self.region_id = region_id  # type: str
        self.office_site_id = office_site_id  # type: str
        self.enable_sso = enable_sso  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetOfficeSiteSsoStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.enable_sso is not None:
            result['EnableSso'] = self.enable_sso
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('EnableSso') is not None:
            self.enable_sso = m.get('EnableSso')
        return self


class SetOfficeSiteSsoStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetOfficeSiteSsoStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetOfficeSiteSsoStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetOfficeSiteSsoStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetOfficeSiteSsoStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetOfficeSiteSsoStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None):
        self.region_id = region_id  # type: str
        self.desktop_id = desktop_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDesktopsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class StartDesktopsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDesktopsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartDesktopsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartDesktopsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartDesktopsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartVirusScanTaskRequest(TeaModel):
    def __init__(self, region_id=None, office_site_id=None, desktop_id=None):
        self.region_id = region_id  # type: str
        self.office_site_id = office_site_id  # type: list[str]
        self.desktop_id = desktop_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartVirusScanTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class StartVirusScanTaskResponseBody(TeaModel):
    def __init__(self, scan_task_id=None, request_id=None):
        self.scan_task_id = scan_task_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartVirusScanTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartVirusScanTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartVirusScanTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartVirusScanTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartVirusScanTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, stopped_mode=None, desktop_id=None):
        self.region_id = region_id  # type: str
        self.stopped_mode = stopped_mode  # type: str
        self.desktop_id = desktop_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDesktopsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stopped_mode is not None:
            result['StoppedMode'] = self.stopped_mode
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StoppedMode') is not None:
            self.stopped_mode = m.get('StoppedMode')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class StopDesktopsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDesktopsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopDesktopsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopDesktopsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopDesktopsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInvocationRequest(TeaModel):
    def __init__(self, region_id=None, invoke_id=None, desktop_id=None):
        self.region_id = region_id  # type: str
        self.invoke_id = invoke_id  # type: str
        self.desktop_id = desktop_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopInvocationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class StopInvocationResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopInvocationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopInvocationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopInvocationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopInvocationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopInvocationResponseBody()
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
    def __init__(self, region_id=None, resource_type=None, resource_id=None, tag=None):
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: list[str]
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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


class UnlockVirtualMFADeviceRequest(TeaModel):
    def __init__(self, region_id=None, serial_number=None):
        self.region_id = region_id  # type: str
        self.serial_number = serial_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockVirtualMFADeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class UnlockVirtualMFADeviceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockVirtualMFADeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnlockVirtualMFADeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UnlockVirtualMFADeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnlockVirtualMFADeviceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnlockVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, all=None, resource_id=None, tag_key=None):
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.all = all  # type: bool
        self.resource_id = resource_id  # type: list[str]
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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


