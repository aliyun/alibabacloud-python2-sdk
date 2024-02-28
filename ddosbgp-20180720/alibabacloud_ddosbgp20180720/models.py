# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddIpRequest(TeaModel):
    def __init__(self, instance_id=None, ip_list=None, region_id=None, resource_group_id=None):
        # The ID of the Anti-DDoS Origin Enterprise instance.
        # 
        # >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin Enterprise instances.
        self.instance_id = instance_id  # type: str
        # The list of IP addresses that you want to add to the Anti-DDoS Origin Enterprise instance. This parameter is a string consisting of JSON arrays. Each element in a JSON array is a JSON struct that includes the following field:
        # 
        # *   **ip**: required. The IP address that you want to add. Data type: string.
        # 
        #     > The IP address must be the IP address of an asset that belongs to the current Alibaba Cloud account.
        self.ip_list = ip_list  # type: str
        # The region ID of the Anti-DDoS Origin Enterprise instance.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query all regions supported by Anti-DDoS Origin.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the Anti-DDoS Origin Enterprise instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](~~94485~~).
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class AddIpResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddIpResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddIpResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachAssetGroupToInstanceRequestAssetGroupList(TeaModel):
    def __init__(self, member_uid=None, name=None, region=None, type=None):
        # The UID of the member to which the asset belongs.
        self.member_uid = member_uid  # type: str
        # The ID of the asset that you want to add. If the asset is a Web Application Firewall (WAF) instance, specify the ID of the WAF instance.
        self.name = name  # type: str
        # The region ID of the asset.
        self.region = region  # type: str
        # The type of the asset.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachAssetGroupToInstanceRequestAssetGroupList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AttachAssetGroupToInstanceRequest(TeaModel):
    def __init__(self, asset_group_list=None, instance_id=None, region_id=None, source_ip=None):
        # The information about the asset to be associated.
        self.asset_group_list = asset_group_list  # type: list[AttachAssetGroupToInstanceRequestAssetGroupList]
        # The ID of the instance to query.
        # 
        # >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin instances of paid editions.
        self.instance_id = instance_id  # type: str
        # The ID of the region in which the instance resides.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The source IP address of the request. The system specifies this parameter.
        self.source_ip = source_ip  # type: str

    def validate(self):
        if self.asset_group_list:
            for k in self.asset_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AttachAssetGroupToInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AssetGroupList'] = []
        if self.asset_group_list is not None:
            for k in self.asset_group_list:
                result['AssetGroupList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.asset_group_list = []
        if m.get('AssetGroupList') is not None:
            for k in m.get('AssetGroupList'):
                temp_model = AttachAssetGroupToInstanceRequestAssetGroupList()
                self.asset_group_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class AttachAssetGroupToInstanceShrinkRequest(TeaModel):
    def __init__(self, asset_group_list_shrink=None, instance_id=None, region_id=None, source_ip=None):
        # The information about the asset to be associated.
        self.asset_group_list_shrink = asset_group_list_shrink  # type: str
        # The ID of the instance to query.
        # 
        # >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin instances of paid editions.
        self.instance_id = instance_id  # type: str
        # The ID of the region in which the instance resides.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The source IP address of the request. The system specifies this parameter.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachAssetGroupToInstanceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_group_list_shrink is not None:
            result['AssetGroupList'] = self.asset_group_list_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetGroupList') is not None:
            self.asset_group_list_shrink = m.get('AssetGroupList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class AttachAssetGroupToInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachAssetGroupToInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachAssetGroupToInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachAssetGroupToInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachAssetGroupToInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachAssetGroupToInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAccessLogAuthRequest(TeaModel):
    def __init__(self, region_id=None, resource_group_id=None):
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # For more information about the valid values of this parameter, see [Regions and zones](~~188196~~).
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management. This parameter is empty by default, which indicates that the Anti-DDoS Origin instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](~~94485~~).
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAccessLogAuthRequest, self).to_map()
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


class CheckAccessLogAuthResponseBody(TeaModel):
    def __init__(self, access_log_auth=None, request_id=None):
        # Indicates whether Anti-DDoS Origin was authorized to access Log Service. Valid values:
        # 
        # *   **true**: Anti-DDoS Origin was authorized.
        # *   **false**: Anti-DDoS Origin was not authorized.
        self.access_log_auth = access_log_auth  # type: bool
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckAccessLogAuthResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_auth is not None:
            result['AccessLogAuth'] = self.access_log_auth
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessLogAuth') is not None:
            self.access_log_auth = m.get('AccessLogAuth')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckAccessLogAuthResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckAccessLogAuthResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckAccessLogAuthResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckAccessLogAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckGrantRequest(TeaModel):
    def __init__(self, is_slr=None, region_id=None, resource_group_id=None):
        # Specifies whether to allow Anti-DDoS Origin to check the service-linked role. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_slr = is_slr  # type: bool
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckGrantRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_slr is not None:
            result['IsSlr'] = self.is_slr
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSlr') is not None:
            self.is_slr = m.get('IsSlr')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CheckGrantResponseBody(TeaModel):
    def __init__(self, request_id=None, status=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether Anti-DDoS Origin is authorized to obtain information about the assets within the current Alibaba Cloud account. Valid values:
        # 
        # *   **1**: Anti-DDoS Origin is authorized to obtain information about the assets within the current Alibaba Cloud account.
        # *   **0**: Anti-DDoS Origin is not authorized to obtain information about the assets within the current Alibaba Cloud account.
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckGrantResponseBody, self).to_map()
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


class CheckGrantResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckGrantResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckGrantResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckGrantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigSchedruleOnDemandRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, rule_action=None, rule_condition_cnt=None,
                 rule_condition_kpps=None, rule_condition_mbps=None, rule_name=None, rule_switch=None, rule_undo_begin_time=None,
                 rule_undo_end_time=None, rule_undo_mode=None, time_zone=None):
        # The ID of the on-demand instance.
        # 
        # >  You can call the [DescribeOnDemandInstance](~~152120~~) operation to query the IDs of all on-demand instances.
        self.instance_id = instance_id  # type: str
        # The region ID of the on-demand instance.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query all regions supported by Anti-DDoS Origin.
        self.region_id = region_id  # type: str
        # The scheduling action. Set the value to **declare**, which indicates that the route is advertised.
        self.rule_action = rule_action  # type: str
        # If the inbound bandwidth or packets consecutively exceed the threshold for the specified number of times, the scheduling rule is triggered and traffic is rerouted to the on-demand instance. The specified number of times is the value of this parameter.
        # 
        # >  The threshold of inbound bandwidth is the value of **RuleConditionMbps**. The threshold of inbound packets is the value of **RuleConditionKpps**.
        self.rule_condition_cnt = rule_condition_cnt  # type: str
        # The threshold of inbound packets. Unit: Kpps. Minimum value: **10**.
        self.rule_condition_kpps = rule_condition_kpps  # type: str
        # The threshold of inbound bandwidth. Unit: Mbit/s. Minimum value: **100**.
        self.rule_condition_mbps = rule_condition_mbps  # type: str
        # The name of the scheduling rule.
        # 
        # The name can contain lowercase letters, digits, hyphens (-), and underscores (\_). The name can be up to 32 characters in length. We recommend that you use the ID of the on-demand instance as the name. Example: `ddosbgp-cn-z2q1qzxb****`.
        self.rule_name = rule_name  # type: str
        # Specifies whether the scheduling rule is enabled. Valid values:
        # 
        # *   **on**: enabled
        # *   **off**: disabled
        self.rule_switch = rule_switch  # type: str
        # The start time of the period during which the scheduling rule is automatically stopped. The time must be in the 24-hour clock and in the `hh:mm` format.
        # 
        # If the system detects that DDoS attacks stop, the system no longer reroutes traffic to the on-demand instance from the time you specified. We recommend that you set this parameter to a value that is defined as off-peak hours.
        # 
        # >  This parameter takes effect only when the **RuleUndoMode** parameter is set to **auto**.
        self.rule_undo_begin_time = rule_undo_begin_time  # type: str
        # The end time of the period during which the scheduling rule is automatically stopped. The time must be in the 24-hour clock and in the `hh:mm` format.
        self.rule_undo_end_time = rule_undo_end_time  # type: str
        # The stop method of the scheduling rule. Valid values:
        # 
        # *   **auto**: The scheduling rule automatically stops.
        # *   **manual**: The scheduling rule is manually stopped.
        self.rule_undo_mode = rule_undo_mode  # type: str
        # The time zone of the time when the scheduling rule automatically stops. The time zone must be in the `GMT-hh:mm` format.
        # 
        # For example, the value `GMT-08:00` indicates that the time zone is UTC+8.
        # 
        # >  This parameter takes effect only when the **RuleUndoMode** parameter is set to **auto**.
        self.time_zone = time_zone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigSchedruleOnDemandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action
        if self.rule_condition_cnt is not None:
            result['RuleConditionCnt'] = self.rule_condition_cnt
        if self.rule_condition_kpps is not None:
            result['RuleConditionKpps'] = self.rule_condition_kpps
        if self.rule_condition_mbps is not None:
            result['RuleConditionMbps'] = self.rule_condition_mbps
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_switch is not None:
            result['RuleSwitch'] = self.rule_switch
        if self.rule_undo_begin_time is not None:
            result['RuleUndoBeginTime'] = self.rule_undo_begin_time
        if self.rule_undo_end_time is not None:
            result['RuleUndoEndTime'] = self.rule_undo_end_time
        if self.rule_undo_mode is not None:
            result['RuleUndoMode'] = self.rule_undo_mode
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')
        if m.get('RuleConditionCnt') is not None:
            self.rule_condition_cnt = m.get('RuleConditionCnt')
        if m.get('RuleConditionKpps') is not None:
            self.rule_condition_kpps = m.get('RuleConditionKpps')
        if m.get('RuleConditionMbps') is not None:
            self.rule_condition_mbps = m.get('RuleConditionMbps')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleSwitch') is not None:
            self.rule_switch = m.get('RuleSwitch')
        if m.get('RuleUndoBeginTime') is not None:
            self.rule_undo_begin_time = m.get('RuleUndoBeginTime')
        if m.get('RuleUndoEndTime') is not None:
            self.rule_undo_end_time = m.get('RuleUndoEndTime')
        if m.get('RuleUndoMode') is not None:
            self.rule_undo_mode = m.get('RuleUndoMode')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class ConfigSchedruleOnDemandResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigSchedruleOnDemandResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigSchedruleOnDemandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigSchedruleOnDemandResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigSchedruleOnDemandResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ConfigSchedruleOnDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSchedruleOnDemandRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, rule_action=None, rule_condition_cnt=None,
                 rule_condition_kpps=None, rule_condition_mbps=None, rule_name=None, rule_switch=None, rule_undo_begin_time=None,
                 rule_undo_end_time=None, rule_undo_mode=None, time_zone=None):
        # The ID of the on-demand instance.
        # 
        # >  You can call the [DescribeOnDemandInstance](~~152120~~) operation to query the IDs of all on-demand instances.
        self.instance_id = instance_id  # type: str
        # The region ID of the on-demand instance.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query all regions supported by Anti-DDoS Origin.
        self.region_id = region_id  # type: str
        # The scheduling action. Set the value to **declare**, which indicates that the route is advertised.
        self.rule_action = rule_action  # type: str
        # If the inbound bandwidth or packets consecutively exceed the threshold for the specified number of times, the scheduling rule is triggered and traffic is rerouted to the on-demand instance. The specified number of times is the value of this parameter.
        # 
        # >  The threshold of inbound bandwidth is the value of **RuleConditionMbps**. The threshold of inbound packets is the value of **RuleConditionKpps**.
        self.rule_condition_cnt = rule_condition_cnt  # type: str
        # The threshold of inbound packets. Unit: Kpps. Minimum value: **10**.
        self.rule_condition_kpps = rule_condition_kpps  # type: str
        # The threshold of inbound bandwidth. Unit: Mbit/s. Minimum value: **100**.
        self.rule_condition_mbps = rule_condition_mbps  # type: str
        # The name of the scheduling rule.
        # 
        # The name can contain lowercase letters, digits, hyphens (-), and underscores (\_). The name can be up to 32 characters in length. We recommend that you use the ID of the on-demand instance as the name. Example: `ddosbgp-cn-z2q1qzxb****`.
        self.rule_name = rule_name  # type: str
        # Specifies whether the scheduling rule is enabled. Valid values:
        # 
        # *   **on**: enabled
        # *   **off**: disabled
        self.rule_switch = rule_switch  # type: str
        # The start time of the period during which the scheduling rule is automatically stopped. The time must be in the 24-hour clock and in the `hh:mm` format.
        # 
        # If the system detects that DDoS attacks stop, the system no longer reroutes traffic to the on-demand instance from the time you specified. We recommend that you set this parameter to a value that is defined as off-peak hours.
        # 
        # >  This parameter takes effect only when the **RuleUndoMode** parameter is set to **auto**.
        self.rule_undo_begin_time = rule_undo_begin_time  # type: str
        # The end time of the period during which the scheduling rule is automatically stopped. The time must be in the 24-hour clock and in the `hh:mm` format.
        self.rule_undo_end_time = rule_undo_end_time  # type: str
        # The stop method of the scheduling rule. Valid values:
        # 
        # *   **auto**: The scheduling rule automatically stops.
        # *   **manual**: The scheduling rule is manually stopped.
        self.rule_undo_mode = rule_undo_mode  # type: str
        # The time zone of the time when the scheduling rule automatically stops. The time zone must be in the `GMT-hh:mm` format.
        # 
        # For example, the value `GMT-08:00` indicates that the time zone is UTC+8.
        # 
        # >  This parameter takes effect only when the **RuleUndoMode** parameter is set to **auto**.
        self.time_zone = time_zone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSchedruleOnDemandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action
        if self.rule_condition_cnt is not None:
            result['RuleConditionCnt'] = self.rule_condition_cnt
        if self.rule_condition_kpps is not None:
            result['RuleConditionKpps'] = self.rule_condition_kpps
        if self.rule_condition_mbps is not None:
            result['RuleConditionMbps'] = self.rule_condition_mbps
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_switch is not None:
            result['RuleSwitch'] = self.rule_switch
        if self.rule_undo_begin_time is not None:
            result['RuleUndoBeginTime'] = self.rule_undo_begin_time
        if self.rule_undo_end_time is not None:
            result['RuleUndoEndTime'] = self.rule_undo_end_time
        if self.rule_undo_mode is not None:
            result['RuleUndoMode'] = self.rule_undo_mode
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')
        if m.get('RuleConditionCnt') is not None:
            self.rule_condition_cnt = m.get('RuleConditionCnt')
        if m.get('RuleConditionKpps') is not None:
            self.rule_condition_kpps = m.get('RuleConditionKpps')
        if m.get('RuleConditionMbps') is not None:
            self.rule_condition_mbps = m.get('RuleConditionMbps')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleSwitch') is not None:
            self.rule_switch = m.get('RuleSwitch')
        if m.get('RuleUndoBeginTime') is not None:
            self.rule_undo_begin_time = m.get('RuleUndoBeginTime')
        if m.get('RuleUndoEndTime') is not None:
            self.rule_undo_end_time = m.get('RuleUndoEndTime')
        if m.get('RuleUndoMode') is not None:
            self.rule_undo_mode = m.get('RuleUndoMode')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class CreateSchedruleOnDemandResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSchedruleOnDemandResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSchedruleOnDemandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSchedruleOnDemandResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSchedruleOnDemandResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSchedruleOnDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBlackholeRequest(TeaModel):
    def __init__(self, instance_id=None, ip=None, region_id=None, resource_group_id=None):
        # The ID of the Anti-DDoS Origin instance.
        # 
        # >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin instances.
        self.instance_id = instance_id  # type: str
        # The IP address for which you want to deactivate blackhole filtering.
        # 
        # >  You can call the [DescribePackIpList](~~118701~~) operation to query all the IP addresses that are protected by the Anti-DDoS Origin instance and the protection status of the IP addresses. For example, you can query whether blackhole filtering is triggered for an IP address.
        self.ip = ip  # type: str
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBlackholeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteBlackholeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteBlackholeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBlackholeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteBlackholeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteBlackholeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBlackholeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpRequest(TeaModel):
    def __init__(self, instance_id=None, ip_list=None, region_id=None, resource_group_id=None):
        # The ID of the Anti-DDoS Origin Enterprise instance.
        # 
        # >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin Enterprise instances.
        self.instance_id = instance_id  # type: str
        # The list of IP addresses that you want to remove from the Anti-DDoS Origin Enterprise instance. This parameter is a string consisting of JSON arrays. Each element in a JSON array is a JSON struct that includes the following field:
        # 
        # *   **ip**: required. The IP address that you want to remove. Data type: string.
        # 
        #     > The IP addresses that you want to remove must be protected by the Anti-DDoS Origin Enterprise instance.
        self.ip_list = ip_list  # type: str
        # The region ID of the Anti-DDoS Origin Enterprise instance.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query all regions supported by Anti-DDoS Origin.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the Anti-DDoS Origin Enterprise instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](~~94485~~).
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteIpResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteIpResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIpResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSchedruleOnDemandRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, rule_name=None):
        # The ID of the on-demand instance.
        # 
        # >  You can call the [DescribeOnDemandInstance](~~152120~~) operation to query the IDs of all on-demand instances.
        self.instance_id = instance_id  # type: str
        # The region ID of the on-demand instance.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query all regions supported by Anti-DDoS Origin.
        self.region_id = region_id  # type: str
        # The name of the scheduling rule that you want to delete.
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSchedruleOnDemandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DeleteSchedruleOnDemandResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSchedruleOnDemandResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSchedruleOnDemandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSchedruleOnDemandResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSchedruleOnDemandResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSchedruleOnDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAssetGroupRequest(TeaModel):
    def __init__(self, name=None, region=None, region_id=None, source_ip=None, type=None):
        # The ID of the asset. If the asset is a Web Application Firewall (WAF) instance, specify the ID of the WAF instance.
        self.name = name  # type: str
        # The region ID of the asset.
        self.region = region  # type: str
        # The ID of the region in which the instance resides.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The source IP address of the request. The system specifies this parameter.
        self.source_ip = source_ip  # type: str
        # The type of the asset. Valid values:
        # 
        # *   **waf**: WAF instance
        # *   **ga**: Global Accelerator (GA) instance
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAssetGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAssetGroupResponseBodyAssetGroupList(TeaModel):
    def __init__(self, name=None, region=None, type=None):
        # The ID of the asset.
        self.name = name  # type: str
        # The region to which the asset belongs.
        self.region = region  # type: str
        # The type of the asset.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAssetGroupResponseBodyAssetGroupList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAssetGroupResponseBody(TeaModel):
    def __init__(self, asset_group_list=None, request_id=None, total=None):
        # The information about the asset.
        self.asset_group_list = asset_group_list  # type: list[DescribeAssetGroupResponseBodyAssetGroupList]
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total = total  # type: long

    def validate(self):
        if self.asset_group_list:
            for k in self.asset_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAssetGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AssetGroupList'] = []
        if self.asset_group_list is not None:
            for k in self.asset_group_list:
                result['AssetGroupList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.asset_group_list = []
        if m.get('AssetGroupList') is not None:
            for k in m.get('AssetGroupList'):
                temp_model = DescribeAssetGroupResponseBodyAssetGroupList()
                self.asset_group_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeAssetGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAssetGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAssetGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAssetGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAssetGroupToInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, member_uid=None, name=None, region=None, region_id=None, source_ip=None,
                 type=None):
        # The ID of the instance to query.
        # 
        # >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin instances of paid editions.
        self.instance_id = instance_id  # type: str
        # The UID of the member to which the asset belongs.
        self.member_uid = member_uid  # type: str
        # The ID of the asset. If the asset is a Web Application Firewall (WAF) instance, specify the ID of the WAF instance.
        self.name = name  # type: str
        # The region ID of the asset.
        self.region = region  # type: str
        # The ID of the region in which the instance resides.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The source IP address of the request. The system specifies this parameter.
        self.source_ip = source_ip  # type: str
        # The type of the asset. Valid values:
        # 
        # *   **waf**: WAF instance
        # *   **ga**: Global Accelerator (GA) instance
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAssetGroupToInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAssetGroupToInstanceResponseBodyDataList(TeaModel):
    def __init__(self, instance_id=None, member_uid=None, name=None, region=None, type=None):
        # The ID of the Anti-DDoS Origin instance of a paid edition.
        self.instance_id = instance_id  # type: str
        # The UID of the member to which the asset belongs.
        self.member_uid = member_uid  # type: str
        # The ID of the asset.
        self.name = name  # type: str
        # The region ID of the asset.
        self.region = region  # type: str
        # The type of the asset.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAssetGroupToInstanceResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAssetGroupToInstanceResponseBody(TeaModel):
    def __init__(self, data_list=None, request_id=None, total=None):
        # The response parameters.
        self.data_list = data_list  # type: list[DescribeAssetGroupToInstanceResponseBodyDataList]
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total = total  # type: long

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAssetGroupToInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeAssetGroupToInstanceResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeAssetGroupToInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAssetGroupToInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAssetGroupToInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAssetGroupToInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosEventRequest(TeaModel):
    def __init__(self, end_time=None, instance_id=None, ip=None, page_no=None, page_size=None, region_id=None,
                 resource_group_id=None, start_time=None):
        # The end time of the DDoS attack event to query. This value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: int
        # The ID of the Anti-DDoS Origin instance to query.
        # 
        # >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin instances.
        self.instance_id = instance_id  # type: str
        # The attacked IP address to query.
        self.ip = ip  # type: str
        # The number of the page to return.
        self.page_no = page_no  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The start time of the DDoS attack event to query. This value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDdosEventRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
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
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDdosEventResponseBodyEvents(TeaModel):
    def __init__(self, end_time=None, ip=None, mbps=None, pps=None, start_time=None, status=None):
        # The time when the DDoS attack stopped. This value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time  # type: int
        # The attacked IP address.
        self.ip = ip  # type: str
        # The volume of the request traffic at the start of the DDoS attack. Unit: Mbit/s.
        self.mbps = mbps  # type: int
        # The number of packets at the start of the DDoS attack. Unit: packets per second (PPS).
        self.pps = pps  # type: int
        # The time when the DDoS attack started. This value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: int
        # The status of the DDoS attack event. Valid values:
        # 
        # *   **hole_begin**: indicates that blackhole filtering is triggered for the attacked IP address.
        # *   **hole_end**: indicates that blackhole filtering is deactivated for the attacked IP address.
        # *   **defense_begin**: indicates that attack traffic is being scrubbed.
        # *   **defense_end**: indicates that attack traffic is scrubbed.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDdosEventResponseBodyEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.mbps is not None:
            result['Mbps'] = self.mbps
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDdosEventResponseBody(TeaModel):
    def __init__(self, events=None, request_id=None, total=None):
        # The details about the DDoS attack event.
        self.events = events  # type: list[DescribeDdosEventResponseBodyEvents]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of DDoS attack events.
        self.total = total  # type: long

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDdosEventResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeDdosEventResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeDdosEventResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDdosEventResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDdosEventResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDdosEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExcpetionCountRequest(TeaModel):
    def __init__(self, region_id=None, resource_group_id=None):
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExcpetionCountRequest, self).to_map()
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


