# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DescribeJobRequest(TeaModel):
    def __init__(self, cluster_id=None, job_id=None):
        self.cluster_id = cluster_id  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DescribeJobResponseBodyMessage(TeaModel):
    def __init__(self, job_info=None):
        self.job_info = job_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeJobResponseBodyMessage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_info is not None:
            result['JobInfo'] = self.job_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobInfo') is not None:
            self.job_info = m.get('JobInfo')
        return self


class DescribeJobResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None):
        self.request_id = request_id  # type: str
        self.message = message  # type: DescribeJobResponseBodyMessage

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        _map = super(DescribeJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            temp_model = DescribeJobResponseBodyMessage()
            self.message = temp_model.from_map(m['Message'])
        return self


class DescribeJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeJobResponse, self).to_map()
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
            temp_model = DescribeJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageRequest(TeaModel):
    def __init__(self, cluster_id=None, repository=None, image_tag=None, container_type=None):
        self.cluster_id = cluster_id  # type: str
        self.repository = repository  # type: str
        self.image_tag = image_tag  # type: str
        self.container_type = container_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.repository is not None:
            result['Repository'] = self.repository
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.container_type is not None:
            result['ContainerType'] = self.container_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('ContainerType') is not None:
            self.container_type = m.get('ContainerType')
        return self


class DeleteImageResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageResponseBody, self).to_map()
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


class DeleteImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteImageResponse, self).to_map()
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
            temp_model = DeleteImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGWSClusterRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGWSClusterRequest, self).to_map()
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


class DeleteGWSClusterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGWSClusterResponseBody, self).to_map()
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


class DeleteGWSClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteGWSClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGWSClusterResponse, self).to_map()
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
            temp_model = DeleteGWSClusterResponseBody()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    def __init__(self, tag=None, name=None, version=None):
        self.tag = tag  # type: str
        self.name = name  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterResponseBodyClusterInfoApplicationsApplicationInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.name is not None:
            result['Name'] = self.name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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


class DescribeClusterResponseBodyClusterInfoPostInstallScriptsPostInstallScriptInfo(TeaModel):
    def __init__(self, url=None, args=None):
        self.url = url  # type: str
        self.args = args  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterResponseBodyClusterInfoPostInstallScriptsPostInstallScriptInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.args is not None:
            result['Args'] = self.args
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Args') is not None:
            self.args = m.get('Args')
        return self


class DescribeClusterResponseBodyClusterInfoPostInstallScripts(TeaModel):
    def __init__(self, post_install_script_info=None):
        self.post_install_script_info = post_install_script_info  # type: list[DescribeClusterResponseBodyClusterInfoPostInstallScriptsPostInstallScriptInfo]

    def validate(self):
        if self.post_install_script_info:
            for k in self.post_install_script_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterResponseBodyClusterInfoPostInstallScripts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PostInstallScriptInfo'] = []
        if self.post_install_script_info is not None:
            for k in self.post_install_script_info:
                result['PostInstallScriptInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.post_install_script_info = []
        if m.get('PostInstallScriptInfo') is not None:
            for k in m.get('PostInstallScriptInfo'):
                temp_model = DescribeClusterResponseBodyClusterInfoPostInstallScriptsPostInstallScriptInfo()
                self.post_install_script_info.append(temp_model.from_map(k))
        return self


class DescribeClusterResponseBodyClusterInfoEcsInfoManager(TeaModel):
    def __init__(self, instance_type=None, count=None):
        self.instance_type = instance_type  # type: str
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterResponseBodyClusterInfoEcsInfoManager, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeClusterResponseBodyClusterInfoEcsInfoCompute(TeaModel):
    def __init__(self, instance_type=None, count=None):
        self.instance_type = instance_type  # type: str
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterResponseBodyClusterInfoEcsInfoCompute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeClusterResponseBodyClusterInfoEcsInfoLogin(TeaModel):
    def __init__(self, instance_type=None, count=None):
        self.instance_type = instance_type  # type: str
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterResponseBodyClusterInfoEcsInfoLogin, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeClusterResponseBodyClusterInfoEcsInfo(TeaModel):
    def __init__(self, manager=None, compute=None, login=None):
        self.manager = manager  # type: DescribeClusterResponseBodyClusterInfoEcsInfoManager
        self.compute = compute  # type: DescribeClusterResponseBodyClusterInfoEcsInfoCompute
        self.login = login  # type: DescribeClusterResponseBodyClusterInfoEcsInfoLogin

    def validate(self):
        if self.manager:
            self.manager.validate()
        if self.compute:
            self.compute.validate()
        if self.login:
            self.login.validate()

    def to_map(self):
        _map = super(DescribeClusterResponseBodyClusterInfoEcsInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['Manager'] = self.manager.to_map()
        if self.compute is not None:
            result['Compute'] = self.compute.to_map()
        if self.login is not None:
            result['Login'] = self.login.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Manager') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoEcsInfoManager()
            self.manager = temp_model.from_map(m['Manager'])
        if m.get('Compute') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoEcsInfoCompute()
            self.compute = temp_model.from_map(m['Compute'])
        if m.get('Login') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoEcsInfoLogin()
            self.login = temp_model.from_map(m['Login'])
        return self


class DescribeClusterResponseBodyClusterInfo(TeaModel):
    def __init__(self, status=None, vpc_id=None, key_pair_name=None, ecs_charge_type=None, security_group_id=None,
                 scc_cluster_id=None, create_time=None, account_type=None, volume_protocol=None, description=None, volume_id=None,
                 ha_enable=None, base_os_tag=None, name=None, image_id=None, scheduler_type=None, deploy_mode=None,
                 image_owner_alias=None, os_tag=None, volume_mountpoint=None, remote_directory=None, region_id=None, v_switch_id=None,
                 image_name=None, volume_type=None, location=None, id=None, client_version=None, applications=None,
                 post_install_scripts=None, ecs_info=None):
        self.status = status  # type: str
        self.vpc_id = vpc_id  # type: str
        self.key_pair_name = key_pair_name  # type: str
        self.ecs_charge_type = ecs_charge_type  # type: str
        self.security_group_id = security_group_id  # type: str
        self.scc_cluster_id = scc_cluster_id  # type: str
        self.create_time = create_time  # type: str
        self.account_type = account_type  # type: str
        self.volume_protocol = volume_protocol  # type: str
        self.description = description  # type: str
        self.volume_id = volume_id  # type: str
        self.ha_enable = ha_enable  # type: bool
        self.base_os_tag = base_os_tag  # type: str
        self.name = name  # type: str
        self.image_id = image_id  # type: str
        self.scheduler_type = scheduler_type  # type: str
        self.deploy_mode = deploy_mode  # type: str
        self.image_owner_alias = image_owner_alias  # type: str
        self.os_tag = os_tag  # type: str
        self.volume_mountpoint = volume_mountpoint  # type: str
        self.remote_directory = remote_directory  # type: str
        self.region_id = region_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.image_name = image_name  # type: str
        self.volume_type = volume_type  # type: str
        self.location = location  # type: str
        self.id = id  # type: str
        self.client_version = client_version  # type: str
        self.applications = applications  # type: DescribeClusterResponseBodyClusterInfoApplications
        self.post_install_scripts = post_install_scripts  # type: DescribeClusterResponseBodyClusterInfoPostInstallScripts
        self.ecs_info = ecs_info  # type: DescribeClusterResponseBodyClusterInfoEcsInfo

    def validate(self):
        if self.applications:
            self.applications.validate()
        if self.post_install_scripts:
            self.post_install_scripts.validate()
        if self.ecs_info:
            self.ecs_info.validate()

    def to_map(self):
        _map = super(DescribeClusterResponseBodyClusterInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.ecs_charge_type is not None:
            result['EcsChargeType'] = self.ecs_charge_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.scc_cluster_id is not None:
            result['SccClusterId'] = self.scc_cluster_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.description is not None:
            result['Description'] = self.description
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        if self.ha_enable is not None:
            result['HaEnable'] = self.ha_enable
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag
        if self.name is not None:
            result['Name'] = self.name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        if self.location is not None:
            result['Location'] = self.location
        if self.id is not None:
            result['Id'] = self.id
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.applications is not None:
            result['Applications'] = self.applications.to_map()
        if self.post_install_scripts is not None:
            result['PostInstallScripts'] = self.post_install_scripts.to_map()
        if self.ecs_info is not None:
            result['EcsInfo'] = self.ecs_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('EcsChargeType') is not None:
            self.ecs_charge_type = m.get('EcsChargeType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SccClusterId') is not None:
            self.scc_cluster_id = m.get('SccClusterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        if m.get('HaEnable') is not None:
            self.ha_enable = m.get('HaEnable')
        if m.get('BaseOsTag') is not None:
            self.base_os_tag = m.get('BaseOsTag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('Applications') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoApplications()
            self.applications = temp_model.from_map(m['Applications'])
        if m.get('PostInstallScripts') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoPostInstallScripts()
            self.post_install_scripts = temp_model.from_map(m['PostInstallScripts'])
        if m.get('EcsInfo') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfoEcsInfo()
            self.ecs_info = temp_model.from_map(m['EcsInfo'])
        return self


class DescribeClusterResponseBody(TeaModel):
    def __init__(self, request_id=None, cluster_info=None):
        self.request_id = request_id  # type: str
        self.cluster_info = cluster_info  # type: DescribeClusterResponseBodyClusterInfo

    def validate(self):
        if self.cluster_info:
            self.cluster_info.validate()

    def to_map(self):
        _map = super(DescribeClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClusterInfo') is not None:
            temp_model = DescribeClusterResponseBodyClusterInfo()
            self.cluster_info = temp_model.from_map(m['ClusterInfo'])
        return self


class DescribeClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeClusterResponseBody()
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
    def __init__(self, name=None, add_time=None, group=None):
        self.name = name  # type: str
        self.add_time = add_time  # type: str
        self.group = group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersResponseBodyUsersUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.add_time is not None:
            result['AddTime'] = self.add_time
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')
        if m.get('Group') is not None:
            self.group = m.get('Group')
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
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, users=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.users is not None:
            result['Users'] = self.users.to_map()
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
        if m.get('Users') is not None:
            temp_model = ListUsersResponseBodyUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class ListUsersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerAppRequest(TeaModel):
    def __init__(self, container_id=None):
        self.container_id = container_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        return self


class DescribeContainerAppResponseBodyContainerAppInfo(TeaModel):
    def __init__(self, type=None, description=None, create_time=None, repository=None, image_tag=None, name=None,
                 id=None):
        self.type = type  # type: str
        self.description = description  # type: str
        self.create_time = create_time  # type: str
        self.repository = repository  # type: str
        self.image_tag = image_tag  # type: str
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeContainerAppResponseBodyContainerAppInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.description is not None:
            result['Description'] = self.description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.repository is not None:
            result['Repository'] = self.repository
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeContainerAppResponseBody(TeaModel):
    def __init__(self, request_id=None, container_app_info=None):
        self.request_id = request_id  # type: str
        self.container_app_info = container_app_info  # type: DescribeContainerAppResponseBodyContainerAppInfo

    def validate(self):
        if self.container_app_info:
            self.container_app_info.validate()

    def to_map(self):
        _map = super(DescribeContainerAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.container_app_info is not None:
            result['ContainerAppInfo'] = self.container_app_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ContainerAppInfo') is not None:
            temp_model = DescribeContainerAppResponseBodyContainerAppInfo()
            self.container_app_info = temp_model.from_map(m['ContainerAppInfo'])
        return self


class DescribeContainerAppResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeContainerAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeContainerAppResponse, self).to_map()
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
            temp_model = DescribeContainerAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PullImageRequest(TeaModel):
    def __init__(self, cluster_id=None, repository=None, image_tag=None, container_type=None):
        self.cluster_id = cluster_id  # type: str
        self.repository = repository  # type: str
        self.image_tag = image_tag  # type: str
        self.container_type = container_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PullImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.repository is not None:
            result['Repository'] = self.repository
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.container_type is not None:
            result['ContainerType'] = self.container_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('ContainerType') is not None:
            self.container_type = m.get('ContainerType')
        return self


class PullImageResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PullImageResponseBody, self).to_map()
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


class PullImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PullImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PullImageResponse, self).to_map()
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
            temp_model = PullImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopNodesRequestInstance(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopNodesRequestInstance, self).to_map()
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


class StopNodesRequest(TeaModel):
    def __init__(self, cluster_id=None, role=None, instance=None):
        self.cluster_id = cluster_id  # type: str
        self.role = role  # type: str
        self.instance = instance  # type: list[StopNodesRequestInstance]

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(StopNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.role is not None:
            result['Role'] = self.role
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = StopNodesRequestInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class StopNodesResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None):
        self.task_id = task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopNodesResponseBody, self).to_map()
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


class StopNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopNodesResponse, self).to_map()
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
            temp_model = StopNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodesByQueueRequest(TeaModel):
    def __init__(self, cluster_id=None, queue_name=None, page_number=None, page_size=None):
        self.cluster_id = cluster_id  # type: str
        self.queue_name = queue_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesByQueueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListNodesByQueueResponseBodyNodesNodeInfoTotalResources(TeaModel):
    def __init__(self, gpu=None, cpu=None, memory=None):
        self.gpu = gpu  # type: int
        self.cpu = cpu  # type: int
        self.memory = memory  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesByQueueResponseBodyNodesNodeInfoTotalResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ListNodesByQueueResponseBodyNodesNodeInfoUsedResources(TeaModel):
    def __init__(self, gpu=None, cpu=None, memory=None):
        self.gpu = gpu  # type: int
        self.cpu = cpu  # type: int
        self.memory = memory  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesByQueueResponseBodyNodesNodeInfoUsedResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ListNodesByQueueResponseBodyNodesNodeInfo(TeaModel):
    def __init__(self, vpc_id=None, status=None, ht_enabled=None, expired=None, image_owner_alias=None,
                 lock_reason=None, host_name=None, public_ip_address=None, spot_strategy=None, created_by_ehpc=None,
                 region_id=None, v_switch_id=None, ip_address=None, expired_time=None, version=None, zone_id=None,
                 add_time=None, image_id=None, location=None, id=None, create_mode=None, total_resources=None,
                 used_resources=None):
        self.vpc_id = vpc_id  # type: str
        self.status = status  # type: str
        self.ht_enabled = ht_enabled  # type: bool
        self.expired = expired  # type: bool
        self.image_owner_alias = image_owner_alias  # type: str
        self.lock_reason = lock_reason  # type: str
        self.host_name = host_name  # type: str
        self.public_ip_address = public_ip_address  # type: str
        self.spot_strategy = spot_strategy  # type: str
        self.created_by_ehpc = created_by_ehpc  # type: bool
        self.region_id = region_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.ip_address = ip_address  # type: str
        self.expired_time = expired_time  # type: str
        self.version = version  # type: str
        self.zone_id = zone_id  # type: str
        self.add_time = add_time  # type: str
        self.image_id = image_id  # type: str
        self.location = location  # type: str
        self.id = id  # type: str
        self.create_mode = create_mode  # type: str
        self.total_resources = total_resources  # type: ListNodesByQueueResponseBodyNodesNodeInfoTotalResources
        self.used_resources = used_resources  # type: ListNodesByQueueResponseBodyNodesNodeInfoUsedResources

    def validate(self):
        if self.total_resources:
            self.total_resources.validate()
        if self.used_resources:
            self.used_resources.validate()

    def to_map(self):
        _map = super(ListNodesByQueueResponseBodyNodesNodeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.status is not None:
            result['Status'] = self.status
        if self.ht_enabled is not None:
            result['HtEnabled'] = self.ht_enabled
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.created_by_ehpc is not None:
            result['CreatedByEhpc'] = self.created_by_ehpc
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.version is not None:
            result['Version'] = self.version
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.add_time is not None:
            result['AddTime'] = self.add_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.location is not None:
            result['Location'] = self.location
        if self.id is not None:
            result['Id'] = self.id
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.total_resources is not None:
            result['TotalResources'] = self.total_resources.to_map()
        if self.used_resources is not None:
            result['UsedResources'] = self.used_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('HtEnabled') is not None:
            self.ht_enabled = m.get('HtEnabled')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('CreatedByEhpc') is not None:
            self.created_by_ehpc = m.get('CreatedByEhpc')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('TotalResources') is not None:
            temp_model = ListNodesByQueueResponseBodyNodesNodeInfoTotalResources()
            self.total_resources = temp_model.from_map(m['TotalResources'])
        if m.get('UsedResources') is not None:
            temp_model = ListNodesByQueueResponseBodyNodesNodeInfoUsedResources()
            self.used_resources = temp_model.from_map(m['UsedResources'])
        return self


class ListNodesByQueueResponseBodyNodes(TeaModel):
    def __init__(self, node_info=None):
        self.node_info = node_info  # type: list[ListNodesByQueueResponseBodyNodesNodeInfo]

    def validate(self):
        if self.node_info:
            for k in self.node_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNodesByQueueResponseBodyNodes, self).to_map()
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
                temp_model = ListNodesByQueueResponseBodyNodesNodeInfo()
                self.node_info.append(temp_model.from_map(k))
        return self


class ListNodesByQueueResponseBody(TeaModel):
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, nodes=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.nodes = nodes  # type: ListNodesByQueueResponseBodyNodes

    def validate(self):
        if self.nodes:
            self.nodes.validate()

    def to_map(self):
        _map = super(ListNodesByQueueResponseBody, self).to_map()
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
        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()
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
        if m.get('Nodes') is not None:
            temp_model = ListNodesByQueueResponseBodyNodes()
            self.nodes = temp_model.from_map(m['Nodes'])
        return self


class ListNodesByQueueResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListNodesByQueueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNodesByQueueResponse, self).to_map()
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
            temp_model = ListNodesByQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyContainerAppAttributesRequest(TeaModel):
    def __init__(self, container_id=None, description=None):
        self.container_id = container_id  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyContainerAppAttributesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifyContainerAppAttributesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyContainerAppAttributesResponseBody, self).to_map()
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


class ModifyContainerAppAttributesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyContainerAppAttributesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyContainerAppAttributesResponse, self).to_map()
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
            temp_model = ModifyContainerAppAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSchedulerInfoRequestPbsInfoAclLimit(TeaModel):
    def __init__(self, queue=None, acl_users=None):
        self.queue = queue  # type: str
        self.acl_users = acl_users  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSchedulerInfoRequestPbsInfoAclLimit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.acl_users is not None:
            result['AclUsers'] = self.acl_users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('AclUsers') is not None:
            self.acl_users = m.get('AclUsers')
        return self


class SetSchedulerInfoRequestPbsInfoResourceLimit(TeaModel):
    def __init__(self, nodes=None, cpus=None, user=None, queue=None, mem=None):
        self.nodes = nodes  # type: int
        self.cpus = cpus  # type: int
        self.user = user  # type: str
        self.queue = queue  # type: str
        self.mem = mem  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSchedulerInfoRequestPbsInfoResourceLimit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        if self.cpus is not None:
            result['Cpus'] = self.cpus
        if self.user is not None:
            result['User'] = self.user
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.mem is not None:
            result['Mem'] = self.mem
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        if m.get('Cpus') is not None:
            self.cpus = m.get('Cpus')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        return self


class SetSchedulerInfoRequestPbsInfo(TeaModel):
    def __init__(self, acl_limit=None, resource_limit=None, job_history_duration=None, sched_interval=None):
        self.acl_limit = acl_limit  # type: list[SetSchedulerInfoRequestPbsInfoAclLimit]
        self.resource_limit = resource_limit  # type: list[SetSchedulerInfoRequestPbsInfoResourceLimit]
        self.job_history_duration = job_history_duration  # type: int
        self.sched_interval = sched_interval  # type: int

    def validate(self):
        if self.acl_limit:
            for k in self.acl_limit:
                if k:
                    k.validate()
        if self.resource_limit:
            for k in self.resource_limit:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SetSchedulerInfoRequestPbsInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclLimit'] = []
        if self.acl_limit is not None:
            for k in self.acl_limit:
                result['AclLimit'].append(k.to_map() if k else None)
        result['ResourceLimit'] = []
        if self.resource_limit is not None:
            for k in self.resource_limit:
                result['ResourceLimit'].append(k.to_map() if k else None)
        if self.job_history_duration is not None:
            result['JobHistoryDuration'] = self.job_history_duration
        if self.sched_interval is not None:
            result['SchedInterval'] = self.sched_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.acl_limit = []
        if m.get('AclLimit') is not None:
            for k in m.get('AclLimit'):
                temp_model = SetSchedulerInfoRequestPbsInfoAclLimit()
                self.acl_limit.append(temp_model.from_map(k))
        self.resource_limit = []
        if m.get('ResourceLimit') is not None:
            for k in m.get('ResourceLimit'):
                temp_model = SetSchedulerInfoRequestPbsInfoResourceLimit()
                self.resource_limit.append(temp_model.from_map(k))
        if m.get('JobHistoryDuration') is not None:
            self.job_history_duration = m.get('JobHistoryDuration')
        if m.get('SchedInterval') is not None:
            self.sched_interval = m.get('SchedInterval')
        return self


class SetSchedulerInfoRequestSlurmInfo(TeaModel):
    def __init__(self, backfill_interval=None, sched_interval=None):
        self.backfill_interval = backfill_interval  # type: int
        self.sched_interval = sched_interval  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSchedulerInfoRequestSlurmInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backfill_interval is not None:
            result['BackfillInterval'] = self.backfill_interval
        if self.sched_interval is not None:
            result['SchedInterval'] = self.sched_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BackfillInterval') is not None:
            self.backfill_interval = m.get('BackfillInterval')
        if m.get('SchedInterval') is not None:
            self.sched_interval = m.get('SchedInterval')
        return self


class SetSchedulerInfoRequestScheduler(TeaModel):
    def __init__(self, sched_name=None):
        self.sched_name = sched_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSchedulerInfoRequestScheduler, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sched_name is not None:
            result['SchedName'] = self.sched_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SchedName') is not None:
            self.sched_name = m.get('SchedName')
        return self


class SetSchedulerInfoRequest(TeaModel):
    def __init__(self, region_id=None, cluster_id=None, pbs_info=None, slurm_info=None, scheduler=None):
        self.region_id = region_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.pbs_info = pbs_info  # type: list[SetSchedulerInfoRequestPbsInfo]
        self.slurm_info = slurm_info  # type: list[SetSchedulerInfoRequestSlurmInfo]
        self.scheduler = scheduler  # type: list[SetSchedulerInfoRequestScheduler]

    def validate(self):
        if self.pbs_info:
            for k in self.pbs_info:
                if k:
                    k.validate()
        if self.slurm_info:
            for k in self.slurm_info:
                if k:
                    k.validate()
        if self.scheduler:
            for k in self.scheduler:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SetSchedulerInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['PbsInfo'] = []
        if self.pbs_info is not None:
            for k in self.pbs_info:
                result['PbsInfo'].append(k.to_map() if k else None)
        result['SlurmInfo'] = []
        if self.slurm_info is not None:
            for k in self.slurm_info:
                result['SlurmInfo'].append(k.to_map() if k else None)
        result['Scheduler'] = []
        if self.scheduler is not None:
            for k in self.scheduler:
                result['Scheduler'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.pbs_info = []
        if m.get('PbsInfo') is not None:
            for k in m.get('PbsInfo'):
                temp_model = SetSchedulerInfoRequestPbsInfo()
                self.pbs_info.append(temp_model.from_map(k))
        self.slurm_info = []
        if m.get('SlurmInfo') is not None:
            for k in m.get('SlurmInfo'):
                temp_model = SetSchedulerInfoRequestSlurmInfo()
                self.slurm_info.append(temp_model.from_map(k))
        self.scheduler = []
        if m.get('Scheduler') is not None:
            for k in m.get('Scheduler'):
                temp_model = SetSchedulerInfoRequestScheduler()
                self.scheduler.append(temp_model.from_map(k))
        return self


class SetSchedulerInfoResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetSchedulerInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetSchedulerInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetSchedulerInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetSchedulerInfoResponse, self).to_map()
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
            temp_model = SetSchedulerInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCloudMetricProfilingRequest(TeaModel):
    def __init__(self, region_id=None, cluster_id=None, profiling_id=None):
        self.region_id = region_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.profiling_id = profiling_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCloudMetricProfilingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.profiling_id is not None:
            result['ProfilingId'] = self.profiling_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ProfilingId') is not None:
            self.profiling_id = m.get('ProfilingId')
        return self


class GetCloudMetricProfilingResponseBodySvgUrlsSvgInfo(TeaModel):
    def __init__(self, type=None, url=None, name=None, size=None):
        self.type = type  # type: str
        self.url = url  # type: str
        self.name = name  # type: str
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCloudMetricProfilingResponseBodySvgUrlsSvgInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.name is not None:
            result['Name'] = self.name
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class GetCloudMetricProfilingResponseBodySvgUrls(TeaModel):
    def __init__(self, svg_info=None):
        self.svg_info = svg_info  # type: list[GetCloudMetricProfilingResponseBodySvgUrlsSvgInfo]

    def validate(self):
        if self.svg_info:
            for k in self.svg_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCloudMetricProfilingResponseBodySvgUrls, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SvgInfo'] = []
        if self.svg_info is not None:
            for k in self.svg_info:
                result['SvgInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.svg_info = []
        if m.get('SvgInfo') is not None:
            for k in m.get('SvgInfo'):
                temp_model = GetCloudMetricProfilingResponseBodySvgUrlsSvgInfo()
                self.svg_info.append(temp_model.from_map(k))
        return self


class GetCloudMetricProfilingResponseBody(TeaModel):
    def __init__(self, request_id=None, svg_urls=None):
        self.request_id = request_id  # type: str
        self.svg_urls = svg_urls  # type: GetCloudMetricProfilingResponseBodySvgUrls

    def validate(self):
        if self.svg_urls:
            self.svg_urls.validate()

    def to_map(self):
        _map = super(GetCloudMetricProfilingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.svg_urls is not None:
            result['SvgUrls'] = self.svg_urls.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SvgUrls') is not None:
            temp_model = GetCloudMetricProfilingResponseBodySvgUrls()
            self.svg_urls = temp_model.from_map(m['SvgUrls'])
        return self


class GetCloudMetricProfilingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetCloudMetricProfilingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCloudMetricProfilingResponse, self).to_map()
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
            temp_model = GetCloudMetricProfilingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImagePriceRequest(TeaModel):
    def __init__(self, image_id=None, price_unit=None, sku_code=None, period=None, amount=None, order_type=None):
        self.image_id = image_id  # type: str
        self.price_unit = price_unit  # type: str
        self.sku_code = sku_code  # type: str
        self.period = period  # type: int
        self.amount = amount  # type: int
        self.order_type = order_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImagePriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.sku_code is not None:
            result['SkuCode'] = self.sku_code
        if self.period is not None:
            result['Period'] = self.period
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('SkuCode') is not None:
            self.sku_code = m.get('SkuCode')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        return self


class DescribeImagePriceResponseBody(TeaModel):
    def __init__(self, amount=None, request_id=None, discount_price=None, trade_price=None, original_price=None,
                 image_id=None):
        self.amount = amount  # type: int
        self.request_id = request_id  # type: str
        self.discount_price = discount_price  # type: float
        self.trade_price = trade_price  # type: float
        self.original_price = original_price  # type: float
        self.image_id = image_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImagePriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class DescribeImagePriceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeImagePriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeImagePriceResponse, self).to_map()
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
            temp_model = DescribeImagePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopGWSInstanceRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopGWSInstanceRequest, self).to_map()
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


class StopGWSInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopGWSInstanceResponseBody, self).to_map()
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


class StopGWSInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopGWSInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopGWSInstanceResponse, self).to_map()
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
            temp_model = StopGWSInstanceResponseBody()
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


class GetAutoScaleConfigResponseBodyQueuesQueueInfoInstanceTypesInstanceTypeInfo(TeaModel):
    def __init__(self, host_name_prefix=None, v_switch_id=None, zone_id=None, spot_price_limit=None,
                 instance_type=None, spot_strategy=None):
        self.host_name_prefix = host_name_prefix  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str
        self.spot_price_limit = spot_price_limit  # type: float
        self.instance_type = instance_type  # type: str
        self.spot_strategy = spot_strategy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAutoScaleConfigResponseBodyQueuesQueueInfoInstanceTypesInstanceTypeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_name_prefix is not None:
            result['HostNamePrefix'] = self.host_name_prefix
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostNamePrefix') is not None:
            self.host_name_prefix = m.get('HostNamePrefix')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        return self


