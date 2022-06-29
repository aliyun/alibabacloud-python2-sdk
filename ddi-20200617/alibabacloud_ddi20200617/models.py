# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CloneFlowJobRequest(TeaModel):
    def __init__(self, id=None, name=None, project_id=None, region_id=None):
        # 克隆的目标作业ID。您可以调用ListFlowJob查看。
        self.id = id  # type: str
        # 克隆的目标作业名称。
        self.name = name  # type: str
        # 克隆的目标作业所属项目。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id  # type: str
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
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
        # 新产生的作业ID。
        self.id = id  # type: str
        # 请求ID。
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloneFlowJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneFlowJobResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateClusterV2ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFlowCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFlowCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowJobRequestResourceList(TeaModel):
    def __init__(self, alias=None, path=None):
        # 保留参数。
        self.alias = alias  # type: str
        # 保留参数。
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
        # 是否临时查询。
        self.adhoc = adhoc  # type: bool
        # 保留参数。
        self.alert_conf = alert_conf  # type: str
        # 保留参数。
        self.client_token = client_token  # type: str
        # 集群ID。您可以调用ListClusters查看集群的ID。
        self.cluster_id = cluster_id  # type: str
        # 自定义变量。
        self.custom_variables = custom_variables  # type: str
        # 作业的描述。
        self.description = description  # type: str
        # 环境变量设置。
        self.env_conf = env_conf  # type: str
        # 失败策略，可能的取值：CONTINUE（提过本次作业），STOP（停止作业）
        self.fail_act = fail_act  # type: str
        # 模型模式，取值如下：  YARN：将作业包装成一个Launcher提交至YARN中执行，LOCAL：作业直接在机器上以进程方式运行。
        self.mode = mode  # type: str
        # 监控配置，仅SPARK_STREAMING类型作业支持监控配置。
        self.monitor_conf = monitor_conf  # type: str
        # 作业的名称。
        self.name = name  # type: str
        # 参数设置。
        self.param_conf = param_conf  # type: str
        # 作业内容。
        self.params = params  # type: str
        # 父目录ID。您可以调用DescribeFlowCategory查看。
        self.parent_category = parent_category  # type: str
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id  # type: str
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
        self.region_id = region_id  # type: str
        # 保留参数。
        self.resource_list = resource_list  # type: list[CreateFlowJobRequestResourceList]
        # 重试策略，保留参数。
        self.retry_policy = retry_policy  # type: str
        # 运行配置，取值如下：priority（优先级），userName（任务的Linux提交用户），memory（内存，单位为MB），cores（核数）
        self.run_conf = run_conf  # type: str
        # 作业的类型，可能的取值有：SPARK，SPARK_STREAMING，ZEPPELIN
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
        # 作业ID。
        self.id = id  # type: str
        # 请求ID。
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFlowJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFlowJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowProjectRequest(TeaModel):
    def __init__(self, client_token=None, description=None, name=None, product_type=None, region_id=None,
                 resource_group_id=None):
        self.client_token = client_token  # type: str
        # 项目描述
        self.description = description  # type: str
        # 项目名称
        self.name = name  # type: str
        # 产品类型，固定值DATABRICKS_DATAINSIGHT
        self.product_type = product_type  # type: str
        # 地域ID
        self.region_id = region_id  # type: str
        # 资源组ID
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
        # 项目ID
        self.id = id  # type: str
        # 请求ID
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFlowProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFlowProjectResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFlowProjectUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFlowProjectUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLibraryRequest(TeaModel):
    def __init__(self, client_token=None, library_version=None, name=None, properties=None, region_id=None,
                 resource_owner_id=None, scope=None, source_location=None, source_type=None, type=None):
        self.client_token = client_token  # type: str
        self.library_version = library_version  # type: str
        self.name = name  # type: str
        self.properties = properties  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.scope = scope  # type: str
        self.source_location = source_location  # type: str
        self.source_type = source_type  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLibraryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.library_version is not None:
            result['LibraryVersion'] = self.library_version
        if self.name is not None:
            result['Name'] = self.name
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.source_location is not None:
            result['SourceLocation'] = self.source_location
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('LibraryVersion') is not None:
            self.library_version = m.get('LibraryVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SourceLocation') is not None:
            self.source_location = m.get('SourceLocation')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateLibraryResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLibraryResponseBody, self).to_map()
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


class CreateLibraryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLibraryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLibraryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLibraryResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
    def __init__(self, flow_id=None, job_id=None, request_id=None, result=None):
        self.flow_id = flow_id  # type: str
        self.job_id = job_id  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowCategoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteFlowCategoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFlowCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFlowCategoryResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFlowProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFlowProjectResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFlowProjectUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFlowProjectUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLibrariesRequest(TeaModel):
    def __init__(self, library_biz_id_list=None, region_id=None, resource_owner_id=None):
        self.library_biz_id_list = library_biz_id_list  # type: list[str]
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLibrariesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.library_biz_id_list is not None:
            result['LibraryBizIdList'] = self.library_biz_id_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LibraryBizIdList') is not None:
            self.library_biz_id_list = m.get('LibraryBizIdList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteLibrariesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLibrariesResponseBody, self).to_map()
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


class DeleteLibrariesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteLibrariesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteLibrariesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteLibrariesResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeClusterV2ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFlowCategoryTreeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFlowCategoryTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowJobRequest(TeaModel):
    def __init__(self, id=None, project_id=None, region_id=None):
        # 作业ID。您可以调用ListFlowJob查看作业ID。
        self.id = id  # type: str
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id  # type: str
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
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
        # 保留参数。
        self.alias = alias  # type: str
        # 保留参数。
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
        # 是否临时查询。
        self.adhoc = adhoc  # type: str
        # 报警配置。
        self.alert_conf = alert_conf  # type: str
        # 作业所在目录ID。
        self.category_id = category_id  # type: str
        # 自定义变量。
        self.custom_variables = custom_variables  # type: str
        # 作业的描述。
        self.description = description  # type: str
        # 保留参数。
        self.edit_lock_detail = edit_lock_detail  # type: str
        # 环境变量设置。
        self.env_conf = env_conf  # type: str
        # 失败策略，可能的取值：CONTINUE（提过本次作业），STOP（停止作业）
        self.fail_act = fail_act  # type: str
        # 创建时间。
        self.gmt_create = gmt_create  # type: long
        # 最后修改时间。
        self.gmt_modified = gmt_modified  # type: long
        # 作业ID。
        self.id = id  # type: str
        # Knox的用户密码，执行Zeppelin Notebook时必须提供。
        self.knox_password = knox_password  # type: str
        # Knox的用户名，执行Zeppelin Notebook时必须提供。
        self.knox_user = knox_user  # type: str
        # 最后一次执行的实例ID。
        self.last_instance_id = last_instance_id  # type: str
        # 最大重试次数。
        self.max_retry = max_retry  # type: int
        # 保留参数。
        self.max_running_time_sec = max_running_time_sec  # type: long
        # 模型模式，取值如下：  YARN：将作业包装成一个Launcher提交至YARN中执行，LOCAL：作业直接在机器上以进程方式运行。
        self.mode = mode  # type: str
        # 监控配置，仅SPARK_STREAMING类型作业支持监控配置。
        self.monitor_conf = monitor_conf  # type: str
        # 作业名称。
        self.name = name  # type: str
        # 参数设置。
        self.param_conf = param_conf  # type: str
        # 作业内容。
        self.params = params  # type: str
        # 请求ID。
        self.request_id = request_id  # type: str
        self.resource_list = resource_list  # type: DescribeFlowJobResponseBodyResourceList
        # 重试间隔 0~300（秒）。
        self.retry_interval = retry_interval  # type: long
        # 重试策略，保留参数。
        self.retry_policy = retry_policy  # type: str
        # 运行配置，取值如下：priority（优先级），userName（任务的Linux提交用户），memory（内存，单位为MB），cores（核数）
        self.run_conf = run_conf  # type: str
        # 作业的类型，可能的取值有：SPARK，SPARK_STREAMING，ZEPPELIN
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFlowJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFlowNodeInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFlowNodeInstanceResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeFlowProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFlowProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLibraryDetailRequest(TeaModel):
    def __init__(self, library_biz_id=None, region_id=None, resource_owner_id=None):
        self.library_biz_id = library_biz_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLibraryDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.library_biz_id is not None:
            result['LibraryBizId'] = self.library_biz_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LibraryBizId') is not None:
            self.library_biz_id = m.get('LibraryBizId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeLibraryDetailResponseBody(TeaModel):
    def __init__(self, biz_id=None, create_time=None, library_version=None, name=None, properties=None,
                 request_id=None, scope=None, source_location=None, source_type=None, type=None, user_id=None):
        self.biz_id = biz_id  # type: str
        self.create_time = create_time  # type: long
        self.library_version = library_version  # type: str
        self.name = name  # type: str
        self.properties = properties  # type: str
        self.request_id = request_id  # type: str
        self.scope = scope  # type: str
        self.source_location = source_location  # type: str
        self.source_type = source_type  # type: str
        self.type = type  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLibraryDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.library_version is not None:
            result['LibraryVersion'] = self.library_version
        if self.name is not None:
            result['Name'] = self.name
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.source_location is not None:
            result['SourceLocation'] = self.source_location
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LibraryVersion') is not None:
            self.library_version = m.get('LibraryVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SourceLocation') is not None:
            self.source_location = m.get('SourceLocation')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeLibraryDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLibraryDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLibraryDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLibraryDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLibraryInstallTaskDetailRequest(TeaModel):
    def __init__(self, region_id=None, resource_owner_id=None, task_biz_id=None):
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_biz_id = task_biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLibraryInstallTaskDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_biz_id is not None:
            result['TaskBizId'] = self.task_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskBizId') is not None:
            self.task_biz_id = m.get('TaskBizId')
        return self


class DescribeLibraryInstallTaskDetailResponseBody(TeaModel):
    def __init__(self, cluster_biz_id=None, detail=None, end_time=None, execute_time=None, hostname=None,
                 library_biz_id=None, request_id=None, start_time=None, task_group_id=None, task_id=None, task_process=None,
                 task_status=None, task_type=None):
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.detail = detail  # type: str
        self.end_time = end_time  # type: long
        self.execute_time = execute_time  # type: long
        self.hostname = hostname  # type: str
        self.library_biz_id = library_biz_id  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: long
        self.task_group_id = task_group_id  # type: str
        self.task_id = task_id  # type: str
        self.task_process = task_process  # type: int
        self.task_status = task_status  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLibraryInstallTaskDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.library_biz_id is not None:
            result['LibraryBizId'] = self.library_biz_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_group_id is not None:
            result['TaskGroupId'] = self.task_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_process is not None:
            result['TaskProcess'] = self.task_process
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('LibraryBizId') is not None:
            self.library_biz_id = m.get('LibraryBizId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskGroupId') is not None:
            self.task_group_id = m.get('TaskGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskProcess') is not None:
            self.task_process = m.get('TaskProcess')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeLibraryInstallTaskDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLibraryInstallTaskDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLibraryInstallTaskDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLibraryInstallTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallLibrariesRequest(TeaModel):
    def __init__(self, cluster_biz_id_list=None, library_biz_id=None, region_id=None, resource_owner_id=None):
        self.cluster_biz_id_list = cluster_biz_id_list  # type: list[str]
        self.library_biz_id = library_biz_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallLibrariesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id_list is not None:
            result['ClusterBizIdList'] = self.cluster_biz_id_list
        if self.library_biz_id is not None:
            result['LibraryBizId'] = self.library_biz_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizIdList') is not None:
            self.cluster_biz_id_list = m.get('ClusterBizIdList')
        if m.get('LibraryBizId') is not None:
            self.library_biz_id = m.get('LibraryBizId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class InstallLibrariesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallLibrariesResponseBody, self).to_map()
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


class InstallLibrariesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InstallLibrariesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InstallLibrariesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InstallLibrariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KillFlowJobRequest(TeaModel):
    def __init__(self, job_instance_id=None, project_id=None, region_id=None):
        # 作业实例ID。您可以调用DescribeFlowJob查看作业实例ID。
        self.job_instance_id = job_instance_id  # type: str
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id  # type: str
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
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
        # 返回执行结果，包含如下：true（执行成功），false（执行失败）
        self.data = data  # type: bool
        # 请求ID。
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: KillFlowJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowRequest(TeaModel):
    def __init__(self, cluster_id=None, id=None, job_id=None, name=None, page_number=None, page_size=None,
                 periodic=None, project_id=None, region_id=None, status=None):
        # 集群ID。您可以调用ListClusters查看集群的ID。
        self.cluster_id = cluster_id  # type: str
        # 工作流ID。您可以调用ListFlowInstance查看工作流ID。
        self.id = id  # type: str
        # 作业ID。您可以调用ListFlowJob查看。
        self.job_id = job_id  # type: str
        # 工作流名称。您可以调用ListFlowInstance查看。
        self.name = name  # type: str
        # 页码。
        self.page_number = page_number  # type: int
        # 每页查询数量。
        self.page_size = page_size  # type: int
        # 是否调度。
        self.periodic = periodic  # type: bool
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id  # type: str
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
        self.region_id = region_id  # type: str
        # 状态：  STOP_SCHEDULE（停止调度） UNDER_SCHEDULE（调度中）
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
        # 工作流列表
        self.flow = flow  # type: ListFlowResponseBodyFlow
        # 页码。
        self.page_number = page_number  # type: int
        # 每页数量。
        self.page_size = page_size  # type: int
        # 请求ID。
        self.request_id = request_id  # type: str
        # 总数。
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowJobHistoryRequest(TeaModel):
    def __init__(self, id=None, instance_id=None, job_type=None, page_number=None, page_size=None, project_id=None,
                 region_id=None, status_list=None, time_range=None):
        # 作业ID。您可以调用ListFlowJob查看作业ID。
        self.id = id  # type: str
        # 作业实例ID。您可以调用DescribeFlowJob查看作业实例ID。
        self.instance_id = instance_id  # type: str
        # 作业的类型，可能的取值有：SPARK，SPARK_STREAMING，ZEPPELIN
        self.job_type = job_type  # type: str
        # 当前页码。
        self.page_number = page_number  # type: int
        # 分页查询时每页行数。
        self.page_size = page_size  # type: int
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id  # type: str
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
        self.region_id = region_id  # type: str
        # 状态列表。取值如下：SUBMITTED, RUNNING, SUCCESS, FAILED, KILL_FAILED, KILL_SUCCESS
        self.status_list = status_list  # type: list[str]
        # 查询的时间范围参数，参数列表：type: range，from: 开始时间（long型时间戳），to: 结束时间（long型时间戳）
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
        # 集群ID。
        self.cluster_id = cluster_id  # type: str
        # 运行结束时间。
        self.end_time = end_time  # type: long
        # 环境变量设置。
        self.env_conf = env_conf  # type: str
        # 启动器的application的ID。
        self.external_id = external_id  # type: str
        # 外部信息。例如，运行作业的错误诊断信息。
        self.external_info = external_info  # type: str
        # 实例对应的Container的状态：SUBMITTED, RUNNING, SUCCESS, FAIL, KILL_FAIL, KILL_SUCCESS
        self.external_status = external_status  # type: str
        # 失败策略，可能的取值：CONTINUE（提过本次作业），STOP（停止作业）
        self.fail_act = fail_act  # type: str
        # 创建时间。
        self.gmt_create = gmt_create  # type: long
        # 创建时间。
        self.gmt_modified = gmt_modified  # type: long
        # 保留参数。
        self.host_name = host_name  # type: str
        # 作业实例ID。
        self.id = id  # type: str
        # 作业ID。
        self.job_id = job_id  # type: str
        # 作业名称。
        self.job_name = job_name  # type: str
        # 作业内容。
        self.job_params = job_params  # type: str
        # 作业类型。
        self.job_type = job_type  # type: str
        # 最大重试次数。
        self.max_retry = max_retry  # type: int
        # 保留参数。
        self.node_name = node_name  # type: str
        # 参数设置。
        self.param_conf = param_conf  # type: str
        # 项目ID。
        self.project_id = project_id  # type: str
        # 重试次数。
        self.retries = retries  # type: int
        # 重试间隔 0-300（秒）。
        self.retry_interval = retry_interval  # type: long
        # 运行配置，取值如下：priority（优先级），userName（任务的Linux提交用户），memory（内存，单位为MB），cores（核数）
        self.run_conf = run_conf  # type: str
        # 运行开始时间。
        self.start_time = start_time  # type: long
        # 实例的执行状态：PREP：准备启动，SUBMITTING：提交中，RUNNING：运行中DONE：已完成，OK：执行成功，FAILED：执行失败，KILLED：已终止，KILL_FAILED：终止失败，START_RETRY：开始重试
        self.status = status  # type: str
        # 节点类型：JOB：作业，CLUSTER：集群，START：开始，END：结束
        self.type = type  # type: str
        # 是否结束。
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
        # 作业实例列表。
        self.node_instances = node_instances  # type: ListFlowJobHistoryResponseBodyNodeInstances
        # 当前页码。
        self.page_number = page_number  # type: int
        # 分页查询时设置的每页行数。
        self.page_size = page_size  # type: int
        # 请求ID。
        self.request_id = request_id  # type: str
        # 记录总数。
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFlowJobHistoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFlowJobHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowJobsRequest(TeaModel):
    def __init__(self, adhoc=None, exact_name=None, id=None, name=None, page_number=None, page_size=None,
                 project_id=None, region_id=None, type=None):
        # 是否为临时查询。用于过滤作业。
        self.adhoc = adhoc  # type: bool
        self.exact_name = exact_name  # type: str
        # 作业ID。您可以调用ListFlowJob查看作业ID。
        self.id = id  # type: str
        # 作业名称。
        self.name = name  # type: str
        # 当前页数。
        self.page_number = page_number  # type: int
        # 每页的作业数量。
        self.page_size = page_size  # type: int
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id  # type: str
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
        self.region_id = region_id  # type: str
        # 作业类型。用于过滤作业，支持的类型有：SPARK，SPARK_STREAMING，ZEPPELIN。
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
        if self.exact_name is not None:
            result['ExactName'] = self.exact_name
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
        if m.get('ExactName') is not None:
            self.exact_name = m.get('ExactName')
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
        # 保留参数。
        self.alias = alias  # type: str
        # 保留参数。
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
        # 是否临时查询。
        self.adhoc = adhoc  # type: str
        # 报警配置。
        self.alert_conf = alert_conf  # type: str
        # 作业所在目录ID。
        self.category_id = category_id  # type: str
        # 自定义变量。
        self.custom_variables = custom_variables  # type: str
        # 作业的描述。
        self.description = description  # type: str
        # 环境变量设置。
        self.env_conf = env_conf  # type: str
        # 失败策略，可能的取值：CONTINUE（提过本次作业），STOP（停止作业）
        self.fail_act = fail_act  # type: str
        # 创建时间。
        self.gmt_create = gmt_create  # type: long
        # 最后修改时间。
        self.gmt_modified = gmt_modified  # type: long
        # 作业ID。
        self.id = id  # type: str
        # 最后一次执行的实例ID。
        self.last_instance_detail = last_instance_detail  # type: str
        # 最大重试次数。
        self.max_retry = max_retry  # type: int
        # 模型模式，取值如下：  YARN：将作业包装成一个Launcher提交至YARN中执行，LOCAL：作业直接在机器上以进程方式运行。
        self.mode = mode  # type: str
        # 监控配置，仅SPARK_STREAMING类型作业支持监控配置。
        self.monitor_conf = monitor_conf  # type: str
        # 作业名称。
        self.name = name  # type: str
        # 参数设置。
        self.param_conf = param_conf  # type: str
        # 作业内容。
        self.params = params  # type: str
        self.resource_list = resource_list  # type: ListFlowJobsResponseBodyJobListJobResourceList
        # 重试间隔 0~300（秒）。
        self.retry_interval = retry_interval  # type: long
        # 运行配置，取值如下：priority（优先级），userName（任务的Linux提交用户），memory（内存，单位为MB），cores（核数）
        self.run_conf = run_conf  # type: str
        # 作业的类型，可能的取值有：SPARK，SPARK_STREAMING，ZEPPELIN
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
        # 当前页数。
        self.page_number = page_number  # type: int
        # 每页的作业数量。
        self.page_size = page_size  # type: int
        # 请求ID。
        self.request_id = request_id  # type: str
        # 作业数量。
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFlowJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFlowJobsResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFlowProjectUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFlowProjectUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowProjectsRequest(TeaModel):
    def __init__(self, name=None, page_number=None, page_size=None, product_type=None, project_id=None,
                 region_id=None, resource_group_id=None):
        # 项目名称，用于过滤项目
        self.name = name  # type: str
        # 页码，用于分页
        self.page_number = page_number  # type: int
        # 每页数量
        self.page_size = page_size  # type: int
        # 产品类型。固定值DATABIRCKS_DATAINSIGHT
        self.product_type = product_type  # type: str
        # 项目ID。您可以调用ListFlowProjects查看项目的ID
        self.project_id = project_id  # type: str
        # 地域ID
        self.region_id = region_id  # type: str
        # 资源组ID
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
        # 项目描述
        self.description = description  # type: str
        # 创建时间戳
        self.gmt_create = gmt_create  # type: long
        # 修改时间戳
        self.gmt_modified = gmt_modified  # type: long
        # 项目ID
        self.id = id  # type: str
        # 项目名称
        self.name = name  # type: str
        # 主账号ID
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
        # 页码
        self.page_number = page_number  # type: int
        # 每页数量
        self.page_size = page_size  # type: int
        # 项目列表
        self.projects = projects  # type: ListFlowProjectsResponseBodyProjects
        # 请求ID
        self.request_id = request_id  # type: str
        # 总数
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFlowProjectsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFlowProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLibrariesRequest(TeaModel):
    def __init__(self, cluster_biz_id=None, current_size=None, limit=None, order_field=None, order_mode=None,
                 page_count=None, page_number=None, page_size=None, region_id=None, resource_owner_id=None):
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.current_size = current_size  # type: int
        self.limit = limit  # type: int
        self.order_field = order_field  # type: str
        self.order_mode = order_mode  # type: str
        self.page_count = page_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLibrariesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.current_size is not None:
            result['CurrentSize'] = self.current_size
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('CurrentSize') is not None:
            self.current_size = m.get('CurrentSize')
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
        return self


class ListLibrariesResponseBodyItemsItem(TeaModel):
    def __init__(self, biz_id=None, create_time=None, library_version=None, name=None, properties=None, scope=None,
                 source_location=None, source_type=None, type=None, user_id=None):
        self.biz_id = biz_id  # type: str
        self.create_time = create_time  # type: long
        self.library_version = library_version  # type: str
        self.name = name  # type: str
        self.properties = properties  # type: str
        self.scope = scope  # type: str
        self.source_location = source_location  # type: str
        self.source_type = source_type  # type: str
        self.type = type  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLibrariesResponseBodyItemsItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.library_version is not None:
            result['LibraryVersion'] = self.library_version
        if self.name is not None:
            result['Name'] = self.name
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.source_location is not None:
            result['SourceLocation'] = self.source_location
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LibraryVersion') is not None:
            self.library_version = m.get('LibraryVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SourceLocation') is not None:
            self.source_location = m.get('SourceLocation')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListLibrariesResponseBodyItems(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[ListLibrariesResponseBodyItemsItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLibrariesResponseBodyItems, self).to_map()
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
                temp_model = ListLibrariesResponseBodyItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class ListLibrariesResponseBody(TeaModel):
    def __init__(self, items=None, next_token=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.items = items  # type: ListLibrariesResponseBodyItems
        self.next_token = next_token  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(ListLibrariesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
            temp_model = ListLibrariesResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLibrariesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLibrariesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLibrariesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLibrariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLibraryInstallTasksRequest(TeaModel):
    def __init__(self, cluster_biz_id=None, current_size=None, library_biz_id=None, limit=None, order_field=None,
                 order_mode=None, page_count=None, page_number=None, page_size=None, region_id=None, resource_owner_id=None):
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.current_size = current_size  # type: int
        self.library_biz_id = library_biz_id  # type: str
        self.limit = limit  # type: int
        self.order_field = order_field  # type: str
        self.order_mode = order_mode  # type: str
        self.page_count = page_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLibraryInstallTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.current_size is not None:
            result['CurrentSize'] = self.current_size
        if self.library_biz_id is not None:
            result['LibraryBizId'] = self.library_biz_id
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('CurrentSize') is not None:
            self.current_size = m.get('CurrentSize')
        if m.get('LibraryBizId') is not None:
            self.library_biz_id = m.get('LibraryBizId')
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
        return self


class ListLibraryInstallTasksResponseBodyItemsItem(TeaModel):
    def __init__(self, cluster_biz_id=None, detail=None, end_time=None, execute_time=None, hostname=None,
                 library_biz_id=None, start_time=None, task_group_id=None, task_id=None, task_process=None, task_status=None,
                 task_type=None):
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.detail = detail  # type: str
        self.end_time = end_time  # type: long
        self.execute_time = execute_time  # type: long
        self.hostname = hostname  # type: str
        self.library_biz_id = library_biz_id  # type: str
        self.start_time = start_time  # type: long
        self.task_group_id = task_group_id  # type: str
        self.task_id = task_id  # type: str
        self.task_process = task_process  # type: int
        self.task_status = task_status  # type: str
        self.task_type = task_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLibraryInstallTasksResponseBodyItemsItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.library_biz_id is not None:
            result['LibraryBizId'] = self.library_biz_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_group_id is not None:
            result['TaskGroupId'] = self.task_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_process is not None:
            result['TaskProcess'] = self.task_process
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('LibraryBizId') is not None:
            self.library_biz_id = m.get('LibraryBizId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskGroupId') is not None:
            self.task_group_id = m.get('TaskGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskProcess') is not None:
            self.task_process = m.get('TaskProcess')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class ListLibraryInstallTasksResponseBodyItems(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[ListLibraryInstallTasksResponseBodyItemsItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLibraryInstallTasksResponseBodyItems, self).to_map()
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
                temp_model = ListLibraryInstallTasksResponseBodyItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class ListLibraryInstallTasksResponseBody(TeaModel):
    def __init__(self, items=None, next_token=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.items = items  # type: ListLibraryInstallTasksResponseBodyItems
        self.next_token = next_token  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(ListLibraryInstallTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
            temp_model = ListLibraryInstallTasksResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLibraryInstallTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLibraryInstallTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLibraryInstallTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLibraryInstallTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLibraryStatusRequest(TeaModel):
    def __init__(self, cluster_biz_id=None, current_size=None, library_biz_id=None, limit=None, order_field=None,
                 order_mode=None, page_count=None, page_number=None, page_size=None, region_id=None, resource_owner_id=None):
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.current_size = current_size  # type: int
        self.library_biz_id = library_biz_id  # type: str
        self.limit = limit  # type: int
        self.order_field = order_field  # type: str
        self.order_mode = order_mode  # type: str
        self.page_count = page_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLibraryStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.current_size is not None:
            result['CurrentSize'] = self.current_size
        if self.library_biz_id is not None:
            result['LibraryBizId'] = self.library_biz_id
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('CurrentSize') is not None:
            self.current_size = m.get('CurrentSize')
        if m.get('LibraryBizId') is not None:
            self.library_biz_id = m.get('LibraryBizId')
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
        return self


class ListLibraryStatusResponseBodyItemsItem(TeaModel):
    def __init__(self, cluster_biz_id=None, cluster_name=None, library_biz_id=None, library_name=None, status=None):
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.library_biz_id = library_biz_id  # type: str
        self.library_name = library_name  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLibraryStatusResponseBodyItemsItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.library_biz_id is not None:
            result['LibraryBizId'] = self.library_biz_id
        if self.library_name is not None:
            result['LibraryName'] = self.library_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('LibraryBizId') is not None:
            self.library_biz_id = m.get('LibraryBizId')
        if m.get('LibraryName') is not None:
            self.library_name = m.get('LibraryName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLibraryStatusResponseBodyItems(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[ListLibraryStatusResponseBodyItemsItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLibraryStatusResponseBodyItems, self).to_map()
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
                temp_model = ListLibraryStatusResponseBodyItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class ListLibraryStatusResponseBody(TeaModel):
    def __init__(self, items=None, next_token=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.items = items  # type: ListLibraryStatusResponseBodyItems
        self.next_token = next_token  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super(ListLibraryStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
            temp_model = ListLibraryStatusResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLibraryStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLibraryStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLibraryStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLibraryStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # 标签键
        self.key = key  # type: str
        # 标签值
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
                 resource_owner_id=None, resource_type=None, tag=None):
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        # 资源组ID
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_id = resource_owner_id  # type: long
        self.resource_type = resource_type  # type: str
        # 标签
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
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
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
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        # 资源ID
        self.resource_id = resource_id  # type: str
        # 资源类型
        self.resource_type = resource_type  # type: str
        # 标签键
        self.tag_key = tag_key  # type: str
        # 标签值
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
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


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, code=None, error_code=None, message=None, request_id=None, success=None, tag_resources=None):
        # 响应码
        self.code = code  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # 响应消息
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 请求是否成功被处理
        self.success = success  # type: bool
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
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyFlowForWebResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyFlowForWebResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowJobRequestResourceList(TeaModel):
    def __init__(self, alias=None, path=None):
        # 保留参数。
        self.alias = alias  # type: str
        # 保留参数。
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
        # 保留参数。
        self.alert_conf = alert_conf  # type: str
        # 集群ID。您可以调用ListClusters查看集群的ID。
        self.cluster_id = cluster_id  # type: str
        # 自定义变量。
        self.custom_variables = custom_variables  # type: str
        # 修改后的作业描述。
        self.description = description  # type: str
        # 环境变量设置。
        self.env_conf = env_conf  # type: str
        # 失败策略，可能的取值：CONTINUE（提过本次作业），STOP（停止作业）
        self.fail_act = fail_act  # type: str
        # 需要修改的作业的ID。
        self.id = id  # type: str
        # Knox的用户密码，执行Zeppelin Notebook时必须提供。
        self.knox_password = knox_password  # type: str
        # Knox的用户名，执行Zeppelin Notebook时必须提供。
        self.knox_user = knox_user  # type: str
        # 模型模式，取值如下：  YARN：将作业包装成一个Launcher提交至YARN中执行，LOCAL：作业直接在机器上以进程方式运行。
        self.mode = mode  # type: str
        # 监控配置，仅SPARK_STREAMING类型作业支持监控配置。
        self.monitor_conf = monitor_conf  # type: str
        # 修改后的作业名称。
        self.name = name  # type: str
        # 参数设置。
        self.param_conf = param_conf  # type: str
        # 作业内容。如果是spark作业，该参数的内容会作为spark-submit的参数。
        self.params = params  # type: str
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id  # type: str
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
        self.region_id = region_id  # type: str
        # 保留参数。
        self.resource_list = resource_list  # type: list[ModifyFlowJobRequestResourceList]
        # 重试策略，保留参数。
        self.retry_policy = retry_policy  # type: str
        # 运行配置，取值如下：priority（优先级），userName（任务的Linux提交用户），memory（内存，单位为MB），cores（核数）
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
        # API调用结果：true（修改成功），false（修改失败）
        self.data = data  # type: bool
        # 请求ID。
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyFlowJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyFlowProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyFlowProjectResponseBody()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleaseClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleaseClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RerunFlowRequest(TeaModel):
    def __init__(self, flow_instance_id=None, project_id=None, re_run_fail=None, region_id=None):
        # 工作流实例ID。您可以调用ListFlowInstance查看工作流实例ID。
        self.flow_instance_id = flow_instance_id  # type: str
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id  # type: str
        # 是否只重试失败节点。
        self.re_run_fail = re_run_fail  # type: bool
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
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
        # 返回执行结果，包含如下：true: 重试工作流成功，false: 重试工作流失败。
        self.data = data  # type: bool
        # 请求ID。
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RerunFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RerunFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeFlowRequest(TeaModel):
    def __init__(self, flow_instance_id=None, project_id=None, region_id=None):
        # 工作流实例ID。您可以调用ListFlowInstance查看工作流ID。
        self.flow_instance_id = flow_instance_id  # type: str
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id  # type: str
        # 区域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
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
        # 返回执行结果。
        self.data = data  # type: bool
        # 请求ID。
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResumeFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResumeFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitFlowRequest(TeaModel):
    def __init__(self, conf=None, flow_id=None, project_id=None, region_id=None):
        # 配置信息{"key":"value"}格式。  本示例中cyctime表示实际调度运行的时间（长整型时间戳）。
        self.conf = conf  # type: str
        # 工作流ID。您可以调用ListFlowInstance查看工作流ID。
        self.flow_id = flow_id  # type: str
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id  # type: str
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
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
        # 过期参数。
        self.data = data  # type: str
        # 工作流实例ID。
        self.id = id  # type: str
        # 过期参数。
        self.instance_id = instance_id  # type: str
        # 请求ID。
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitFlowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitFlowJobRequest(TeaModel):
    def __init__(self, cluster_id=None, conf=None, host_name=None, job_id=None, project_id=None, region_id=None):
        # 集群ID。您可以调用ListClusters查看集群的ID。
        self.cluster_id = cluster_id  # type: str
        # 配置参数信息：{"key1":"value1"}。key为params的参数值会覆盖实际作业中运行的内容。
        self.conf = conf  # type: str
        # 保留参数。
        self.host_name = host_name  # type: str
        # 作业ID。您可以调用ListFlowJob查看作业ID。
        self.job_id = job_id  # type: str
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id  # type: str
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
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
        # 运行的作业实例ID。
        self.id = id  # type: str
        # 请求ID。
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitFlowJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitFlowJobResponseBody()
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
    def __init__(self, region_id=None, resource_group_id=None, resource_id=None, resource_owner_id=None,
                 resource_type=None, tag=None):
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        # 资源ID
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_id = resource_owner_id  # type: long
        # 资源类型
        self.resource_type = resource_type  # type: str
        # 标签列表
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
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
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
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, code=None, error_code=None, message=None, request_id=None, success=None):
        # 响应码
        self.code = code  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # 响应消息
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 请求是否成功被处理
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class UninstallLibrariesRequest(TeaModel):
    def __init__(self, cluster_biz_id_list=None, library_biz_id=None, region_id=None, resource_owner_id=None):
        self.cluster_biz_id_list = cluster_biz_id_list  # type: list[str]
        self.library_biz_id = library_biz_id  # type: str
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallLibrariesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id_list is not None:
            result['ClusterBizIdList'] = self.cluster_biz_id_list
        if self.library_biz_id is not None:
            result['LibraryBizId'] = self.library_biz_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterBizIdList') is not None:
            self.cluster_biz_id_list = m.get('ClusterBizIdList')
        if m.get('LibraryBizId') is not None:
            self.library_biz_id = m.get('LibraryBizId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UninstallLibrariesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallLibrariesResponseBody, self).to_map()
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


class UninstallLibrariesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UninstallLibrariesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UninstallLibrariesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UninstallLibrariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, region_id=None, resource_group_id=None, resource_id=None, resource_owner_id=None,
                 resource_type=None, tag_key=None):
        # 是否解绑资源的所有标签
        self.all = all  # type: bool
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        # 集群ID列表
        self.resource_id = resource_id  # type: list[str]
        self.resource_owner_id = resource_owner_id  # type: long
        # 资源类型
        self.resource_type = resource_type  # type: str
        # 解绑的标签键列表
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
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
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
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, code=None, error_code=None, message=None, request_id=None, success=None):
        # 响应码
        self.code = code  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # 响应消息
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        # 请求是否成功被处理
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class UpdateLibraryInstallTaskStatusRequest(TeaModel):
    def __init__(self, region_id=None, resource_owner_id=None, status=None, task_biz_id=None):
        self.region_id = region_id  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.status = status  # type: str
        self.task_biz_id = task_biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLibraryInstallTaskStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_biz_id is not None:
            result['TaskBizId'] = self.task_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskBizId') is not None:
            self.task_biz_id = m.get('TaskBizId')
        return self


class UpdateLibraryInstallTaskStatusResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLibraryInstallTaskStatusResponseBody, self).to_map()
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


class UpdateLibraryInstallTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateLibraryInstallTaskStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLibraryInstallTaskStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateLibraryInstallTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