class DescribeExcpetionCountResponseBody(TeaModel):
    def __init__(self, exception_ip_count=None, expire_time_count=None, request_id=None):
        # The number of assets that are in an abnormal state.
        self.exception_ip_count = exception_ip_count  # type: int
        # The number of Anti-DDoS Origin instances that are about to expire.
        self.expire_time_count = expire_time_count  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeExcpetionCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exception_ip_count is not None:
            result['ExceptionIpCount'] = self.exception_ip_count
        if self.expire_time_count is not None:
            result['ExpireTimeCount'] = self.expire_time_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExceptionIpCount') is not None:
            self.exception_ip_count = m.get('ExceptionIpCount')
        if m.get('ExpireTimeCount') is not None:
            self.expire_time_count = m.get('ExpireTimeCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeExcpetionCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeExcpetionCountResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeExcpetionCountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeExcpetionCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceListRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag that is added to the Anti-DDoS Origin instance to query.
        self.key = key  # type: str
        # The value of the tag that is added to the Anti-DDoS Origin instance to query.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceListRequestTag, self).to_map()
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


class DescribeInstanceListRequest(TeaModel):
    def __init__(self, instance_id_list=None, instance_type=None, instance_type_list=None, ip=None, ip_version=None,
                 orderby=None, orderdire=None, page_no=None, page_size=None, region_id=None, remark=None,
                 resource_group_id=None, tag=None):
        # The IDs of the Anti-DDoS Origin instances to query. Specify the value is in the `["<Instance ID 1>","<Instance ID 2>",……]` format.
        self.instance_id_list = instance_id_list  # type: str
        # The mitigation plan of the Anti-DDoS Origin instance to query. Valid values:
        # 
        # *   **0**: the Professional mitigation plan
        # *   **1**: the Enterprise mitigation plan
        self.instance_type = instance_type  # type: str
        self.instance_type_list = instance_type_list  # type: list[str]
        # The IP address of the object that is protected by the Anti-DDoS Origin instance to query.
        self.ip = ip  # type: str
        # The protocol type of the IP address asset that is protected by the Anti-DDoS Origin instance to query. Valid values:
        # 
        # *   **Ipv4**: IPv4
        # *   **Ipv6**: IPv6
        self.ip_version = ip_version  # type: str
        # The field that is used to sort the Anti-DDoS Origin instances. Set the value to **expireTime**, which indicates that the instances are sorted based on the expiration time.
        # 
        # You can set the **Orderdire** parameter to specify the sorting method.
        self.orderby = orderby  # type: str
        # The sorting method. Valid values:
        # 
        # *   **desc**: the descending order. This is the default value.
        # *   **asc**: the ascending order.
        self.orderdire = orderdire  # type: str
        # The number of the page to return.
        self.page_no = page_no  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The ID of the region where the Anti-DDoS Origin instance to query resides.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The remarks of the Anti-DDoS Origin instance to query. Fuzzy match is supported.
        self.remark = remark  # type: str
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.tag = tag  # type: list[DescribeInstanceListRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_type_list is not None:
            result['InstanceTypeList'] = self.instance_type_list
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.orderby is not None:
            result['Orderby'] = self.orderby
        if self.orderdire is not None:
            result['Orderdire'] = self.orderdire
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceTypeList') is not None:
            self.instance_type_list = m.get('InstanceTypeList')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Orderby') is not None:
            self.orderby = m.get('Orderby')
        if m.get('Orderdire') is not None:
            self.orderdire = m.get('Orderdire')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstanceListRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstanceListResponseBodyInstanceListAutoProtectCondition(TeaModel):
    def __init__(self, events=None):
        self.events = events  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceListResponseBodyInstanceListAutoProtectCondition, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.events is not None:
            result['Events'] = self.events
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Events') is not None:
            self.events = m.get('Events')
        return self


class DescribeInstanceListResponseBodyInstanceList(TeaModel):
    def __init__(self, auto_protect_condition=None, auto_renewal=None, blackholding_count=None,
                 commodity_type=None, coverage_type=None, expire_time=None, gmt_create=None, instance_id=None, instance_type=None,
                 ip_type=None, product=None, remark=None, status=None):
        self.auto_protect_condition = auto_protect_condition  # type: DescribeInstanceListResponseBodyInstanceListAutoProtectCondition
        # Indicates whether auto-renewal is enabled for the instance. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.auto_renewal = auto_renewal  # type: bool
        # The number of protected public IP addresses for which blackhole filtering is triggered.
        # 
        # >  You can call the [DeleteBlackhole](~~118692~~) operation to deactivate blackhole filtering for a protected IP address.
        self.blackholding_count = blackholding_count  # type: str
        self.commodity_type = commodity_type  # type: str
        self.coverage_type = coverage_type  # type: int
        # The time when the instance expires. This value is a UNIX timestamp. Unit: milliseconds.
        self.expire_time = expire_time  # type: long
        # The time when the instance was purchased. This value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create  # type: long
        # The ID of the instance.
        self.instance_id = instance_id  # type: str
        # The mitigation plan of the instance. Valid values:
        # 
        # *   **0**: the Professional mitigation plan
        # *   **1**: the Enterprise mitigation plan
        self.instance_type = instance_type  # type: str
        # The protocol type of the IP address asset that is protected by the instance. Valid values:
        # 
        # *   **Ipv4**: IPv4
        # *   **Ipv6**: IPv6
        self.ip_type = ip_type  # type: str
        # The type of the cloud service that is associated with the Anti-DDoS Origin instance. By default, this parameter is not returned. If the Anti-DDoS Origin instance is created by using a different cloud service, the code of the cloud service is returned.
        # 
        # Valid values:
        # 
        # *   **gamebox**: The Anti-DDoS Origin instance is created by using Game Security Box.
        # *   **eip**: The Anti-DDoS Origin instance is created by using an elastic IP address (EIP) for which Anti-DDoS (Enhanced Edition) is enabled.
        self.product = product  # type: str
        # The remarks of the instance.
        self.remark = remark  # type: str
        # The status of the instance. Valid values:
        # 
        # *   **1**: normal
        # *   **2**: expired
        # *   **3**: released
        self.status = status  # type: str

    def validate(self):
        if self.auto_protect_condition:
            self.auto_protect_condition.validate()

    def to_map(self):
        _map = super(DescribeInstanceListResponseBodyInstanceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_protect_condition is not None:
            result['AutoProtectCondition'] = self.auto_protect_condition.to_map()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.blackholding_count is not None:
            result['BlackholdingCount'] = self.blackholding_count
        if self.commodity_type is not None:
            result['CommodityType'] = self.commodity_type
        if self.coverage_type is not None:
            result['CoverageType'] = self.coverage_type
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip_type is not None:
            result['IpType'] = self.ip_type
        if self.product is not None:
            result['Product'] = self.product
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoProtectCondition') is not None:
            temp_model = DescribeInstanceListResponseBodyInstanceListAutoProtectCondition()
            self.auto_protect_condition = temp_model.from_map(m['AutoProtectCondition'])
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('BlackholdingCount') is not None:
            self.blackholding_count = m.get('BlackholdingCount')
        if m.get('CommodityType') is not None:
            self.commodity_type = m.get('CommodityType')
        if m.get('CoverageType') is not None:
            self.coverage_type = m.get('CoverageType')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeInstanceListResponseBody(TeaModel):
    def __init__(self, instance_list=None, request_id=None, total=None):
        # The details about the Anti-DDoS Origin instance.
        self.instance_list = instance_list  # type: list[DescribeInstanceListResponseBodyInstanceList]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of Anti-DDoS Origin instances.
        self.total = total  # type: long

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = DescribeInstanceListResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeInstanceListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSpecsRequest(TeaModel):
    def __init__(self, instance_id_list=None, region_id=None, resource_group_id=None):
        # The ID of the Anti-DDoS Origin Enterprise instance. This parameter value is a string consisting of JSON arrays. Each element in a JSON array indicates an instance ID. If you want to query more than one instance, separate instance IDs with commas (,).
        # 
        # >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin Enterprise instances in a specific region.
        self.instance_id_list = instance_id_list  # type: str
        # The region ID of the Anti-DDoS Origin Enterprise instance. Default value: **cn-hangzhou**, which indicates the China (Hangzhou) region.
        # 
        # >  If your instance does not reside in the China (Hangzhou) region, you must specify this parameter to the region ID of your instance. You can call the [DescribeRegions](~~118703~~) operation to query the regions of cloud assets that are supported by an Anti-DDoS Origin instance.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the Anti-DDoS Origin Enterprise instance belongs in Resource Management. This parameter is empty by default, which indicates that the Anti-DDoS Origin Enterprise instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](~~94485~~).
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceSpecsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeInstanceSpecsResponseBodyInstanceSpecsPackConfig(TeaModel):
    def __init__(self, bandwidth=None, bind_ip_count=None, ip_advance_thre=None, ip_basic_thre=None, ip_spec=None,
                 normal_bandwidth=None, pack_adv_thre=None, pack_basic_thre=None):
        # The bandwidth of the package configuration.
        self.bandwidth = bandwidth  # type: long
        # The number of IP addresses that are protected by the Anti-DDoS Origin Enterprise instance.
        self.bind_ip_count = bind_ip_count  # type: int
        # The burstable bandwidth of each protected IP address. Unit: Gbit/s.
        self.ip_advance_thre = ip_advance_thre  # type: int
        # The basic bandwidth of each protected IP address. Unit: Gbit/s.
        self.ip_basic_thre = ip_basic_thre  # type: int
        # The number of IP addresses that can be protected by the Anti-DDoS Origin Enterprise instance.
        self.ip_spec = ip_spec  # type: int
        # The normal clean bandwidth. Unit: Mbit/s.
        self.normal_bandwidth = normal_bandwidth  # type: int
        # The burstable protection bandwidth of the Anti-DDoS Origin Enterprise instance. Unit: Gbit/s.
        self.pack_adv_thre = pack_adv_thre  # type: int
        # The basic protection bandwidth of the Anti-DDoS Origin Enterprise instance. Unit: Gbit/s.
        self.pack_basic_thre = pack_basic_thre  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceSpecsResponseBodyInstanceSpecsPackConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bind_ip_count is not None:
            result['BindIpCount'] = self.bind_ip_count
        if self.ip_advance_thre is not None:
            result['IpAdvanceThre'] = self.ip_advance_thre
        if self.ip_basic_thre is not None:
            result['IpBasicThre'] = self.ip_basic_thre
        if self.ip_spec is not None:
            result['IpSpec'] = self.ip_spec
        if self.normal_bandwidth is not None:
            result['NormalBandwidth'] = self.normal_bandwidth
        if self.pack_adv_thre is not None:
            result['PackAdvThre'] = self.pack_adv_thre
        if self.pack_basic_thre is not None:
            result['PackBasicThre'] = self.pack_basic_thre
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BindIpCount') is not None:
            self.bind_ip_count = m.get('BindIpCount')
        if m.get('IpAdvanceThre') is not None:
            self.ip_advance_thre = m.get('IpAdvanceThre')
        if m.get('IpBasicThre') is not None:
            self.ip_basic_thre = m.get('IpBasicThre')
        if m.get('IpSpec') is not None:
            self.ip_spec = m.get('IpSpec')
        if m.get('NormalBandwidth') is not None:
            self.normal_bandwidth = m.get('NormalBandwidth')
        if m.get('PackAdvThre') is not None:
            self.pack_adv_thre = m.get('PackAdvThre')
        if m.get('PackBasicThre') is not None:
            self.pack_basic_thre = m.get('PackBasicThre')
        return self


class DescribeInstanceSpecsResponseBodyInstanceSpecs(TeaModel):
    def __init__(self, available_defense_times=None, available_delete_blackhole_count=None,
                 defense_times_percent=None, instance_id=None, is_full_defense_mode=None, pack_config=None, region=None,
                 total_defense_times=None):
        # The number of times that the unlimited protection feature can be enabled.
        self.available_defense_times = available_defense_times  # type: int
        # The number of times that blackhole filtering can be deactivated.
        self.available_delete_blackhole_count = available_delete_blackhole_count  # type: str
        self.defense_times_percent = defense_times_percent  # type: int
        # The ID of the Anti-DDoS Origin Enterprise instance.
        self.instance_id = instance_id  # type: str
        # Indicates whether the unlimited protection feature is enabled. Valid values:
        # 
        # *   **0**: The unlimited protection feature is disabled.
        # *   **1**: The unlimited protection feature is enabled.
        self.is_full_defense_mode = is_full_defense_mode  # type: int
        # The configurations of the Anti-DDoS Origin Enterprise instance, including the number of protected IP addresses and protection bandwidth.
        self.pack_config = pack_config  # type: DescribeInstanceSpecsResponseBodyInstanceSpecsPackConfig
        # The region ID of the Anti-DDoS Origin Enterprise instance.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the name of the region.
        self.region = region  # type: str
        # The number of times that the unlimited protection feature can be enabled.
        self.total_defense_times = total_defense_times  # type: int

    def validate(self):
        if self.pack_config:
            self.pack_config.validate()

    def to_map(self):
        _map = super(DescribeInstanceSpecsResponseBodyInstanceSpecs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_defense_times is not None:
            result['AvailableDefenseTimes'] = self.available_defense_times
        if self.available_delete_blackhole_count is not None:
            result['AvailableDeleteBlackholeCount'] = self.available_delete_blackhole_count
        if self.defense_times_percent is not None:
            result['DefenseTimesPercent'] = self.defense_times_percent
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_full_defense_mode is not None:
            result['IsFullDefenseMode'] = self.is_full_defense_mode
        if self.pack_config is not None:
            result['PackConfig'] = self.pack_config.to_map()
        if self.region is not None:
            result['Region'] = self.region
        if self.total_defense_times is not None:
            result['TotalDefenseTimes'] = self.total_defense_times
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableDefenseTimes') is not None:
            self.available_defense_times = m.get('AvailableDefenseTimes')
        if m.get('AvailableDeleteBlackholeCount') is not None:
            self.available_delete_blackhole_count = m.get('AvailableDeleteBlackholeCount')
        if m.get('DefenseTimesPercent') is not None:
            self.defense_times_percent = m.get('DefenseTimesPercent')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsFullDefenseMode') is not None:
            self.is_full_defense_mode = m.get('IsFullDefenseMode')
        if m.get('PackConfig') is not None:
            temp_model = DescribeInstanceSpecsResponseBodyInstanceSpecsPackConfig()
            self.pack_config = temp_model.from_map(m['PackConfig'])
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('TotalDefenseTimes') is not None:
            self.total_defense_times = m.get('TotalDefenseTimes')
        return self


class DescribeInstanceSpecsResponseBody(TeaModel):
    def __init__(self, instance_specs=None, request_id=None):
        # The specifications of the Anti-DDoS Origin Enterprise instance, including whether the unlimited protection feature is enabled, and the numbers of times that the unlimited protection feature can be enabled and has been enabled.
        self.instance_specs = instance_specs  # type: list[DescribeInstanceSpecsResponseBodyInstanceSpecs]
        # The ID of the request.
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


class DescribeOnDemandDdosEventRequest(TeaModel):
    def __init__(self, end_time=None, instance_id=None, ip=None, page_no=None, page_size=None, region_id=None,
                 resource_group_id=None, start_time=None):
        # The timestamp that specifies the end of the time range to query. Unit: seconds. The timestamp follows the UNIX time format. It is the number of seconds that have elapsed since 00:00:00 Thursday, 1 January 1970.
        self.end_time = end_time  # type: int
        # The ID of the on-demand instance to query.
        self.instance_id = instance_id  # type: str
        # The IP address of the protection target.
        self.ip = ip  # type: str
        # The number of the page to return. Default value: **1**.
        self.page_no = page_no  # type: int
        # The number of entries to return on each page. The maximum value is **50**. The default value is **10**.
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The timestamp that specifies the beginning of the time range to query. Unit: seconds. The timestamp follows the UNIX time format. It is the number of seconds that have elapsed since 00:00:00 Thursday, 1 January 1970.
        self.start_time = start_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOnDemandDdosEventRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
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
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeOnDemandDdosEventResponseBodyEvents(TeaModel):
    def __init__(self, end_time=None, ip=None, mbps=None, pps=None, start_time=None, status=None):
        # The timestamp that indicates the end time of the attack. Unit: seconds. The timestamp follows the UNIX time format. It is the number of seconds that have elapsed since 00:00:00 Thursday, 1 January 1970.
        self.end_time = end_time  # type: int
        # The IP address of the protection target that encounters the DDoS attack.
        self.ip = ip  # type: str
        # The throughput of the DDoS attack. Unit: Mbit/s.
        self.mbps = mbps  # type: int
        # The packet forwarding rate of the DDoS attack. Unit: packets per second (PPS).
        self.pps = pps  # type: int
        # The timestamp that indicates the start time of the attack. Unit: seconds. The timestamp follows the UNIX time format. It is the number of seconds that have elapsed since 00:00:00 Thursday, 1 January 1970.
        self.start_time = start_time  # type: int
        # The status of the event. Valid values:
        # 
        # *   **hole_begin **: indicates that the event is in the blackhole state.
        # *   **hole_end **: indicates that blackhole ends.
        # *   **defense_begin **: indicates that the event is in the cleaning state.
        # *   **defense_end **: indicates that cleaning ends.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOnDemandDdosEventResponseBodyEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.mbps is not None:
            result['Mbps'] = self.mbps
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeOnDemandDdosEventResponseBody(TeaModel):
    def __init__(self, events=None, request_id=None, total=None):
        # The list of DDoS events and the details of each event.
        self.events = events  # type: list[DescribeOnDemandDdosEventResponseBodyEvents]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of DDoS events.
        self.total = total  # type: long

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOnDemandDdosEventResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeOnDemandDdosEventResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeOnDemandDdosEventResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOnDemandDdosEventResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOnDemandDdosEventResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeOnDemandDdosEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOnDemandInstanceStatusRequest(TeaModel):
    def __init__(self, instance_id_list=None, region_id=None):
        # The IDs of on-demand instances.
        # 
        # >  You can call the [DescribeOnDemandInstance](~~152120~~) operation to query the IDs of all on-demand instances.
        self.instance_id_list = instance_id_list  # type: list[str]
        # The region ID of the on-demand instance.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query all regions supported by Anti-DDoS Origin.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOnDemandInstanceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeOnDemandInstanceStatusResponseBodyInstances(TeaModel):
    def __init__(self, declared=None, desc=None, instance_id=None, mode=None, net=None, registed_as=None,
                 user_id=None):
        # The details of route advertisement for data centers outside the Chinese mainland. This parameter is a JSON string. The following fields are included in the value:
        # 
        # *   **region**: The code of the data center outside the Chinese mainland. The value is of the STRING type. For more information, see **Codes of data centers outside the Chinese mainland**.
        # *   **declared**: indicates whether the data center advertised the route. The value is of the STRING type. Valid values: **0** and **1**. The value of 0 indicates that the data center did not advertise the route. The value of 1 indicates that the data center advertised the route.
        self.declared = declared  # type: str
        # The description of the on-demand instance.
        # 
        # >  The value of this parameter is returned only when the information about multiple on-demand instances is returned. The value of this parameter is not returned because the information about only one on-demand instance is returned.
        self.desc = desc  # type: str
        # The ID of the on-demand instance.
        # 
        # >  The value of this parameter is returned only when the information about multiple on-demand instances is returned. The value of this parameter is not returned because the information about only one on-demand instance is returned.
        self.instance_id = instance_id  # type: str
        # The mode used to start the on-demand instance. Valid values:
        # 
        # *   **manual**: The instance is manually started.
        # *   **netflow-auto**: The instance is automatically started by using NetFlow that monitors network traffic.
        self.mode = mode  # type: str
        # The CIDR block of the on-demand instance.
        self.net = net  # type: str
        # The number of the autonomous system (AS). Set the value to **0**, which indicates that AS is disabled.
        self.registed_as = registed_as  # type: str
        # The ID of the Alibaba Cloud account.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOnDemandInstanceStatusResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.declared is not None:
            result['Declared'] = self.declared
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.net is not None:
            result['Net'] = self.net
        if self.registed_as is not None:
            result['RegistedAs'] = self.registed_as
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Declared') is not None:
            self.declared = m.get('Declared')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Net') is not None:
            self.net = m.get('Net')
        if m.get('RegistedAs') is not None:
            self.registed_as = m.get('RegistedAs')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeOnDemandInstanceStatusResponseBody(TeaModel):
    def __init__(self, instances=None, request_id=None):
        # The details of the on-demand instance.
        self.instances = instances  # type: list[DescribeOnDemandInstanceStatusResponseBodyInstances]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeOnDemandInstanceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeOnDemandInstanceStatusResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOnDemandInstanceStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeOnDemandInstanceStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeOnDemandInstanceStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeOnDemandInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOpEntitiesRequest(TeaModel):
    def __init__(self, current_page=None, end_time=None, instance_id=None, order_by=None, order_dir=None,
                 page_size=None, region_id=None, resource_group_id=None, start_time=None):
        # The operation that you want to perform. Set the value to **DescribeOpEntities**.
        self.current_page = current_page  # type: int
        # The details of the operation log.
        self.end_time = end_time  # type: long
        # The page number of the returned page.
        self.instance_id = instance_id  # type: str
        # The sort order of operation logs. Valid values:
        # 
        # *   **ASC**: the ascending order.
        # *   **DESC**: the descending order.
        self.order_by = order_by  # type: str
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        self.order_dir = order_dir  # type: str
        # The type of the operation object. The value is fixed as **1**, which indicates Anti-DDoS Origin instances.
        self.page_size = page_size  # type: int
        # The ID of the Alibaba Cloud account that performs the operation.
        # 
        # >  If the value is **system**, the operation is performed by Anti-DDoS Origin.
        self.region_id = region_id  # type: str
        # The details about the operation. The value is a string that consists of a JSON struct. The JSON struct contains the following fields:
        # 
        # *   **entity**: the operation object. Data type: object. The fields that are included in the value of the **entity** parameter vary based on the value of the **OpAction** parameter. Take note of the following items:
        # 
        #     *   If the value of the **OpAction** parameter is **3**, the value of the **entity** parameter consists of the following field:
        # 
        #         *   **ips**: the public IP addresses that are protected by the Anti-DDoS Origin instance. Data type: array
        # 
        #     *   If the value of the **OpAction** parameter is **4**, the value of the **entity** parameter consists of the following field:
        # 
        #         *   **ips**: the public IP addresses that are no longer protected by the Anti-DDoS Origin instance. Data type: array.
        # 
        #     *   If the value of the **OpAction** parameter is **5**, the value of the **entity** parameter consists of the following fields:
        # 
        #         *   **baseBandwidth**: the basic protection bandwidth. Unit: Gbit/s. Data type: integer.
        #         *   **elasticBandwidth**: the burstable protection bandwidth. Unit: Gbit/s. Data type: integer.
        #         *   **opSource**: the source of the operation. The value is fixed as **1**, indicating that the operation is performed by Anti-DDoS Origin. Data type: integer.
        # 
        #     *   If the value of the **OpAction** parameter is **6**, the value of the **entity** parameter consists of the following field:
        # 
        #         *   **ips**: the public IP addresses for which to deactivate blackhole filtering. Data type: array.
        # 
        #     *   If the value of the **OpAction** parameter is **7**, the **entity** parameter is not returned.
        # 
        #     *   If the value of the **OpAction** parameter is **8**, the value of the **entity** parameter consists of the following fields:
        # 
        #         *   **baseBandwidth**: the basic protection bandwidth. Unit: Gbit/s. Data type: integer.
        #         *   **elasticBandwidth**: the burstable protection bandwidth. Unit: Gbit/s. Data type: integer.
        self.resource_group_id = resource_group_id  # type: str
        # The sorting method of operation logs. Set the value to **opdate**, which indicates sorting based on the operation time.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeOpEntitiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_dir is not None:
            result['OrderDir'] = self.order_dir
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderDir') is not None:
            self.order_dir = m.get('OrderDir')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeOpEntitiesResponseBodyOpEntities(TeaModel):
    def __init__(self, entity_object=None, entity_type=None, gmt_create=None, op_account=None, op_action=None,
                 op_desc=None):
        # Queries the operation logs of an Anti-DDoS Origin instance.
        self.entity_object = entity_object  # type: str
        # All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see [Common parameters](~~118841~~).
        # 
        # For more information about sample requests, see the **"Examples"** section of this topic.
        self.entity_type = entity_type  # type: int
        # WB01342967
        self.gmt_create = gmt_create  # type: long
        self.op_account = op_account  # type: str
        # DescribeOpEntities
        self.op_action = op_action  # type: int
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
        # The ID of the request.
        self.op_entities = op_entities  # type: list[DescribeOpEntitiesResponseBodyOpEntities]
        # The end time. Operation logs that were generated before this time are queried.**** This value is a UNIX timestamp. Unit: milliseconds.
        self.request_id = request_id  # type: str
        # The time when the log was generated. This value is a UNIX timestamp. Unit: milliseconds.
        self.total_count = total_count  # type: int

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


class DescribePackIpListRequest(TeaModel):
    def __init__(self, instance_id=None, ip=None, member_uid=None, page_no=None, page_size=None, product_name=None,
                 region_id=None, resource_group_id=None):
        # The ID of the Anti-DDoS Origin instance to query.
        # 
        # >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin instances.
        self.instance_id = instance_id  # type: str
        # The protected IP address to query.
        self.ip = ip  # type: str
        # The ID of the member.
        self.member_uid = member_uid  # type: str
        # The number of the page to return.
        self.page_no = page_no  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The type of the cloud asset to which the protected IP address to query belongs. Valid values:
        # 
        # *   **ECS**: an Elastic Compute Service (ECS) instance.
        # *   **SLB**: a Classic Load Balancer (CLB) instance, originally called a Server Load Balancer (SLB) instance.
        # *   **EIP**: an elastic IP address (EIP). An Internet-facing Application Load Balancer (ALB) instance uses an EIP. If the IP address belongs to the Internet-facing ALB instance, set this parameter to EIP.
        # *   **WAF**: a Web Application Firewall (WAF) instance.
        self.product_name = product_name  # type: str
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePackIpListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribePackIpListResponseBodyIpList(TeaModel):
    def __init__(self, ip=None, member_uid=None, nsm_status=None, product=None, region=None, remark=None, status=None):
        # The IP address.
        self.ip = ip  # type: str
        # The ID of the member.
        self.member_uid = member_uid  # type: str
        self.nsm_status = nsm_status  # type: int
        # The type of the cloud asset to which the IP address belongs. Valid values:
        # 
        # *   **ECS**: an ECS instance.
        # *   **SLB**: a CLB instance, originally called an SLB instance.
        # *   **EIP**: an EIP. If the IP address belongs to an ALB instance, the value EIP is returned.
        # *   **WAF**: a WAF instance.
        self.product = product  # type: str
        # The region to which the protected IP address belongs.
        # 
        # >  If the protected IP address is in the same region as the instance, this parameter is not returned.
        self.region = region  # type: str
        # The description of the cloud asset to which the IP address belongs. The asset can be an ECS instance or an SLB instance.
        # 
        # >  If no descriptions are provided for the asset, this parameter is not returned.
        self.remark = remark  # type: str
        # The status of the IP address. Valid values:
        # 
        # *   **normal**: The IP address is in the normal state, which indicates that the IP address is not under attack.
        # *   **hole_begin**: Blackhole filtering is triggered for the IP address.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePackIpListResponseBodyIpList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.nsm_status is not None:
            result['NsmStatus'] = self.nsm_status
        if self.product is not None:
            result['Product'] = self.product
        if self.region is not None:
            result['Region'] = self.region
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('NsmStatus') is not None:
            self.nsm_status = m.get('NsmStatus')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribePackIpListResponseBody(TeaModel):
    def __init__(self, code=None, ip_list=None, request_id=None, success=None, total=None):
        # The HTTP status code of the request.
        # 
        # For more information about status codes, see [Common parameters](~~118841~~).
        self.code = code  # type: str
        # The IP addresses that are protected by the instance.
        self.ip_list = ip_list  # type: list[DescribePackIpListResponseBodyIpList]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The call is successful.
        # *   **false**: The call fails.
        self.success = success  # type: bool
        # The number of protected IP addresses.
        self.total = total  # type: int

    def validate(self):
        if self.ip_list:
            for k in self.ip_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePackIpListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['IpList'] = []
        if self.ip_list is not None:
            for k in self.ip_list:
                result['IpList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.ip_list = []
        if m.get('IpList') is not None:
            for k in m.get('IpList'):
                temp_model = DescribePackIpListResponseBodyIpList()
                self.ip_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribePackIpListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePackIpListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePackIpListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePackIpListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, region_id=None, resource_group_id=None):
        # The region ID to query. The default value is **cn-hangzhou**, which indicates that the regions of cloud assets that are supported by an Anti-DDoS Origin instance in the China (Hangzhou) region are queried.
        # 
        # For more information about the IDs of other regions, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](~~94485~~).
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
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


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region_en_name=None, region_id=None, region_name=None):
        # The English name of the region where the cloud assets reside.
        self.region_en_name = region_en_name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The name of the region where the cloud assets reside.
        self.region_name = region_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_en_name is not None:
            result['RegionEnName'] = self.region_en_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionEnName') is not None:
            self.region_en_name = m.get('RegionEnName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, code=None, regions=None, request_id=None, success=None):
        # The HTTP status code.
        self.code = code  # type: str
        # The information about regions of the cloud assets that are supported by the Anti-DDoS Origin instance. The information includes region IDs and names.
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request failed.
        self.success = success  # type: bool

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
        if self.code is not None:
            result['Code'] = self.code
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrafficRequest(TeaModel):
    def __init__(self, end_time=None, flow_type=None, instance_id=None, interval=None, ip=None, ipnet=None,
                 region_id=None, resource_group_id=None, start_time=None):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # If you do not specify this parameter, the current system time is used as the end time.
        self.end_time = end_time  # type: int
        # The type of the traffic statistics to query. Valid values:
        # 
        # *   **max**: the peak traffic within the specified interval
        # *   **avg**: the average traffic within the specified interval
        self.flow_type = flow_type  # type: str
        # The ID of the Anti-DDoS Origin instance to query.
        # 
        # >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin instances.
        # 
        # If you specify an on-demand instance, you must configure the **Interval** parameter.
        self.instance_id = instance_id  # type: str
        # The interval at which the traffic statistics are calculated. Unit: seconds. Default value: **5**.
        self.interval = interval  # type: int
        # The public IP address of the asset to query. If you do not specify this parameter, the traffic statistics of all public IP addresses that are protected by the Anti-DDoS Origin instance are queried.
        # 
        # >  The public IP address must be a protected object of the Anti-DDoS Origin instance. You can call the [DescribePackIpList](~~118701~~) operation to query all protected objects of the Anti-DDoS Origin instance.
        self.ip = ip  # type: str
        # The Classless Inter-Domain Routing (CIDR) block of the on-demand instance that you want to query.
        self.ipnet = ipnet  # type: str
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTrafficRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.flow_type is not None:
            result['FlowType'] = self.flow_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.ipnet is not None:
            result['Ipnet'] = self.ipnet
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Ipnet') is not None:
            self.ipnet = m.get('Ipnet')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeTrafficResponseBodyFlowList(TeaModel):
    def __init__(self, attack_bps=None, attack_pps=None, flow_type=None, kbps=None, name=None, pps=None, time=None):
        # The bandwidth of attack traffic. Unit: bit/s.
        # 
        # >  This parameter is returned only if attack traffic exists.
        self.attack_bps = attack_bps  # type: long
        # The packet forwarding rate of attack traffic. Unit: packets per second.
        # 
        # >  This parameter is returned only if attack traffic exists.
        self.attack_pps = attack_pps  # type: long
        # The type of the traffic statistics. Valid values:
        # 
        # *   **max**: the peak traffic within the specified interval
        # *   **avg**: the average traffic within the specified interval
        self.flow_type = flow_type  # type: str
        # The bandwidth of the total traffic. Unit: Kbit/s.
        self.kbps = kbps  # type: int
        # The ID of the traffic statistics.
        self.name = name  # type: str
        # The packet forwarding rate of the total traffic. Unit: packets per second.
        self.pps = pps  # type: int
        # The time when the traffic statistics are calculated. This value is a UNIX timestamp. Unit: seconds.
        self.time = time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTrafficResponseBodyFlowList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_bps is not None:
            result['AttackBps'] = self.attack_bps
        if self.attack_pps is not None:
            result['AttackPps'] = self.attack_pps
        if self.flow_type is not None:
            result['FlowType'] = self.flow_type
        if self.kbps is not None:
            result['Kbps'] = self.kbps
        if self.name is not None:
            result['Name'] = self.name
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttackBps') is not None:
            self.attack_bps = m.get('AttackBps')
        if m.get('AttackPps') is not None:
            self.attack_pps = m.get('AttackPps')
        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')
        if m.get('Kbps') is not None:
            self.kbps = m.get('Kbps')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeTrafficResponseBody(TeaModel):
    def __init__(self, flow_list=None, request_id=None):
        # The queried traffic statistics.
        self.flow_list = flow_list  # type: list[DescribeTrafficResponseBodyFlowList]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.flow_list:
            for k in self.flow_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTrafficResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FlowList'] = []
        if self.flow_list is not None:
            for k in self.flow_list:
                result['FlowList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.flow_list = []
        if m.get('FlowList') is not None:
            for k in m.get('FlowList'):
                temp_model = DescribeTrafficResponseBodyFlowList()
                self.flow_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTrafficResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTrafficResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTrafficResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTrafficResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DettachAssetGroupToInstanceRequestAssetGroupList(TeaModel):
    def __init__(self, name=None, region=None, type=None):
        # The ID of the asset. If the asset is a Web Application Firewall (WAF) instance, specify the ID of the WAF instance.
        self.name = name  # type: str
        # The region ID of the asset.
        self.region = region  # type: str
        # The type of the asset. Valid values:
        # 
        # *   **waf**: WAF instance
        # *   **ga**: Global Accelerator (GA) instance
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DettachAssetGroupToInstanceRequestAssetGroupList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region is not None:
            result['Region'] = self.region
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DettachAssetGroupToInstanceRequest(TeaModel):
    def __init__(self, asset_group_list=None, instance_id=None, region_id=None, source_ip=None):
        # The information about the asset that you want to dissociate.
        self.asset_group_list = asset_group_list  # type: list[DettachAssetGroupToInstanceRequestAssetGroupList]
        # The ID of the instance.
        # 
        # >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin instances of paid editions.
        self.instance_id = instance_id  # type: str
        # The ID of the region in which the instance resides.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The source IP address of the request. The system specifies this parameter.
        self.source_ip = source_ip  # type: str

    def validate(self):
        if self.asset_group_list:
            for k in self.asset_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DettachAssetGroupToInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AssetGroupList'] = []
        if self.asset_group_list is not None:
            for k in self.asset_group_list:
                result['AssetGroupList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.asset_group_list = []
        if m.get('AssetGroupList') is not None:
            for k in m.get('AssetGroupList'):
                temp_model = DettachAssetGroupToInstanceRequestAssetGroupList()
                self.asset_group_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DettachAssetGroupToInstanceShrinkRequest(TeaModel):
    def __init__(self, asset_group_list_shrink=None, instance_id=None, region_id=None, source_ip=None):
        # The information about the asset that you want to dissociate.
        self.asset_group_list_shrink = asset_group_list_shrink  # type: str
        # The ID of the instance.
        # 
        # >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin instances of paid editions.
        self.instance_id = instance_id  # type: str
        # The ID of the region in which the instance resides.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The source IP address of the request. The system specifies this parameter.
        self.source_ip = source_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DettachAssetGroupToInstanceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_group_list_shrink is not None:
            result['AssetGroupList'] = self.asset_group_list_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetGroupList') is not None:
            self.asset_group_list_shrink = m.get('AssetGroupList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DettachAssetGroupToInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DettachAssetGroupToInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DettachAssetGroupToInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DettachAssetGroupToInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DettachAssetGroupToInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DettachAssetGroupToInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSlsOpenStatusRequest(TeaModel):
    def __init__(self, region_id=None, resource_group_id=None):
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # For more information about the valid values of this parameter, see [Regions and zones](~~188196~~).
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management. This parameter is empty by default, which indicates that the Anti-DDoS Origin instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](~~94485~~).
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSlsOpenStatusRequest, self).to_map()
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


class GetSlsOpenStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, sls_open_status=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether Log Service was activated. Valid values:
        # 
        # *   **true**: Log Service was activated.
        # *   **false**: Log Service was not activated.
        self.sls_open_status = sls_open_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSlsOpenStatusResponseBody, self).to_map()
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


class GetSlsOpenStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSlsOpenStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSlsOpenStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSlsOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOpenedAccessLogInstancesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, resource_group_id=None):
        # The number of the page to return. Pages start from page 1. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size  # type: int
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management. This parameter is empty by default, which indicates that the Anti-DDoS Origin instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](~~94485~~).
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOpenedAccessLogInstancesRequest, self).to_map()
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