class GetAutoScaleConfigResponseBodyQueuesQueueInfoInstanceTypes(TeaModel):
    def __init__(self, instance_type_info=None):
        self.instance_type_info = instance_type_info  # type: list[GetAutoScaleConfigResponseBodyQueuesQueueInfoInstanceTypesInstanceTypeInfo]

    def validate(self):
        if self.instance_type_info:
            for k in self.instance_type_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAutoScaleConfigResponseBodyQueuesQueueInfoInstanceTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceTypeInfo'] = []
        if self.instance_type_info is not None:
            for k in self.instance_type_info:
                result['InstanceTypeInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_type_info = []
        if m.get('InstanceTypeInfo') is not None:
            for k in m.get('InstanceTypeInfo'):
                temp_model = GetAutoScaleConfigResponseBodyQueuesQueueInfoInstanceTypesInstanceTypeInfo()
                self.instance_type_info.append(temp_model.from_map(k))
        return self


class GetAutoScaleConfigResponseBodyQueuesQueueInfo(TeaModel):
    def __init__(self, queue_image_id=None, system_disk_category=None, instance_type=None, host_name_suffix=None,
                 spot_strategy=None, min_nodes_in_queue=None, host_name_prefix=None, system_disk_size=None,
                 max_nodes_in_queue=None, enable_auto_shrink=None, queue_name=None, enable_auto_grow=None, system_disk_level=None,
                 resource_group_id=None, spot_price_limit=None, instance_types=None):
        self.queue_image_id = queue_image_id  # type: str
        self.system_disk_category = system_disk_category  # type: str
        self.instance_type = instance_type  # type: str
        self.host_name_suffix = host_name_suffix  # type: str
        self.spot_strategy = spot_strategy  # type: str
        self.min_nodes_in_queue = min_nodes_in_queue  # type: int
        self.host_name_prefix = host_name_prefix  # type: str
        self.system_disk_size = system_disk_size  # type: int
        self.max_nodes_in_queue = max_nodes_in_queue  # type: int
        self.enable_auto_shrink = enable_auto_shrink  # type: bool
        self.queue_name = queue_name  # type: str
        self.enable_auto_grow = enable_auto_grow  # type: bool
        self.system_disk_level = system_disk_level  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.spot_price_limit = spot_price_limit  # type: float
        self.instance_types = instance_types  # type: GetAutoScaleConfigResponseBodyQueuesQueueInfoInstanceTypes

    def validate(self):
        if self.instance_types:
            self.instance_types.validate()

    def to_map(self):
        _map = super(GetAutoScaleConfigResponseBodyQueuesQueueInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue_image_id is not None:
            result['QueueImageId'] = self.queue_image_id
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.host_name_suffix is not None:
            result['HostNameSuffix'] = self.host_name_suffix
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.min_nodes_in_queue is not None:
            result['MinNodesInQueue'] = self.min_nodes_in_queue
        if self.host_name_prefix is not None:
            result['HostNamePrefix'] = self.host_name_prefix
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.max_nodes_in_queue is not None:
            result['MaxNodesInQueue'] = self.max_nodes_in_queue
        if self.enable_auto_shrink is not None:
            result['EnableAutoShrink'] = self.enable_auto_shrink
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.enable_auto_grow is not None:
            result['EnableAutoGrow'] = self.enable_auto_grow
        if self.system_disk_level is not None:
            result['SystemDiskLevel'] = self.system_disk_level
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QueueImageId') is not None:
            self.queue_image_id = m.get('QueueImageId')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('HostNameSuffix') is not None:
            self.host_name_suffix = m.get('HostNameSuffix')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('MinNodesInQueue') is not None:
            self.min_nodes_in_queue = m.get('MinNodesInQueue')
        if m.get('HostNamePrefix') is not None:
            self.host_name_prefix = m.get('HostNamePrefix')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('MaxNodesInQueue') is not None:
            self.max_nodes_in_queue = m.get('MaxNodesInQueue')
        if m.get('EnableAutoShrink') is not None:
            self.enable_auto_shrink = m.get('EnableAutoShrink')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('EnableAutoGrow') is not None:
            self.enable_auto_grow = m.get('EnableAutoGrow')
        if m.get('SystemDiskLevel') is not None:
            self.system_disk_level = m.get('SystemDiskLevel')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('InstanceTypes') is not None:
            temp_model = GetAutoScaleConfigResponseBodyQueuesQueueInfoInstanceTypes()
            self.instance_types = temp_model.from_map(m['InstanceTypes'])
        return self


class GetAutoScaleConfigResponseBodyQueues(TeaModel):
    def __init__(self, queue_info=None):
        self.queue_info = queue_info  # type: list[GetAutoScaleConfigResponseBodyQueuesQueueInfo]

    def validate(self):
        if self.queue_info:
            for k in self.queue_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAutoScaleConfigResponseBodyQueues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QueueInfo'] = []
        if self.queue_info is not None:
            for k in self.queue_info:
                result['QueueInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.queue_info = []
        if m.get('QueueInfo') is not None:
            for k in m.get('QueueInfo'):
                temp_model = GetAutoScaleConfigResponseBodyQueuesQueueInfo()
                self.queue_info.append(temp_model.from_map(k))
        return self


class GetAutoScaleConfigResponseBody(TeaModel):
    def __init__(self, max_nodes_in_cluster=None, grow_timeout_in_minutes=None, spot_strategy=None,
                 enable_auto_shrink=None, request_id=None, enable_auto_grow=None, cluster_type=None, exclude_nodes=None,
                 shrink_interval_in_minutes=None, grow_interval_in_minutes=None, spot_price_limit=None, extra_nodes_grow_ratio=None,
                 shrink_idle_times=None, image_id=None, grow_ratio=None, cluster_id=None, uid=None, queues=None):
        self.max_nodes_in_cluster = max_nodes_in_cluster  # type: int
        self.grow_timeout_in_minutes = grow_timeout_in_minutes  # type: int
        self.spot_strategy = spot_strategy  # type: str
        self.enable_auto_shrink = enable_auto_shrink  # type: bool
        self.request_id = request_id  # type: str
        self.enable_auto_grow = enable_auto_grow  # type: bool
        self.cluster_type = cluster_type  # type: str
        self.exclude_nodes = exclude_nodes  # type: str
        self.shrink_interval_in_minutes = shrink_interval_in_minutes  # type: int
        self.grow_interval_in_minutes = grow_interval_in_minutes  # type: int
        self.spot_price_limit = spot_price_limit  # type: float
        self.extra_nodes_grow_ratio = extra_nodes_grow_ratio  # type: int
        self.shrink_idle_times = shrink_idle_times  # type: int
        self.image_id = image_id  # type: str
        self.grow_ratio = grow_ratio  # type: int
        self.cluster_id = cluster_id  # type: str
        self.uid = uid  # type: str
        self.queues = queues  # type: GetAutoScaleConfigResponseBodyQueues

    def validate(self):
        if self.queues:
            self.queues.validate()

    def to_map(self):
        _map = super(GetAutoScaleConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_nodes_in_cluster is not None:
            result['MaxNodesInCluster'] = self.max_nodes_in_cluster
        if self.grow_timeout_in_minutes is not None:
            result['GrowTimeoutInMinutes'] = self.grow_timeout_in_minutes
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.enable_auto_shrink is not None:
            result['EnableAutoShrink'] = self.enable_auto_shrink
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.enable_auto_grow is not None:
            result['EnableAutoGrow'] = self.enable_auto_grow
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.exclude_nodes is not None:
            result['ExcludeNodes'] = self.exclude_nodes
        if self.shrink_interval_in_minutes is not None:
            result['ShrinkIntervalInMinutes'] = self.shrink_interval_in_minutes
        if self.grow_interval_in_minutes is not None:
            result['GrowIntervalInMinutes'] = self.grow_interval_in_minutes
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.extra_nodes_grow_ratio is not None:
            result['ExtraNodesGrowRatio'] = self.extra_nodes_grow_ratio
        if self.shrink_idle_times is not None:
            result['ShrinkIdleTimes'] = self.shrink_idle_times
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.grow_ratio is not None:
            result['GrowRatio'] = self.grow_ratio
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.queues is not None:
            result['Queues'] = self.queues.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxNodesInCluster') is not None:
            self.max_nodes_in_cluster = m.get('MaxNodesInCluster')
        if m.get('GrowTimeoutInMinutes') is not None:
            self.grow_timeout_in_minutes = m.get('GrowTimeoutInMinutes')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('EnableAutoShrink') is not None:
            self.enable_auto_shrink = m.get('EnableAutoShrink')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EnableAutoGrow') is not None:
            self.enable_auto_grow = m.get('EnableAutoGrow')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ExcludeNodes') is not None:
            self.exclude_nodes = m.get('ExcludeNodes')
        if m.get('ShrinkIntervalInMinutes') is not None:
            self.shrink_interval_in_minutes = m.get('ShrinkIntervalInMinutes')
        if m.get('GrowIntervalInMinutes') is not None:
            self.grow_interval_in_minutes = m.get('GrowIntervalInMinutes')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('ExtraNodesGrowRatio') is not None:
            self.extra_nodes_grow_ratio = m.get('ExtraNodesGrowRatio')
        if m.get('ShrinkIdleTimes') is not None:
            self.shrink_idle_times = m.get('ShrinkIdleTimes')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('GrowRatio') is not None:
            self.grow_ratio = m.get('GrowRatio')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Queues') is not None:
            temp_model = GetAutoScaleConfigResponseBodyQueues()
            self.queues = temp_model.from_map(m['Queues'])
        return self


class GetAutoScaleConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAutoScaleConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAutoScaleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodesRequest(TeaModel):
    def __init__(self, cluster_id=None, role=None, host_name=None, page_number=None, page_size=None, sequence=None,
                 sort_by=None, filter=None, private_ip_address=None, host_name_prefix=None, host_name_suffix=None):
        self.cluster_id = cluster_id  # type: str
        self.role = role  # type: str
        self.host_name = host_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.sequence = sequence  # type: str
        self.sort_by = sort_by  # type: str
        self.filter = filter  # type: str
        self.private_ip_address = private_ip_address  # type: str
        self.host_name_prefix = host_name_prefix  # type: str
        self.host_name_suffix = host_name_suffix  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.role is not None:
            result['Role'] = self.role
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sequence is not None:
            result['Sequence'] = self.sequence
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.host_name_prefix is not None:
            result['HostNamePrefix'] = self.host_name_prefix
        if self.host_name_suffix is not None:
            result['HostNameSuffix'] = self.host_name_suffix
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('HostNamePrefix') is not None:
            self.host_name_prefix = m.get('HostNamePrefix')
        if m.get('HostNameSuffix') is not None:
            self.host_name_suffix = m.get('HostNameSuffix')
        return self


class ListNodesResponseBodyNodesNodeInfoRoles(TeaModel):
    def __init__(self, role=None):
        self.role = role  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesResponseBodyNodesNodeInfoRoles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class ListNodesResponseBodyNodesNodeInfoTotalResources(TeaModel):
    def __init__(self, gpu=None, cpu=None, memory=None):
        self.gpu = gpu  # type: int
        self.cpu = cpu  # type: int
        self.memory = memory  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesResponseBodyNodesNodeInfoTotalResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ListNodesResponseBodyNodesNodeInfoUsedResources(TeaModel):
    def __init__(self, gpu=None, cpu=None, memory=None):
        self.gpu = gpu  # type: int
        self.cpu = cpu  # type: int
        self.memory = memory  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesResponseBodyNodesNodeInfoUsedResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ListNodesResponseBodyNodesNodeInfo(TeaModel):
    def __init__(self, vpc_id=None, status=None, ht_enabled=None, expired=None, image_owner_alias=None,
                 lock_reason=None, host_name=None, instance_type=None, public_ip_address=None, spot_strategy=None,
                 created_by_ehpc=None, region_id=None, v_switch_id=None, ip_address=None, expired_time=None, version=None,
                 zone_id=None, add_time=None, image_id=None, location=None, id=None, create_mode=None, roles=None,
                 total_resources=None, used_resources=None):
        self.vpc_id = vpc_id  # type: str
        self.status = status  # type: str
        self.ht_enabled = ht_enabled  # type: bool
        self.expired = expired  # type: bool
        self.image_owner_alias = image_owner_alias  # type: str
        self.lock_reason = lock_reason  # type: str
        self.host_name = host_name  # type: str
        self.instance_type = instance_type  # type: str
        self.public_ip_address = public_ip_address  # type: str
        self.spot_strategy = spot_strategy  # type: str
        self.created_by_ehpc = created_by_ehpc  # type: bool
        self.region_id = region_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.ip_address = ip_address  # type: str
        self.expired_time = expired_time  # type: str
        self.version = version  # type: str
        self.zone_id = zone_id  # type: str
        self.add_time = add_time  # type: str
        self.image_id = image_id  # type: str
        self.location = location  # type: str
        self.id = id  # type: str
        self.create_mode = create_mode  # type: str
        self.roles = roles  # type: ListNodesResponseBodyNodesNodeInfoRoles
        self.total_resources = total_resources  # type: ListNodesResponseBodyNodesNodeInfoTotalResources
        self.used_resources = used_resources  # type: ListNodesResponseBodyNodesNodeInfoUsedResources

    def validate(self):
        if self.roles:
            self.roles.validate()
        if self.total_resources:
            self.total_resources.validate()
        if self.used_resources:
            self.used_resources.validate()

    def to_map(self):
        _map = super(ListNodesResponseBodyNodesNodeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.status is not None:
            result['Status'] = self.status
        if self.ht_enabled is not None:
            result['HtEnabled'] = self.ht_enabled
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.created_by_ehpc is not None:
            result['CreatedByEhpc'] = self.created_by_ehpc
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.version is not None:
            result['Version'] = self.version
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.add_time is not None:
            result['AddTime'] = self.add_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.location is not None:
            result['Location'] = self.location
        if self.id is not None:
            result['Id'] = self.id
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.roles is not None:
            result['Roles'] = self.roles.to_map()
        if self.total_resources is not None:
            result['TotalResources'] = self.total_resources.to_map()
        if self.used_resources is not None:
            result['UsedResources'] = self.used_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('HtEnabled') is not None:
            self.ht_enabled = m.get('HtEnabled')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('CreatedByEhpc') is not None:
            self.created_by_ehpc = m.get('CreatedByEhpc')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('Roles') is not None:
            temp_model = ListNodesResponseBodyNodesNodeInfoRoles()
            self.roles = temp_model.from_map(m['Roles'])
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
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, nodes=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.nodes = nodes  # type: ListNodesResponseBodyNodes

    def validate(self):
        if self.nodes:
            self.nodes.validate()

    def to_map(self):
        _map = super(ListNodesResponseBody, self).to_map()
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
        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()
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
        if m.get('Nodes') is not None:
            temp_model = ListNodesResponseBodyNodes()
            self.nodes = temp_model.from_map(m['Nodes'])
        return self


class ListNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCommandsRequest(TeaModel):
    def __init__(self, cluster_id=None, command_id=None, page_number=None, page_size=None):
        self.cluster_id = cluster_id  # type: str
        self.command_id = command_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCommandsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCommandsResponseBodyCommandsCommand(TeaModel):
    def __init__(self, timeout=None, command_id=None, working_dir=None, command_content=None):
        self.timeout = timeout  # type: str
        self.command_id = command_id  # type: str
        self.working_dir = working_dir  # type: str
        self.command_content = command_content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCommandsResponseBodyCommandsCommand, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        return self


class ListCommandsResponseBodyCommands(TeaModel):
    def __init__(self, command=None):
        self.command = command  # type: list[ListCommandsResponseBodyCommandsCommand]

    def validate(self):
        if self.command:
            for k in self.command:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCommandsResponseBodyCommands, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Command'] = []
        if self.command is not None:
            for k in self.command:
                result['Command'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.command = []
        if m.get('Command') is not None:
            for k in m.get('Command'):
                temp_model = ListCommandsResponseBodyCommandsCommand()
                self.command.append(temp_model.from_map(k))
        return self


class ListCommandsResponseBody(TeaModel):
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, commands=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.commands = commands  # type: ListCommandsResponseBodyCommands

    def validate(self):
        if self.commands:
            self.commands.validate()

    def to_map(self):
        _map = super(ListCommandsResponseBody, self).to_map()
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
        if self.commands is not None:
            result['Commands'] = self.commands.to_map()
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
        if m.get('Commands') is not None:
            temp_model = ListCommandsResponseBodyCommands()
            self.commands = temp_model.from_map(m['Commands'])
        return self


class ListCommandsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListCommandsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCommandsResponse, self).to_map()
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
            temp_model = ListCommandsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGWSImageRequest(TeaModel):
    def __init__(self, instance_id=None, name=None):
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGWSImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateGWSImageResponseBody(TeaModel):
    def __init__(self, image_id=None, request_id=None):
        self.image_id = image_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGWSImageResponseBody, self).to_map()
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


class CreateGWSImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateGWSImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGWSImageResponse, self).to_map()
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
            temp_model = CreateGWSImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeShellCommandRequestInstance(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InvokeShellCommandRequestInstance, self).to_map()
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


class InvokeShellCommandRequest(TeaModel):
    def __init__(self, cluster_id=None, command=None, working_dir=None, timeout=None, instance=None):
        self.cluster_id = cluster_id  # type: str
        self.command = command  # type: str
        self.working_dir = working_dir  # type: str
        self.timeout = timeout  # type: int
        self.instance = instance  # type: list[InvokeShellCommandRequestInstance]

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(InvokeShellCommandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.command is not None:
            result['Command'] = self.command
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = InvokeShellCommandRequestInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class InvokeShellCommandResponseBodyInstanceIds(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(InvokeShellCommandResponseBodyInstanceIds, self).to_map()
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


class InvokeShellCommandResponseBody(TeaModel):
    def __init__(self, command_id=None, request_id=None, instance_ids=None):
        self.command_id = command_id  # type: str
        self.request_id = request_id  # type: str
        self.instance_ids = instance_ids  # type: InvokeShellCommandResponseBodyInstanceIds

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super(InvokeShellCommandResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceIds') is not None:
            temp_model = InvokeShellCommandResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        return self


class InvokeShellCommandResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InvokeShellCommandResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InvokeShellCommandResponse, self).to_map()
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
            temp_model = InvokeShellCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFileSystemWithMountTargetsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFileSystemWithMountTargetsRequest, self).to_map()
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


class ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsPackageListPackages(TeaModel):
    def __init__(self, package_id=None):
        self.package_id = package_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsPackageListPackages, self).to_map()
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


class ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsPackageList(TeaModel):
    def __init__(self, packages=None):
        self.packages = packages  # type: list[ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsPackageListPackages]

    def validate(self):
        if self.packages:
            for k in self.packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsPackageList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Packages'] = []
        if self.packages is not None:
            for k in self.packages:
                result['Packages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.packages = []
        if m.get('Packages') is not None:
            for k in m.get('Packages'):
                temp_model = ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsPackageListPackages()
                self.packages.append(temp_model.from_map(k))
        return self


class ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsMountTargetListMountTargets(TeaModel):
    def __init__(self, status=None, vpc_id=None, mount_target_domain=None, access_group=None, vsw_id=None,
                 network_type=None):
        self.status = status  # type: str
        self.vpc_id = vpc_id  # type: str
        self.mount_target_domain = mount_target_domain  # type: str
        self.access_group = access_group  # type: str
        self.vsw_id = vsw_id  # type: str
        self.network_type = network_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsMountTargetListMountTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.access_group is not None:
            result['AccessGroup'] = self.access_group
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('AccessGroup') is not None:
            self.access_group = m.get('AccessGroup')
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        return self


class ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsMountTargetList(TeaModel):
    def __init__(self, mount_targets=None):
        self.mount_targets = mount_targets  # type: list[ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsMountTargetListMountTargets]

    def validate(self):
        if self.mount_targets:
            for k in self.mount_targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsMountTargetList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MountTargets'] = []
        if self.mount_targets is not None:
            for k in self.mount_targets:
                result['MountTargets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.mount_targets = []
        if m.get('MountTargets') is not None:
            for k in m.get('MountTargets'):
                temp_model = ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsMountTargetListMountTargets()
                self.mount_targets.append(temp_model.from_map(k))
        return self


class ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystems(TeaModel):
    def __init__(self, status=None, capacity=None, create_time=None, storage_type=None, band_width=None,
                 region_id=None, file_system_id=None, file_system_type=None, metered_size=None, encrypt_type=None,
                 protocol_type=None, destription=None, package_list=None, mount_target_list=None):
        self.status = status  # type: str
        self.capacity = capacity  # type: int
        self.create_time = create_time  # type: str
        self.storage_type = storage_type  # type: str
        self.band_width = band_width  # type: int
        self.region_id = region_id  # type: str
        self.file_system_id = file_system_id  # type: str
        self.file_system_type = file_system_type  # type: str
        self.metered_size = metered_size  # type: int
        self.encrypt_type = encrypt_type  # type: int
        self.protocol_type = protocol_type  # type: str
        self.destription = destription  # type: str
        self.package_list = package_list  # type: ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsPackageList
        self.mount_target_list = mount_target_list  # type: ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsMountTargetList

    def validate(self):
        if self.package_list:
            self.package_list.validate()
        if self.mount_target_list:
            self.mount_target_list.validate()

    def to_map(self):
        _map = super(ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.band_width is not None:
            result['BandWidth'] = self.band_width
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.destription is not None:
            result['Destription'] = self.destription
        if self.package_list is not None:
            result['PackageList'] = self.package_list.to_map()
        if self.mount_target_list is not None:
            result['MountTargetList'] = self.mount_target_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Destription') is not None:
            self.destription = m.get('Destription')
        if m.get('PackageList') is not None:
            temp_model = ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsPackageList()
            self.package_list = temp_model.from_map(m['PackageList'])
        if m.get('MountTargetList') is not None:
            temp_model = ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystemsMountTargetList()
            self.mount_target_list = temp_model.from_map(m['MountTargetList'])
        return self


class ListFileSystemWithMountTargetsResponseBodyFileSystemList(TeaModel):
    def __init__(self, file_systems=None):
        self.file_systems = file_systems  # type: list[ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystems]

    def validate(self):
        if self.file_systems:
            for k in self.file_systems:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFileSystemWithMountTargetsResponseBodyFileSystemList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileSystems'] = []
        if self.file_systems is not None:
            for k in self.file_systems:
                result['FileSystems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.file_systems = []
        if m.get('FileSystems') is not None:
            for k in m.get('FileSystems'):
                temp_model = ListFileSystemWithMountTargetsResponseBodyFileSystemListFileSystems()
                self.file_systems.append(temp_model.from_map(k))
        return self


class ListFileSystemWithMountTargetsResponseBody(TeaModel):
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, file_system_list=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.file_system_list = file_system_list  # type: ListFileSystemWithMountTargetsResponseBodyFileSystemList

    def validate(self):
        if self.file_system_list:
            self.file_system_list.validate()

    def to_map(self):
        _map = super(ListFileSystemWithMountTargetsResponseBody, self).to_map()
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
        if self.file_system_list is not None:
            result['FileSystemList'] = self.file_system_list.to_map()
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
        if m.get('FileSystemList') is not None:
            temp_model = ListFileSystemWithMountTargetsResponseBodyFileSystemList()
            self.file_system_list = temp_model.from_map(m['FileSystemList'])
        return self


class ListFileSystemWithMountTargetsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFileSystemWithMountTargetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFileSystemWithMountTargetsResponse, self).to_map()
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
            temp_model = ListFileSystemWithMountTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterAttributesRequest(TeaModel):
    def __init__(self, cluster_id=None, name=None, description=None, image_owner_alias=None, image_id=None):
        self.cluster_id = cluster_id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.image_owner_alias = image_owner_alias  # type: str
        self.image_id = image_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyClusterAttributesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyClusterAttributesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyClusterAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobTemplatesRequest(TeaModel):
    def __init__(self, templates=None):
        self.templates = templates  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteJobTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.templates is not None:
            result['Templates'] = self.templates
        return result

    def from_map(self, m=None):
        m = m or dict()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteJobTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteJobTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCloudMetricLogsRequest(TeaModel):
    def __init__(self, cluster_id=None, from_=None, to=None, reverse=None, aggregation_type=None,
                 aggregation_interval=None, metric_scope=None, filter=None, metric_categories=None):
        self.cluster_id = cluster_id  # type: str
        self.from_ = from_  # type: int
        self.to = to  # type: int
        self.reverse = reverse  # type: bool
        self.aggregation_type = aggregation_type  # type: str
        self.aggregation_interval = aggregation_interval  # type: int
        self.metric_scope = metric_scope  # type: str
        self.filter = filter  # type: str
        self.metric_categories = metric_categories  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCloudMetricLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.from_ is not None:
            result['From'] = self.from_
        if self.to is not None:
            result['To'] = self.to
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.aggregation_type is not None:
            result['AggregationType'] = self.aggregation_type
        if self.aggregation_interval is not None:
            result['AggregationInterval'] = self.aggregation_interval
        if self.metric_scope is not None:
            result['MetricScope'] = self.metric_scope
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.metric_categories is not None:
            result['MetricCategories'] = self.metric_categories
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('AggregationType') is not None:
            self.aggregation_type = m.get('AggregationType')
        if m.get('AggregationInterval') is not None:
            self.aggregation_interval = m.get('AggregationInterval')
        if m.get('MetricScope') is not None:
            self.metric_scope = m.get('MetricScope')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('MetricCategories') is not None:
            self.metric_categories = m.get('MetricCategories')
        return self


class GetCloudMetricLogsResponseBodyMetricLogsMetricLog(TeaModel):
    def __init__(self, time=None, disk_device=None, network_interface=None, metric_data=None, hostname=None,
                 instance_id=None):
        self.time = time  # type: int
        self.disk_device = disk_device  # type: str
        self.network_interface = network_interface  # type: str
        self.metric_data = metric_data  # type: str
        self.hostname = hostname  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCloudMetricLogsResponseBodyMetricLogsMetricLog, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.disk_device is not None:
            result['DiskDevice'] = self.disk_device
        if self.network_interface is not None:
            result['NetworkInterface'] = self.network_interface
        if self.metric_data is not None:
            result['MetricData'] = self.metric_data
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('DiskDevice') is not None:
            self.disk_device = m.get('DiskDevice')
        if m.get('NetworkInterface') is not None:
            self.network_interface = m.get('NetworkInterface')
        if m.get('MetricData') is not None:
            self.metric_data = m.get('MetricData')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetCloudMetricLogsResponseBodyMetricLogs(TeaModel):
    def __init__(self, metric_log=None):
        self.metric_log = metric_log  # type: list[GetCloudMetricLogsResponseBodyMetricLogsMetricLog]

    def validate(self):
        if self.metric_log:
            for k in self.metric_log:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCloudMetricLogsResponseBodyMetricLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MetricLog'] = []
        if self.metric_log is not None:
            for k in self.metric_log:
                result['MetricLog'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.metric_log = []
        if m.get('MetricLog') is not None:
            for k in m.get('MetricLog'):
                temp_model = GetCloudMetricLogsResponseBodyMetricLogsMetricLog()
                self.metric_log.append(temp_model.from_map(k))
        return self


class GetCloudMetricLogsResponseBody(TeaModel):
    def __init__(self, request_id=None, metric_logs=None):
        self.request_id = request_id  # type: str
        self.metric_logs = metric_logs  # type: GetCloudMetricLogsResponseBodyMetricLogs

    def validate(self):
        if self.metric_logs:
            self.metric_logs.validate()

    def to_map(self):
        _map = super(GetCloudMetricLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.metric_logs is not None:
            result['MetricLogs'] = self.metric_logs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MetricLogs') is not None:
            temp_model = GetCloudMetricLogsResponseBodyMetricLogs()
            self.metric_logs = temp_model.from_map(m['MetricLogs'])
        return self


class GetCloudMetricLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetCloudMetricLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCloudMetricLogsResponse, self).to_map()
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
            temp_model = GetCloudMetricLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobTemplateRequest(TeaModel):
    def __init__(self, command_line=None, name=None, runas_user=None, priority=None, package_path=None,
                 stdout_redirect_path=None, stderr_redirect_path=None, re_runable=None, array_request=None, variables=None, queue=None,
                 clock_time=None, node=None, task=None, thread=None, mem=None, gpu=None):
        self.command_line = command_line  # type: str
        self.name = name  # type: str
        self.runas_user = runas_user  # type: str
        self.priority = priority  # type: int
        self.package_path = package_path  # type: str
        self.stdout_redirect_path = stdout_redirect_path  # type: str
        self.stderr_redirect_path = stderr_redirect_path  # type: str
        self.re_runable = re_runable  # type: bool
        self.array_request = array_request  # type: str
        self.variables = variables  # type: str
        self.queue = queue  # type: str
        self.clock_time = clock_time  # type: str
        self.node = node  # type: int
        self.task = task  # type: int
        self.thread = thread  # type: int
        self.mem = mem  # type: str
        self.gpu = gpu  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_line is not None:
            result['CommandLine'] = self.command_line
        if self.name is not None:
            result['Name'] = self.name
        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.package_path is not None:
            result['PackagePath'] = self.package_path
        if self.stdout_redirect_path is not None:
            result['StdoutRedirectPath'] = self.stdout_redirect_path
        if self.stderr_redirect_path is not None:
            result['StderrRedirectPath'] = self.stderr_redirect_path
        if self.re_runable is not None:
            result['ReRunable'] = self.re_runable
        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request
        if self.variables is not None:
            result['Variables'] = self.variables
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.clock_time is not None:
            result['ClockTime'] = self.clock_time
        if self.node is not None:
            result['Node'] = self.node
        if self.task is not None:
            result['Task'] = self.task
        if self.thread is not None:
            result['Thread'] = self.thread
        if self.mem is not None:
            result['Mem'] = self.mem
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('PackagePath') is not None:
            self.package_path = m.get('PackagePath')
        if m.get('StdoutRedirectPath') is not None:
            self.stdout_redirect_path = m.get('StdoutRedirectPath')
        if m.get('StderrRedirectPath') is not None:
            self.stderr_redirect_path = m.get('StderrRedirectPath')
        if m.get('ReRunable') is not None:
            self.re_runable = m.get('ReRunable')
        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('ClockTime') is not None:
            self.clock_time = m.get('ClockTime')
        if m.get('Node') is not None:
            self.node = m.get('Node')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        if m.get('Thread') is not None:
            self.thread = m.get('Thread')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        return self


class CreateJobTemplateResponseBody(TeaModel):
    def __init__(self, template_id=None, request_id=None):
        self.template_id = template_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateJobTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateJobTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateJobTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHybridClusterConfigRequest(TeaModel):
    def __init__(self, cluster_id=None, node=None):
        self.cluster_id = cluster_id  # type: str
        self.node = node  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHybridClusterConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.node is not None:
            result['Node'] = self.node
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Node') is not None:
            self.node = m.get('Node')
        return self


class GetHybridClusterConfigResponseBody(TeaModel):
    def __init__(self, cluster_config=None, request_id=None):
        self.cluster_config = cluster_config  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHybridClusterConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_config is not None:
            result['ClusterConfig'] = self.cluster_config
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterConfig') is not None:
            self.cluster_config = m.get('ClusterConfig')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHybridClusterConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHybridClusterConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHybridClusterConfigResponse, self).to_map()
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
            temp_model = GetHybridClusterConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGWSInstancesRequest(TeaModel):
    def __init__(self, cluster_id=None, instance_id=None, page_number=None, page_size=None, user_uid=None,
                 user_name=None):
        self.cluster_id = cluster_id  # type: str
        self.instance_id = instance_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.user_uid = user_uid  # type: long
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGWSInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_uid is not None:
            result['UserUid'] = self.user_uid
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserUid') is not None:
            self.user_uid = m.get('UserUid')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeGWSInstancesResponseBodyInstancesInstanceInfoAppListAppInfo(TeaModel):
    def __init__(self, app_name=None, app_args=None, app_path=None):
        self.app_name = app_name  # type: str
        self.app_args = app_args  # type: str
        self.app_path = app_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGWSInstancesResponseBodyInstancesInstanceInfoAppListAppInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_args is not None:
            result['AppArgs'] = self.app_args
        if self.app_path is not None:
            result['AppPath'] = self.app_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppArgs') is not None:
            self.app_args = m.get('AppArgs')
        if m.get('AppPath') is not None:
            self.app_path = m.get('AppPath')
        return self


class DescribeGWSInstancesResponseBodyInstancesInstanceInfoAppList(TeaModel):
    def __init__(self, app_info=None):
        self.app_info = app_info  # type: list[DescribeGWSInstancesResponseBodyInstancesInstanceInfoAppListAppInfo]

    def validate(self):
        if self.app_info:
            for k in self.app_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGWSInstancesResponseBodyInstancesInstanceInfoAppList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInfo'] = []
        if self.app_info is not None:
            for k in self.app_info:
                result['AppInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_info = []
        if m.get('AppInfo') is not None:
            for k in m.get('AppInfo'):
                temp_model = DescribeGWSInstancesResponseBodyInstancesInstanceInfoAppListAppInfo()
                self.app_info.append(temp_model.from_map(k))
        return self


class DescribeGWSInstancesResponseBodyInstancesInstanceInfo(TeaModel):
    def __init__(self, status=None, work_mode=None, expire_time=None, create_time=None, instance_id=None, name=None,
                 instance_type=None, user_name=None, cluster_id=None, app_list=None):
        self.status = status  # type: str
        self.work_mode = work_mode  # type: str
        self.expire_time = expire_time  # type: str
        self.create_time = create_time  # type: str
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.instance_type = instance_type  # type: str
        self.user_name = user_name  # type: str
        self.cluster_id = cluster_id  # type: str
        self.app_list = app_list  # type: DescribeGWSInstancesResponseBodyInstancesInstanceInfoAppList

    def validate(self):
        if self.app_list:
            self.app_list.validate()

    def to_map(self):
        _map = super(DescribeGWSInstancesResponseBodyInstancesInstanceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.app_list is not None:
            result['AppList'] = self.app_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('AppList') is not None:
            temp_model = DescribeGWSInstancesResponseBodyInstancesInstanceInfoAppList()
            self.app_list = temp_model.from_map(m['AppList'])
        return self


class DescribeGWSInstancesResponseBodyInstances(TeaModel):
    def __init__(self, instance_info=None):
        self.instance_info = instance_info  # type: list[DescribeGWSInstancesResponseBodyInstancesInstanceInfo]

    def validate(self):
        if self.instance_info:
            for k in self.instance_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGWSInstancesResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceInfo'] = []
        if self.instance_info is not None:
            for k in self.instance_info:
                result['InstanceInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_info = []
        if m.get('InstanceInfo') is not None:
            for k in m.get('InstanceInfo'):
                temp_model = DescribeGWSInstancesResponseBodyInstancesInstanceInfo()
                self.instance_info.append(temp_model.from_map(k))
        return self


class DescribeGWSInstancesResponseBody(TeaModel):
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, instances=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.instances = instances  # type: DescribeGWSInstancesResponseBodyInstances

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        _map = super(DescribeGWSInstancesResponseBody, self).to_map()
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
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
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
        if m.get('Instances') is not None:
            temp_model = DescribeGWSInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        return self


class DescribeGWSInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeGWSInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGWSInstancesResponse, self).to_map()
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
            temp_model = DescribeGWSInstancesResponseBody()
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
    def __init__(self, task_id=None, request_id=None):
        self.task_id = task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetNodesResponseBody, self).to_map()
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


class ResetNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResetNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallSoftwareRequest(TeaModel):
    def __init__(self, cluster_id=None, application=None):
        self.cluster_id = cluster_id  # type: str
        self.application = application  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallSoftwareRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.application is not None:
            result['Application'] = self.application
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Application') is not None:
            self.application = m.get('Application')
        return self


class UninstallSoftwareResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UninstallSoftwareResponseBody, self).to_map()
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


class UninstallSoftwareResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UninstallSoftwareResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UninstallSoftwareResponse, self).to_map()
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
            temp_model = UninstallSoftwareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyNodesRequestZoneInfos(TeaModel):
    def __init__(self, v_switch_id=None, zone_id=None):
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyNodesRequestZoneInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ApplyNodesRequestInstanceTypeModel(TeaModel):
    def __init__(self, max_price=None, target_image_id=None, instance_type=None):
        self.max_price = max_price  # type: float
        self.target_image_id = target_image_id  # type: str
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyNodesRequestInstanceTypeModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_price is not None:
            result['MaxPrice'] = self.max_price
        if self.target_image_id is not None:
            result['TargetImageId'] = self.target_image_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxPrice') is not None:
            self.max_price = m.get('MaxPrice')
        if m.get('TargetImageId') is not None:
            self.target_image_id = m.get('TargetImageId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class ApplyNodesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyNodesRequestTag, self).to_map()
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


class ApplyNodesRequest(TeaModel):
    def __init__(self, cluster_id=None, image_id=None, compute_spot_strategy=None, compute_spot_price_limit=None,
                 system_disk_type=None, system_disk_size=None, host_name_prefix=None, host_name_suffix=None,
                 allocate_public_address=None, internet_charge_type=None, internet_max_band_width_in=None,
                 internet_max_band_width_out=None, cores=None, memory=None, instance_family_level=None, target_capacity=None,
                 resource_amount_type=None, priority_strategy=None, strict_satisfied_target_capacity=None, system_disk_level=None,
                 strict_resource_provision=None, round=None, interval=None, zone_infos=None, instance_type_model=None, tag=None):
        self.cluster_id = cluster_id  # type: str
        self.image_id = image_id  # type: str
        self.compute_spot_strategy = compute_spot_strategy  # type: str
        self.compute_spot_price_limit = compute_spot_price_limit  # type: float
        self.system_disk_type = system_disk_type  # type: str
        self.system_disk_size = system_disk_size  # type: int
        self.host_name_prefix = host_name_prefix  # type: str
        self.host_name_suffix = host_name_suffix  # type: str
        self.allocate_public_address = allocate_public_address  # type: bool
        self.internet_charge_type = internet_charge_type  # type: str
        self.internet_max_band_width_in = internet_max_band_width_in  # type: int
        self.internet_max_band_width_out = internet_max_band_width_out  # type: int
        self.cores = cores  # type: int
        self.memory = memory  # type: int
        self.instance_family_level = instance_family_level  # type: str
        self.target_capacity = target_capacity  # type: int
        self.resource_amount_type = resource_amount_type  # type: str
        self.priority_strategy = priority_strategy  # type: str
        self.strict_satisfied_target_capacity = strict_satisfied_target_capacity  # type: bool
        self.system_disk_level = system_disk_level  # type: str
        self.strict_resource_provision = strict_resource_provision  # type: bool
        self.round = round  # type: int
        self.interval = interval  # type: int
        self.zone_infos = zone_infos  # type: list[ApplyNodesRequestZoneInfos]
        self.instance_type_model = instance_type_model  # type: list[ApplyNodesRequestInstanceTypeModel]
        self.tag = tag  # type: list[ApplyNodesRequestTag]

    def validate(self):
        if self.zone_infos:
            for k in self.zone_infos:
                if k:
                    k.validate()
        if self.instance_type_model:
            for k in self.instance_type_model:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ApplyNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.compute_spot_strategy is not None:
            result['ComputeSpotStrategy'] = self.compute_spot_strategy
        if self.compute_spot_price_limit is not None:
            result['ComputeSpotPriceLimit'] = self.compute_spot_price_limit
        if self.system_disk_type is not None:
            result['SystemDiskType'] = self.system_disk_type
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.host_name_prefix is not None:
            result['HostNamePrefix'] = self.host_name_prefix
        if self.host_name_suffix is not None:
            result['HostNameSuffix'] = self.host_name_suffix
        if self.allocate_public_address is not None:
            result['AllocatePublicAddress'] = self.allocate_public_address
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_band_width_in is not None:
            result['InternetMaxBandWidthIn'] = self.internet_max_band_width_in
        if self.internet_max_band_width_out is not None:
            result['InternetMaxBandWidthOut'] = self.internet_max_band_width_out
        if self.cores is not None:
            result['Cores'] = self.cores
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level
        if self.target_capacity is not None:
            result['TargetCapacity'] = self.target_capacity
        if self.resource_amount_type is not None:
            result['ResourceAmountType'] = self.resource_amount_type
        if self.priority_strategy is not None:
            result['PriorityStrategy'] = self.priority_strategy
        if self.strict_satisfied_target_capacity is not None:
            result['StrictSatisfiedTargetCapacity'] = self.strict_satisfied_target_capacity
        if self.system_disk_level is not None:
            result['SystemDiskLevel'] = self.system_disk_level
        if self.strict_resource_provision is not None:
            result['StrictResourceProvision'] = self.strict_resource_provision
        if self.round is not None:
            result['Round'] = self.round
        if self.interval is not None:
            result['Interval'] = self.interval
        result['ZoneInfos'] = []
        if self.zone_infos is not None:
            for k in self.zone_infos:
                result['ZoneInfos'].append(k.to_map() if k else None)
        result['InstanceTypeModel'] = []
        if self.instance_type_model is not None:
            for k in self.instance_type_model:
                result['InstanceTypeModel'].append(k.to_map() if k else None)
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ComputeSpotStrategy') is not None:
            self.compute_spot_strategy = m.get('ComputeSpotStrategy')
        if m.get('ComputeSpotPriceLimit') is not None:
            self.compute_spot_price_limit = m.get('ComputeSpotPriceLimit')
        if m.get('SystemDiskType') is not None:
            self.system_disk_type = m.get('SystemDiskType')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('HostNamePrefix') is not None:
            self.host_name_prefix = m.get('HostNamePrefix')
        if m.get('HostNameSuffix') is not None:
            self.host_name_suffix = m.get('HostNameSuffix')
        if m.get('AllocatePublicAddress') is not None:
            self.allocate_public_address = m.get('AllocatePublicAddress')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandWidthIn') is not None:
            self.internet_max_band_width_in = m.get('InternetMaxBandWidthIn')
        if m.get('InternetMaxBandWidthOut') is not None:
            self.internet_max_band_width_out = m.get('InternetMaxBandWidthOut')
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')
        if m.get('TargetCapacity') is not None:
            self.target_capacity = m.get('TargetCapacity')
        if m.get('ResourceAmountType') is not None:
            self.resource_amount_type = m.get('ResourceAmountType')
        if m.get('PriorityStrategy') is not None:
            self.priority_strategy = m.get('PriorityStrategy')
        if m.get('StrictSatisfiedTargetCapacity') is not None:
            self.strict_satisfied_target_capacity = m.get('StrictSatisfiedTargetCapacity')
        if m.get('SystemDiskLevel') is not None:
            self.system_disk_level = m.get('SystemDiskLevel')
        if m.get('StrictResourceProvision') is not None:
            self.strict_resource_provision = m.get('StrictResourceProvision')
        if m.get('Round') is not None:
            self.round = m.get('Round')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        self.zone_infos = []
        if m.get('ZoneInfos') is not None:
            for k in m.get('ZoneInfos'):
                temp_model = ApplyNodesRequestZoneInfos()
                self.zone_infos.append(temp_model.from_map(k))
        self.instance_type_model = []
        if m.get('InstanceTypeModel') is not None:
            for k in m.get('InstanceTypeModel'):
                temp_model = ApplyNodesRequestInstanceTypeModel()
                self.instance_type_model.append(temp_model.from_map(k))
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ApplyNodesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ApplyNodesResponseBodyInstanceIds(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyNodesResponseBodyInstanceIds, self).to_map()
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


class ApplyNodesResponseBody(TeaModel):
    def __init__(self, request_id=None, satisfied_amount=None, task_id=None, detail=None, instance_ids=None):
        self.request_id = request_id  # type: str
        self.satisfied_amount = satisfied_amount  # type: int
        self.task_id = task_id  # type: str
        self.detail = detail  # type: str
        self.instance_ids = instance_ids  # type: ApplyNodesResponseBodyInstanceIds

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super(ApplyNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.satisfied_amount is not None:
            result['SatisfiedAmount'] = self.satisfied_amount
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SatisfiedAmount') is not None:
            self.satisfied_amount = m.get('SatisfiedAmount')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('InstanceIds') is not None:
            temp_model = ApplyNodesResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        return self


class ApplyNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ApplyNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyNodesResponse, self).to_map()
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
            temp_model = ApplyNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGWSClustersRequest(TeaModel):
    def __init__(self, cluster_id=None, page_number=None, page_size=None):
        self.cluster_id = cluster_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGWSClustersRequest, self).to_map()
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


class DescribeGWSClustersResponseBodyClustersClusterInfo(TeaModel):
    def __init__(self, vpc_id=None, status=None, instance_count=None, create_time=None, cluster_id=None):
        self.vpc_id = vpc_id  # type: str
        self.status = status  # type: str
        self.instance_count = instance_count  # type: int
        self.create_time = create_time  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGWSClustersResponseBodyClustersClusterInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.status is not None:
            result['Status'] = self.status
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeGWSClustersResponseBodyClusters(TeaModel):
    def __init__(self, cluster_info=None):
        self.cluster_info = cluster_info  # type: list[DescribeGWSClustersResponseBodyClustersClusterInfo]

    def validate(self):
        if self.cluster_info:
            for k in self.cluster_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGWSClustersResponseBodyClusters, self).to_map()
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
                temp_model = DescribeGWSClustersResponseBodyClustersClusterInfo()
                self.cluster_info.append(temp_model.from_map(k))
        return self


class DescribeGWSClustersResponseBody(TeaModel):
    def __init__(self, page_size=None, page_number=None, request_id=None, caller_type=None, total_count=None,
                 clusters=None):
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.request_id = request_id  # type: str
        self.caller_type = caller_type  # type: str
        self.total_count = total_count  # type: int
        self.clusters = clusters  # type: DescribeGWSClustersResponseBodyClusters

    def validate(self):
        if self.clusters:
            self.clusters.validate()

    def to_map(self):
        _map = super(DescribeGWSClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.caller_type is not None:
            result['CallerType'] = self.caller_type
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.clusters is not None:
            result['Clusters'] = self.clusters.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Clusters') is not None:
            temp_model = DescribeGWSClustersResponseBodyClusters()
            self.clusters = temp_model.from_map(m['Clusters'])
        return self


class DescribeGWSClustersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeGWSClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGWSClustersResponse, self).to_map()
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
            temp_model = DescribeGWSClustersResponseBody()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListContainerImagesRequest(TeaModel):
    def __init__(self, cluster_id=None, container_type=None, page_number=None, page_size=None):
        self.cluster_id = cluster_id  # type: str
        self.container_type = container_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListContainerImagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.container_type is not None:
            result['ContainerType'] = self.container_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContainerType') is not None:
            self.container_type = m.get('ContainerType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListContainerImagesResponseBodyImagesImages(TeaModel):
    def __init__(self, type=None, status=None, update_date_time=None, repository=None, tag=None, system=None,
                 image_id=None):
        self.type = type  # type: str
        self.status = status  # type: str
        self.update_date_time = update_date_time  # type: str
        self.repository = repository  # type: str
        self.tag = tag  # type: str
        self.system = system  # type: str
        self.image_id = image_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListContainerImagesResponseBodyImagesImages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.update_date_time is not None:
            result['UpdateDateTime'] = self.update_date_time
        if self.repository is not None:
            result['Repository'] = self.repository
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.system is not None:
            result['System'] = self.system
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateDateTime') is not None:
            self.update_date_time = m.get('UpdateDateTime')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('System') is not None:
            self.system = m.get('System')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class ListContainerImagesResponseBodyImages(TeaModel):
    def __init__(self, images=None):
        self.images = images  # type: list[ListContainerImagesResponseBodyImagesImages]

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListContainerImagesResponseBodyImages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListContainerImagesResponseBodyImagesImages()
                self.images.append(temp_model.from_map(k))
        return self


class ListContainerImagesResponseBody(TeaModel):
    def __init__(self, page_size=None, page_number=None, request_id=None, total_count=None, dbinfo=None, images=None):
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.dbinfo = dbinfo  # type: str
        self.images = images  # type: ListContainerImagesResponseBodyImages

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        _map = super(ListContainerImagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.dbinfo is not None:
            result['DBInfo'] = self.dbinfo
        if self.images is not None:
            result['Images'] = self.images.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('DBInfo') is not None:
            self.dbinfo = m.get('DBInfo')
        if m.get('Images') is not None:
            temp_model = ListContainerImagesResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        return self


class ListContainerImagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListContainerImagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListContainerImagesResponse, self).to_map()
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
            temp_model = ListContainerImagesResponseBody()
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
    def __init__(self, cluster_id=None, release_instance=None, sync=None, instance=None):
        self.cluster_id = cluster_id  # type: str
        self.release_instance = release_instance  # type: bool
        self.sync = sync  # type: bool
        self.instance = instance  # type: list[DeleteNodesRequestInstance]

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
        if self.release_instance is not None:
            result['ReleaseInstance'] = self.release_instance
        if self.sync is not None:
            result['Sync'] = self.sync
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ReleaseInstance') is not None:
            self.release_instance = m.get('ReleaseInstance')
        if m.get('Sync') is not None:
            self.sync = m.get('Sync')
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = DeleteNodesRequestInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class DeleteNodesResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None):
        self.task_id = task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNodesResponseBody, self).to_map()
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


class DeleteNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(self, cluster_id=None, owner=None, state=None, rerunable=None, page_number=None, page_size=None):
        self.cluster_id = cluster_id  # type: str
        self.owner = owner  # type: str
        self.state = state  # type: str
        self.rerunable = rerunable  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

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
        if self.state is not None:
            result['State'] = self.state
        if self.rerunable is not None:
            result['Rerunable'] = self.rerunable
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Rerunable') is not None:
            self.rerunable = m.get('Rerunable')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListJobsResponseBodyJobsJobInfoResources(TeaModel):
    def __init__(self, nodes=None, cores=None):
        self.nodes = nodes  # type: int
        self.cores = cores  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobsResponseBodyJobsJobInfoResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        if self.cores is not None:
            result['Cores'] = self.cores
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')
        return self


class ListJobsResponseBodyJobsJobInfo(TeaModel):
    def __init__(self, owner=None, comment=None, state=None, stderr=None, priority=None, shell_path=None, stdout=None,
                 array_request=None, start_time=None, last_modify_time=None, node_list=None, name=None, id=None, submit_time=None,
                 resources=None):
        self.owner = owner  # type: str
        self.comment = comment  # type: str
        self.state = state  # type: str
        self.stderr = stderr  # type: str
        self.priority = priority  # type: str
        self.shell_path = shell_path  # type: str
        self.stdout = stdout  # type: str
        self.array_request = array_request  # type: str
        self.start_time = start_time  # type: str
        self.last_modify_time = last_modify_time  # type: str
        self.node_list = node_list  # type: str
        self.name = name  # type: str
        self.id = id  # type: str
        self.submit_time = submit_time  # type: str
        self.resources = resources  # type: ListJobsResponseBodyJobsJobInfoResources

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super(ListJobsResponseBodyJobsJobInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.state is not None:
            result['State'] = self.state
        if self.stderr is not None:
            result['Stderr'] = self.stderr
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.shell_path is not None:
            result['ShellPath'] = self.shell_path
        if self.stdout is not None:
            result['Stdout'] = self.stdout
        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.node_list is not None:
            result['NodeList'] = self.node_list
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Stderr') is not None:
            self.stderr = m.get('Stderr')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ShellPath') is not None:
            self.shell_path = m.get('ShellPath')
        if m.get('Stdout') is not None:
            self.stdout = m.get('Stdout')
        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('NodeList') is not None:
            self.node_list = m.get('NodeList')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('Resources') is not None:
            temp_model = ListJobsResponseBodyJobsJobInfoResources()
            self.resources = temp_model.from_map(m['Resources'])
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
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, jobs=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.jobs = jobs  # type: ListJobsResponseBodyJobs

    def validate(self):
        if self.jobs:
            self.jobs.validate()

    def to_map(self):
        _map = super(ListJobsResponseBody, self).to_map()
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
        if self.jobs is not None:
            result['Jobs'] = self.jobs.to_map()
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
        if m.get('Jobs') is not None:
            temp_model = ListJobsResponseBodyJobs()
            self.jobs = temp_model.from_map(m['Jobs'])
        return self


class ListJobsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCpfsFileSystemsRequest(TeaModel):
    def __init__(self, file_system_id=None, page_number=None, page_size=None):
        self.file_system_id = file_system_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCpfsFileSystemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCpfsFileSystemsResponseBodyFileSystemListFileSystemsMountTargetListMountTargets(TeaModel):
    def __init__(self, vpc_id=None, status=None, vsw_id=None, network_type=None, mount_target_domain=None):
        self.vpc_id = vpc_id  # type: str
        self.status = status  # type: str
        self.vsw_id = vsw_id  # type: str
        self.network_type = network_type  # type: str
        self.mount_target_domain = mount_target_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCpfsFileSystemsResponseBodyFileSystemListFileSystemsMountTargetListMountTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.status is not None:
            result['Status'] = self.status
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        return self


class ListCpfsFileSystemsResponseBodyFileSystemListFileSystemsMountTargetList(TeaModel):
    def __init__(self, mount_targets=None):
        self.mount_targets = mount_targets  # type: list[ListCpfsFileSystemsResponseBodyFileSystemListFileSystemsMountTargetListMountTargets]

    def validate(self):
        if self.mount_targets:
            for k in self.mount_targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCpfsFileSystemsResponseBodyFileSystemListFileSystemsMountTargetList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MountTargets'] = []
        if self.mount_targets is not None:
            for k in self.mount_targets:
                result['MountTargets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.mount_targets = []
        if m.get('MountTargets') is not None:
            for k in m.get('MountTargets'):
                temp_model = ListCpfsFileSystemsResponseBodyFileSystemListFileSystemsMountTargetListMountTargets()
                self.mount_targets.append(temp_model.from_map(k))
        return self


class ListCpfsFileSystemsResponseBodyFileSystemListFileSystems(TeaModel):
    def __init__(self, file_system_id=None, capacity=None, create_time=None, zone_id=None, protocol_type=None,
                 destription=None, region_id=None, mount_target_list=None):
        self.file_system_id = file_system_id  # type: str
        self.capacity = capacity  # type: str
        self.create_time = create_time  # type: str
        self.zone_id = zone_id  # type: str
        self.protocol_type = protocol_type  # type: str
        self.destription = destription  # type: str
        self.region_id = region_id  # type: str
        self.mount_target_list = mount_target_list  # type: ListCpfsFileSystemsResponseBodyFileSystemListFileSystemsMountTargetList

    def validate(self):
        if self.mount_target_list:
            self.mount_target_list.validate()

    def to_map(self):
        _map = super(ListCpfsFileSystemsResponseBodyFileSystemListFileSystems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.destription is not None:
            result['Destription'] = self.destription
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.mount_target_list is not None:
            result['MountTargetList'] = self.mount_target_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Destription') is not None:
            self.destription = m.get('Destription')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MountTargetList') is not None:
            temp_model = ListCpfsFileSystemsResponseBodyFileSystemListFileSystemsMountTargetList()
            self.mount_target_list = temp_model.from_map(m['MountTargetList'])
        return self


class ListCpfsFileSystemsResponseBodyFileSystemList(TeaModel):
    def __init__(self, file_systems=None):
        self.file_systems = file_systems  # type: list[ListCpfsFileSystemsResponseBodyFileSystemListFileSystems]

    def validate(self):
        if self.file_systems:
            for k in self.file_systems:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCpfsFileSystemsResponseBodyFileSystemList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileSystems'] = []
        if self.file_systems is not None:
            for k in self.file_systems:
                result['FileSystems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.file_systems = []
        if m.get('FileSystems') is not None:
            for k in m.get('FileSystems'):
                temp_model = ListCpfsFileSystemsResponseBodyFileSystemListFileSystems()
                self.file_systems.append(temp_model.from_map(k))
        return self


class ListCpfsFileSystemsResponseBody(TeaModel):
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, file_system_list=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.file_system_list = file_system_list  # type: ListCpfsFileSystemsResponseBodyFileSystemList

    def validate(self):
        if self.file_system_list:
            self.file_system_list.validate()

    def to_map(self):
        _map = super(ListCpfsFileSystemsResponseBody, self).to_map()
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
        if self.file_system_list is not None:
            result['FileSystemList'] = self.file_system_list.to_map()
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
        if m.get('FileSystemList') is not None:
            temp_model = ListCpfsFileSystemsResponseBodyFileSystemList()
            self.file_system_list = temp_model.from_map(m['FileSystemList'])
        return self


class ListCpfsFileSystemsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListCpfsFileSystemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCpfsFileSystemsResponse, self).to_map()
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
            temp_model = ListCpfsFileSystemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersMetaRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersMetaRequest, self).to_map()
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


class ListClustersMetaResponseBodyClustersClusterInfoSimple(TeaModel):
    def __init__(self, status=None, vpc_id=None, scheduler_type=None, deploy_mode=None, is_compute_ess=None,
                 os_tag=None, account_type=None, description=None, name=None, id=None, location=None, client_version=None):
        self.status = status  # type: str
        self.vpc_id = vpc_id  # type: str
        self.scheduler_type = scheduler_type  # type: str
        self.deploy_mode = deploy_mode  # type: str
        self.is_compute_ess = is_compute_ess  # type: bool
        self.os_tag = os_tag  # type: str
        self.account_type = account_type  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.id = id  # type: str
        self.location = location  # type: str
        self.client_version = client_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersMetaResponseBodyClustersClusterInfoSimple, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.is_compute_ess is not None:
            result['IsComputeEss'] = self.is_compute_ess
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.location is not None:
            result['Location'] = self.location
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('IsComputeEss') is not None:
            self.is_compute_ess = m.get('IsComputeEss')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        return self


class ListClustersMetaResponseBodyClusters(TeaModel):
    def __init__(self, cluster_info_simple=None):
        self.cluster_info_simple = cluster_info_simple  # type: list[ListClustersMetaResponseBodyClustersClusterInfoSimple]

    def validate(self):
        if self.cluster_info_simple:
            for k in self.cluster_info_simple:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClustersMetaResponseBodyClusters, self).to_map()
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
                temp_model = ListClustersMetaResponseBodyClustersClusterInfoSimple()
                self.cluster_info_simple.append(temp_model.from_map(k))
        return self


class ListClustersMetaResponseBody(TeaModel):
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, clusters=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.clusters = clusters  # type: ListClustersMetaResponseBodyClusters

    def validate(self):
        if self.clusters:
            self.clusters.validate()

    def to_map(self):
        _map = super(ListClustersMetaResponseBody, self).to_map()
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
        if self.clusters is not None:
            result['Clusters'] = self.clusters.to_map()
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
        if m.get('Clusters') is not None:
            temp_model = ListClustersMetaResponseBodyClusters()
            self.clusters = temp_model.from_map(m['Clusters'])
        return self


class ListClustersMetaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListClustersMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClustersMetaResponse, self).to_map()
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
            temp_model = ListClustersMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryServicePackAndPriceResponseBodyServicePackServicePackInfo(TeaModel):
    def __init__(self, end_time=None, capacity=None, start_time=None, instance_name=None):
        self.end_time = end_time  # type: int
        self.capacity = capacity  # type: int
        self.start_time = start_time  # type: int
        self.instance_name = instance_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryServicePackAndPriceResponseBodyServicePackServicePackInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class QueryServicePackAndPriceResponseBodyServicePack(TeaModel):
    def __init__(self, service_pack_info=None):
        self.service_pack_info = service_pack_info  # type: list[QueryServicePackAndPriceResponseBodyServicePackServicePackInfo]

    def validate(self):
        if self.service_pack_info:
            for k in self.service_pack_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryServicePackAndPriceResponseBodyServicePack, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServicePackInfo'] = []
        if self.service_pack_info is not None:
            for k in self.service_pack_info:
                result['ServicePackInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.service_pack_info = []
        if m.get('ServicePackInfo') is not None:
            for k in m.get('ServicePackInfo'):
                temp_model = QueryServicePackAndPriceResponseBodyServicePackServicePackInfo()
                self.service_pack_info.append(temp_model.from_map(k))
        return self


class QueryServicePackAndPriceResponseBody(TeaModel):
    def __init__(self, original_amount=None, request_id=None, discount_price=None, trade_price=None,
                 original_price=None, charge_amount=None, currency=None, region_id=None, service_pack=None):
        self.original_amount = original_amount  # type: int
        self.request_id = request_id  # type: str
        self.discount_price = discount_price  # type: float
        self.trade_price = trade_price  # type: float
        self.original_price = original_price  # type: float
        self.charge_amount = charge_amount  # type: int
        self.currency = currency  # type: str
        self.region_id = region_id  # type: str
        self.service_pack = service_pack  # type: QueryServicePackAndPriceResponseBodyServicePack

    def validate(self):
        if self.service_pack:
            self.service_pack.validate()

    def to_map(self):
        _map = super(QueryServicePackAndPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.charge_amount is not None:
            result['ChargeAmount'] = self.charge_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_pack is not None:
            result['ServicePack'] = self.service_pack.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('ChargeAmount') is not None:
            self.charge_amount = m.get('ChargeAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServicePack') is not None:
            temp_model = QueryServicePackAndPriceResponseBodyServicePack()
            self.service_pack = temp_model.from_map(m['ServicePack'])
        return self


class QueryServicePackAndPriceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryServicePackAndPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryServicePackAndPriceResponse, self).to_map()
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
            temp_model = QueryServicePackAndPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteContainerAppsRequestContainerApp(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteContainerAppsRequestContainerApp, self).to_map()
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


class DeleteContainerAppsRequest(TeaModel):
    def __init__(self, container_app=None):
        self.container_app = container_app  # type: list[DeleteContainerAppsRequestContainerApp]

    def validate(self):
        if self.container_app:
            for k in self.container_app:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DeleteContainerAppsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContainerApp'] = []
        if self.container_app is not None:
            for k in self.container_app:
                result['ContainerApp'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.container_app = []
        if m.get('ContainerApp') is not None:
            for k in m.get('ContainerApp'):
                temp_model = DeleteContainerAppsRequestContainerApp()
                self.container_app.append(temp_model.from_map(k))
        return self


class DeleteContainerAppsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteContainerAppsResponseBody, self).to_map()
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


class DeleteContainerAppsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteContainerAppsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteContainerAppsResponse, self).to_map()
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
            temp_model = DeleteContainerAppsResponseBody()
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


class ListVolumesResponseBodyVolumesVolumeInfoAdditionalVolumesVolumeInfo(TeaModel):
    def __init__(self, job_queue=None, volume_id=None, remote_directory=None, volume_mountpoint=None, role=None,
                 local_directory=None, volume_type=None, location=None, volume_protocol=None):
        self.job_queue = job_queue  # type: str
        self.volume_id = volume_id  # type: str
        self.remote_directory = remote_directory  # type: str
        self.volume_mountpoint = volume_mountpoint  # type: str
        self.role = role  # type: str
        self.local_directory = local_directory  # type: str
        self.volume_type = volume_type  # type: str
        self.location = location  # type: str
        self.volume_protocol = volume_protocol  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVolumesResponseBodyVolumesVolumeInfoAdditionalVolumesVolumeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.role is not None:
            result['Role'] = self.role
        if self.local_directory is not None:
            result['LocalDirectory'] = self.local_directory
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        if self.location is not None:
            result['Location'] = self.location
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('LocalDirectory') is not None:
            self.local_directory = m.get('LocalDirectory')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        return self


class ListVolumesResponseBodyVolumesVolumeInfoAdditionalVolumes(TeaModel):
    def __init__(self, volume_info=None):
        self.volume_info = volume_info  # type: list[ListVolumesResponseBodyVolumesVolumeInfoAdditionalVolumesVolumeInfo]

    def validate(self):
        if self.volume_info:
            for k in self.volume_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVolumesResponseBodyVolumesVolumeInfoAdditionalVolumes, self).to_map()
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
                temp_model = ListVolumesResponseBodyVolumesVolumeInfoAdditionalVolumesVolumeInfo()
                self.volume_info.append(temp_model.from_map(k))
        return self


class ListVolumesResponseBodyVolumesVolumeInfo(TeaModel):
    def __init__(self, volume_id=None, cluster_name=None, remote_directory=None, volume_mountpoint=None,
                 volume_type=None, volume_protocol=None, region_id=None, cluster_id=None, additional_volumes=None):
        self.volume_id = volume_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.remote_directory = remote_directory  # type: str
        self.volume_mountpoint = volume_mountpoint  # type: str
        self.volume_type = volume_type  # type: str
        self.volume_protocol = volume_protocol  # type: str
        self.region_id = region_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.additional_volumes = additional_volumes  # type: ListVolumesResponseBodyVolumesVolumeInfoAdditionalVolumes

    def validate(self):
        if self.additional_volumes:
            self.additional_volumes.validate()

    def to_map(self):
        _map = super(ListVolumesResponseBodyVolumesVolumeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.additional_volumes is not None:
            result['AdditionalVolumes'] = self.additional_volumes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('AdditionalVolumes') is not None:
            temp_model = ListVolumesResponseBodyVolumesVolumeInfoAdditionalVolumes()
            self.additional_volumes = temp_model.from_map(m['AdditionalVolumes'])
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
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, volumes=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.volumes is not None:
            result['Volumes'] = self.volumes.to_map()
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
        if m.get('Volumes') is not None:
            temp_model = ListVolumesResponseBodyVolumes()
            self.volumes = temp_model.from_map(m['Volumes'])
        return self


class ListVolumesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListVolumesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListVolumesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInvocationStatusRequest(TeaModel):
    def __init__(self, cluster_id=None, command_id=None):
        self.cluster_id = cluster_id  # type: str
        self.command_id = command_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInvocationStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        return self


class ListInvocationStatusResponseBodyInvokeInstancesInvokeInstance(TeaModel):
    def __init__(self, instance_invoke_status=None, instance_id=None):
        self.instance_invoke_status = instance_invoke_status  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInvocationStatusResponseBodyInvokeInstancesInvokeInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_invoke_status is not None:
            result['InstanceInvokeStatus'] = self.instance_invoke_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceInvokeStatus') is not None:
            self.instance_invoke_status = m.get('InstanceInvokeStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListInvocationStatusResponseBodyInvokeInstances(TeaModel):
    def __init__(self, invoke_instance=None):
        self.invoke_instance = invoke_instance  # type: list[ListInvocationStatusResponseBodyInvokeInstancesInvokeInstance]

    def validate(self):
        if self.invoke_instance:
            for k in self.invoke_instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInvocationStatusResponseBodyInvokeInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InvokeInstance'] = []
        if self.invoke_instance is not None:
            for k in self.invoke_instance:
                result['InvokeInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.invoke_instance = []
        if m.get('InvokeInstance') is not None:
            for k in m.get('InvokeInstance'):
                temp_model = ListInvocationStatusResponseBodyInvokeInstancesInvokeInstance()
                self.invoke_instance.append(temp_model.from_map(k))
        return self


class ListInvocationStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, command_id=None, invoke_status=None, invoke_instances=None):
        self.request_id = request_id  # type: str
        self.command_id = command_id  # type: str
        self.invoke_status = invoke_status  # type: str
        self.invoke_instances = invoke_instances  # type: ListInvocationStatusResponseBodyInvokeInstances

    def validate(self):
        if self.invoke_instances:
            self.invoke_instances.validate()

    def to_map(self):
        _map = super(ListInvocationStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.invoke_status is not None:
            result['InvokeStatus'] = self.invoke_status
        if self.invoke_instances is not None:
            result['InvokeInstances'] = self.invoke_instances.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('InvokeStatus') is not None:
            self.invoke_status = m.get('InvokeStatus')
        if m.get('InvokeInstances') is not None:
            temp_model = ListInvocationStatusResponseBodyInvokeInstances()
            self.invoke_instances = temp_model.from_map(m['InvokeInstances'])
        return self


class ListInvocationStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListInvocationStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInvocationStatusResponse, self).to_map()
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
            temp_model = ListInvocationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyImageGatewayConfigRequestRepo(TeaModel):
    def __init__(self, auth=None, url=None, location=None):
        self.auth = auth  # type: str
        self.url = url  # type: str
        self.location = location  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyImageGatewayConfigRequestRepo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth is not None:
            result['Auth'] = self.auth
        if self.url is not None:
            result['URL'] = self.url
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class ModifyImageGatewayConfigRequest(TeaModel):
    def __init__(self, cluster_id=None, dbtype=None, dbusername=None, dbpassword=None, dbserver_info=None,
                 default_repo_location=None, pull_update_timeout=None, image_expiration_timeout=None, repo=None):
        self.cluster_id = cluster_id  # type: str
        self.dbtype = dbtype  # type: str
        self.dbusername = dbusername  # type: str
        self.dbpassword = dbpassword  # type: str
        self.dbserver_info = dbserver_info  # type: str
        self.default_repo_location = default_repo_location  # type: str
        self.pull_update_timeout = pull_update_timeout  # type: int
        self.image_expiration_timeout = image_expiration_timeout  # type: str
        self.repo = repo  # type: list[ModifyImageGatewayConfigRequestRepo]

    def validate(self):
        if self.repo:
            for k in self.repo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyImageGatewayConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbusername is not None:
            result['DBUsername'] = self.dbusername
        if self.dbpassword is not None:
            result['DBPassword'] = self.dbpassword
        if self.dbserver_info is not None:
            result['DBServerInfo'] = self.dbserver_info
        if self.default_repo_location is not None:
            result['DefaultRepoLocation'] = self.default_repo_location
        if self.pull_update_timeout is not None:
            result['PullUpdateTimeout'] = self.pull_update_timeout
        if self.image_expiration_timeout is not None:
            result['ImageExpirationTimeout'] = self.image_expiration_timeout
        result['Repo'] = []
        if self.repo is not None:
            for k in self.repo:
                result['Repo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBUsername') is not None:
            self.dbusername = m.get('DBUsername')
        if m.get('DBPassword') is not None:
            self.dbpassword = m.get('DBPassword')
        if m.get('DBServerInfo') is not None:
            self.dbserver_info = m.get('DBServerInfo')
        if m.get('DefaultRepoLocation') is not None:
            self.default_repo_location = m.get('DefaultRepoLocation')
        if m.get('PullUpdateTimeout') is not None:
            self.pull_update_timeout = m.get('PullUpdateTimeout')
        if m.get('ImageExpirationTimeout') is not None:
            self.image_expiration_timeout = m.get('ImageExpirationTimeout')
        self.repo = []
        if m.get('Repo') is not None:
            for k in m.get('Repo'):
                temp_model = ModifyImageGatewayConfigRequestRepo()
                self.repo.append(temp_model.from_map(k))
        return self


class ModifyImageGatewayConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyImageGatewayConfigResponseBody, self).to_map()
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


class ModifyImageGatewayConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyImageGatewayConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyImageGatewayConfigResponse, self).to_map()
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
            temp_model = ModifyImageGatewayConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListContainerAppsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListContainerAppsRequest, self).to_map()
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


class ListContainerAppsResponseBodyContainerAppsContainerApps(TeaModel):
    def __init__(self, type=None, description=None, create_time=None, repository=None, image_tag=None, name=None,
                 id=None):
        self.type = type  # type: str
        self.description = description  # type: str
        self.create_time = create_time  # type: str
        self.repository = repository  # type: str
        self.image_tag = image_tag  # type: str
        self.name = name  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListContainerAppsResponseBodyContainerAppsContainerApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.description is not None:
            result['Description'] = self.description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.repository is not None:
            result['Repository'] = self.repository
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListContainerAppsResponseBodyContainerApps(TeaModel):
    def __init__(self, container_apps=None):
        self.container_apps = container_apps  # type: list[ListContainerAppsResponseBodyContainerAppsContainerApps]

    def validate(self):
        if self.container_apps:
            for k in self.container_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListContainerAppsResponseBodyContainerApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContainerApps'] = []
        if self.container_apps is not None:
            for k in self.container_apps:
                result['ContainerApps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.container_apps = []
        if m.get('ContainerApps') is not None:
            for k in m.get('ContainerApps'):
                temp_model = ListContainerAppsResponseBodyContainerAppsContainerApps()
                self.container_apps.append(temp_model.from_map(k))
        return self


class ListContainerAppsResponseBody(TeaModel):
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, container_apps=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.container_apps = container_apps  # type: ListContainerAppsResponseBodyContainerApps

    def validate(self):
        if self.container_apps:
            self.container_apps.validate()

    def to_map(self):
        _map = super(ListContainerAppsResponseBody, self).to_map()
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
        if self.container_apps is not None:
            result['ContainerApps'] = self.container_apps.to_map()
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
        if m.get('ContainerApps') is not None:
            temp_model = ListContainerAppsResponseBodyContainerApps()
            self.container_apps = temp_model.from_map(m['ContainerApps'])
        return self


class ListContainerAppsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListContainerAppsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListContainerAppsResponse, self).to_map()
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
            temp_model = ListContainerAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecurityGroupRequest(TeaModel):
    def __init__(self, cluster_id=None, security_group_id=None):
        self.cluster_id = cluster_id  # type: str
        self.security_group_id = security_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSecurityGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class DeleteSecurityGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSecurityGroupResponseBody, self).to_map()
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


class DeleteSecurityGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSecurityGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSecurityGroupResponse, self).to_map()
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
            temp_model = DeleteSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNFSClientStatusRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNFSClientStatusRequest, self).to_map()
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


class DescribeNFSClientStatusResponseBodyResult(TeaModel):
    def __init__(self, output=None, invoke_record_status=None, exit_code=None):
        self.output = output  # type: str
        self.invoke_record_status = invoke_record_status  # type: str
        self.exit_code = exit_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNFSClientStatusResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output
        if self.invoke_record_status is not None:
            result['InvokeRecordStatus'] = self.invoke_record_status
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('InvokeRecordStatus') is not None:
            self.invoke_record_status = m.get('InvokeRecordStatus')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        return self


class DescribeNFSClientStatusResponseBody(TeaModel):
    def __init__(self, status=None, request_id=None, result=None):
        self.status = status  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: DescribeNFSClientStatusResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(DescribeNFSClientStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = DescribeNFSClientStatusResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DescribeNFSClientStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeNFSClientStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNFSClientStatusResponse, self).to_map()
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
            temp_model = DescribeNFSClientStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EcdDeleteDesktopsRequest(TeaModel):
    def __init__(self, desktop_id=None):
        self.desktop_id = desktop_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(EcdDeleteDesktopsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class EcdDeleteDesktopsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EcdDeleteDesktopsResponseBody, self).to_map()
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


class EcdDeleteDesktopsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EcdDeleteDesktopsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EcdDeleteDesktopsResponse, self).to_map()
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
            temp_model = EcdDeleteDesktopsResponseBody()
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


class ListClustersResponseBodyClustersClusterInfoSimpleManagers(TeaModel):
    def __init__(self, operating_count=None, exception_count=None, stopped_count=None, total=None,
                 normal_count=None):
        self.operating_count = operating_count  # type: int
        self.exception_count = exception_count  # type: int
        self.stopped_count = stopped_count  # type: int
        self.total = total  # type: int
        self.normal_count = normal_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersResponseBodyClustersClusterInfoSimpleManagers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operating_count is not None:
            result['OperatingCount'] = self.operating_count
        if self.exception_count is not None:
            result['ExceptionCount'] = self.exception_count
        if self.stopped_count is not None:
            result['StoppedCount'] = self.stopped_count
        if self.total is not None:
            result['Total'] = self.total
        if self.normal_count is not None:
            result['NormalCount'] = self.normal_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatingCount') is not None:
            self.operating_count = m.get('OperatingCount')
        if m.get('ExceptionCount') is not None:
            self.exception_count = m.get('ExceptionCount')
        if m.get('StoppedCount') is not None:
            self.stopped_count = m.get('StoppedCount')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('NormalCount') is not None:
            self.normal_count = m.get('NormalCount')
        return self


class ListClustersResponseBodyClustersClusterInfoSimpleComputes(TeaModel):
    def __init__(self, operating_count=None, exception_count=None, stopped_count=None, total=None,
                 normal_count=None):
        self.operating_count = operating_count  # type: int
        self.exception_count = exception_count  # type: int
        self.stopped_count = stopped_count  # type: int
        self.total = total  # type: int
        self.normal_count = normal_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersResponseBodyClustersClusterInfoSimpleComputes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operating_count is not None:
            result['OperatingCount'] = self.operating_count
        if self.exception_count is not None:
            result['ExceptionCount'] = self.exception_count
        if self.stopped_count is not None:
            result['StoppedCount'] = self.stopped_count
        if self.total is not None:
            result['Total'] = self.total
        if self.normal_count is not None:
            result['NormalCount'] = self.normal_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatingCount') is not None:
            self.operating_count = m.get('OperatingCount')
        if m.get('ExceptionCount') is not None:
            self.exception_count = m.get('ExceptionCount')
        if m.get('StoppedCount') is not None:
            self.stopped_count = m.get('StoppedCount')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('NormalCount') is not None:
            self.normal_count = m.get('NormalCount')
        return self


class ListClustersResponseBodyClustersClusterInfoSimpleTotalResources(TeaModel):
    def __init__(self, gpu=None, cpu=None, memory=None):
        self.gpu = gpu  # type: int
        self.cpu = cpu  # type: int
        self.memory = memory  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersResponseBodyClustersClusterInfoSimpleTotalResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ListClustersResponseBodyClustersClusterInfoSimpleUsedResources(TeaModel):
    def __init__(self, gpu=None, cpu=None, memory=None):
        self.gpu = gpu  # type: int
        self.cpu = cpu  # type: int
        self.memory = memory  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersResponseBodyClustersClusterInfoSimpleUsedResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ListClustersResponseBodyClustersClusterInfoSimple(TeaModel):
    def __init__(self, vpc_id=None, status=None, create_time=None, is_compute_ess=None, compute_spot_strategy=None,
                 account_type=None, count=None, ehpc_version=None, description=None, base_os_tag=None, name=None, image_id=None,
                 compute_spot_price_limit=None, scheduler_type=None, deploy_mode=None, node_suffix=None, image_owner_alias=None, os_tag=None,
                 node_prefix=None, instance_type=None, region_id=None, instance_charge_type=None, v_switch_id=None,
                 zone_id=None, login_nodes=None, id=None, location=None, client_version=None, managers=None, computes=None,
                 total_resources=None, used_resources=None):
        self.vpc_id = vpc_id  # type: str
        self.status = status  # type: str
        self.create_time = create_time  # type: str
        self.is_compute_ess = is_compute_ess  # type: bool
        self.compute_spot_strategy = compute_spot_strategy  # type: str
        self.account_type = account_type  # type: str
        self.count = count  # type: int
        self.ehpc_version = ehpc_version  # type: str
        self.description = description  # type: str
        self.base_os_tag = base_os_tag  # type: str
        self.name = name  # type: str
        self.image_id = image_id  # type: str
        self.compute_spot_price_limit = compute_spot_price_limit  # type: float
        self.scheduler_type = scheduler_type  # type: str
        self.deploy_mode = deploy_mode  # type: str
        self.node_suffix = node_suffix  # type: str
        self.image_owner_alias = image_owner_alias  # type: str
        self.os_tag = os_tag  # type: str
        self.node_prefix = node_prefix  # type: str
        self.instance_type = instance_type  # type: str
        self.region_id = region_id  # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str
        self.login_nodes = login_nodes  # type: str
        self.id = id  # type: str
        self.location = location  # type: str
        self.client_version = client_version  # type: str
        self.managers = managers  # type: ListClustersResponseBodyClustersClusterInfoSimpleManagers
        self.computes = computes  # type: ListClustersResponseBodyClustersClusterInfoSimpleComputes
        self.total_resources = total_resources  # type: ListClustersResponseBodyClustersClusterInfoSimpleTotalResources
        self.used_resources = used_resources  # type: ListClustersResponseBodyClustersClusterInfoSimpleUsedResources

    def validate(self):
        if self.managers:
            self.managers.validate()
        if self.computes:
            self.computes.validate()
        if self.total_resources:
            self.total_resources.validate()
        if self.used_resources:
            self.used_resources.validate()

    def to_map(self):
        _map = super(ListClustersResponseBodyClustersClusterInfoSimple, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.is_compute_ess is not None:
            result['IsComputeEss'] = self.is_compute_ess
        if self.compute_spot_strategy is not None:
            result['ComputeSpotStrategy'] = self.compute_spot_strategy
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.count is not None:
            result['Count'] = self.count
        if self.ehpc_version is not None:
            result['EhpcVersion'] = self.ehpc_version
        if self.description is not None:
            result['Description'] = self.description
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag
        if self.name is not None:
            result['Name'] = self.name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.compute_spot_price_limit is not None:
            result['ComputeSpotPriceLimit'] = self.compute_spot_price_limit
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.node_suffix is not None:
            result['NodeSuffix'] = self.node_suffix
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.node_prefix is not None:
            result['NodePrefix'] = self.node_prefix
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.login_nodes is not None:
            result['LoginNodes'] = self.login_nodes
        if self.id is not None:
            result['Id'] = self.id
        if self.location is not None:
            result['Location'] = self.location
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.managers is not None:
            result['Managers'] = self.managers.to_map()
        if self.computes is not None:
            result['Computes'] = self.computes.to_map()
        if self.total_resources is not None:
            result['TotalResources'] = self.total_resources.to_map()
        if self.used_resources is not None:
            result['UsedResources'] = self.used_resources.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IsComputeEss') is not None:
            self.is_compute_ess = m.get('IsComputeEss')
        if m.get('ComputeSpotStrategy') is not None:
            self.compute_spot_strategy = m.get('ComputeSpotStrategy')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('EhpcVersion') is not None:
            self.ehpc_version = m.get('EhpcVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('BaseOsTag') is not None:
            self.base_os_tag = m.get('BaseOsTag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ComputeSpotPriceLimit') is not None:
            self.compute_spot_price_limit = m.get('ComputeSpotPriceLimit')
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('NodeSuffix') is not None:
            self.node_suffix = m.get('NodeSuffix')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('NodePrefix') is not None:
            self.node_prefix = m.get('NodePrefix')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('LoginNodes') is not None:
            self.login_nodes = m.get('LoginNodes')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('Managers') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoSimpleManagers()
            self.managers = temp_model.from_map(m['Managers'])
        if m.get('Computes') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoSimpleComputes()
            self.computes = temp_model.from_map(m['Computes'])
        if m.get('TotalResources') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoSimpleTotalResources()
            self.total_resources = temp_model.from_map(m['TotalResources'])
        if m.get('UsedResources') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoSimpleUsedResources()
            self.used_resources = temp_model.from_map(m['UsedResources'])
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
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, clusters=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.clusters = clusters  # type: ListClustersResponseBodyClusters

    def validate(self):
        if self.clusters:
            self.clusters.validate()

    def to_map(self):
        _map = super(ListClustersResponseBody, self).to_map()
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
        if self.clusters is not None:
            result['Clusters'] = self.clusters.to_map()
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
        if m.get('Clusters') is not None:
            temp_model = ListClustersResponseBodyClusters()
            self.clusters = temp_model.from_map(m['Clusters'])
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


class SubmitJobRequest(TeaModel):
    def __init__(self, cluster_id=None, command_line=None, runas_user=None, runas_user_password=None, name=None,
                 priority=None, package_path=None, stdout_redirect_path=None, stderr_redirect_path=None, re_runable=None,
                 array_request=None, variables=None, input_file_url=None, unzip_cmd=None, post_cmd_line=None, container_id=None,
                 job_queue=None, node=None, task=None, thread=None, mem=None, gpu=None, clock_time=None):
        self.cluster_id = cluster_id  # type: str
        self.command_line = command_line  # type: str
        self.runas_user = runas_user  # type: str
        self.runas_user_password = runas_user_password  # type: str
        self.name = name  # type: str
        self.priority = priority  # type: int
        self.package_path = package_path  # type: str
        self.stdout_redirect_path = stdout_redirect_path  # type: str
        self.stderr_redirect_path = stderr_redirect_path  # type: str
        self.re_runable = re_runable  # type: bool
        self.array_request = array_request  # type: str
        self.variables = variables  # type: str
        self.input_file_url = input_file_url  # type: str
        self.unzip_cmd = unzip_cmd  # type: str
        self.post_cmd_line = post_cmd_line  # type: str
        self.container_id = container_id  # type: str
        self.job_queue = job_queue  # type: str
        self.node = node  # type: int
        self.task = task  # type: int
        self.thread = thread  # type: int
        self.mem = mem  # type: str
        self.gpu = gpu  # type: int
        self.clock_time = clock_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.command_line is not None:
            result['CommandLine'] = self.command_line
        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user
        if self.runas_user_password is not None:
            result['RunasUserPassword'] = self.runas_user_password
        if self.name is not None:
            result['Name'] = self.name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.package_path is not None:
            result['PackagePath'] = self.package_path
        if self.stdout_redirect_path is not None:
            result['StdoutRedirectPath'] = self.stdout_redirect_path
        if self.stderr_redirect_path is not None:
            result['StderrRedirectPath'] = self.stderr_redirect_path
        if self.re_runable is not None:
            result['ReRunable'] = self.re_runable
        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request
        if self.variables is not None:
            result['Variables'] = self.variables
        if self.input_file_url is not None:
            result['InputFileUrl'] = self.input_file_url
        if self.unzip_cmd is not None:
            result['UnzipCmd'] = self.unzip_cmd
        if self.post_cmd_line is not None:
            result['PostCmdLine'] = self.post_cmd_line
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.node is not None:
            result['Node'] = self.node
        if self.task is not None:
            result['Task'] = self.task
        if self.thread is not None:
            result['Thread'] = self.thread
        if self.mem is not None:
            result['Mem'] = self.mem
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.clock_time is not None:
            result['ClockTime'] = self.clock_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')
        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')
        if m.get('RunasUserPassword') is not None:
            self.runas_user_password = m.get('RunasUserPassword')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('PackagePath') is not None:
            self.package_path = m.get('PackagePath')
        if m.get('StdoutRedirectPath') is not None:
            self.stdout_redirect_path = m.get('StdoutRedirectPath')
        if m.get('StderrRedirectPath') is not None:
            self.stderr_redirect_path = m.get('StderrRedirectPath')
        if m.get('ReRunable') is not None:
            self.re_runable = m.get('ReRunable')
        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        if m.get('InputFileUrl') is not None:
            self.input_file_url = m.get('InputFileUrl')
        if m.get('UnzipCmd') is not None:
            self.unzip_cmd = m.get('UnzipCmd')
        if m.get('PostCmdLine') is not None:
            self.post_cmd_line = m.get('PostCmdLine')
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('Node') is not None:
            self.node = m.get('Node')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        if m.get('Thread') is not None:
            self.thread = m.get('Thread')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('ClockTime') is not None:
            self.clock_time = m.get('ClockTime')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountingReportRequest(TeaModel):
    def __init__(self, cluster_id=None, start_time=None, end_time=None, report_type=None, filter_value=None,
                 dim=None, job_id=None, page_size=None, page_number=None):
        self.cluster_id = cluster_id  # type: str
        self.start_time = start_time  # type: int
        self.end_time = end_time  # type: int
        self.report_type = report_type  # type: str
        self.filter_value = filter_value  # type: str
        self.dim = dim  # type: str
        self.job_id = job_id  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountingReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.dim is not None:
            result['Dim'] = self.dim
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('Dim') is not None:
            self.dim = m.get('Dim')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class GetAccountingReportResponseBodyData(TeaModel):
    def __init__(self, data=None):
        self.data = data  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountingReportResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetAccountingReportResponseBody(TeaModel):
    def __init__(self, total_core_time=None, metrics=None, request_id=None, page_size=None, page_number=None,
                 total_count=None, data=None):
        self.total_core_time = total_core_time  # type: int
        self.metrics = metrics  # type: str
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.data = data  # type: GetAccountingReportResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAccountingReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_core_time is not None:
            result['TotalCoreTime'] = self.total_core_time
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCoreTime') is not None:
            self.total_core_time = m.get('TotalCoreTime')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Data') is not None:
            temp_model = GetAccountingReportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAccountingReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAccountingReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAccountingReportResponse, self).to_map()
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
            temp_model = GetAccountingReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoScaleConfigRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutoScaleConfigRequest, self).to_map()
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


class DescribeAutoScaleConfigResponseBody(TeaModel):
    def __init__(self, max_nodes_in_cluster=None, grow_timeout_in_minutes=None, spot_strategy=None,
                 request_id=None, enable_auto_shrink=None, cluster_type=None, enable_auto_grow=None, exclude_nodes=None,
                 grow_interval_in_minutes=None, shrink_interval_in_minutes=None, spot_price_limit=None, shrink_idle_times=None,
                 extra_nodes_grow_ratio=None, grow_ratio=None, uid=None, cluster_id=None):
        self.max_nodes_in_cluster = max_nodes_in_cluster  # type: int
        self.grow_timeout_in_minutes = grow_timeout_in_minutes  # type: int
        self.spot_strategy = spot_strategy  # type: str
        self.request_id = request_id  # type: str
        self.enable_auto_shrink = enable_auto_shrink  # type: bool
        self.cluster_type = cluster_type  # type: str
        self.enable_auto_grow = enable_auto_grow  # type: bool
        self.exclude_nodes = exclude_nodes  # type: str
        self.grow_interval_in_minutes = grow_interval_in_minutes  # type: int
        self.shrink_interval_in_minutes = shrink_interval_in_minutes  # type: int
        self.spot_price_limit = spot_price_limit  # type: str
        self.shrink_idle_times = shrink_idle_times  # type: int
        self.extra_nodes_grow_ratio = extra_nodes_grow_ratio  # type: int
        self.grow_ratio = grow_ratio  # type: int
        self.uid = uid  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAutoScaleConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_nodes_in_cluster is not None:
            result['MaxNodesInCluster'] = self.max_nodes_in_cluster
        if self.grow_timeout_in_minutes is not None:
            result['GrowTimeoutInMinutes'] = self.grow_timeout_in_minutes
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.enable_auto_shrink is not None:
            result['EnableAutoShrink'] = self.enable_auto_shrink
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.enable_auto_grow is not None:
            result['EnableAutoGrow'] = self.enable_auto_grow
        if self.exclude_nodes is not None:
            result['ExcludeNodes'] = self.exclude_nodes
        if self.grow_interval_in_minutes is not None:
            result['GrowIntervalInMinutes'] = self.grow_interval_in_minutes
        if self.shrink_interval_in_minutes is not None:
            result['ShrinkIntervalInMinutes'] = self.shrink_interval_in_minutes
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.shrink_idle_times is not None:
            result['ShrinkIdleTimes'] = self.shrink_idle_times
        if self.extra_nodes_grow_ratio is not None:
            result['ExtraNodesGrowRatio'] = self.extra_nodes_grow_ratio
        if self.grow_ratio is not None:
            result['GrowRatio'] = self.grow_ratio
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxNodesInCluster') is not None:
            self.max_nodes_in_cluster = m.get('MaxNodesInCluster')
        if m.get('GrowTimeoutInMinutes') is not None:
            self.grow_timeout_in_minutes = m.get('GrowTimeoutInMinutes')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EnableAutoShrink') is not None:
            self.enable_auto_shrink = m.get('EnableAutoShrink')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('EnableAutoGrow') is not None:
            self.enable_auto_grow = m.get('EnableAutoGrow')
        if m.get('ExcludeNodes') is not None:
            self.exclude_nodes = m.get('ExcludeNodes')
        if m.get('GrowIntervalInMinutes') is not None:
            self.grow_interval_in_minutes = m.get('GrowIntervalInMinutes')
        if m.get('ShrinkIntervalInMinutes') is not None:
            self.shrink_interval_in_minutes = m.get('ShrinkIntervalInMinutes')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('ShrinkIdleTimes') is not None:
            self.shrink_idle_times = m.get('ShrinkIdleTimes')
        if m.get('ExtraNodesGrowRatio') is not None:
            self.extra_nodes_grow_ratio = m.get('ExtraNodesGrowRatio')
        if m.get('GrowRatio') is not None:
            self.grow_ratio = m.get('GrowRatio')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeAutoScaleConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAutoScaleConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAutoScaleConfigResponse, self).to_map()
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
            temp_model = DescribeAutoScaleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVisualServiceStatusRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVisualServiceStatusRequest, self).to_map()
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


class GetVisualServiceStatusResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVisualServiceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetVisualServiceStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetVisualServiceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVisualServiceStatusResponse, self).to_map()
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
            temp_model = GetVisualServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartVisualServiceRequest(TeaModel):
    def __init__(self, cluster_id=None, cidr_ip=None, port=None):
        self.cluster_id = cluster_id  # type: str
        self.cidr_ip = cidr_ip  # type: str
        self.port = port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartVisualServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class StartVisualServiceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartVisualServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartVisualServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartVisualServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartVisualServiceResponse, self).to_map()
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
            temp_model = StartVisualServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIfEcsTypeSupportHtConfigRequest(TeaModel):
    def __init__(self, instance_type=None):
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIfEcsTypeSupportHtConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class GetIfEcsTypeSupportHtConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, default_ht_enabled=None, instance_type=None, support_ht_config=None):
        self.request_id = request_id  # type: str
        self.default_ht_enabled = default_ht_enabled  # type: bool
        self.instance_type = instance_type  # type: str
        self.support_ht_config = support_ht_config  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIfEcsTypeSupportHtConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.default_ht_enabled is not None:
            result['DefaultHtEnabled'] = self.default_ht_enabled
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.support_ht_config is not None:
            result['SupportHtConfig'] = self.support_ht_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DefaultHtEnabled') is not None:
            self.default_ht_enabled = m.get('DefaultHtEnabled')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('SupportHtConfig') is not None:
            self.support_ht_config = m.get('SupportHtConfig')
        return self


class GetIfEcsTypeSupportHtConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetIfEcsTypeSupportHtConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIfEcsTypeSupportHtConfigResponse, self).to_map()
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
            temp_model = GetIfEcsTypeSupportHtConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSchedulerInfoRequestScheduler(TeaModel):
    def __init__(self, sched_name=None):
        self.sched_name = sched_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSchedulerInfoRequestScheduler, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sched_name is not None:
            result['SchedName'] = self.sched_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SchedName') is not None:
            self.sched_name = m.get('SchedName')
        return self


