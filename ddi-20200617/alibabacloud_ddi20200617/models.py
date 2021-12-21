# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CloneFlowRequest(TeaModel):
    def __init__(self, id=None, project_id=None, region_id=None):
        self.id = id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CloneFlowResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CloneFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloneFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CloneFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneFlowJobRequest(TeaModel):
    def __init__(self, id=None, name=None, project_id=None, region_id=None):
        self.id = id  # type: str
        self.name = name  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneFlowJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CloneFlowJobResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloneFlowJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneFlowJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CloneFlowJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloneFlowJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CloneFlowJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CommitFlowEntitySnapshotRequest(TeaModel):
    def __init__(self, entity_id=None, entity_type=None, message=None, region_id=None, resource_owner_id=None):
        self.entity_id = entity_id  # type: str
        self.entity_type = entity_type  # type: str
        self.message = message  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CommitFlowEntitySnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CommitFlowEntitySnapshotResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CommitFlowEntitySnapshotResponseBody, self).to_map()
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


class CommitFlowEntitySnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CommitFlowEntitySnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CommitFlowEntitySnapshotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CommitFlowEntitySnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterV2RequestBootstrapAction(TeaModel):
    def __init__(self, arg=None, name=None, path=None):
        self.arg = arg  # type: str
        self.name = name  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterV2RequestBootstrapAction, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateClusterV2RequestConfig(TeaModel):
    def __init__(self, config_key=None, config_value=None, encrypt=None, file_name=None, replace=None,
                 service_name=None):
        self.config_key = config_key  # type: str
        self.config_value = config_value  # type: str
        self.encrypt = encrypt  # type: str
        self.file_name = file_name  # type: str
        self.replace = replace  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterV2RequestConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.replace is not None:
            result['Replace'] = self.replace
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Replace') is not None:
            self.replace = m.get('Replace')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class CreateClusterV2RequestHostComponentInfo(TeaModel):
    def __init__(self, component_name_list=None, host_name=None, service_name=None):
        self.component_name_list = component_name_list  # type: list[str]
        self.host_name = host_name  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterV2RequestHostComponentInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name_list is not None:
            result['ComponentNameList'] = self.component_name_list
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentNameList') is not None:
            self.component_name_list = m.get('ComponentNameList')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class CreateClusterV2RequestHostGroup(TeaModel):
    def __init__(self, auto_renew=None, charge_type=None, cluster_id=None, comment=None, create_type=None,
                 disk_capacity=None, disk_count=None, disk_type=None, gpu_driver=None, host_group_id=None, host_group_name=None,
                 host_group_type=None, instance_type=None, node_count=None, period=None, sys_disk_capacity=None, sys_disk_type=None,
                 v_switch_id=None):
        self.auto_renew = auto_renew  # type: bool
        self.charge_type = charge_type  # type: str
        self.cluster_id = cluster_id  # type: str
        self.comment = comment  # type: str
        self.create_type = create_type  # type: str
        self.disk_capacity = disk_capacity  # type: int
        self.disk_count = disk_count  # type: int
        self.disk_type = disk_type  # type: str
        self.gpu_driver = gpu_driver  # type: str
        self.host_group_id = host_group_id  # type: str
        self.host_group_name = host_group_name  # type: str
        self.host_group_type = host_group_type  # type: str
        self.instance_type = instance_type  # type: str
        self.node_count = node_count  # type: int
        self.period = period  # type: int
        self.sys_disk_capacity = sys_disk_capacity  # type: int
        self.sys_disk_type = sys_disk_type  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterV2RequestHostGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.create_type is not None:
            result['CreateType'] = self.create_type
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.disk_count is not None:
            result['DiskCount'] = self.disk_count
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.gpu_driver is not None:
            result['GpuDriver'] = self.gpu_driver
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.host_group_type is not None:
            result['HostGroupType'] = self.host_group_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.period is not None:
            result['Period'] = self.period
        if self.sys_disk_capacity is not None:
            result['SysDiskCapacity'] = self.sys_disk_capacity
        if self.sys_disk_type is not None:
            result['SysDiskType'] = self.sys_disk_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('DiskCount') is not None:
            self.disk_count = m.get('DiskCount')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('GpuDriver') is not None:
            self.gpu_driver = m.get('GpuDriver')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('HostGroupType') is not None:
            self.host_group_type = m.get('HostGroupType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('SysDiskCapacity') is not None:
            self.sys_disk_capacity = m.get('SysDiskCapacity')
        if m.get('SysDiskType') is not None:
            self.sys_disk_type = m.get('SysDiskType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateClusterV2RequestPromotionInfo(TeaModel):
    def __init__(self, product_code=None, promotion_option_code=None, promotion_option_no=None):
        self.product_code = product_code  # type: str
        self.promotion_option_code = promotion_option_code  # type: str
        self.promotion_option_no = promotion_option_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterV2RequestPromotionInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.promotion_option_code is not None:
            result['PromotionOptionCode'] = self.promotion_option_code
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('PromotionOptionCode') is not None:
            self.promotion_option_code = m.get('PromotionOptionCode')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        return self


class CreateClusterV2RequestServiceInfo(TeaModel):
    def __init__(self, service_name=None, service_version=None):
        self.service_name = service_name  # type: str
        self.service_version = service_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterV2RequestServiceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class CreateClusterV2RequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterV2RequestTag, self).to_map()
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


class CreateClusterV2RequestUserInfo(TeaModel):
    def __init__(self, password=None, user_id=None, user_name=None):
        self.password = password  # type: str
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterV2RequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateClusterV2Request(TeaModel):
    def __init__(self, authorize_content=None, auto=None, auto_pay_order=None, bootstrap_action=None,
                 charge_type=None, click_house_conf=None, client_token=None, cluster_type=None, config=None,
                 configurations=None, deposit_type=None, emr_ver=None, enable_eas=None, enable_high_availability=None,
                 enable_ssh=None, extra_attributes=None, host_component_info=None, host_group=None,
                 init_custom_hive_meta_db=None, instance_generation=None, is_open_public_ip=None, key_pair_name=None, log_path=None,
                 machine_type=None, master_pwd=None, meta_store_conf=None, meta_store_type=None, name=None, net_type=None,
                 period=None, promotion_info=None, region_id=None, related_cluster_id=None, resource_group_id=None,
                 resource_owner_id=None, security_group_id=None, security_group_name=None, service_info=None, tag=None,
                 use_custom_hive_meta_db=None, use_local_meta_db=None, user_defined_emr_ecs_role=None, user_info=None, v_switch_id=None,
                 vpc_id=None, white_list_type=None, zone_id=None):
        self.authorize_content = authorize_content  # type: str
        self.auto = auto  # type: bool
        self.auto_pay_order = auto_pay_order  # type: bool
        self.bootstrap_action = bootstrap_action  # type: list[CreateClusterV2RequestBootstrapAction]
        self.charge_type = charge_type  # type: str
        self.click_house_conf = click_house_conf  # type: str
        self.client_token = client_token  # type: str
        self.cluster_type = cluster_type  # type: str
        self.config = config  # type: list[CreateClusterV2RequestConfig]
        self.configurations = configurations  # type: str
        self.deposit_type = deposit_type  # type: str
        self.emr_ver = emr_ver  # type: str
        self.enable_eas = enable_eas  # type: bool
        self.enable_high_availability = enable_high_availability  # type: bool
        self.enable_ssh = enable_ssh  # type: bool
        self.extra_attributes = extra_attributes  # type: str
        self.host_component_info = host_component_info  # type: list[CreateClusterV2RequestHostComponentInfo]
        self.host_group = host_group  # type: list[CreateClusterV2RequestHostGroup]
        self.init_custom_hive_meta_db = init_custom_hive_meta_db  # type: bool
        self.instance_generation = instance_generation  # type: str
        self.is_open_public_ip = is_open_public_ip  # type: bool
        self.key_pair_name = key_pair_name  # type: str
        self.log_path = log_path  # type: str
        self.machine_type = machine_type  # type: str
        self.master_pwd = master_pwd  # type: str
        self.meta_store_conf = meta_store_conf  # type: str
        self.meta_store_type = meta_store_type  # type: str
        self.name = name  # type: str
        self.net_type = net_type  # type: str
        self.period = period  # type: int
        self.promotion_info = promotion_info  # type: list[CreateClusterV2RequestPromotionInfo]
        self.region_id = region_id  # type: str
        self.related_cluster_id = related_cluster_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.security_group_id = security_group_id  # type: str
        self.security_group_name = security_group_name  # type: str
        self.service_info = service_info  # type: list[CreateClusterV2RequestServiceInfo]
        self.tag = tag  # type: list[CreateClusterV2RequestTag]
        self.use_custom_hive_meta_db = use_custom_hive_meta_db  # type: bool
        self.use_local_meta_db = use_local_meta_db  # type: bool
        self.user_defined_emr_ecs_role = user_defined_emr_ecs_role  # type: str
        self.user_info = user_info  # type: list[CreateClusterV2RequestUserInfo]
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.white_list_type = white_list_type  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.bootstrap_action:
            for k in self.bootstrap_action:
                if k:
                    k.validate()
        if self.config:
            for k in self.config:
                if k:
                    k.validate()
        if self.host_component_info:
            for k in self.host_component_info:
                if k:
                    k.validate()
        if self.host_group:
            for k in self.host_group:
                if k:
                    k.validate()
        if self.promotion_info:
            for k in self.promotion_info:
                if k:
                    k.validate()
        if self.service_info:
            for k in self.service_info:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.user_info:
            for k in self.user_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateClusterV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorize_content is not None:
            result['AuthorizeContent'] = self.authorize_content
        if self.auto is not None:
            result['Auto'] = self.auto
        if self.auto_pay_order is not None:
            result['AutoPayOrder'] = self.auto_pay_order
        result['BootstrapAction'] = []
        if self.bootstrap_action is not None:
            for k in self.bootstrap_action:
                result['BootstrapAction'].append(k.to_map() if k else None)
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.click_house_conf is not None:
            result['ClickHouseConf'] = self.click_house_conf
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        result['Config'] = []
        if self.config is not None:
            for k in self.config:
                result['Config'].append(k.to_map() if k else None)
        if self.configurations is not None:
            result['Configurations'] = self.configurations
        if self.deposit_type is not None:
            result['DepositType'] = self.deposit_type
        if self.emr_ver is not None:
            result['EmrVer'] = self.emr_ver
        if self.enable_eas is not None:
            result['EnableEas'] = self.enable_eas
        if self.enable_high_availability is not None:
            result['EnableHighAvailability'] = self.enable_high_availability
        if self.enable_ssh is not None:
            result['EnableSsh'] = self.enable_ssh
        if self.extra_attributes is not None:
            result['ExtraAttributes'] = self.extra_attributes
        result['HostComponentInfo'] = []
        if self.host_component_info is not None:
            for k in self.host_component_info:
                result['HostComponentInfo'].append(k.to_map() if k else None)
        result['HostGroup'] = []
        if self.host_group is not None:
            for k in self.host_group:
                result['HostGroup'].append(k.to_map() if k else None)
        if self.init_custom_hive_meta_db is not None:
            result['InitCustomHiveMetaDB'] = self.init_custom_hive_meta_db
        if self.instance_generation is not None:
            result['InstanceGeneration'] = self.instance_generation
        if self.is_open_public_ip is not None:
            result['IsOpenPublicIp'] = self.is_open_public_ip
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.log_path is not None:
            result['LogPath'] = self.log_path
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        if self.master_pwd is not None:
            result['MasterPwd'] = self.master_pwd
        if self.meta_store_conf is not None:
            result['MetaStoreConf'] = self.meta_store_conf
        if self.meta_store_type is not None:
            result['MetaStoreType'] = self.meta_store_type
        if self.name is not None:
            result['Name'] = self.name
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.period is not None:
            result['Period'] = self.period
        result['PromotionInfo'] = []
        if self.promotion_info is not None:
            for k in self.promotion_info:
                result['PromotionInfo'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.related_cluster_id is not None:
            result['RelatedClusterId'] = self.related_cluster_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        result['ServiceInfo'] = []
        if self.service_info is not None:
            for k in self.service_info:
                result['ServiceInfo'].append(k.to_map() if k else None)
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.use_custom_hive_meta_db is not None:
            result['UseCustomHiveMetaDB'] = self.use_custom_hive_meta_db
        if self.use_local_meta_db is not None:
            result['UseLocalMetaDb'] = self.use_local_meta_db
        if self.user_defined_emr_ecs_role is not None:
            result['UserDefinedEmrEcsRole'] = self.user_defined_emr_ecs_role
        result['UserInfo'] = []
        if self.user_info is not None:
            for k in self.user_info:
                result['UserInfo'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.white_list_type is not None:
            result['WhiteListType'] = self.white_list_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizeContent') is not None:
            self.authorize_content = m.get('AuthorizeContent')
        if m.get('Auto') is not None:
            self.auto = m.get('Auto')
        if m.get('AutoPayOrder') is not None:
            self.auto_pay_order = m.get('AutoPayOrder')
        self.bootstrap_action = []
        if m.get('BootstrapAction') is not None:
            for k in m.get('BootstrapAction'):
                temp_model = CreateClusterV2RequestBootstrapAction()
                self.bootstrap_action.append(temp_model.from_map(k))
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClickHouseConf') is not None:
            self.click_house_conf = m.get('ClickHouseConf')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        self.config = []
        if m.get('Config') is not None:
            for k in m.get('Config'):
                temp_model = CreateClusterV2RequestConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('Configurations') is not None:
            self.configurations = m.get('Configurations')
        if m.get('DepositType') is not None:
            self.deposit_type = m.get('DepositType')
        if m.get('EmrVer') is not None:
            self.emr_ver = m.get('EmrVer')
        if m.get('EnableEas') is not None:
            self.enable_eas = m.get('EnableEas')
        if m.get('EnableHighAvailability') is not None:
            self.enable_high_availability = m.get('EnableHighAvailability')
        if m.get('EnableSsh') is not None:
            self.enable_ssh = m.get('EnableSsh')
        if m.get('ExtraAttributes') is not None:
            self.extra_attributes = m.get('ExtraAttributes')
        self.host_component_info = []
        if m.get('HostComponentInfo') is not None:
            for k in m.get('HostComponentInfo'):
                temp_model = CreateClusterV2RequestHostComponentInfo()
                self.host_component_info.append(temp_model.from_map(k))
        self.host_group = []
        if m.get('HostGroup') is not None:
            for k in m.get('HostGroup'):
                temp_model = CreateClusterV2RequestHostGroup()
                self.host_group.append(temp_model.from_map(k))
        if m.get('InitCustomHiveMetaDB') is not None:
            self.init_custom_hive_meta_db = m.get('InitCustomHiveMetaDB')
        if m.get('InstanceGeneration') is not None:
            self.instance_generation = m.get('InstanceGeneration')
        if m.get('IsOpenPublicIp') is not None:
            self.is_open_public_ip = m.get('IsOpenPublicIp')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('LogPath') is not None:
            self.log_path = m.get('LogPath')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('MasterPwd') is not None:
            self.master_pwd = m.get('MasterPwd')
        if m.get('MetaStoreConf') is not None:
            self.meta_store_conf = m.get('MetaStoreConf')
        if m.get('MetaStoreType') is not None:
            self.meta_store_type = m.get('MetaStoreType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        self.promotion_info = []
        if m.get('PromotionInfo') is not None:
            for k in m.get('PromotionInfo'):
                temp_model = CreateClusterV2RequestPromotionInfo()
                self.promotion_info.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RelatedClusterId') is not None:
            self.related_cluster_id = m.get('RelatedClusterId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        self.service_info = []
        if m.get('ServiceInfo') is not None:
            for k in m.get('ServiceInfo'):
                temp_model = CreateClusterV2RequestServiceInfo()
                self.service_info.append(temp_model.from_map(k))
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateClusterV2RequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UseCustomHiveMetaDB') is not None:
            self.use_custom_hive_meta_db = m.get('UseCustomHiveMetaDB')
        if m.get('UseLocalMetaDb') is not None:
            self.use_local_meta_db = m.get('UseLocalMetaDb')
        if m.get('UserDefinedEmrEcsRole') is not None:
            self.user_defined_emr_ecs_role = m.get('UserDefinedEmrEcsRole')
        self.user_info = []
        if m.get('UserInfo') is not None:
            for k in m.get('UserInfo'):
                temp_model = CreateClusterV2RequestUserInfo()
                self.user_info.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WhiteListType') is not None:
            self.white_list_type = m.get('WhiteListType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateClusterV2ResponseBody(TeaModel):
    def __init__(self, cluster_id=None, core_order_id=None, emr_order_id=None, master_order_id=None,
                 request_id=None):
        self.cluster_id = cluster_id  # type: str
        self.core_order_id = core_order_id  # type: str
        self.emr_order_id = emr_order_id  # type: str
        self.master_order_id = master_order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterV2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.core_order_id is not None:
            result['CoreOrderId'] = self.core_order_id
        if self.emr_order_id is not None:
            result['EmrOrderId'] = self.emr_order_id
        if self.master_order_id is not None:
            result['MasterOrderId'] = self.master_order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CoreOrderId') is not None:
            self.core_order_id = m.get('CoreOrderId')
        if m.get('EmrOrderId') is not None:
            self.emr_order_id = m.get('EmrOrderId')
        if m.get('MasterOrderId') is not None:
            self.master_order_id = m.get('MasterOrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateClusterV2Response(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateClusterV2ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateClusterV2Response, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateClusterV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowRequest(TeaModel):
    def __init__(self, alert_conf=None, alert_ding_ding_group_biz_id=None, alert_user_group_biz_id=None,
                 application=None, client_token=None, cluster_id=None, create_cluster=None, cron_expression=None,
                 description=None, end_schedule=None, host_name=None, name=None, namespace=None, parent_category=None,
                 parent_flow_list=None, project_id=None, region_id=None, start_schedule=None):
        self.alert_conf = alert_conf  # type: str
        self.alert_ding_ding_group_biz_id = alert_ding_ding_group_biz_id  # type: str
        self.alert_user_group_biz_id = alert_user_group_biz_id  # type: str
        self.application = application  # type: str
        self.client_token = client_token  # type: str
        self.cluster_id = cluster_id  # type: str
        self.create_cluster = create_cluster  # type: bool
        self.cron_expression = cron_expression  # type: str
        self.description = description  # type: str
        self.end_schedule = end_schedule  # type: long
        self.host_name = host_name  # type: str
        self.name = name  # type: str
        self.namespace = namespace  # type: str
        self.parent_category = parent_category  # type: str
        self.parent_flow_list = parent_flow_list  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.start_schedule = start_schedule  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.alert_ding_ding_group_biz_id is not None:
            result['AlertDingDingGroupBizId'] = self.alert_ding_ding_group_biz_id
        if self.alert_user_group_biz_id is not None:
            result['AlertUserGroupBizId'] = self.alert_user_group_biz_id
        if self.application is not None:
            result['Application'] = self.application
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_cluster is not None:
            result['CreateCluster'] = self.create_cluster
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.description is not None:
            result['Description'] = self.description
        if self.end_schedule is not None:
            result['EndSchedule'] = self.end_schedule
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.parent_category is not None:
            result['ParentCategory'] = self.parent_category
        if self.parent_flow_list is not None:
            result['ParentFlowList'] = self.parent_flow_list
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_schedule is not None:
            result['StartSchedule'] = self.start_schedule
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('AlertDingDingGroupBizId') is not None:
            self.alert_ding_ding_group_biz_id = m.get('AlertDingDingGroupBizId')
        if m.get('AlertUserGroupBizId') is not None:
            self.alert_user_group_biz_id = m.get('AlertUserGroupBizId')
        if m.get('Application') is not None:
            self.application = m.get('Application')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateCluster') is not None:
            self.create_cluster = m.get('CreateCluster')
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndSchedule') is not None:
            self.end_schedule = m.get('EndSchedule')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ParentCategory') is not None:
            self.parent_category = m.get('ParentCategory')
        if m.get('ParentFlowList') is not None:
            self.parent_flow_list = m.get('ParentFlowList')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartSchedule') is not None:
            self.start_schedule = m.get('StartSchedule')
        return self


class CreateFlowResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowCategoryRequest(TeaModel):
    def __init__(self, client_token=None, name=None, parent_id=None, project_id=None, region_id=None, type=None):
        self.client_token = client_token  # type: str
        self.name = name  # type: str
        self.parent_id = parent_id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFlowCategoryResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowCategoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFlowCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateFlowCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFlowCategoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFlowCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowEditLockRequest(TeaModel):
    def __init__(self, entity_id=None, force=None, region_id=None, resource_owner_id=None):
        self.entity_id = entity_id  # type: str
        self.force = force  # type: bool
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowEditLockRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.force is not None:
            result['Force'] = self.force
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateFlowEditLockResponseBody(TeaModel):
    def __init__(self, biz_id=None, entity_id=None, owner_id=None, request_id=None, status=None, user_id=None):
        self.biz_id = biz_id  # type: str
        self.entity_id = entity_id  # type: str
        self.owner_id = owner_id  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowEditLockResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateFlowEditLockResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateFlowEditLockResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFlowEditLockResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFlowEditLockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowJobRequestResourceList(TeaModel):
    def __init__(self, alias=None, path=None):
        self.alias = alias  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowJobRequestResourceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateFlowJobRequest(TeaModel):
    def __init__(self, adhoc=None, alert_conf=None, client_token=None, cluster_id=None, custom_variables=None,
                 description=None, env_conf=None, fail_act=None, mode=None, monitor_conf=None, name=None, param_conf=None,
                 params=None, parent_category=None, project_id=None, region_id=None, resource_list=None, retry_policy=None,
                 run_conf=None, type=None):
        self.adhoc = adhoc  # type: bool
        self.alert_conf = alert_conf  # type: str
        self.client_token = client_token  # type: str
        self.cluster_id = cluster_id  # type: str
        self.custom_variables = custom_variables  # type: str
        self.description = description  # type: str
        self.env_conf = env_conf  # type: str
        self.fail_act = fail_act  # type: str
        self.mode = mode  # type: str
        self.monitor_conf = monitor_conf  # type: str
        self.name = name  # type: str
        self.param_conf = param_conf  # type: str
        self.params = params  # type: str
        self.parent_category = parent_category  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_list = resource_list  # type: list[CreateFlowJobRequestResourceList]
        self.retry_policy = retry_policy  # type: str
        self.run_conf = run_conf  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateFlowJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adhoc is not None:
            result['Adhoc'] = self.adhoc
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.custom_variables is not None:
            result['CustomVariables'] = self.custom_variables
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        if self.fail_act is not None:
            result['FailAct'] = self.fail_act
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.monitor_conf is not None:
            result['MonitorConf'] = self.monitor_conf
        if self.name is not None:
            result['Name'] = self.name
        if self.param_conf is not None:
            result['ParamConf'] = self.param_conf
        if self.params is not None:
            result['Params'] = self.params
        if self.parent_category is not None:
            result['ParentCategory'] = self.parent_category
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['ResourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['ResourceList'].append(k.to_map() if k else None)
        if self.retry_policy is not None:
            result['RetryPolicy'] = self.retry_policy
        if self.run_conf is not None:
            result['RunConf'] = self.run_conf
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Adhoc') is not None:
            self.adhoc = m.get('Adhoc')
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CustomVariables') is not None:
            self.custom_variables = m.get('CustomVariables')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        if m.get('FailAct') is not None:
            self.fail_act = m.get('FailAct')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('MonitorConf') is not None:
            self.monitor_conf = m.get('MonitorConf')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamConf') is not None:
            self.param_conf = m.get('ParamConf')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ParentCategory') is not None:
            self.parent_category = m.get('ParentCategory')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k in m.get('ResourceList'):
                temp_model = CreateFlowJobRequestResourceList()
                self.resource_list.append(temp_model.from_map(k))
        if m.get('RetryPolicy') is not None:
            self.retry_policy = m.get('RetryPolicy')
        if m.get('RunConf') is not None:
            self.run_conf = m.get('RunConf')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFlowJobResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFlowJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateFlowJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFlowJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFlowJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowProjectRequest(TeaModel):
    def __init__(self, client_token=None, description=None, name=None, product_type=None, region_id=None,
                 resource_group_id=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.product_type = product_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateFlowProjectResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFlowProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateFlowProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFlowProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFlowProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowProjectClusterSettingRequest(TeaModel):
    def __init__(self, client_token=None, cluster_id=None, default_queue=None, default_user=None, host_list=None,
                 project_id=None, queue_list=None, region_id=None, user_list=None):
        self.client_token = client_token  # type: str
        self.cluster_id = cluster_id  # type: str
        self.default_queue = default_queue  # type: str
        self.default_user = default_user  # type: str
        self.host_list = host_list  # type: list[str]
        self.project_id = project_id  # type: str
        self.queue_list = queue_list  # type: list[str]
        self.region_id = region_id  # type: str
        self.user_list = user_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowProjectClusterSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.default_queue is not None:
            result['DefaultQueue'] = self.default_queue
        if self.default_user is not None:
            result['DefaultUser'] = self.default_user
        if self.host_list is not None:
            result['HostList'] = self.host_list
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.queue_list is not None:
            result['QueueList'] = self.queue_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_list is not None:
            result['UserList'] = self.user_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DefaultQueue') is not None:
            self.default_queue = m.get('DefaultQueue')
        if m.get('DefaultUser') is not None:
            self.default_user = m.get('DefaultUser')
        if m.get('HostList') is not None:
            self.host_list = m.get('HostList')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('QueueList') is not None:
            self.queue_list = m.get('QueueList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserList') is not None:
            self.user_list = m.get('UserList')
        return self


class CreateFlowProjectClusterSettingResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowProjectClusterSettingResponseBody, self).to_map()
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


class CreateFlowProjectClusterSettingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateFlowProjectClusterSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFlowProjectClusterSettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFlowProjectClusterSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowProjectUserRequestUser(TeaModel):
    def __init__(self, user_id=None, user_name=None):
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowProjectUserRequestUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateFlowProjectUserRequest(TeaModel):
    def __init__(self, client_token=None, project_id=None, region_id=None, user=None):
        self.client_token = client_token  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.user = user  # type: list[CreateFlowProjectUserRequestUser]

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateFlowProjectUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = CreateFlowProjectUserRequestUser()
                self.user.append(temp_model.from_map(k))
        return self


class CreateFlowProjectUserResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowProjectUserResponseBody, self).to_map()
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


class CreateFlowProjectUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateFlowProjectUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFlowProjectUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFlowProjectUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowRequest(TeaModel):
    def __init__(self, id=None, project_id=None, region_id=None):
        self.id = id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteFlowResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowResponseBody, self).to_map()
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


class DeleteFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowCategoryRequest(TeaModel):
    def __init__(self, id=None, project_id=None, region_id=None):
        self.id = id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteFlowCategoryResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowCategoryResponseBody, self).to_map()
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


class DeleteFlowCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteFlowCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFlowCategoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFlowCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowEditLockRequest(TeaModel):
    def __init__(self, entity_id=None, region_id=None, resource_owner_id=None):
        self.entity_id = entity_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowEditLockRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteFlowEditLockResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowEditLockResponseBody, self).to_map()
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


class DeleteFlowEditLockResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteFlowEditLockResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFlowEditLockResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFlowEditLockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowProjectRequest(TeaModel):
    def __init__(self, project_id=None, region_id=None):
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteFlowProjectResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowProjectResponseBody, self).to_map()
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


class DeleteFlowProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteFlowProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFlowProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFlowProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowProjectClusterSettingRequest(TeaModel):
    def __init__(self, cluster_id=None, project_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowProjectClusterSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteFlowProjectClusterSettingResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowProjectClusterSettingResponseBody, self).to_map()
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


class DeleteFlowProjectClusterSettingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteFlowProjectClusterSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFlowProjectClusterSettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFlowProjectClusterSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowProjectUserRequest(TeaModel):
    def __init__(self, project_id=None, region_id=None, user_name=None):
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowProjectUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DeleteFlowProjectUserResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowProjectUserResponseBody, self).to_map()
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


class DeleteFlowProjectUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteFlowProjectUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFlowProjectUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFlowProjectUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterV2Request(TeaModel):
    def __init__(self, id=None, region_id=None, resource_owner_id=None):
        self.id = id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeClusterV2ResponseBodyClusterInfoAccessInfoZKLinksZKLink(TeaModel):
    def __init__(self, link=None, port=None):
        self.link = link  # type: str
        self.port = port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoAccessInfoZKLinksZKLink, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.link is not None:
            result['Link'] = self.link
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Link') is not None:
            self.link = m.get('Link')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeClusterV2ResponseBodyClusterInfoAccessInfoZKLinks(TeaModel):
    def __init__(self, zklink=None):
        self.zklink = zklink  # type: list[DescribeClusterV2ResponseBodyClusterInfoAccessInfoZKLinksZKLink]

    def validate(self):
        if self.zklink:
            for k in self.zklink:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoAccessInfoZKLinks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ZKLink'] = []
        if self.zklink is not None:
            for k in self.zklink:
                result['ZKLink'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.zklink = []
        if m.get('ZKLink') is not None:
            for k in m.get('ZKLink'):
                temp_model = DescribeClusterV2ResponseBodyClusterInfoAccessInfoZKLinksZKLink()
                self.zklink.append(temp_model.from_map(k))
        return self


class DescribeClusterV2ResponseBodyClusterInfoAccessInfo(TeaModel):
    def __init__(self, zklinks=None):
        self.zklinks = zklinks  # type: DescribeClusterV2ResponseBodyClusterInfoAccessInfoZKLinks

    def validate(self):
        if self.zklinks:
            self.zklinks.validate()

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoAccessInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zklinks is not None:
            result['ZKLinks'] = self.zklinks.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ZKLinks') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoAccessInfoZKLinks()
            self.zklinks = temp_model.from_map(m['ZKLinks'])
        return self


class DescribeClusterV2ResponseBodyClusterInfoBootstrapActionListBootstrapAction(TeaModel):
    def __init__(self, arg=None, name=None, path=None):
        self.arg = arg  # type: str
        self.name = name  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoBootstrapActionListBootstrapAction, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeClusterV2ResponseBodyClusterInfoBootstrapActionList(TeaModel):
    def __init__(self, bootstrap_action=None):
        self.bootstrap_action = bootstrap_action  # type: list[DescribeClusterV2ResponseBodyClusterInfoBootstrapActionListBootstrapAction]

    def validate(self):
        if self.bootstrap_action:
            for k in self.bootstrap_action:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoBootstrapActionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BootstrapAction'] = []
        if self.bootstrap_action is not None:
            for k in self.bootstrap_action:
                result['BootstrapAction'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bootstrap_action = []
        if m.get('BootstrapAction') is not None:
            for k in m.get('BootstrapAction'):
                temp_model = DescribeClusterV2ResponseBodyClusterInfoBootstrapActionListBootstrapAction()
                self.bootstrap_action.append(temp_model.from_map(k))
        return self


class DescribeClusterV2ResponseBodyClusterInfoFailReason(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoFailReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterV2ResponseBodyClusterInfoGatewayClusterInfoListGatewayClusterInfo(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, status=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoGatewayClusterInfoListGatewayClusterInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClusterV2ResponseBodyClusterInfoGatewayClusterInfoList(TeaModel):
    def __init__(self, gateway_cluster_info=None):
        self.gateway_cluster_info = gateway_cluster_info  # type: list[DescribeClusterV2ResponseBodyClusterInfoGatewayClusterInfoListGatewayClusterInfo]

    def validate(self):
        if self.gateway_cluster_info:
            for k in self.gateway_cluster_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoGatewayClusterInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GatewayClusterInfo'] = []
        if self.gateway_cluster_info is not None:
            for k in self.gateway_cluster_info:
                result['GatewayClusterInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.gateway_cluster_info = []
        if m.get('GatewayClusterInfo') is not None:
            for k in m.get('GatewayClusterInfo'):
                temp_model = DescribeClusterV2ResponseBodyClusterInfoGatewayClusterInfoListGatewayClusterInfo()
                self.gateway_cluster_info.append(temp_model.from_map(k))
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDaemonInfosDaemonInfo(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDaemonInfosDaemonInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDaemonInfos(TeaModel):
    def __init__(self, daemon_info=None):
        self.daemon_info = daemon_info  # type: list[DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDaemonInfosDaemonInfo]

    def validate(self):
        if self.daemon_info:
            for k in self.daemon_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDaemonInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DaemonInfo'] = []
        if self.daemon_info is not None:
            for k in self.daemon_info:
                result['DaemonInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.daemon_info = []
        if m.get('DaemonInfo') is not None:
            for k in m.get('DaemonInfo'):
                temp_model = DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDaemonInfosDaemonInfo()
                self.daemon_info.append(temp_model.from_map(k))
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDiskInfosDiskInfo(TeaModel):
    def __init__(self, device=None, disk_id=None, disk_name=None, size=None, type=None):
        self.device = device  # type: str
        self.disk_id = disk_id  # type: str
        self.disk_name = disk_name  # type: str
        self.size = size  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDiskInfosDiskInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device is not None:
            result['Device'] = self.device
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDiskInfos(TeaModel):
    def __init__(self, disk_info=None):
        self.disk_info = disk_info  # type: list[DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDiskInfosDiskInfo]

    def validate(self):
        if self.disk_info:
            for k in self.disk_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDiskInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DiskInfo'] = []
        if self.disk_info is not None:
            for k in self.disk_info:
                result['DiskInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.disk_info = []
        if m.get('DiskInfo') is not None:
            for k in m.get('DiskInfo'):
                temp_model = DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDiskInfosDiskInfo()
                self.disk_info.append(temp_model.from_map(k))
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNode(TeaModel):
    def __init__(self, create_time=None, daemon_infos=None, disk_infos=None, emr_expired_time=None,
                 expired_time=None, inner_ip=None, instance_id=None, pub_ip=None, status=None, support_ip_v6=None, zone_id=None):
        self.create_time = create_time  # type: str
        self.daemon_infos = daemon_infos  # type: DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDaemonInfos
        self.disk_infos = disk_infos  # type: DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDiskInfos
        self.emr_expired_time = emr_expired_time  # type: str
        self.expired_time = expired_time  # type: str
        self.inner_ip = inner_ip  # type: str
        self.instance_id = instance_id  # type: str
        self.pub_ip = pub_ip  # type: str
        self.status = status  # type: str
        self.support_ip_v6 = support_ip_v6  # type: bool
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.daemon_infos:
            self.daemon_infos.validate()
        if self.disk_infos:
            self.disk_infos.validate()

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNode, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.daemon_infos is not None:
            result['DaemonInfos'] = self.daemon_infos.to_map()
        if self.disk_infos is not None:
            result['DiskInfos'] = self.disk_infos.to_map()
        if self.emr_expired_time is not None:
            result['EmrExpiredTime'] = self.emr_expired_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.inner_ip is not None:
            result['InnerIp'] = self.inner_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pub_ip is not None:
            result['PubIp'] = self.pub_ip
        if self.status is not None:
            result['Status'] = self.status
        if self.support_ip_v6 is not None:
            result['SupportIpV6'] = self.support_ip_v6
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DaemonInfos') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDaemonInfos()
            self.daemon_infos = temp_model.from_map(m['DaemonInfos'])
        if m.get('DiskInfos') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDiskInfos()
            self.disk_infos = temp_model.from_map(m['DiskInfos'])
        if m.get('EmrExpiredTime') is not None:
            self.emr_expired_time = m.get('EmrExpiredTime')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InnerIp') is not None:
            self.inner_ip = m.get('InnerIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PubIp') is not None:
            self.pub_ip = m.get('PubIp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportIpV6') is not None:
            self.support_ip_v6 = m.get('SupportIpV6')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodes(TeaModel):
    def __init__(self, node=None):
        self.node = node  # type: list[DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNode]

    def validate(self):
        if self.node:
            for k in self.node:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Node'] = []
        if self.node is not None:
            for k in self.node:
                result['Node'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.node = []
        if m.get('Node') is not None:
            for k in m.get('Node'):
                temp_model = DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNode()
                self.node.append(temp_model.from_map(k))
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroup(TeaModel):
    def __init__(self, band_width=None, charge_type=None, cpu_core=None, disk_capacity=None, disk_count=None,
                 disk_type=None, host_group_change_status=None, host_group_change_type=None, host_group_id=None,
                 host_group_name=None, host_group_sub_type=None, host_group_type=None, instance_type=None, lock_reason=None,
                 lock_type=None, memory_capacity=None, node_count=None, nodes=None, period=None):
        self.band_width = band_width  # type: str
        self.charge_type = charge_type  # type: str
        self.cpu_core = cpu_core  # type: int
        self.disk_capacity = disk_capacity  # type: int
        self.disk_count = disk_count  # type: int
        self.disk_type = disk_type  # type: str
        self.host_group_change_status = host_group_change_status  # type: str
        self.host_group_change_type = host_group_change_type  # type: str
        self.host_group_id = host_group_id  # type: str
        self.host_group_name = host_group_name  # type: str
        self.host_group_sub_type = host_group_sub_type  # type: str
        self.host_group_type = host_group_type  # type: str
        self.instance_type = instance_type  # type: str
        self.lock_reason = lock_reason  # type: str
        self.lock_type = lock_type  # type: str
        self.memory_capacity = memory_capacity  # type: int
        self.node_count = node_count  # type: int
        self.nodes = nodes  # type: DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodes
        self.period = period  # type: str

    def validate(self):
        if self.nodes:
            self.nodes.validate()

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_width is not None:
            result['BandWidth'] = self.band_width
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cpu_core is not None:
            result['CpuCore'] = self.cpu_core
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.disk_count is not None:
            result['DiskCount'] = self.disk_count
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.host_group_change_status is not None:
            result['HostGroupChangeStatus'] = self.host_group_change_status
        if self.host_group_change_type is not None:
            result['HostGroupChangeType'] = self.host_group_change_type
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.host_group_sub_type is not None:
            result['HostGroupSubType'] = self.host_group_sub_type
        if self.host_group_type is not None:
            result['HostGroupType'] = self.host_group_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.lock_type is not None:
            result['LockType'] = self.lock_type
        if self.memory_capacity is not None:
            result['MemoryCapacity'] = self.memory_capacity
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()
        if self.period is not None:
            result['Period'] = self.period
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CpuCore') is not None:
            self.cpu_core = m.get('CpuCore')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('DiskCount') is not None:
            self.disk_count = m.get('DiskCount')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('HostGroupChangeStatus') is not None:
            self.host_group_change_status = m.get('HostGroupChangeStatus')
        if m.get('HostGroupChangeType') is not None:
            self.host_group_change_type = m.get('HostGroupChangeType')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('HostGroupSubType') is not None:
            self.host_group_sub_type = m.get('HostGroupSubType')
        if m.get('HostGroupType') is not None:
            self.host_group_type = m.get('HostGroupType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('LockType') is not None:
            self.lock_type = m.get('LockType')
        if m.get('MemoryCapacity') is not None:
            self.memory_capacity = m.get('MemoryCapacity')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('Nodes') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodes()
            self.nodes = temp_model.from_map(m['Nodes'])
        if m.get('Period') is not None:
            self.period = m.get('Period')
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostGroupList(TeaModel):
    def __init__(self, host_group=None):
        self.host_group = host_group  # type: list[DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroup]

    def validate(self):
        if self.host_group:
            for k in self.host_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoHostGroupList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostGroup'] = []
        if self.host_group is not None:
            for k in self.host_group:
                result['HostGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.host_group = []
        if m.get('HostGroup') is not None:
            for k in m.get('HostGroup'):
                temp_model = DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroup()
                self.host_group.append(temp_model.from_map(k))
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostPoolInfo(TeaModel):
    def __init__(self, hp_biz_id=None, hp_name=None):
        self.hp_biz_id = hp_biz_id  # type: str
        self.hp_name = hp_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoHostPoolInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hp_biz_id is not None:
            result['HpBizId'] = self.hp_biz_id
        if self.hp_name is not None:
            result['HpName'] = self.hp_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HpBizId') is not None:
            self.hp_biz_id = m.get('HpBizId')
        if m.get('HpName') is not None:
            self.hp_name = m.get('HpName')
        return self


class DescribeClusterV2ResponseBodyClusterInfoRelateClusterInfo(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, status=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoRelateClusterInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClusterV2ResponseBodyClusterInfoSoftwareInfoSoftwaresSoftware(TeaModel):
    def __init__(self, display_name=None, name=None, only_display=None, start_tpe=None, version=None):
        self.display_name = display_name  # type: str
        self.name = name  # type: str
        self.only_display = only_display  # type: bool
        self.start_tpe = start_tpe  # type: int
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoSoftwareInfoSoftwaresSoftware, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.name is not None:
            result['Name'] = self.name
        if self.only_display is not None:
            result['OnlyDisplay'] = self.only_display
        if self.start_tpe is not None:
            result['StartTpe'] = self.start_tpe
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OnlyDisplay') is not None:
            self.only_display = m.get('OnlyDisplay')
        if m.get('StartTpe') is not None:
            self.start_tpe = m.get('StartTpe')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeClusterV2ResponseBodyClusterInfoSoftwareInfoSoftwares(TeaModel):
    def __init__(self, software=None):
        self.software = software  # type: list[DescribeClusterV2ResponseBodyClusterInfoSoftwareInfoSoftwaresSoftware]

    def validate(self):
        if self.software:
            for k in self.software:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoSoftwareInfoSoftwares, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Software'] = []
        if self.software is not None:
            for k in self.software:
                result['Software'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.software = []
        if m.get('Software') is not None:
            for k in m.get('Software'):
                temp_model = DescribeClusterV2ResponseBodyClusterInfoSoftwareInfoSoftwaresSoftware()
                self.software.append(temp_model.from_map(k))
        return self


class DescribeClusterV2ResponseBodyClusterInfoSoftwareInfo(TeaModel):
    def __init__(self, cluster_type=None, emr_ver=None, softwares=None):
        self.cluster_type = cluster_type  # type: str
        self.emr_ver = emr_ver  # type: str
        self.softwares = softwares  # type: DescribeClusterV2ResponseBodyClusterInfoSoftwareInfoSoftwares

    def validate(self):
        if self.softwares:
            self.softwares.validate()

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfoSoftwareInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.emr_ver is not None:
            result['EmrVer'] = self.emr_ver
        if self.softwares is not None:
            result['Softwares'] = self.softwares.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('EmrVer') is not None:
            self.emr_ver = m.get('EmrVer')
        if m.get('Softwares') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoSoftwareInfoSoftwares()
            self.softwares = temp_model.from_map(m['Softwares'])
        return self


class DescribeClusterV2ResponseBodyClusterInfo(TeaModel):
    def __init__(self, access_info=None, auto_scaling_allowed=None, auto_scaling_by_load_allowed=None,
                 auto_scaling_enable=None, auto_scaling_spot_with_limit_allowed=None, auto_scaling_version=None,
                 auto_scaling_with_grace_allowed=None, bootstrap_action_list=None, bootstrap_failed=None, charge_type=None, configurations=None,
                 core_node_in_service=None, core_node_total=None, create_resource=None, create_type=None, deposit_type=None,
                 eas_enable=None, expired_time=None, extra_info=None, fail_reason=None, gateway_cluster_ids=None,
                 gateway_cluster_info_list=None, high_availability_enable=None, host_group_list=None, host_pool_info=None, id=None,
                 image_id=None, instance_generation=None, io_optimized=None, k_8s_cluster_id=None, local_meta_db=None,
                 log_enable=None, log_path=None, machine_type=None, master_node_in_service=None, master_node_total=None,
                 meta_store_type=None, name=None, net_type=None, period=None, region_id=None, relate_cluster_id=None,
                 relate_cluster_info=None, resize_disk_enable=None, running_time=None, security_group_id=None,
                 security_group_name=None, show_software_interface=None, software_info=None, start_time=None, status=None,
                 stop_time=None, task_node_in_service=None, task_node_total=None, user_defined_emr_ecs_role=None,
                 user_id=None, v_switch_id=None, vpc_id=None, zone_id=None):
        self.access_info = access_info  # type: DescribeClusterV2ResponseBodyClusterInfoAccessInfo
        self.auto_scaling_allowed = auto_scaling_allowed  # type: bool
        self.auto_scaling_by_load_allowed = auto_scaling_by_load_allowed  # type: bool
        self.auto_scaling_enable = auto_scaling_enable  # type: bool
        self.auto_scaling_spot_with_limit_allowed = auto_scaling_spot_with_limit_allowed  # type: bool
        self.auto_scaling_version = auto_scaling_version  # type: str
        self.auto_scaling_with_grace_allowed = auto_scaling_with_grace_allowed  # type: bool
        self.bootstrap_action_list = bootstrap_action_list  # type: DescribeClusterV2ResponseBodyClusterInfoBootstrapActionList
        self.bootstrap_failed = bootstrap_failed  # type: bool
        self.charge_type = charge_type  # type: str
        self.configurations = configurations  # type: str
        self.core_node_in_service = core_node_in_service  # type: int
        self.core_node_total = core_node_total  # type: int
        self.create_resource = create_resource  # type: str
        self.create_type = create_type  # type: str
        self.deposit_type = deposit_type  # type: str
        self.eas_enable = eas_enable  # type: bool
        self.expired_time = expired_time  # type: long
        self.extra_info = extra_info  # type: str
        self.fail_reason = fail_reason  # type: DescribeClusterV2ResponseBodyClusterInfoFailReason
        self.gateway_cluster_ids = gateway_cluster_ids  # type: str
        self.gateway_cluster_info_list = gateway_cluster_info_list  # type: DescribeClusterV2ResponseBodyClusterInfoGatewayClusterInfoList
        self.high_availability_enable = high_availability_enable  # type: bool
        self.host_group_list = host_group_list  # type: DescribeClusterV2ResponseBodyClusterInfoHostGroupList
        self.host_pool_info = host_pool_info  # type: DescribeClusterV2ResponseBodyClusterInfoHostPoolInfo
        self.id = id  # type: str
        self.image_id = image_id  # type: str
        self.instance_generation = instance_generation  # type: str
        self.io_optimized = io_optimized  # type: bool
        self.k_8s_cluster_id = k_8s_cluster_id  # type: str
        self.local_meta_db = local_meta_db  # type: bool
        self.log_enable = log_enable  # type: bool
        self.log_path = log_path  # type: str
        self.machine_type = machine_type  # type: str
        self.master_node_in_service = master_node_in_service  # type: int
        self.master_node_total = master_node_total  # type: int
        self.meta_store_type = meta_store_type  # type: str
        self.name = name  # type: str
        self.net_type = net_type  # type: str
        self.period = period  # type: int
        self.region_id = region_id  # type: str
        self.relate_cluster_id = relate_cluster_id  # type: str
        self.relate_cluster_info = relate_cluster_info  # type: DescribeClusterV2ResponseBodyClusterInfoRelateClusterInfo
        self.resize_disk_enable = resize_disk_enable  # type: bool
        self.running_time = running_time  # type: int
        self.security_group_id = security_group_id  # type: str
        self.security_group_name = security_group_name  # type: str
        self.show_software_interface = show_software_interface  # type: bool
        self.software_info = software_info  # type: DescribeClusterV2ResponseBodyClusterInfoSoftwareInfo
        self.start_time = start_time  # type: long
        self.status = status  # type: str
        self.stop_time = stop_time  # type: long
        self.task_node_in_service = task_node_in_service  # type: int
        self.task_node_total = task_node_total  # type: int
        self.user_defined_emr_ecs_role = user_defined_emr_ecs_role  # type: str
        self.user_id = user_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.access_info:
            self.access_info.validate()
        if self.bootstrap_action_list:
            self.bootstrap_action_list.validate()
        if self.fail_reason:
            self.fail_reason.validate()
        if self.gateway_cluster_info_list:
            self.gateway_cluster_info_list.validate()
        if self.host_group_list:
            self.host_group_list.validate()
        if self.host_pool_info:
            self.host_pool_info.validate()
        if self.relate_cluster_info:
            self.relate_cluster_info.validate()
        if self.software_info:
            self.software_info.validate()

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBodyClusterInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_info is not None:
            result['AccessInfo'] = self.access_info.to_map()
        if self.auto_scaling_allowed is not None:
            result['AutoScalingAllowed'] = self.auto_scaling_allowed
        if self.auto_scaling_by_load_allowed is not None:
            result['AutoScalingByLoadAllowed'] = self.auto_scaling_by_load_allowed
        if self.auto_scaling_enable is not None:
            result['AutoScalingEnable'] = self.auto_scaling_enable
        if self.auto_scaling_spot_with_limit_allowed is not None:
            result['AutoScalingSpotWithLimitAllowed'] = self.auto_scaling_spot_with_limit_allowed
        if self.auto_scaling_version is not None:
            result['AutoScalingVersion'] = self.auto_scaling_version
        if self.auto_scaling_with_grace_allowed is not None:
            result['AutoScalingWithGraceAllowed'] = self.auto_scaling_with_grace_allowed
        if self.bootstrap_action_list is not None:
            result['BootstrapActionList'] = self.bootstrap_action_list.to_map()
        if self.bootstrap_failed is not None:
            result['BootstrapFailed'] = self.bootstrap_failed
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.configurations is not None:
            result['Configurations'] = self.configurations
        if self.core_node_in_service is not None:
            result['CoreNodeInService'] = self.core_node_in_service
        if self.core_node_total is not None:
            result['CoreNodeTotal'] = self.core_node_total
        if self.create_resource is not None:
            result['CreateResource'] = self.create_resource
        if self.create_type is not None:
            result['CreateType'] = self.create_type
        if self.deposit_type is not None:
            result['DepositType'] = self.deposit_type
        if self.eas_enable is not None:
            result['EasEnable'] = self.eas_enable
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason.to_map()
        if self.gateway_cluster_ids is not None:
            result['GatewayClusterIds'] = self.gateway_cluster_ids
        if self.gateway_cluster_info_list is not None:
            result['GatewayClusterInfoList'] = self.gateway_cluster_info_list.to_map()
        if self.high_availability_enable is not None:
            result['HighAvailabilityEnable'] = self.high_availability_enable
        if self.host_group_list is not None:
            result['HostGroupList'] = self.host_group_list.to_map()
        if self.host_pool_info is not None:
            result['HostPoolInfo'] = self.host_pool_info.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_generation is not None:
            result['InstanceGeneration'] = self.instance_generation
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.local_meta_db is not None:
            result['LocalMetaDb'] = self.local_meta_db
        if self.log_enable is not None:
            result['LogEnable'] = self.log_enable
        if self.log_path is not None:
            result['LogPath'] = self.log_path
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        if self.master_node_in_service is not None:
            result['MasterNodeInService'] = self.master_node_in_service
        if self.master_node_total is not None:
            result['MasterNodeTotal'] = self.master_node_total
        if self.meta_store_type is not None:
            result['MetaStoreType'] = self.meta_store_type
        if self.name is not None:
            result['Name'] = self.name
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.relate_cluster_id is not None:
            result['RelateClusterId'] = self.relate_cluster_id
        if self.relate_cluster_info is not None:
            result['RelateClusterInfo'] = self.relate_cluster_info.to_map()
        if self.resize_disk_enable is not None:
            result['ResizeDiskEnable'] = self.resize_disk_enable
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.show_software_interface is not None:
            result['ShowSoftwareInterface'] = self.show_software_interface
        if self.software_info is not None:
            result['SoftwareInfo'] = self.software_info.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        if self.task_node_in_service is not None:
            result['TaskNodeInService'] = self.task_node_in_service
        if self.task_node_total is not None:
            result['TaskNodeTotal'] = self.task_node_total
        if self.user_defined_emr_ecs_role is not None:
            result['UserDefinedEmrEcsRole'] = self.user_defined_emr_ecs_role
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessInfo') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoAccessInfo()
            self.access_info = temp_model.from_map(m['AccessInfo'])
        if m.get('AutoScalingAllowed') is not None:
            self.auto_scaling_allowed = m.get('AutoScalingAllowed')
        if m.get('AutoScalingByLoadAllowed') is not None:
            self.auto_scaling_by_load_allowed = m.get('AutoScalingByLoadAllowed')
        if m.get('AutoScalingEnable') is not None:
            self.auto_scaling_enable = m.get('AutoScalingEnable')
        if m.get('AutoScalingSpotWithLimitAllowed') is not None:
            self.auto_scaling_spot_with_limit_allowed = m.get('AutoScalingSpotWithLimitAllowed')
        if m.get('AutoScalingVersion') is not None:
            self.auto_scaling_version = m.get('AutoScalingVersion')
        if m.get('AutoScalingWithGraceAllowed') is not None:
            self.auto_scaling_with_grace_allowed = m.get('AutoScalingWithGraceAllowed')
        if m.get('BootstrapActionList') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoBootstrapActionList()
            self.bootstrap_action_list = temp_model.from_map(m['BootstrapActionList'])
        if m.get('BootstrapFailed') is not None:
            self.bootstrap_failed = m.get('BootstrapFailed')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Configurations') is not None:
            self.configurations = m.get('Configurations')
        if m.get('CoreNodeInService') is not None:
            self.core_node_in_service = m.get('CoreNodeInService')
        if m.get('CoreNodeTotal') is not None:
            self.core_node_total = m.get('CoreNodeTotal')
        if m.get('CreateResource') is not None:
            self.create_resource = m.get('CreateResource')
        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')
        if m.get('DepositType') is not None:
            self.deposit_type = m.get('DepositType')
        if m.get('EasEnable') is not None:
            self.eas_enable = m.get('EasEnable')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('FailReason') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoFailReason()
            self.fail_reason = temp_model.from_map(m['FailReason'])
        if m.get('GatewayClusterIds') is not None:
            self.gateway_cluster_ids = m.get('GatewayClusterIds')
        if m.get('GatewayClusterInfoList') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoGatewayClusterInfoList()
            self.gateway_cluster_info_list = temp_model.from_map(m['GatewayClusterInfoList'])
        if m.get('HighAvailabilityEnable') is not None:
            self.high_availability_enable = m.get('HighAvailabilityEnable')
        if m.get('HostGroupList') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoHostGroupList()
            self.host_group_list = temp_model.from_map(m['HostGroupList'])
        if m.get('HostPoolInfo') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoHostPoolInfo()
            self.host_pool_info = temp_model.from_map(m['HostPoolInfo'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceGeneration') is not None:
            self.instance_generation = m.get('InstanceGeneration')
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('LocalMetaDb') is not None:
            self.local_meta_db = m.get('LocalMetaDb')
        if m.get('LogEnable') is not None:
            self.log_enable = m.get('LogEnable')
        if m.get('LogPath') is not None:
            self.log_path = m.get('LogPath')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('MasterNodeInService') is not None:
            self.master_node_in_service = m.get('MasterNodeInService')
        if m.get('MasterNodeTotal') is not None:
            self.master_node_total = m.get('MasterNodeTotal')
        if m.get('MetaStoreType') is not None:
            self.meta_store_type = m.get('MetaStoreType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RelateClusterId') is not None:
            self.relate_cluster_id = m.get('RelateClusterId')
        if m.get('RelateClusterInfo') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoRelateClusterInfo()
            self.relate_cluster_info = temp_model.from_map(m['RelateClusterInfo'])
        if m.get('ResizeDiskEnable') is not None:
            self.resize_disk_enable = m.get('ResizeDiskEnable')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('ShowSoftwareInterface') is not None:
            self.show_software_interface = m.get('ShowSoftwareInterface')
        if m.get('SoftwareInfo') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoSoftwareInfo()
            self.software_info = temp_model.from_map(m['SoftwareInfo'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        if m.get('TaskNodeInService') is not None:
            self.task_node_in_service = m.get('TaskNodeInService')
        if m.get('TaskNodeTotal') is not None:
            self.task_node_total = m.get('TaskNodeTotal')
        if m.get('UserDefinedEmrEcsRole') is not None:
            self.user_defined_emr_ecs_role = m.get('UserDefinedEmrEcsRole')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeClusterV2ResponseBody(TeaModel):
    def __init__(self, cluster_info=None, request_id=None):
        self.cluster_info = cluster_info  # type: DescribeClusterV2ResponseBodyClusterInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cluster_info:
            self.cluster_info.validate()

    def to_map(self):
        _map = super(DescribeClusterV2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterInfo') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfo()
            self.cluster_info = temp_model.from_map(m['ClusterInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterV2Response(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClusterV2ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterV2Response, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeClusterV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowRequest(TeaModel):
    def __init__(self, id=None, project_id=None, region_id=None):
        self.id = id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeFlowResponseBodyParentFlowListParentFlow(TeaModel):
    def __init__(self, parent_flow_id=None, parent_flow_name=None, project_id=None, project_name=None):
        self.parent_flow_id = parent_flow_id  # type: str
        self.parent_flow_name = parent_flow_name  # type: str
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowResponseBodyParentFlowListParentFlow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_flow_id is not None:
            result['ParentFlowId'] = self.parent_flow_id
        if self.parent_flow_name is not None:
            result['ParentFlowName'] = self.parent_flow_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParentFlowId') is not None:
            self.parent_flow_id = m.get('ParentFlowId')
        if m.get('ParentFlowName') is not None:
            self.parent_flow_name = m.get('ParentFlowName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DescribeFlowResponseBodyParentFlowList(TeaModel):
    def __init__(self, parent_flow=None):
        self.parent_flow = parent_flow  # type: list[DescribeFlowResponseBodyParentFlowListParentFlow]

    def validate(self):
        if self.parent_flow:
            for k in self.parent_flow:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFlowResponseBodyParentFlowList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ParentFlow'] = []
        if self.parent_flow is not None:
            for k in self.parent_flow:
                result['ParentFlow'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.parent_flow = []
        if m.get('ParentFlow') is not None:
            for k in m.get('ParentFlow'):
                temp_model = DescribeFlowResponseBodyParentFlowListParentFlow()
                self.parent_flow.append(temp_model.from_map(k))
        return self


class DescribeFlowResponseBody(TeaModel):
    def __init__(self, alert_conf=None, alert_ding_ding_group_biz_id=None, alert_user_group_biz_id=None,
                 application=None, category_id=None, cluster_id=None, create_cluster=None, cron_expr=None, description=None,
                 edit_lock_detail=None, end_schedule=None, gmt_create=None, gmt_modified=None, graph=None, host_name=None, id=None,
                 name=None, namespace=None, parent_flow_list=None, periodic=None, request_id=None, start_schedule=None,
                 status=None, type=None):
        self.alert_conf = alert_conf  # type: str
        self.alert_ding_ding_group_biz_id = alert_ding_ding_group_biz_id  # type: str
        self.alert_user_group_biz_id = alert_user_group_biz_id  # type: str
        self.application = application  # type: str
        self.category_id = category_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.create_cluster = create_cluster  # type: bool
        self.cron_expr = cron_expr  # type: str
        self.description = description  # type: str
        self.edit_lock_detail = edit_lock_detail  # type: str
        self.end_schedule = end_schedule  # type: long
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.graph = graph  # type: str
        self.host_name = host_name  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.namespace = namespace  # type: str
        self.parent_flow_list = parent_flow_list  # type: DescribeFlowResponseBodyParentFlowList
        self.periodic = periodic  # type: bool
        self.request_id = request_id  # type: str
        self.start_schedule = start_schedule  # type: long
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.parent_flow_list:
            self.parent_flow_list.validate()

    def to_map(self):
        _map = super(DescribeFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.alert_ding_ding_group_biz_id is not None:
            result['AlertDingDingGroupBizId'] = self.alert_ding_ding_group_biz_id
        if self.alert_user_group_biz_id is not None:
            result['AlertUserGroupBizId'] = self.alert_user_group_biz_id
        if self.application is not None:
            result['Application'] = self.application
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_cluster is not None:
            result['CreateCluster'] = self.create_cluster
        if self.cron_expr is not None:
            result['CronExpr'] = self.cron_expr
        if self.description is not None:
            result['Description'] = self.description
        if self.edit_lock_detail is not None:
            result['EditLockDetail'] = self.edit_lock_detail
        if self.end_schedule is not None:
            result['EndSchedule'] = self.end_schedule
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.graph is not None:
            result['Graph'] = self.graph
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.parent_flow_list is not None:
            result['ParentFlowList'] = self.parent_flow_list.to_map()
        if self.periodic is not None:
            result['Periodic'] = self.periodic
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_schedule is not None:
            result['StartSchedule'] = self.start_schedule
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('AlertDingDingGroupBizId') is not None:
            self.alert_ding_ding_group_biz_id = m.get('AlertDingDingGroupBizId')
        if m.get('AlertUserGroupBizId') is not None:
            self.alert_user_group_biz_id = m.get('AlertUserGroupBizId')
        if m.get('Application') is not None:
            self.application = m.get('Application')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateCluster') is not None:
            self.create_cluster = m.get('CreateCluster')
        if m.get('CronExpr') is not None:
            self.cron_expr = m.get('CronExpr')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EditLockDetail') is not None:
            self.edit_lock_detail = m.get('EditLockDetail')
        if m.get('EndSchedule') is not None:
            self.end_schedule = m.get('EndSchedule')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Graph') is not None:
            self.graph = m.get('Graph')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ParentFlowList') is not None:
            temp_model = DescribeFlowResponseBodyParentFlowList()
            self.parent_flow_list = temp_model.from_map(m['ParentFlowList'])
        if m.get('Periodic') is not None:
            self.periodic = m.get('Periodic')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartSchedule') is not None:
            self.start_schedule = m.get('StartSchedule')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowCategoryTreeRequest(TeaModel):
    def __init__(self, category_id=None, keyword=None, mode=None, project_id=None, region_id=None, type=None):
        self.category_id = category_id  # type: str
        self.keyword = keyword  # type: str
        self.mode = mode  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowCategoryTreeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeFlowCategoryTreeResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowCategoryTreeResponseBody, self).to_map()
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


class DescribeFlowCategoryTreeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeFlowCategoryTreeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFlowCategoryTreeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFlowCategoryTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowInstanceRequest(TeaModel):
    def __init__(self, id=None, project_id=None, region_id=None):
        self.id = id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeFlowInstanceResponseBodyDependencyFlowListParentFlow(TeaModel):
    def __init__(self, biz_date=None, dependency_flow_id=None, dependency_instance_id=None, flow_id=None,
                 flow_instance_id=None, meet=None, project_id=None, schedule_key=None):
        self.biz_date = biz_date  # type: long
        self.dependency_flow_id = dependency_flow_id  # type: str
        self.dependency_instance_id = dependency_instance_id  # type: str
        self.flow_id = flow_id  # type: str
        self.flow_instance_id = flow_instance_id  # type: str
        self.meet = meet  # type: bool
        self.project_id = project_id  # type: str
        self.schedule_key = schedule_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowInstanceResponseBodyDependencyFlowListParentFlow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.dependency_flow_id is not None:
            result['DependencyFlowId'] = self.dependency_flow_id
        if self.dependency_instance_id is not None:
            result['DependencyInstanceId'] = self.dependency_instance_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        if self.meet is not None:
            result['Meet'] = self.meet
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.schedule_key is not None:
            result['ScheduleKey'] = self.schedule_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('DependencyFlowId') is not None:
            self.dependency_flow_id = m.get('DependencyFlowId')
        if m.get('DependencyInstanceId') is not None:
            self.dependency_instance_id = m.get('DependencyInstanceId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        if m.get('Meet') is not None:
            self.meet = m.get('Meet')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ScheduleKey') is not None:
            self.schedule_key = m.get('ScheduleKey')
        return self


class DescribeFlowInstanceResponseBodyDependencyFlowList(TeaModel):
    def __init__(self, parent_flow=None):
        self.parent_flow = parent_flow  # type: list[DescribeFlowInstanceResponseBodyDependencyFlowListParentFlow]

    def validate(self):
        if self.parent_flow:
            for k in self.parent_flow:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFlowInstanceResponseBodyDependencyFlowList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ParentFlow'] = []
        if self.parent_flow is not None:
            for k in self.parent_flow:
                result['ParentFlow'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.parent_flow = []
        if m.get('ParentFlow') is not None:
            for k in m.get('ParentFlow'):
                temp_model = DescribeFlowInstanceResponseBodyDependencyFlowListParentFlow()
                self.parent_flow.append(temp_model.from_map(k))
        return self


class DescribeFlowInstanceResponseBodyNodeInstanceNodeInstance(TeaModel):
    def __init__(self, cluster_id=None, duration=None, end_time=None, external_id=None, external_info=None,
                 external_status=None, fail_act=None, gmt_create=None, gmt_modified=None, host_name=None, id=None, job_id=None,
                 job_name=None, job_type=None, max_retry=None, node_name=None, pending=None, project_id=None, retries=None,
                 retry_interval=None, start_time=None, status=None, type=None):
        self.cluster_id = cluster_id  # type: str
        self.duration = duration  # type: long
        self.end_time = end_time  # type: long
        self.external_id = external_id  # type: str
        self.external_info = external_info  # type: str
        self.external_status = external_status  # type: str
        self.fail_act = fail_act  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.host_name = host_name  # type: str
        self.id = id  # type: str
        self.job_id = job_id  # type: str
        self.job_name = job_name  # type: str
        self.job_type = job_type  # type: str
        self.max_retry = max_retry  # type: str
        self.node_name = node_name  # type: str
        self.pending = pending  # type: bool
        self.project_id = project_id  # type: str
        self.retries = retries  # type: int
        self.retry_interval = retry_interval  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowInstanceResponseBodyNodeInstanceNodeInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.external_info is not None:
            result['ExternalInfo'] = self.external_info
        if self.external_status is not None:
            result['ExternalStatus'] = self.external_status
        if self.fail_act is not None:
            result['FailAct'] = self.fail_act
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.max_retry is not None:
            result['MaxRetry'] = self.max_retry
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.pending is not None:
            result['Pending'] = self.pending
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.retries is not None:
            result['Retries'] = self.retries
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('ExternalInfo') is not None:
            self.external_info = m.get('ExternalInfo')
        if m.get('ExternalStatus') is not None:
            self.external_status = m.get('ExternalStatus')
        if m.get('FailAct') is not None:
            self.fail_act = m.get('FailAct')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MaxRetry') is not None:
            self.max_retry = m.get('MaxRetry')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('Pending') is not None:
            self.pending = m.get('Pending')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Retries') is not None:
            self.retries = m.get('Retries')
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeFlowInstanceResponseBodyNodeInstance(TeaModel):
    def __init__(self, node_instance=None):
        self.node_instance = node_instance  # type: list[DescribeFlowInstanceResponseBodyNodeInstanceNodeInstance]

    def validate(self):
        if self.node_instance:
            for k in self.node_instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFlowInstanceResponseBodyNodeInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeInstance'] = []
        if self.node_instance is not None:
            for k in self.node_instance:
                result['NodeInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.node_instance = []
        if m.get('NodeInstance') is not None:
            for k in m.get('NodeInstance'):
                temp_model = DescribeFlowInstanceResponseBodyNodeInstanceNodeInstance()
                self.node_instance.append(temp_model.from_map(k))
        return self


class DescribeFlowInstanceResponseBody(TeaModel):
    def __init__(self, cluster_id=None, cron_expression=None, dependency_flow_list=None, duration=None,
                 end_time=None, flow_id=None, flow_name=None, gmt_create=None, gmt_modified=None, graph=None,
                 has_node_failed=None, id=None, namespace=None, node_instance=None, project_id=None, request_id=None,
                 schedule_time=None, start_time=None, status=None):
        self.cluster_id = cluster_id  # type: str
        self.cron_expression = cron_expression  # type: str
        self.dependency_flow_list = dependency_flow_list  # type: DescribeFlowInstanceResponseBodyDependencyFlowList
        self.duration = duration  # type: long
        self.end_time = end_time  # type: long
        self.flow_id = flow_id  # type: str
        self.flow_name = flow_name  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.graph = graph  # type: str
        self.has_node_failed = has_node_failed  # type: bool
        self.id = id  # type: str
        self.namespace = namespace  # type: str
        self.node_instance = node_instance  # type: DescribeFlowInstanceResponseBodyNodeInstance
        self.project_id = project_id  # type: str
        self.request_id = request_id  # type: str
        self.schedule_time = schedule_time  # type: long
        self.start_time = start_time  # type: long
        self.status = status  # type: str

    def validate(self):
        if self.dependency_flow_list:
            self.dependency_flow_list.validate()
        if self.node_instance:
            self.node_instance.validate()

    def to_map(self):
        _map = super(DescribeFlowInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.dependency_flow_list is not None:
            result['DependencyFlowList'] = self.dependency_flow_list.to_map()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.graph is not None:
            result['Graph'] = self.graph
        if self.has_node_failed is not None:
            result['HasNodeFailed'] = self.has_node_failed
        if self.id is not None:
            result['Id'] = self.id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.node_instance is not None:
            result['NodeInstance'] = self.node_instance.to_map()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('DependencyFlowList') is not None:
            temp_model = DescribeFlowInstanceResponseBodyDependencyFlowList()
            self.dependency_flow_list = temp_model.from_map(m['DependencyFlowList'])
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Graph') is not None:
            self.graph = m.get('Graph')
        if m.get('HasNodeFailed') is not None:
            self.has_node_failed = m.get('HasNodeFailed')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NodeInstance') is not None:
            temp_model = DescribeFlowInstanceResponseBodyNodeInstance()
            self.node_instance = temp_model.from_map(m['NodeInstance'])
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeFlowInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeFlowInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFlowInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFlowInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowJobRequest(TeaModel):
    def __init__(self, id=None, project_id=None, region_id=None):
        self.id = id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeFlowJobResponseBodyResourceListResource(TeaModel):
    def __init__(self, alias=None, path=None):
        self.alias = alias  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowJobResponseBodyResourceListResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeFlowJobResponseBodyResourceList(TeaModel):
    def __init__(self, resource=None):
        self.resource = resource  # type: list[DescribeFlowJobResponseBodyResourceListResource]

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFlowJobResponseBodyResourceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = DescribeFlowJobResponseBodyResourceListResource()
                self.resource.append(temp_model.from_map(k))
        return self


class DescribeFlowJobResponseBody(TeaModel):
    def __init__(self, adhoc=None, alert_conf=None, category_id=None, custom_variables=None, description=None,
                 edit_lock_detail=None, env_conf=None, fail_act=None, gmt_create=None, gmt_modified=None, id=None, knox_password=None,
                 knox_user=None, last_instance_id=None, max_retry=None, max_running_time_sec=None, mode=None,
                 monitor_conf=None, name=None, param_conf=None, params=None, request_id=None, resource_list=None,
                 retry_interval=None, retry_policy=None, run_conf=None, type=None):
        self.adhoc = adhoc  # type: str
        self.alert_conf = alert_conf  # type: str
        self.category_id = category_id  # type: str
        self.custom_variables = custom_variables  # type: str
        self.description = description  # type: str
        self.edit_lock_detail = edit_lock_detail  # type: str
        self.env_conf = env_conf  # type: str
        self.fail_act = fail_act  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.id = id  # type: str
        self.knox_password = knox_password  # type: str
        self.knox_user = knox_user  # type: str
        self.last_instance_id = last_instance_id  # type: str
        self.max_retry = max_retry  # type: int
        self.max_running_time_sec = max_running_time_sec  # type: long
        self.mode = mode  # type: str
        self.monitor_conf = monitor_conf  # type: str
        self.name = name  # type: str
        self.param_conf = param_conf  # type: str
        self.params = params  # type: str
        self.request_id = request_id  # type: str
        self.resource_list = resource_list  # type: DescribeFlowJobResponseBodyResourceList
        self.retry_interval = retry_interval  # type: long
        self.retry_policy = retry_policy  # type: str
        self.run_conf = run_conf  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.resource_list:
            self.resource_list.validate()

    def to_map(self):
        _map = super(DescribeFlowJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adhoc is not None:
            result['Adhoc'] = self.adhoc
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.custom_variables is not None:
            result['CustomVariables'] = self.custom_variables
        if self.description is not None:
            result['Description'] = self.description
        if self.edit_lock_detail is not None:
            result['EditLockDetail'] = self.edit_lock_detail
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        if self.fail_act is not None:
            result['FailAct'] = self.fail_act
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.knox_password is not None:
            result['KnoxPassword'] = self.knox_password
        if self.knox_user is not None:
            result['KnoxUser'] = self.knox_user
        if self.last_instance_id is not None:
            result['LastInstanceId'] = self.last_instance_id
        if self.max_retry is not None:
            result['MaxRetry'] = self.max_retry
        if self.max_running_time_sec is not None:
            result['MaxRunningTimeSec'] = self.max_running_time_sec
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.monitor_conf is not None:
            result['MonitorConf'] = self.monitor_conf
        if self.name is not None:
            result['Name'] = self.name
        if self.param_conf is not None:
            result['ParamConf'] = self.param_conf
        if self.params is not None:
            result['Params'] = self.params
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_list is not None:
            result['ResourceList'] = self.resource_list.to_map()
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.retry_policy is not None:
            result['RetryPolicy'] = self.retry_policy
        if self.run_conf is not None:
            result['RunConf'] = self.run_conf
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Adhoc') is not None:
            self.adhoc = m.get('Adhoc')
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CustomVariables') is not None:
            self.custom_variables = m.get('CustomVariables')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EditLockDetail') is not None:
            self.edit_lock_detail = m.get('EditLockDetail')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        if m.get('FailAct') is not None:
            self.fail_act = m.get('FailAct')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KnoxPassword') is not None:
            self.knox_password = m.get('KnoxPassword')
        if m.get('KnoxUser') is not None:
            self.knox_user = m.get('KnoxUser')
        if m.get('LastInstanceId') is not None:
            self.last_instance_id = m.get('LastInstanceId')
        if m.get('MaxRetry') is not None:
            self.max_retry = m.get('MaxRetry')
        if m.get('MaxRunningTimeSec') is not None:
            self.max_running_time_sec = m.get('MaxRunningTimeSec')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('MonitorConf') is not None:
            self.monitor_conf = m.get('MonitorConf')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamConf') is not None:
            self.param_conf = m.get('ParamConf')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceList') is not None:
            temp_model = DescribeFlowJobResponseBodyResourceList()
            self.resource_list = temp_model.from_map(m['ResourceList'])
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('RetryPolicy') is not None:
            self.retry_policy = m.get('RetryPolicy')
        if m.get('RunConf') is not None:
            self.run_conf = m.get('RunConf')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeFlowJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeFlowJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFlowJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFlowJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowNodeInstanceRequest(TeaModel):
    def __init__(self, id=None, project_id=None, region_id=None):
        self.id = id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowNodeInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeFlowNodeInstanceResponseBody(TeaModel):
    def __init__(self, adhoc=None, cluster_id=None, cluster_name=None, duration=None, end_time=None, env_conf=None,
                 external_child_ids=None, external_id=None, external_info=None, external_status=None, external_sub_id=None,
                 fail_act=None, flow_id=None, flow_instance_id=None, gmt_create=None, gmt_modified=None, host_name=None,
                 id=None, job_id=None, job_name=None, job_params=None, job_type=None, max_retry=None, mode=None,
                 monitor_conf=None, node_name=None, param_conf=None, pending=None, project_id=None, request_id=None, retries=None,
                 retry_interval=None, retry_policy=None, run_conf=None, start_time=None, status=None, type=None):
        self.adhoc = adhoc  # type: bool
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.duration = duration  # type: long
        self.end_time = end_time  # type: long
        self.env_conf = env_conf  # type: str
        self.external_child_ids = external_child_ids  # type: str
        self.external_id = external_id  # type: str
        self.external_info = external_info  # type: str
        self.external_status = external_status  # type: str
        self.external_sub_id = external_sub_id  # type: str
        self.fail_act = fail_act  # type: str
        self.flow_id = flow_id  # type: str
        self.flow_instance_id = flow_instance_id  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.host_name = host_name  # type: str
        self.id = id  # type: str
        self.job_id = job_id  # type: str
        self.job_name = job_name  # type: str
        self.job_params = job_params  # type: str
        self.job_type = job_type  # type: str
        self.max_retry = max_retry  # type: str
        self.mode = mode  # type: str
        self.monitor_conf = monitor_conf  # type: str
        self.node_name = node_name  # type: str
        self.param_conf = param_conf  # type: str
        self.pending = pending  # type: bool
        self.project_id = project_id  # type: str
        self.request_id = request_id  # type: str
        self.retries = retries  # type: int
        self.retry_interval = retry_interval  # type: str
        self.retry_policy = retry_policy  # type: str
        self.run_conf = run_conf  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowNodeInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adhoc is not None:
            result['Adhoc'] = self.adhoc
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        if self.external_child_ids is not None:
            result['ExternalChildIds'] = self.external_child_ids
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.external_info is not None:
            result['ExternalInfo'] = self.external_info
        if self.external_status is not None:
            result['ExternalStatus'] = self.external_status
        if self.external_sub_id is not None:
            result['ExternalSubId'] = self.external_sub_id
        if self.fail_act is not None:
            result['FailAct'] = self.fail_act
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_params is not None:
            result['JobParams'] = self.job_params
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.max_retry is not None:
            result['MaxRetry'] = self.max_retry
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.monitor_conf is not None:
            result['MonitorConf'] = self.monitor_conf
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.param_conf is not None:
            result['ParamConf'] = self.param_conf
        if self.pending is not None:
            result['Pending'] = self.pending
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.retries is not None:
            result['Retries'] = self.retries
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.retry_policy is not None:
            result['RetryPolicy'] = self.retry_policy
        if self.run_conf is not None:
            result['RunConf'] = self.run_conf
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Adhoc') is not None:
            self.adhoc = m.get('Adhoc')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        if m.get('ExternalChildIds') is not None:
            self.external_child_ids = m.get('ExternalChildIds')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('ExternalInfo') is not None:
            self.external_info = m.get('ExternalInfo')
        if m.get('ExternalStatus') is not None:
            self.external_status = m.get('ExternalStatus')
        if m.get('ExternalSubId') is not None:
            self.external_sub_id = m.get('ExternalSubId')
        if m.get('FailAct') is not None:
            self.fail_act = m.get('FailAct')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobParams') is not None:
            self.job_params = m.get('JobParams')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MaxRetry') is not None:
            self.max_retry = m.get('MaxRetry')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('MonitorConf') is not None:
            self.monitor_conf = m.get('MonitorConf')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('ParamConf') is not None:
            self.param_conf = m.get('ParamConf')
        if m.get('Pending') is not None:
            self.pending = m.get('Pending')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Retries') is not None:
            self.retries = m.get('Retries')
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('RetryPolicy') is not None:
            self.retry_policy = m.get('RetryPolicy')
        if m.get('RunConf') is not None:
            self.run_conf = m.get('RunConf')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeFlowNodeInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeFlowNodeInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFlowNodeInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFlowNodeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowNodeInstanceContainerLogRequest(TeaModel):
    def __init__(self, app_id=None, container_id=None, length=None, log_name=None, node_instance_id=None,
                 offset=None, project_id=None, region_id=None):
        self.app_id = app_id  # type: str
        self.container_id = container_id  # type: str
        self.length = length  # type: int
        self.log_name = log_name  # type: str
        self.node_instance_id = node_instance_id  # type: str
        self.offset = offset  # type: int
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowNodeInstanceContainerLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        if self.length is not None:
            result['Length'] = self.length
        if self.log_name is not None:
            result['LogName'] = self.log_name
        if self.node_instance_id is not None:
            result['NodeInstanceId'] = self.node_instance_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')
        if m.get('NodeInstanceId') is not None:
            self.node_instance_id = m.get('NodeInstanceId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeFlowNodeInstanceContainerLogResponseBodyLogEntrysLogEntry(TeaModel):
    def __init__(self, content=None):
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowNodeInstanceContainerLogResponseBodyLogEntrysLogEntry, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeFlowNodeInstanceContainerLogResponseBodyLogEntrys(TeaModel):
    def __init__(self, log_entry=None):
        self.log_entry = log_entry  # type: list[DescribeFlowNodeInstanceContainerLogResponseBodyLogEntrysLogEntry]

    def validate(self):
        if self.log_entry:
            for k in self.log_entry:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFlowNodeInstanceContainerLogResponseBodyLogEntrys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogEntry'] = []
        if self.log_entry is not None:
            for k in self.log_entry:
                result['LogEntry'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_entry = []
        if m.get('LogEntry') is not None:
            for k in m.get('LogEntry'):
                temp_model = DescribeFlowNodeInstanceContainerLogResponseBodyLogEntrysLogEntry()
                self.log_entry.append(temp_model.from_map(k))
        return self


class DescribeFlowNodeInstanceContainerLogResponseBody(TeaModel):
    def __init__(self, log_end=None, log_entrys=None, request_id=None):
        self.log_end = log_end  # type: bool
        self.log_entrys = log_entrys  # type: DescribeFlowNodeInstanceContainerLogResponseBodyLogEntrys
        self.request_id = request_id  # type: str

    def validate(self):
        if self.log_entrys:
            self.log_entrys.validate()

    def to_map(self):
        _map = super(DescribeFlowNodeInstanceContainerLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_end is not None:
            result['LogEnd'] = self.log_end
        if self.log_entrys is not None:
            result['LogEntrys'] = self.log_entrys.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogEnd') is not None:
            self.log_end = m.get('LogEnd')
        if m.get('LogEntrys') is not None:
            temp_model = DescribeFlowNodeInstanceContainerLogResponseBodyLogEntrys()
            self.log_entrys = temp_model.from_map(m['LogEntrys'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFlowNodeInstanceContainerLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeFlowNodeInstanceContainerLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFlowNodeInstanceContainerLogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFlowNodeInstanceContainerLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowNodeInstanceLauncherLogRequest(TeaModel):
    def __init__(self, end_time=None, length=None, lines=None, node_instance_id=None, offset=None, project_id=None,
                 region_id=None, reverse=None, start=None, start_time=None):
        self.end_time = end_time  # type: long
        self.length = length  # type: int
        self.lines = lines  # type: int
        self.node_instance_id = node_instance_id  # type: str
        self.offset = offset  # type: int
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.reverse = reverse  # type: bool
        self.start = start  # type: int
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowNodeInstanceLauncherLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.length is not None:
            result['Length'] = self.length
        if self.lines is not None:
            result['Lines'] = self.lines
        if self.node_instance_id is not None:
            result['NodeInstanceId'] = self.node_instance_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.start is not None:
            result['Start'] = self.start
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('Lines') is not None:
            self.lines = m.get('Lines')
        if m.get('NodeInstanceId') is not None:
            self.node_instance_id = m.get('NodeInstanceId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeFlowNodeInstanceLauncherLogResponseBodyLogEntrysLogEntry(TeaModel):
    def __init__(self, content=None):
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowNodeInstanceLauncherLogResponseBodyLogEntrysLogEntry, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeFlowNodeInstanceLauncherLogResponseBodyLogEntrys(TeaModel):
    def __init__(self, log_entry=None):
        self.log_entry = log_entry  # type: list[DescribeFlowNodeInstanceLauncherLogResponseBodyLogEntrysLogEntry]

    def validate(self):
        if self.log_entry:
            for k in self.log_entry:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeFlowNodeInstanceLauncherLogResponseBodyLogEntrys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogEntry'] = []
        if self.log_entry is not None:
            for k in self.log_entry:
                result['LogEntry'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_entry = []
        if m.get('LogEntry') is not None:
            for k in m.get('LogEntry'):
                temp_model = DescribeFlowNodeInstanceLauncherLogResponseBodyLogEntrysLogEntry()
                self.log_entry.append(temp_model.from_map(k))
        return self


class DescribeFlowNodeInstanceLauncherLogResponseBody(TeaModel):
    def __init__(self, log_end=None, log_entrys=None, request_id=None):
        self.log_end = log_end  # type: bool
        self.log_entrys = log_entrys  # type: DescribeFlowNodeInstanceLauncherLogResponseBodyLogEntrys
        self.request_id = request_id  # type: str

    def validate(self):
        if self.log_entrys:
            self.log_entrys.validate()

    def to_map(self):
        _map = super(DescribeFlowNodeInstanceLauncherLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_end is not None:
            result['LogEnd'] = self.log_end
        if self.log_entrys is not None:
            result['LogEntrys'] = self.log_entrys.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogEnd') is not None:
            self.log_end = m.get('LogEnd')
        if m.get('LogEntrys') is not None:
            temp_model = DescribeFlowNodeInstanceLauncherLogResponseBodyLogEntrys()
            self.log_entrys = temp_model.from_map(m['LogEntrys'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFlowNodeInstanceLauncherLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeFlowNodeInstanceLauncherLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFlowNodeInstanceLauncherLogResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFlowNodeInstanceLauncherLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowProjectRequest(TeaModel):
    def __init__(self, project_id=None, region_id=None):
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeFlowProjectResponseBody(TeaModel):
    def __init__(self, description=None, gmt_create=None, gmt_modified=None, id=None, name=None, request_id=None,
                 user_id=None):
        self.description = description  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.id = id  # type: str
        self.name = name  # type: str
        self.request_id = request_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFlowProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeFlowProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFlowProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFlowProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowProjectClusterSettingRequest(TeaModel):
    def __init__(self, cluster_id=None, project_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowProjectClusterSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeFlowProjectClusterSettingResponseBodyHostList(TeaModel):
    def __init__(self, host=None):
        self.host = host  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowProjectClusterSettingResponseBodyHostList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        return self


class DescribeFlowProjectClusterSettingResponseBodyQueueList(TeaModel):
    def __init__(self, queue=None):
        self.queue = queue  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowProjectClusterSettingResponseBodyQueueList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue is not None:
            result['Queue'] = self.queue
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        return self


class DescribeFlowProjectClusterSettingResponseBodyUserList(TeaModel):
    def __init__(self, user=None):
        self.user = user  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowProjectClusterSettingResponseBodyUserList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DescribeFlowProjectClusterSettingResponseBody(TeaModel):
    def __init__(self, cluster_id=None, default_queue=None, default_user=None, gmt_create=None, gmt_modified=None,
                 host_list=None, k_8s_cluster_id=None, project_id=None, queue_list=None, request_id=None, user_list=None):
        self.cluster_id = cluster_id  # type: str
        self.default_queue = default_queue  # type: str
        self.default_user = default_user  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.host_list = host_list  # type: DescribeFlowProjectClusterSettingResponseBodyHostList
        self.k_8s_cluster_id = k_8s_cluster_id  # type: str
        self.project_id = project_id  # type: str
        self.queue_list = queue_list  # type: DescribeFlowProjectClusterSettingResponseBodyQueueList
        self.request_id = request_id  # type: str
        self.user_list = user_list  # type: DescribeFlowProjectClusterSettingResponseBodyUserList

    def validate(self):
        if self.host_list:
            self.host_list.validate()
        if self.queue_list:
            self.queue_list.validate()
        if self.user_list:
            self.user_list.validate()

    def to_map(self):
        _map = super(DescribeFlowProjectClusterSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.default_queue is not None:
            result['DefaultQueue'] = self.default_queue
        if self.default_user is not None:
            result['DefaultUser'] = self.default_user
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.host_list is not None:
            result['HostList'] = self.host_list.to_map()
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.queue_list is not None:
            result['QueueList'] = self.queue_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_list is not None:
            result['UserList'] = self.user_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DefaultQueue') is not None:
            self.default_queue = m.get('DefaultQueue')
        if m.get('DefaultUser') is not None:
            self.default_user = m.get('DefaultUser')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HostList') is not None:
            temp_model = DescribeFlowProjectClusterSettingResponseBodyHostList()
            self.host_list = temp_model.from_map(m['HostList'])
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('QueueList') is not None:
            temp_model = DescribeFlowProjectClusterSettingResponseBodyQueueList()
            self.queue_list = temp_model.from_map(m['QueueList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserList') is not None:
            temp_model = DescribeFlowProjectClusterSettingResponseBodyUserList()
            self.user_list = temp_model.from_map(m['UserList'])
        return self


class DescribeFlowProjectClusterSettingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeFlowProjectClusterSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFlowProjectClusterSettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFlowProjectClusterSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowSLARequest(TeaModel):
    def __init__(self, from_=None, metrics=None, period_type=None, project_id=None, region_id=None,
                 resource_group_id=None, resource_owner_id=None, to=None, type=None):
        self.from_ = from_  # type: long
        self.metrics = metrics  # type: str
        self.period_type = period_type  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.to = to  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowSLARequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.period_type is not None:
            result['PeriodType'] = self.period_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.to is not None:
            result['To'] = self.to
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeFlowSLAResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowSLAResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeFlowSLAResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeFlowSLAResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFlowSLAResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFlowSLAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowVariableCollectionRequest(TeaModel):
    def __init__(self, entity_id=None, region_id=None, resource_group_id=None):
        self.entity_id = entity_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowVariableCollectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeFlowVariableCollectionResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeFlowVariableCollectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeFlowVariableCollectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeFlowVariableCollectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeFlowVariableCollectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFlowVariableCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowAuditLogsRequest(TeaModel):
    def __init__(self, current_size=None, entity_group_id=None, entity_id=None, entity_type=None, limit=None,
                 operation=None, operator_id=None, order_field=None, order_mode=None, page_count=None, page_number=None,
                 page_size=None, region_id=None, resource_owner_id=None, status=None):
        self.current_size = current_size  # type: int
        self.entity_group_id = entity_group_id  # type: str
        self.entity_id = entity_id  # type: str
        self.entity_type = entity_type  # type: str
        self.limit = limit  # type: int
        self.operation = operation  # type: str
        self.operator_id = operator_id  # type: str
        self.order_field = order_field  # type: str
        self.order_mode = order_mode  # type: str
        self.page_count = page_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFlowAuditLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_size is not None:
            result['CurrentSize'] = self.current_size
        if self.entity_group_id is not None:
            result['EntityGroupId'] = self.entity_group_id
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.order_mode is not None:
            result['OrderMode'] = self.order_mode
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentSize') is not None:
            self.current_size = m.get('CurrentSize')
        if m.get('EntityGroupId') is not None:
            self.entity_group_id = m.get('EntityGroupId')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('OrderMode') is not None:
            self.order_mode = m.get('OrderMode')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetFlowAuditLogsResponseBodyItemsItem(TeaModel):
    def __init__(self, content=None, entity_group_id=None, entity_id=None, entity_type=None, operation=None,
                 operator_id=None, status=None, ts=None, user_id=None):
        self.content = content  # type: str
        self.entity_group_id = entity_group_id  # type: str
        self.entity_id = entity_id  # type: str
        self.entity_type = entity_type  # type: str
        self.operation = operation  # type: str
        self.operator_id = operator_id  # type: str
        self.status = status  # type: str
        self.ts = ts  # type: long
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFlowAuditLogsResponseBodyItemsItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.entity_group_id is not None:
            result['EntityGroupId'] = self.entity_group_id
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.status is not None:
            result['Status'] = self.status
        if self.ts is not None:
            result['Ts'] = self.ts
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EntityGroupId') is not None:
            self.entity_group_id = m.get('EntityGroupId')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Ts') is not None:
            self.ts = m.get('Ts')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetFlowAuditLogsResponseBodyItems(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[GetFlowAuditLogsResponseBodyItemsItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFlowAuditLogsResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = GetFlowAuditLogsResponseBodyItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class GetFlowAuditLogsResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.items = items  # type: GetFlowAuditLogsResponseBodyItems
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(GetFlowAuditLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
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
        if m.get('Items') is not None:
            temp_model = GetFlowAuditLogsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetFlowAuditLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetFlowAuditLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFlowAuditLogsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetFlowAuditLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KillFlowRequest(TeaModel):
    def __init__(self, flow_instance_id=None, project_id=None, region_id=None):
        self.flow_instance_id = flow_instance_id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(KillFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class KillFlowResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(KillFlowResponseBody, self).to_map()
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


class KillFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: KillFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(KillFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = KillFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KillFlowJobRequest(TeaModel):
    def __init__(self, job_instance_id=None, project_id=None, region_id=None):
        self.job_instance_id = job_instance_id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(KillFlowJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_instance_id is not None:
            result['JobInstanceId'] = self.job_instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobInstanceId') is not None:
            self.job_instance_id = m.get('JobInstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class KillFlowJobResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(KillFlowJobResponseBody, self).to_map()
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


class KillFlowJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: KillFlowJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(KillFlowJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = KillFlowJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersRequestTag, self).to_map()
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


class ListClustersRequest(TeaModel):
    def __init__(self, cluster_type_list=None, create_type=None, default_status=None, deposit_type=None,
                 expired_tag_list=None, is_desc=None, machine_type=None, name=None, page_number=None, page_size=None, region_id=None,
                 resource_group_id=None, resource_owner_id=None, status_list=None, tag=None):
        self.cluster_type_list = cluster_type_list  # type: list[str]
        self.create_type = create_type  # type: str
        self.default_status = default_status  # type: bool
        self.deposit_type = deposit_type  # type: str
        self.expired_tag_list = expired_tag_list  # type: list[str]
        self.is_desc = is_desc  # type: bool
        self.machine_type = machine_type  # type: str
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.status_list = status_list  # type: list[str]
        self.tag = tag  # type: list[ListClustersRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type_list is not None:
            result['ClusterTypeList'] = self.cluster_type_list
        if self.create_type is not None:
            result['CreateType'] = self.create_type
        if self.default_status is not None:
            result['DefaultStatus'] = self.default_status
        if self.deposit_type is not None:
            result['DepositType'] = self.deposit_type
        if self.expired_tag_list is not None:
            result['ExpiredTagList'] = self.expired_tag_list
        if self.is_desc is not None:
            result['IsDesc'] = self.is_desc
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterTypeList') is not None:
            self.cluster_type_list = m.get('ClusterTypeList')
        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')
        if m.get('DefaultStatus') is not None:
            self.default_status = m.get('DefaultStatus')
        if m.get('DepositType') is not None:
            self.deposit_type = m.get('DepositType')
        if m.get('ExpiredTagList') is not None:
            self.expired_tag_list = m.get('ExpiredTagList')
        if m.get('IsDesc') is not None:
            self.is_desc = m.get('IsDesc')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListClustersRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListClustersResponseBodyClustersClusterInfoFailReason(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersResponseBodyClustersClusterInfoFailReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListClustersResponseBodyClustersClusterInfoOrderTaskInfo(TeaModel):
    def __init__(self, current_count=None, order_id_list=None, target_count=None):
        self.current_count = current_count  # type: int
        self.order_id_list = order_id_list  # type: str
        self.target_count = target_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersResponseBodyClustersClusterInfoOrderTaskInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_count is not None:
            result['CurrentCount'] = self.current_count
        if self.order_id_list is not None:
            result['OrderIdList'] = self.order_id_list
        if self.target_count is not None:
            result['TargetCount'] = self.target_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentCount') is not None:
            self.current_count = m.get('CurrentCount')
        if m.get('OrderIdList') is not None:
            self.order_id_list = m.get('OrderIdList')
        if m.get('TargetCount') is not None:
            self.target_count = m.get('TargetCount')
        return self


class ListClustersResponseBodyClustersClusterInfoTagsTag(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersResponseBodyClustersClusterInfoTagsTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListClustersResponseBodyClustersClusterInfoTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: list[ListClustersResponseBodyClustersClusterInfoTagsTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClustersResponseBodyClustersClusterInfoTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListClustersResponseBodyClustersClusterInfoTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListClustersResponseBodyClustersClusterInfo(TeaModel):
    def __init__(self, charge_type=None, create_resource=None, create_time=None, deposit_type=None,
                 expired_time=None, fail_reason=None, has_uncompleted_order=None, id=None, k_8s_cluster_id=None,
                 machine_type=None, meta_store_type=None, name=None, order_list=None, order_task_info=None, period=None,
                 running_time=None, status=None, tags=None, type=None):
        self.charge_type = charge_type  # type: str
        self.create_resource = create_resource  # type: str
        self.create_time = create_time  # type: long
        self.deposit_type = deposit_type  # type: str
        self.expired_time = expired_time  # type: long
        self.fail_reason = fail_reason  # type: ListClustersResponseBodyClustersClusterInfoFailReason
        self.has_uncompleted_order = has_uncompleted_order  # type: bool
        self.id = id  # type: str
        self.k_8s_cluster_id = k_8s_cluster_id  # type: str
        self.machine_type = machine_type  # type: str
        self.meta_store_type = meta_store_type  # type: str
        self.name = name  # type: str
        self.order_list = order_list  # type: str
        self.order_task_info = order_task_info  # type: ListClustersResponseBodyClustersClusterInfoOrderTaskInfo
        self.period = period  # type: int
        self.running_time = running_time  # type: int
        self.status = status  # type: str
        self.tags = tags  # type: ListClustersResponseBodyClustersClusterInfoTags
        self.type = type  # type: str

    def validate(self):
        if self.fail_reason:
            self.fail_reason.validate()
        if self.order_task_info:
            self.order_task_info.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super(ListClustersResponseBodyClustersClusterInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_resource is not None:
            result['CreateResource'] = self.create_resource
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deposit_type is not None:
            result['DepositType'] = self.deposit_type
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason.to_map()
        if self.has_uncompleted_order is not None:
            result['HasUncompletedOrder'] = self.has_uncompleted_order
        if self.id is not None:
            result['Id'] = self.id
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        if self.meta_store_type is not None:
            result['MetaStoreType'] = self.meta_store_type
        if self.name is not None:
            result['Name'] = self.name
        if self.order_list is not None:
            result['OrderList'] = self.order_list
        if self.order_task_info is not None:
            result['OrderTaskInfo'] = self.order_task_info.to_map()
        if self.period is not None:
            result['Period'] = self.period
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateResource') is not None:
            self.create_resource = m.get('CreateResource')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DepositType') is not None:
            self.deposit_type = m.get('DepositType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FailReason') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoFailReason()
            self.fail_reason = temp_model.from_map(m['FailReason'])
        if m.get('HasUncompletedOrder') is not None:
            self.has_uncompleted_order = m.get('HasUncompletedOrder')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('MetaStoreType') is not None:
            self.meta_store_type = m.get('MetaStoreType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderList') is not None:
            self.order_list = m.get('OrderList')
        if m.get('OrderTaskInfo') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoOrderTaskInfo()
            self.order_task_info = temp_model.from_map(m['OrderTaskInfo'])
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListClustersResponseBodyClusters(TeaModel):
    def __init__(self, cluster_info=None):
        self.cluster_info = cluster_info  # type: list[ListClustersResponseBodyClustersClusterInfo]

    def validate(self):
        if self.cluster_info:
            for k in self.cluster_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClustersResponseBodyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClusterInfo'] = []
        if self.cluster_info is not None:
            for k in self.cluster_info:
                result['ClusterInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cluster_info = []
        if m.get('ClusterInfo') is not None:
            for k in m.get('ClusterInfo'):
                temp_model = ListClustersResponseBodyClustersClusterInfo()
                self.cluster_info.append(temp_model.from_map(k))
        return self


class ListClustersResponseBody(TeaModel):
    def __init__(self, clusters=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.clusters = clusters  # type: ListClustersResponseBodyClusters
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.clusters:
            self.clusters.validate()

    def to_map(self):
        _map = super(ListClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['Clusters'] = self.clusters.to_map()
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
        if m.get('Clusters') is not None:
            temp_model = ListClustersResponseBodyClusters()
            self.clusters = temp_model.from_map(m['Clusters'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListClustersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClustersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowRequest(TeaModel):
    def __init__(self, cluster_id=None, id=None, job_id=None, name=None, page_number=None, page_size=None,
                 periodic=None, project_id=None, region_id=None, status=None):
        self.cluster_id = cluster_id  # type: str
        self.id = id  # type: str
        self.job_id = job_id  # type: str
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.periodic = periodic  # type: bool
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.id is not None:
            result['Id'] = self.id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.periodic is not None:
            result['Periodic'] = self.periodic
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Periodic') is not None:
            self.periodic = m.get('Periodic')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFlowResponseBodyFlowFlow(TeaModel):
    def __init__(self, alert_conf=None, alert_ding_ding_group_biz_id=None, alert_user_group_biz_id=None,
                 category_id=None, cluster_id=None, create_cluster=None, cron_expr=None, description=None, end_schedule=None,
                 gmt_create=None, gmt_modified=None, graph=None, host_name=None, id=None, name=None, periodic=None,
                 project_id=None, start_schedule=None, status=None, type=None):
        self.alert_conf = alert_conf  # type: str
        self.alert_ding_ding_group_biz_id = alert_ding_ding_group_biz_id  # type: str
        self.alert_user_group_biz_id = alert_user_group_biz_id  # type: str
        self.category_id = category_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.create_cluster = create_cluster  # type: bool
        self.cron_expr = cron_expr  # type: str
        self.description = description  # type: str
        self.end_schedule = end_schedule  # type: long
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.graph = graph  # type: str
        self.host_name = host_name  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.periodic = periodic  # type: bool
        self.project_id = project_id  # type: str
        self.start_schedule = start_schedule  # type: long
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowResponseBodyFlowFlow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.alert_ding_ding_group_biz_id is not None:
            result['AlertDingDingGroupBizId'] = self.alert_ding_ding_group_biz_id
        if self.alert_user_group_biz_id is not None:
            result['AlertUserGroupBizId'] = self.alert_user_group_biz_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_cluster is not None:
            result['CreateCluster'] = self.create_cluster
        if self.cron_expr is not None:
            result['CronExpr'] = self.cron_expr
        if self.description is not None:
            result['Description'] = self.description
        if self.end_schedule is not None:
            result['EndSchedule'] = self.end_schedule
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.graph is not None:
            result['Graph'] = self.graph
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.periodic is not None:
            result['Periodic'] = self.periodic
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.start_schedule is not None:
            result['StartSchedule'] = self.start_schedule
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('AlertDingDingGroupBizId') is not None:
            self.alert_ding_ding_group_biz_id = m.get('AlertDingDingGroupBizId')
        if m.get('AlertUserGroupBizId') is not None:
            self.alert_user_group_biz_id = m.get('AlertUserGroupBizId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateCluster') is not None:
            self.create_cluster = m.get('CreateCluster')
        if m.get('CronExpr') is not None:
            self.cron_expr = m.get('CronExpr')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndSchedule') is not None:
            self.end_schedule = m.get('EndSchedule')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Graph') is not None:
            self.graph = m.get('Graph')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Periodic') is not None:
            self.periodic = m.get('Periodic')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('StartSchedule') is not None:
            self.start_schedule = m.get('StartSchedule')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFlowResponseBodyFlow(TeaModel):
    def __init__(self, flow=None):
        self.flow = flow  # type: list[ListFlowResponseBodyFlowFlow]

    def validate(self):
        if self.flow:
            for k in self.flow:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowResponseBodyFlow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Flow'] = []
        if self.flow is not None:
            for k in self.flow:
                result['Flow'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.flow = []
        if m.get('Flow') is not None:
            for k in m.get('Flow'):
                temp_model = ListFlowResponseBodyFlowFlow()
                self.flow.append(temp_model.from_map(k))
        return self


class ListFlowResponseBody(TeaModel):
    def __init__(self, flow=None, page_number=None, page_size=None, request_id=None, total=None):
        self.flow = flow  # type: ListFlowResponseBodyFlow
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        if self.flow:
            self.flow.validate()

    def to_map(self):
        _map = super(ListFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flow') is not None:
            temp_model = ListFlowResponseBodyFlow()
            self.flow = temp_model.from_map(m['Flow'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowClusterRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None, region_id=None, resource_group_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListFlowClusterResponseBodyClustersClusterInfoFailReason(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowClusterResponseBodyClustersClusterInfoFailReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFlowClusterResponseBodyClustersClusterInfoOrderTaskInfo(TeaModel):
    def __init__(self, current_count=None, order_id_list=None, target_count=None):
        self.current_count = current_count  # type: int
        self.order_id_list = order_id_list  # type: str
        self.target_count = target_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowClusterResponseBodyClustersClusterInfoOrderTaskInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_count is not None:
            result['CurrentCount'] = self.current_count
        if self.order_id_list is not None:
            result['OrderIdList'] = self.order_id_list
        if self.target_count is not None:
            result['TargetCount'] = self.target_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentCount') is not None:
            self.current_count = m.get('CurrentCount')
        if m.get('OrderIdList') is not None:
            self.order_id_list = m.get('OrderIdList')
        if m.get('TargetCount') is not None:
            self.target_count = m.get('TargetCount')
        return self


class ListFlowClusterResponseBodyClustersClusterInfo(TeaModel):
    def __init__(self, charge_type=None, create_resource=None, create_time=None, expired_time=None,
                 fail_reason=None, has_uncompleted_order=None, id=None, k_8s_cluster_id=None, name=None, order_list=None,
                 order_task_info=None, period=None, running_time=None, status=None, type=None):
        self.charge_type = charge_type  # type: str
        self.create_resource = create_resource  # type: str
        self.create_time = create_time  # type: long
        self.expired_time = expired_time  # type: long
        self.fail_reason = fail_reason  # type: ListFlowClusterResponseBodyClustersClusterInfoFailReason
        self.has_uncompleted_order = has_uncompleted_order  # type: bool
        self.id = id  # type: str
        self.k_8s_cluster_id = k_8s_cluster_id  # type: str
        self.name = name  # type: str
        self.order_list = order_list  # type: str
        self.order_task_info = order_task_info  # type: ListFlowClusterResponseBodyClustersClusterInfoOrderTaskInfo
        self.period = period  # type: int
        self.running_time = running_time  # type: int
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.fail_reason:
            self.fail_reason.validate()
        if self.order_task_info:
            self.order_task_info.validate()

    def to_map(self):
        _map = super(ListFlowClusterResponseBodyClustersClusterInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_resource is not None:
            result['CreateResource'] = self.create_resource
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason.to_map()
        if self.has_uncompleted_order is not None:
            result['HasUncompletedOrder'] = self.has_uncompleted_order
        if self.id is not None:
            result['Id'] = self.id
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.name is not None:
            result['Name'] = self.name
        if self.order_list is not None:
            result['OrderList'] = self.order_list
        if self.order_task_info is not None:
            result['OrderTaskInfo'] = self.order_task_info.to_map()
        if self.period is not None:
            result['Period'] = self.period
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateResource') is not None:
            self.create_resource = m.get('CreateResource')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FailReason') is not None:
            temp_model = ListFlowClusterResponseBodyClustersClusterInfoFailReason()
            self.fail_reason = temp_model.from_map(m['FailReason'])
        if m.get('HasUncompletedOrder') is not None:
            self.has_uncompleted_order = m.get('HasUncompletedOrder')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderList') is not None:
            self.order_list = m.get('OrderList')
        if m.get('OrderTaskInfo') is not None:
            temp_model = ListFlowClusterResponseBodyClustersClusterInfoOrderTaskInfo()
            self.order_task_info = temp_model.from_map(m['OrderTaskInfo'])
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFlowClusterResponseBodyClusters(TeaModel):
    def __init__(self, cluster_info=None):
        self.cluster_info = cluster_info  # type: list[ListFlowClusterResponseBodyClustersClusterInfo]

    def validate(self):
        if self.cluster_info:
            for k in self.cluster_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowClusterResponseBodyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClusterInfo'] = []
        if self.cluster_info is not None:
            for k in self.cluster_info:
                result['ClusterInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cluster_info = []
        if m.get('ClusterInfo') is not None:
            for k in m.get('ClusterInfo'):
                temp_model = ListFlowClusterResponseBodyClustersClusterInfo()
                self.cluster_info.append(temp_model.from_map(k))
        return self


class ListFlowClusterResponseBody(TeaModel):
    def __init__(self, clusters=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.clusters = clusters  # type: ListFlowClusterResponseBodyClusters
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.clusters:
            self.clusters.validate()

    def to_map(self):
        _map = super(ListFlowClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['Clusters'] = self.clusters.to_map()
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
        if m.get('Clusters') is not None:
            temp_model = ListFlowClusterResponseBodyClusters()
            self.clusters = temp_model.from_map(m['Clusters'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFlowClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFlowClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowClusterAllRequest(TeaModel):
    def __init__(self, product_type=None, region_id=None, resource_group_id=None):
        self.product_type = product_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowClusterAllRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListFlowClusterAllResponseBodyClustersClusterInfoFailReason(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowClusterAllResponseBodyClustersClusterInfoFailReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFlowClusterAllResponseBodyClustersClusterInfoOrderTaskInfo(TeaModel):
    def __init__(self, current_count=None, order_id_list=None, target_count=None):
        self.current_count = current_count  # type: int
        self.order_id_list = order_id_list  # type: str
        self.target_count = target_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowClusterAllResponseBodyClustersClusterInfoOrderTaskInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_count is not None:
            result['CurrentCount'] = self.current_count
        if self.order_id_list is not None:
            result['OrderIdList'] = self.order_id_list
        if self.target_count is not None:
            result['TargetCount'] = self.target_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentCount') is not None:
            self.current_count = m.get('CurrentCount')
        if m.get('OrderIdList') is not None:
            self.order_id_list = m.get('OrderIdList')
        if m.get('TargetCount') is not None:
            self.target_count = m.get('TargetCount')
        return self


class ListFlowClusterAllResponseBodyClustersClusterInfo(TeaModel):
    def __init__(self, charge_type=None, create_resource=None, create_time=None, expired_time=None,
                 fail_reason=None, has_uncompleted_order=None, id=None, k_8s_cluster_id=None, name=None, order_list=None,
                 order_task_info=None, period=None, running_time=None, status=None, type=None):
        self.charge_type = charge_type  # type: str
        self.create_resource = create_resource  # type: str
        self.create_time = create_time  # type: long
        self.expired_time = expired_time  # type: long
        self.fail_reason = fail_reason  # type: ListFlowClusterAllResponseBodyClustersClusterInfoFailReason
        self.has_uncompleted_order = has_uncompleted_order  # type: bool
        self.id = id  # type: str
        self.k_8s_cluster_id = k_8s_cluster_id  # type: str
        self.name = name  # type: str
        self.order_list = order_list  # type: str
        self.order_task_info = order_task_info  # type: ListFlowClusterAllResponseBodyClustersClusterInfoOrderTaskInfo
        self.period = period  # type: int
        self.running_time = running_time  # type: int
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.fail_reason:
            self.fail_reason.validate()
        if self.order_task_info:
            self.order_task_info.validate()

    def to_map(self):
        _map = super(ListFlowClusterAllResponseBodyClustersClusterInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_resource is not None:
            result['CreateResource'] = self.create_resource
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason.to_map()
        if self.has_uncompleted_order is not None:
            result['HasUncompletedOrder'] = self.has_uncompleted_order
        if self.id is not None:
            result['Id'] = self.id
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.name is not None:
            result['Name'] = self.name
        if self.order_list is not None:
            result['OrderList'] = self.order_list
        if self.order_task_info is not None:
            result['OrderTaskInfo'] = self.order_task_info.to_map()
        if self.period is not None:
            result['Period'] = self.period
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateResource') is not None:
            self.create_resource = m.get('CreateResource')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FailReason') is not None:
            temp_model = ListFlowClusterAllResponseBodyClustersClusterInfoFailReason()
            self.fail_reason = temp_model.from_map(m['FailReason'])
        if m.get('HasUncompletedOrder') is not None:
            self.has_uncompleted_order = m.get('HasUncompletedOrder')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderList') is not None:
            self.order_list = m.get('OrderList')
        if m.get('OrderTaskInfo') is not None:
            temp_model = ListFlowClusterAllResponseBodyClustersClusterInfoOrderTaskInfo()
            self.order_task_info = temp_model.from_map(m['OrderTaskInfo'])
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFlowClusterAllResponseBodyClusters(TeaModel):
    def __init__(self, cluster_info=None):
        self.cluster_info = cluster_info  # type: list[ListFlowClusterAllResponseBodyClustersClusterInfo]

    def validate(self):
        if self.cluster_info:
            for k in self.cluster_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowClusterAllResponseBodyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClusterInfo'] = []
        if self.cluster_info is not None:
            for k in self.cluster_info:
                result['ClusterInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cluster_info = []
        if m.get('ClusterInfo') is not None:
            for k in m.get('ClusterInfo'):
                temp_model = ListFlowClusterAllResponseBodyClustersClusterInfo()
                self.cluster_info.append(temp_model.from_map(k))
        return self


class ListFlowClusterAllResponseBody(TeaModel):
    def __init__(self, clusters=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.clusters = clusters  # type: ListFlowClusterAllResponseBodyClusters
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.clusters:
            self.clusters.validate()

    def to_map(self):
        _map = super(ListFlowClusterAllResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['Clusters'] = self.clusters.to_map()
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
        if m.get('Clusters') is not None:
            temp_model = ListFlowClusterAllResponseBodyClusters()
            self.clusters = temp_model.from_map(m['Clusters'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFlowClusterAllResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFlowClusterAllResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowClusterAllResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowClusterAllResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowClusterAllHostsRequest(TeaModel):
    def __init__(self, cluster_id=None, project_id=None, region_id=None, resource_group_id=None):
        self.cluster_id = cluster_id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowClusterAllHostsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListFlowClusterAllHostsResponseBodyHostListHost(TeaModel):
    def __init__(self, cpu=None, host_id=None, host_instance_id=None, host_name=None, instance_type=None,
                 memory=None, private_ip=None, public_ip=None, role=None, serial_number=None, status=None, type=None):
        self.cpu = cpu  # type: int
        self.host_id = host_id  # type: str
        self.host_instance_id = host_instance_id  # type: str
        self.host_name = host_name  # type: str
        self.instance_type = instance_type  # type: str
        self.memory = memory  # type: int
        self.private_ip = private_ip  # type: str
        self.public_ip = public_ip  # type: str
        self.role = role  # type: str
        self.serial_number = serial_number  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowClusterAllHostsResponseBodyHostListHost, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_instance_id is not None:
            result['HostInstanceId'] = self.host_instance_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        if self.role is not None:
            result['Role'] = self.role
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostInstanceId') is not None:
            self.host_instance_id = m.get('HostInstanceId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFlowClusterAllHostsResponseBodyHostList(TeaModel):
    def __init__(self, host=None):
        self.host = host  # type: list[ListFlowClusterAllHostsResponseBodyHostListHost]

    def validate(self):
        if self.host:
            for k in self.host:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowClusterAllHostsResponseBodyHostList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Host'] = []
        if self.host is not None:
            for k in self.host:
                result['Host'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.host = []
        if m.get('Host') is not None:
            for k in m.get('Host'):
                temp_model = ListFlowClusterAllHostsResponseBodyHostListHost()
                self.host.append(temp_model.from_map(k))
        return self


class ListFlowClusterAllHostsResponseBody(TeaModel):
    def __init__(self, host_list=None, request_id=None):
        self.host_list = host_list  # type: ListFlowClusterAllHostsResponseBodyHostList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.host_list:
            self.host_list.validate()

    def to_map(self):
        _map = super(ListFlowClusterAllHostsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_list is not None:
            result['HostList'] = self.host_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostList') is not None:
            temp_model = ListFlowClusterAllHostsResponseBodyHostList()
            self.host_list = temp_model.from_map(m['HostList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFlowClusterAllHostsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFlowClusterAllHostsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowClusterAllHostsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowClusterAllHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowClusterHostRequest(TeaModel):
    def __init__(self, cluster_id=None, project_id=None, region_id=None, resource_group_id=None):
        self.cluster_id = cluster_id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowClusterHostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListFlowClusterHostResponseBodyHostListHost(TeaModel):
    def __init__(self, cpu=None, host_id=None, host_instance_id=None, host_name=None, instance_type=None,
                 memory=None, private_ip=None, public_ip=None, role=None, serial_number=None, status=None, type=None):
        self.cpu = cpu  # type: int
        self.host_id = host_id  # type: str
        self.host_instance_id = host_instance_id  # type: str
        self.host_name = host_name  # type: str
        self.instance_type = instance_type  # type: str
        self.memory = memory  # type: int
        self.private_ip = private_ip  # type: str
        self.public_ip = public_ip  # type: str
        self.role = role  # type: str
        self.serial_number = serial_number  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowClusterHostResponseBodyHostListHost, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_instance_id is not None:
            result['HostInstanceId'] = self.host_instance_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        if self.role is not None:
            result['Role'] = self.role
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostInstanceId') is not None:
            self.host_instance_id = m.get('HostInstanceId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFlowClusterHostResponseBodyHostList(TeaModel):
    def __init__(self, host=None):
        self.host = host  # type: list[ListFlowClusterHostResponseBodyHostListHost]

    def validate(self):
        if self.host:
            for k in self.host:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowClusterHostResponseBodyHostList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Host'] = []
        if self.host is not None:
            for k in self.host:
                result['Host'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.host = []
        if m.get('Host') is not None:
            for k in m.get('Host'):
                temp_model = ListFlowClusterHostResponseBodyHostListHost()
                self.host.append(temp_model.from_map(k))
        return self


class ListFlowClusterHostResponseBody(TeaModel):
    def __init__(self, host_list=None, request_id=None):
        self.host_list = host_list  # type: ListFlowClusterHostResponseBodyHostList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.host_list:
            self.host_list.validate()

    def to_map(self):
        _map = super(ListFlowClusterHostResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_list is not None:
            result['HostList'] = self.host_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostList') is not None:
            temp_model = ListFlowClusterHostResponseBodyHostList()
            self.host_list = temp_model.from_map(m['HostList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFlowClusterHostResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFlowClusterHostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowClusterHostResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowClusterHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowEntitySnapshotRequest(TeaModel):
    def __init__(self, committer_id=None, current_size=None, entity_group_id=None, entity_id=None, entity_type=None,
                 limit=None, order_field=None, order_mode=None, page_count=None, page_number=None, page_size=None,
                 region_id=None, resource_owner_id=None, revision=None):
        self.committer_id = committer_id  # type: str
        self.current_size = current_size  # type: int
        self.entity_group_id = entity_group_id  # type: str
        self.entity_id = entity_id  # type: str
        self.entity_type = entity_type  # type: str
        self.limit = limit  # type: int
        self.order_field = order_field  # type: str
        self.order_mode = order_mode  # type: str
        self.page_count = page_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.revision = revision  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowEntitySnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.committer_id is not None:
            result['CommitterId'] = self.committer_id
        if self.current_size is not None:
            result['CurrentSize'] = self.current_size
        if self.entity_group_id is not None:
            result['EntityGroupId'] = self.entity_group_id
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.order_mode is not None:
            result['OrderMode'] = self.order_mode
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.revision is not None:
            result['Revision'] = self.revision
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommitterId') is not None:
            self.committer_id = m.get('CommitterId')
        if m.get('CurrentSize') is not None:
            self.current_size = m.get('CurrentSize')
        if m.get('EntityGroupId') is not None:
            self.entity_group_id = m.get('EntityGroupId')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('OrderMode') is not None:
            self.order_mode = m.get('OrderMode')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        return self


class ListFlowEntitySnapshotResponseBodyItemsItem(TeaModel):
    def __init__(self, active=None, committer_id=None, data=None, entity_group_id=None, entity_id=None,
                 entity_type=None, gmt_create=None, message=None, revision=None, user_id=None):
        self.active = active  # type: bool
        self.committer_id = committer_id  # type: str
        self.data = data  # type: str
        self.entity_group_id = entity_group_id  # type: str
        self.entity_id = entity_id  # type: str
        self.entity_type = entity_type  # type: str
        self.gmt_create = gmt_create  # type: long
        self.message = message  # type: str
        self.revision = revision  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowEntitySnapshotResponseBodyItemsItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.committer_id is not None:
            result['CommitterId'] = self.committer_id
        if self.data is not None:
            result['Data'] = self.data
        if self.entity_group_id is not None:
            result['EntityGroupId'] = self.entity_group_id
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.message is not None:
            result['Message'] = self.message
        if self.revision is not None:
            result['Revision'] = self.revision
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('CommitterId') is not None:
            self.committer_id = m.get('CommitterId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('EntityGroupId') is not None:
            self.entity_group_id = m.get('EntityGroupId')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListFlowEntitySnapshotResponseBodyItems(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[ListFlowEntitySnapshotResponseBodyItemsItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowEntitySnapshotResponseBodyItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = ListFlowEntitySnapshotResponseBodyItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class ListFlowEntitySnapshotResponseBody(TeaModel):
    def __init__(self, items=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.items = items  # type: ListFlowEntitySnapshotResponseBodyItems
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(ListFlowEntitySnapshotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
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
        if m.get('Items') is not None:
            temp_model = ListFlowEntitySnapshotResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFlowEntitySnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFlowEntitySnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowEntitySnapshotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowEntitySnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowInstanceRequest(TeaModel):
    def __init__(self, flow_id=None, flow_name=None, id=None, instance_id=None, order_by=None, order_type=None,
                 owner=None, page_number=None, page_size=None, project_id=None, region_id=None, status_list=None,
                 time_range=None):
        self.flow_id = flow_id  # type: str
        self.flow_name = flow_name  # type: str
        self.id = id  # type: str
        self.instance_id = instance_id  # type: str
        self.order_by = order_by  # type: str
        self.order_type = order_type  # type: str
        self.owner = owner  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.status_list = status_list  # type: list[str]
        self.time_range = time_range  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.time_range is not None:
            result['TimeRange'] = self.time_range
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')
        return self


class ListFlowInstanceResponseBodyFlowInstancesFlowInstance(TeaModel):
    def __init__(self, cluster_id=None, duration=None, end_time=None, flow_id=None, flow_name=None, gmt_create=None,
                 gmt_modified=None, has_node_failed=None, id=None, owner=None, project_id=None, schedule_time=None,
                 start_time=None, status=None):
        self.cluster_id = cluster_id  # type: str
        self.duration = duration  # type: long
        self.end_time = end_time  # type: long
        self.flow_id = flow_id  # type: str
        self.flow_name = flow_name  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.has_node_failed = has_node_failed  # type: bool
        self.id = id  # type: str
        self.owner = owner  # type: str
        self.project_id = project_id  # type: str
        self.schedule_time = schedule_time  # type: long
        self.start_time = start_time  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowInstanceResponseBodyFlowInstancesFlowInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.has_node_failed is not None:
            result['HasNodeFailed'] = self.has_node_failed
        if self.id is not None:
            result['Id'] = self.id
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HasNodeFailed') is not None:
            self.has_node_failed = m.get('HasNodeFailed')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFlowInstanceResponseBodyFlowInstances(TeaModel):
    def __init__(self, flow_instance=None):
        self.flow_instance = flow_instance  # type: list[ListFlowInstanceResponseBodyFlowInstancesFlowInstance]

    def validate(self):
        if self.flow_instance:
            for k in self.flow_instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowInstanceResponseBodyFlowInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FlowInstance'] = []
        if self.flow_instance is not None:
            for k in self.flow_instance:
                result['FlowInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.flow_instance = []
        if m.get('FlowInstance') is not None:
            for k in m.get('FlowInstance'):
                temp_model = ListFlowInstanceResponseBodyFlowInstancesFlowInstance()
                self.flow_instance.append(temp_model.from_map(k))
        return self


class ListFlowInstanceResponseBody(TeaModel):
    def __init__(self, flow_instances=None, page_number=None, page_size=None, request_id=None, total=None):
        self.flow_instances = flow_instances  # type: ListFlowInstanceResponseBodyFlowInstances
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        if self.flow_instances:
            self.flow_instances.validate()

    def to_map(self):
        _map = super(ListFlowInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_instances is not None:
            result['FlowInstances'] = self.flow_instances.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowInstances') is not None:
            temp_model = ListFlowInstanceResponseBodyFlowInstances()
            self.flow_instances = temp_model.from_map(m['FlowInstances'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFlowInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFlowInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowJobHistoryRequest(TeaModel):
    def __init__(self, id=None, instance_id=None, job_type=None, page_number=None, page_size=None, project_id=None,
                 region_id=None, status_list=None, time_range=None):
        self.id = id  # type: str
        self.instance_id = instance_id  # type: str
        self.job_type = job_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.status_list = status_list  # type: list[str]
        self.time_range = time_range  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowJobHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.time_range is not None:
            result['TimeRange'] = self.time_range
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')
        return self


class ListFlowJobHistoryResponseBodyNodeInstancesNodeInstance(TeaModel):
    def __init__(self, cluster_id=None, end_time=None, env_conf=None, external_id=None, external_info=None,
                 external_status=None, fail_act=None, gmt_create=None, gmt_modified=None, host_name=None, id=None, job_id=None,
                 job_name=None, job_params=None, job_type=None, max_retry=None, node_name=None, param_conf=None,
                 project_id=None, retries=None, retry_interval=None, run_conf=None, start_time=None, status=None, type=None,
                 pending=None):
        self.cluster_id = cluster_id  # type: str
        self.end_time = end_time  # type: long
        self.env_conf = env_conf  # type: str
        self.external_id = external_id  # type: str
        self.external_info = external_info  # type: str
        self.external_status = external_status  # type: str
        self.fail_act = fail_act  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.host_name = host_name  # type: str
        self.id = id  # type: str
        self.job_id = job_id  # type: str
        self.job_name = job_name  # type: str
        self.job_params = job_params  # type: str
        self.job_type = job_type  # type: str
        self.max_retry = max_retry  # type: int
        self.node_name = node_name  # type: str
        self.param_conf = param_conf  # type: str
        self.project_id = project_id  # type: str
        self.retries = retries  # type: int
        self.retry_interval = retry_interval  # type: long
        self.run_conf = run_conf  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: str
        self.type = type  # type: str
        self.pending = pending  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowJobHistoryResponseBodyNodeInstancesNodeInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.external_info is not None:
            result['ExternalInfo'] = self.external_info
        if self.external_status is not None:
            result['ExternalStatus'] = self.external_status
        if self.fail_act is not None:
            result['FailAct'] = self.fail_act
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_params is not None:
            result['JobParams'] = self.job_params
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.max_retry is not None:
            result['MaxRetry'] = self.max_retry
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.param_conf is not None:
            result['ParamConf'] = self.param_conf
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.retries is not None:
            result['Retries'] = self.retries
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.run_conf is not None:
            result['RunConf'] = self.run_conf
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.pending is not None:
            result['pending'] = self.pending
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('ExternalInfo') is not None:
            self.external_info = m.get('ExternalInfo')
        if m.get('ExternalStatus') is not None:
            self.external_status = m.get('ExternalStatus')
        if m.get('FailAct') is not None:
            self.fail_act = m.get('FailAct')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobParams') is not None:
            self.job_params = m.get('JobParams')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MaxRetry') is not None:
            self.max_retry = m.get('MaxRetry')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('ParamConf') is not None:
            self.param_conf = m.get('ParamConf')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Retries') is not None:
            self.retries = m.get('Retries')
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('RunConf') is not None:
            self.run_conf = m.get('RunConf')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('pending') is not None:
            self.pending = m.get('pending')
        return self


class ListFlowJobHistoryResponseBodyNodeInstances(TeaModel):
    def __init__(self, node_instance=None):
        self.node_instance = node_instance  # type: list[ListFlowJobHistoryResponseBodyNodeInstancesNodeInstance]

    def validate(self):
        if self.node_instance:
            for k in self.node_instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowJobHistoryResponseBodyNodeInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeInstance'] = []
        if self.node_instance is not None:
            for k in self.node_instance:
                result['NodeInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.node_instance = []
        if m.get('NodeInstance') is not None:
            for k in m.get('NodeInstance'):
                temp_model = ListFlowJobHistoryResponseBodyNodeInstancesNodeInstance()
                self.node_instance.append(temp_model.from_map(k))
        return self


class ListFlowJobHistoryResponseBody(TeaModel):
    def __init__(self, node_instances=None, page_number=None, page_size=None, request_id=None, total=None):
        self.node_instances = node_instances  # type: ListFlowJobHistoryResponseBodyNodeInstances
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        if self.node_instances:
            self.node_instances.validate()

    def to_map(self):
        _map = super(ListFlowJobHistoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_instances is not None:
            result['NodeInstances'] = self.node_instances.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeInstances') is not None:
            temp_model = ListFlowJobHistoryResponseBodyNodeInstances()
            self.node_instances = temp_model.from_map(m['NodeInstances'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFlowJobHistoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFlowJobHistoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowJobHistoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowJobHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowJobsRequest(TeaModel):
    def __init__(self, adhoc=None, id=None, name=None, page_number=None, page_size=None, project_id=None,
                 region_id=None, type=None):
        self.adhoc = adhoc  # type: bool
        self.id = id  # type: str
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adhoc is not None:
            result['Adhoc'] = self.adhoc
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Adhoc') is not None:
            self.adhoc = m.get('Adhoc')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFlowJobsResponseBodyJobListJobResourceListResource(TeaModel):
    def __init__(self, alias=None, path=None):
        self.alias = alias  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowJobsResponseBodyJobListJobResourceListResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ListFlowJobsResponseBodyJobListJobResourceList(TeaModel):
    def __init__(self, resource=None):
        self.resource = resource  # type: list[ListFlowJobsResponseBodyJobListJobResourceListResource]

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowJobsResponseBodyJobListJobResourceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = ListFlowJobsResponseBodyJobListJobResourceListResource()
                self.resource.append(temp_model.from_map(k))
        return self


class ListFlowJobsResponseBodyJobListJob(TeaModel):
    def __init__(self, adhoc=None, alert_conf=None, category_id=None, custom_variables=None, description=None,
                 env_conf=None, fail_act=None, gmt_create=None, gmt_modified=None, id=None, last_instance_detail=None,
                 max_retry=None, mode=None, monitor_conf=None, name=None, param_conf=None, params=None, resource_list=None,
                 retry_interval=None, run_conf=None, type=None):
        self.adhoc = adhoc  # type: str
        self.alert_conf = alert_conf  # type: str
        self.category_id = category_id  # type: str
        self.custom_variables = custom_variables  # type: str
        self.description = description  # type: str
        self.env_conf = env_conf  # type: str
        self.fail_act = fail_act  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.id = id  # type: str
        self.last_instance_detail = last_instance_detail  # type: str
        self.max_retry = max_retry  # type: int
        self.mode = mode  # type: str
        self.monitor_conf = monitor_conf  # type: str
        self.name = name  # type: str
        self.param_conf = param_conf  # type: str
        self.params = params  # type: str
        self.resource_list = resource_list  # type: ListFlowJobsResponseBodyJobListJobResourceList
        self.retry_interval = retry_interval  # type: long
        self.run_conf = run_conf  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.resource_list:
            self.resource_list.validate()

    def to_map(self):
        _map = super(ListFlowJobsResponseBodyJobListJob, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adhoc is not None:
            result['Adhoc'] = self.adhoc
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.custom_variables is not None:
            result['CustomVariables'] = self.custom_variables
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        if self.fail_act is not None:
            result['FailAct'] = self.fail_act
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.last_instance_detail is not None:
            result['LastInstanceDetail'] = self.last_instance_detail
        if self.max_retry is not None:
            result['MaxRetry'] = self.max_retry
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.monitor_conf is not None:
            result['MonitorConf'] = self.monitor_conf
        if self.name is not None:
            result['Name'] = self.name
        if self.param_conf is not None:
            result['ParamConf'] = self.param_conf
        if self.params is not None:
            result['Params'] = self.params
        if self.resource_list is not None:
            result['ResourceList'] = self.resource_list.to_map()
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.run_conf is not None:
            result['RunConf'] = self.run_conf
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Adhoc') is not None:
            self.adhoc = m.get('Adhoc')
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CustomVariables') is not None:
            self.custom_variables = m.get('CustomVariables')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        if m.get('FailAct') is not None:
            self.fail_act = m.get('FailAct')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastInstanceDetail') is not None:
            self.last_instance_detail = m.get('LastInstanceDetail')
        if m.get('MaxRetry') is not None:
            self.max_retry = m.get('MaxRetry')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('MonitorConf') is not None:
            self.monitor_conf = m.get('MonitorConf')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamConf') is not None:
            self.param_conf = m.get('ParamConf')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ResourceList') is not None:
            temp_model = ListFlowJobsResponseBodyJobListJobResourceList()
            self.resource_list = temp_model.from_map(m['ResourceList'])
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('RunConf') is not None:
            self.run_conf = m.get('RunConf')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFlowJobsResponseBodyJobList(TeaModel):
    def __init__(self, job=None):
        self.job = job  # type: list[ListFlowJobsResponseBodyJobListJob]

    def validate(self):
        if self.job:
            for k in self.job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowJobsResponseBodyJobList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Job'] = []
        if self.job is not None:
            for k in self.job:
                result['Job'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.job = []
        if m.get('Job') is not None:
            for k in m.get('Job'):
                temp_model = ListFlowJobsResponseBodyJobListJob()
                self.job.append(temp_model.from_map(k))
        return self


class ListFlowJobsResponseBody(TeaModel):
    def __init__(self, job_list=None, page_number=None, page_size=None, request_id=None, total=None):
        self.job_list = job_list  # type: ListFlowJobsResponseBodyJobList
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        if self.job_list:
            self.job_list.validate()

    def to_map(self):
        _map = super(ListFlowJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_list is not None:
            result['JobList'] = self.job_list.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobList') is not None:
            temp_model = ListFlowJobsResponseBodyJobList()
            self.job_list = temp_model.from_map(m['JobList'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFlowJobsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFlowJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowJobsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowNodeInstanceContainerStatusRequest(TeaModel):
    def __init__(self, node_instance_id=None, page_number=None, page_size=None, project_id=None, region_id=None):
        self.node_instance_id = node_instance_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowNodeInstanceContainerStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_instance_id is not None:
            result['NodeInstanceId'] = self.node_instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeInstanceId') is not None:
            self.node_instance_id = m.get('NodeInstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListFlowNodeInstanceContainerStatusResponseBodyContainerStatusListContainerStatus(TeaModel):
    def __init__(self, application_id=None, container_id=None, host_name=None, status=None):
        self.application_id = application_id  # type: str
        self.container_id = container_id  # type: str
        self.host_name = host_name  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowNodeInstanceContainerStatusResponseBodyContainerStatusListContainerStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFlowNodeInstanceContainerStatusResponseBodyContainerStatusList(TeaModel):
    def __init__(self, container_status=None):
        self.container_status = container_status  # type: list[ListFlowNodeInstanceContainerStatusResponseBodyContainerStatusListContainerStatus]

    def validate(self):
        if self.container_status:
            for k in self.container_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowNodeInstanceContainerStatusResponseBodyContainerStatusList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContainerStatus'] = []
        if self.container_status is not None:
            for k in self.container_status:
                result['ContainerStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.container_status = []
        if m.get('ContainerStatus') is not None:
            for k in m.get('ContainerStatus'):
                temp_model = ListFlowNodeInstanceContainerStatusResponseBodyContainerStatusListContainerStatus()
                self.container_status.append(temp_model.from_map(k))
        return self


class ListFlowNodeInstanceContainerStatusResponseBody(TeaModel):
    def __init__(self, container_status_list=None, page_number=None, page_size=None, request_id=None, total=None):
        self.container_status_list = container_status_list  # type: ListFlowNodeInstanceContainerStatusResponseBodyContainerStatusList
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        if self.container_status_list:
            self.container_status_list.validate()

    def to_map(self):
        _map = super(ListFlowNodeInstanceContainerStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_status_list is not None:
            result['ContainerStatusList'] = self.container_status_list.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerStatusList') is not None:
            temp_model = ListFlowNodeInstanceContainerStatusResponseBodyContainerStatusList()
            self.container_status_list = temp_model.from_map(m['ContainerStatusList'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFlowNodeInstanceContainerStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFlowNodeInstanceContainerStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowNodeInstanceContainerStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowNodeInstanceContainerStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowNodeSqlResultRequest(TeaModel):
    def __init__(self, length=None, node_instance_id=None, offset=None, project_id=None, region_id=None,
                 sql_index=None):
        self.length = length  # type: int
        self.node_instance_id = node_instance_id  # type: str
        self.offset = offset  # type: int
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.sql_index = sql_index  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowNodeSqlResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.length is not None:
            result['Length'] = self.length
        if self.node_instance_id is not None:
            result['NodeInstanceId'] = self.node_instance_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sql_index is not None:
            result['SqlIndex'] = self.sql_index
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('NodeInstanceId') is not None:
            self.node_instance_id = m.get('NodeInstanceId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SqlIndex') is not None:
            self.sql_index = m.get('SqlIndex')
        return self


class ListFlowNodeSqlResultResponseBodyHeaderList(TeaModel):
    def __init__(self, header=None):
        self.header = header  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowNodeSqlResultResponseBodyHeaderList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header is not None:
            result['Header'] = self.header
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Header') is not None:
            self.header = m.get('Header')
        return self


class ListFlowNodeSqlResultResponseBodyRowListRowRowItemList(TeaModel):
    def __init__(self, row_item=None):
        self.row_item = row_item  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowNodeSqlResultResponseBodyRowListRowRowItemList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.row_item is not None:
            result['RowItem'] = self.row_item
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RowItem') is not None:
            self.row_item = m.get('RowItem')
        return self


class ListFlowNodeSqlResultResponseBodyRowListRow(TeaModel):
    def __init__(self, row_index=None, row_item_list=None):
        self.row_index = row_index  # type: int
        self.row_item_list = row_item_list  # type: ListFlowNodeSqlResultResponseBodyRowListRowRowItemList

    def validate(self):
        if self.row_item_list:
            self.row_item_list.validate()

    def to_map(self):
        _map = super(ListFlowNodeSqlResultResponseBodyRowListRow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.row_index is not None:
            result['RowIndex'] = self.row_index
        if self.row_item_list is not None:
            result['RowItemList'] = self.row_item_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RowIndex') is not None:
            self.row_index = m.get('RowIndex')
        if m.get('RowItemList') is not None:
            temp_model = ListFlowNodeSqlResultResponseBodyRowListRowRowItemList()
            self.row_item_list = temp_model.from_map(m['RowItemList'])
        return self


class ListFlowNodeSqlResultResponseBodyRowList(TeaModel):
    def __init__(self, row=None):
        self.row = row  # type: list[ListFlowNodeSqlResultResponseBodyRowListRow]

    def validate(self):
        if self.row:
            for k in self.row:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowNodeSqlResultResponseBodyRowList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Row'] = []
        if self.row is not None:
            for k in self.row:
                result['Row'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.row = []
        if m.get('Row') is not None:
            for k in m.get('Row'):
                temp_model = ListFlowNodeSqlResultResponseBodyRowListRow()
                self.row.append(temp_model.from_map(k))
        return self


class ListFlowNodeSqlResultResponseBody(TeaModel):
    def __init__(self, end=None, header_list=None, request_id=None, row_list=None):
        self.end = end  # type: bool
        self.header_list = header_list  # type: ListFlowNodeSqlResultResponseBodyHeaderList
        self.request_id = request_id  # type: str
        self.row_list = row_list  # type: ListFlowNodeSqlResultResponseBodyRowList

    def validate(self):
        if self.header_list:
            self.header_list.validate()
        if self.row_list:
            self.row_list.validate()

    def to_map(self):
        _map = super(ListFlowNodeSqlResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.header_list is not None:
            result['HeaderList'] = self.header_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.row_list is not None:
            result['RowList'] = self.row_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('HeaderList') is not None:
            temp_model = ListFlowNodeSqlResultResponseBodyHeaderList()
            self.header_list = temp_model.from_map(m['HeaderList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RowList') is not None:
            temp_model = ListFlowNodeSqlResultResponseBodyRowList()
            self.row_list = temp_model.from_map(m['RowList'])
        return self


class ListFlowNodeSqlResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFlowNodeSqlResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowNodeSqlResultResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowNodeSqlResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowProjectClusterSettingRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None, region_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowProjectClusterSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListFlowProjectClusterSettingResponseBodyClusterSettingsClusterSettingHostList(TeaModel):
    def __init__(self, host=None):
        self.host = host  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowProjectClusterSettingResponseBodyClusterSettingsClusterSettingHostList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        return self


class ListFlowProjectClusterSettingResponseBodyClusterSettingsClusterSettingQueueList(TeaModel):
    def __init__(self, queue=None):
        self.queue = queue  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowProjectClusterSettingResponseBodyClusterSettingsClusterSettingQueueList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue is not None:
            result['Queue'] = self.queue
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        return self


class ListFlowProjectClusterSettingResponseBodyClusterSettingsClusterSettingUserList(TeaModel):
    def __init__(self, user=None):
        self.user = user  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowProjectClusterSettingResponseBodyClusterSettingsClusterSettingUserList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class ListFlowProjectClusterSettingResponseBodyClusterSettingsClusterSetting(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, default_queue=None, default_user=None, gmt_create=None,
                 gmt_modified=None, host_list=None, k_8s_cluster_id=None, project_id=None, queue_list=None, user_list=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.default_queue = default_queue  # type: str
        self.default_user = default_user  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.host_list = host_list  # type: ListFlowProjectClusterSettingResponseBodyClusterSettingsClusterSettingHostList
        self.k_8s_cluster_id = k_8s_cluster_id  # type: str
        self.project_id = project_id  # type: str
        self.queue_list = queue_list  # type: ListFlowProjectClusterSettingResponseBodyClusterSettingsClusterSettingQueueList
        self.user_list = user_list  # type: ListFlowProjectClusterSettingResponseBodyClusterSettingsClusterSettingUserList

    def validate(self):
        if self.host_list:
            self.host_list.validate()
        if self.queue_list:
            self.queue_list.validate()
        if self.user_list:
            self.user_list.validate()

    def to_map(self):
        _map = super(ListFlowProjectClusterSettingResponseBodyClusterSettingsClusterSetting, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.default_queue is not None:
            result['DefaultQueue'] = self.default_queue
        if self.default_user is not None:
            result['DefaultUser'] = self.default_user
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.host_list is not None:
            result['HostList'] = self.host_list.to_map()
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.queue_list is not None:
            result['QueueList'] = self.queue_list.to_map()
        if self.user_list is not None:
            result['UserList'] = self.user_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('DefaultQueue') is not None:
            self.default_queue = m.get('DefaultQueue')
        if m.get('DefaultUser') is not None:
            self.default_user = m.get('DefaultUser')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HostList') is not None:
            temp_model = ListFlowProjectClusterSettingResponseBodyClusterSettingsClusterSettingHostList()
            self.host_list = temp_model.from_map(m['HostList'])
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('QueueList') is not None:
            temp_model = ListFlowProjectClusterSettingResponseBodyClusterSettingsClusterSettingQueueList()
            self.queue_list = temp_model.from_map(m['QueueList'])
        if m.get('UserList') is not None:
            temp_model = ListFlowProjectClusterSettingResponseBodyClusterSettingsClusterSettingUserList()
            self.user_list = temp_model.from_map(m['UserList'])
        return self


class ListFlowProjectClusterSettingResponseBodyClusterSettings(TeaModel):
    def __init__(self, cluster_setting=None):
        self.cluster_setting = cluster_setting  # type: list[ListFlowProjectClusterSettingResponseBodyClusterSettingsClusterSetting]

    def validate(self):
        if self.cluster_setting:
            for k in self.cluster_setting:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowProjectClusterSettingResponseBodyClusterSettings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClusterSetting'] = []
        if self.cluster_setting is not None:
            for k in self.cluster_setting:
                result['ClusterSetting'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cluster_setting = []
        if m.get('ClusterSetting') is not None:
            for k in m.get('ClusterSetting'):
                temp_model = ListFlowProjectClusterSettingResponseBodyClusterSettingsClusterSetting()
                self.cluster_setting.append(temp_model.from_map(k))
        return self


class ListFlowProjectClusterSettingResponseBody(TeaModel):
    def __init__(self, cluster_settings=None, page_number=None, page_size=None, request_id=None, total=None):
        self.cluster_settings = cluster_settings  # type: ListFlowProjectClusterSettingResponseBodyClusterSettings
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        if self.cluster_settings:
            self.cluster_settings.validate()

    def to_map(self):
        _map = super(ListFlowProjectClusterSettingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_settings is not None:
            result['ClusterSettings'] = self.cluster_settings.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterSettings') is not None:
            temp_model = ListFlowProjectClusterSettingResponseBodyClusterSettings()
            self.cluster_settings = temp_model.from_map(m['ClusterSettings'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFlowProjectClusterSettingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFlowProjectClusterSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowProjectClusterSettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowProjectClusterSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowProjectUserRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None, region_id=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowProjectUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListFlowProjectUserResponseBodyUsersUser(TeaModel):
    def __init__(self, account_user_id=None, gmt_create=None, gmt_modified=None, owner_id=None, project_id=None,
                 user_name=None):
        self.account_user_id = account_user_id  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.owner_id = owner_id  # type: str
        self.project_id = project_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowProjectUserResponseBodyUsersUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_user_id is not None:
            result['AccountUserId'] = self.account_user_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountUserId') is not None:
            self.account_user_id = m.get('AccountUserId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListFlowProjectUserResponseBodyUsers(TeaModel):
    def __init__(self, user=None):
        self.user = user  # type: list[ListFlowProjectUserResponseBodyUsersUser]

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowProjectUserResponseBodyUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = ListFlowProjectUserResponseBodyUsersUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListFlowProjectUserResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total=None, users=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total = total  # type: int
        self.users = users  # type: ListFlowProjectUserResponseBodyUsers

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        _map = super(ListFlowProjectUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.users is not None:
            result['Users'] = self.users.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Users') is not None:
            temp_model = ListFlowProjectUserResponseBodyUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class ListFlowProjectUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFlowProjectUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowProjectUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowProjectUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowProjectsRequest(TeaModel):
    def __init__(self, name=None, page_number=None, page_size=None, product_type=None, project_id=None,
                 region_id=None, resource_group_id=None):
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.product_type = product_type  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowProjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListFlowProjectsResponseBodyProjectsProject(TeaModel):
    def __init__(self, description=None, gmt_create=None, gmt_modified=None, id=None, name=None, user_id=None):
        self.description = description  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.id = id  # type: str
        self.name = name  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowProjectsResponseBodyProjectsProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListFlowProjectsResponseBodyProjects(TeaModel):
    def __init__(self, project=None):
        self.project = project  # type: list[ListFlowProjectsResponseBodyProjectsProject]

    def validate(self):
        if self.project:
            for k in self.project:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowProjectsResponseBodyProjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Project'] = []
        if self.project is not None:
            for k in self.project:
                result['Project'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.project = []
        if m.get('Project') is not None:
            for k in m.get('Project'):
                temp_model = ListFlowProjectsResponseBodyProjectsProject()
                self.project.append(temp_model.from_map(k))
        return self


class ListFlowProjectsResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, projects=None, request_id=None, total=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.projects = projects  # type: ListFlowProjectsResponseBodyProjects
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        if self.projects:
            self.projects.validate()

    def to_map(self):
        _map = super(ListFlowProjectsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.projects is not None:
            result['Projects'] = self.projects.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Projects') is not None:
            temp_model = ListFlowProjectsResponseBodyProjects()
            self.projects = temp_model.from_map(m['Projects'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFlowProjectsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFlowProjectsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowProjectsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowsRequest(TeaModel):
    def __init__(self, cluster_id=None, id=None, job_id=None, name=None, page_number=None, page_size=None,
                 periodic=None, project_id=None, region_id=None, status=None):
        self.cluster_id = cluster_id  # type: str
        self.id = id  # type: str
        self.job_id = job_id  # type: str
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.periodic = periodic  # type: bool
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.id is not None:
            result['Id'] = self.id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.periodic is not None:
            result['Periodic'] = self.periodic
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Periodic') is not None:
            self.periodic = m.get('Periodic')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFlowsResponseBodyFlowFlow(TeaModel):
    def __init__(self, alert_conf=None, alert_ding_ding_group_biz_id=None, alert_user_group_biz_id=None,
                 category_id=None, cluster_id=None, create_cluster=None, cron_expr=None, description=None, end_schedule=None,
                 gmt_create=None, gmt_modified=None, graph=None, host_name=None, id=None, name=None, periodic=None,
                 project_id=None, start_schedule=None, status=None, type=None):
        self.alert_conf = alert_conf  # type: str
        self.alert_ding_ding_group_biz_id = alert_ding_ding_group_biz_id  # type: str
        self.alert_user_group_biz_id = alert_user_group_biz_id  # type: str
        self.category_id = category_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.create_cluster = create_cluster  # type: bool
        self.cron_expr = cron_expr  # type: str
        self.description = description  # type: str
        self.end_schedule = end_schedule  # type: long
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.graph = graph  # type: str
        self.host_name = host_name  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.periodic = periodic  # type: bool
        self.project_id = project_id  # type: str
        self.start_schedule = start_schedule  # type: long
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowsResponseBodyFlowFlow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.alert_ding_ding_group_biz_id is not None:
            result['AlertDingDingGroupBizId'] = self.alert_ding_ding_group_biz_id
        if self.alert_user_group_biz_id is not None:
            result['AlertUserGroupBizId'] = self.alert_user_group_biz_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_cluster is not None:
            result['CreateCluster'] = self.create_cluster
        if self.cron_expr is not None:
            result['CronExpr'] = self.cron_expr
        if self.description is not None:
            result['Description'] = self.description
        if self.end_schedule is not None:
            result['EndSchedule'] = self.end_schedule
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.graph is not None:
            result['Graph'] = self.graph
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.periodic is not None:
            result['Periodic'] = self.periodic
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.start_schedule is not None:
            result['StartSchedule'] = self.start_schedule
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('AlertDingDingGroupBizId') is not None:
            self.alert_ding_ding_group_biz_id = m.get('AlertDingDingGroupBizId')
        if m.get('AlertUserGroupBizId') is not None:
            self.alert_user_group_biz_id = m.get('AlertUserGroupBizId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateCluster') is not None:
            self.create_cluster = m.get('CreateCluster')
        if m.get('CronExpr') is not None:
            self.cron_expr = m.get('CronExpr')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndSchedule') is not None:
            self.end_schedule = m.get('EndSchedule')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Graph') is not None:
            self.graph = m.get('Graph')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Periodic') is not None:
            self.periodic = m.get('Periodic')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('StartSchedule') is not None:
            self.start_schedule = m.get('StartSchedule')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFlowsResponseBodyFlow(TeaModel):
    def __init__(self, flow=None):
        self.flow = flow  # type: list[ListFlowsResponseBodyFlowFlow]

    def validate(self):
        if self.flow:
            for k in self.flow:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowsResponseBodyFlow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Flow'] = []
        if self.flow is not None:
            for k in self.flow:
                result['Flow'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.flow = []
        if m.get('Flow') is not None:
            for k in m.get('Flow'):
                temp_model = ListFlowsResponseBodyFlowFlow()
                self.flow.append(temp_model.from_map(k))
        return self


class ListFlowsResponseBody(TeaModel):
    def __init__(self, flow=None, page_number=None, page_size=None, request_id=None, total=None):
        self.flow = flow  # type: ListFlowsResponseBodyFlow
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        if self.flow:
            self.flow.validate()

    def to_map(self):
        _map = super(ListFlowsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Flow') is not None:
            temp_model = ListFlowsResponseBodyFlow()
            self.flow = temp_model.from_map(m['Flow'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFlowsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFlowsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMainVersionsRequest(TeaModel):
    def __init__(self, region_id=None, resource_group_id=None, resource_owner_id=None):
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMainVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListMainVersionsResponseBodyMainVersionListClusterTypeInfoList(TeaModel):
    def __init__(self, cluster_type=None):
        self.cluster_type = cluster_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMainVersionsResponseBodyMainVersionListClusterTypeInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        return self


class ListMainVersionsResponseBodyMainVersionList(TeaModel):
    def __init__(self, cluster_type_info_list=None, extra_info=None, main_version_name=None, region_id=None):
        self.cluster_type_info_list = cluster_type_info_list  # type: list[ListMainVersionsResponseBodyMainVersionListClusterTypeInfoList]
        self.extra_info = extra_info  # type: str
        self.main_version_name = main_version_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.cluster_type_info_list:
            for k in self.cluster_type_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMainVersionsResponseBodyMainVersionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClusterTypeInfoList'] = []
        if self.cluster_type_info_list is not None:
            for k in self.cluster_type_info_list:
                result['ClusterTypeInfoList'].append(k.to_map() if k else None)
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.main_version_name is not None:
            result['MainVersionName'] = self.main_version_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cluster_type_info_list = []
        if m.get('ClusterTypeInfoList') is not None:
            for k in m.get('ClusterTypeInfoList'):
                temp_model = ListMainVersionsResponseBodyMainVersionListClusterTypeInfoList()
                self.cluster_type_info_list.append(temp_model.from_map(k))
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('MainVersionName') is not None:
            self.main_version_name = m.get('MainVersionName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListMainVersionsResponseBody(TeaModel):
    def __init__(self, main_version_list=None, request_id=None):
        self.main_version_list = main_version_list  # type: list[ListMainVersionsResponseBodyMainVersionList]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.main_version_list:
            for k in self.main_version_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMainVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MainVersionList'] = []
        if self.main_version_list is not None:
            for k in self.main_version_list:
                result['MainVersionList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.main_version_list = []
        if m.get('MainVersionList') is not None:
            for k in m.get('MainVersionList'):
                temp_model = ListMainVersionsResponseBodyMainVersionList()
                self.main_version_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListMainVersionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListMainVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMainVersionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListMainVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowRequest(TeaModel):
    def __init__(self, alert_conf=None, alert_ding_ding_group_biz_id=None, alert_user_group_biz_id=None,
                 application=None, cluster_id=None, create_cluster=None, cron_expr=None, description=None, end_schedule=None,
                 host_name=None, id=None, name=None, parent_category=None, parent_flow_list=None, periodic=None,
                 project_id=None, region_id=None, start_schedule=None, status=None):
        self.alert_conf = alert_conf  # type: str
        self.alert_ding_ding_group_biz_id = alert_ding_ding_group_biz_id  # type: str
        self.alert_user_group_biz_id = alert_user_group_biz_id  # type: str
        self.application = application  # type: str
        self.cluster_id = cluster_id  # type: str
        self.create_cluster = create_cluster  # type: bool
        self.cron_expr = cron_expr  # type: str
        self.description = description  # type: str
        self.end_schedule = end_schedule  # type: long
        self.host_name = host_name  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.parent_category = parent_category  # type: str
        self.parent_flow_list = parent_flow_list  # type: str
        self.periodic = periodic  # type: bool
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.start_schedule = start_schedule  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.alert_ding_ding_group_biz_id is not None:
            result['AlertDingDingGroupBizId'] = self.alert_ding_ding_group_biz_id
        if self.alert_user_group_biz_id is not None:
            result['AlertUserGroupBizId'] = self.alert_user_group_biz_id
        if self.application is not None:
            result['Application'] = self.application
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_cluster is not None:
            result['CreateCluster'] = self.create_cluster
        if self.cron_expr is not None:
            result['CronExpr'] = self.cron_expr
        if self.description is not None:
            result['Description'] = self.description
        if self.end_schedule is not None:
            result['EndSchedule'] = self.end_schedule
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_category is not None:
            result['ParentCategory'] = self.parent_category
        if self.parent_flow_list is not None:
            result['ParentFlowList'] = self.parent_flow_list
        if self.periodic is not None:
            result['Periodic'] = self.periodic
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_schedule is not None:
            result['StartSchedule'] = self.start_schedule
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('AlertDingDingGroupBizId') is not None:
            self.alert_ding_ding_group_biz_id = m.get('AlertDingDingGroupBizId')
        if m.get('AlertUserGroupBizId') is not None:
            self.alert_user_group_biz_id = m.get('AlertUserGroupBizId')
        if m.get('Application') is not None:
            self.application = m.get('Application')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateCluster') is not None:
            self.create_cluster = m.get('CreateCluster')
        if m.get('CronExpr') is not None:
            self.cron_expr = m.get('CronExpr')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndSchedule') is not None:
            self.end_schedule = m.get('EndSchedule')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentCategory') is not None:
            self.parent_category = m.get('ParentCategory')
        if m.get('ParentFlowList') is not None:
            self.parent_flow_list = m.get('ParentFlowList')
        if m.get('Periodic') is not None:
            self.periodic = m.get('Periodic')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartSchedule') is not None:
            self.start_schedule = m.get('StartSchedule')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyFlowResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowResponseBody, self).to_map()
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


class ModifyFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowCategoryRequest(TeaModel):
    def __init__(self, id=None, name=None, parent_id=None, project_id=None, region_id=None):
        self.id = id  # type: str
        self.name = name  # type: str
        self.parent_id = parent_id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyFlowCategoryResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowCategoryResponseBody, self).to_map()
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


class ModifyFlowCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyFlowCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFlowCategoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyFlowCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowForWebRequest(TeaModel):
    def __init__(self, alert_conf=None, alert_ding_ding_group_biz_id=None, alert_user_group_biz_id=None,
                 cluster_id=None, create_cluster=None, cron_expr=None, description=None, end_schedule=None, graph=None,
                 host_name=None, id=None, name=None, namespace=None, parent_category=None, parent_flow_list=None,
                 periodic=None, project_id=None, region_id=None, start_schedule=None, status=None):
        self.alert_conf = alert_conf  # type: str
        self.alert_ding_ding_group_biz_id = alert_ding_ding_group_biz_id  # type: str
        self.alert_user_group_biz_id = alert_user_group_biz_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.create_cluster = create_cluster  # type: bool
        self.cron_expr = cron_expr  # type: str
        self.description = description  # type: str
        self.end_schedule = end_schedule  # type: long
        self.graph = graph  # type: str
        self.host_name = host_name  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.namespace = namespace  # type: str
        self.parent_category = parent_category  # type: str
        self.parent_flow_list = parent_flow_list  # type: str
        self.periodic = periodic  # type: bool
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.start_schedule = start_schedule  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowForWebRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.alert_ding_ding_group_biz_id is not None:
            result['AlertDingDingGroupBizId'] = self.alert_ding_ding_group_biz_id
        if self.alert_user_group_biz_id is not None:
            result['AlertUserGroupBizId'] = self.alert_user_group_biz_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_cluster is not None:
            result['CreateCluster'] = self.create_cluster
        if self.cron_expr is not None:
            result['CronExpr'] = self.cron_expr
        if self.description is not None:
            result['Description'] = self.description
        if self.end_schedule is not None:
            result['EndSchedule'] = self.end_schedule
        if self.graph is not None:
            result['Graph'] = self.graph
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.parent_category is not None:
            result['ParentCategory'] = self.parent_category
        if self.parent_flow_list is not None:
            result['ParentFlowList'] = self.parent_flow_list
        if self.periodic is not None:
            result['Periodic'] = self.periodic
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_schedule is not None:
            result['StartSchedule'] = self.start_schedule
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('AlertDingDingGroupBizId') is not None:
            self.alert_ding_ding_group_biz_id = m.get('AlertDingDingGroupBizId')
        if m.get('AlertUserGroupBizId') is not None:
            self.alert_user_group_biz_id = m.get('AlertUserGroupBizId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateCluster') is not None:
            self.create_cluster = m.get('CreateCluster')
        if m.get('CronExpr') is not None:
            self.cron_expr = m.get('CronExpr')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndSchedule') is not None:
            self.end_schedule = m.get('EndSchedule')
        if m.get('Graph') is not None:
            self.graph = m.get('Graph')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ParentCategory') is not None:
            self.parent_category = m.get('ParentCategory')
        if m.get('ParentFlowList') is not None:
            self.parent_flow_list = m.get('ParentFlowList')
        if m.get('Periodic') is not None:
            self.periodic = m.get('Periodic')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartSchedule') is not None:
            self.start_schedule = m.get('StartSchedule')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyFlowForWebResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowForWebResponseBody, self).to_map()
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


class ModifyFlowForWebResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyFlowForWebResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFlowForWebResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyFlowForWebResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowJobRequestResourceList(TeaModel):
    def __init__(self, alias=None, path=None):
        self.alias = alias  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowJobRequestResourceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ModifyFlowJobRequest(TeaModel):
    def __init__(self, alert_conf=None, cluster_id=None, custom_variables=None, description=None, env_conf=None,
                 fail_act=None, id=None, knox_password=None, knox_user=None, mode=None, monitor_conf=None, name=None,
                 param_conf=None, params=None, project_id=None, region_id=None, resource_list=None, retry_policy=None,
                 run_conf=None):
        self.alert_conf = alert_conf  # type: str
        self.cluster_id = cluster_id  # type: str
        self.custom_variables = custom_variables  # type: str
        self.description = description  # type: str
        self.env_conf = env_conf  # type: str
        self.fail_act = fail_act  # type: str
        self.id = id  # type: str
        self.knox_password = knox_password  # type: str
        self.knox_user = knox_user  # type: str
        self.mode = mode  # type: str
        self.monitor_conf = monitor_conf  # type: str
        self.name = name  # type: str
        self.param_conf = param_conf  # type: str
        self.params = params  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_list = resource_list  # type: list[ModifyFlowJobRequestResourceList]
        self.retry_policy = retry_policy  # type: str
        self.run_conf = run_conf  # type: str

    def validate(self):
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyFlowJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.custom_variables is not None:
            result['CustomVariables'] = self.custom_variables
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        if self.fail_act is not None:
            result['FailAct'] = self.fail_act
        if self.id is not None:
            result['Id'] = self.id
        if self.knox_password is not None:
            result['KnoxPassword'] = self.knox_password
        if self.knox_user is not None:
            result['KnoxUser'] = self.knox_user
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.monitor_conf is not None:
            result['MonitorConf'] = self.monitor_conf
        if self.name is not None:
            result['Name'] = self.name
        if self.param_conf is not None:
            result['ParamConf'] = self.param_conf
        if self.params is not None:
            result['Params'] = self.params
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['ResourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['ResourceList'].append(k.to_map() if k else None)
        if self.retry_policy is not None:
            result['RetryPolicy'] = self.retry_policy
        if self.run_conf is not None:
            result['RunConf'] = self.run_conf
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CustomVariables') is not None:
            self.custom_variables = m.get('CustomVariables')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        if m.get('FailAct') is not None:
            self.fail_act = m.get('FailAct')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KnoxPassword') is not None:
            self.knox_password = m.get('KnoxPassword')
        if m.get('KnoxUser') is not None:
            self.knox_user = m.get('KnoxUser')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('MonitorConf') is not None:
            self.monitor_conf = m.get('MonitorConf')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamConf') is not None:
            self.param_conf = m.get('ParamConf')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k in m.get('ResourceList'):
                temp_model = ModifyFlowJobRequestResourceList()
                self.resource_list.append(temp_model.from_map(k))
        if m.get('RetryPolicy') is not None:
            self.retry_policy = m.get('RetryPolicy')
        if m.get('RunConf') is not None:
            self.run_conf = m.get('RunConf')
        return self


class ModifyFlowJobResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowJobResponseBody, self).to_map()
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


class ModifyFlowJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyFlowJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFlowJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyFlowJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowProjectRequest(TeaModel):
    def __init__(self, description=None, name=None, project_id=None, region_id=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyFlowProjectResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowProjectResponseBody, self).to_map()
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


class ModifyFlowProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyFlowProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFlowProjectResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyFlowProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowProjectClusterSettingRequest(TeaModel):
    def __init__(self, cluster_id=None, default_queue=None, default_user=None, host_list=None, project_id=None,
                 queue_list=None, region_id=None, user_list=None):
        self.cluster_id = cluster_id  # type: str
        self.default_queue = default_queue  # type: str
        self.default_user = default_user  # type: str
        self.host_list = host_list  # type: list[str]
        self.project_id = project_id  # type: str
        self.queue_list = queue_list  # type: list[str]
        self.region_id = region_id  # type: str
        self.user_list = user_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowProjectClusterSettingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.default_queue is not None:
            result['DefaultQueue'] = self.default_queue
        if self.default_user is not None:
            result['DefaultUser'] = self.default_user
        if self.host_list is not None:
            result['HostList'] = self.host_list
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.queue_list is not None:
            result['QueueList'] = self.queue_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_list is not None:
            result['UserList'] = self.user_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DefaultQueue') is not None:
            self.default_queue = m.get('DefaultQueue')
        if m.get('DefaultUser') is not None:
            self.default_user = m.get('DefaultUser')
        if m.get('HostList') is not None:
            self.host_list = m.get('HostList')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('QueueList') is not None:
            self.queue_list = m.get('QueueList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserList') is not None:
            self.user_list = m.get('UserList')
        return self


class ModifyFlowProjectClusterSettingResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowProjectClusterSettingResponseBody, self).to_map()
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


class ModifyFlowProjectClusterSettingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyFlowProjectClusterSettingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFlowProjectClusterSettingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyFlowProjectClusterSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowVariableCollectionRequest(TeaModel):
    def __init__(self, data=None, region_id=None, resource_group_id=None):
        self.data = data  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowVariableCollectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ModifyFlowVariableCollectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFlowVariableCollectionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyFlowVariableCollectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyFlowVariableCollectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFlowVariableCollectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyFlowVariableCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseClusterRequest(TeaModel):
    def __init__(self, force_release=None, id=None, region_id=None, resource_owner_id=None):
        self.force_release = force_release  # type: bool
        self.id = id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_release is not None:
            result['ForceRelease'] = self.force_release
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForceRelease') is not None:
            self.force_release = m.get('ForceRelease')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ReleaseClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReleaseClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleaseClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RerunFlowRequest(TeaModel):
    def __init__(self, flow_instance_id=None, project_id=None, re_run_fail=None, region_id=None):
        self.flow_instance_id = flow_instance_id  # type: str
        self.project_id = project_id  # type: str
        self.re_run_fail = re_run_fail  # type: bool
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RerunFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.re_run_fail is not None:
            result['ReRunFail'] = self.re_run_fail
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ReRunFail') is not None:
            self.re_run_fail = m.get('ReRunFail')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RerunFlowResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RerunFlowResponseBody, self).to_map()
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


class RerunFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RerunFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RerunFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RerunFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreFlowEntitySnapshotRequest(TeaModel):
    def __init__(self, entity_id=None, entity_type=None, operator_id=None, region_id=None, resource_owner_id=None,
                 revision=None):
        self.entity_id = entity_id  # type: str
        self.entity_type = entity_type  # type: str
        self.operator_id = operator_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.revision = revision  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreFlowEntitySnapshotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.revision is not None:
            result['Revision'] = self.revision
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Revision') is not None:
            self.revision = m.get('Revision')
        return self


class RestoreFlowEntitySnapshotResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestoreFlowEntitySnapshotResponseBody, self).to_map()
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


class RestoreFlowEntitySnapshotResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RestoreFlowEntitySnapshotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestoreFlowEntitySnapshotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RestoreFlowEntitySnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeFlowRequest(TeaModel):
    def __init__(self, flow_instance_id=None, project_id=None, region_id=None):
        self.flow_instance_id = flow_instance_id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ResumeFlowResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeFlowResponseBody, self).to_map()
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


class ResumeFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResumeFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResumeFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartFlowRequest(TeaModel):
    def __init__(self, flow_instance_id=None, project_id=None, region_id=None):
        self.flow_instance_id = flow_instance_id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartFlowResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartFlowResponseBody, self).to_map()
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


class StartFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitFlowRequest(TeaModel):
    def __init__(self, conf=None, flow_id=None, project_id=None, region_id=None):
        self.conf = conf  # type: str
        self.flow_id = flow_id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conf is not None:
            result['Conf'] = self.conf
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Conf') is not None:
            self.conf = m.get('Conf')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SubmitFlowResponseBody(TeaModel):
    def __init__(self, data=None, id=None, instance_id=None, request_id=None):
        self.data = data  # type: str
        self.id = id  # type: str
        self.instance_id = instance_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitFlowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitFlowJobRequest(TeaModel):
    def __init__(self, cluster_id=None, conf=None, host_name=None, job_id=None, project_id=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.conf = conf  # type: str
        self.host_name = host_name  # type: str
        self.job_id = job_id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitFlowJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.conf is not None:
            result['Conf'] = self.conf
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Conf') is not None:
            self.conf = m.get('Conf')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SubmitFlowJobResponseBody(TeaModel):
    def __init__(self, id=None, request_id=None):
        self.id = id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitFlowJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitFlowJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitFlowJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitFlowJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitFlowJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendFlowRequest(TeaModel):
    def __init__(self, flow_instance_id=None, project_id=None, region_id=None):
        self.flow_instance_id = flow_instance_id  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SuspendFlowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SuspendFlowResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SuspendFlowResponseBody, self).to_map()
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


class SuspendFlowResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SuspendFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SuspendFlowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SuspendFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