class ListOpenedAccessLogInstancesResponseBodySlsConfigStatus(TeaModel):
    def __init__(self, enable=None, instance_id=None):
        # Indicates whether log analysis was enabled for the Anti-DDoS Origin instance. Valid values:
        # 
        # *   **true**: Log analysis was enabled.
        # *   **false**: Log analysis was disabled.
        self.enable = enable  # type: bool
        # The ID of the Anti-DDoS Origin instance.
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOpenedAccessLogInstancesResponseBodySlsConfigStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListOpenedAccessLogInstancesResponseBody(TeaModel):
    def __init__(self, request_id=None, sls_config_status=None, total_count=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The configuration of log analysis for the Anti-DDoS Origin instance.
        self.sls_config_status = sls_config_status  # type: list[ListOpenedAccessLogInstancesResponseBodySlsConfigStatus]
        # The number of the Anti-DDoS Origin instances for which log analysis was enabled.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.sls_config_status:
            for k in self.sls_config_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOpenedAccessLogInstancesResponseBody, self).to_map()
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
                temp_model = ListOpenedAccessLogInstancesResponseBodySlsConfigStatus()
                self.sls_config_status.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOpenedAccessLogInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOpenedAccessLogInstancesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOpenedAccessLogInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListOpenedAccessLogInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(self, current_page=None, page_size=None, region_id=None, resource_group_id=None,
                 resource_type=None):
        # The number of the page to return. Pages start from page **1**. Default value: **1**.
        self.current_page = current_page  # type: int
        # The number of entries to return on each page. Valid values: 1 to **50**. Default value: **10**.
        self.page_size = page_size  # type: int
        # The region ID.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The type of the resource. Valid value: **INSTANCE**.
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
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
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagKeysResponseBodyTagKeys(TeaModel):
    def __init__(self, tag_count=None, tag_key=None):
        # The total number of tag values that correspond to each key.
        self.tag_count = tag_count  # type: int
        # The key of each tag.
        self.tag_key = tag_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagKeysResponseBodyTagKeys, self).to_map()
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