class GetSchedulerInfoRequest(TeaModel):
    def __init__(self, region_id=None, cluster_id=None, scheduler=None):
        self.region_id = region_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.scheduler = scheduler  # type: list[GetSchedulerInfoRequestScheduler]

    def validate(self):
        if self.scheduler:
            for k in self.scheduler:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSchedulerInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['Scheduler'] = []
        if self.scheduler is not None:
            for k in self.scheduler:
                result['Scheduler'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.scheduler = []
        if m.get('Scheduler') is not None:
            for k in m.get('Scheduler'):
                temp_model = GetSchedulerInfoRequestScheduler()
                self.scheduler.append(temp_model.from_map(k))
        return self


class GetSchedulerInfoResponseBodySchedInfo(TeaModel):
    def __init__(self, configuration=None, sched_name=None):
        self.configuration = configuration  # type: str
        self.sched_name = sched_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSchedulerInfoResponseBodySchedInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        if self.sched_name is not None:
            result['SchedName'] = self.sched_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        if m.get('SchedName') is not None:
            self.sched_name = m.get('SchedName')
        return self


class GetSchedulerInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, sched_info=None):
        self.request_id = request_id  # type: str
        self.sched_info = sched_info  # type: list[GetSchedulerInfoResponseBodySchedInfo]

    def validate(self):
        if self.sched_info:
            for k in self.sched_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSchedulerInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SchedInfo'] = []
        if self.sched_info is not None:
            for k in self.sched_info:
                result['SchedInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sched_info = []
        if m.get('SchedInfo') is not None:
            for k in m.get('SchedInfo'):
                temp_model = GetSchedulerInfoResponseBodySchedInfo()
                self.sched_info.append(temp_model.from_map(k))
        return self


class GetSchedulerInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSchedulerInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSchedulerInfoResponse, self).to_map()
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
            temp_model = GetSchedulerInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGWSInstanceUserRequest(TeaModel):
    def __init__(self, instance_id=None, user_uid=None, user_name=None):
        self.instance_id = instance_id  # type: str
        self.user_uid = user_uid  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetGWSInstanceUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_uid is not None:
            result['UserUid'] = self.user_uid
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserUid') is not None:
            self.user_uid = m.get('UserUid')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class SetGWSInstanceUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetGWSInstanceUserResponseBody, self).to_map()
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


class SetGWSInstanceUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetGWSInstanceUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetGWSInstanceUserResponse, self).to_map()
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
            temp_model = SetGWSInstanceUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkbenchTokenRequest(TeaModel):
    def __init__(self, cluster_id=None, user_name=None, user_password=None, port=None, account_session_ticket=None,
                 account_uid=None, instance_id=None):
        self.cluster_id = cluster_id  # type: str
        self.user_name = user_name  # type: str
        self.user_password = user_password  # type: str
        self.port = port  # type: int
        self.account_session_ticket = account_session_ticket  # type: str
        self.account_uid = account_uid  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkbenchTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_password is not None:
            result['UserPassword'] = self.user_password
        if self.port is not None:
            result['Port'] = self.port
        if self.account_session_ticket is not None:
            result['AccountSessionTicket'] = self.account_session_ticket
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserPassword') is not None:
            self.user_password = m.get('UserPassword')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('AccountSessionTicket') is not None:
            self.account_session_ticket = m.get('AccountSessionTicket')
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetWorkbenchTokenResponseBodyRootInstanceLoginView(TeaModel):
    def __init__(self, default_view_url=None, rdp_view_url=None, base_view_url=None, file_tree_view_url=None,
                 terminal_view_url=None, view_name=None):
        self.default_view_url = default_view_url  # type: str
        self.rdp_view_url = rdp_view_url  # type: str
        self.base_view_url = base_view_url  # type: str
        self.file_tree_view_url = file_tree_view_url  # type: str
        self.terminal_view_url = terminal_view_url  # type: str
        self.view_name = view_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkbenchTokenResponseBodyRootInstanceLoginView, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_view_url is not None:
            result['defaultViewUrl'] = self.default_view_url
        if self.rdp_view_url is not None:
            result['rdpViewUrl'] = self.rdp_view_url
        if self.base_view_url is not None:
            result['baseViewUrl'] = self.base_view_url
        if self.file_tree_view_url is not None:
            result['fileTreeViewUrl'] = self.file_tree_view_url
        if self.terminal_view_url is not None:
            result['terminalViewUrl'] = self.terminal_view_url
        if self.view_name is not None:
            result['viewName'] = self.view_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('defaultViewUrl') is not None:
            self.default_view_url = m.get('defaultViewUrl')
        if m.get('rdpViewUrl') is not None:
            self.rdp_view_url = m.get('rdpViewUrl')
        if m.get('baseViewUrl') is not None:
            self.base_view_url = m.get('baseViewUrl')
        if m.get('fileTreeViewUrl') is not None:
            self.file_tree_view_url = m.get('fileTreeViewUrl')
        if m.get('terminalViewUrl') is not None:
            self.terminal_view_url = m.get('terminalViewUrl')
        if m.get('viewName') is not None:
            self.view_name = m.get('viewName')
        return self


class GetWorkbenchTokenResponseBodyRoot(TeaModel):
    def __init__(self, instance_login_view=None):
        self.instance_login_view = instance_login_view  # type: GetWorkbenchTokenResponseBodyRootInstanceLoginView

    def validate(self):
        if self.instance_login_view:
            self.instance_login_view.validate()

    def to_map(self):
        _map = super(GetWorkbenchTokenResponseBodyRoot, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_login_view is not None:
            result['instanceLoginView'] = self.instance_login_view.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceLoginView') is not None:
            temp_model = GetWorkbenchTokenResponseBodyRootInstanceLoginView()
            self.instance_login_view = temp_model.from_map(m['instanceLoginView'])
        return self


class GetWorkbenchTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, root=None):
        self.request_id = request_id  # type: str
        self.root = root  # type: GetWorkbenchTokenResponseBodyRoot

    def validate(self):
        if self.root:
            self.root.validate()

    def to_map(self):
        _map = super(GetWorkbenchTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root is not None:
            result['root'] = self.root.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('root') is not None:
            temp_model = GetWorkbenchTokenResponseBodyRoot()
            self.root = temp_model.from_map(m['root'])
        return self


class GetWorkbenchTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetWorkbenchTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWorkbenchTokenResponse, self).to_map()
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
            temp_model = GetWorkbenchTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallSoftwareRequest(TeaModel):
    def __init__(self, cluster_id=None, application=None):
        self.cluster_id = cluster_id  # type: str
        self.application = application  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallSoftwareRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.application is not None:
            result['Application'] = self.application
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Application') is not None:
            self.application = m.get('Application')
        return self


class InstallSoftwareResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstallSoftwareResponseBody, self).to_map()
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


class InstallSoftwareResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InstallSoftwareResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InstallSoftwareResponse, self).to_map()
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
            temp_model = InstallSoftwareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAvailableEcsTypesRequest(TeaModel):
    def __init__(self, zone_id=None, spot_strategy=None, instance_charge_type=None, show_sold_out=None):
        self.zone_id = zone_id  # type: str
        self.spot_strategy = spot_strategy  # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.show_sold_out = show_sold_out  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAvailableEcsTypesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.show_sold_out is not None:
            result['ShowSoldOut'] = self.show_sold_out
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('ShowSoldOut') is not None:
            self.show_sold_out = m.get('ShowSoldOut')
        return self


class ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypesTypesInfoZoneIds(TeaModel):
    def __init__(self, zone_id=None):
        self.zone_id = zone_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypesTypesInfoZoneIds, self).to_map()
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


class ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypesTypesInfo(TeaModel):
    def __init__(self, status=None, instance_type_id=None, instance_bandwidth_rx=None, gpuspec=None,
                 instance_bandwidth_tx=None, instance_pps_rx=None, instance_pps_tx=None, gpuamount=None, cpu_core_count=None,
                 memory_size=None, eni_quantity=None, zone_ids=None):
        self.status = status  # type: str
        self.instance_type_id = instance_type_id  # type: str
        self.instance_bandwidth_rx = instance_bandwidth_rx  # type: int
        self.gpuspec = gpuspec  # type: str
        self.instance_bandwidth_tx = instance_bandwidth_tx  # type: int
        self.instance_pps_rx = instance_pps_rx  # type: int
        self.instance_pps_tx = instance_pps_tx  # type: int
        self.gpuamount = gpuamount  # type: int
        self.cpu_core_count = cpu_core_count  # type: int
        self.memory_size = memory_size  # type: int
        self.eni_quantity = eni_quantity  # type: int
        self.zone_ids = zone_ids  # type: ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypesTypesInfoZoneIds

    def validate(self):
        if self.zone_ids:
            self.zone_ids.validate()

    def to_map(self):
        _map = super(ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypesTypesInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id
        if self.instance_bandwidth_rx is not None:
            result['InstanceBandwidthRx'] = self.instance_bandwidth_rx
        if self.gpuspec is not None:
            result['GPUSpec'] = self.gpuspec
        if self.instance_bandwidth_tx is not None:
            result['InstanceBandwidthTx'] = self.instance_bandwidth_tx
        if self.instance_pps_rx is not None:
            result['InstancePpsRx'] = self.instance_pps_rx
        if self.instance_pps_tx is not None:
            result['InstancePpsTx'] = self.instance_pps_tx
        if self.gpuamount is not None:
            result['GPUAmount'] = self.gpuamount
        if self.cpu_core_count is not None:
            result['CpuCoreCount'] = self.cpu_core_count
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.eni_quantity is not None:
            result['EniQuantity'] = self.eni_quantity
        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')
        if m.get('InstanceBandwidthRx') is not None:
            self.instance_bandwidth_rx = m.get('InstanceBandwidthRx')
        if m.get('GPUSpec') is not None:
            self.gpuspec = m.get('GPUSpec')
        if m.get('InstanceBandwidthTx') is not None:
            self.instance_bandwidth_tx = m.get('InstanceBandwidthTx')
        if m.get('InstancePpsRx') is not None:
            self.instance_pps_rx = m.get('InstancePpsRx')
        if m.get('InstancePpsTx') is not None:
            self.instance_pps_tx = m.get('InstancePpsTx')
        if m.get('GPUAmount') is not None:
            self.gpuamount = m.get('GPUAmount')
        if m.get('CpuCoreCount') is not None:
            self.cpu_core_count = m.get('CpuCoreCount')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('EniQuantity') is not None:
            self.eni_quantity = m.get('EniQuantity')
        if m.get('ZoneIds') is not None:
            temp_model = ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypesTypesInfoZoneIds()
            self.zone_ids = temp_model.from_map(m['ZoneIds'])
        return self


class ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypes(TeaModel):
    def __init__(self, types_info=None):
        self.types_info = types_info  # type: list[ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypesTypesInfo]

    def validate(self):
        if self.types_info:
            for k in self.types_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TypesInfo'] = []
        if self.types_info is not None:
            for k in self.types_info:
                result['TypesInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.types_info = []
        if m.get('TypesInfo') is not None:
            for k in m.get('TypesInfo'):
                temp_model = ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypesTypesInfo()
                self.types_info.append(temp_model.from_map(k))
        return self


class ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfo(TeaModel):
    def __init__(self, generation=None, instance_type_family_id=None, types=None):
        self.generation = generation  # type: str
        self.instance_type_family_id = instance_type_family_id  # type: str
        self.types = types  # type: ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypes

    def validate(self):
        if self.types:
            self.types.validate()

    def to_map(self):
        _map = super(ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generation is not None:
            result['Generation'] = self.generation
        if self.instance_type_family_id is not None:
            result['InstanceTypeFamilyId'] = self.instance_type_family_id
        if self.types is not None:
            result['Types'] = self.types.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Generation') is not None:
            self.generation = m.get('Generation')
        if m.get('InstanceTypeFamilyId') is not None:
            self.instance_type_family_id = m.get('InstanceTypeFamilyId')
        if m.get('Types') is not None:
            temp_model = ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfoTypes()
            self.types = temp_model.from_map(m['Types'])
        return self


class ListAvailableEcsTypesResponseBodyInstanceTypeFamilies(TeaModel):
    def __init__(self, instance_type_family_info=None):
        self.instance_type_family_info = instance_type_family_info  # type: list[ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfo]

    def validate(self):
        if self.instance_type_family_info:
            for k in self.instance_type_family_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAvailableEcsTypesResponseBodyInstanceTypeFamilies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceTypeFamilyInfo'] = []
        if self.instance_type_family_info is not None:
            for k in self.instance_type_family_info:
                result['InstanceTypeFamilyInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_type_family_info = []
        if m.get('InstanceTypeFamilyInfo') is not None:
            for k in m.get('InstanceTypeFamilyInfo'):
                temp_model = ListAvailableEcsTypesResponseBodyInstanceTypeFamiliesInstanceTypeFamilyInfo()
                self.instance_type_family_info.append(temp_model.from_map(k))
        return self


class ListAvailableEcsTypesResponseBody(TeaModel):
    def __init__(self, support_spot_instance=None, request_id=None, instance_type_families=None):
        self.support_spot_instance = support_spot_instance  # type: bool
        self.request_id = request_id  # type: str
        self.instance_type_families = instance_type_families  # type: ListAvailableEcsTypesResponseBodyInstanceTypeFamilies

    def validate(self):
        if self.instance_type_families:
            self.instance_type_families.validate()

    def to_map(self):
        _map = super(ListAvailableEcsTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.support_spot_instance is not None:
            result['SupportSpotInstance'] = self.support_spot_instance
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_type_families is not None:
            result['InstanceTypeFamilies'] = self.instance_type_families.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SupportSpotInstance') is not None:
            self.support_spot_instance = m.get('SupportSpotInstance')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceTypeFamilies') is not None:
            temp_model = ListAvailableEcsTypesResponseBodyInstanceTypeFamilies()
            self.instance_type_families = temp_model.from_map(m['InstanceTypeFamilies'])
        return self


class ListAvailableEcsTypesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAvailableEcsTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAvailableEcsTypesResponse, self).to_map()
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
            temp_model = ListAvailableEcsTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MountNFSRequest(TeaModel):
    def __init__(self, instance_id=None, nfs_dir=None, mount_dir=None, protocol_type=None, remote_dir=None):
        self.instance_id = instance_id  # type: str
        self.nfs_dir = nfs_dir  # type: str
        self.mount_dir = mount_dir  # type: str
        self.protocol_type = protocol_type  # type: str
        self.remote_dir = remote_dir  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MountNFSRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.nfs_dir is not None:
            result['NfsDir'] = self.nfs_dir
        if self.mount_dir is not None:
            result['MountDir'] = self.mount_dir
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.remote_dir is not None:
            result['RemoteDir'] = self.remote_dir
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NfsDir') is not None:
            self.nfs_dir = m.get('NfsDir')
        if m.get('MountDir') is not None:
            self.mount_dir = m.get('MountDir')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('RemoteDir') is not None:
            self.remote_dir = m.get('RemoteDir')
        return self


class MountNFSResponseBody(TeaModel):
    def __init__(self, invoke_id=None, request_id=None):
        self.invoke_id = invoke_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MountNFSResponseBody, self).to_map()
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


class MountNFSResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: MountNFSResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MountNFSResponse, self).to_map()
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
            temp_model = MountNFSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddQueueRequest(TeaModel):
    def __init__(self, cluster_id=None, queue_name=None):
        self.cluster_id = cluster_id  # type: str
        self.queue_name = queue_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddQueueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        return self


class AddQueueResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddQueueResponseBody, self).to_map()
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


class AddQueueResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddQueueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddQueueResponse, self).to_map()
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
            temp_model = AddQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGWSInstanceRequest(TeaModel):
    def __init__(self, cluster_id=None, image_id=None, system_disk_size=None, system_disk_category=None,
                 instance_type=None, instance_charge_type=None, work_mode=None, allocate_public_address=None,
                 internet_charge_type=None, internet_max_bandwidth_in=None, internet_max_bandwidth_out=None, name=None, period=None,
                 period_unit=None, auto_renew=None, app_list=None, v_switch_id=None):
        self.cluster_id = cluster_id  # type: str
        self.image_id = image_id  # type: str
        self.system_disk_size = system_disk_size  # type: int
        self.system_disk_category = system_disk_category  # type: str
        self.instance_type = instance_type  # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.work_mode = work_mode  # type: str
        self.allocate_public_address = allocate_public_address  # type: bool
        self.internet_charge_type = internet_charge_type  # type: str
        self.internet_max_bandwidth_in = internet_max_bandwidth_in  # type: int
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: int
        self.name = name  # type: str
        self.period = period  # type: str
        self.period_unit = period_unit  # type: str
        self.auto_renew = auto_renew  # type: bool
        self.app_list = app_list  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGWSInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode
        if self.allocate_public_address is not None:
            result['AllocatePublicAddress'] = self.allocate_public_address
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.name is not None:
            result['Name'] = self.name
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.app_list is not None:
            result['AppList'] = self.app_list
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')
        if m.get('AllocatePublicAddress') is not None:
            self.allocate_public_address = m.get('AllocatePublicAddress')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AppList') is not None:
            self.app_list = m.get('AppList')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateGWSInstanceResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        self.instance_id = instance_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGWSInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGWSInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateGWSInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGWSInstanceResponse, self).to_map()
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
            temp_model = CreateGWSInstanceResponseBody()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListCurrentClientVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListCurrentClientVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClusterVolumesRequestAdditionalVolumesRoles(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateClusterVolumesRequestAdditionalVolumesRoles, self).to_map()
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


class UpdateClusterVolumesRequestAdditionalVolumes(TeaModel):
    def __init__(self, job_queue=None, volume_id=None, roles=None, volume_mountpoint=None, remote_directory=None,
                 volume_type=None, local_directory=None, volume_protocol=None, location=None):
        self.job_queue = job_queue  # type: str
        self.volume_id = volume_id  # type: str
        self.roles = roles  # type: list[UpdateClusterVolumesRequestAdditionalVolumesRoles]
        self.volume_mountpoint = volume_mountpoint  # type: str
        self.remote_directory = remote_directory  # type: str
        self.volume_type = volume_type  # type: str
        self.local_directory = local_directory  # type: str
        self.volume_protocol = volume_protocol  # type: str
        self.location = location  # type: str

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateClusterVolumesRequestAdditionalVolumes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        result['Roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['Roles'].append(k.to_map() if k else None)
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        if self.local_directory is not None:
            result['LocalDirectory'] = self.local_directory
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        self.roles = []
        if m.get('Roles') is not None:
            for k in m.get('Roles'):
                temp_model = UpdateClusterVolumesRequestAdditionalVolumesRoles()
                self.roles.append(temp_model.from_map(k))
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        if m.get('LocalDirectory') is not None:
            self.local_directory = m.get('LocalDirectory')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class UpdateClusterVolumesRequest(TeaModel):
    def __init__(self, cluster_id=None, additional_volumes=None):
        self.cluster_id = cluster_id  # type: str
        self.additional_volumes = additional_volumes  # type: list[UpdateClusterVolumesRequestAdditionalVolumes]

    def validate(self):
        if self.additional_volumes:
            for k in self.additional_volumes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateClusterVolumesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        result['AdditionalVolumes'] = []
        if self.additional_volumes is not None:
            for k in self.additional_volumes:
                result['AdditionalVolumes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        self.additional_volumes = []
        if m.get('AdditionalVolumes') is not None:
            for k in m.get('AdditionalVolumes'):
                temp_model = UpdateClusterVolumesRequestAdditionalVolumes()
                self.additional_volumes.append(temp_model.from_map(k))
        return self


class UpdateClusterVolumesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateClusterVolumesResponseBody, self).to_map()
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


class UpdateClusterVolumesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateClusterVolumesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateClusterVolumesResponse, self).to_map()
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
            temp_model = UpdateClusterVolumesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartGWSInstanceRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartGWSInstanceRequest, self).to_map()
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


class StartGWSInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartGWSInstanceResponseBody, self).to_map()
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


class StartGWSInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartGWSInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartGWSInstanceResponse, self).to_map()
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
            temp_model = StartGWSInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInvocationResultsRequestInstance(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInvocationResultsRequestInstance, self).to_map()
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


class ListInvocationResultsRequest(TeaModel):
    def __init__(self, cluster_id=None, command_id=None, invoke_record_status=None, page_number=None,
                 page_size=None, instance=None):
        self.cluster_id = cluster_id  # type: str
        self.command_id = command_id  # type: str
        self.invoke_record_status = invoke_record_status  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.instance = instance  # type: list[ListInvocationResultsRequestInstance]

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInvocationResultsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.invoke_record_status is not None:
            result['InvokeRecordStatus'] = self.invoke_record_status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('InvokeRecordStatus') is not None:
            self.invoke_record_status = m.get('InvokeRecordStatus')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = ListInvocationResultsRequestInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class ListInvocationResultsResponseBodyInvocationResultsInvocationResult(TeaModel):
    def __init__(self, success=None, message=None, finished_time=None, command_id=None, instance_id=None,
                 invoke_record_status=None, exit_code=None):
        self.success = success  # type: bool
        self.message = message  # type: str
        self.finished_time = finished_time  # type: str
        self.command_id = command_id  # type: str
        self.instance_id = instance_id  # type: str
        self.invoke_record_status = invoke_record_status  # type: str
        self.exit_code = exit_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInvocationResultsResponseBodyInvocationResultsInvocationResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.message is not None:
            result['Message'] = self.message
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.invoke_record_status is not None:
            result['InvokeRecordStatus'] = self.invoke_record_status
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InvokeRecordStatus') is not None:
            self.invoke_record_status = m.get('InvokeRecordStatus')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        return self


class ListInvocationResultsResponseBodyInvocationResults(TeaModel):
    def __init__(self, invocation_result=None):
        self.invocation_result = invocation_result  # type: list[ListInvocationResultsResponseBodyInvocationResultsInvocationResult]

    def validate(self):
        if self.invocation_result:
            for k in self.invocation_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInvocationResultsResponseBodyInvocationResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InvocationResult'] = []
        if self.invocation_result is not None:
            for k in self.invocation_result:
                result['InvocationResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.invocation_result = []
        if m.get('InvocationResult') is not None:
            for k in m.get('InvocationResult'):
                temp_model = ListInvocationResultsResponseBodyInvocationResultsInvocationResult()
                self.invocation_result.append(temp_model.from_map(k))
        return self


class ListInvocationResultsResponseBody(TeaModel):
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, invocation_results=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.invocation_results = invocation_results  # type: ListInvocationResultsResponseBodyInvocationResults

    def validate(self):
        if self.invocation_results:
            self.invocation_results.validate()

    def to_map(self):
        _map = super(ListInvocationResultsResponseBody, self).to_map()
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
        if self.invocation_results is not None:
            result['InvocationResults'] = self.invocation_results.to_map()
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
        if m.get('InvocationResults') is not None:
            temp_model = ListInvocationResultsResponseBodyInvocationResults()
            self.invocation_results = temp_model.from_map(m['InvocationResults'])
        return self


class ListInvocationResultsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListInvocationResultsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInvocationResultsResponse, self).to_map()
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
            temp_model = ListInvocationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAutoScaleConfigRequestQueuesInstanceTypes(TeaModel):
    def __init__(self, v_switch_id=None, zone_id=None, spot_price_limit=None, instance_type=None,
                 spot_strategy=None):
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id  # type: str
        self.spot_price_limit = spot_price_limit  # type: float
        self.instance_type = instance_type  # type: str
        self.spot_strategy = spot_strategy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAutoScaleConfigRequestQueuesInstanceTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        return self


class SetAutoScaleConfigRequestQueues(TeaModel):
    def __init__(self, queue_image_id=None, system_disk_category=None, instance_type=None, host_name_suffix=None,
                 spot_strategy=None, host_name_prefix=None, min_nodes_in_queue=None, system_disk_size=None,
                 max_nodes_in_queue=None, enable_auto_shrink=None, queue_name=None, enable_auto_grow=None, system_disk_level=None,
                 spot_price_limit=None, instance_types=None):
        self.queue_image_id = queue_image_id  # type: str
        self.system_disk_category = system_disk_category  # type: str
        self.instance_type = instance_type  # type: str
        self.host_name_suffix = host_name_suffix  # type: str
        self.spot_strategy = spot_strategy  # type: str
        self.host_name_prefix = host_name_prefix  # type: str
        self.min_nodes_in_queue = min_nodes_in_queue  # type: int
        self.system_disk_size = system_disk_size  # type: int
        self.max_nodes_in_queue = max_nodes_in_queue  # type: int
        self.enable_auto_shrink = enable_auto_shrink  # type: bool
        self.queue_name = queue_name  # type: str
        self.enable_auto_grow = enable_auto_grow  # type: bool
        self.system_disk_level = system_disk_level  # type: str
        self.spot_price_limit = spot_price_limit  # type: float
        self.instance_types = instance_types  # type: list[SetAutoScaleConfigRequestQueuesInstanceTypes]

    def validate(self):
        if self.instance_types:
            for k in self.instance_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SetAutoScaleConfigRequestQueues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue_image_id is not None:
            result['QueueImageId'] = self.queue_image_id
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.host_name_suffix is not None:
            result['HostNameSuffix'] = self.host_name_suffix
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.host_name_prefix is not None:
            result['HostNamePrefix'] = self.host_name_prefix
        if self.min_nodes_in_queue is not None:
            result['MinNodesInQueue'] = self.min_nodes_in_queue
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.max_nodes_in_queue is not None:
            result['MaxNodesInQueue'] = self.max_nodes_in_queue
        if self.enable_auto_shrink is not None:
            result['EnableAutoShrink'] = self.enable_auto_shrink
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.enable_auto_grow is not None:
            result['EnableAutoGrow'] = self.enable_auto_grow
        if self.system_disk_level is not None:
            result['SystemDiskLevel'] = self.system_disk_level
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        result['InstanceTypes'] = []
        if self.instance_types is not None:
            for k in self.instance_types:
                result['InstanceTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QueueImageId') is not None:
            self.queue_image_id = m.get('QueueImageId')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('HostNameSuffix') is not None:
            self.host_name_suffix = m.get('HostNameSuffix')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('HostNamePrefix') is not None:
            self.host_name_prefix = m.get('HostNamePrefix')
        if m.get('MinNodesInQueue') is not None:
            self.min_nodes_in_queue = m.get('MinNodesInQueue')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('MaxNodesInQueue') is not None:
            self.max_nodes_in_queue = m.get('MaxNodesInQueue')
        if m.get('EnableAutoShrink') is not None:
            self.enable_auto_shrink = m.get('EnableAutoShrink')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('EnableAutoGrow') is not None:
            self.enable_auto_grow = m.get('EnableAutoGrow')
        if m.get('SystemDiskLevel') is not None:
            self.system_disk_level = m.get('SystemDiskLevel')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        self.instance_types = []
        if m.get('InstanceTypes') is not None:
            for k in m.get('InstanceTypes'):
                temp_model = SetAutoScaleConfigRequestQueuesInstanceTypes()
                self.instance_types.append(temp_model.from_map(k))
        return self


