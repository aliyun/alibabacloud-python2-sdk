# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class CreateADConnectorDirectoryRequest(TeaModel):
    def __init__(self, region_id=None, domain_name=None, domain_user_name=None, domain_password=None,
                 directory_name=None, enable_admin_access=None, desktop_access_type=None, sub_domain_name=None, dns_address=None,
                 v_switch_id=None, sub_domain_dns_address=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.domain_user_name = TeaConverter.to_unicode(domain_user_name)  # type: unicode
        self.domain_password = TeaConverter.to_unicode(domain_password)  # type: unicode
        self.directory_name = TeaConverter.to_unicode(directory_name)  # type: unicode
        self.enable_admin_access = enable_admin_access  # type: bool
        self.desktop_access_type = TeaConverter.to_unicode(desktop_access_type)  # type: unicode
        self.sub_domain_name = TeaConverter.to_unicode(sub_domain_name)  # type: unicode
        self.dns_address = dns_address  # type: list[unicode]
        self.v_switch_id = v_switch_id  # type: list[unicode]
        self.sub_domain_dns_address = sub_domain_dns_address  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('SubDomainDnsAddress') is not None:
            self.sub_domain_dns_address = m.get('SubDomainDnsAddress')
        return self


class CreateADConnectorDirectoryResponseBodyAdConnectors(TeaModel):
    def __init__(self, address=None):
        self.address = TeaConverter.to_unicode(address)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, trust_password=None, directory_id=None, request_id=None, ad_connectors=None):
        self.trust_password = TeaConverter.to_unicode(trust_password)  # type: unicode
        self.directory_id = TeaConverter.to_unicode(directory_id)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.ad_connectors = ad_connectors  # type: list[CreateADConnectorDirectoryResponseBodyAdConnectors]

    def validate(self):
        if self.ad_connectors:
            for k in self.ad_connectors:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.trust_password is not None:
            result['TrustPassword'] = self.trust_password
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AdConnectors'] = []
        if self.ad_connectors is not None:
            for k in self.ad_connectors:
                result['AdConnectors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TrustPassword') is not None:
            self.trust_password = m.get('TrustPassword')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.ad_connectors = []
        if m.get('AdConnectors') is not None:
            for k in m.get('AdConnectors'):
                temp_model = CreateADConnectorDirectoryResponseBodyAdConnectors()
                self.ad_connectors.append(temp_model.from_map(k))
        return self


class CreateADConnectorDirectoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateADConnectorDirectoryResponseBody

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
            temp_model = CreateADConnectorDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBundleRequest(TeaModel):
    def __init__(self, region_id=None, image_id=None, desktop_type=None, root_disk_size_gib=None, bundle_name=None,
                 description=None, user_disk_size_gib=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.image_id = TeaConverter.to_unicode(image_id)  # type: unicode
        self.desktop_type = TeaConverter.to_unicode(desktop_type)  # type: unicode
        self.root_disk_size_gib = root_disk_size_gib  # type: int
        self.bundle_name = TeaConverter.to_unicode(bundle_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.user_disk_size_gib = user_disk_size_gib  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
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
        self.bundle_id = TeaConverter.to_unicode(bundle_id)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateBundleResponseBody

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
            temp_model = CreateBundleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDesktopsRequestTag(TeaModel):
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


class CreateDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, group_id=None, bundle_id=None, system_disk_size=None, data_disk_size=None,
                 desktop_name=None, user_name=None, vpc_id=None, amount=None, directory_id=None, policy_group_id=None,
                 charge_type=None, period=None, period_unit=None, auto_pay=None, end_user_id=None, tag=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.group_id = TeaConverter.to_unicode(group_id)  # type: unicode
        self.bundle_id = TeaConverter.to_unicode(bundle_id)  # type: unicode
        self.system_disk_size = system_disk_size  # type: int
        self.data_disk_size = data_disk_size  # type: int
        self.desktop_name = TeaConverter.to_unicode(desktop_name)  # type: unicode
        self.user_name = TeaConverter.to_unicode(user_name)  # type: unicode
        self.vpc_id = TeaConverter.to_unicode(vpc_id)  # type: unicode
        self.amount = amount  # type: int
        self.directory_id = TeaConverter.to_unicode(directory_id)  # type: unicode
        self.policy_group_id = TeaConverter.to_unicode(policy_group_id)  # type: unicode
        self.charge_type = TeaConverter.to_unicode(charge_type)  # type: unicode
        self.period = period  # type: int
        self.period_unit = TeaConverter.to_unicode(period_unit)  # type: unicode
        self.auto_pay = auto_pay  # type: bool
        self.end_user_id = end_user_id  # type: list[unicode]
        self.tag = tag  # type: list[CreateDesktopsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
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
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
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
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateDesktopsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateDesktopsResponseBody(TeaModel):
    def __init__(self, request_id=None, desktop_id=None, order_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.desktop_id = desktop_id  # type: list[unicode]
        self.order_id = TeaConverter.to_unicode(order_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateDesktopsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateDesktopsResponseBody

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
            temp_model = CreateDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None, image_name=None, description=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.desktop_id = TeaConverter.to_unicode(desktop_id)  # type: unicode
        self.image_name = TeaConverter.to_unicode(image_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.description is not None:
            result['Description'] = self.description
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
        return self


class CreateImageResponseBody(TeaModel):
    def __init__(self, request_id=None, image_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.image_id = TeaConverter.to_unicode(image_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class CreateImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateImageResponseBody

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
            temp_model = CreateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyGroupRequest(TeaModel):
    def __init__(self, region_id=None, clipboard=None, local_drive=None, usb_redirect=None, watermark=None,
                 name=None, watermark_type=None, watermark_custom_text=None, watermark_transparency=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.clipboard = TeaConverter.to_unicode(clipboard)  # type: unicode
        self.local_drive = TeaConverter.to_unicode(local_drive)  # type: unicode
        self.usb_redirect = TeaConverter.to_unicode(usb_redirect)  # type: unicode
        self.watermark = TeaConverter.to_unicode(watermark)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.watermark_type = TeaConverter.to_unicode(watermark_type)  # type: unicode
        self.watermark_custom_text = TeaConverter.to_unicode(watermark_custom_text)  # type: unicode
        self.watermark_transparency = TeaConverter.to_unicode(watermark_transparency)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        if self.name is not None:
            result['Name'] = self.name
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        if self.watermark_custom_text is not None:
            result['WatermarkCustomText'] = self.watermark_custom_text
        if self.watermark_transparency is not None:
            result['WatermarkTransparency'] = self.watermark_transparency
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
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        if m.get('WatermarkCustomText') is not None:
            self.watermark_custom_text = m.get('WatermarkCustomText')
        if m.get('WatermarkTransparency') is not None:
            self.watermark_transparency = m.get('WatermarkTransparency')
        return self


class CreatePolicyGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, policy_group_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.policy_group_id = TeaConverter.to_unicode(policy_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        return self


class CreatePolicyGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreatePolicyGroupResponseBody

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
            temp_model = CreatePolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRAMDirectoryRequest(TeaModel):
    def __init__(self, region_id=None, directory_name=None, enable_internet_access=None, enable_admin_access=None,
                 desktop_access_type=None, v_switch_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.directory_name = TeaConverter.to_unicode(directory_name)  # type: unicode
        self.enable_internet_access = enable_internet_access  # type: bool
        self.enable_admin_access = enable_admin_access  # type: bool
        self.desktop_access_type = TeaConverter.to_unicode(desktop_access_type)  # type: unicode
        self.v_switch_id = v_switch_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
        self.directory_id = TeaConverter.to_unicode(directory_id)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateRAMDirectoryResponseBody

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
            temp_model = CreateRAMDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSnapshotRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None, snapshot_name=None, description=None, source_disk_type=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.desktop_id = TeaConverter.to_unicode(desktop_id)  # type: unicode
        self.snapshot_name = TeaConverter.to_unicode(snapshot_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.source_disk_type = TeaConverter.to_unicode(source_disk_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.snapshot_id = TeaConverter.to_unicode(snapshot_id)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateSnapshotResponseBody

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
            temp_model = CreateSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBundlesRequest(TeaModel):
    def __init__(self, region_id=None, bundle_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.bundle_id = bundle_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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


class DeleteBundlesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteBundlesResponseBody

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
            temp_model = DeleteBundlesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.desktop_id = desktop_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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


class DeleteDesktopsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteDesktopsResponseBody

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
            temp_model = DeleteDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDirectoriesRequest(TeaModel):
    def __init__(self, region_id=None, directory_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.directory_id = directory_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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


class DeleteDirectoriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteDirectoriesResponseBody

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
            temp_model = DeleteDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImagesRequest(TeaModel):
    def __init__(self, region_id=None, image_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.image_id = image_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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


class DeleteImagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteImagesResponseBody

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
            temp_model = DeleteImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyGroupsRequest(TeaModel):
    def __init__(self, region_id=None, policy_group_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.policy_group_id = policy_group_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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


class DeletePolicyGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeletePolicyGroupsResponseBody

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
            temp_model = DeletePolicyGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotRequest(TeaModel):
    def __init__(self, region_id=None, snapshot_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.snapshot_id = snapshot_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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


class DeleteSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteSnapshotResponseBody

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
            temp_model = DeleteSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVirtualMFADeviceRequest(TeaModel):
    def __init__(self, region_id=None, serial_number=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.serial_number = TeaConverter.to_unicode(serial_number)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class DeleteVirtualMFADeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteVirtualMFADeviceResponseBody

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
            temp_model = DeleteVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBundlesRequest(TeaModel):
    def __init__(self, region_id=None, max_results=None, next_token=None, user_name=None, category=None,
                 bundle_type=None, bundle_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.max_results = max_results  # type: int
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.user_name = TeaConverter.to_unicode(user_name)  # type: unicode
        self.category = TeaConverter.to_unicode(category)  # type: unicode
        self.bundle_type = TeaConverter.to_unicode(bundle_type)  # type: unicode
        self.bundle_id = bundle_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.category is not None:
            result['Category'] = self.category
        if self.bundle_type is not None:
            result['BundleType'] = self.bundle_type
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
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('BundleType') is not None:
            self.bundle_type = m.get('BundleType')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        return self


class DescribeBundlesResponseBodyBundlesDisks(TeaModel):
    def __init__(self, disk_size=None, disk_type=None):
        self.disk_size = disk_size  # type: int
        self.disk_type = TeaConverter.to_unicode(disk_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        return self


class DescribeBundlesResponseBodyBundlesDesktopTypeAttribute(TeaModel):
    def __init__(self, cpu_count=None, gpu_count=None, gpu_spec=None, memory_size=None):
        self.cpu_count = cpu_count  # type: int
        self.gpu_count = gpu_count  # type: int
        self.gpu_spec = TeaConverter.to_unicode(gpu_spec)  # type: unicode
        self.memory_size = memory_size  # type: int

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, disks=None, bundle_type=None, description=None, desktop_type=None,
                 desktop_type_attribute=None, bundle_id=None, image_id=None, bundle_name=None):
        self.disks = disks  # type: list[DescribeBundlesResponseBodyBundlesDisks]
        self.bundle_type = TeaConverter.to_unicode(bundle_type)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.desktop_type = TeaConverter.to_unicode(desktop_type)  # type: unicode
        self.desktop_type_attribute = desktop_type_attribute  # type: DescribeBundlesResponseBodyBundlesDesktopTypeAttribute
        self.bundle_id = TeaConverter.to_unicode(bundle_id)  # type: unicode
        self.image_id = TeaConverter.to_unicode(image_id)  # type: unicode
        self.bundle_name = TeaConverter.to_unicode(bundle_name)  # type: unicode

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()
        if self.desktop_type_attribute:
            self.desktop_type_attribute.validate()

    def to_map(self):
        result = dict()
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.bundle_type is not None:
            result['BundleType'] = self.bundle_type
        if self.description is not None:
            result['Description'] = self.description
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.desktop_type_attribute is not None:
            result['DesktopTypeAttribute'] = self.desktop_type_attribute.to_map()
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.bundle_name is not None:
            result['BundleName'] = self.bundle_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeBundlesResponseBodyBundlesDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('BundleType') is not None:
            self.bundle_type = m.get('BundleType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('DesktopTypeAttribute') is not None:
            temp_model = DescribeBundlesResponseBodyBundlesDesktopTypeAttribute()
            self.desktop_type_attribute = temp_model.from_map(m['DesktopTypeAttribute'])
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('BundleName') is not None:
            self.bundle_name = m.get('BundleName')
        return self


class DescribeBundlesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, bundles=None):
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.bundles = bundles  # type: list[DescribeBundlesResponseBodyBundles]

    def validate(self):
        if self.bundles:
            for k in self.bundles:
                if k:
                    k.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeBundlesResponseBody

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
            temp_model = DescribeBundlesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClientEventsRequest(TeaModel):
    def __init__(self, region_id=None, end_user_id=None, desktop_id=None, desktop_ip=None, directory_id=None,
                 event_type=None, start_time=None, end_time=None, max_results=None, next_token=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.end_user_id = TeaConverter.to_unicode(end_user_id)  # type: unicode
        self.desktop_id = TeaConverter.to_unicode(desktop_id)  # type: unicode
        self.desktop_ip = TeaConverter.to_unicode(desktop_ip)  # type: unicode
        self.directory_id = TeaConverter.to_unicode(directory_id)  # type: unicode
        self.event_type = TeaConverter.to_unicode(event_type)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.max_results = max_results  # type: int
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
                 ali_uid=None, desktop_id=None, region_id=None, event_id=None, directory_type=None, event_type=None,
                 end_user_id=None, client_ip=None, client_os=None, directory_id=None, client_version=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.bytes_received = TeaConverter.to_unicode(bytes_received)  # type: unicode
        self.desktop_ip = TeaConverter.to_unicode(desktop_ip)  # type: unicode
        self.event_time = TeaConverter.to_unicode(event_time)  # type: unicode
        self.bytes_send = TeaConverter.to_unicode(bytes_send)  # type: unicode
        self.ali_uid = TeaConverter.to_unicode(ali_uid)  # type: unicode
        self.desktop_id = TeaConverter.to_unicode(desktop_id)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.event_id = TeaConverter.to_unicode(event_id)  # type: unicode
        self.directory_type = TeaConverter.to_unicode(directory_type)  # type: unicode
        self.event_type = TeaConverter.to_unicode(event_type)  # type: unicode
        self.end_user_id = TeaConverter.to_unicode(end_user_id)  # type: unicode
        self.client_ip = TeaConverter.to_unicode(client_ip)  # type: unicode
        self.client_os = TeaConverter.to_unicode(client_os)  # type: unicode
        self.directory_id = TeaConverter.to_unicode(directory_id)  # type: unicode
        self.client_version = TeaConverter.to_unicode(client_version)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        return self


class DescribeClientEventsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, events=None):
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.events = events  # type: list[DescribeClientEventsResponseBodyEvents]

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeClientEventsResponseBody

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
            temp_model = DescribeClientEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopPolicysRequest(TeaModel):
    def __init__(self, region_id=None, next_token=None, max_results=None, desktop_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.max_results = max_results  # type: int
        self.desktop_id = desktop_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
        self.usb_redirect = TeaConverter.to_unicode(usb_redirect)  # type: unicode
        self.desktop_id = TeaConverter.to_unicode(desktop_id)  # type: unicode
        self.watermark = TeaConverter.to_unicode(watermark)  # type: unicode
        self.clipboard = TeaConverter.to_unicode(clipboard)  # type: unicode
        self.local_drive = TeaConverter.to_unicode(local_drive)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.describe_desktop_policys = describe_desktop_policys  # type: list[DescribeDesktopPolicysResponseBodyDescribeDesktopPolicys]

    def validate(self):
        if self.describe_desktop_policys:
            for k in self.describe_desktop_policys:
                if k:
                    k.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDesktopPolicysResponseBody

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
            temp_model = DescribeDesktopPolicysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, group_id=None, desktop_status=None, max_results=None, next_token=None,
                 user_name=None, desktop_name=None, directory_id=None, policy_group_id=None, desktop_id=None,
                 end_user_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.group_id = TeaConverter.to_unicode(group_id)  # type: unicode
        self.desktop_status = TeaConverter.to_unicode(desktop_status)  # type: unicode
        self.max_results = max_results  # type: int
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.user_name = TeaConverter.to_unicode(user_name)  # type: unicode
        self.desktop_name = TeaConverter.to_unicode(desktop_name)  # type: unicode
        self.directory_id = TeaConverter.to_unicode(directory_id)  # type: unicode
        self.policy_group_id = TeaConverter.to_unicode(policy_group_id)  # type: unicode
        self.desktop_id = desktop_id  # type: list[unicode]
        self.end_user_id = end_user_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
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
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        return self


class DescribeDesktopsResponseBodyDesktopsTags(TeaModel):
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


class DescribeDesktopsResponseBodyDesktopsDisks(TeaModel):
    def __init__(self, disk_size=None, disk_type=None, disk_id=None):
        self.disk_size = disk_size  # type: int
        self.disk_type = TeaConverter.to_unicode(disk_type)  # type: unicode
        self.disk_id = TeaConverter.to_unicode(disk_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        return self


class DescribeDesktopsResponseBodyDesktops(TeaModel):
    def __init__(self, creation_time=None, charge_type=None, desktop_name=None, tags=None, disks=None,
                 system_disk_size=None, policy_group_id=None, desktop_status=None, desktop_type=None, gpu_count=None, memory=None,
                 gpu_spec=None, image_id=None, directory_id=None, data_disk_category=None, system_disk_category=None,
                 network_interface_id=None, data_disk_size=None, desktop_id=None, end_user_ids=None, start_time=None, cpu=None,
                 expired_time=None, connection_status=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.charge_type = TeaConverter.to_unicode(charge_type)  # type: unicode
        self.desktop_name = TeaConverter.to_unicode(desktop_name)  # type: unicode
        self.tags = tags  # type: list[DescribeDesktopsResponseBodyDesktopsTags]
        self.disks = disks  # type: list[DescribeDesktopsResponseBodyDesktopsDisks]
        self.system_disk_size = system_disk_size  # type: int
        self.policy_group_id = TeaConverter.to_unicode(policy_group_id)  # type: unicode
        self.desktop_status = TeaConverter.to_unicode(desktop_status)  # type: unicode
        self.desktop_type = TeaConverter.to_unicode(desktop_type)  # type: unicode
        self.gpu_count = gpu_count  # type: int
        self.memory = memory  # type: long
        self.gpu_spec = TeaConverter.to_unicode(gpu_spec)  # type: unicode
        self.image_id = TeaConverter.to_unicode(image_id)  # type: unicode
        self.directory_id = TeaConverter.to_unicode(directory_id)  # type: unicode
        self.data_disk_category = TeaConverter.to_unicode(data_disk_category)  # type: unicode
        self.system_disk_category = TeaConverter.to_unicode(system_disk_category)  # type: unicode
        self.network_interface_id = network_interface_id  # type: long
        self.data_disk_size = TeaConverter.to_unicode(data_disk_size)  # type: unicode
        self.desktop_id = TeaConverter.to_unicode(desktop_id)  # type: unicode
        self.end_user_ids = end_user_ids  # type: list[unicode]
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.cpu = cpu  # type: int
        self.expired_time = TeaConverter.to_unicode(expired_time)  # type: unicode
        self.connection_status = TeaConverter.to_unicode(connection_status)  # type: unicode

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
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
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDesktopsResponseBodyDesktopsTags()
                self.tags.append(temp_model.from_map(k))
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeDesktopsResponseBodyDesktopsDisks()
                self.disks.append(temp_model.from_map(k))
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
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        return self


class DescribeDesktopsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, desktops=None):
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.desktops = desktops  # type: list[DescribeDesktopsResponseBodyDesktops]

    def validate(self):
        if self.desktops:
            for k in self.desktops:
                if k:
                    k.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDesktopsResponseBody

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
            temp_model = DescribeDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopTypesRequest(TeaModel):
    def __init__(self, region_id=None, desktop_type_id=None, instance_type_family=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.desktop_type_id = TeaConverter.to_unicode(desktop_type_id)  # type: unicode
        self.instance_type_family = TeaConverter.to_unicode(instance_type_family)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_type_id is not None:
            result['DesktopTypeId'] = self.desktop_type_id
        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopTypeId') is not None:
            self.desktop_type_id = m.get('DesktopTypeId')
        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')
        return self


class DescribeDesktopTypesResponseBodyDesktopTypesAllowDiskSize(TeaModel):
    def __init__(self, system_disk_size=None, data_disk_size=None):
        self.system_disk_size = system_disk_size  # type: int
        self.data_disk_size = data_disk_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        return self


class DescribeDesktopTypesResponseBodyDesktopTypes(TeaModel):
    def __init__(self, system_disk_size=None, desktop_type_id=None, data_disk_size=None, cpu_count=None,
                 gpu_count=None, gpu_spec=None, instance_type_family=None, memory_size=None, allow_disk_size=None):
        self.system_disk_size = TeaConverter.to_unicode(system_disk_size)  # type: unicode
        self.desktop_type_id = TeaConverter.to_unicode(desktop_type_id)  # type: unicode
        self.data_disk_size = TeaConverter.to_unicode(data_disk_size)  # type: unicode
        self.cpu_count = TeaConverter.to_unicode(cpu_count)  # type: unicode
        self.gpu_count = gpu_count  # type: int
        self.gpu_spec = TeaConverter.to_unicode(gpu_spec)  # type: unicode
        self.instance_type_family = TeaConverter.to_unicode(instance_type_family)  # type: unicode
        self.memory_size = TeaConverter.to_unicode(memory_size)  # type: unicode
        self.allow_disk_size = allow_disk_size  # type: list[DescribeDesktopTypesResponseBodyDesktopTypesAllowDiskSize]

    def validate(self):
        if self.allow_disk_size:
            for k in self.allow_disk_size:
                if k:
                    k.validate()

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.desktop_types = desktop_types  # type: list[DescribeDesktopTypesResponseBodyDesktopTypes]

    def validate(self):
        if self.desktop_types:
            for k in self.desktop_types:
                if k:
                    k.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDesktopTypesResponseBody

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
            temp_model = DescribeDesktopTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDirectoriesRequest(TeaModel):
    def __init__(self, region_id=None, directory_type=None, max_results=None, next_token=None, directory_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.directory_type = TeaConverter.to_unicode(directory_type)  # type: unicode
        self.max_results = max_results  # type: int
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.directory_id = directory_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
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
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class DescribeDirectoriesResponseBodyDirectoriesLogs(TeaModel):
    def __init__(self, step=None, message=None, time_stamp=None, level=None):
        self.step = TeaConverter.to_unicode(step)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.time_stamp = TeaConverter.to_unicode(time_stamp)  # type: unicode
        self.level = TeaConverter.to_unicode(level)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class DescribeDirectoriesResponseBodyDirectoriesADConnectors(TeaModel):
    def __init__(self, connector_status=None, v_switch_id=None, network_interface_id=None,
                 adconnector_address=None):
        self.connector_status = TeaConverter.to_unicode(connector_status)  # type: unicode
        self.v_switch_id = TeaConverter.to_unicode(v_switch_id)  # type: unicode
        self.network_interface_id = TeaConverter.to_unicode(network_interface_id)  # type: unicode
        self.adconnector_address = TeaConverter.to_unicode(adconnector_address)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.connector_status is not None:
            result['ConnectorStatus'] = self.connector_status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.adconnector_address is not None:
            result['ADConnectorAddress'] = self.adconnector_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectorStatus') is not None:
            self.connector_status = m.get('ConnectorStatus')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('ADConnectorAddress') is not None:
            self.adconnector_address = m.get('ADConnectorAddress')
        return self


class DescribeDirectoriesResponseBodyDirectories(TeaModel):
    def __init__(self, enable_internet_access=None, vpc_id=None, creation_time=None, status=None,
                 domain_password=None, custom_security_group_id=None, domain_user_name=None, desktop_vpc_endpoint=None,
                 desktop_access_type=None, domain_name=None, directory_type=None, dns_user_name=None, logs=None, trust_password=None,
                 v_switch_ids=None, name=None, adconnectors=None, dns_address=None, directory_id=None):
        self.enable_internet_access = enable_internet_access  # type: bool
        self.vpc_id = TeaConverter.to_unicode(vpc_id)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.domain_password = TeaConverter.to_unicode(domain_password)  # type: unicode
        self.custom_security_group_id = TeaConverter.to_unicode(custom_security_group_id)  # type: unicode
        self.domain_user_name = TeaConverter.to_unicode(domain_user_name)  # type: unicode
        self.desktop_vpc_endpoint = TeaConverter.to_unicode(desktop_vpc_endpoint)  # type: unicode
        self.desktop_access_type = TeaConverter.to_unicode(desktop_access_type)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.directory_type = TeaConverter.to_unicode(directory_type)  # type: unicode
        self.dns_user_name = TeaConverter.to_unicode(dns_user_name)  # type: unicode
        self.logs = logs  # type: list[DescribeDirectoriesResponseBodyDirectoriesLogs]
        self.trust_password = TeaConverter.to_unicode(trust_password)  # type: unicode
        self.v_switch_ids = v_switch_ids  # type: list[unicode]
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.adconnectors = adconnectors  # type: list[DescribeDirectoriesResponseBodyDirectoriesADConnectors]
        self.dns_address = dns_address  # type: list[unicode]
        self.directory_id = TeaConverter.to_unicode(directory_id)  # type: unicode

    def validate(self):
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()
        if self.adconnectors:
            for k in self.adconnectors:
                if k:
                    k.validate()

    def to_map(self):
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
        if self.custom_security_group_id is not None:
            result['CustomSecurityGroupId'] = self.custom_security_group_id
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.desktop_vpc_endpoint is not None:
            result['DesktopVpcEndpoint'] = self.desktop_vpc_endpoint
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.dns_user_name is not None:
            result['DnsUserName'] = self.dns_user_name
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.trust_password is not None:
            result['TrustPassword'] = self.trust_password
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.name is not None:
            result['Name'] = self.name
        result['ADConnectors'] = []
        if self.adconnectors is not None:
            for k in self.adconnectors:
                result['ADConnectors'].append(k.to_map() if k else None)
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
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
        if m.get('CustomSecurityGroupId') is not None:
            self.custom_security_group_id = m.get('CustomSecurityGroupId')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('DesktopVpcEndpoint') is not None:
            self.desktop_vpc_endpoint = m.get('DesktopVpcEndpoint')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('DnsUserName') is not None:
            self.dns_user_name = m.get('DnsUserName')
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = DescribeDirectoriesResponseBodyDirectoriesLogs()
                self.logs.append(temp_model.from_map(k))
        if m.get('TrustPassword') is not None:
            self.trust_password = m.get('TrustPassword')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.adconnectors = []
        if m.get('ADConnectors') is not None:
            for k in m.get('ADConnectors'):
                temp_model = DescribeDirectoriesResponseBodyDirectoriesADConnectors()
                self.adconnectors.append(temp_model.from_map(k))
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class DescribeDirectoriesResponseBody(TeaModel):
    def __init__(self, directories=None, next_token=None, request_id=None):
        self.directories = directories  # type: list[DescribeDirectoriesResponseBodyDirectories]
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.directories:
            for k in self.directories:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Directories'] = []
        if self.directories is not None:
            for k in self.directories:
                result['Directories'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.directories = []
        if m.get('Directories') is not None:
            for k in m.get('Directories'):
                temp_model = DescribeDirectoriesResponseBodyDirectories()
                self.directories.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDirectoriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeDirectoriesResponseBody

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
            temp_model = DescribeDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImagesRequest(TeaModel):
    def __init__(self, region_id=None, max_results=None, next_token=None, image_type=None, image_status=None,
                 gpu_category=None, image_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.max_results = max_results  # type: int
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.image_type = TeaConverter.to_unicode(image_type)  # type: unicode
        self.image_status = TeaConverter.to_unicode(image_status)  # type: unicode
        self.gpu_category = gpu_category  # type: bool
        self.image_id = image_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class DescribeImagesResponseBodyImages(TeaModel):
    def __init__(self, status=None, creation_time=None, image_type=None, progress=None, description=None, size=None,
                 os_type=None, data_disk_size=None, name=None, gpu_category=None, image_id=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.image_type = TeaConverter.to_unicode(image_type)  # type: unicode
        self.progress = TeaConverter.to_unicode(progress)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.size = size  # type: int
        self.os_type = TeaConverter.to_unicode(os_type)  # type: unicode
        self.data_disk_size = data_disk_size  # type: int
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.gpu_category = gpu_category  # type: bool
        self.image_id = TeaConverter.to_unicode(image_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.description is not None:
            result['Description'] = self.description
        if self.size is not None:
            result['Size'] = self.size
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.name is not None:
            result['Name'] = self.name
        if self.gpu_category is not None:
            result['GpuCategory'] = self.gpu_category
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('GpuCategory') is not None:
            self.gpu_category = m.get('GpuCategory')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class DescribeImagesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, images=None):
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.images = images  # type: list[DescribeImagesResponseBodyImages]

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeImagesResponseBody

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
            temp_model = DescribeImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInvocationsRequest(TeaModel):
    def __init__(self, region_id=None, invoke_id=None, command_type=None, invoke_status=None, desktop_id=None,
                 include_output=None, content_encoding=None, max_results=None, next_token=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.invoke_id = TeaConverter.to_unicode(invoke_id)  # type: unicode
        self.command_type = TeaConverter.to_unicode(command_type)  # type: unicode
        self.invoke_status = TeaConverter.to_unicode(invoke_status)  # type: unicode
        self.desktop_id = TeaConverter.to_unicode(desktop_id)  # type: unicode
        self.include_output = include_output  # type: bool
        self.content_encoding = TeaConverter.to_unicode(content_encoding)  # type: unicode
        self.max_results = max_results  # type: int
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, creation_time=None, update_time=None, finish_time=None, invocation_status=None, repeats=None,
                 output=None, desktop_id=None, dropped=None, stop_time=None, exit_code=None, start_time=None,
                 error_info=None, error_code=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.update_time = TeaConverter.to_unicode(update_time)  # type: unicode
        self.finish_time = TeaConverter.to_unicode(finish_time)  # type: unicode
        self.invocation_status = TeaConverter.to_unicode(invocation_status)  # type: unicode
        self.repeats = repeats  # type: int
        self.output = TeaConverter.to_unicode(output)  # type: unicode
        self.desktop_id = TeaConverter.to_unicode(desktop_id)  # type: unicode
        self.dropped = dropped  # type: int
        self.stop_time = TeaConverter.to_unicode(stop_time)  # type: unicode
        self.exit_code = exit_code  # type: long
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.error_info = TeaConverter.to_unicode(error_info)  # type: unicode
        self.error_code = TeaConverter.to_unicode(error_code)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.repeats is not None:
            result['Repeats'] = self.repeats
        if self.output is not None:
            result['Output'] = self.output
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
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
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('Repeats') is not None:
            self.repeats = m.get('Repeats')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
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
    def __init__(self, creation_time=None, invocation_status=None, invoke_desktops=None, command_content=None,
                 invoke_id=None, command_type=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.invocation_status = TeaConverter.to_unicode(invocation_status)  # type: unicode
        self.invoke_desktops = invoke_desktops  # type: list[DescribeInvocationsResponseBodyInvocationsInvokeDesktops]
        self.command_content = TeaConverter.to_unicode(command_content)  # type: unicode
        self.invoke_id = TeaConverter.to_unicode(invoke_id)  # type: unicode
        self.command_type = TeaConverter.to_unicode(command_type)  # type: unicode

    def validate(self):
        if self.invoke_desktops:
            for k in self.invoke_desktops:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        result['InvokeDesktops'] = []
        if self.invoke_desktops is not None:
            for k in self.invoke_desktops:
                result['InvokeDesktops'].append(k.to_map() if k else None)
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.command_type is not None:
            result['CommandType'] = self.command_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        self.invoke_desktops = []
        if m.get('InvokeDesktops') is not None:
            for k in m.get('InvokeDesktops'):
                temp_model = DescribeInvocationsResponseBodyInvocationsInvokeDesktops()
                self.invoke_desktops.append(temp_model.from_map(k))
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')
        return self


class DescribeInvocationsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, invocations=None):
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.invocations = invocations  # type: list[DescribeInvocationsResponseBodyInvocations]

    def validate(self):
        if self.invocations:
            for k in self.invocations:
                if k:
                    k.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeInvocationsResponseBody

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
            temp_model = DescribeInvocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyGroupsRequest(TeaModel):
    def __init__(self, region_id=None, max_results=None, next_token=None, policy_group_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.max_results = max_results  # type: int
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.policy_group_id = policy_group_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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


class DescribePolicyGroupsResponseBodyDescribePolicyGroups(TeaModel):
    def __init__(self, policy_status=None, watermark_type=None, policy_group_id=None, watermark_transparency=None,
                 usb_redirect=None, policy_group_type=None, watermark_custom_text=None, watermark=None, clipboard=None,
                 name=None, local_drive=None):
        self.policy_status = TeaConverter.to_unicode(policy_status)  # type: unicode
        self.watermark_type = TeaConverter.to_unicode(watermark_type)  # type: unicode
        self.policy_group_id = TeaConverter.to_unicode(policy_group_id)  # type: unicode
        self.watermark_transparency = TeaConverter.to_unicode(watermark_transparency)  # type: unicode
        self.usb_redirect = TeaConverter.to_unicode(usb_redirect)  # type: unicode
        self.policy_group_type = TeaConverter.to_unicode(policy_group_type)  # type: unicode
        self.watermark_custom_text = TeaConverter.to_unicode(watermark_custom_text)  # type: unicode
        self.watermark = TeaConverter.to_unicode(watermark)  # type: unicode
        self.clipboard = TeaConverter.to_unicode(clipboard)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.local_drive = TeaConverter.to_unicode(local_drive)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.watermark_transparency is not None:
            result['WatermarkTransparency'] = self.watermark_transparency
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.policy_group_type is not None:
            result['PolicyGroupType'] = self.policy_group_type
        if self.watermark_custom_text is not None:
            result['WatermarkCustomText'] = self.watermark_custom_text
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.name is not None:
            result['Name'] = self.name
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('WatermarkTransparency') is not None:
            self.watermark_transparency = m.get('WatermarkTransparency')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('PolicyGroupType') is not None:
            self.policy_group_type = m.get('PolicyGroupType')
        if m.get('WatermarkCustomText') is not None:
            self.watermark_custom_text = m.get('WatermarkCustomText')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        return self


class DescribePolicyGroupsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, describe_policy_groups=None):
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.describe_policy_groups = describe_policy_groups  # type: list[DescribePolicyGroupsResponseBodyDescribePolicyGroups]

    def validate(self):
        if self.describe_policy_groups:
            for k in self.describe_policy_groups:
                if k:
                    k.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribePolicyGroupsResponseBody

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
            temp_model = DescribePolicyGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.region_endpoint = TeaConverter.to_unicode(region_endpoint)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeRegionsResponseBody

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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSnapshotsRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None, snapshot_id=None, max_results=None, next_token=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.desktop_id = TeaConverter.to_unicode(desktop_id)  # type: unicode
        self.snapshot_id = TeaConverter.to_unicode(snapshot_id)  # type: unicode
        self.max_results = max_results  # type: int
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.snapshot_type = TeaConverter.to_unicode(snapshot_type)  # type: unicode
        self.snapshot_name = TeaConverter.to_unicode(snapshot_name)  # type: unicode
        self.progress = TeaConverter.to_unicode(progress)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.snapshot_id = TeaConverter.to_unicode(snapshot_id)  # type: unicode
        self.remain_time = remain_time  # type: int
        self.source_disk_size = TeaConverter.to_unicode(source_disk_size)  # type: unicode
        self.source_disk_type = TeaConverter.to_unicode(source_disk_type)  # type: unicode
        self.desktop_id = TeaConverter.to_unicode(desktop_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.snapshots = snapshots  # type: list[DescribeSnapshotsResponseBodySnapshots]

    def validate(self):
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeSnapshotsResponseBody

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
            temp_model = DescribeSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVirtualMFADevicesRequest(TeaModel):
    def __init__(self, region_id=None, max_results=None, next_token=None, directory_id=None, end_user_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.max_results = max_results  # type: int
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.directory_id = TeaConverter.to_unicode(directory_id)  # type: unicode
        self.end_user_id = end_user_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
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
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        return self


class DescribeVirtualMFADevicesResponseBodyVirtualMFADevices(TeaModel):
    def __init__(self, gmt_unlock=None, serial_number=None, end_user_id=None, consecutive_fails=None, status=None,
                 directory_id=None, gmt_enabled=None):
        self.gmt_unlock = TeaConverter.to_unicode(gmt_unlock)  # type: unicode
        self.serial_number = TeaConverter.to_unicode(serial_number)  # type: unicode
        self.end_user_id = TeaConverter.to_unicode(end_user_id)  # type: unicode
        self.consecutive_fails = consecutive_fails  # type: int
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.directory_id = TeaConverter.to_unicode(directory_id)  # type: unicode
        self.gmt_enabled = TeaConverter.to_unicode(gmt_enabled)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_unlock is not None:
            result['GmtUnlock'] = self.gmt_unlock
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.consecutive_fails is not None:
            result['ConsecutiveFails'] = self.consecutive_fails
        if self.status is not None:
            result['status'] = self.status
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.gmt_enabled is not None:
            result['GmtEnabled'] = self.gmt_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtUnlock') is not None:
            self.gmt_unlock = m.get('GmtUnlock')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ConsecutiveFails') is not None:
            self.consecutive_fails = m.get('ConsecutiveFails')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('GmtEnabled') is not None:
            self.gmt_enabled = m.get('GmtEnabled')
        return self


class DescribeVirtualMFADevicesResponseBody(TeaModel):
    def __init__(self, virtual_mfadevices=None, next_token=None, request_id=None):
        self.virtual_mfadevices = virtual_mfadevices  # type: list[DescribeVirtualMFADevicesResponseBodyVirtualMFADevices]
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.virtual_mfadevices:
            for k in self.virtual_mfadevices:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VirtualMFADevices'] = []
        if self.virtual_mfadevices is not None:
            for k in self.virtual_mfadevices:
                result['VirtualMFADevices'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.virtual_mfadevices = []
        if m.get('VirtualMFADevices') is not None:
            for k in m.get('VirtualMFADevices'):
                temp_model = DescribeVirtualMFADevicesResponseBodyVirtualMFADevices()
                self.virtual_mfadevices.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVirtualMFADevicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVirtualMFADevicesResponseBody

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
            temp_model = DescribeVirtualMFADevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.zone_id = TeaConverter.to_unicode(zone_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.zones = zones  # type: list[DescribeZonesResponseBodyZones]

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeZonesResponseBody

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
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoCheckResourceRequest(TeaModel):
    def __init__(self, invoker=None, pk=None, bid=None, hid=None, country=None, task_identifier=None,
                 task_extra_data=None, gmt_wakeup=None, region_id=None):
        self.invoker = TeaConverter.to_unicode(invoker)  # type: unicode
        self.pk = TeaConverter.to_unicode(pk)  # type: unicode
        self.bid = TeaConverter.to_unicode(bid)  # type: unicode
        self.hid = hid  # type: long
        self.country = TeaConverter.to_unicode(country)  # type: unicode
        self.task_identifier = TeaConverter.to_unicode(task_identifier)  # type: unicode
        self.task_extra_data = TeaConverter.to_unicode(task_extra_data)  # type: unicode
        self.gmt_wakeup = TeaConverter.to_unicode(gmt_wakeup)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.gmt_wakeup = TeaConverter.to_unicode(gmt_wakeup)  # type: unicode
        self.hid = hid  # type: long
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.task_identifier = TeaConverter.to_unicode(task_identifier)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.success = success  # type: bool
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.interrupt = interrupt  # type: bool
        self.invoker = TeaConverter.to_unicode(invoker)  # type: unicode
        self.task_extra_data = TeaConverter.to_unicode(task_extra_data)  # type: unicode
        self.country = TeaConverter.to_unicode(country)  # type: unicode
        self.prompt = TeaConverter.to_unicode(prompt)  # type: unicode
        self.level = level  # type: long
        self.pk = TeaConverter.to_unicode(pk)  # type: unicode
        self.bid = TeaConverter.to_unicode(bid)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DoCheckResourceResponseBody

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
            temp_model = DoCheckResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoLogicalDeleteResourceRequest(TeaModel):
    def __init__(self, invoker=None, pk=None, bid=None, hid=None, country=None, task_identifier=None,
                 task_extra_data=None, gmt_wakeup=None, region_id=None):
        self.invoker = TeaConverter.to_unicode(invoker)  # type: unicode
        self.pk = TeaConverter.to_unicode(pk)  # type: unicode
        self.bid = TeaConverter.to_unicode(bid)  # type: unicode
        self.hid = hid  # type: long
        self.country = TeaConverter.to_unicode(country)  # type: unicode
        self.task_identifier = TeaConverter.to_unicode(task_identifier)  # type: unicode
        self.task_extra_data = TeaConverter.to_unicode(task_extra_data)  # type: unicode
        self.gmt_wakeup = TeaConverter.to_unicode(gmt_wakeup)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.gmt_wakeup = TeaConverter.to_unicode(gmt_wakeup)  # type: unicode
        self.hid = hid  # type: long
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.task_identifier = TeaConverter.to_unicode(task_identifier)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.invoker = TeaConverter.to_unicode(invoker)  # type: unicode
        self.task_extra_data = TeaConverter.to_unicode(task_extra_data)  # type: unicode
        self.country = TeaConverter.to_unicode(country)  # type: unicode
        self.pk = TeaConverter.to_unicode(pk)  # type: unicode
        self.bid = TeaConverter.to_unicode(bid)  # type: unicode
        self.success = success  # type: bool
        self.interrupt = interrupt  # type: bool

    def validate(self):
        pass

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DoLogicalDeleteResourceResponseBody

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
            temp_model = DoLogicalDeleteResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoPhysicalDeleteResourceRequest(TeaModel):
    def __init__(self, invoker=None, pk=None, bid=None, hid=None, country=None, task_identifier=None,
                 task_extra_data=None, gmt_wakeup=None, region_id=None):
        self.invoker = TeaConverter.to_unicode(invoker)  # type: unicode
        self.pk = TeaConverter.to_unicode(pk)  # type: unicode
        self.bid = TeaConverter.to_unicode(bid)  # type: unicode
        self.hid = hid  # type: long
        self.country = TeaConverter.to_unicode(country)  # type: unicode
        self.task_identifier = TeaConverter.to_unicode(task_identifier)  # type: unicode
        self.task_extra_data = TeaConverter.to_unicode(task_extra_data)  # type: unicode
        self.gmt_wakeup = TeaConverter.to_unicode(gmt_wakeup)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.gmt_wakeup = TeaConverter.to_unicode(gmt_wakeup)  # type: unicode
        self.hid = hid  # type: long
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.task_identifier = TeaConverter.to_unicode(task_identifier)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.invoker = TeaConverter.to_unicode(invoker)  # type: unicode
        self.task_extra_data = TeaConverter.to_unicode(task_extra_data)  # type: unicode
        self.country = TeaConverter.to_unicode(country)  # type: unicode
        self.pk = TeaConverter.to_unicode(pk)  # type: unicode
        self.bid = TeaConverter.to_unicode(bid)  # type: unicode
        self.success = success  # type: bool
        self.interrupt = interrupt  # type: bool

    def validate(self):
        pass

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DoPhysicalDeleteResourceResponseBody

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
            temp_model = DoPhysicalDeleteResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConnectionTicketRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, region_id=None,
                 instance_id=None, user_name=None, password=None, task_id=None, desktop_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.user_name = TeaConverter.to_unicode(user_name)  # type: unicode
        self.password = TeaConverter.to_unicode(password)  # type: unicode
        self.task_id = TeaConverter.to_unicode(task_id)  # type: unicode
        self.desktop_id = TeaConverter.to_unicode(desktop_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.ticket = TeaConverter.to_unicode(ticket)  # type: unicode
        self.task_id = TeaConverter.to_unicode(task_id)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.task_status = TeaConverter.to_unicode(task_status)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetConnectionTicketResponseBody

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
            temp_model = GetConnectionTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDirectoryUsersRequest(TeaModel):
    def __init__(self, region_id=None, filter=None, directory_id=None, next_token=None, max_results=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.filter = TeaConverter.to_unicode(filter)  # type: unicode
        self.directory_id = TeaConverter.to_unicode(directory_id)  # type: unicode
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.max_results = max_results  # type: int

    def validate(self):
        pass

    def to_map(self):
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
        self.end_user = TeaConverter.to_unicode(end_user)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.users = users  # type: list[ListDirectoryUsersResponseBodyUsers]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListDirectoryUsersResponseBody

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
            temp_model = ListDirectoryUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
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


class ListTagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, next_token=None, resource_id=None, tag=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.resource_id = resource_id  # type: list[unicode]
        self.tag = tag  # type: list[ListTagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
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


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        self.next_token = TeaConverter.to_unicode(next_token)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.tag_resources = tag_resources  # type: list[ListTagResourcesResponseBodyTagResources]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListTagResourcesResponseBody

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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockVirtualMFADeviceRequest(TeaModel):
    def __init__(self, region_id=None, serial_number=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.serial_number = TeaConverter.to_unicode(serial_number)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class LockVirtualMFADeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: LockVirtualMFADeviceResponseBody

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
            temp_model = LockVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyADConnectorDirectoryRequest(TeaModel):
    def __init__(self, region_id=None, directory_id=None, domain_name=None, domain_user_name=None,
                 domain_password=None, directory_name=None, sub_domain_name=None, mfa_enabled=None, dns_address=None,
                 sub_domain_dns_address=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.directory_id = TeaConverter.to_unicode(directory_id)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.domain_user_name = TeaConverter.to_unicode(domain_user_name)  # type: unicode
        self.domain_password = TeaConverter.to_unicode(domain_password)  # type: unicode
        self.directory_name = TeaConverter.to_unicode(directory_name)  # type: unicode
        self.sub_domain_name = TeaConverter.to_unicode(sub_domain_name)  # type: unicode
        self.mfa_enabled = mfa_enabled  # type: bool
        self.dns_address = dns_address  # type: list[unicode]
        self.sub_domain_dns_address = sub_domain_dns_address  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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


class ModifyADConnectorDirectoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyADConnectorDirectoryResponseBody

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
            temp_model = ModifyADConnectorDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopNameRequest(TeaModel):
    def __init__(self, region_id=None, new_desktop_name=None, desktop_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.new_desktop_name = TeaConverter.to_unicode(new_desktop_name)  # type: unicode
        self.desktop_id = TeaConverter.to_unicode(desktop_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class ModifyDesktopNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDesktopNameResponseBody

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
            temp_model = ModifyDesktopNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopPolicysRequest(TeaModel):
    def __init__(self, region_id=None, clipboard=None, local_drive=None, usb_redirect=None, watermark=None,
                 desktop_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.clipboard = TeaConverter.to_unicode(clipboard)  # type: unicode
        self.local_drive = TeaConverter.to_unicode(local_drive)  # type: unicode
        self.usb_redirect = TeaConverter.to_unicode(usb_redirect)  # type: unicode
        self.watermark = TeaConverter.to_unicode(watermark)  # type: unicode
        self.desktop_id = desktop_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
        self.success = TeaConverter.to_unicode(success)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.desktop_id = TeaConverter.to_unicode(desktop_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.results = results  # type: list[ModifyDesktopPolicysResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDesktopPolicysResponseBody

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
            temp_model = ModifyDesktopPolicysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopsPolicyGroupRequest(TeaModel):
    def __init__(self, region_id=None, policy_group_id=None, desktop_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.policy_group_id = TeaConverter.to_unicode(policy_group_id)  # type: unicode
        self.desktop_id = desktop_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.message = message  # type: int
        self.desktop_id = TeaConverter.to_unicode(desktop_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.modify_results = modify_results  # type: list[ModifyDesktopsPolicyGroupResponseBodyModifyResults]

    def validate(self):
        if self.modify_results:
            for k in self.modify_results:
                if k:
                    k.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyDesktopsPolicyGroupResponseBody

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
            temp_model = ModifyDesktopsPolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyEntitlementRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None, end_user_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.desktop_id = TeaConverter.to_unicode(desktop_id)  # type: unicode
        self.end_user_id = end_user_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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


class ModifyEntitlementResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyEntitlementResponseBody

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
            temp_model = ModifyEntitlementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyImageAttributeRequest(TeaModel):
    def __init__(self, region_id=None, image_id=None, name=None, description=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.image_id = TeaConverter.to_unicode(image_id)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class ModifyImageAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyImageAttributeResponseBody

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
            temp_model = ModifyImageAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPolicyGroupRequest(TeaModel):
    def __init__(self, region_id=None, policy_group_id=None, name=None, clipboard=None, local_drive=None,
                 usb_redirect=None, watermark=None, watermark_type=None, watermark_custom_text=None,
                 watermark_transparency=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.policy_group_id = TeaConverter.to_unicode(policy_group_id)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.clipboard = TeaConverter.to_unicode(clipboard)  # type: unicode
        self.local_drive = TeaConverter.to_unicode(local_drive)  # type: unicode
        self.usb_redirect = TeaConverter.to_unicode(usb_redirect)  # type: unicode
        self.watermark = TeaConverter.to_unicode(watermark)  # type: unicode
        self.watermark_type = TeaConverter.to_unicode(watermark_type)  # type: unicode
        self.watermark_custom_text = TeaConverter.to_unicode(watermark_custom_text)  # type: unicode
        self.watermark_transparency = TeaConverter.to_unicode(watermark_transparency)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        if self.watermark_custom_text is not None:
            result['WatermarkCustomText'] = self.watermark_custom_text
        if self.watermark_transparency is not None:
            result['WatermarkTransparency'] = self.watermark_transparency
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
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        if m.get('WatermarkCustomText') is not None:
            self.watermark_custom_text = m.get('WatermarkCustomText')
        if m.get('WatermarkTransparency') is not None:
            self.watermark_transparency = m.get('WatermarkTransparency')
        return self


class ModifyPolicyGroupResponseBody(TeaModel):
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


class ModifyPolicyGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ModifyPolicyGroupResponseBody

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
            temp_model = ModifyPolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PayOrderCallbackRequest(TeaModel):
    def __init__(self, data=None):
        self.data = TeaConverter.to_unicode(data)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class PayOrderCallbackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: PayOrderCallbackResponseBody

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
            temp_model = PayOrderCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.desktop_id = desktop_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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


class RebootDesktopsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RebootDesktopsResponseBody

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
            temp_model = RebootDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, period=None, period_unit=None, auto_pay=None, desktop_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.period = period  # type: int
        self.period_unit = TeaConverter.to_unicode(period_unit)  # type: unicode
        self.auto_pay = auto_pay  # type: bool
        self.desktop_id = desktop_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, request_id=None, order_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.order_id = TeaConverter.to_unicode(order_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class RenewDesktopsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RenewDesktopsResponseBody

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
            temp_model = RenewDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetSnapshotRequest(TeaModel):
    def __init__(self, region_id=None, snapshot_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.snapshot_id = TeaConverter.to_unicode(snapshot_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class ResetSnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ResetSnapshotResponseBody

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
            temp_model = ResetSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCommandRequest(TeaModel):
    def __init__(self, region_id=None, type=None, command_content=None, timeout=None, content_encoding=None,
                 desktop_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.command_content = TeaConverter.to_unicode(command_content)  # type: unicode
        self.timeout = timeout  # type: long
        self.content_encoding = TeaConverter.to_unicode(content_encoding)  # type: unicode
        self.desktop_id = desktop_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, request_id=None, invoke_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.invoke_id = TeaConverter.to_unicode(invoke_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        return self


class RunCommandResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RunCommandResponseBody

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
            temp_model = RunCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.desktop_id = desktop_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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


class StartDesktopsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: StartDesktopsResponseBody

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
            temp_model = StartDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.desktop_id = desktop_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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


class StopDesktopsResponseBody(TeaModel):
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


class StopDesktopsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: StopDesktopsResponseBody

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
            temp_model = StopDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInvocationRequest(TeaModel):
    def __init__(self, region_id=None, invoke_id=None, desktop_id=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.invoke_id = TeaConverter.to_unicode(invoke_id)  # type: unicode
        self.desktop_id = desktop_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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


class StopInvocationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: StopInvocationResponseBody

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
            temp_model = StopInvocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
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


class TagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, resource_id=None, tag=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.resource_id = resource_id  # type: list[unicode]
        self.tag = tag  # type: list[TagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
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


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: TagResourcesResponseBody

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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockVirtualMFADeviceRequest(TeaModel):
    def __init__(self, region_id=None, serial_number=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.serial_number = TeaConverter.to_unicode(serial_number)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class UnlockVirtualMFADeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UnlockVirtualMFADeviceResponseBody

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
            temp_model = UnlockVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, all=None, resource_id=None, tag_key=None):
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.all = all  # type: bool
        self.resource_id = resource_id  # type: list[unicode]
        self.tag_key = tag_key  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UntagResourcesResponseBody

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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