class ListTagKeysResponseBody(TeaModel):
    def __init__(self, current_page=None, page_size=None, request_id=None, tag_keys=None, total_count=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The list of tags and the details of each tag.
        self.tag_keys = tag_keys  # type: list[ListTagKeysResponseBodyTagKeys]
        # The total number of tags.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.tag_keys:
            for k in self.tag_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
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
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k in m.get('TagKeys'):
                temp_model = ListTagKeysResponseBodyTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagKeysResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagKeysResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag to query.
        # 
        # >  The **ResourceIds.N** parameter and the key-value pair (Tag.N.Key and Tag.N.Value) cannot be left empty at the same time.
        self.key = key  # type: str
        # The value of the tag to query.
        # 
        # >  The **ResourceIds.N** parameter and the key-value pair (Tag.N.Key and Tag.N.Value) cannot be left empty at the same time.
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
    def __init__(self, next_token=None, region_id=None, resource_group_id=None, resource_id=None,
                 resource_type=None, tag=None):
        # The query token. Set the value to the **NextToken** value that is returned in the last call to the ListTagResources operation. Leave this parameter empty the first time you call this operation.
        self.next_token = next_token  # type: str
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The IDs of Anti-DDoS Origin Instances to query.
        # 
        # >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin instances.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resource to query. Set the value to **INSTANCE**, which indicates instances.
        self.resource_type = resource_type  # type: str
        # The tags to query.
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        # The ID of the Anti-DDoS Origin instance.
        self.resource_id = resource_id  # type: str
        # The type of the resource. The value is fixed as **INSTANCE**, which indicates instances.
        self.resource_type = resource_type  # type: str
        # The key of the tag that is added to the instance.
        self.tag_key = tag_key  # type: str
        # The value of the tag that is added to the instance.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResourcesTagResource, self).to_map()
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


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, tag_resource=None):
        self.tag_resource = tag_resource  # type: list[ListTagResourcesResponseBodyTagResourcesTagResource]

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
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
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        # The query token that is returned in this call.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The list of tags that are added to the Anti-DDoS Origin instance.
        self.tag_resources = tag_resources  # type: ListTagResourcesResponseBodyTagResources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
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
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRemarkRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, remark=None, resource_group_id=None):
        # The ID of the Anti-DDoS Origin instance for which you want to add remarks.
        # 
        # >  You can call the [DescribeInstanceList](~~118698~~) operation to query the IDs of all Anti-DDoS Origin instances.
        self.instance_id = instance_id  # type: str
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The remarks for the Anti-DDoS Origin instance.
        self.remark = remark  # type: str
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyRemarkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyRemarkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyRemarkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyRemarkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyRemarkResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyRemarkResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySchedruleOnDemandRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        # The ID of the on-demand instance.
        # 
        # >  You can call the [DescribeOnDemandInstance](~~152120~~) operation to query the IDs of all on-demand instances.
        self.instance_id = instance_id  # type: str
        # The region ID of the on-demand instance.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query all regions supported by Anti-DDoS Origin.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySchedruleOnDemandRequest, self).to_map()
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