class SetAutoScaleConfigRequest(TeaModel):
    def __init__(self, cluster_id=None, enable_auto_grow=None, enable_auto_shrink=None,
                 grow_interval_in_minutes=None, shrink_interval_in_minutes=None, shrink_idle_times=None, grow_timeout_in_minutes=None,
                 extra_nodes_grow_ratio=None, grow_ratio=None, max_nodes_in_cluster=None, exclude_nodes=None, spot_strategy=None,
                 spot_price_limit=None, image_id=None, queues=None):
        self.cluster_id = cluster_id  # type: str
        self.enable_auto_grow = enable_auto_grow  # type: bool
        self.enable_auto_shrink = enable_auto_shrink  # type: bool
        self.grow_interval_in_minutes = grow_interval_in_minutes  # type: int
        self.shrink_interval_in_minutes = shrink_interval_in_minutes  # type: int
        self.shrink_idle_times = shrink_idle_times  # type: int
        self.grow_timeout_in_minutes = grow_timeout_in_minutes  # type: int
        self.extra_nodes_grow_ratio = extra_nodes_grow_ratio  # type: int
        self.grow_ratio = grow_ratio  # type: int
        self.max_nodes_in_cluster = max_nodes_in_cluster  # type: int
        self.exclude_nodes = exclude_nodes  # type: str
        self.spot_strategy = spot_strategy  # type: str
        self.spot_price_limit = spot_price_limit  # type: float
        self.image_id = image_id  # type: str
        self.queues = queues  # type: list[SetAutoScaleConfigRequestQueues]

    def validate(self):
        if self.queues:
            for k in self.queues:
                if k:
                    k.validate()

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
        if self.grow_interval_in_minutes is not None:
            result['GrowIntervalInMinutes'] = self.grow_interval_in_minutes
        if self.shrink_interval_in_minutes is not None:
            result['ShrinkIntervalInMinutes'] = self.shrink_interval_in_minutes
        if self.shrink_idle_times is not None:
            result['ShrinkIdleTimes'] = self.shrink_idle_times
        if self.grow_timeout_in_minutes is not None:
            result['GrowTimeoutInMinutes'] = self.grow_timeout_in_minutes
        if self.extra_nodes_grow_ratio is not None:
            result['ExtraNodesGrowRatio'] = self.extra_nodes_grow_ratio
        if self.grow_ratio is not None:
            result['GrowRatio'] = self.grow_ratio
        if self.max_nodes_in_cluster is not None:
            result['MaxNodesInCluster'] = self.max_nodes_in_cluster
        if self.exclude_nodes is not None:
            result['ExcludeNodes'] = self.exclude_nodes
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        result['Queues'] = []
        if self.queues is not None:
            for k in self.queues:
                result['Queues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('EnableAutoGrow') is not None:
            self.enable_auto_grow = m.get('EnableAutoGrow')
        if m.get('EnableAutoShrink') is not None:
            self.enable_auto_shrink = m.get('EnableAutoShrink')
        if m.get('GrowIntervalInMinutes') is not None:
            self.grow_interval_in_minutes = m.get('GrowIntervalInMinutes')
        if m.get('ShrinkIntervalInMinutes') is not None:
            self.shrink_interval_in_minutes = m.get('ShrinkIntervalInMinutes')
        if m.get('ShrinkIdleTimes') is not None:
            self.shrink_idle_times = m.get('ShrinkIdleTimes')
        if m.get('GrowTimeoutInMinutes') is not None:
            self.grow_timeout_in_minutes = m.get('GrowTimeoutInMinutes')
        if m.get('ExtraNodesGrowRatio') is not None:
            self.extra_nodes_grow_ratio = m.get('ExtraNodesGrowRatio')
        if m.get('GrowRatio') is not None:
            self.grow_ratio = m.get('GrowRatio')
        if m.get('MaxNodesInCluster') is not None:
            self.max_nodes_in_cluster = m.get('MaxNodesInCluster')
        if m.get('ExcludeNodes') is not None:
            self.exclude_nodes = m.get('ExcludeNodes')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        self.queues = []
        if m.get('Queues') is not None:
            for k in m.get('Queues'):
                temp_model = SetAutoScaleConfigRequestQueues()
                self.queues.append(temp_model.from_map(k))
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetAutoScaleConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetAutoScaleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddNodesRequest(TeaModel):
    def __init__(self, cluster_id=None, image_owner_alias=None, image_id=None, count=None, instance_type=None,
                 compute_spot_strategy=None, compute_spot_price_limit=None, ecs_charge_type=None, period=None, period_unit=None,
                 auto_renew=None, auto_renew_period=None, job_queue=None, create_mode=None, system_disk_type=None,
                 system_disk_size=None, zone_id=None, v_switch_id=None, host_name_prefix=None, host_name_suffix=None,
                 compute_enable_ht=None, allocate_public_address=None, internet_charge_type=None, internet_max_band_width_in=None,
                 internet_max_band_width_out=None, client_token=None, system_disk_level=None, min_count=None, sync=None):
        self.cluster_id = cluster_id  # type: str
        self.image_owner_alias = image_owner_alias  # type: str
        self.image_id = image_id  # type: str
        self.count = count  # type: int
        self.instance_type = instance_type  # type: str
        self.compute_spot_strategy = compute_spot_strategy  # type: str
        self.compute_spot_price_limit = compute_spot_price_limit  # type: str
        self.ecs_charge_type = ecs_charge_type  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.auto_renew = auto_renew  # type: str
        self.auto_renew_period = auto_renew_period  # type: int
        self.job_queue = job_queue  # type: str
        self.create_mode = create_mode  # type: str
        self.system_disk_type = system_disk_type  # type: str
        self.system_disk_size = system_disk_size  # type: int
        self.zone_id = zone_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.host_name_prefix = host_name_prefix  # type: str
        self.host_name_suffix = host_name_suffix  # type: str
        self.compute_enable_ht = compute_enable_ht  # type: bool
        self.allocate_public_address = allocate_public_address  # type: bool
        self.internet_charge_type = internet_charge_type  # type: str
        self.internet_max_band_width_in = internet_max_band_width_in  # type: int
        self.internet_max_band_width_out = internet_max_band_width_out  # type: int
        self.client_token = client_token  # type: str
        self.system_disk_level = system_disk_level  # type: str
        self.min_count = min_count  # type: int
        self.sync = sync  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.compute_spot_strategy is not None:
            result['ComputeSpotStrategy'] = self.compute_spot_strategy
        if self.compute_spot_price_limit is not None:
            result['ComputeSpotPriceLimit'] = self.compute_spot_price_limit
        if self.ecs_charge_type is not None:
            result['EcsChargeType'] = self.ecs_charge_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.create_mode is not None:
            result['CreateMode'] = self.create_mode
        if self.system_disk_type is not None:
            result['SystemDiskType'] = self.system_disk_type
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.host_name_prefix is not None:
            result['HostNamePrefix'] = self.host_name_prefix
        if self.host_name_suffix is not None:
            result['HostNameSuffix'] = self.host_name_suffix
        if self.compute_enable_ht is not None:
            result['ComputeEnableHt'] = self.compute_enable_ht
        if self.allocate_public_address is not None:
            result['AllocatePublicAddress'] = self.allocate_public_address
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_band_width_in is not None:
            result['InternetMaxBandWidthIn'] = self.internet_max_band_width_in
        if self.internet_max_band_width_out is not None:
            result['InternetMaxBandWidthOut'] = self.internet_max_band_width_out
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.system_disk_level is not None:
            result['SystemDiskLevel'] = self.system_disk_level
        if self.min_count is not None:
            result['MinCount'] = self.min_count
        if self.sync is not None:
            result['Sync'] = self.sync
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('ComputeSpotStrategy') is not None:
            self.compute_spot_strategy = m.get('ComputeSpotStrategy')
        if m.get('ComputeSpotPriceLimit') is not None:
            self.compute_spot_price_limit = m.get('ComputeSpotPriceLimit')
        if m.get('EcsChargeType') is not None:
            self.ecs_charge_type = m.get('EcsChargeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('CreateMode') is not None:
            self.create_mode = m.get('CreateMode')
        if m.get('SystemDiskType') is not None:
            self.system_disk_type = m.get('SystemDiskType')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('HostNamePrefix') is not None:
            self.host_name_prefix = m.get('HostNamePrefix')
        if m.get('HostNameSuffix') is not None:
            self.host_name_suffix = m.get('HostNameSuffix')
        if m.get('ComputeEnableHt') is not None:
            self.compute_enable_ht = m.get('ComputeEnableHt')
        if m.get('AllocatePublicAddress') is not None:
            self.allocate_public_address = m.get('AllocatePublicAddress')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandWidthIn') is not None:
            self.internet_max_band_width_in = m.get('InternetMaxBandWidthIn')
        if m.get('InternetMaxBandWidthOut') is not None:
            self.internet_max_band_width_out = m.get('InternetMaxBandWidthOut')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('SystemDiskLevel') is not None:
            self.system_disk_level = m.get('SystemDiskLevel')
        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')
        if m.get('Sync') is not None:
            self.sync = m.get('Sync')
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
    def __init__(self, task_id=None, request_id=None, instance_ids=None):
        self.task_id = task_id  # type: str
        self.request_id = request_id  # type: str
        self.instance_ids = instance_ids  # type: AddNodesResponseBodyInstanceIds

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super(AddNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceIds') is not None:
            temp_model = AddNodesResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        return self


class AddNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSoftwaresRequest(TeaModel):
    def __init__(self, ehpc_version=None, os_tag=None):
        self.ehpc_version = ehpc_version  # type: str
        self.os_tag = os_tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSoftwaresRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ehpc_version is not None:
            result['EhpcVersion'] = self.ehpc_version
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EhpcVersion') is not None:
            self.ehpc_version = m.get('EhpcVersion')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        return self


class ListSoftwaresResponseBodySoftwaresSoftwareInfoApplicationsApplicationInfo(TeaModel):
    def __init__(self, required=None, tag=None, name=None, version=None):
        self.required = required  # type: bool
        self.tag = tag  # type: str
        self.name = name  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSoftwaresResponseBodySoftwaresSoftwareInfoApplicationsApplicationInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required is not None:
            result['Required'] = self.required
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.name is not None:
            result['Name'] = self.name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
    def __init__(self, scheduler_type=None, os_tag=None, scheduler_version=None, account_version=None,
                 account_type=None, ehpc_version=None, applications=None):
        self.scheduler_type = scheduler_type  # type: str
        self.os_tag = os_tag  # type: str
        self.scheduler_version = scheduler_version  # type: str
        self.account_version = account_version  # type: str
        self.account_type = account_type  # type: str
        self.ehpc_version = ehpc_version  # type: str
        self.applications = applications  # type: ListSoftwaresResponseBodySoftwaresSoftwareInfoApplications

    def validate(self):
        if self.applications:
            self.applications.validate()

    def to_map(self):
        _map = super(ListSoftwaresResponseBodySoftwaresSoftwareInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.scheduler_version is not None:
            result['SchedulerVersion'] = self.scheduler_version
        if self.account_version is not None:
            result['AccountVersion'] = self.account_version
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.ehpc_version is not None:
            result['EhpcVersion'] = self.ehpc_version
        if self.applications is not None:
            result['Applications'] = self.applications.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('SchedulerVersion') is not None:
            self.scheduler_version = m.get('SchedulerVersion')
        if m.get('AccountVersion') is not None:
            self.account_version = m.get('AccountVersion')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('EhpcVersion') is not None:
            self.ehpc_version = m.get('EhpcVersion')
        if m.get('Applications') is not None:
            temp_model = ListSoftwaresResponseBodySoftwaresSoftwareInfoApplications()
            self.applications = temp_model.from_map(m['Applications'])
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSoftwaresResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSoftwaresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecurityGroupsRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecurityGroupsRequest, self).to_map()
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


class ListSecurityGroupsResponseBodySecurityGroups(TeaModel):
    def __init__(self, security_group=None):
        self.security_group = security_group  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecurityGroupsResponseBodySecurityGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')
        return self


class ListSecurityGroupsResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, security_groups=None):
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.security_groups = security_groups  # type: ListSecurityGroupsResponseBodySecurityGroups

    def validate(self):
        if self.security_groups:
            self.security_groups.validate()

    def to_map(self):
        _map = super(ListSecurityGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_groups is not None:
            result['SecurityGroups'] = self.security_groups.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityGroups') is not None:
            temp_model = ListSecurityGroupsResponseBodySecurityGroups()
            self.security_groups = temp_model.from_map(m['SecurityGroups'])
        return self


class ListSecurityGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSecurityGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSecurityGroupsResponse, self).to_map()
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
            temp_model = ListSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGWSImagesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGWSImagesRequest, self).to_map()
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


class DescribeGWSImagesResponseBodyImagesImageInfo(TeaModel):
    def __init__(self, status=None, image_type=None, progress=None, size=None, create_time=None, name=None,
                 image_id=None):
        self.status = status  # type: str
        self.image_type = image_type  # type: str
        self.progress = progress  # type: str
        self.size = size  # type: int
        self.create_time = create_time  # type: str
        self.name = name  # type: str
        self.image_id = image_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGWSImagesResponseBodyImagesImageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.size is not None:
            result['Size'] = self.size
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.name is not None:
            result['Name'] = self.name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class DescribeGWSImagesResponseBodyImages(TeaModel):
    def __init__(self, image_info=None):
        self.image_info = image_info  # type: list[DescribeGWSImagesResponseBodyImagesImageInfo]

    def validate(self):
        if self.image_info:
            for k in self.image_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGWSImagesResponseBodyImages, self).to_map()
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
                temp_model = DescribeGWSImagesResponseBodyImagesImageInfo()
                self.image_info.append(temp_model.from_map(k))
        return self


class DescribeGWSImagesResponseBody(TeaModel):
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, images=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.images = images  # type: DescribeGWSImagesResponseBodyImages

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        _map = super(DescribeGWSImagesResponseBody, self).to_map()
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
        if self.images is not None:
            result['Images'] = self.images.to_map()
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
        if m.get('Images') is not None:
            temp_model = DescribeGWSImagesResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        return self


class DescribeGWSImagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeGWSImagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGWSImagesResponse, self).to_map()
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
            temp_model = DescribeGWSImagesResponseBody()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartNodesRequestInstance(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartNodesRequestInstance, self).to_map()
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


class StartNodesRequest(TeaModel):
    def __init__(self, cluster_id=None, role=None, instance=None):
        self.cluster_id = cluster_id  # type: str
        self.role = role  # type: str
        self.instance = instance  # type: list[StartNodesRequestInstance]

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(StartNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.role is not None:
            result['Role'] = self.role
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = StartNodesRequestInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class StartNodesResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None):
        self.task_id = task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartNodesResponseBody, self).to_map()
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


class StartNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartNodesResponse, self).to_map()
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
            temp_model = StartNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserGroupsRequestUser(TeaModel):
    def __init__(self, name=None, group=None):
        self.name = name  # type: str
        self.group = group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserGroupsRequestUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Group') is not None:
            self.group = m.get('Group')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyUserGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyUserGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetQueueRequestNode(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetQueueRequestNode, self).to_map()
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


class SetQueueRequest(TeaModel):
    def __init__(self, cluster_id=None, queue_name=None, node=None):
        self.cluster_id = cluster_id  # type: str
        self.queue_name = queue_name  # type: str
        self.node = node  # type: list[SetQueueRequestNode]

    def validate(self):
        if self.node:
            for k in self.node:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SetQueueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        result['Node'] = []
        if self.node is not None:
            for k in self.node:
                result['Node'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        self.node = []
        if m.get('Node') is not None:
            for k in m.get('Node'):
                temp_model = SetQueueRequestNode()
                self.node.append(temp_model.from_map(k))
        return self


class SetQueueResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetQueueResponseBody, self).to_map()
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


class SetQueueResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetQueueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetQueueResponse, self).to_map()
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
            temp_model = SetQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartClusterRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartClusterRequest, self).to_map()
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


class StartClusterResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None):
        self.task_id = task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartClusterResponseBody, self).to_map()
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


class StartClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartClusterResponse, self).to_map()
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
            temp_model = StartClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomImagesRequest(TeaModel):
    def __init__(self, image_owner_alias=None, base_os_tag=None, instance_type=None, cluster_id=None):
        self.image_owner_alias = image_owner_alias  # type: str
        self.base_os_tag = base_os_tag  # type: str
        self.instance_type = instance_type  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomImagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('BaseOsTag') is not None:
            self.base_os_tag = m.get('BaseOsTag')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ListCustomImagesResponseBodyImagesImageInfoBaseOsTag(TeaModel):
    def __init__(self, platform=None, os_tag=None, version=None, architecture=None):
        self.platform = platform  # type: str
        self.os_tag = os_tag  # type: str
        self.version = version  # type: str
        self.architecture = architecture  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomImagesResponseBodyImagesImageInfoBaseOsTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.version is not None:
            result['Version'] = self.version
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        return self


class ListCustomImagesResponseBodyImagesImageInfoOsTag(TeaModel):
    def __init__(self, platform=None, os_tag=None, version=None, architecture=None, base_os_tag=None):
        self.platform = platform  # type: str
        self.os_tag = os_tag  # type: str
        self.version = version  # type: str
        self.architecture = architecture  # type: str
        self.base_os_tag = base_os_tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCustomImagesResponseBodyImagesImageInfoOsTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.version is not None:
            result['Version'] = self.version
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('BaseOsTag') is not None:
            self.base_os_tag = m.get('BaseOsTag')
        return self


class ListCustomImagesResponseBodyImagesImageInfo(TeaModel):
    def __init__(self, status=None, post_install_script=None, description=None, size=None, image_owner_alias=None,
                 image_name=None, sku_code=None, pricing_cycle=None, image_id=None, product_code=None, uid=None,
                 base_os_tag=None, os_tag=None):
        self.status = status  # type: str
        self.post_install_script = post_install_script  # type: str
        self.description = description  # type: str
        self.size = size  # type: int
        self.image_owner_alias = image_owner_alias  # type: str
        self.image_name = image_name  # type: str
        self.sku_code = sku_code  # type: str
        self.pricing_cycle = pricing_cycle  # type: str
        self.image_id = image_id  # type: str
        self.product_code = product_code  # type: str
        self.uid = uid  # type: str
        self.base_os_tag = base_os_tag  # type: ListCustomImagesResponseBodyImagesImageInfoBaseOsTag
        self.os_tag = os_tag  # type: ListCustomImagesResponseBodyImagesImageInfoOsTag

    def validate(self):
        if self.base_os_tag:
            self.base_os_tag.validate()
        if self.os_tag:
            self.os_tag.validate()

    def to_map(self):
        _map = super(ListCustomImagesResponseBodyImagesImageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.post_install_script is not None:
            result['PostInstallScript'] = self.post_install_script
        if self.description is not None:
            result['Description'] = self.description
        if self.size is not None:
            result['Size'] = self.size
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.sku_code is not None:
            result['SkuCode'] = self.sku_code
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag.to_map()
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PostInstallScript') is not None:
            self.post_install_script = m.get('PostInstallScript')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('SkuCode') is not None:
            self.sku_code = m.get('SkuCode')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('BaseOsTag') is not None:
            temp_model = ListCustomImagesResponseBodyImagesImageInfoBaseOsTag()
            self.base_os_tag = temp_model.from_map(m['BaseOsTag'])
        if m.get('OsTag') is not None:
            temp_model = ListCustomImagesResponseBodyImagesImageInfoOsTag()
            self.os_tag = temp_model.from_map(m['OsTag'])
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
    def __init__(self, request_id=None, images=None):
        self.request_id = request_id  # type: str
        self.images = images  # type: ListCustomImagesResponseBodyImages

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        _map = super(ListCustomImagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.images is not None:
            result['Images'] = self.images.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Images') is not None:
            temp_model = ListCustomImagesResponseBodyImages()
            self.images = temp_model.from_map(m['Images'])
        return self


class ListCustomImagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListCustomImagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListCustomImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUsersRequestUser(TeaModel):
    def __init__(self, password=None, name=None, group=None):
        self.password = password  # type: str
        self.name = name  # type: str
        self.group = group  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUsersRequestUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.name is not None:
            result['Name'] = self.name
        if self.group is not None:
            result['Group'] = self.group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        return self


class AddUsersRequest(TeaModel):
    def __init__(self, cluster_id=None, user=None):
        self.cluster_id = cluster_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGWSClusterRequest(TeaModel):
    def __init__(self, vpc_id=None, cluster_type=None, name=None, v_switch_id=None):
        self.vpc_id = vpc_id  # type: str
        self.cluster_type = cluster_type  # type: str
        self.name = name  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGWSClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.name is not None:
            result['Name'] = self.name
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateGWSClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None):
        self.cluster_id = cluster_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGWSClusterResponseBody, self).to_map()
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


class CreateGWSClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateGWSClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGWSClusterResponse, self).to_map()
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
            temp_model = CreateGWSClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobTemplatesRequest(TeaModel):
    def __init__(self, name=None, page_number=None, page_size=None):
        self.name = name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListJobTemplatesResponseBodyTemplatesJobTemplates(TeaModel):
    def __init__(self, task=None, variables=None, command_line=None, queue=None, priority=None, mem=None, thread=None,
                 array_request=None, stderr_redirect_path=None, node=None, stdout_redirect_path=None, gpu=None, package_path=None,
                 clock_time=None, re_runable=None, name=None, id=None, runas_user=None):
        self.task = task  # type: int
        self.variables = variables  # type: str
        self.command_line = command_line  # type: str
        self.queue = queue  # type: str
        self.priority = priority  # type: int
        self.mem = mem  # type: str
        self.thread = thread  # type: int
        self.array_request = array_request  # type: str
        self.stderr_redirect_path = stderr_redirect_path  # type: str
        self.node = node  # type: int
        self.stdout_redirect_path = stdout_redirect_path  # type: str
        self.gpu = gpu  # type: int
        self.package_path = package_path  # type: str
        self.clock_time = clock_time  # type: str
        self.re_runable = re_runable  # type: bool
        self.name = name  # type: str
        self.id = id  # type: str
        self.runas_user = runas_user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobTemplatesResponseBodyTemplatesJobTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task is not None:
            result['Task'] = self.task
        if self.variables is not None:
            result['Variables'] = self.variables
        if self.command_line is not None:
            result['CommandLine'] = self.command_line
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.mem is not None:
            result['Mem'] = self.mem
        if self.thread is not None:
            result['Thread'] = self.thread
        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request
        if self.stderr_redirect_path is not None:
            result['StderrRedirectPath'] = self.stderr_redirect_path
        if self.node is not None:
            result['Node'] = self.node
        if self.stdout_redirect_path is not None:
            result['StdoutRedirectPath'] = self.stdout_redirect_path
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.package_path is not None:
            result['PackagePath'] = self.package_path
        if self.clock_time is not None:
            result['ClockTime'] = self.clock_time
        if self.re_runable is not None:
            result['ReRunable'] = self.re_runable
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Task') is not None:
            self.task = m.get('Task')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        if m.get('Thread') is not None:
            self.thread = m.get('Thread')
        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')
        if m.get('StderrRedirectPath') is not None:
            self.stderr_redirect_path = m.get('StderrRedirectPath')
        if m.get('Node') is not None:
            self.node = m.get('Node')
        if m.get('StdoutRedirectPath') is not None:
            self.stdout_redirect_path = m.get('StdoutRedirectPath')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('PackagePath') is not None:
            self.package_path = m.get('PackagePath')
        if m.get('ClockTime') is not None:
            self.clock_time = m.get('ClockTime')
        if m.get('ReRunable') is not None:
            self.re_runable = m.get('ReRunable')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')
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
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, templates=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.templates = templates  # type: ListJobTemplatesResponseBodyTemplates

    def validate(self):
        if self.templates:
            self.templates.validate()

    def to_map(self):
        _map = super(ListJobTemplatesResponseBody, self).to_map()
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
        if self.templates is not None:
            result['Templates'] = self.templates.to_map()
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
        if m.get('Templates') is not None:
            temp_model = ListJobTemplatesResponseBodyTemplates()
            self.templates = temp_model.from_map(m['Templates'])
        return self


class ListJobTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListJobTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListJobTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageGatewayConfigRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageGatewayConfigRequest, self).to_map()
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


class DescribeImageGatewayConfigResponseBodyImagegwLocationsLocationInfo(TeaModel):
    def __init__(self, url=None, remote_type=None, location=None, authentication=None):
        self.url = url  # type: str
        self.remote_type = remote_type  # type: str
        self.location = location  # type: str
        self.authentication = authentication  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageGatewayConfigResponseBodyImagegwLocationsLocationInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['URL'] = self.url
        if self.remote_type is not None:
            result['RemoteType'] = self.remote_type
        if self.location is not None:
            result['Location'] = self.location
        if self.authentication is not None:
            result['Authentication'] = self.authentication
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('URL') is not None:
            self.url = m.get('URL')
        if m.get('RemoteType') is not None:
            self.remote_type = m.get('RemoteType')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Authentication') is not None:
            self.authentication = m.get('Authentication')
        return self


class DescribeImageGatewayConfigResponseBodyImagegwLocations(TeaModel):
    def __init__(self, location_info=None):
        self.location_info = location_info  # type: list[DescribeImageGatewayConfigResponseBodyImagegwLocationsLocationInfo]

    def validate(self):
        if self.location_info:
            for k in self.location_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeImageGatewayConfigResponseBodyImagegwLocations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LocationInfo'] = []
        if self.location_info is not None:
            for k in self.location_info:
                result['LocationInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.location_info = []
        if m.get('LocationInfo') is not None:
            for k in m.get('LocationInfo'):
                temp_model = DescribeImageGatewayConfigResponseBodyImagegwLocationsLocationInfo()
                self.location_info.append(temp_model.from_map(k))
        return self


class DescribeImageGatewayConfigResponseBodyImagegw(TeaModel):
    def __init__(self, update_date_time=None, image_expiration_timeout=None, mongo_dburi=None,
                 default_image_location=None, pull_update_timeout=None, locations=None):
        self.update_date_time = update_date_time  # type: str
        self.image_expiration_timeout = image_expiration_timeout  # type: str
        self.mongo_dburi = mongo_dburi  # type: str
        self.default_image_location = default_image_location  # type: str
        self.pull_update_timeout = pull_update_timeout  # type: long
        self.locations = locations  # type: DescribeImageGatewayConfigResponseBodyImagegwLocations

    def validate(self):
        if self.locations:
            self.locations.validate()

    def to_map(self):
        _map = super(DescribeImageGatewayConfigResponseBodyImagegw, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_date_time is not None:
            result['UpdateDateTime'] = self.update_date_time
        if self.image_expiration_timeout is not None:
            result['ImageExpirationTimeout'] = self.image_expiration_timeout
        if self.mongo_dburi is not None:
            result['MongoDBURI'] = self.mongo_dburi
        if self.default_image_location is not None:
            result['DefaultImageLocation'] = self.default_image_location
        if self.pull_update_timeout is not None:
            result['PullUpdateTimeout'] = self.pull_update_timeout
        if self.locations is not None:
            result['Locations'] = self.locations.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UpdateDateTime') is not None:
            self.update_date_time = m.get('UpdateDateTime')
        if m.get('ImageExpirationTimeout') is not None:
            self.image_expiration_timeout = m.get('ImageExpirationTimeout')
        if m.get('MongoDBURI') is not None:
            self.mongo_dburi = m.get('MongoDBURI')
        if m.get('DefaultImageLocation') is not None:
            self.default_image_location = m.get('DefaultImageLocation')
        if m.get('PullUpdateTimeout') is not None:
            self.pull_update_timeout = m.get('PullUpdateTimeout')
        if m.get('Locations') is not None:
            temp_model = DescribeImageGatewayConfigResponseBodyImagegwLocations()
            self.locations = temp_model.from_map(m['Locations'])
        return self


class DescribeImageGatewayConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, imagegw=None):
        self.request_id = request_id  # type: str
        self.imagegw = imagegw  # type: DescribeImageGatewayConfigResponseBodyImagegw

    def validate(self):
        if self.imagegw:
            self.imagegw.validate()

    def to_map(self):
        _map = super(DescribeImageGatewayConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.imagegw is not None:
            result['Imagegw'] = self.imagegw.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Imagegw') is not None:
            temp_model = DescribeImageGatewayConfigResponseBodyImagegw()
            self.imagegw = temp_model.from_map(m['Imagegw'])
        return self


class DescribeImageGatewayConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeImageGatewayConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeImageGatewayConfigResponse, self).to_map()
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
            temp_model = DescribeImageGatewayConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGWSConnectTicketRequest(TeaModel):
    def __init__(self, instance_id=None, app_name=None):
        self.instance_id = instance_id  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGWSConnectTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class GetGWSConnectTicketResponseBody(TeaModel):
    def __init__(self, ticket=None, request_id=None):
        self.ticket = ticket  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGWSConnectTicketResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetGWSConnectTicketResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetGWSConnectTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGWSConnectTicketResponse, self).to_map()
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
            temp_model = GetGWSConnectTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(self, cluster_id=None, page_number=None, page_size=None, task_id=None, archived=None):
        self.cluster_id = cluster_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.task_id = task_id  # type: str
        self.archived = archived  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.archived is not None:
            result['Archived'] = self.archived
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Archived') is not None:
            self.archived = m.get('Archived')
        return self


class ListTasksResponseBodyTasks(TeaModel):
    def __init__(self, status=None, task_type=None, total_steps=None, current_step=None, result=None, errors=None,
                 task_id=None, request=None, cluster_id=None):
        self.status = status  # type: str
        self.task_type = task_type  # type: str
        self.total_steps = total_steps  # type: int
        self.current_step = current_step  # type: int
        self.result = result  # type: str
        self.errors = errors  # type: str
        self.task_id = task_id  # type: str
        self.request = request  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTasksResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.total_steps is not None:
            result['TotalSteps'] = self.total_steps
        if self.current_step is not None:
            result['CurrentStep'] = self.current_step
        if self.result is not None:
            result['Result'] = self.result
        if self.errors is not None:
            result['Errors'] = self.errors
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request is not None:
            result['Request'] = self.request
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TotalSteps') is not None:
            self.total_steps = m.get('TotalSteps')
        if m.get('CurrentStep') is not None:
            self.current_step = m.get('CurrentStep')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Errors') is not None:
            self.errors = m.get('Errors')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Request') is not None:
            self.request = m.get('Request')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, tasks=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.tasks = tasks  # type: list[ListTasksResponseBodyTasks]

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTasksResponseBody, self).to_map()
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
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
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
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class ListTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTasksResponse, self).to_map()
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
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopClusterRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopClusterRequest, self).to_map()
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


class StopClusterResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None):
        self.task_id = task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopClusterResponseBody, self).to_map()
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


class StopClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopClusterResponse, self).to_map()
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
            temp_model = StopClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSecurityGroupRequest(TeaModel):
    def __init__(self, cluster_id=None, security_group_id=None, client_token=None):
        self.cluster_id = cluster_id  # type: str
        self.security_group_id = security_group_id  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSecurityGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class AddSecurityGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSecurityGroupResponseBody, self).to_map()
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


class AddSecurityGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddSecurityGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddSecurityGroupResponse, self).to_map()
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
            temp_model = AddSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodesNoPagingRequest(TeaModel):
    def __init__(self, cluster_id=None, role=None, host_name=None, only_detached=None, sequence=None):
        self.cluster_id = cluster_id  # type: str
        self.role = role  # type: str
        self.host_name = host_name  # type: str
        self.only_detached = only_detached  # type: bool
        self.sequence = sequence  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesNoPagingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.role is not None:
            result['Role'] = self.role
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.only_detached is not None:
            result['OnlyDetached'] = self.only_detached
        if self.sequence is not None:
            result['Sequence'] = self.sequence
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('OnlyDetached') is not None:
            self.only_detached = m.get('OnlyDetached')
        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')
        return self


class ListNodesNoPagingResponseBodyNodesNodeInfo(TeaModel):
    def __init__(self, status=None, host_name=None, instance_type=None, image_id=None, id=None):
        self.status = status  # type: str
        self.host_name = host_name  # type: str
        self.instance_type = instance_type  # type: str
        self.image_id = image_id  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodesNoPagingResponseBodyNodesNodeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
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
    def __init__(self, request_id=None, nodes=None):
        self.request_id = request_id  # type: str
        self.nodes = nodes  # type: ListNodesNoPagingResponseBodyNodes

    def validate(self):
        if self.nodes:
            self.nodes.validate()

    def to_map(self):
        _map = super(ListNodesNoPagingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Nodes') is not None:
            temp_model = ListNodesNoPagingResponseBodyNodes()
            self.nodes = temp_model.from_map(m['Nodes'])
        return self


class ListNodesNoPagingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListNodesNoPagingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNodesNoPagingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGWSInstanceNameRequest(TeaModel):
    def __init__(self, instance_id=None, name=None):
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetGWSInstanceNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SetGWSInstanceNameResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetGWSInstanceNameResponseBody, self).to_map()
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


class SetGWSInstanceNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetGWSInstanceNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetGWSInstanceNameResponse, self).to_map()
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
            temp_model = SetGWSInstanceNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHybridClusterRequestEcsOrderCompute(TeaModel):
    def __init__(self, instance_type=None):
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHybridClusterRequestEcsOrderCompute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateHybridClusterRequestEcsOrder(TeaModel):
    def __init__(self, compute=None):
        self.compute = compute  # type: CreateHybridClusterRequestEcsOrderCompute

    def validate(self):
        self.validate_required(self.compute, 'compute')
        if self.compute:
            self.compute.validate()

    def to_map(self):
        _map = super(CreateHybridClusterRequestEcsOrder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute is not None:
            result['Compute'] = self.compute.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Compute') is not None:
            temp_model = CreateHybridClusterRequestEcsOrderCompute()
            self.compute = temp_model.from_map(m['Compute'])
        return self


class CreateHybridClusterRequestNodes(TeaModel):
    def __init__(self, scheduler_type=None, ip_address=None, host_name=None, role=None, account_type=None):
        self.scheduler_type = scheduler_type  # type: str
        self.ip_address = ip_address  # type: str
        self.host_name = host_name  # type: str
        self.role = role  # type: str
        self.account_type = account_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHybridClusterRequestNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.role is not None:
            result['Role'] = self.role
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class CreateHybridClusterRequestApplication(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHybridClusterRequestApplication, self).to_map()
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


class CreateHybridClusterRequestPostInstallScript(TeaModel):
    def __init__(self, args=None, url=None):
        self.args = args  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHybridClusterRequestPostInstallScript, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateHybridClusterRequest(TeaModel):
    def __init__(self, ecs_order=None, zone_id=None, name=None, description=None, ehpc_version=None,
                 client_version=None, os_tag=None, domain=None, location=None, security_group_id=None, security_group_name=None,
                 vpc_id=None, v_switch_id=None, volume_type=None, volume_id=None, volume_protocol=None,
                 volume_mountpoint=None, remote_directory=None, on_premise_volume_protocol=None, on_premise_volume_mount_point=None,
                 on_premise_volume_remote_path=None, on_premise_volume_local_path=None, password=None, key_pair_name=None, job_queue=None,
                 resource_group_id=None, scheduler_pre_install=None, compute_spot_strategy=None, compute_spot_price_limit=None,
                 image_owner_alias=None, image_id=None, client_token=None, multi_os=None, nodes=None, application=None,
                 post_install_script=None):
        self.ecs_order = ecs_order  # type: CreateHybridClusterRequestEcsOrder
        self.zone_id = zone_id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.ehpc_version = ehpc_version  # type: str
        self.client_version = client_version  # type: str
        self.os_tag = os_tag  # type: str
        self.domain = domain  # type: str
        self.location = location  # type: str
        self.security_group_id = security_group_id  # type: str
        self.security_group_name = security_group_name  # type: str
        self.vpc_id = vpc_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.volume_type = volume_type  # type: str
        self.volume_id = volume_id  # type: str
        self.volume_protocol = volume_protocol  # type: str
        self.volume_mountpoint = volume_mountpoint  # type: str
        self.remote_directory = remote_directory  # type: str
        self.on_premise_volume_protocol = on_premise_volume_protocol  # type: str
        self.on_premise_volume_mount_point = on_premise_volume_mount_point  # type: str
        self.on_premise_volume_remote_path = on_premise_volume_remote_path  # type: str
        self.on_premise_volume_local_path = on_premise_volume_local_path  # type: str
        self.password = password  # type: str
        self.key_pair_name = key_pair_name  # type: str
        self.job_queue = job_queue  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.scheduler_pre_install = scheduler_pre_install  # type: bool
        self.compute_spot_strategy = compute_spot_strategy  # type: str
        self.compute_spot_price_limit = compute_spot_price_limit  # type: float
        self.image_owner_alias = image_owner_alias  # type: str
        self.image_id = image_id  # type: str
        self.client_token = client_token  # type: str
        self.multi_os = multi_os  # type: bool
        self.nodes = nodes  # type: list[CreateHybridClusterRequestNodes]
        self.application = application  # type: list[CreateHybridClusterRequestApplication]
        self.post_install_script = post_install_script  # type: list[CreateHybridClusterRequestPostInstallScript]

    def validate(self):
        if self.ecs_order:
            self.ecs_order.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.application:
            for k in self.application:
                if k:
                    k.validate()
        if self.post_install_script:
            for k in self.post_install_script:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateHybridClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_order is not None:
            result['EcsOrder'] = self.ecs_order.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.ehpc_version is not None:
            result['EhpcVersion'] = self.ehpc_version
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.location is not None:
            result['Location'] = self.location
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        if self.on_premise_volume_protocol is not None:
            result['OnPremiseVolumeProtocol'] = self.on_premise_volume_protocol
        if self.on_premise_volume_mount_point is not None:
            result['OnPremiseVolumeMountPoint'] = self.on_premise_volume_mount_point
        if self.on_premise_volume_remote_path is not None:
            result['OnPremiseVolumeRemotePath'] = self.on_premise_volume_remote_path
        if self.on_premise_volume_local_path is not None:
            result['OnPremiseVolumeLocalPath'] = self.on_premise_volume_local_path
        if self.password is not None:
            result['Password'] = self.password
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scheduler_pre_install is not None:
            result['SchedulerPreInstall'] = self.scheduler_pre_install
        if self.compute_spot_strategy is not None:
            result['ComputeSpotStrategy'] = self.compute_spot_strategy
        if self.compute_spot_price_limit is not None:
            result['ComputeSpotPriceLimit'] = self.compute_spot_price_limit
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.multi_os is not None:
            result['MultiOs'] = self.multi_os
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        result['Application'] = []
        if self.application is not None:
            for k in self.application:
                result['Application'].append(k.to_map() if k else None)
        result['PostInstallScript'] = []
        if self.post_install_script is not None:
            for k in self.post_install_script:
                result['PostInstallScript'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EcsOrder') is not None:
            temp_model = CreateHybridClusterRequestEcsOrder()
            self.ecs_order = temp_model.from_map(m['EcsOrder'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EhpcVersion') is not None:
            self.ehpc_version = m.get('EhpcVersion')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        if m.get('OnPremiseVolumeProtocol') is not None:
            self.on_premise_volume_protocol = m.get('OnPremiseVolumeProtocol')
        if m.get('OnPremiseVolumeMountPoint') is not None:
            self.on_premise_volume_mount_point = m.get('OnPremiseVolumeMountPoint')
        if m.get('OnPremiseVolumeRemotePath') is not None:
            self.on_premise_volume_remote_path = m.get('OnPremiseVolumeRemotePath')
        if m.get('OnPremiseVolumeLocalPath') is not None:
            self.on_premise_volume_local_path = m.get('OnPremiseVolumeLocalPath')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SchedulerPreInstall') is not None:
            self.scheduler_pre_install = m.get('SchedulerPreInstall')
        if m.get('ComputeSpotStrategy') is not None:
            self.compute_spot_strategy = m.get('ComputeSpotStrategy')
        if m.get('ComputeSpotPriceLimit') is not None:
            self.compute_spot_price_limit = m.get('ComputeSpotPriceLimit')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MultiOs') is not None:
            self.multi_os = m.get('MultiOs')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = CreateHybridClusterRequestNodes()
                self.nodes.append(temp_model.from_map(k))
        self.application = []
        if m.get('Application') is not None:
            for k in m.get('Application'):
                temp_model = CreateHybridClusterRequestApplication()
                self.application.append(temp_model.from_map(k))
        self.post_install_script = []
        if m.get('PostInstallScript') is not None:
            for k in m.get('PostInstallScript'):
                temp_model = CreateHybridClusterRequestPostInstallScript()
                self.post_install_script.append(temp_model.from_map(k))
        return self


class CreateHybridClusterResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None, cluster_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHybridClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class CreateHybridClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateHybridClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateHybridClusterResponse, self).to_map()
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
            temp_model = CreateHybridClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQueueConfigRequest(TeaModel):
    def __init__(self, cluster_id=None, queue_name=None, resource_group_id=None, compute_instance_type=None):
        self.cluster_id = cluster_id  # type: str
        self.queue_name = queue_name  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.compute_instance_type = compute_instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateQueueConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.compute_instance_type is not None:
            result['ComputeInstanceType'] = self.compute_instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ComputeInstanceType') is not None:
            self.compute_instance_type = m.get('ComputeInstanceType')
        return self


class UpdateQueueConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateQueueConfigResponseBody, self).to_map()
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


class UpdateQueueConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateQueueConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateQueueConfigResponse, self).to_map()
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
            temp_model = UpdateQueueConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopVisualServiceRequest(TeaModel):
    def __init__(self, cluster_id=None, cidr_ip=None, port=None):
        self.cluster_id = cluster_id  # type: str
        self.cidr_ip = cidr_ip  # type: str
        self.port = port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopVisualServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class StopVisualServiceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopVisualServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopVisualServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopVisualServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopVisualServiceResponse, self).to_map()
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
            temp_model = StopVisualServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
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


class CreateClusterRequestEcsOrder(TeaModel):
    def __init__(self, manager=None, compute=None, login=None):
        self.manager = manager  # type: CreateClusterRequestEcsOrderManager
        self.compute = compute  # type: CreateClusterRequestEcsOrderCompute
        self.login = login  # type: CreateClusterRequestEcsOrderLogin

    def validate(self):
        self.validate_required(self.manager, 'manager')
        if self.manager:
            self.manager.validate()
        self.validate_required(self.compute, 'compute')
        if self.compute:
            self.compute.validate()
        self.validate_required(self.login, 'login')
        if self.login:
            self.login.validate()

    def to_map(self):
        _map = super(CreateClusterRequestEcsOrder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['Manager'] = self.manager.to_map()
        if self.compute is not None:
            result['Compute'] = self.compute.to_map()
        if self.login is not None:
            result['Login'] = self.login.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Manager') is not None:
            temp_model = CreateClusterRequestEcsOrderManager()
            self.manager = temp_model.from_map(m['Manager'])
        if m.get('Compute') is not None:
            temp_model = CreateClusterRequestEcsOrderCompute()
            self.compute = temp_model.from_map(m['Compute'])
        if m.get('Login') is not None:
            temp_model = CreateClusterRequestEcsOrderLogin()
            self.login = temp_model.from_map(m['Login'])
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


class CreateClusterRequestAdditionalVolumesRoles(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequestAdditionalVolumesRoles, self).to_map()
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


class CreateClusterRequestAdditionalVolumes(TeaModel):
    def __init__(self, job_queue=None, volume_id=None, roles=None, volume_mountpoint=None, remote_directory=None,
                 volume_type=None, local_directory=None, volume_protocol=None, location=None):
        self.job_queue = job_queue  # type: str
        self.volume_id = volume_id  # type: str
        self.roles = roles  # type: list[CreateClusterRequestAdditionalVolumesRoles]
        self.volume_mountpoint = volume_mountpoint  # type: str
        self.remote_directory = remote_directory  # type: str
        self.volume_type = volume_type  # type: str
        self.local_directory = local_directory  # type: str
        self.volume_protocol = volume_protocol  # type: str
        self.location = location  # type: str

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateClusterRequestAdditionalVolumes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        result['Roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['Roles'].append(k.to_map() if k else None)
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        if self.local_directory is not None:
            result['LocalDirectory'] = self.local_directory
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        self.roles = []
        if m.get('Roles') is not None:
            for k in m.get('Roles'):
                temp_model = CreateClusterRequestAdditionalVolumesRoles()
                self.roles.append(temp_model.from_map(k))
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        if m.get('LocalDirectory') is not None:
            self.local_directory = m.get('LocalDirectory')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class CreateClusterRequestPostInstallScript(TeaModel):
    def __init__(self, args=None, url=None):
        self.args = args  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequestPostInstallScript, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateClusterRequest(TeaModel):
    def __init__(self, ecs_order=None, zone_id=None, name=None, description=None, ehpc_version=None,
                 client_version=None, os_tag=None, account_type=None, scheduler_type=None, security_group_id=None,
                 security_group_name=None, vpc_id=None, v_switch_id=None, volume_type=None, volume_id=None, volume_protocol=None,
                 volume_mountpoint=None, remote_directory=None, deploy_mode=None, ha_enable=None, ecs_charge_type=None, password=None,
                 key_pair_name=None, image_owner_alias=None, image_id=None, scc_cluster_id=None, compute_spot_strategy=None,
                 compute_spot_price_limit=None, compute_enable_ht=None, period=None, period_unit=None, auto_renew=None,
                 auto_renew_period=None, input_file_url=None, job_queue=None, system_disk_type=None, system_disk_size=None,
                 remote_vis_enable=None, resource_group_id=None, client_token=None, without_elastic_ip=None, system_disk_level=None,
                 is_compute_ess=None, cluster_version=None, application=None, additional_volumes=None, post_install_script=None):
        self.ecs_order = ecs_order  # type: CreateClusterRequestEcsOrder
        self.zone_id = zone_id  # type: str
        self.name = name  # type: str
        self.description = description  # type: str
        self.ehpc_version = ehpc_version  # type: str
        self.client_version = client_version  # type: str
        self.os_tag = os_tag  # type: str
        self.account_type = account_type  # type: str
        self.scheduler_type = scheduler_type  # type: str
        self.security_group_id = security_group_id  # type: str
        self.security_group_name = security_group_name  # type: str
        self.vpc_id = vpc_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.volume_type = volume_type  # type: str
        self.volume_id = volume_id  # type: str
        self.volume_protocol = volume_protocol  # type: str
        self.volume_mountpoint = volume_mountpoint  # type: str
        self.remote_directory = remote_directory  # type: str
        self.deploy_mode = deploy_mode  # type: str
        self.ha_enable = ha_enable  # type: bool
        self.ecs_charge_type = ecs_charge_type  # type: str
        self.password = password  # type: str
        self.key_pair_name = key_pair_name  # type: str
        self.image_owner_alias = image_owner_alias  # type: str
        self.image_id = image_id  # type: str
        self.scc_cluster_id = scc_cluster_id  # type: str
        self.compute_spot_strategy = compute_spot_strategy  # type: str
        self.compute_spot_price_limit = compute_spot_price_limit  # type: str
        self.compute_enable_ht = compute_enable_ht  # type: bool
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.auto_renew = auto_renew  # type: str
        self.auto_renew_period = auto_renew_period  # type: int
        self.input_file_url = input_file_url  # type: str
        self.job_queue = job_queue  # type: str
        self.system_disk_type = system_disk_type  # type: str
        self.system_disk_size = system_disk_size  # type: int
        self.remote_vis_enable = remote_vis_enable  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.client_token = client_token  # type: str
        self.without_elastic_ip = without_elastic_ip  # type: bool
        self.system_disk_level = system_disk_level  # type: str
        self.is_compute_ess = is_compute_ess  # type: bool
        self.cluster_version = cluster_version  # type: str
        self.application = application  # type: list[CreateClusterRequestApplication]
        self.additional_volumes = additional_volumes  # type: list[CreateClusterRequestAdditionalVolumes]
        self.post_install_script = post_install_script  # type: list[CreateClusterRequestPostInstallScript]

    def validate(self):
        if self.ecs_order:
            self.ecs_order.validate()
        if self.application:
            for k in self.application:
                if k:
                    k.validate()
        if self.additional_volumes:
            for k in self.additional_volumes:
                if k:
                    k.validate()
        if self.post_install_script:
            for k in self.post_install_script:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_order is not None:
            result['EcsOrder'] = self.ecs_order.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.ehpc_version is not None:
            result['EhpcVersion'] = self.ehpc_version
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.ha_enable is not None:
            result['HaEnable'] = self.ha_enable
        if self.ecs_charge_type is not None:
            result['EcsChargeType'] = self.ecs_charge_type
        if self.password is not None:
            result['Password'] = self.password
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.scc_cluster_id is not None:
            result['SccClusterId'] = self.scc_cluster_id
        if self.compute_spot_strategy is not None:
            result['ComputeSpotStrategy'] = self.compute_spot_strategy
        if self.compute_spot_price_limit is not None:
            result['ComputeSpotPriceLimit'] = self.compute_spot_price_limit
        if self.compute_enable_ht is not None:
            result['ComputeEnableHt'] = self.compute_enable_ht
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.input_file_url is not None:
            result['InputFileUrl'] = self.input_file_url
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.system_disk_type is not None:
            result['SystemDiskType'] = self.system_disk_type
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.remote_vis_enable is not None:
            result['RemoteVisEnable'] = self.remote_vis_enable
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.without_elastic_ip is not None:
            result['WithoutElasticIp'] = self.without_elastic_ip
        if self.system_disk_level is not None:
            result['SystemDiskLevel'] = self.system_disk_level
        if self.is_compute_ess is not None:
            result['IsComputeEss'] = self.is_compute_ess
        if self.cluster_version is not None:
            result['ClusterVersion'] = self.cluster_version
        result['Application'] = []
        if self.application is not None:
            for k in self.application:
                result['Application'].append(k.to_map() if k else None)
        result['AdditionalVolumes'] = []
        if self.additional_volumes is not None:
            for k in self.additional_volumes:
                result['AdditionalVolumes'].append(k.to_map() if k else None)
        result['PostInstallScript'] = []
        if self.post_install_script is not None:
            for k in self.post_install_script:
                result['PostInstallScript'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EcsOrder') is not None:
            temp_model = CreateClusterRequestEcsOrder()
            self.ecs_order = temp_model.from_map(m['EcsOrder'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EhpcVersion') is not None:
            self.ehpc_version = m.get('EhpcVersion')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('HaEnable') is not None:
            self.ha_enable = m.get('HaEnable')
        if m.get('EcsChargeType') is not None:
            self.ecs_charge_type = m.get('EcsChargeType')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('SccClusterId') is not None:
            self.scc_cluster_id = m.get('SccClusterId')
        if m.get('ComputeSpotStrategy') is not None:
            self.compute_spot_strategy = m.get('ComputeSpotStrategy')
        if m.get('ComputeSpotPriceLimit') is not None:
            self.compute_spot_price_limit = m.get('ComputeSpotPriceLimit')
        if m.get('ComputeEnableHt') is not None:
            self.compute_enable_ht = m.get('ComputeEnableHt')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('InputFileUrl') is not None:
            self.input_file_url = m.get('InputFileUrl')
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('SystemDiskType') is not None:
            self.system_disk_type = m.get('SystemDiskType')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('RemoteVisEnable') is not None:
            self.remote_vis_enable = m.get('RemoteVisEnable')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('WithoutElasticIp') is not None:
            self.without_elastic_ip = m.get('WithoutElasticIp')
        if m.get('SystemDiskLevel') is not None:
            self.system_disk_level = m.get('SystemDiskLevel')
        if m.get('IsComputeEss') is not None:
            self.is_compute_ess = m.get('IsComputeEss')
        if m.get('ClusterVersion') is not None:
            self.cluster_version = m.get('ClusterVersion')
        self.application = []
        if m.get('Application') is not None:
            for k in m.get('Application'):
                temp_model = CreateClusterRequestApplication()
                self.application.append(temp_model.from_map(k))
        self.additional_volumes = []
        if m.get('AdditionalVolumes') is not None:
            for k in m.get('AdditionalVolumes'):
                temp_model = CreateClusterRequestAdditionalVolumes()
                self.additional_volumes.append(temp_model.from_map(k))
        self.post_install_script = []
        if m.get('PostInstallScript') is not None:
            for k in m.get('PostInstallScript'):
                temp_model = CreateClusterRequestPostInstallScript()
                self.post_install_script.append(temp_model.from_map(k))
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None, cluster_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageRequest(TeaModel):
    def __init__(self, cluster_id=None, repository=None, image_tag=None, container_type=None):
        self.cluster_id = cluster_id  # type: str
        self.repository = repository  # type: str
        self.image_tag = image_tag  # type: str
        self.container_type = container_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.repository is not None:
            result['Repository'] = self.repository
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.container_type is not None:
            result['ContainerType'] = self.container_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('ContainerType') is not None:
            self.container_type = m.get('ContainerType')
        return self


class DescribeImageResponseBodyImageInfo(TeaModel):
    def __init__(self, type=None, status=None, update_date_time=None, repository=None, tag=None, system=None,
                 image_id=None):
        self.type = type  # type: str
        self.status = status  # type: str
        self.update_date_time = update_date_time  # type: str
        self.repository = repository  # type: str
        self.tag = tag  # type: str
        self.system = system  # type: str
        self.image_id = image_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeImageResponseBodyImageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.update_date_time is not None:
            result['UpdateDateTime'] = self.update_date_time
        if self.repository is not None:
            result['Repository'] = self.repository
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.system is not None:
            result['System'] = self.system
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateDateTime') is not None:
            self.update_date_time = m.get('UpdateDateTime')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('System') is not None:
            self.system = m.get('System')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class DescribeImageResponseBody(TeaModel):
    def __init__(self, request_id=None, image_info=None):
        self.request_id = request_id  # type: str
        self.image_info = image_info  # type: DescribeImageResponseBodyImageInfo

    def validate(self):
        if self.image_info:
            self.image_info.validate()

    def to_map(self):
        _map = super(DescribeImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.image_info is not None:
            result['ImageInfo'] = self.image_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ImageInfo') is not None:
            temp_model = DescribeImageResponseBodyImageInfo()
            self.image_info = temp_model.from_map(m['ImageInfo'])
        return self


class DescribeImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeImageResponse, self).to_map()
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
            temp_model = DescribeImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserPasswordsRequestUser(TeaModel):
    def __init__(self, password=None, name=None):
        self.password = password  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserPasswordsRequestUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Name') is not None:
            self.name = m.get('Name')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyUserPasswordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyUserPasswordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQueueRequest(TeaModel):
    def __init__(self, cluster_id=None, queue_name=None):
        self.cluster_id = cluster_id  # type: str
        self.queue_name = queue_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQueueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        return self


class DeleteQueueResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQueueResponseBody, self).to_map()
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


class DeleteQueueResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteQueueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteQueueResponse, self).to_map()
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
            temp_model = DeleteQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstalledSoftwareRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstalledSoftwareRequest, self).to_map()
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


class ListInstalledSoftwareResponseBodySoftwareListSoftwareList(TeaModel):
    def __init__(self, software_id=None, software_status=None, software_version=None, software_name=None):
        self.software_id = software_id  # type: str
        self.software_status = software_status  # type: str
        self.software_version = software_version  # type: str
        self.software_name = software_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstalledSoftwareResponseBodySoftwareListSoftwareList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.software_id is not None:
            result['SoftwareId'] = self.software_id
        if self.software_status is not None:
            result['SoftwareStatus'] = self.software_status
        if self.software_version is not None:
            result['SoftwareVersion'] = self.software_version
        if self.software_name is not None:
            result['SoftwareName'] = self.software_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SoftwareId') is not None:
            self.software_id = m.get('SoftwareId')
        if m.get('SoftwareStatus') is not None:
            self.software_status = m.get('SoftwareStatus')
        if m.get('SoftwareVersion') is not None:
            self.software_version = m.get('SoftwareVersion')
        if m.get('SoftwareName') is not None:
            self.software_name = m.get('SoftwareName')
        return self


class ListInstalledSoftwareResponseBodySoftwareList(TeaModel):
    def __init__(self, software_list=None):
        self.software_list = software_list  # type: list[ListInstalledSoftwareResponseBodySoftwareListSoftwareList]

    def validate(self):
        if self.software_list:
            for k in self.software_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstalledSoftwareResponseBodySoftwareList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SoftwareList'] = []
        if self.software_list is not None:
            for k in self.software_list:
                result['SoftwareList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.software_list = []
        if m.get('SoftwareList') is not None:
            for k in m.get('SoftwareList'):
                temp_model = ListInstalledSoftwareResponseBodySoftwareListSoftwareList()
                self.software_list.append(temp_model.from_map(k))
        return self


class ListInstalledSoftwareResponseBody(TeaModel):
    def __init__(self, request_id=None, software_list=None):
        self.request_id = request_id  # type: str
        self.software_list = software_list  # type: ListInstalledSoftwareResponseBodySoftwareList

    def validate(self):
        if self.software_list:
            self.software_list.validate()

    def to_map(self):
        _map = super(ListInstalledSoftwareResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.software_list is not None:
            result['SoftwareList'] = self.software_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SoftwareList') is not None:
            temp_model = ListInstalledSoftwareResponseBodySoftwareList()
            self.software_list = temp_model.from_map(m['SoftwareList'])
        return self


class ListInstalledSoftwareResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListInstalledSoftwareResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstalledSoftwareResponse, self).to_map()
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
            temp_model = ListInstalledSoftwareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHealthMonitorLogsRequest(TeaModel):
    def __init__(self, cluster_id=None, start_time=None, end_time=None, enable_reverse=None, filter=None):
        self.cluster_id = cluster_id  # type: str
        self.start_time = start_time  # type: int
        self.end_time = end_time  # type: int
        self.enable_reverse = enable_reverse  # type: bool
        self.filter = filter  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHealthMonitorLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.enable_reverse is not None:
            result['EnableReverse'] = self.enable_reverse
        if self.filter is not None:
            result['Filter'] = self.filter
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EnableReverse') is not None:
            self.enable_reverse = m.get('EnableReverse')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        return self


class GetHealthMonitorLogsResponseBodyLogInfoLogsCheckListCheckList(TeaModel):
    def __init__(self, check_info=None, check_description=None, check_solution=None, check_name=None):
        self.check_info = check_info  # type: str
        self.check_description = check_description  # type: str
        self.check_solution = check_solution  # type: str
        self.check_name = check_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHealthMonitorLogsResponseBodyLogInfoLogsCheckListCheckList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_info is not None:
            result['CheckInfo'] = self.check_info
        if self.check_description is not None:
            result['CheckDescription'] = self.check_description
        if self.check_solution is not None:
            result['CheckSolution'] = self.check_solution
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckInfo') is not None:
            self.check_info = m.get('CheckInfo')
        if m.get('CheckDescription') is not None:
            self.check_description = m.get('CheckDescription')
        if m.get('CheckSolution') is not None:
            self.check_solution = m.get('CheckSolution')
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        return self


class GetHealthMonitorLogsResponseBodyLogInfoLogsCheckList(TeaModel):
    def __init__(self, check_list=None):
        self.check_list = check_list  # type: list[GetHealthMonitorLogsResponseBodyLogInfoLogsCheckListCheckList]

    def validate(self):
        if self.check_list:
            for k in self.check_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHealthMonitorLogsResponseBodyLogInfoLogsCheckList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CheckList'] = []
        if self.check_list is not None:
            for k in self.check_list:
                result['CheckList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.check_list = []
        if m.get('CheckList') is not None:
            for k in m.get('CheckList'):
                temp_model = GetHealthMonitorLogsResponseBodyLogInfoLogsCheckListCheckList()
                self.check_list.append(temp_model.from_map(k))
        return self


class GetHealthMonitorLogsResponseBodyLogInfoLogs(TeaModel):
    def __init__(self, time=None, item_description=None, item_name=None, health_id=None, scene_description=None,
                 host_name=None, scene_name=None, instance_id=None, level=None, check_list=None):
        self.time = time  # type: int
        self.item_description = item_description  # type: str
        self.item_name = item_name  # type: str
        self.health_id = health_id  # type: str
        self.scene_description = scene_description  # type: str
        self.host_name = host_name  # type: str
        self.scene_name = scene_name  # type: str
        self.instance_id = instance_id  # type: str
        self.level = level  # type: str
        self.check_list = check_list  # type: GetHealthMonitorLogsResponseBodyLogInfoLogsCheckList

    def validate(self):
        if self.check_list:
            self.check_list.validate()

    def to_map(self):
        _map = super(GetHealthMonitorLogsResponseBodyLogInfoLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.item_description is not None:
            result['ItemDescription'] = self.item_description
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.health_id is not None:
            result['HealthId'] = self.health_id
        if self.scene_description is not None:
            result['SceneDescription'] = self.scene_description
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.level is not None:
            result['Level'] = self.level
        if self.check_list is not None:
            result['CheckList'] = self.check_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('ItemDescription') is not None:
            self.item_description = m.get('ItemDescription')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('HealthId') is not None:
            self.health_id = m.get('HealthId')
        if m.get('SceneDescription') is not None:
            self.scene_description = m.get('SceneDescription')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('CheckList') is not None:
            temp_model = GetHealthMonitorLogsResponseBodyLogInfoLogsCheckList()
            self.check_list = temp_model.from_map(m['CheckList'])
        return self


class GetHealthMonitorLogsResponseBodyLogInfo(TeaModel):
    def __init__(self, logs=None):
        self.logs = logs  # type: list[GetHealthMonitorLogsResponseBodyLogInfoLogs]

    def validate(self):
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHealthMonitorLogsResponseBodyLogInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = GetHealthMonitorLogsResponseBodyLogInfoLogs()
                self.logs.append(temp_model.from_map(k))
        return self


class GetHealthMonitorLogsResponseBody(TeaModel):
    def __init__(self, request_id=None, log_info=None):
        self.request_id = request_id  # type: str
        self.log_info = log_info  # type: GetHealthMonitorLogsResponseBodyLogInfo

    def validate(self):
        if self.log_info:
            self.log_info.validate()

    def to_map(self):
        _map = super(GetHealthMonitorLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.log_info is not None:
            result['LogInfo'] = self.log_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LogInfo') is not None:
            temp_model = GetHealthMonitorLogsResponseBodyLogInfo()
            self.log_info = temp_model.from_map(m['LogInfo'])
        return self


class GetHealthMonitorLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHealthMonitorLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHealthMonitorLogsResponse, self).to_map()
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
            temp_model = GetHealthMonitorLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeClientRequest(TeaModel):
    def __init__(self, cluster_id=None, client_version=None):
        self.cluster_id = cluster_id  # type: str
        self.client_version = client_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeClientRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpgradeClientResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpgradeClientResponseBody()
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
    def __init__(self, task_id=None, request_id=None):
        self.task_id = task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterResponseBody, self).to_map()
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


class DeleteClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImagesRequest(TeaModel):
    def __init__(self, base_os_tag=None, instance_type=None):
        self.base_os_tag = base_os_tag  # type: str
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BaseOsTag') is not None:
            self.base_os_tag = m.get('BaseOsTag')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class ListImagesResponseBodyOsTagsOsInfo(TeaModel):
    def __init__(self, version=None, base_os_tag=None, platform=None, os_tag=None, image_id=None, architecture=None):
        self.version = version  # type: str
        self.base_os_tag = base_os_tag  # type: str
        self.platform = platform  # type: str
        self.os_tag = os_tag  # type: str
        self.image_id = image_id  # type: str
        self.architecture = architecture  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListImagesResponseBodyOsTagsOsInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.base_os_tag is not None:
            result['BaseOsTag'] = self.base_os_tag
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('BaseOsTag') is not None:
            self.base_os_tag = m.get('BaseOsTag')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
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
    def __init__(self, request_id=None, os_tags=None):
        self.request_id = request_id  # type: str
        self.os_tags = os_tags  # type: ListImagesResponseBodyOsTags

    def validate(self):
        if self.os_tags:
            self.os_tags.validate()

    def to_map(self):
        _map = super(ListImagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.os_tags is not None:
            result['OsTags'] = self.os_tags.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OsTags') is not None:
            temp_model = ListImagesResponseBodyOsTags()
            self.os_tags = temp_model.from_map(m['OsTags'])
        return self


class ListImagesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListImagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGWSClusterPolicyRequest(TeaModel):
    def __init__(self, cluster_id=None, clipboard=None, local_drive=None, usb_redirect=None, watermark=None,
                 udp_port=None, async_mode=None):
        self.cluster_id = cluster_id  # type: str
        self.clipboard = clipboard  # type: str
        self.local_drive = local_drive  # type: str
        self.usb_redirect = usb_redirect  # type: str
        self.watermark = watermark  # type: str
        self.udp_port = udp_port  # type: str
        self.async_mode = async_mode  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetGWSClusterPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.udp_port is not None:
            result['UdpPort'] = self.udp_port
        if self.async_mode is not None:
            result['AsyncMode'] = self.async_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('UdpPort') is not None:
            self.udp_port = m.get('UdpPort')
        if m.get('AsyncMode') is not None:
            self.async_mode = m.get('AsyncMode')
        return self


class SetGWSClusterPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetGWSClusterPolicyResponseBody, self).to_map()
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


class SetGWSClusterPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetGWSClusterPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetGWSClusterPolicyResponse, self).to_map()
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
            temp_model = SetGWSClusterPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueuesRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueuesRequest, self).to_map()
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


class ListQueuesResponseBodyQueuesQueueInfoSpotInstanceTypesInstance(TeaModel):
    def __init__(self, instance_type=None, spot_price_limit=None):
        self.instance_type = instance_type  # type: str
        self.spot_price_limit = spot_price_limit  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueuesResponseBodyQueuesQueueInfoSpotInstanceTypesInstance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')
        return self


class ListQueuesResponseBodyQueuesQueueInfoSpotInstanceTypes(TeaModel):
    def __init__(self, instance=None):
        self.instance = instance  # type: list[ListQueuesResponseBodyQueuesQueueInfoSpotInstanceTypesInstance]

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQueuesResponseBodyQueuesQueueInfoSpotInstanceTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = ListQueuesResponseBodyQueuesQueueInfoSpotInstanceTypesInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class ListQueuesResponseBodyQueuesQueueInfoComputeInstanceType(TeaModel):
    def __init__(self, instance_type=None):
        self.instance_type = instance_type  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQueuesResponseBodyQueuesQueueInfoComputeInstanceType, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class ListQueuesResponseBodyQueuesQueueInfo(TeaModel):
    def __init__(self, type=None, host_name_prefix=None, queue_name=None, enable_auto_grow=None,
                 resource_group_id=None, image_id=None, host_name_suffix=None, spot_strategy=None, spot_instance_types=None,
                 compute_instance_type=None):
        self.type = type  # type: str
        self.host_name_prefix = host_name_prefix  # type: str
        self.queue_name = queue_name  # type: str
        self.enable_auto_grow = enable_auto_grow  # type: bool
        self.resource_group_id = resource_group_id  # type: str
        self.image_id = image_id  # type: str
        self.host_name_suffix = host_name_suffix  # type: str
        self.spot_strategy = spot_strategy  # type: str
        self.spot_instance_types = spot_instance_types  # type: ListQueuesResponseBodyQueuesQueueInfoSpotInstanceTypes
        self.compute_instance_type = compute_instance_type  # type: ListQueuesResponseBodyQueuesQueueInfoComputeInstanceType

    def validate(self):
        if self.spot_instance_types:
            self.spot_instance_types.validate()
        if self.compute_instance_type:
            self.compute_instance_type.validate()

    def to_map(self):
        _map = super(ListQueuesResponseBodyQueuesQueueInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.host_name_prefix is not None:
            result['HostNamePrefix'] = self.host_name_prefix
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.enable_auto_grow is not None:
            result['EnableAutoGrow'] = self.enable_auto_grow
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.host_name_suffix is not None:
            result['HostNameSuffix'] = self.host_name_suffix
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.spot_instance_types is not None:
            result['SpotInstanceTypes'] = self.spot_instance_types.to_map()
        if self.compute_instance_type is not None:
            result['ComputeInstanceType'] = self.compute_instance_type.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('HostNamePrefix') is not None:
            self.host_name_prefix = m.get('HostNamePrefix')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('EnableAutoGrow') is not None:
            self.enable_auto_grow = m.get('EnableAutoGrow')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('HostNameSuffix') is not None:
            self.host_name_suffix = m.get('HostNameSuffix')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('SpotInstanceTypes') is not None:
            temp_model = ListQueuesResponseBodyQueuesQueueInfoSpotInstanceTypes()
            self.spot_instance_types = temp_model.from_map(m['SpotInstanceTypes'])
        if m.get('ComputeInstanceType') is not None:
            temp_model = ListQueuesResponseBodyQueuesQueueInfoComputeInstanceType()
            self.compute_instance_type = temp_model.from_map(m['ComputeInstanceType'])
        return self


class ListQueuesResponseBodyQueues(TeaModel):
    def __init__(self, queue_info=None):
        self.queue_info = queue_info  # type: list[ListQueuesResponseBodyQueuesQueueInfo]

    def validate(self):
        if self.queue_info:
            for k in self.queue_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQueuesResponseBodyQueues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QueueInfo'] = []
        if self.queue_info is not None:
            for k in self.queue_info:
                result['QueueInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.queue_info = []
        if m.get('QueueInfo') is not None:
            for k in m.get('QueueInfo'):
                temp_model = ListQueuesResponseBodyQueuesQueueInfo()
                self.queue_info.append(temp_model.from_map(k))
        return self


class ListQueuesResponseBody(TeaModel):
    def __init__(self, request_id=None, queues=None):
        self.request_id = request_id  # type: str
        self.queues = queues  # type: ListQueuesResponseBodyQueues

    def validate(self):
        if self.queues:
            self.queues.validate()

    def to_map(self):
        _map = super(ListQueuesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.queues is not None:
            result['Queues'] = self.queues.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Queues') is not None:
            temp_model = ListQueuesResponseBodyQueues()
            self.queues = temp_model.from_map(m['Queues'])
        return self


class ListQueuesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListQueuesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListQueuesResponse, self).to_map()
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
            temp_model = ListQueuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobFileRequest(TeaModel):
    def __init__(self, cluster_id=None, runas_user=None, runas_user_password=None, content=None, target_file=None):
        self.cluster_id = cluster_id  # type: str
        self.runas_user = runas_user  # type: str
        self.runas_user_password = runas_user_password  # type: str
        self.content = content  # type: str
        self.target_file = target_file  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user
        if self.runas_user_password is not None:
            result['RunasUserPassword'] = self.runas_user_password
        if self.content is not None:
            result['Content'] = self.content
        if self.target_file is not None:
            result['TargetFile'] = self.target_file
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')
        if m.get('RunasUserPassword') is not None:
            self.runas_user_password = m.get('RunasUserPassword')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('TargetFile') is not None:
            self.target_file = m.get('TargetFile')
        return self


class CreateJobFileResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateJobFileResponseBody, self).to_map()
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


class CreateJobFileResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateJobFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateJobFileResponse, self).to_map()
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
            temp_model = CreateJobFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCloudMetricProfilingsRequest(TeaModel):
    def __init__(self, region_id=None, cluster_id=None, page_number=None, page_size=None):
        self.region_id = region_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCloudMetricProfilingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCloudMetricProfilingsResponseBodyProfilingsProfilingInfo(TeaModel):
    def __init__(self, profiling_id=None, trigger_time=None, pid=None, host_name=None, duration=None,
                 instance_id=None, freq=None):
        self.profiling_id = profiling_id  # type: str
        self.trigger_time = trigger_time  # type: str
        self.pid = pid  # type: int
        self.host_name = host_name  # type: str
        self.duration = duration  # type: int
        self.instance_id = instance_id  # type: str
        self.freq = freq  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCloudMetricProfilingsResponseBodyProfilingsProfilingInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.profiling_id is not None:
            result['ProfilingId'] = self.profiling_id
        if self.trigger_time is not None:
            result['TriggerTime'] = self.trigger_time
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.freq is not None:
            result['Freq'] = self.freq
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProfilingId') is not None:
            self.profiling_id = m.get('ProfilingId')
        if m.get('TriggerTime') is not None:
            self.trigger_time = m.get('TriggerTime')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        return self


class ListCloudMetricProfilingsResponseBodyProfilings(TeaModel):
    def __init__(self, profiling_info=None):
        self.profiling_info = profiling_info  # type: list[ListCloudMetricProfilingsResponseBodyProfilingsProfilingInfo]

    def validate(self):
        if self.profiling_info:
            for k in self.profiling_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCloudMetricProfilingsResponseBodyProfilings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProfilingInfo'] = []
        if self.profiling_info is not None:
            for k in self.profiling_info:
                result['ProfilingInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.profiling_info = []
        if m.get('ProfilingInfo') is not None:
            for k in m.get('ProfilingInfo'):
                temp_model = ListCloudMetricProfilingsResponseBodyProfilingsProfilingInfo()
                self.profiling_info.append(temp_model.from_map(k))
        return self


class ListCloudMetricProfilingsResponseBody(TeaModel):
    def __init__(self, page_size=None, request_id=None, page_number=None, total_count=None, profilings=None):
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.profilings = profilings  # type: ListCloudMetricProfilingsResponseBodyProfilings

    def validate(self):
        if self.profilings:
            self.profilings.validate()

    def to_map(self):
        _map = super(ListCloudMetricProfilingsResponseBody, self).to_map()
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
        if self.profilings is not None:
            result['Profilings'] = self.profilings.to_map()
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
        if m.get('Profilings') is not None:
            temp_model = ListCloudMetricProfilingsResponseBodyProfilings()
            self.profilings = temp_model.from_map(m['Profilings'])
        return self


class ListCloudMetricProfilingsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListCloudMetricProfilingsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCloudMetricProfilingsResponse, self).to_map()
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
            temp_model = ListCloudMetricProfilingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterVolumesRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterVolumesRequest, self).to_map()
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


class GetClusterVolumesResponseBodyVolumesVolumeInfoRolesRoleInfo(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterVolumesResponseBodyVolumesVolumeInfoRolesRoleInfo, self).to_map()
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


class GetClusterVolumesResponseBodyVolumesVolumeInfoRoles(TeaModel):
    def __init__(self, role_info=None):
        self.role_info = role_info  # type: list[GetClusterVolumesResponseBodyVolumesVolumeInfoRolesRoleInfo]

    def validate(self):
        if self.role_info:
            for k in self.role_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetClusterVolumesResponseBodyVolumesVolumeInfoRoles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RoleInfo'] = []
        if self.role_info is not None:
            for k in self.role_info:
                result['RoleInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.role_info = []
        if m.get('RoleInfo') is not None:
            for k in m.get('RoleInfo'):
                temp_model = GetClusterVolumesResponseBodyVolumesVolumeInfoRolesRoleInfo()
                self.role_info.append(temp_model.from_map(k))
        return self


class GetClusterVolumesResponseBodyVolumesVolumeInfo(TeaModel):
    def __init__(self, job_queue=None, volume_id=None, remote_directory=None, volume_mountpoint=None,
                 local_directory=None, volume_type=None, must_keep=None, location=None, volume_protocol=None, roles=None):
        self.job_queue = job_queue  # type: str
        self.volume_id = volume_id  # type: str
        self.remote_directory = remote_directory  # type: str
        self.volume_mountpoint = volume_mountpoint  # type: str
        self.local_directory = local_directory  # type: str
        self.volume_type = volume_type  # type: str
        self.must_keep = must_keep  # type: bool
        self.location = location  # type: str
        self.volume_protocol = volume_protocol  # type: str
        self.roles = roles  # type: GetClusterVolumesResponseBodyVolumesVolumeInfoRoles

    def validate(self):
        if self.roles:
            self.roles.validate()

    def to_map(self):
        _map = super(GetClusterVolumesResponseBodyVolumesVolumeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.volume_id is not None:
            result['VolumeId'] = self.volume_id
        if self.remote_directory is not None:
            result['RemoteDirectory'] = self.remote_directory
        if self.volume_mountpoint is not None:
            result['VolumeMountpoint'] = self.volume_mountpoint
        if self.local_directory is not None:
            result['LocalDirectory'] = self.local_directory
        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type
        if self.must_keep is not None:
            result['MustKeep'] = self.must_keep
        if self.location is not None:
            result['Location'] = self.location
        if self.volume_protocol is not None:
            result['VolumeProtocol'] = self.volume_protocol
        if self.roles is not None:
            result['Roles'] = self.roles.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('VolumeId') is not None:
            self.volume_id = m.get('VolumeId')
        if m.get('RemoteDirectory') is not None:
            self.remote_directory = m.get('RemoteDirectory')
        if m.get('VolumeMountpoint') is not None:
            self.volume_mountpoint = m.get('VolumeMountpoint')
        if m.get('LocalDirectory') is not None:
            self.local_directory = m.get('LocalDirectory')
        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')
        if m.get('MustKeep') is not None:
            self.must_keep = m.get('MustKeep')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('VolumeProtocol') is not None:
            self.volume_protocol = m.get('VolumeProtocol')
        if m.get('Roles') is not None:
            temp_model = GetClusterVolumesResponseBodyVolumesVolumeInfoRoles()
            self.roles = temp_model.from_map(m['Roles'])
        return self


class GetClusterVolumesResponseBodyVolumes(TeaModel):
    def __init__(self, volume_info=None):
        self.volume_info = volume_info  # type: list[GetClusterVolumesResponseBodyVolumesVolumeInfo]

    def validate(self):
        if self.volume_info:
            for k in self.volume_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetClusterVolumesResponseBodyVolumes, self).to_map()
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
                temp_model = GetClusterVolumesResponseBodyVolumesVolumeInfo()
                self.volume_info.append(temp_model.from_map(k))
        return self


class GetClusterVolumesResponseBody(TeaModel):
    def __init__(self, region_id=None, request_id=None, volumes=None):
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.volumes = volumes  # type: GetClusterVolumesResponseBodyVolumes

    def validate(self):
        if self.volumes:
            self.volumes.validate()

    def to_map(self):
        _map = super(GetClusterVolumesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.volumes is not None:
            result['Volumes'] = self.volumes.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Volumes') is not None:
            temp_model = GetClusterVolumesResponseBodyVolumes()
            self.volumes = temp_model.from_map(m['Volumes'])
        return self


class GetClusterVolumesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetClusterVolumesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetClusterVolumesResponse, self).to_map()
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
            temp_model = GetClusterVolumesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGWSInstanceRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGWSInstanceRequest, self).to_map()
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


class DeleteGWSInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGWSInstanceResponseBody, self).to_map()
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


class DeleteGWSInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteGWSInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGWSInstanceResponse, self).to_map()
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
            temp_model = DeleteGWSInstanceResponseBody()
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
    def __init__(self, request_id=None, regions=None):
        self.request_id = request_id  # type: str
        self.regions = regions  # type: ListRegionsResponseBodyRegions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(ListRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = ListRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class ListRegionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeEHPCRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitializeEHPCRequest, self).to_map()
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


class InitializeEHPCResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitializeEHPCResponseBody, self).to_map()
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


class InitializeEHPCResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InitializeEHPCResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitializeEHPCResponse, self).to_map()
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
            temp_model = InitializeEHPCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCloudMetricProfilingRequest(TeaModel):
    def __init__(self, region_id=None, cluster_id=None, host_name=None, process_id=None, duration=None, freq=None):
        self.region_id = region_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.host_name = host_name  # type: str
        self.process_id = process_id  # type: int
        self.duration = duration  # type: int
        self.freq = freq  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunCloudMetricProfilingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.process_id is not None:
            result['ProcessId'] = self.process_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.freq is not None:
            result['Freq'] = self.freq
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        return self


class RunCloudMetricProfilingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunCloudMetricProfilingResponseBody, self).to_map()
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


class RunCloudMetricProfilingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RunCloudMetricProfilingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RunCloudMetricProfilingResponse, self).to_map()
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
            temp_model = RunCloudMetricProfilingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddExistedNodesRequestInstance(TeaModel):
    def __init__(self, id=None):
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddExistedNodesRequestInstance, self).to_map()
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


class AddExistedNodesRequest(TeaModel):
    def __init__(self, cluster_id=None, image_id=None, job_queue=None, client_token=None, image_owner_alias=None,
                 instance=None):
        self.cluster_id = cluster_id  # type: str
        self.image_id = image_id  # type: str
        self.job_queue = job_queue  # type: str
        self.client_token = client_token  # type: str
        self.image_owner_alias = image_owner_alias  # type: str
        self.instance = instance  # type: list[AddExistedNodesRequestInstance]

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddExistedNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = AddExistedNodesRequestInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class AddExistedNodesResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None):
        self.task_id = task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddExistedNodesResponseBody, self).to_map()
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


class AddExistedNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddExistedNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddExistedNodesResponse, self).to_map()
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
            temp_model = AddExistedNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePriceRequestCommodities(TeaModel):
    def __init__(self, amount=None, system_disk_size=None, system_disk_performance_level=None, node_type=None,
                 system_disk_category=None, internet_charge_type=None, network_type=None, instance_type=None, period=None,
                 internet_max_band_width_out=None):
        self.amount = amount  # type: int
        self.system_disk_size = system_disk_size  # type: int
        self.system_disk_performance_level = system_disk_performance_level  # type: str
        self.node_type = node_type  # type: str
        self.system_disk_category = system_disk_category  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.network_type = network_type  # type: str
        self.instance_type = instance_type  # type: str
        self.period = period  # type: int
        self.internet_max_band_width_out = internet_max_band_width_out  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePriceRequestCommodities, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.system_disk_performance_level is not None:
            result['SystemDiskPerformanceLevel'] = self.system_disk_performance_level
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.period is not None:
            result['Period'] = self.period
        if self.internet_max_band_width_out is not None:
            result['InternetMaxBandWidthOut'] = self.internet_max_band_width_out
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('SystemDiskPerformanceLevel') is not None:
            self.system_disk_performance_level = m.get('SystemDiskPerformanceLevel')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('InternetMaxBandWidthOut') is not None:
            self.internet_max_band_width_out = m.get('InternetMaxBandWidthOut')
        return self


class DescribePriceRequest(TeaModel):
    def __init__(self, price_unit=None, charge_type=None, order_type=None, commodities=None):
        self.price_unit = price_unit  # type: str
        self.charge_type = charge_type  # type: str
        self.order_type = order_type  # type: str
        self.commodities = commodities  # type: list[DescribePriceRequestCommodities]

    def validate(self):
        if self.commodities:
            for k in self.commodities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        result['Commodities'] = []
        if self.commodities is not None:
            for k in self.commodities:
                result['Commodities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        self.commodities = []
        if m.get('Commodities') is not None:
            for k in m.get('Commodities'):
                temp_model = DescribePriceRequestCommodities()
                self.commodities.append(temp_model.from_map(k))
        return self


class DescribePriceResponseBodyPricesPriceInfo(TeaModel):
    def __init__(self, original_price=None, node_type=None, currency=None, trade_price=None):
        self.original_price = original_price  # type: float
        self.node_type = node_type  # type: str
        self.currency = currency  # type: str
        self.trade_price = trade_price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePriceResponseBodyPricesPriceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class DescribePriceResponseBodyPrices(TeaModel):
    def __init__(self, price_info=None):
        self.price_info = price_info  # type: list[DescribePriceResponseBodyPricesPriceInfo]

    def validate(self):
        if self.price_info:
            for k in self.price_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePriceResponseBodyPrices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PriceInfo'] = []
        if self.price_info is not None:
            for k in self.price_info:
                result['PriceInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.price_info = []
        if m.get('PriceInfo') is not None:
            for k in m.get('PriceInfo'):
                temp_model = DescribePriceResponseBodyPricesPriceInfo()
                self.price_info.append(temp_model.from_map(k))
        return self


class DescribePriceResponseBody(TeaModel):
    def __init__(self, total_trade_price=None, request_id=None, prices=None):
        self.total_trade_price = total_trade_price  # type: float
        self.request_id = request_id  # type: str
        self.prices = prices  # type: DescribePriceResponseBodyPrices

    def validate(self):
        if self.prices:
            self.prices.validate()

    def to_map(self):
        _map = super(DescribePriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_trade_price is not None:
            result['TotalTradePrice'] = self.total_trade_price
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prices is not None:
            result['Prices'] = self.prices.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalTradePrice') is not None:
            self.total_trade_price = m.get('TotalTradePrice')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Prices') is not None:
            temp_model = DescribePriceResponseBodyPrices()
            self.prices = temp_model.from_map(m['Prices'])
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RerunJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RerunJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGWSClusterPolicyRequest(TeaModel):
    def __init__(self, cluster_id=None, task_id=None, async_mode=None):
        self.cluster_id = cluster_id  # type: str
        self.task_id = task_id  # type: str
        self.async_mode = async_mode  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGWSClusterPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.async_mode is not None:
            result['AsyncMode'] = self.async_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('AsyncMode') is not None:
            self.async_mode = m.get('AsyncMode')
        return self


class DescribeGWSClusterPolicyResponseBody(TeaModel):
    def __init__(self, watermark=None, clipboard=None, request_id=None, usb_redirect=None, local_drive=None):
        self.watermark = watermark  # type: str
        self.clipboard = clipboard  # type: str
        self.request_id = request_id  # type: str
        self.usb_redirect = usb_redirect  # type: str
        self.local_drive = local_drive  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGWSClusterPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        return self


class DescribeGWSClusterPolicyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeGWSClusterPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGWSClusterPolicyResponse, self).to_map()
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
            temp_model = DescribeGWSClusterPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddLocalNodesRequest(TeaModel):
    def __init__(self, cluster_id=None, nodes=None):
        self.cluster_id = cluster_id  # type: str
        self.nodes = nodes  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddLocalNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        return self


class AddLocalNodesResponseBodyInstanceIds(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddLocalNodesResponseBodyInstanceIds, self).to_map()
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


class AddLocalNodesResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_ids=None):
        self.request_id = request_id  # type: str
        self.instance_ids = instance_ids  # type: AddLocalNodesResponseBodyInstanceIds

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super(AddLocalNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceIds') is not None:
            temp_model = AddLocalNodesResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        return self


class AddLocalNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddLocalNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddLocalNodesResponse, self).to_map()
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
            temp_model = AddLocalNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditJobTemplateRequest(TeaModel):
    def __init__(self, template_id=None, command_line=None, name=None, runas_user=None, priority=None,
                 package_path=None, stdout_redirect_path=None, stderr_redirect_path=None, re_runable=None, array_request=None,
                 variables=None, queue=None, clock_time=None, node=None, task=None, thread=None, mem=None, gpu=None):
        self.template_id = template_id  # type: str
        self.command_line = command_line  # type: str
        self.name = name  # type: str
        self.runas_user = runas_user  # type: str
        self.priority = priority  # type: int
        self.package_path = package_path  # type: str
        self.stdout_redirect_path = stdout_redirect_path  # type: str
        self.stderr_redirect_path = stderr_redirect_path  # type: str
        self.re_runable = re_runable  # type: bool
        self.array_request = array_request  # type: str
        self.variables = variables  # type: str
        self.queue = queue  # type: str
        self.clock_time = clock_time  # type: str
        self.node = node  # type: int
        self.task = task  # type: int
        self.thread = thread  # type: int
        self.mem = mem  # type: str
        self.gpu = gpu  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditJobTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.command_line is not None:
            result['CommandLine'] = self.command_line
        if self.name is not None:
            result['Name'] = self.name
        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.package_path is not None:
            result['PackagePath'] = self.package_path
        if self.stdout_redirect_path is not None:
            result['StdoutRedirectPath'] = self.stdout_redirect_path
        if self.stderr_redirect_path is not None:
            result['StderrRedirectPath'] = self.stderr_redirect_path
        if self.re_runable is not None:
            result['ReRunable'] = self.re_runable
        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request
        if self.variables is not None:
            result['Variables'] = self.variables
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.clock_time is not None:
            result['ClockTime'] = self.clock_time
        if self.node is not None:
            result['Node'] = self.node
        if self.task is not None:
            result['Task'] = self.task
        if self.thread is not None:
            result['Thread'] = self.thread
        if self.mem is not None:
            result['Mem'] = self.mem
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('PackagePath') is not None:
            self.package_path = m.get('PackagePath')
        if m.get('StdoutRedirectPath') is not None:
            self.stdout_redirect_path = m.get('StdoutRedirectPath')
        if m.get('StderrRedirectPath') is not None:
            self.stderr_redirect_path = m.get('StderrRedirectPath')
        if m.get('ReRunable') is not None:
            self.re_runable = m.get('ReRunable')
        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('ClockTime') is not None:
            self.clock_time = m.get('ClockTime')
        if m.get('Node') is not None:
            self.node = m.get('Node')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        if m.get('Thread') is not None:
            self.thread = m.get('Thread')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        return self


class EditJobTemplateResponseBody(TeaModel):
    def __init__(self, template_id=None, request_id=None):
        self.template_id = template_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditJobTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EditJobTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EditJobTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EditJobTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVisualServicePasswdRequest(TeaModel):
    def __init__(self, cluster_id=None, runas_user=None, runas_user_password=None, passwd=None):
        self.cluster_id = cluster_id  # type: str
        self.runas_user = runas_user  # type: str
        self.runas_user_password = runas_user_password  # type: str
        self.passwd = passwd  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVisualServicePasswdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user
        if self.runas_user_password is not None:
            result['RunasUserPassword'] = self.runas_user_password
        if self.passwd is not None:
            result['Passwd'] = self.passwd
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')
        if m.get('RunasUserPassword') is not None:
            self.runas_user_password = m.get('RunasUserPassword')
        if m.get('Passwd') is not None:
            self.passwd = m.get('Passwd')
        return self


class ModifyVisualServicePasswdResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVisualServicePasswdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVisualServicePasswdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyVisualServicePasswdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyVisualServicePasswdResponse, self).to_map()
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
            temp_model = ModifyVisualServicePasswdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPreferredEcsTypesRequest(TeaModel):
    def __init__(self, zone_id=None, spot_strategy=None, instance_charge_type=None):
        self.zone_id = zone_id  # type: str
        self.spot_strategy = spot_strategy  # type: str
        self.instance_charge_type = instance_charge_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPreferredEcsTypesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
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


class ListPreferredEcsTypesResponseBodySeriesSeriesInfoRoles(TeaModel):
    def __init__(self, manager=None, compute=None, login=None):
        self.manager = manager  # type: ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesManager
        self.compute = compute  # type: ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesCompute
        self.login = login  # type: ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesLogin

    def validate(self):
        if self.manager:
            self.manager.validate()
        if self.compute:
            self.compute.validate()
        if self.login:
            self.login.validate()

    def to_map(self):
        _map = super(ListPreferredEcsTypesResponseBodySeriesSeriesInfoRoles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.manager is not None:
            result['Manager'] = self.manager.to_map()
        if self.compute is not None:
            result['Compute'] = self.compute.to_map()
        if self.login is not None:
            result['Login'] = self.login.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Manager') is not None:
            temp_model = ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesManager()
            self.manager = temp_model.from_map(m['Manager'])
        if m.get('Compute') is not None:
            temp_model = ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesCompute()
            self.compute = temp_model.from_map(m['Compute'])
        if m.get('Login') is not None:
            temp_model = ListPreferredEcsTypesResponseBodySeriesSeriesInfoRolesLogin()
            self.login = temp_model.from_map(m['Login'])
        return self


class ListPreferredEcsTypesResponseBodySeriesSeriesInfo(TeaModel):
    def __init__(self, series_name=None, series_id=None, roles=None):
        self.series_name = series_name  # type: str
        self.series_id = series_id  # type: str
        self.roles = roles  # type: ListPreferredEcsTypesResponseBodySeriesSeriesInfoRoles

    def validate(self):
        if self.roles:
            self.roles.validate()

    def to_map(self):
        _map = super(ListPreferredEcsTypesResponseBodySeriesSeriesInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.series_name is not None:
            result['SeriesName'] = self.series_name
        if self.series_id is not None:
            result['SeriesId'] = self.series_id
        if self.roles is not None:
            result['Roles'] = self.roles.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SeriesName') is not None:
            self.series_name = m.get('SeriesName')
        if m.get('SeriesId') is not None:
            self.series_id = m.get('SeriesId')
        if m.get('Roles') is not None:
            temp_model = ListPreferredEcsTypesResponseBodySeriesSeriesInfoRoles()
            self.roles = temp_model.from_map(m['Roles'])
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
    def __init__(self, support_spot_instance=None, request_id=None, series=None):
        self.support_spot_instance = support_spot_instance  # type: bool
        self.request_id = request_id  # type: str
        self.series = series  # type: ListPreferredEcsTypesResponseBodySeries

    def validate(self):
        if self.series:
            self.series.validate()

    def to_map(self):
        _map = super(ListPreferredEcsTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.support_spot_instance is not None:
            result['SupportSpotInstance'] = self.support_spot_instance
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.series is not None:
            result['Series'] = self.series.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SupportSpotInstance') is not None:
            self.support_spot_instance = m.get('SupportSpotInstance')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Series') is not None:
            temp_model = ListPreferredEcsTypesResponseBodySeries()
            self.series = temp_model.from_map(m['Series'])
        return self


class ListPreferredEcsTypesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPreferredEcsTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPreferredEcsTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddContainerAppRequest(TeaModel):
    def __init__(self, name=None, repository=None, description=None, image_tag=None, container_type=None):
        self.name = name  # type: str
        self.repository = repository  # type: str
        self.description = description  # type: str
        self.image_tag = image_tag  # type: str
        self.container_type = container_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddContainerAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.repository is not None:
            result['Repository'] = self.repository
        if self.description is not None:
            result['Description'] = self.description
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.container_type is not None:
            result['ContainerType'] = self.container_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Repository') is not None:
            self.repository = m.get('Repository')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('ContainerType') is not None:
            self.container_type = m.get('ContainerType')
        return self


class AddContainerAppResponseBodyContainerId(TeaModel):
    def __init__(self, container_id=None):
        self.container_id = container_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddContainerAppResponseBodyContainerId, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        return self


class AddContainerAppResponseBody(TeaModel):
    def __init__(self, request_id=None, container_id=None):
        self.request_id = request_id  # type: str
        self.container_id = container_id  # type: AddContainerAppResponseBodyContainerId

    def validate(self):
        if self.container_id:
            self.container_id.validate()

    def to_map(self):
        _map = super(AddContainerAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.container_id is not None:
            result['ContainerId'] = self.container_id.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ContainerId') is not None:
            temp_model = AddContainerAppResponseBodyContainerId()
            self.container_id = temp_model.from_map(m['ContainerId'])
        return self


class AddContainerAppResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddContainerAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddContainerAppResponse, self).to_map()
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
            temp_model = AddContainerAppResponseBody()
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
    def __init__(self, operation=None, message=None, create_time=None, level=None):
        self.operation = operation  # type: str
        self.message = message  # type: str
        self.create_time = create_time  # type: str
        self.level = level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterLogsResponseBodyLogsLogInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.message is not None:
            result['Message'] = self.message
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Level') is not None:
            self.level = m.get('Level')
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
    def __init__(self, page_size=None, page_number=None, request_id=None, total_count=None, cluster_id=None,
                 logs=None):
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.cluster_id = cluster_id  # type: str
        self.logs = logs  # type: ListClusterLogsResponseBodyLogs

    def validate(self):
        if self.logs:
            self.logs.validate()

    def to_map(self):
        _map = super(ListClusterLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.logs is not None:
            result['Logs'] = self.logs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Logs') is not None:
            temp_model = ListClusterLogsResponseBodyLogs()
            self.logs = temp_model.from_map(m['Logs'])
        return self


class ListClusterLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListClusterLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListClusterLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoverClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, os_tag=None, account_type=None, scheduler_type=None, image_owner_alias=None,
                 image_id=None, client_version=None):
        self.cluster_id = cluster_id  # type: str
        self.os_tag = os_tag  # type: str
        self.account_type = account_type  # type: str
        self.scheduler_type = scheduler_type  # type: str
        self.image_owner_alias = image_owner_alias  # type: str
        self.image_id = image_id  # type: str
        self.client_version = client_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecoverClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.os_tag is not None:
            result['OsTag'] = self.os_tag
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type
        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')
        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        return self


class RecoverClusterResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None):
        self.task_id = task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecoverClusterResponseBody, self).to_map()
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


class RecoverClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecoverClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecoverClusterResponse, self).to_map()
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
            temp_model = RecoverClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


