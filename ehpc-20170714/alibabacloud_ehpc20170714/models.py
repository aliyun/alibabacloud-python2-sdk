# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddNodesRequest(TeaModel):
    def __init__(self, cluster_id=None, compute_spot_price_limit=None, compute_spot_strategy=None, count=None,
                 image_id=None, image_owner_alias=None):
        self.cluster_id = cluster_id  # type: str
        self.compute_spot_price_limit = compute_spot_price_limit  # type: str
        self.compute_spot_strategy = compute_spot_strategy  # type: str
        self.count = count  # type: int
        self.image_id = image_id  # type: str
        self.image_owner_alias = image_owner_alias  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.compute_spot_price_limit is not None:
            result['ComputeSpotPriceLimit'] = self.compute_spot_price_limit
        if self.compute_spot_strategy is not None:
            result['ComputeSpotStrategy'] = self.compute_spot_strategy
        if self.count is not None:
            result['Count'] = self.count
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ComputeSpotPriceLimit') is not None:
            self.compute_spot_price_limit = m.get('ComputeSpotPriceLimit')
        if m.get('ComputeSpotStrategy') is not None:
            self.compute_spot_strategy = m.get('ComputeSpotStrategy')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        return self


class AddNodesResponseBodyInstanceIds(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddNodesResponseBodyInstanceIds, self).to_map()
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


class AddNodesResponseBody(TeaModel):
    def __init__(self, instance_ids=None, request_id=None):
        self.instance_ids = instance_ids  # type: AddNodesResponseBodyInstanceIds
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super(AddNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            temp_model = AddNodesResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddNodesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddNodesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUsersRequestUser(TeaModel):
    def __init__(self, group=None, name=None, password=None):
        self.group = group  # type: str
        self.name = name  # type: str
        self.password = password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUsersRequestUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['Group'] = self.group
        if self.name is not None:
            result['Name'] = self.name
        if self.password is not None:
            result['Password'] = self.password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        return self


class AddUsersRequest(TeaModel):
    def __init__(self, cluster_id=None, release_instance=None, user=None):
        self.cluster_id = cluster_id  # type: str
        self.release_instance = release_instance  # type: bool
        self.user = user  # type: list[AddUsersRequestUser]

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.release_instance is not None:
            result['ReleaseInstance'] = self.release_instance
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ReleaseInstance') is not None:
            self.release_instance = m.get('ReleaseInstance')
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = AddUsersRequestUser()
                self.user.append(temp_model.from_map(k))
        return self


class AddUsersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUsersResponseBody, self).to_map()
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


class AddUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequestEcsOrderCompute(TeaModel):
    def __init__(self, count=None, instance_type=None):
        self.count = count  # type: int
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequestEcsOrderCompute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateClusterRequestEcsOrderLogin(TeaModel):
    def __init__(self, count=None, instance_type=None):
        self.count = count  # type: int
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequestEcsOrderLogin, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateClusterRequestEcsOrderManager(TeaModel):
    def __init__(self, count=None, instance_type=None):
        self.count = count  # type: int
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequestEcsOrderManager, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateClusterRequestEcsOrder(TeaModel):
    def __init__(self, compute=None, login=None, manager=None):
        self.compute = compute  # type: CreateClusterRequestEcsOrderCompute
        self.login = login  # type: CreateClusterRequestEcsOrderLogin
        self.manager = manager  # type: CreateClusterRequestEcsOrderManager

    def validate(self):
        self.validate_required(self.compute, 'compute')
        if self.compute:
            self.compute.validate()
        self.validate_required(self.login, 'login')
        if self.login:
            self.login.validate()
        self.validate_required(self.manager, 'manager')
        if self.manager:
            self.manager.validate()

    def to_map(self):
        _map = super(CreateClusterRequestEcsOrder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute is not None:
            result['Compute'] = self.compute.to_map()
        if self.login is not None:
            result['Login'] = self.login.to_map()
        if self.manager is not None:
            result['Manager'] = self.manager.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Compute') is not None:
            temp_model = CreateClusterRequestEcsOrderCompute()
            self.compute = temp_model.from_map(m['Compute'])
        if m.get('Login') is not None:
            temp_model = CreateClusterRequestEcsOrderLogin()
            self.login = temp_model.from_map(m['Login'])
        if m.get('Manager') is not None:
            temp_model = CreateClusterRequestEcsOrderManager()
            self.manager = temp_model.from_map(m['Manager'])
        return self


class CreateClusterRequestApplication(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequestApplication, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class CreateClusterRequest(TeaModel):
    def __init__(self, ecs_order=None, account_type=None, application=None, compute_spot_price_limit=None,
                 compute_spot_strategy=None, description=None, ecs_charge_type=None, ehpc_version=None, ha_enable=None, image_id=None,
                 image_owner_alias=None, key_pair_name=None, name=None, os_tag=None, password=None, remote_directory=None,
                 scc_cluster_id=None, scheduler_type=None, security_group_id=None, security_group_name=None, v_switch_id=None,
                 volume_id=None, volume_mountpoint=None, volume_protocol=None, volume_type=None, vpc_id=None, zone_id=None):
        self.ecs_order = ecs_order  # type: CreateClusterRequestEcsOrder
        self.account_type = account_type  # type: str
        self.application = application  # type: list[CreateClusterRequestApplication]
        self.compute_spot_price_limit = compute_spot_price_limit  # type: str
        self.compute_spot_strategy = compute_spot_strategy  # type: str
        self.description = description  # type: str
        self.ecs_charge_type = ecs_charge_type  # type: str
        self.ehpc_version = ehpc_version  # type: str
        self.ha_enable = ha_enable  # type: bool
        self.image_id = image_id  # type: str
        self.image_owner_alias = image_owner_alias  # type: str
        self.key_pair_name = key_pair_name  # type: str
        self.name = name  # type: str
        self.os_tag = os_tag  # type: str
        self.password = password  # type: str
        self.remote_directory = remote_directory  # type: str
        self.scc_cluster_id = scc_cluster_id  # type: str
        self.scheduler_type = scheduler_type  # type: str
        self.security_group_id = security_group_id  # type: str
        self.security_group_name = security_group_name  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.volume_id = volume_id  # type: str
        self.volume_mountpoint = volume_mountpoint  # type: str
        self.volume_protocol = volume_protocol  # type: str
        self.volume_type = volume_type  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.ecs_order:
            self.ecs_order.validate()
        if self.application:
            for k in self.application:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_order is not None:
            result['EcsOrder'] = self.ecs_order.to_map()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        result['Application'] = []
        if self.application is not None:
            for k in self.application:
                result['Application'].append(k.to_map() if k else None)
        if self.compute_spot_price_limit is not None:
            result['ComputeSpotPriceLimit'] = self.compute_spot_price_limit
        if self.compute_spot_strategy is not None:
            result['ComputeSpotStrategy'] = self.compute_spot_strategy
        if self.description is not None:
            result['Description'] = self.description
        if self.ecs_charge_type is not None:
            result['EcsChargeType'] = self.ecs_charge_type
        if self.ehpc_version is not None:
            result['EhpcVersion'] = self.ehpc_version
        if self.ha_enable is not None:
            result['HaEnable'] = self.ha_enable
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.name is not None:
            result['Name'] = self.name
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.password is not None:
            result['Password'] = self.password
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        if self.scc_cluster_id is not None:
            result['SccClusterId'] = self.scc_cluster_id
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EcsOrder') is not None:
            temp_model = CreateClusterRequestEcsOrder()
            self.ecs_order = temp_model.from_map(m['EcsOrder'])
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        self.application = []
        if m.get('Application') is not None:
            for k in m.get('Application'):
                temp_model = CreateClusterRequestApplication()
                self.application.append(temp_model.from_map(k))
        if m.get('ComputeSpotPriceLimit') is not None:
            self.compute_spot_price_limit = m.get('ComputeSpotPriceLimit')
        if m.get('ComputeSpotStrategy') is not None:
            self.compute_spot_strategy = m.get('ComputeSpotStrategy')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EcsChargeType') is not None:
            self.ecs_charge_type = m.get('EcsChargeType')
        if m.get('EhpcVersion') is not None:
            self.ehpc_version = m.get('EhpcVersion')
        if m.get('HaEnable') is not None:
            self.ha_enable = m.get('HaEnable')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        if m.get('SccClusterId') is not None:
            self.scc_cluster_id = m.get('SccClusterId')
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None):
        self.cluster_id = cluster_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobTemplateRequest(TeaModel):
    def __init__(self, array_request=None, command_line=None, name=None, package_path=None, priority=None,
                 re_runable=None, region_id=None, runas_user=None, stderr_redirect_path=None, stdout_redirect_path=None,
                 variables=None):
        self.array_request = array_request  # type: str
        self.command_line = command_line  # type: str
        self.name = name  # type: str
        self.package_path = package_path  # type: str
        self.priority = priority  # type: int
        self.re_runable = re_runable  # type: bool
        self.region_id = region_id  # type: str
        self.runas_user = runas_user  # type: str
        self.stderr_redirect_path = stderr_redirect_path  # type: str
        self.stdout_redirect_path = stdout_redirect_path  # type: str
        self.variables = variables  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request
        if self.command_line is not None:
            result['CommandLine'] = self.command_line
        if self.name is not None:
            result['Name'] = self.name
        if self.package_path is not None:
            result['PackagePath'] = self.package_path
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.re_runable is not None:
            result['ReRunable'] = self.re_runable
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user
        if self.stderr_redirect_path is not None:
            result['StderrRedirectPath'] = self.stderr_redirect_path
        if self.stdout_redirect_path is not None:
            result['StdoutRedirectPath'] = self.stdout_redirect_path
        if self.variables is not None:
            result['Variables'] = self.variables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')
        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackagePath') is not None:
            self.package_path = m.get('PackagePath')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ReRunable') is not None:
            self.re_runable = m.get('ReRunable')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')
        if m.get('StderrRedirectPath') is not None:
            self.stderr_redirect_path = m.get('StderrRedirectPath')
        if m.get('StdoutRedirectPath') is not None:
            self.stdout_redirect_path = m.get('StdoutRedirectPath')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        return self


class CreateJobTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_id=None):
        self.request_id = request_id  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobTemplateResponseBody, self).to_map()
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


class CreateJobTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateJobTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateJobTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateJobTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, release_instance=None):
        self.cluster_id = cluster_id  # type: str
        self.release_instance = release_instance  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.release_instance is not None:
            result['ReleaseInstance'] = self.release_instance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ReleaseInstance') is not None:
            self.release_instance = m.get('ReleaseInstance')
        return self


class DeleteClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterResponseBody, self).to_map()
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


class DeleteClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobTemplatesRequest(TeaModel):
    def __init__(self, region_id=None, templates=None):
        self.region_id = region_id  # type: str
        self.templates = templates  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteJobTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.templates is not None:
            result['Templates'] = self.templates
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Templates') is not None:
            self.templates = m.get('Templates')
        return self


class DeleteJobTemplatesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteJobTemplatesResponseBody, self).to_map()
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


class DeleteJobTemplatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteJobTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteJobTemplatesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteJobTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobsRequest(TeaModel):
    def __init__(self, cluster_id=None, jobs=None):
        self.cluster_id = cluster_id  # type: str
        self.jobs = jobs  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.jobs is not None:
            result['Jobs'] = self.jobs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Jobs') is not None:
            self.jobs = m.get('Jobs')
        return self


class DeleteJobsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteJobsResponseBody, self).to_map()
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


class DeleteJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteJobsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNodesRequestInstance(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNodesRequestInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteNodesRequest(TeaModel):
    def __init__(self, cluster_id=None, instance=None, release_instance=None):
        self.cluster_id = cluster_id  # type: str
        self.instance = instance  # type: list[DeleteNodesRequestInstance]
        self.release_instance = release_instance  # type: bool

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DeleteNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        if self.release_instance is not None:
            result['ReleaseInstance'] = self.release_instance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = DeleteNodesRequestInstance()
                self.instance.append(temp_model.from_map(k))
        if m.get('ReleaseInstance') is not None:
            self.release_instance = m.get('ReleaseInstance')
        return self


class DeleteNodesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNodesResponseBody, self).to_map()
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


class DeleteNodesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNodesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUsersRequestUser(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUsersRequestUser, self).to_map()
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


class DeleteUsersRequest(TeaModel):
    def __init__(self, cluster_id=None, user=None):
        self.cluster_id = cluster_id  # type: str
        self.user = user  # type: list[DeleteUsersRequestUser]

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DeleteUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = DeleteUsersRequestUser()
                self.user.append(temp_model.from_map(k))
        return self


class DeleteUsersResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUsersResponseBody, self).to_map()
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


class DeleteUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeClusterResponseBodyClusterInfoApplicationsApplicationInfo(TeaModel):
    def __init__(self, name=None, tag=None, version=None):
        self.name = name  # type: str
        self.tag = tag  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterResponseBodyClusterInfoApplicationsApplicationInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeClusterResponseBodyClusterInfoApplications(TeaModel):
    def __init__(self, application_info=None):
        self.application_info = application_info  # type: list[DescribeClusterResponseBodyClusterInfoApplicationsApplicationInfo]

    def validate(self):
        if self.application_info:
            for k in self.application_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterResponseBodyClusterInfoApplications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationInfo'] = []
        if self.application_info is not None:
            for k in self.application_info:
                result['ApplicationInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.application_info = []
        if m.get('ApplicationInfo') is not None:
            for k in m.get('ApplicationInfo'):
                temp_model = DescribeClusterResponseBodyClusterInfoApplicationsApplicationInfo()
                self.application_info.append(temp_model.from_map(k))
        return self


class DescribeClusterResponseBodyClusterInfoEcsInfoCompute(TeaModel):
    def __init__(self, count=None, instance_type=None):
        self.count = count  # type: int
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterResponseBodyClusterInfoEcsInfoCompute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeClusterResponseBodyClusterInfoEcsInfoLogin(TeaModel):
    def __init__(self, count=None, instance_type=None):
        self.count = count  # type: int
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterResponseBodyClusterInfoEcsInfoLogin, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeClusterResponseBodyClusterInfoEcsInfoManager(TeaModel):
    def __init__(self, count=None, instance_type=None):
        self.count = count  # type: int
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterResponseBodyClusterInfoEcsInfoManager, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeClusterResponseBodyClusterInfoEcsInfo(TeaModel):
    def __init__(self, compute=None, login=None, manager=None):
        self.compute = compute  # type: DescribeClusterResponseBodyClusterInfoEcsInfoCompute
        self.login = login  # type: DescribeClusterResponseBodyClusterInfoEcsInfoLogin
        self.manager = manager  # type: DescribeClusterResponseBodyClusterInfoEcsInfoManager

    def validate(self):
        if self.compute:
            self.compute.validate()
        if self.login:
            self.login.validate()
        if self.manager:
            self.manager.validate()

    def to_map(self):
        _map = super(DescribeClusterResponseBodyClusterInfoEcsInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute is not None:
            result['Compute'] = self.compute.to_map()
        if self.login is not None:
            result['Login'] = self.login.to_map()
        if self.manager is not None:
            result['Manager'] = self.manager.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Compute') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoEcsInfoCompute()
            self.compute = temp_model.from_map(m['Compute'])
        if m.get('Login') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoEcsInfoLogin()
            self.login = temp_model.from_map(m['Login'])
        if m.get('Manager') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoEcsInfoManager()
            self.manager = temp_model.from_map(m['Manager'])
        return self


class DescribeClusterResponseBodyClusterInfo(TeaModel):
    def __init__(self, account_type=None, applications=None, client_version=None, create_time=None,
                 description=None, ecs_charge_type=None, ecs_info=None, ha_enable=None, id=None, image_id=None,
                 image_owner_alias=None, key_pair_name=None, name=None, os_tag=None, region_id=None, remote_directory=None,
                 scc_cluster_id=None, scheduler_type=None, security_group_id=None, status=None, v_switch_id=None, volume_id=None,
                 volume_mountpoint=None, volume_protocol=None, volume_type=None):
        self.account_type = account_type  # type: str
        self.applications = applications  # type: DescribeClusterResponseBodyClusterInfoApplications
        self.client_version = client_version  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.ecs_charge_type = ecs_charge_type  # type: str
        self.ecs_info = ecs_info  # type: DescribeClusterResponseBodyClusterInfoEcsInfo
        self.ha_enable = ha_enable  # type: bool
        self.id = id  # type: str
        self.image_id = image_id  # type: str
        self.image_owner_alias = image_owner_alias  # type: str
        self.key_pair_name = key_pair_name  # type: str
        self.name = name  # type: str
        self.os_tag = os_tag  # type: str
        self.region_id = region_id  # type: str
        self.remote_directory = remote_directory  # type: str
        self.scc_cluster_id = scc_cluster_id  # type: str
        self.scheduler_type = scheduler_type  # type: str
        self.security_group_id = security_group_id  # type: str
        self.status = status  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.volume_id = volume_id  # type: str
        self.volume_mountpoint = volume_mountpoint  # type: str
        self.volume_protocol = volume_protocol  # type: str
        self.volume_type = volume_type  # type: str

    def validate(self):
        if self.applications:
            self.applications.validate()
        if self.ecs_info:
            self.ecs_info.validate()

    def to_map(self):
        _map = super(DescribeClusterResponseBodyClusterInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.applications is not None:
            result['Applications'] = self.applications.to_map()
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.ecs_charge_type is not None:
            result['EcsChargeType'] = self.ecs_charge_type
        if self.ecs_info is not None:
            result['EcsInfo'] = self.ecs_info.to_map()
        if self.ha_enable is not None:
            result['HaEnable'] = self.ha_enable
        if self.id is not None:
            result['Id'] = self.id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.name is not None:
            result['Name'] = self.name
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        if self.scc_cluster_id is not None:
            result['SccClusterId'] = self.scc_cluster_id
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Applications') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoApplications()
            self.applications = temp_model.from_map(m['Applications'])
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EcsChargeType') is not None:
            self.ecs_charge_type = m.get('EcsChargeType')
        if m.get('EcsInfo') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoEcsInfo()
            self.ecs_info = temp_model.from_map(m['EcsInfo'])
        if m.get('HaEnable') is not None:
            self.ha_enable = m.get('HaEnable')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        if m.get('SccClusterId') is not None:
            self.scc_cluster_id = m.get('SccClusterId')
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        return self


class DescribeClusterResponseBody(TeaModel):
    def __init__(self, cluster_info=None, request_id=None):
        self.cluster_info = cluster_info  # type: DescribeClusterResponseBodyClusterInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cluster_info:
            self.cluster_info.validate()

    def to_map(self):
        _map = super(DescribeClusterResponseBody, self).to_map()
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
            temp_model = DescribeClusterResponseBodyClusterInfo()
            self.cluster_info = temp_model.from_map(m['ClusterInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditJobTemplateRequest(TeaModel):
    def __init__(self, array_request=None, command_line=None, name=None, package_path=None, priority=None,
                 re_runable=None, region_id=None, runas_user=None, stderr_redirect_path=None, stdout_redirect_path=None,
                 template_id=None, variables=None):
        self.array_request = array_request  # type: str
        self.command_line = command_line  # type: str
        self.name = name  # type: str
        self.package_path = package_path  # type: str
        self.priority = priority  # type: int
        self.re_runable = re_runable  # type: bool
        self.region_id = region_id  # type: str
        self.runas_user = runas_user  # type: str
        self.stderr_redirect_path = stderr_redirect_path  # type: str
        self.stdout_redirect_path = stdout_redirect_path  # type: str
        self.template_id = template_id  # type: str
        self.variables = variables  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditJobTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request
        if self.command_line is not None:
            result['CommandLine'] = self.command_line
        if self.name is not None:
            result['Name'] = self.name
        if self.package_path is not None:
            result['PackagePath'] = self.package_path
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.re_runable is not None:
            result['ReRunable'] = self.re_runable
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user
        if self.stderr_redirect_path is not None:
            result['StderrRedirectPath'] = self.stderr_redirect_path
        if self.stdout_redirect_path is not None:
            result['StdoutRedirectPath'] = self.stdout_redirect_path
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.variables is not None:
            result['Variables'] = self.variables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')
        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackagePath') is not None:
            self.package_path = m.get('PackagePath')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ReRunable') is not None:
            self.re_runable = m.get('ReRunable')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')
        if m.get('StderrRedirectPath') is not None:
            self.stderr_redirect_path = m.get('StderrRedirectPath')
        if m.get('StdoutRedirectPath') is not None:
            self.stdout_redirect_path = m.get('StdoutRedirectPath')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        return self


class EditJobTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_id=None):
        self.request_id = request_id  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditJobTemplateResponseBody, self).to_map()
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


class EditJobTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EditJobTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EditJobTemplateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EditJobTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutoScaleConfigRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAutoScaleConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class GetAutoScaleConfigResponseBody(TeaModel):
    def __init__(self, cluster_id=None, cluster_type=None, enable_auto_grow=None, enable_auto_shrink=None,
                 exclude_nodes=None, extra_nodes_grow_ratio=None, grow_interval_in_minutes=None, grow_ratio=None,
                 grow_timeout_in_minutes=None, max_nodes_in_cluster=None, request_id=None, shrink_idle_times=None,
                 shrink_interval_in_minutes=None, uid=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_type = cluster_type  # type: str
        self.enable_auto_grow = enable_auto_grow  # type: bool
        self.enable_auto_shrink = enable_auto_shrink  # type: bool
        self.exclude_nodes = exclude_nodes  # type: str
        self.extra_nodes_grow_ratio = extra_nodes_grow_ratio  # type: int
        self.grow_interval_in_minutes = grow_interval_in_minutes  # type: int
        self.grow_ratio = grow_ratio  # type: int
        self.grow_timeout_in_minutes = grow_timeout_in_minutes  # type: int
        self.max_nodes_in_cluster = max_nodes_in_cluster  # type: int
        self.request_id = request_id  # type: str
        self.shrink_idle_times = shrink_idle_times  # type: int
        self.shrink_interval_in_minutes = shrink_interval_in_minutes  # type: int
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAutoScaleConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.enable_auto_grow is not None:
            result['EnableAutoGrow'] = self.enable_auto_grow
        if self.enable_auto_shrink is not None:
            result['EnableAutoShrink'] = self.enable_auto_shrink
        if self.exclude_nodes is not None:
            result['ExcludeNodes'] = self.exclude_nodes
        if self.extra_nodes_grow_ratio is not None:
            result['ExtraNodesGrowRatio'] = self.extra_nodes_grow_ratio
        if self.grow_interval_in_minutes is not None:
            result['GrowIntervalInMinutes'] = self.grow_interval_in_minutes
        if self.grow_ratio is not None:
            result['GrowRatio'] = self.grow_ratio
        if self.grow_timeout_in_minutes is not None:
            result['GrowTimeoutInMinutes'] = self.grow_timeout_in_minutes
        if self.max_nodes_in_cluster is not None:
            result['MaxNodesInCluster'] = self.max_nodes_in_cluster
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.shrink_idle_times is not None:
            result['ShrinkIdleTimes'] = self.shrink_idle_times
        if self.shrink_interval_in_minutes is not None:
            result['ShrinkIntervalInMinutes'] = self.shrink_interval_in_minutes
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('EnableAutoGrow') is not None:
            self.enable_auto_grow = m.get('EnableAutoGrow')
        if m.get('EnableAutoShrink') is not None:
            self.enable_auto_shrink = m.get('EnableAutoShrink')
        if m.get('ExcludeNodes') is not None:
            self.exclude_nodes = m.get('ExcludeNodes')
        if m.get('ExtraNodesGrowRatio') is not None:
            self.extra_nodes_grow_ratio = m.get('ExtraNodesGrowRatio')
        if m.get('GrowIntervalInMinutes') is not None:
            self.grow_interval_in_minutes = m.get('GrowIntervalInMinutes')
        if m.get('GrowRatio') is not None:
            self.grow_ratio = m.get('GrowRatio')
        if m.get('GrowTimeoutInMinutes') is not None:
            self.grow_timeout_in_minutes = m.get('GrowTimeoutInMinutes')
        if m.get('MaxNodesInCluster') is not None:
            self.max_nodes_in_cluster = m.get('MaxNodesInCluster')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShrinkIdleTimes') is not None:
            self.shrink_idle_times = m.get('ShrinkIdleTimes')
        if m.get('ShrinkIntervalInMinutes') is not None:
            self.shrink_interval_in_minutes = m.get('ShrinkIntervalInMinutes')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetAutoScaleConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAutoScaleConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAutoScaleConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAutoScaleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterLogsRequest(TeaModel):
    def __init__(self, cluster_id=None, page_number=None, page_size=None):
        self.cluster_id = cluster_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListClusterLogsResponseBodyLogsLogInfo(TeaModel):
    def __init__(self, create_time=None, level=None, message=None, operation=None):
        self.create_time = create_time  # type: str
        self.level = level  # type: str
        self.message = message  # type: str
        self.operation = operation  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterLogsResponseBodyLogsLogInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.operation is not None:
            result['Operation'] = self.operation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        return self


class ListClusterLogsResponseBodyLogs(TeaModel):
    def __init__(self, log_info=None):
        self.log_info = log_info  # type: list[ListClusterLogsResponseBodyLogsLogInfo]

    def validate(self):
        if self.log_info:
            for k in self.log_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClusterLogsResponseBodyLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogInfo'] = []
        if self.log_info is not None:
            for k in self.log_info:
                result['LogInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_info = []
        if m.get('LogInfo') is not None:
            for k in m.get('LogInfo'):
                temp_model = ListClusterLogsResponseBodyLogsLogInfo()
                self.log_info.append(temp_model.from_map(k))
        return self


class ListClusterLogsResponseBody(TeaModel):
    def __init__(self, cluster_id=None, logs=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.cluster_id = cluster_id  # type: str
        self.logs = logs  # type: ListClusterLogsResponseBodyLogs
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.logs:
            self.logs.validate()

    def to_map(self):
        _map = super(ListClusterLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.logs is not None:
            result['Logs'] = self.logs.to_map()
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
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Logs') is not None:
            temp_model = ListClusterLogsResponseBodyLogs()
            self.logs = temp_model.from_map(m['Logs'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListClusterLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListClusterLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClusterLogsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListClusterLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListClustersResponseBodyClustersClusterInfoSimpleComputes(TeaModel):
    def __init__(self, exception_count=None, normal_count=None, total=None):
        self.exception_count = exception_count  # type: int
        self.normal_count = normal_count  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersResponseBodyClustersClusterInfoSimpleComputes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exception_count is not None:
            result['ExceptionCount'] = self.exception_count
        if self.normal_count is not None:
            result['NormalCount'] = self.normal_count
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExceptionCount') is not None:
            self.exception_count = m.get('ExceptionCount')
        if m.get('NormalCount') is not None:
            self.normal_count = m.get('NormalCount')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListClustersResponseBodyClustersClusterInfoSimpleManagers(TeaModel):
    def __init__(self, exception_count=None, normal_count=None, total=None):
        self.exception_count = exception_count  # type: int
        self.normal_count = normal_count  # type: int
        self.total = total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersResponseBodyClustersClusterInfoSimpleManagers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exception_count is not None:
            result['ExceptionCount'] = self.exception_count
        if self.normal_count is not None:
            result['NormalCount'] = self.normal_count
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExceptionCount') is not None:
            self.exception_count = m.get('ExceptionCount')
        if m.get('NormalCount') is not None:
            self.normal_count = m.get('NormalCount')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListClustersResponseBodyClustersClusterInfoSimpleTotalResources(TeaModel):
    def __init__(self, cpu=None, gpu=None, memory=None):
        self.cpu = cpu  # type: int
        self.gpu = gpu  # type: int
        self.memory = memory  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersResponseBodyClustersClusterInfoSimpleTotalResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ListClustersResponseBodyClustersClusterInfoSimpleUsedResources(TeaModel):
    def __init__(self, cpu=None, gpu=None, memory=None):
        self.cpu = cpu  # type: int
        self.gpu = gpu  # type: int
        self.memory = memory  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersResponseBodyClustersClusterInfoSimpleUsedResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ListClustersResponseBodyClustersClusterInfoSimple(TeaModel):
    def __init__(self, account_type=None, computes=None, count=None, create_time=None, description=None, id=None,
                 image_id=None, image_owner_alias=None, instance_type=None, login_nodes=None, managers=None, name=None,
                 os_tag=None, region_id=None, scheduler_type=None, status=None, total_resources=None, used_resources=None,
                 zone_id=None):
        self.account_type = account_type  # type: str
        self.computes = computes  # type: ListClustersResponseBodyClustersClusterInfoSimpleComputes
        self.count = count  # type: int
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.id = id  # type: str
        self.image_id = image_id  # type: str
        self.image_owner_alias = image_owner_alias  # type: str
        self.instance_type = instance_type  # type: str
        self.login_nodes = login_nodes  # type: str
        self.managers = managers  # type: ListClustersResponseBodyClustersClusterInfoSimpleManagers
        self.name = name  # type: str
        self.os_tag = os_tag  # type: str
        self.region_id = region_id  # type: str
        self.scheduler_type = scheduler_type  # type: str
        self.status = status  # type: str
        self.total_resources = total_resources  # type: ListClustersResponseBodyClustersClusterInfoSimpleTotalResources
        self.used_resources = used_resources  # type: ListClustersResponseBodyClustersClusterInfoSimpleUsedResources
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.computes:
            self.computes.validate()
        if self.managers:
            self.managers.validate()
        if self.total_resources:
            self.total_resources.validate()
        if self.used_resources:
            self.used_resources.validate()

    def to_map(self):
        _map = super(ListClustersResponseBodyClustersClusterInfoSimple, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.computes is not None:
            result['Computes'] = self.computes.to_map()
        if self.count is not None:
            result['Count'] = self.count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.login_nodes is not None:
            result['LoginNodes'] = self.login_nodes
        if self.managers is not None:
            result['Managers'] = self.managers.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        if self.status is not None:
            result['Status'] = self.status
        if self.total_resources is not None:
            result['TotalResources'] = self.total_resources.to_map()
        if self.used_resources is not None:
            result['UsedResources'] = self.used_resources.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Computes') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoSimpleComputes()
            self.computes = temp_model.from_map(m['Computes'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('LoginNodes') is not None:
            self.login_nodes = m.get('LoginNodes')
        if m.get('Managers') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoSimpleManagers()
            self.managers = temp_model.from_map(m['Managers'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalResources') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoSimpleTotalResources()
            self.total_resources = temp_model.from_map(m['TotalResources'])
        if m.get('UsedResources') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoSimpleUsedResources()
            self.used_resources = temp_model.from_map(m['UsedResources'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListClustersResponseBodyClusters(TeaModel):
    def __init__(self, cluster_info_simple=None):
        self.cluster_info_simple = cluster_info_simple  # type: list[ListClustersResponseBodyClustersClusterInfoSimple]

    def validate(self):
        if self.cluster_info_simple:
            for k in self.cluster_info_simple:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClustersResponseBodyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClusterInfoSimple'] = []
        if self.cluster_info_simple is not None:
            for k in self.cluster_info_simple:
                result['ClusterInfoSimple'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cluster_info_simple = []
        if m.get('ClusterInfoSimple') is not None:
            for k in m.get('ClusterInfoSimple'):
                temp_model = ListClustersResponseBodyClustersClusterInfoSimple()
                self.cluster_info_simple.append(temp_model.from_map(k))
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


class ListCurrentClientVersionResponseBody(TeaModel):
    def __init__(self, client_version=None, request_id=None):
        self.client_version = client_version  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCurrentClientVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCurrentClientVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCurrentClientVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCurrentClientVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCurrentClientVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomImagesRequest(TeaModel):
    def __init__(self, base_os_tag=None, image_owner_alias=None, region_id=None):
        self.base_os_tag = base_os_tag  # type: str
        self.image_owner_alias = image_owner_alias  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomImagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BaseOsTag') is not None:
            self.base_os_tag = m.get('BaseOsTag')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCustomImagesResponseBodyImagesImageInfoBaseOsTag(TeaModel):
    def __init__(self, architecture=None, os_tag=None, platform=None, version=None):
        self.architecture = architecture  # type: str
        self.os_tag = os_tag  # type: str
        self.platform = platform  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomImagesResponseBodyImagesImageInfoBaseOsTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListCustomImagesResponseBodyImagesImageInfo(TeaModel):
    def __init__(self, base_os_tag=None, description=None, image_id=None, image_name=None, image_owner_alias=None):
        self.base_os_tag = base_os_tag  # type: ListCustomImagesResponseBodyImagesImageInfoBaseOsTag
        self.description = description  # type: str
        self.image_id = image_id  # type: str
        self.image_name = image_name  # type: str
        self.image_owner_alias = image_owner_alias  # type: str

    def validate(self):
        if self.base_os_tag:
            self.base_os_tag.validate()

    def to_map(self):
        _map = super(ListCustomImagesResponseBodyImagesImageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BaseOsTag') is not None:
            temp_model = ListCustomImagesResponseBodyImagesImageInfoBaseOsTag()
            self.base_os_tag = temp_model.from_map(m['BaseOsTag'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        return self


class ListCustomImagesResponseBodyImages(TeaModel):
    def __init__(self, image_info=None):
        self.image_info = image_info  # type: list[ListCustomImagesResponseBodyImagesImageInfo]

    def validate(self):
        if self.image_info:
            for k in self.image_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCustomImagesResponseBodyImages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageInfo'] = []
        if self.image_info is not None:
            for k in self.image_info:
                result['ImageInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.image_info = []
        if m.get('ImageInfo') is not None:
            for k in m.get('ImageInfo'):
                temp_model = ListCustomImagesResponseBodyImagesImageInfo()
                self.image_info.append(temp_model.from_map(k))
        return self


class ListCustomImagesResponseBody(TeaModel):
    def __init__(self, images=None, request_id=None):
        self.images = images  # type: ListCustomImagesResponseBodyImages
        self.request_id = request_id  # type: str

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        _map = super(ListCustomImagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.images is not None:
            result['Images'] = self.images.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Images') is not None:
            temp_model = ListCustomImagesResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCustomImagesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCustomImagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCustomImagesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCustomImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImagesResponseBodyOsTagsOsInfo(TeaModel):
    def __init__(self, architecture=None, os_tag=None, platform=None, version=None):
        self.architecture = architecture  # type: str
        self.os_tag = os_tag  # type: str
        self.platform = platform  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesResponseBodyOsTagsOsInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListImagesResponseBodyOsTags(TeaModel):
    def __init__(self, os_info=None):
        self.os_info = os_info  # type: list[ListImagesResponseBodyOsTagsOsInfo]

    def validate(self):
        if self.os_info:
            for k in self.os_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListImagesResponseBodyOsTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OsInfo'] = []
        if self.os_info is not None:
            for k in self.os_info:
                result['OsInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.os_info = []
        if m.get('OsInfo') is not None:
            for k in m.get('OsInfo'):
                temp_model = ListImagesResponseBodyOsTagsOsInfo()
                self.os_info.append(temp_model.from_map(k))
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(self, os_tags=None, request_id=None):
        self.os_tags = os_tags  # type: ListImagesResponseBodyOsTags
        self.request_id = request_id  # type: str

    def validate(self):
        if self.os_tags:
            self.os_tags.validate()

    def to_map(self):
        _map = super(ListImagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.os_tags is not None:
            result['OsTags'] = self.os_tags.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OsTags') is not None:
            temp_model = ListImagesResponseBodyOsTags()
            self.os_tags = temp_model.from_map(m['OsTags'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListImagesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListImagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListImagesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobTemplatesRequest(TeaModel):
    def __init__(self, name=None, page_number=None, page_size=None, region_id=None):
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListJobTemplatesResponseBodyTemplatesJobTemplates(TeaModel):
    def __init__(self, array_request=None, command_line=None, id=None, name=None, package_path=None, priority=None,
                 re_runable=None, runas_user=None, stderr_redirect_path=None, stdout_redirect_path=None, variables=None):
        self.array_request = array_request  # type: str
        self.command_line = command_line  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.package_path = package_path  # type: str
        self.priority = priority  # type: int
        self.re_runable = re_runable  # type: bool
        self.runas_user = runas_user  # type: str
        self.stderr_redirect_path = stderr_redirect_path  # type: str
        self.stdout_redirect_path = stdout_redirect_path  # type: str
        self.variables = variables  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobTemplatesResponseBodyTemplatesJobTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request
        if self.command_line is not None:
            result['CommandLine'] = self.command_line
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.package_path is not None:
            result['PackagePath'] = self.package_path
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.re_runable is not None:
            result['ReRunable'] = self.re_runable
        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user
        if self.stderr_redirect_path is not None:
            result['StderrRedirectPath'] = self.stderr_redirect_path
        if self.stdout_redirect_path is not None:
            result['StdoutRedirectPath'] = self.stdout_redirect_path
        if self.variables is not None:
            result['Variables'] = self.variables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')
        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackagePath') is not None:
            self.package_path = m.get('PackagePath')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ReRunable') is not None:
            self.re_runable = m.get('ReRunable')
        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')
        if m.get('StderrRedirectPath') is not None:
            self.stderr_redirect_path = m.get('StderrRedirectPath')
        if m.get('StdoutRedirectPath') is not None:
            self.stdout_redirect_path = m.get('StdoutRedirectPath')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        return self


class ListJobTemplatesResponseBodyTemplates(TeaModel):
    def __init__(self, job_templates=None):
        self.job_templates = job_templates  # type: list[ListJobTemplatesResponseBodyTemplatesJobTemplates]

    def validate(self):
        if self.job_templates:
            for k in self.job_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListJobTemplatesResponseBodyTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobTemplates'] = []
        if self.job_templates is not None:
            for k in self.job_templates:
                result['JobTemplates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.job_templates = []
        if m.get('JobTemplates') is not None:
            for k in m.get('JobTemplates'):
                temp_model = ListJobTemplatesResponseBodyTemplatesJobTemplates()
                self.job_templates.append(temp_model.from_map(k))
        return self


class ListJobTemplatesResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, templates=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.templates = templates  # type: ListJobTemplatesResponseBodyTemplates
        self.total_count = total_count  # type: int

    def validate(self):
        if self.templates:
            self.templates.validate()

    def to_map(self):
        _map = super(ListJobTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.templates is not None:
            result['Templates'] = self.templates.to_map()
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
        if m.get('Templates') is not None:
            temp_model = ListJobTemplatesResponseBodyTemplates()
            self.templates = temp_model.from_map(m['Templates'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListJobTemplatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListJobTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListJobTemplatesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(self, cluster_id=None, owner=None, page_number=None, page_size=None, rerunable=None, state=None):
        self.cluster_id = cluster_id  # type: str
        self.owner = owner  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.rerunable = rerunable  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rerunable is not None:
            result['Rerunable'] = self.rerunable
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Rerunable') is not None:
            self.rerunable = m.get('Rerunable')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListJobsResponseBodyJobsJobInfoResources(TeaModel):
    def __init__(self, cores=None, nodes=None):
        self.cores = cores  # type: int
        self.nodes = nodes  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsResponseBodyJobsJobInfoResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cores is not None:
            result['Cores'] = self.cores
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        return self


class ListJobsResponseBodyJobsJobInfo(TeaModel):
    def __init__(self, array_request=None, comment=None, id=None, last_modify_time=None, name=None, owner=None,
                 priority=None, resources=None, shell_path=None, start_time=None, state=None, stderr=None, stdout=None,
                 submit_time=None):
        self.array_request = array_request  # type: str
        self.comment = comment  # type: str
        self.id = id  # type: str
        self.last_modify_time = last_modify_time  # type: str
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.priority = priority  # type: int
        self.resources = resources  # type: ListJobsResponseBodyJobsJobInfoResources
        self.shell_path = shell_path  # type: str
        self.start_time = start_time  # type: str
        self.state = state  # type: str
        self.stderr = stderr  # type: str
        self.stdout = stdout  # type: str
        self.submit_time = submit_time  # type: str

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super(ListJobsResponseBodyJobsJobInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        if self.shell_path is not None:
            result['ShellPath'] = self.shell_path
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.stderr is not None:
            result['Stderr'] = self.stderr
        if self.stdout is not None:
            result['Stdout'] = self.stdout
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Resources') is not None:
            temp_model = ListJobsResponseBodyJobsJobInfoResources()
            self.resources = temp_model.from_map(m['Resources'])
        if m.get('ShellPath') is not None:
            self.shell_path = m.get('ShellPath')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Stderr') is not None:
            self.stderr = m.get('Stderr')
        if m.get('Stdout') is not None:
            self.stdout = m.get('Stdout')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class ListJobsResponseBodyJobs(TeaModel):
    def __init__(self, job_info=None):
        self.job_info = job_info  # type: list[ListJobsResponseBodyJobsJobInfo]

    def validate(self):
        if self.job_info:
            for k in self.job_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListJobsResponseBodyJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobInfo'] = []
        if self.job_info is not None:
            for k in self.job_info:
                result['JobInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.job_info = []
        if m.get('JobInfo') is not None:
            for k in m.get('JobInfo'):
                temp_model = ListJobsResponseBodyJobsJobInfo()
                self.job_info.append(temp_model.from_map(k))
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(self, jobs=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.jobs = jobs  # type: ListJobsResponseBodyJobs
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.jobs:
            self.jobs.validate()

    def to_map(self):
        _map = super(ListJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jobs is not None:
            result['Jobs'] = self.jobs.to_map()
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
        if m.get('Jobs') is not None:
            temp_model = ListJobsResponseBodyJobs()
            self.jobs = temp_model.from_map(m['Jobs'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListJobsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodesRequest(TeaModel):
    def __init__(self, cluster_id=None, host_name=None, page_number=None, page_size=None, role=None):
        self.cluster_id = cluster_id  # type: str
        self.host_name = host_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.role = role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class ListNodesResponseBodyNodesNodeInfoTotalResources(TeaModel):
    def __init__(self, cpu=None, gpu=None, memory=None):
        self.cpu = cpu  # type: int
        self.gpu = gpu  # type: int
        self.memory = memory  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesResponseBodyNodesNodeInfoTotalResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ListNodesResponseBodyNodesNodeInfoUsedResources(TeaModel):
    def __init__(self, cpu=None, gpu=None, memory=None):
        self.cpu = cpu  # type: int
        self.gpu = gpu  # type: int
        self.memory = memory  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesResponseBodyNodesNodeInfoUsedResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ListNodesResponseBodyNodesNodeInfo(TeaModel):
    def __init__(self, add_time=None, created_by_ehpc=None, expired=None, expired_time=None, id=None, image_id=None,
                 image_owner_alias=None, lock_reason=None, region_id=None, role=None, spot_strategy=None, status=None,
                 total_resources=None, used_resources=None):
        self.add_time = add_time  # type: str
        self.created_by_ehpc = created_by_ehpc  # type: bool
        self.expired = expired  # type: bool
        self.expired_time = expired_time  # type: str
        self.id = id  # type: str
        self.image_id = image_id  # type: str
        self.image_owner_alias = image_owner_alias  # type: str
        self.lock_reason = lock_reason  # type: str
        self.region_id = region_id  # type: str
        self.role = role  # type: str
        self.spot_strategy = spot_strategy  # type: str
        self.status = status  # type: str
        self.total_resources = total_resources  # type: ListNodesResponseBodyNodesNodeInfoTotalResources
        self.used_resources = used_resources  # type: ListNodesResponseBodyNodesNodeInfoUsedResources

    def validate(self):
        if self.total_resources:
            self.total_resources.validate()
        if self.used_resources:
            self.used_resources.validate()

    def to_map(self):
        _map = super(ListNodesResponseBodyNodesNodeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_time is not None:
            result['AddTime'] = self.add_time
        if self.created_by_ehpc is not None:
            result['CreatedByEhpc'] = self.created_by_ehpc
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.id is not None:
            result['Id'] = self.id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role is not None:
            result['Role'] = self.role
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.status is not None:
            result['Status'] = self.status
        if self.total_resources is not None:
            result['TotalResources'] = self.total_resources.to_map()
        if self.used_resources is not None:
            result['UsedResources'] = self.used_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')
        if m.get('CreatedByEhpc') is not None:
            self.created_by_ehpc = m.get('CreatedByEhpc')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalResources') is not None:
            temp_model = ListNodesResponseBodyNodesNodeInfoTotalResources()
            self.total_resources = temp_model.from_map(m['TotalResources'])
        if m.get('UsedResources') is not None:
            temp_model = ListNodesResponseBodyNodesNodeInfoUsedResources()
            self.used_resources = temp_model.from_map(m['UsedResources'])
        return self


class ListNodesResponseBodyNodes(TeaModel):
    def __init__(self, node_info=None):
        self.node_info = node_info  # type: list[ListNodesResponseBodyNodesNodeInfo]

    def validate(self):
        if self.node_info:
            for k in self.node_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNodesResponseBodyNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeInfo'] = []
        if self.node_info is not None:
            for k in self.node_info:
                result['NodeInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.node_info = []
        if m.get('NodeInfo') is not None:
            for k in m.get('NodeInfo'):
                temp_model = ListNodesResponseBodyNodesNodeInfo()
                self.node_info.append(temp_model.from_map(k))
        return self


class ListNodesResponseBody(TeaModel):
    def __init__(self, nodes=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.nodes = nodes  # type: ListNodesResponseBodyNodes
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.nodes:
            self.nodes.validate()

    def to_map(self):
        _map = super(ListNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()
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
        if m.get('Nodes') is not None:
            temp_model = ListNodesResponseBodyNodes()
            self.nodes = temp_model.from_map(m['Nodes'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNodesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodesNoPagingRequest(TeaModel):
    def __init__(self, cluster_id=None, host_name=None, only_detached=None, role=None):
        self.cluster_id = cluster_id  # type: str
        self.host_name = host_name  # type: str
        self.only_detached = only_detached  # type: bool
        self.role = role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesNoPagingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.only_detached is not None:
            result['OnlyDetached'] = self.only_detached
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('OnlyDetached') is not None:
            self.only_detached = m.get('OnlyDetached')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class ListNodesNoPagingResponseBodyNodesNodeInfoTotalResources(TeaModel):
    def __init__(self, cpu=None, gpu=None, memory=None):
        self.cpu = cpu  # type: int
        self.gpu = gpu  # type: int
        self.memory = memory  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesNoPagingResponseBodyNodesNodeInfoTotalResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ListNodesNoPagingResponseBodyNodesNodeInfoUsedResources(TeaModel):
    def __init__(self, cpu=None, gpu=None, memory=None):
        self.cpu = cpu  # type: int
        self.gpu = gpu  # type: int
        self.memory = memory  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesNoPagingResponseBodyNodesNodeInfoUsedResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ListNodesNoPagingResponseBodyNodesNodeInfo(TeaModel):
    def __init__(self, add_time=None, created_by_ehpc=None, expired=None, expired_time=None, id=None, image_id=None,
                 image_owner_alias=None, lock_reason=None, region_id=None, role=None, spot_strategy=None, status=None,
                 total_resources=None, used_resources=None):
        self.add_time = add_time  # type: str
        self.created_by_ehpc = created_by_ehpc  # type: bool
        self.expired = expired  # type: bool
        self.expired_time = expired_time  # type: str
        self.id = id  # type: str
        self.image_id = image_id  # type: str
        self.image_owner_alias = image_owner_alias  # type: str
        self.lock_reason = lock_reason  # type: str
        self.region_id = region_id  # type: str
        self.role = role  # type: str
        self.spot_strategy = spot_strategy  # type: str
        self.status = status  # type: str
        self.total_resources = total_resources  # type: ListNodesNoPagingResponseBodyNodesNodeInfoTotalResources
        self.used_resources = used_resources  # type: ListNodesNoPagingResponseBodyNodesNodeInfoUsedResources

    def validate(self):
        if self.total_resources:
            self.total_resources.validate()
        if self.used_resources:
            self.used_resources.validate()

    def to_map(self):
        _map = super(ListNodesNoPagingResponseBodyNodesNodeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_time is not None:
            result['AddTime'] = self.add_time
        if self.created_by_ehpc is not None:
            result['CreatedByEhpc'] = self.created_by_ehpc
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.id is not None:
            result['Id'] = self.id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role is not None:
            result['Role'] = self.role
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.status is not None:
            result['Status'] = self.status
        if self.total_resources is not None:
            result['TotalResources'] = self.total_resources.to_map()
        if self.used_resources is not None:
            result['UsedResources'] = self.used_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')
        if m.get('CreatedByEhpc') is not None:
            self.created_by_ehpc = m.get('CreatedByEhpc')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalResources') is not None:
            temp_model = ListNodesNoPagingResponseBodyNodesNodeInfoTotalResources()
            self.total_resources = temp_model.from_map(m['TotalResources'])
        if m.get('UsedResources') is not None:
            temp_model = ListNodesNoPagingResponseBodyNodesNodeInfoUsedResources()
            self.used_resources = temp_model.from_map(m['UsedResources'])
        return self


class ListNodesNoPagingResponseBodyNodes(TeaModel):
    def __init__(self, node_info=None):
        self.node_info = node_info  # type: list[ListNodesNoPagingResponseBodyNodesNodeInfo]

    def validate(self):
        if self.node_info:
            for k in self.node_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNodesNoPagingResponseBodyNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeInfo'] = []
        if self.node_info is not None:
            for k in self.node_info:
                result['NodeInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.node_info = []
        if m.get('NodeInfo') is not None:
            for k in m.get('NodeInfo'):
                temp_model = ListNodesNoPagingResponseBodyNodesNodeInfo()
                self.node_info.append(temp_model.from_map(k))
        return self


class ListNodesNoPagingResponseBody(TeaModel):
    def __init__(self, nodes=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.nodes = nodes  # type: ListNodesNoPagingResponseBodyNodes
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.nodes:
            self.nodes.validate()

    def to_map(self):
        _map = super(ListNodesNoPagingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()
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
        if m.get('Nodes') is not None:
            temp_model = ListNodesNoPagingResponseBodyNodes()
            self.nodes = temp_model.from_map(m['Nodes'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodesNoPagingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNodesNoPagingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNodesNoPagingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNodesNoPagingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPreferredEcsTypesRequest(TeaModel):
    def __init__(self, spot_strategy=None, zone_id=None):
        self.spot_strategy = spot_strategy  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPreferredEcsTypesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesCompute(TeaModel):
    def __init__(self, instance_type_id=None):
        self.instance_type_id = instance_type_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesCompute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')
        return self


class ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesLogin(TeaModel):
    def __init__(self, instance_type_id=None):
        self.instance_type_id = instance_type_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesLogin, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')
        return self


class ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesManager(TeaModel):
    def __init__(self, instance_type_id=None):
        self.instance_type_id = instance_type_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesManager, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')
        return self


class ListPreferredEcsTypesResponseBodySeriesSeriesInfoRoles(TeaModel):
    def __init__(self, compute=None, login=None, manager=None):
        self.compute = compute  # type: ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesCompute
        self.login = login  # type: ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesLogin
        self.manager = manager  # type: ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesManager

    def validate(self):
        if self.compute:
            self.compute.validate()
        if self.login:
            self.login.validate()
        if self.manager:
            self.manager.validate()

    def to_map(self):
        _map = super(ListPreferredEcsTypesResponseBodySeriesSeriesInfoRoles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute is not None:
            result['Compute'] = self.compute.to_map()
        if self.login is not None:
            result['Login'] = self.login.to_map()
        if self.manager is not None:
            result['Manager'] = self.manager.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Compute') is not None:
            temp_model = ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesCompute()
            self.compute = temp_model.from_map(m['Compute'])
        if m.get('Login') is not None:
            temp_model = ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesLogin()
            self.login = temp_model.from_map(m['Login'])
        if m.get('Manager') is not None:
            temp_model = ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesManager()
            self.manager = temp_model.from_map(m['Manager'])
        return self


class ListPreferredEcsTypesResponseBodySeriesSeriesInfo(TeaModel):
    def __init__(self, roles=None, series_id=None, series_name=None):
        self.roles = roles  # type: ListPreferredEcsTypesResponseBodySeriesSeriesInfoRoles
        self.series_id = series_id  # type: str
        self.series_name = series_name  # type: str

    def validate(self):
        if self.roles:
            self.roles.validate()

    def to_map(self):
        _map = super(ListPreferredEcsTypesResponseBodySeriesSeriesInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.roles is not None:
            result['Roles'] = self.roles.to_map()
        if self.series_id is not None:
            result['SeriesId'] = self.series_id
        if self.series_name is not None:
            result['SeriesName'] = self.series_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Roles') is not None:
            temp_model = ListPreferredEcsTypesResponseBodySeriesSeriesInfoRoles()
            self.roles = temp_model.from_map(m['Roles'])
        if m.get('SeriesId') is not None:
            self.series_id = m.get('SeriesId')
        if m.get('SeriesName') is not None:
            self.series_name = m.get('SeriesName')
        return self


class ListPreferredEcsTypesResponseBodySeries(TeaModel):
    def __init__(self, series_info=None):
        self.series_info = series_info  # type: list[ListPreferredEcsTypesResponseBodySeriesSeriesInfo]

    def validate(self):
        if self.series_info:
            for k in self.series_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPreferredEcsTypesResponseBodySeries, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SeriesInfo'] = []
        if self.series_info is not None:
            for k in self.series_info:
                result['SeriesInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.series_info = []
        if m.get('SeriesInfo') is not None:
            for k in m.get('SeriesInfo'):
                temp_model = ListPreferredEcsTypesResponseBodySeriesSeriesInfo()
                self.series_info.append(temp_model.from_map(k))
        return self


class ListPreferredEcsTypesResponseBody(TeaModel):
    def __init__(self, request_id=None, series=None, support_spot_instance=None):
        self.request_id = request_id  # type: str
        self.series = series  # type: ListPreferredEcsTypesResponseBodySeries
        self.support_spot_instance = support_spot_instance  # type: bool

    def validate(self):
        if self.series:
            self.series.validate()

    def to_map(self):
        _map = super(ListPreferredEcsTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.series is not None:
            result['Series'] = self.series.to_map()
        if self.support_spot_instance is not None:
            result['SupportSpotInstance'] = self.support_spot_instance
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Series') is not None:
            temp_model = ListPreferredEcsTypesResponseBodySeries()
            self.series = temp_model.from_map(m['Series'])
        if m.get('SupportSpotInstance') is not None:
            self.support_spot_instance = m.get('SupportSpotInstance')
        return self


class ListPreferredEcsTypesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPreferredEcsTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPreferredEcsTypesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPreferredEcsTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBodyRegionsRegionInfo(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRegionsResponseBodyRegionsRegionInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region_info=None):
        self.region_info = region_info  # type: list[ListRegionsResponseBodyRegionsRegionInfo]

    def validate(self):
        if self.region_info:
            for k in self.region_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionInfo'] = []
        if self.region_info is not None:
            for k in self.region_info:
                result['RegionInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region_info = []
        if m.get('RegionInfo') is not None:
            for k in m.get('RegionInfo'):
                temp_model = ListRegionsResponseBodyRegionsRegionInfo()
                self.region_info.append(temp_model.from_map(k))
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: ListRegionsResponseBodyRegions
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(ListRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = ListRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRegionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSoftwaresRequest(TeaModel):
    def __init__(self, ehpc_version=None):
        self.ehpc_version = ehpc_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSoftwaresRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ehpc_version is not None:
            result['EhpcVersion'] = self.ehpc_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EhpcVersion') is not None:
            self.ehpc_version = m.get('EhpcVersion')
        return self


class ListSoftwaresResponseBodySoftwaresSoftwareInfoApplicationsApplicationInfo(TeaModel):
    def __init__(self, name=None, required=None, tag=None, version=None):
        self.name = name  # type: str
        self.required = required  # type: bool
        self.tag = tag  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSoftwaresResponseBodySoftwaresSoftwareInfoApplicationsApplicationInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.required is not None:
            result['Required'] = self.required
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListSoftwaresResponseBodySoftwaresSoftwareInfoApplications(TeaModel):
    def __init__(self, application_info=None):
        self.application_info = application_info  # type: list[ListSoftwaresResponseBodySoftwaresSoftwareInfoApplicationsApplicationInfo]

    def validate(self):
        if self.application_info:
            for k in self.application_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSoftwaresResponseBodySoftwaresSoftwareInfoApplications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationInfo'] = []
        if self.application_info is not None:
            for k in self.application_info:
                result['ApplicationInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.application_info = []
        if m.get('ApplicationInfo') is not None:
            for k in m.get('ApplicationInfo'):
                temp_model = ListSoftwaresResponseBodySoftwaresSoftwareInfoApplicationsApplicationInfo()
                self.application_info.append(temp_model.from_map(k))
        return self


class ListSoftwaresResponseBodySoftwaresSoftwareInfo(TeaModel):
    def __init__(self, account_type=None, account_version=None, applications=None, ehpc_version=None, os_tag=None,
                 scheduler_type=None, scheduler_version=None):
        self.account_type = account_type  # type: str
        self.account_version = account_version  # type: str
        self.applications = applications  # type: ListSoftwaresResponseBodySoftwaresSoftwareInfoApplications
        self.ehpc_version = ehpc_version  # type: str
        self.os_tag = os_tag  # type: str
        self.scheduler_type = scheduler_type  # type: str
        self.scheduler_version = scheduler_version  # type: str

    def validate(self):
        if self.applications:
            self.applications.validate()

    def to_map(self):
        _map = super(ListSoftwaresResponseBodySoftwaresSoftwareInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_version is not None:
            result['AccountVersion'] = self.account_version
        if self.applications is not None:
            result['Applications'] = self.applications.to_map()
        if self.ehpc_version is not None:
            result['EhpcVersion'] = self.ehpc_version
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        if self.scheduler_version is not None:
            result['SchedulerVersion'] = self.scheduler_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountVersion') is not None:
            self.account_version = m.get('AccountVersion')
        if m.get('Applications') is not None:
            temp_model = ListSoftwaresResponseBodySoftwaresSoftwareInfoApplications()
            self.applications = temp_model.from_map(m['Applications'])
        if m.get('EhpcVersion') is not None:
            self.ehpc_version = m.get('EhpcVersion')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        if m.get('SchedulerVersion') is not None:
            self.scheduler_version = m.get('SchedulerVersion')
        return self


class ListSoftwaresResponseBodySoftwares(TeaModel):
    def __init__(self, software_info=None):
        self.software_info = software_info  # type: list[ListSoftwaresResponseBodySoftwaresSoftwareInfo]

    def validate(self):
        if self.software_info:
            for k in self.software_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSoftwaresResponseBodySoftwares, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SoftwareInfo'] = []
        if self.software_info is not None:
            for k in self.software_info:
                result['SoftwareInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.software_info = []
        if m.get('SoftwareInfo') is not None:
            for k in m.get('SoftwareInfo'):
                temp_model = ListSoftwaresResponseBodySoftwaresSoftwareInfo()
                self.software_info.append(temp_model.from_map(k))
        return self


class ListSoftwaresResponseBody(TeaModel):
    def __init__(self, request_id=None, softwares=None):
        self.request_id = request_id  # type: str
        self.softwares = softwares  # type: ListSoftwaresResponseBodySoftwares

    def validate(self):
        if self.softwares:
            self.softwares.validate()

    def to_map(self):
        _map = super(ListSoftwaresResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.softwares is not None:
            result['Softwares'] = self.softwares.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Softwares') is not None:
            temp_model = ListSoftwaresResponseBodySoftwares()
            self.softwares = temp_model.from_map(m['Softwares'])
        return self


class ListSoftwaresResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSoftwaresResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSoftwaresResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSoftwaresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(self, cluster_id=None, page_number=None, page_size=None):
        self.cluster_id = cluster_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUsersResponseBodyUsersUserInfo(TeaModel):
    def __init__(self, add_time=None, group=None, name=None):
        self.add_time = add_time  # type: str
        self.group = group  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersResponseBodyUsersUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_time is not None:
            result['AddTime'] = self.add_time
        if self.group is not None:
            result['Group'] = self.group
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListUsersResponseBodyUsers(TeaModel):
    def __init__(self, user_info=None):
        self.user_info = user_info  # type: list[ListUsersResponseBodyUsersUserInfo]

    def validate(self):
        if self.user_info:
            for k in self.user_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUsersResponseBodyUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UserInfo'] = []
        if self.user_info is not None:
            for k in self.user_info:
                result['UserInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.user_info = []
        if m.get('UserInfo') is not None:
            for k in m.get('UserInfo'):
                temp_model = ListUsersResponseBodyUsersUserInfo()
                self.user_info.append(temp_model.from_map(k))
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, users=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.users = users  # type: ListUsersResponseBodyUsers

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        _map = super(ListUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
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
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Users') is not None:
            temp_model = ListUsersResponseBodyUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class ListUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVolumesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVolumesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListVolumesResponseBodyVolumesVolumeInfo(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, region_id=None, remote_directory=None, volume_id=None,
                 volume_mountpoint=None, volume_protocol=None, volume_type=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.region_id = region_id  # type: str
        self.remote_directory = remote_directory  # type: str
        self.volume_id = volume_id  # type: str
        self.volume_mountpoint = volume_mountpoint  # type: str
        self.volume_protocol = volume_protocol  # type: str
        self.volume_type = volume_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVolumesResponseBodyVolumesVolumeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        return self


class ListVolumesResponseBodyVolumes(TeaModel):
    def __init__(self, volume_info=None):
        self.volume_info = volume_info  # type: list[ListVolumesResponseBodyVolumesVolumeInfo]

    def validate(self):
        if self.volume_info:
            for k in self.volume_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVolumesResponseBodyVolumes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VolumeInfo'] = []
        if self.volume_info is not None:
            for k in self.volume_info:
                result['VolumeInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.volume_info = []
        if m.get('VolumeInfo') is not None:
            for k in m.get('VolumeInfo'):
                temp_model = ListVolumesResponseBodyVolumesVolumeInfo()
                self.volume_info.append(temp_model.from_map(k))
        return self


class ListVolumesResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, volumes=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.volumes = volumes  # type: ListVolumesResponseBodyVolumes

    def validate(self):
        if self.volumes:
            self.volumes.validate()

    def to_map(self):
        _map = super(ListVolumesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.volumes is not None:
            result['Volumes'] = self.volumes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Volumes') is not None:
            temp_model = ListVolumesResponseBodyVolumes()
            self.volumes = temp_model.from_map(m['Volumes'])
        return self


class ListVolumesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVolumesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVolumesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVolumesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterAttributesRequest(TeaModel):
    def __init__(self, cluster_id=None, description=None, name=None):
        self.cluster_id = cluster_id  # type: str
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterAttributesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyClusterAttributesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterAttributesResponseBody, self).to_map()
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


class ModifyClusterAttributesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyClusterAttributesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyClusterAttributesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyClusterAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserGroupsRequestUser(TeaModel):
    def __init__(self, group=None, name=None):
        self.group = group  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserGroupsRequestUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['Group'] = self.group
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyUserGroupsRequest(TeaModel):
    def __init__(self, cluster_id=None, user=None):
        self.cluster_id = cluster_id  # type: str
        self.user = user  # type: list[ModifyUserGroupsRequestUser]

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyUserGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = ModifyUserGroupsRequestUser()
                self.user.append(temp_model.from_map(k))
        return self


class ModifyUserGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserGroupsResponseBody, self).to_map()
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


class ModifyUserGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyUserGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyUserGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyUserGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserPasswordsRequestUser(TeaModel):
    def __init__(self, name=None, password=None):
        self.name = name  # type: str
        self.password = password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserPasswordsRequestUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.password is not None:
            result['Password'] = self.password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        return self


class ModifyUserPasswordsRequest(TeaModel):
    def __init__(self, cluster_id=None, user=None):
        self.cluster_id = cluster_id  # type: str
        self.user = user  # type: list[ModifyUserPasswordsRequestUser]

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyUserPasswordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = ModifyUserPasswordsRequestUser()
                self.user.append(temp_model.from_map(k))
        return self


class ModifyUserPasswordsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserPasswordsResponseBody, self).to_map()
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


class ModifyUserPasswordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyUserPasswordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyUserPasswordsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyUserPasswordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RerunJobsRequest(TeaModel):
    def __init__(self, cluster_id=None, jobs=None):
        self.cluster_id = cluster_id  # type: str
        self.jobs = jobs  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RerunJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.jobs is not None:
            result['Jobs'] = self.jobs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Jobs') is not None:
            self.jobs = m.get('Jobs')
        return self


class RerunJobsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RerunJobsResponseBody, self).to_map()
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


class RerunJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RerunJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RerunJobsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RerunJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetNodesRequestInstance(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetNodesRequestInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ResetNodesRequest(TeaModel):
    def __init__(self, cluster_id=None, instance=None):
        self.cluster_id = cluster_id  # type: str
        self.instance = instance  # type: list[ResetNodesRequestInstance]

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ResetNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = ResetNodesRequestInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class ResetNodesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetNodesResponseBody, self).to_map()
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


class ResetNodesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetNodesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAutoScaleConfigRequest(TeaModel):
    def __init__(self, cluster_id=None, enable_auto_grow=None, enable_auto_shrink=None, exclude_nodes=None,
                 extra_nodes_grow_ratio=None, grow_interval_in_minutes=None, grow_ratio=None, grow_timeout_in_minutes=None,
                 max_nodes_in_cluster=None, shrink_idle_times=None, shrink_interval_in_minutes=None):
        self.cluster_id = cluster_id  # type: str
        self.enable_auto_grow = enable_auto_grow  # type: bool
        self.enable_auto_shrink = enable_auto_shrink  # type: bool
        self.exclude_nodes = exclude_nodes  # type: str
        self.extra_nodes_grow_ratio = extra_nodes_grow_ratio  # type: int
        self.grow_interval_in_minutes = grow_interval_in_minutes  # type: int
        self.grow_ratio = grow_ratio  # type: int
        self.grow_timeout_in_minutes = grow_timeout_in_minutes  # type: int
        self.max_nodes_in_cluster = max_nodes_in_cluster  # type: int
        self.shrink_idle_times = shrink_idle_times  # type: int
        self.shrink_interval_in_minutes = shrink_interval_in_minutes  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAutoScaleConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.enable_auto_grow is not None:
            result['EnableAutoGrow'] = self.enable_auto_grow
        if self.enable_auto_shrink is not None:
            result['EnableAutoShrink'] = self.enable_auto_shrink
        if self.exclude_nodes is not None:
            result['ExcludeNodes'] = self.exclude_nodes
        if self.extra_nodes_grow_ratio is not None:
            result['ExtraNodesGrowRatio'] = self.extra_nodes_grow_ratio
        if self.grow_interval_in_minutes is not None:
            result['GrowIntervalInMinutes'] = self.grow_interval_in_minutes
        if self.grow_ratio is not None:
            result['GrowRatio'] = self.grow_ratio
        if self.grow_timeout_in_minutes is not None:
            result['GrowTimeoutInMinutes'] = self.grow_timeout_in_minutes
        if self.max_nodes_in_cluster is not None:
            result['MaxNodesInCluster'] = self.max_nodes_in_cluster
        if self.shrink_idle_times is not None:
            result['ShrinkIdleTimes'] = self.shrink_idle_times
        if self.shrink_interval_in_minutes is not None:
            result['ShrinkIntervalInMinutes'] = self.shrink_interval_in_minutes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('EnableAutoGrow') is not None:
            self.enable_auto_grow = m.get('EnableAutoGrow')
        if m.get('EnableAutoShrink') is not None:
            self.enable_auto_shrink = m.get('EnableAutoShrink')
        if m.get('ExcludeNodes') is not None:
            self.exclude_nodes = m.get('ExcludeNodes')
        if m.get('ExtraNodesGrowRatio') is not None:
            self.extra_nodes_grow_ratio = m.get('ExtraNodesGrowRatio')
        if m.get('GrowIntervalInMinutes') is not None:
            self.grow_interval_in_minutes = m.get('GrowIntervalInMinutes')
        if m.get('GrowRatio') is not None:
            self.grow_ratio = m.get('GrowRatio')
        if m.get('GrowTimeoutInMinutes') is not None:
            self.grow_timeout_in_minutes = m.get('GrowTimeoutInMinutes')
        if m.get('MaxNodesInCluster') is not None:
            self.max_nodes_in_cluster = m.get('MaxNodesInCluster')
        if m.get('ShrinkIdleTimes') is not None:
            self.shrink_idle_times = m.get('ShrinkIdleTimes')
        if m.get('ShrinkIntervalInMinutes') is not None:
            self.shrink_interval_in_minutes = m.get('ShrinkIntervalInMinutes')
        return self


class SetAutoScaleConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAutoScaleConfigResponseBody, self).to_map()
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


class SetAutoScaleConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetAutoScaleConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetAutoScaleConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetAutoScaleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetJobUserRequest(TeaModel):
    def __init__(self, cluster_id=None, runas_user=None, runas_user_password=None):
        self.cluster_id = cluster_id  # type: str
        self.runas_user = runas_user  # type: str
        self.runas_user_password = runas_user_password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetJobUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user
        if self.runas_user_password is not None:
            result['RunasUserPassword'] = self.runas_user_password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')
        if m.get('RunasUserPassword') is not None:
            self.runas_user_password = m.get('RunasUserPassword')
        return self


class SetJobUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetJobUserResponseBody, self).to_map()
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


class SetJobUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetJobUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetJobUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetJobUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopJobsRequest(TeaModel):
    def __init__(self, cluster_id=None, jobs=None):
        self.cluster_id = cluster_id  # type: str
        self.jobs = jobs  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.jobs is not None:
            result['Jobs'] = self.jobs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Jobs') is not None:
            self.jobs = m.get('Jobs')
        return self


class StopJobsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopJobsResponseBody, self).to_map()
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


class StopJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopJobsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitJobRequest(TeaModel):
    def __init__(self, array_request=None, cluster_id=None, command_line=None, name=None, package_path=None,
                 priority=None, re_runable=None, runas_user=None, runas_user_password=None, stderr_redirect_path=None,
                 stdout_redirect_path=None, variables=None):
        self.array_request = array_request  # type: str
        self.cluster_id = cluster_id  # type: str
        self.command_line = command_line  # type: str
        self.name = name  # type: str
        self.package_path = package_path  # type: str
        self.priority = priority  # type: int
        self.re_runable = re_runable  # type: bool
        self.runas_user = runas_user  # type: str
        self.runas_user_password = runas_user_password  # type: str
        self.stderr_redirect_path = stderr_redirect_path  # type: str
        self.stdout_redirect_path = stdout_redirect_path  # type: str
        self.variables = variables  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.command_line is not None:
            result['CommandLine'] = self.command_line
        if self.name is not None:
            result['Name'] = self.name
        if self.package_path is not None:
            result['PackagePath'] = self.package_path
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.re_runable is not None:
            result['ReRunable'] = self.re_runable
        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user
        if self.runas_user_password is not None:
            result['RunasUserPassword'] = self.runas_user_password
        if self.stderr_redirect_path is not None:
            result['StderrRedirectPath'] = self.stderr_redirect_path
        if self.stdout_redirect_path is not None:
            result['StdoutRedirectPath'] = self.stdout_redirect_path
        if self.variables is not None:
            result['Variables'] = self.variables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackagePath') is not None:
            self.package_path = m.get('PackagePath')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ReRunable') is not None:
            self.re_runable = m.get('ReRunable')
        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')
        if m.get('RunasUserPassword') is not None:
            self.runas_user_password = m.get('RunasUserPassword')
        if m.get('StderrRedirectPath') is not None:
            self.stderr_redirect_path = m.get('StderrRedirectPath')
        if m.get('StdoutRedirectPath') is not None:
            self.stdout_redirect_path = m.get('StdoutRedirectPath')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        return self


class SubmitJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        self.job_id = job_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitJobResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeClientRequest(TeaModel):
    def __init__(self, client_version=None, cluster_id=None):
        self.client_version = client_version  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeClientRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class UpgradeClientResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeClientResponseBody, self).to_map()
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


class UpgradeClientResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpgradeClientResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeClientResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpgradeClientResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