class QuerySchedruleOnDemandResponseBodyRuleConfig(TeaModel):
    def __init__(self, rule_action=None, rule_condition_cnt=None, rule_condition_kpps=None,
                 rule_condition_mbps=None, rule_name=None, rule_switch=None, rule_undo_begin_time=None, rule_undo_end_time=None,
                 rule_undo_mode=None, time_zone=None):
        # The scheduling action. Set the value to **declare**, which indicates that the route is advertised.
        self.rule_action = rule_action  # type: str
        # If the inbound bandwidth or packets consecutively exceed the threshold for the specified number of times, the scheduling rule is triggered and traffic is rerouted to the on-demand instance. The specified number of times is the value of this parameter.
        # 
        # >  The threshold of inbound bandwidth is the value of **RuleConditionMbps**. The threshold of inbound packets is the value of **RuleConditionKpps**.
        self.rule_condition_cnt = rule_condition_cnt  # type: str
        # The threshold of inbound packets. Unit: Kpps. Minimum value: **10**.
        self.rule_condition_kpps = rule_condition_kpps  # type: str
        # The threshold of inbound bandwidth. Unit: Mbit/s. Minimum value: **100**.
        self.rule_condition_mbps = rule_condition_mbps  # type: str
        # The name of the scheduling rule.
        self.rule_name = rule_name  # type: str
        # Indicates whether the scheduling rule is enabled. Valid values:
        # 
        # *   **on**: enabled
        # *   **off**: disabled
        self.rule_switch = rule_switch  # type: str
        # The start time of the period during which the scheduling rule is automatically stopped. The time must be in the 24-hour clock and in the `hh:mm` format.
        # 
        # If the system detects that DDoS attacks stop, the system no longer reroutes traffic to the on-demand instance from the time you specified. We recommend that you set this parameter to a value that is defined as off-peak hours.
        # 
        # >  This parameter takes effect only when the **RuleUndoMode** parameter is set to **auto**.
        self.rule_undo_begin_time = rule_undo_begin_time  # type: str
        # The end time of the period during which the scheduling rule is automatically stopped. The time must be in the 24-hour clock and in the `hh:mm` format.
        self.rule_undo_end_time = rule_undo_end_time  # type: str
        # The stop method of the scheduling rule. Valid values:
        # 
        # *   **auto**: The scheduling rule automatically stops.
        # *   **manual**: The scheduling rule is manually stopped.
        self.rule_undo_mode = rule_undo_mode  # type: str
        # The time zone of the time when the scheduling rule automatically stops. The time zone must be in the `GMT-hh:mm` format.
        # 
        # For example, the value `GMT-08:00` indicates that the time zone is UTC+8.
        # 
        # >  This parameter takes effect only when the **RuleUndoMode** parameter is set to **auto**.
        self.time_zone = time_zone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySchedruleOnDemandResponseBodyRuleConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action
        if self.rule_condition_cnt is not None:
            result['RuleConditionCnt'] = self.rule_condition_cnt
        if self.rule_condition_kpps is not None:
            result['RuleConditionKpps'] = self.rule_condition_kpps
        if self.rule_condition_mbps is not None:
            result['RuleConditionMbps'] = self.rule_condition_mbps
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_switch is not None:
            result['RuleSwitch'] = self.rule_switch
        if self.rule_undo_begin_time is not None:
            result['RuleUndoBeginTime'] = self.rule_undo_begin_time
        if self.rule_undo_end_time is not None:
            result['RuleUndoEndTime'] = self.rule_undo_end_time
        if self.rule_undo_mode is not None:
            result['RuleUndoMode'] = self.rule_undo_mode
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')
        if m.get('RuleConditionCnt') is not None:
            self.rule_condition_cnt = m.get('RuleConditionCnt')
        if m.get('RuleConditionKpps') is not None:
            self.rule_condition_kpps = m.get('RuleConditionKpps')
        if m.get('RuleConditionMbps') is not None:
            self.rule_condition_mbps = m.get('RuleConditionMbps')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleSwitch') is not None:
            self.rule_switch = m.get('RuleSwitch')
        if m.get('RuleUndoBeginTime') is not None:
            self.rule_undo_begin_time = m.get('RuleUndoBeginTime')
        if m.get('RuleUndoEndTime') is not None:
            self.rule_undo_end_time = m.get('RuleUndoEndTime')
        if m.get('RuleUndoMode') is not None:
            self.rule_undo_mode = m.get('RuleUndoMode')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class QuerySchedruleOnDemandResponseBodyRuleStatus(TeaModel):
    def __init__(self, net=None, rule_sched_status=None):
        # The CIDR block of the on-demand instance.
        self.net = net  # type: str
        # The scheduling status. Valid values:
        # 
        # *   **scheduled**\
        # *   **unscheduled**\
        self.rule_sched_status = rule_sched_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySchedruleOnDemandResponseBodyRuleStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net is not None:
            result['Net'] = self.net
        if self.rule_sched_status is not None:
            result['RuleSchedStatus'] = self.rule_sched_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Net') is not None:
            self.net = m.get('Net')
        if m.get('RuleSchedStatus') is not None:
            self.rule_sched_status = m.get('RuleSchedStatus')
        return self


class QuerySchedruleOnDemandResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None, rule_config=None, rule_status=None, user_id=None):
        # The ID of the on-demand instance.
        self.instance_id = instance_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The configurations of the scheduling rule.
        self.rule_config = rule_config  # type: list[QuerySchedruleOnDemandResponseBodyRuleConfig]
        # The status of the scheduling rule.
        self.rule_status = rule_status  # type: list[QuerySchedruleOnDemandResponseBodyRuleStatus]
        # The ID of the Alibaba Cloud account.
        self.user_id = user_id  # type: str

    def validate(self):
        if self.rule_config:
            for k in self.rule_config:
                if k:
                    k.validate()
        if self.rule_status:
            for k in self.rule_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySchedruleOnDemandResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RuleConfig'] = []
        if self.rule_config is not None:
            for k in self.rule_config:
                result['RuleConfig'].append(k.to_map() if k else None)
        result['RuleStatus'] = []
        if self.rule_status is not None:
            for k in self.rule_status:
                result['RuleStatus'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_config = []
        if m.get('RuleConfig') is not None:
            for k in m.get('RuleConfig'):
                temp_model = QuerySchedruleOnDemandResponseBodyRuleConfig()
                self.rule_config.append(temp_model.from_map(k))
        self.rule_status = []
        if m.get('RuleStatus') is not None:
            for k in m.get('RuleStatus'):
                temp_model = QuerySchedruleOnDemandResponseBodyRuleStatus()
                self.rule_status.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QuerySchedruleOnDemandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySchedruleOnDemandResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySchedruleOnDemandResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QuerySchedruleOnDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetInstanceModeOnDemandRequest(TeaModel):
    def __init__(self, instance_id_list=None, mode=None, region_id=None):
        # The IDs of on-demand instances.
        # 
        # >  You can call the [DescribeOnDemandInstance](~~152120~~) operation to query the IDs of all on-demand instances.
        self.instance_id_list = instance_id_list  # type: list[str]
        # The scheduling mode of the on-demand instance. Valid values:
        # 
        # *   **manual**: manual scheduling
        # *   **netflow-auto**: automatic scheduling
        self.mode = mode  # type: str
        # The region ID of the on-demand instance.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query all regions supported by Anti-DDoS Origin.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetInstanceModeOnDemandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetInstanceModeOnDemandResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetInstanceModeOnDemandResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetInstanceModeOnDemandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetInstanceModeOnDemandResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetInstanceModeOnDemandResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetInstanceModeOnDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag to add.
        # 
        # >  If the specified key does not exist, a key is created.
        self.key = key  # type: str
        # The value of the tag to add.
        # 
        # >  If the specified value does not exist, a value is created.
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
    def __init__(self, region_id=None, resource_group_id=None, resource_id=None, resource_type=None, tag=None):
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](~~118703~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        # The type of the resource to which you want to add tags. Set the value to **INSTANCE**, which indicates instances.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, region_id=None, resource_group_id=None, resource_id=None, resource_type=None,
                 tag_key=None):
        # Specifies whether to remove all tags from the specified Anti-DDoS Origin Enterprise instances.
        self.all = all  # type: bool
        # The ID of the region where the Anti-DDoS Origin Enterprise instances reside.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        # The type of the specified resource. Set the value to **INSTANCE**.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UntagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


