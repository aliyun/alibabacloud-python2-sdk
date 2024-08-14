# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class Tag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Tag, self).to_map()
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


class AttachClusterToHubRequest(TeaModel):
    def __init__(self, attach_to_mesh=None, cluster_id=None, cluster_ids=None):
        # The operation that you want to perform. Set the value to **AttachClusterToHub**.
        self.attach_to_mesh = attach_to_mesh  # type: bool
        # The ID of the task.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str
        # The ID of the request.
        # 
        # This parameter is required.
        self.cluster_ids = cluster_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachClusterToHubRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_to_mesh is not None:
            result['AttachToMesh'] = self.attach_to_mesh
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachToMesh') is not None:
            self.attach_to_mesh = m.get('AttachToMesh')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')
        return self


class AttachClusterToHubResponseBody(TeaModel):
    def __init__(self, cluster_id=None, managed_cluster_ids=None, request_id=None, task_id=None):
        # You can call the AttachClusterToHub operation to associate an Container Service for Kubernetes (ACK) cluster with a master instance of ACK One.
        self.cluster_id = cluster_id  # type: str
        # Zhishi
        self.managed_cluster_ids = managed_cluster_ids  # type: list[str]
        # Example 1
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachClusterToHubResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.managed_cluster_ids is not None:
            result['ManagedClusterIds'] = self.managed_cluster_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ManagedClusterIds') is not None:
            self.managed_cluster_ids = m.get('ManagedClusterIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AttachClusterToHubResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachClusterToHubResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachClusterToHubResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachClusterToHubResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(self, new_resource_group_id=None, resource_id=None, resource_type=None):
        # The ID of the new resource group. You can view the available resource groups in the Resource Management console.
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id  # type: str
        # The ID of the resource. The value of this parameter varies with the resource type. For example, if you set ResourceType to cluster, this parameter specifies a cluster ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id  # type: str
        # The resource type. Set the value to cluster.
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupResponseBody, self).to_map()
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


class ChangeResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeResourceGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeResourceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHubClusterRequest(TeaModel):
    def __init__(self, api_server_public_eip=None, argo_server_enabled=None, audit_log_enabled=None,
                 is_enterprise_security_group=None, name=None, price_limit=None, profile=None, region_id=None, resource_group_id=None, tag=None,
                 v_switches=None, vpc_id=None, workflow_schedule_mode=None):
        # Specifies whether to expose the API server to the Internet. Valid values:
        # 
        # *   true: exposes the API server to the Internet.
        # *   false: exposes the API server to the internal network.
        self.api_server_public_eip = api_server_public_eip  # type: bool
        # Specifies whether to enable the workflow instance UI. This parameter takes effect only if Profile is set to XFlow. Valid values:
        # 
        # *   true
        # *   false
        self.argo_server_enabled = argo_server_enabled  # type: bool
        # Specifies whether to enable the audit log feature. Valid values:
        # 
        # *   true: enables the audit log feature.
        # *   false: disables the audit log feature.
        self.audit_log_enabled = audit_log_enabled  # type: bool
        # Specifies whether to use an advanced security group.
        self.is_enterprise_security_group = is_enterprise_security_group  # type: bool
        # The name of the master instance.
        self.name = name  # type: str
        # The limit on the prices of containers in the workflow. This parameter takes effect only if the WorkflowScheduleMode parameter is set to cost-optimized.
        self.price_limit = price_limit  # type: str
        # The type of scenario for which the master instance is suitable. Valid values:
        # 
        # *   `Default`: The master instance is suitable for standard scenarios.
        # *   `XFlow`: The master instance is suitable for workflow scenarios.
        # 
        # Default value: `Default`.
        self.profile = profile  # type: str
        # The ID of the region. You can call the DescribeRegions operation to query available regions.
        # 
        # This parameter is required.
        self.region_id = region_id  # type: str
        # The Resource Group ID.
        self.resource_group_id = resource_group_id  # type: str
        # The tags.
        # 
        # You can specify at most 20 tags in each call.
        self.tag = tag  # type: list[Tag]
        # The ID of the vSwitch.
        # 
        # This parameter is required.
        self.v_switches = v_switches  # type: str
        # The ID of the virtual private cloud (VPC) to which the master instance belongs. You can call the DescribeVpcs operation to query available VPCs.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id  # type: str
        # The scheduling mode of the workflow. This parameter takes effect only if Profile is set to XFlow. Valid values:
        # 
        # *   cost-optimized: cost-prioritized scheduling mode.
        # *   stock-optimized: inventory-prioritized scheduling mode.
        self.workflow_schedule_mode = workflow_schedule_mode  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateHubClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server_public_eip is not None:
            result['ApiServerPublicEip'] = self.api_server_public_eip
        if self.argo_server_enabled is not None:
            result['ArgoServerEnabled'] = self.argo_server_enabled
        if self.audit_log_enabled is not None:
            result['AuditLogEnabled'] = self.audit_log_enabled
        if self.is_enterprise_security_group is not None:
            result['IsEnterpriseSecurityGroup'] = self.is_enterprise_security_group
        if self.name is not None:
            result['Name'] = self.name
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.workflow_schedule_mode is not None:
            result['WorkflowScheduleMode'] = self.workflow_schedule_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = m.get('ApiServerPublicEip')
        if m.get('ArgoServerEnabled') is not None:
            self.argo_server_enabled = m.get('ArgoServerEnabled')
        if m.get('AuditLogEnabled') is not None:
            self.audit_log_enabled = m.get('AuditLogEnabled')
        if m.get('IsEnterpriseSecurityGroup') is not None:
            self.is_enterprise_security_group = m.get('IsEnterpriseSecurityGroup')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = Tag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WorkflowScheduleMode') is not None:
            self.workflow_schedule_mode = m.get('WorkflowScheduleMode')
        return self


class CreateHubClusterShrinkRequest(TeaModel):
    def __init__(self, api_server_public_eip=None, argo_server_enabled=None, audit_log_enabled=None,
                 is_enterprise_security_group=None, name=None, price_limit=None, profile=None, region_id=None, resource_group_id=None,
                 tag_shrink=None, v_switches=None, vpc_id=None, workflow_schedule_mode=None):
        # Specifies whether to expose the API server to the Internet. Valid values:
        # 
        # *   true: exposes the API server to the Internet.
        # *   false: exposes the API server to the internal network.
        self.api_server_public_eip = api_server_public_eip  # type: bool
        # Specifies whether to enable the workflow instance UI. This parameter takes effect only if Profile is set to XFlow. Valid values:
        # 
        # *   true
        # *   false
        self.argo_server_enabled = argo_server_enabled  # type: bool
        # Specifies whether to enable the audit log feature. Valid values:
        # 
        # *   true: enables the audit log feature.
        # *   false: disables the audit log feature.
        self.audit_log_enabled = audit_log_enabled  # type: bool
        # Specifies whether to use an advanced security group.
        self.is_enterprise_security_group = is_enterprise_security_group  # type: bool
        # The name of the master instance.
        self.name = name  # type: str
        # The limit on the prices of containers in the workflow. This parameter takes effect only if the WorkflowScheduleMode parameter is set to cost-optimized.
        self.price_limit = price_limit  # type: str
        # The type of scenario for which the master instance is suitable. Valid values:
        # 
        # *   `Default`: The master instance is suitable for standard scenarios.
        # *   `XFlow`: The master instance is suitable for workflow scenarios.
        # 
        # Default value: `Default`.
        self.profile = profile  # type: str
        # The ID of the region. You can call the DescribeRegions operation to query available regions.
        # 
        # This parameter is required.
        self.region_id = region_id  # type: str
        # The Resource Group ID.
        self.resource_group_id = resource_group_id  # type: str
        # The tags.
        # 
        # You can specify at most 20 tags in each call.
        self.tag_shrink = tag_shrink  # type: str
        # The ID of the vSwitch.
        # 
        # This parameter is required.
        self.v_switches = v_switches  # type: str
        # The ID of the virtual private cloud (VPC) to which the master instance belongs. You can call the DescribeVpcs operation to query available VPCs.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id  # type: str
        # The scheduling mode of the workflow. This parameter takes effect only if Profile is set to XFlow. Valid values:
        # 
        # *   cost-optimized: cost-prioritized scheduling mode.
        # *   stock-optimized: inventory-prioritized scheduling mode.
        self.workflow_schedule_mode = workflow_schedule_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHubClusterShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server_public_eip is not None:
            result['ApiServerPublicEip'] = self.api_server_public_eip
        if self.argo_server_enabled is not None:
            result['ArgoServerEnabled'] = self.argo_server_enabled
        if self.audit_log_enabled is not None:
            result['AuditLogEnabled'] = self.audit_log_enabled
        if self.is_enterprise_security_group is not None:
            result['IsEnterpriseSecurityGroup'] = self.is_enterprise_security_group
        if self.name is not None:
            result['Name'] = self.name
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id
        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.workflow_schedule_mode is not None:
            result['WorkflowScheduleMode'] = self.workflow_schedule_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = m.get('ApiServerPublicEip')
        if m.get('ArgoServerEnabled') is not None:
            self.argo_server_enabled = m.get('ArgoServerEnabled')
        if m.get('AuditLogEnabled') is not None:
            self.audit_log_enabled = m.get('AuditLogEnabled')
        if m.get('IsEnterpriseSecurityGroup') is not None:
            self.is_enterprise_security_group = m.get('IsEnterpriseSecurityGroup')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')
        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WorkflowScheduleMode') is not None:
            self.workflow_schedule_mode = m.get('WorkflowScheduleMode')
        return self


class CreateHubClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None, task_id=None):
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the task.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHubClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateHubClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateHubClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateHubClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateHubClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHubClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, force=None, retain_resources=None):
        # The ID of the master instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str
        # Specifies whether to forcefully delete the master instance in ACK One. Valid values:
        # 
        # *   true: forcefully deletes the master instance in ACK One.
        # *   false: does not forcibly delete the master instance in ACK One.
        # 
        # Default value: false.
        self.force = force  # type: bool
        # The list of resources to retain.
        self.retain_resources = retain_resources  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHubClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.force is not None:
            result['Force'] = self.force
        if self.retain_resources is not None:
            result['RetainResources'] = self.retain_resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('RetainResources') is not None:
            self.retain_resources = m.get('RetainResources')
        return self


class DeleteHubClusterShrinkRequest(TeaModel):
    def __init__(self, cluster_id=None, force=None, retain_resources_shrink=None):
        # The ID of the master instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str
        # Specifies whether to forcefully delete the master instance in ACK One. Valid values:
        # 
        # *   true: forcefully deletes the master instance in ACK One.
        # *   false: does not forcibly delete the master instance in ACK One.
        # 
        # Default value: false.
        self.force = force  # type: bool
        # The list of resources to retain.
        self.retain_resources_shrink = retain_resources_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHubClusterShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.force is not None:
            result['Force'] = self.force
        if self.retain_resources_shrink is not None:
            result['RetainResources'] = self.retain_resources_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('RetainResources') is not None:
            self.retain_resources_shrink = m.get('RetainResources')
        return self


class DeleteHubClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None, task_id=None):
        # The ID of the cluster.
        self.cluster_id = cluster_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the job.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHubClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteHubClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteHubClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteHubClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteHubClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyInstanceRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_ids=None, policy_name=None):
        # The ID of the master instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str
        # A array of JSON strings. The JSON strings in the array indicate the IDs of the associated clusters for which the policy is deleted.
        self.cluster_ids = cluster_ids  # type: list[str]
        # The name of the policy.
        # 
        # This parameter is required.
        self.policy_name = policy_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class DeletePolicyInstanceShrinkRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_ids_shrink=None, policy_name=None):
        # The ID of the master instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str
        # A array of JSON strings. The JSON strings in the array indicate the IDs of the associated clusters for which the policy is deleted.
        self.cluster_ids_shrink = cluster_ids_shrink  # type: str
        # The name of the policy.
        # 
        # This parameter is required.
        self.policy_name = policy_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyInstanceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_ids_shrink is not None:
            result['ClusterIds'] = self.cluster_ids_shrink
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterIds') is not None:
            self.cluster_ids_shrink = m.get('ClusterIds')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class DeletePolicyInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePolicyInstanceResponseBody, self).to_map()
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


class DeletePolicyInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePolicyInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePolicyInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePolicyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserPermissionRequest(TeaModel):
    def __init__(self, cluster_id=None, user_id=None):
        # The ID of the master instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str
        # The ID of the RAM user.
        # 
        # This parameter is required.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserPermissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteUserPermissionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserPermissionResponseBody, self).to_map()
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


class DeleteUserPermissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteUserPermissionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserPermissionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUserPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployPolicyInstanceRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_ids=None, namespaces=None, policy_action=None, policy_name=None):
        # The ID of the master instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str
        # An array of JSON strings. The JSON strings in the array indicate the IDs of the associated clusters in which the policy instance is deployed.
        # 
        # This parameter is required.
        self.cluster_ids = cluster_ids  # type: list[str]
        # A list of namespaces.
        self.namespaces = namespaces  # type: list[str]
        # The action of the policy. Valid values:
        # 
        # *   deny: blocks deployments that match the policy.
        # *   warn: generates alerts for deployments that match the policy.
        # 
        # This parameter is required.
        self.policy_action = policy_action  # type: str
        # The name of the policy.
        # 
        # This parameter is required.
        self.policy_name = policy_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployPolicyInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids
        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')
        if m.get('Namespaces') is not None:
            self.namespaces = m.get('Namespaces')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class DeployPolicyInstanceShrinkRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_ids_shrink=None, namespaces_shrink=None, policy_action=None,
                 policy_name=None):
        # The ID of the master instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str
        # An array of JSON strings. The JSON strings in the array indicate the IDs of the associated clusters in which the policy instance is deployed.
        # 
        # This parameter is required.
        self.cluster_ids_shrink = cluster_ids_shrink  # type: str
        # A list of namespaces.
        self.namespaces_shrink = namespaces_shrink  # type: str
        # The action of the policy. Valid values:
        # 
        # *   deny: blocks deployments that match the policy.
        # *   warn: generates alerts for deployments that match the policy.
        # 
        # This parameter is required.
        self.policy_action = policy_action  # type: str
        # The name of the policy.
        # 
        # This parameter is required.
        self.policy_name = policy_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployPolicyInstanceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_ids_shrink is not None:
            result['ClusterIds'] = self.cluster_ids_shrink
        if self.namespaces_shrink is not None:
            result['Namespaces'] = self.namespaces_shrink
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterIds') is not None:
            self.cluster_ids_shrink = m.get('ClusterIds')
        if m.get('Namespaces') is not None:
            self.namespaces_shrink = m.get('Namespaces')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class DeployPolicyInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployPolicyInstanceResponseBody, self).to_map()
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


class DeployPolicyInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeployPolicyInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeployPolicyInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeployPolicyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHubClusterDetailsRequest(TeaModel):
    def __init__(self, cluster_id=None):
        # The ID of the master instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsRequest, self).to_map()
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


class DescribeHubClusterDetailsResponseBodyClusterApiServer(TeaModel):
    def __init__(self, api_server_eip_id=None, enabled_public=None, load_balancer_id=None):
        # The ID of the elastic IP address (EIP).
        self.api_server_eip_id = api_server_eip_id  # type: str
        # Indicates whether the API server is accessible over the Internet. Valid values:
        # 
        # *   true: The API server is accessible over the Internet.
        # *   false: The API server is inaccessible over the Internet.
        self.enabled_public = enabled_public  # type: bool
        # The ID of the Server Load Balancer (SLB) instance.
        self.load_balancer_id = load_balancer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterApiServer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server_eip_id is not None:
            result['ApiServerEipId'] = self.api_server_eip_id
        if self.enabled_public is not None:
            result['EnabledPublic'] = self.enabled_public
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiServerEipId') is not None:
            self.api_server_eip_id = m.get('ApiServerEipId')
        if m.get('EnabledPublic') is not None:
            self.enabled_public = m.get('EnabledPublic')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaDataACKOneGitOps(TeaModel):
    def __init__(self, access_control_list=None, enabled=None, haenabled=None, public_access_enabled=None):
        # The Internet access control list (ACL). This parameter takes effect only if PublicAccessEnabled is set to true.
        self.access_control_list = access_control_list  # type: list[str]
        # Indicates whether GitOps is enabled. Valid values:
        # 
        # *   true: GitOps is enabled.
        # *   false: GitOps is disabled.
        self.enabled = enabled  # type: bool
        # Indicates whether GitOps High Availability is enabled. Valid values:
        # 
        # *   true:  GitOps High Availability is enabled.
        # *   false:  GitOps High Availability is disabled.
        self.haenabled = haenabled  # type: bool
        # Specifies whether to enable public domain name resolution in the Argo CD or Argo Workflow console. Valid values:
        # 
        # *   true
        # *   false
        self.public_access_enabled = public_access_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaDataACKOneGitOps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_list is not None:
            result['AccessControlList'] = self.access_control_list
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.haenabled is not None:
            result['HAEnabled'] = self.haenabled
        if self.public_access_enabled is not None:
            result['PublicAccessEnabled'] = self.public_access_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessControlList') is not None:
            self.access_control_list = m.get('AccessControlList')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('HAEnabled') is not None:
            self.haenabled = m.get('HAEnabled')
        if m.get('PublicAccessEnabled') is not None:
            self.public_access_enabled = m.get('PublicAccessEnabled')
        return self


class DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaDataACKOneWorkFlowArgoWorkflow(TeaModel):
    def __init__(self, access_control_list=None, enabled=None, public_access_enabled=None, server_enabled=None):
        # The Internet access control list (ACL). This parameter takes effect only if PublicAccessEnabled is set to true.
        self.access_control_list = access_control_list  # type: list[str]
        # Specifies whether to enable the argo workflow. Valid values:
        # 
        # *   **false** (default)
        # *   **true**\
        self.enabled = enabled  # type: bool
        # Specifies whether to enable public domain name resolution in the Argo CD or Argo Workflow console. Valid values:
        # 
        # *   true
        # *   false
        self.public_access_enabled = public_access_enabled  # type: bool
        # Specifies whether to enable the argo workflow. UI Valid values:
        # 
        # *   **false** (default)
        # *   **true**\
        self.server_enabled = server_enabled  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaDataACKOneWorkFlowArgoWorkflow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_list is not None:
            result['AccessControlList'] = self.access_control_list
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.public_access_enabled is not None:
            result['PublicAccessEnabled'] = self.public_access_enabled
        if self.server_enabled is not None:
            result['ServerEnabled'] = self.server_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessControlList') is not None:
            self.access_control_list = m.get('AccessControlList')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('PublicAccessEnabled') is not None:
            self.public_access_enabled = m.get('PublicAccessEnabled')
        if m.get('ServerEnabled') is not None:
            self.server_enabled = m.get('ServerEnabled')
        return self


class DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaDataACKOneWorkFlow(TeaModel):
    def __init__(self, argo_workflow=None):
        # The Argo workflow metadata.
        self.argo_workflow = argo_workflow  # type: DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaDataACKOneWorkFlowArgoWorkflow

    def validate(self):
        if self.argo_workflow:
            self.argo_workflow.validate()

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaDataACKOneWorkFlow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.argo_workflow is not None:
            result['ArgoWorkflow'] = self.argo_workflow.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArgoWorkflow') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaDataACKOneWorkFlowArgoWorkflow()
            self.argo_workflow = temp_model.from_map(m['ArgoWorkflow'])
        return self


class DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaDataACKOne(TeaModel):
    def __init__(self, git_ops=None, work_flow=None):
        # The GitOps metadata.
        self.git_ops = git_ops  # type: DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaDataACKOneGitOps
        # The workflow metadata.
        self.work_flow = work_flow  # type: DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaDataACKOneWorkFlow

    def validate(self):
        if self.git_ops:
            self.git_ops.validate()
        if self.work_flow:
            self.work_flow.validate()

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaDataACKOne, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.git_ops is not None:
            result['GitOps'] = self.git_ops.to_map()
        if self.work_flow is not None:
            result['WorkFlow'] = self.work_flow.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GitOps') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaDataACKOneGitOps()
            self.git_ops = temp_model.from_map(m['GitOps'])
        if m.get('WorkFlow') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaDataACKOneWorkFlow()
            self.work_flow = temp_model.from_map(m['WorkFlow'])
        return self


class DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaData(TeaModel):
    def __init__(self, ackone=None):
        # The cluster metadata.
        self.ackone = ackone  # type: DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaDataACKOne

    def validate(self):
        if self.ackone:
            self.ackone.validate()

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ackone is not None:
            result['ACKOne'] = self.ackone.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ACKOne') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaDataACKOne()
            self.ackone = temp_model.from_map(m['ACKOne'])
        return self


class DescribeHubClusterDetailsResponseBodyClusterClusterInfoTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterClusterInfoTags, self).to_map()
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


class DescribeHubClusterDetailsResponseBodyClusterClusterInfo(TeaModel):
    def __init__(self, cluster_id=None, cluster_spec=None, creation_time=None, error_message=None, meta_data=None,
                 name=None, profile=None, region_id=None, resource_group_id=None, state=None, tags=None, update_time=None,
                 version=None):
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str
        # The specification of the master instance. Valid value:
        # 
        # *   ack.pro.small: ACK Pro cluster
        self.cluster_spec = cluster_spec  # type: str
        # The time when the master instance was created.
        self.creation_time = creation_time  # type: str
        # The error message returned when the master instance failed to be created.
        self.error_message = error_message  # type: str
        # The cluster metadata.
        self.meta_data = meta_data  # type: DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaData
        # The name of the master instance.
        self.name = name  # type: str
        # The configurations of the master instance.
        self.profile = profile  # type: str
        # The ID of the region in which the master instance resides.
        self.region_id = region_id  # type: str
        # The ID of Resource Group.
        self.resource_group_id = resource_group_id  # type: str
        # The status of the master instance. Valid values:
        # 
        # *   initial: The master instance is being initialized.
        # *   failed: The master instance failed to be created.
        # *   running: The master instance is running
        # *   inactive: The master instance is pending.
        # *   deleting: The master instance is being deleted.
        # *   delete_failed: The master instance failed to be deleted.
        # *   deleted: The master instance is deleted.
        self.state = state  # type: str
        self.tags = tags  # type: list[DescribeHubClusterDetailsResponseBodyClusterClusterInfoTags]
        # The time when the master instance was updated.
        self.update_time = update_time  # type: str
        # The version of the master instance.
        self.version = version  # type: str

    def validate(self):
        if self.meta_data:
            self.meta_data.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterClusterInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.meta_data is not None:
            result['MetaData'] = self.meta_data.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('MetaData') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterClusterInfoMetaData()
            self.meta_data = temp_model.from_map(m['MetaData'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeHubClusterDetailsResponseBodyClusterClusterInfoTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeHubClusterDetailsResponseBodyClusterConditions(TeaModel):
    def __init__(self, message=None, reason=None, status=None, type=None):
        # The error message returned.
        self.message = message  # type: str
        # The reason for the deletion condition.
        self.reason = reason  # type: str
        # The status of the master instance that the deletion condition indicates. Valid values:
        # 
        # *   True: The master instance cannot be deleted.
        # *   False: The master instance can be deleted.
        # *   Unknow: Whether the master instance can be deleted is unknown.
        self.status = status  # type: str
        # The type of deletion condition.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeHubClusterDetailsResponseBodyClusterEndpoints(TeaModel):
    def __init__(self, intranet_api_server_endpoint=None, public_api_server_endpoint=None):
        # The endpoint that is used to access the API server over the internal network.
        self.intranet_api_server_endpoint = intranet_api_server_endpoint  # type: str
        # The endpoint that is used to access the API server over the Internet.
        self.public_api_server_endpoint = public_api_server_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intranet_api_server_endpoint is not None:
            result['IntranetApiServerEndpoint'] = self.intranet_api_server_endpoint
        if self.public_api_server_endpoint is not None:
            result['PublicApiServerEndpoint'] = self.public_api_server_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntranetApiServerEndpoint') is not None:
            self.intranet_api_server_endpoint = m.get('IntranetApiServerEndpoint')
        if m.get('PublicApiServerEndpoint') is not None:
            self.public_api_server_endpoint = m.get('PublicApiServerEndpoint')
        return self


class DescribeHubClusterDetailsResponseBodyClusterLogConfig(TeaModel):
    def __init__(self, enable_log=None, log_project=None, log_store_ttl=None):
        # Indicates whether the audit logging feature is enabled. Valid values:
        # 
        # *   true: Audit logging is enabled.
        # *   false: Audit logging is disabled.
        self.enable_log = enable_log  # type: bool
        # The name of the project of Log Service.
        self.log_project = log_project  # type: str
        # The number of days that logs are retained by Log Service.
        self.log_store_ttl = log_store_ttl  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterLogConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_log is not None:
            result['EnableLog'] = self.enable_log
        if self.log_project is not None:
            result['LogProject'] = self.log_project
        if self.log_store_ttl is not None:
            result['LogStoreTTL'] = self.log_store_ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableLog') is not None:
            self.enable_log = m.get('EnableLog')
        if m.get('LogProject') is not None:
            self.log_project = m.get('LogProject')
        if m.get('LogStoreTTL') is not None:
            self.log_store_ttl = m.get('LogStoreTTL')
        return self


class DescribeHubClusterDetailsResponseBodyClusterMeshConfig(TeaModel):
    def __init__(self, enable_mesh=None, mesh_id=None):
        # Indicates whether ASM is enabled. Valid values:
        # 
        # *   true: ASM is enabled.
        # *   false: ASM is disabled.
        self.enable_mesh = enable_mesh  # type: bool
        # service mesh (ASM) instance ID
        self.mesh_id = mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterMeshConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_mesh is not None:
            result['EnableMesh'] = self.enable_mesh
        if self.mesh_id is not None:
            result['MeshId'] = self.mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableMesh') is not None:
            self.enable_mesh = m.get('EnableMesh')
        if m.get('MeshId') is not None:
            self.mesh_id = m.get('MeshId')
        return self


class DescribeHubClusterDetailsResponseBodyClusterNetwork(TeaModel):
    def __init__(self, cluster_domain=None, ipstack=None, security_group_ids=None, v_switches=None, vpc_id=None):
        # The domain name of the master instance.
        self.cluster_domain = cluster_domain  # type: str
        # The IP version that is supported by the master instance. Valid values:
        # 
        # *   ipv4: IPv4.
        # *   ipv6: IPv6.
        # *   dual: IPv4 and IPv6.
        self.ipstack = ipstack  # type: str
        # The IDs of the associated security groups.
        self.security_group_ids = security_group_ids  # type: list[str]
        # The details of the vSwitches.
        self.v_switches = v_switches  # type: list[str]
        # The ID of the virtual private cloud (VPC) in which the master instance resides.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterNetwork, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.ipstack is not None:
            result['IPStack'] = self.ipstack
        if self.security_group_ids is not None:
            result['SecurityGroupIDs'] = self.security_group_ids
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('IPStack') is not None:
            self.ipstack = m.get('IPStack')
        if m.get('SecurityGroupIDs') is not None:
            self.security_group_ids = m.get('SecurityGroupIDs')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeHubClusterDetailsResponseBodyClusterWorkflowConfigWorkflowUnitsVSwitches(TeaModel):
    def __init__(self, vswitch_id=None, zone_id=None):
        # The ID of the vSwitch.
        self.vswitch_id = vswitch_id  # type: str
        # The zone ID of the cluster.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent zone list.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterWorkflowConfigWorkflowUnitsVSwitches, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeHubClusterDetailsResponseBodyClusterWorkflowConfigWorkflowUnits(TeaModel):
    def __init__(self, region_id=None, v_switches=None, vpc_id=None):
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The vSwitches.
        self.v_switches = v_switches  # type: list[DescribeHubClusterDetailsResponseBodyClusterWorkflowConfigWorkflowUnitsVSwitches]
        # The ID of the VPC.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.v_switches:
            for k in self.v_switches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterWorkflowConfigWorkflowUnits, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['VSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['VSwitches'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k in m.get('VSwitches'):
                temp_model = DescribeHubClusterDetailsResponseBodyClusterWorkflowConfigWorkflowUnitsVSwitches()
                self.v_switches.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeHubClusterDetailsResponseBodyClusterWorkflowConfig(TeaModel):
    def __init__(self, argo_server_enabled=None, price_limit=None, workflow_schedule_mode=None,
                 workflow_units=None):
        # Specifies whether to enable the workflow instance UI. This parameter takes effect only if Profile is set to XFlow. Valid values:
        # 
        # *   true
        # *   false
        self.argo_server_enabled = argo_server_enabled  # type: bool
        # The limit on the prices of containers in the workflow. This parameter takes effect only if the WorkflowScheduleMode parameter is set to cost-optimized.
        self.price_limit = price_limit  # type: str
        # The scheduling mode of the workflow. This parameter takes effect only if Profile is set to XFlow. Valid values:
        # 
        # *   cost-optimized: cost-prioritized scheduling mode.
        # *   stock-optimized: inventory-prioritized scheduling mode.
        self.workflow_schedule_mode = workflow_schedule_mode  # type: str
        # The Argo workflow regions  configuration.
        self.workflow_units = workflow_units  # type: list[DescribeHubClusterDetailsResponseBodyClusterWorkflowConfigWorkflowUnits]

    def validate(self):
        if self.workflow_units:
            for k in self.workflow_units:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterWorkflowConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.argo_server_enabled is not None:
            result['ArgoServerEnabled'] = self.argo_server_enabled
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        if self.workflow_schedule_mode is not None:
            result['WorkflowScheduleMode'] = self.workflow_schedule_mode
        result['WorkflowUnits'] = []
        if self.workflow_units is not None:
            for k in self.workflow_units:
                result['WorkflowUnits'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArgoServerEnabled') is not None:
            self.argo_server_enabled = m.get('ArgoServerEnabled')
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        if m.get('WorkflowScheduleMode') is not None:
            self.workflow_schedule_mode = m.get('WorkflowScheduleMode')
        self.workflow_units = []
        if m.get('WorkflowUnits') is not None:
            for k in m.get('WorkflowUnits'):
                temp_model = DescribeHubClusterDetailsResponseBodyClusterWorkflowConfigWorkflowUnits()
                self.workflow_units.append(temp_model.from_map(k))
        return self


class DescribeHubClusterDetailsResponseBodyCluster(TeaModel):
    def __init__(self, api_server=None, cluster_info=None, conditions=None, endpoints=None, log_config=None,
                 mesh_config=None, network=None, workflow_config=None):
        # The details of the API server of the master instance.
        self.api_server = api_server  # type: DescribeHubClusterDetailsResponseBodyClusterApiServer
        # The details of the master instance.
        self.cluster_info = cluster_info  # type: DescribeHubClusterDetailsResponseBodyClusterClusterInfo
        # The deletion conditions of the master instance.
        self.conditions = conditions  # type: list[DescribeHubClusterDetailsResponseBodyClusterConditions]
        # The endpoint of the master instance.
        self.endpoints = endpoints  # type: DescribeHubClusterDetailsResponseBodyClusterEndpoints
        # The logging configuration.
        self.log_config = log_config  # type: DescribeHubClusterDetailsResponseBodyClusterLogConfig
        # The configurations of Alibaba Cloud Service Mesh (ASM).
        self.mesh_config = mesh_config  # type: DescribeHubClusterDetailsResponseBodyClusterMeshConfig
        # The network configurations of the master instance.
        self.network = network  # type: DescribeHubClusterDetailsResponseBodyClusterNetwork
        # The Argo workflow configuration.
        self.workflow_config = workflow_config  # type: DescribeHubClusterDetailsResponseBodyClusterWorkflowConfig

    def validate(self):
        if self.api_server:
            self.api_server.validate()
        if self.cluster_info:
            self.cluster_info.validate()
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()
        if self.endpoints:
            self.endpoints.validate()
        if self.log_config:
            self.log_config.validate()
        if self.mesh_config:
            self.mesh_config.validate()
        if self.network:
            self.network.validate()
        if self.workflow_config:
            self.workflow_config.validate()

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server is not None:
            result['ApiServer'] = self.api_server.to_map()
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info.to_map()
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        if self.log_config is not None:
            result['LogConfig'] = self.log_config.to_map()
        if self.mesh_config is not None:
            result['MeshConfig'] = self.mesh_config.to_map()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.workflow_config is not None:
            result['WorkflowConfig'] = self.workflow_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiServer') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterApiServer()
            self.api_server = temp_model.from_map(m['ApiServer'])
        if m.get('ClusterInfo') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterClusterInfo()
            self.cluster_info = temp_model.from_map(m['ClusterInfo'])
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = DescribeHubClusterDetailsResponseBodyClusterConditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('Endpoints') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('LogConfig') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterLogConfig()
            self.log_config = temp_model.from_map(m['LogConfig'])
        if m.get('MeshConfig') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterMeshConfig()
            self.mesh_config = temp_model.from_map(m['MeshConfig'])
        if m.get('Network') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('WorkflowConfig') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterWorkflowConfig()
            self.workflow_config = temp_model.from_map(m['WorkflowConfig'])
        return self


class DescribeHubClusterDetailsResponseBody(TeaModel):
    def __init__(self, cluster=None, request_id=None):
        # The details of the master instance.
        self.cluster = cluster  # type: DescribeHubClusterDetailsResponseBodyCluster
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cluster:
            self.cluster.validate()

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['Cluster'] = self.cluster.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cluster') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyCluster()
            self.cluster = temp_model.from_map(m['Cluster'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHubClusterDetailsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHubClusterDetailsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHubClusterDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHubClusterKubeconfigRequest(TeaModel):
    def __init__(self, cluster_id=None, private_ip_address=None):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str
        # Specifies whether to obtain the kubeconfig file that is used to connect to the cluster over the internal network. Valid values:
        # 
        # *   `true`: obtains the kubeconfig file that is used to connect to the master instance over the internal network.
        # *   `false`: obtains the kubeconfig file that is used to connect to the master instance over the Internet.
        # 
        # Default value: `false`
        self.private_ip_address = private_ip_address  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterKubeconfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class DescribeHubClusterKubeconfigResponseBody(TeaModel):
    def __init__(self, kubeconfig=None, request_id=None):
        # The content of the kubeconfig file.
        self.kubeconfig = kubeconfig  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterKubeconfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kubeconfig is not None:
            result['Kubeconfig'] = self.kubeconfig
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Kubeconfig') is not None:
            self.kubeconfig = m.get('Kubeconfig')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHubClusterKubeconfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHubClusterKubeconfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHubClusterKubeconfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHubClusterKubeconfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHubClusterLogsRequest(TeaModel):
    def __init__(self, cluster_id=None):
        # The ID of the Fleet instance. You can call the [DescribeHubClusters](https://help.aliyun.com/document_detail/424404.html) operation to query the created Fleet instances.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterLogsRequest, self).to_map()
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


class DescribeHubClusterLogsResponseBodyLogs(TeaModel):
    def __init__(self, cluster_id=None, cluster_log=None, creation_time=None, log_level=None):
        # The ID of the Fleet instance.
        self.cluster_id = cluster_id  # type: str
        # The log of the Fleet instance.
        self.cluster_log = cluster_log  # type: str
        # The time when the log was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time  # type: str
        # The log level. Valid values:
        # 
        # *   error
        # *   warn
        # *   info
        self.log_level = log_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterLogsResponseBodyLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_log is not None:
            result['ClusterLog'] = self.cluster_log
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterLog') is not None:
            self.cluster_log = m.get('ClusterLog')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        return self


class DescribeHubClusterLogsResponseBody(TeaModel):
    def __init__(self, logs=None, request_id=None):
        # The details of operations logs.
        self.logs = logs  # type: list[DescribeHubClusterLogsResponseBodyLogs]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHubClusterLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = DescribeHubClusterLogsResponseBodyLogs()
                self.logs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHubClusterLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHubClusterLogsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHubClusterLogsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHubClusterLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHubClustersRequest(TeaModel):
    def __init__(self, profile=None, resource_group_id=None, tag=None):
        # The configurations of the cluster.
        self.profile = profile  # type: str
        # The resource group ID.
        self.resource_group_id = resource_group_id  # type: str
        # The tags.
        self.tag = tag  # type: list[Tag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHubClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = Tag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeHubClustersShrinkRequest(TeaModel):
    def __init__(self, profile=None, resource_group_id=None, tag_shrink=None):
        # The configurations of the cluster.
        self.profile = profile  # type: str
        # The resource group ID.
        self.resource_group_id = resource_group_id  # type: str
        # The tags.
        self.tag_shrink = tag_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClustersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')
        return self


class DescribeHubClustersResponseBodyClustersApiServer(TeaModel):
    def __init__(self, api_server_eip_id=None, enabled_public=None, load_balancer_id=None):
        # The elastic IP address (EIP) ID.
        self.api_server_eip_id = api_server_eip_id  # type: str
        # Indicates whether the public endpoint is enabled for the API server. Valid values:
        # 
        # *   true
        # *   false
        self.enabled_public = enabled_public  # type: bool
        # The ID of the Server Load Balancer (SLB) instance that is associated with the cluster.
        self.load_balancer_id = load_balancer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClustersApiServer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server_eip_id is not None:
            result['ApiServerEipId'] = self.api_server_eip_id
        if self.enabled_public is not None:
            result['EnabledPublic'] = self.enabled_public
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiServerEipId') is not None:
            self.api_server_eip_id = m.get('ApiServerEipId')
        if m.get('EnabledPublic') is not None:
            self.enabled_public = m.get('EnabledPublic')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class DescribeHubClustersResponseBodyClustersClusterInfoTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClustersClusterInfoTags, self).to_map()
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


class DescribeHubClustersResponseBodyClustersClusterInfo(TeaModel):
    def __init__(self, cluster_id=None, cluster_spec=None, creation_time=None, error_message=None, name=None,
                 profile=None, region_id=None, resource_group_id=None, state=None, tags=None, update_time=None, version=None):
        # The cluster ID.
        self.cluster_id = cluster_id  # type: str
        # The specifications of the cluster.
        # 
        # *   Only ack.pro.small may be returned.
        self.cluster_spec = cluster_spec  # type: str
        # The time when the cluster was created.
        self.creation_time = creation_time  # type: str
        # The error message that is returned if the cluster failed to be created.
        self.error_message = error_message  # type: str
        # The cluster name.
        self.name = name  # type: str
        # The configurations of the cluster.
        self.profile = profile  # type: str
        # The region ID.
        self.region_id = region_id  # type: str
        # The resource group ID.
        self.resource_group_id = resource_group_id  # type: str
        # The state of the cluster. Valid values:
        # 
        # *   initial: The cluster is being initialized.
        # *   failed: The cluster failed to be created.
        # *   running: The cluster is running
        # *   inactive: The cluster is not activated.
        # *   deleting: The cluster is being deleted.
        # *   delete_failed: The cluster failed to be deleted.
        # *   deleted: The cluster is deleted.
        self.state = state  # type: str
        # The tags.
        self.tags = tags  # type: list[DescribeHubClustersResponseBodyClustersClusterInfoTags]
        # The time when the cluster was last modified.
        self.update_time = update_time  # type: str
        # The version of the cluster.
        self.version = version  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClustersClusterInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.name is not None:
            result['Name'] = self.name
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeHubClustersResponseBodyClustersClusterInfoTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeHubClustersResponseBodyClustersConditions(TeaModel):
    def __init__(self, message=None, reason=None, status=None, type=None):
        # The error message returned.
        self.message = message  # type: str
        # The reason for the deletion condition.
        self.reason = reason  # type: str
        # The state of the cluster that the deletion condition indicates. Valid values:
        # 
        # *   True: The cluster cannot be deleted.
        # *   False: The cluster can be deleted.
        # *   Unknow: Whether the cluster can be deleted is unknown.
        self.status = status  # type: str
        # The type of deletion condition.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClustersConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeHubClustersResponseBodyClustersEndpoints(TeaModel):
    def __init__(self, intranet_api_server_endpoint=None, public_api_server_endpoint=None):
        # The internal endpoint of the API server.
        self.intranet_api_server_endpoint = intranet_api_server_endpoint  # type: str
        # The public endpoint of the API server.
        self.public_api_server_endpoint = public_api_server_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClustersEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intranet_api_server_endpoint is not None:
            result['IntranetApiServerEndpoint'] = self.intranet_api_server_endpoint
        if self.public_api_server_endpoint is not None:
            result['PublicApiServerEndpoint'] = self.public_api_server_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntranetApiServerEndpoint') is not None:
            self.intranet_api_server_endpoint = m.get('IntranetApiServerEndpoint')
        if m.get('PublicApiServerEndpoint') is not None:
            self.public_api_server_endpoint = m.get('PublicApiServerEndpoint')
        return self


class DescribeHubClustersResponseBodyClustersLogConfig(TeaModel):
    def __init__(self, enable_log=None, log_project=None, log_store_ttl=None):
        # Indicates whether the audit logging feature is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.enable_log = enable_log  # type: bool
        # The name of the project in Simple Log Service.
        self.log_project = log_project  # type: str
        # The number of days that logs are retained by Simple Log Service.
        self.log_store_ttl = log_store_ttl  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClustersLogConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_log is not None:
            result['EnableLog'] = self.enable_log
        if self.log_project is not None:
            result['LogProject'] = self.log_project
        if self.log_store_ttl is not None:
            result['LogStoreTTL'] = self.log_store_ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableLog') is not None:
            self.enable_log = m.get('EnableLog')
        if m.get('LogProject') is not None:
            self.log_project = m.get('LogProject')
        if m.get('LogStoreTTL') is not None:
            self.log_store_ttl = m.get('LogStoreTTL')
        return self


class DescribeHubClustersResponseBodyClustersMeshConfig(TeaModel):
    def __init__(self, enable_mesh=None, mesh_id=None):
        # Indicates whether ASM is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.enable_mesh = enable_mesh  # type: bool
        # The ASM instance ID.
        self.mesh_id = mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClustersMeshConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_mesh is not None:
            result['EnableMesh'] = self.enable_mesh
        if self.mesh_id is not None:
            result['MeshId'] = self.mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableMesh') is not None:
            self.enable_mesh = m.get('EnableMesh')
        if m.get('MeshId') is not None:
            self.mesh_id = m.get('MeshId')
        return self


class DescribeHubClustersResponseBodyClustersNetwork(TeaModel):
    def __init__(self, cluster_domain=None, security_group_ids=None, v_switches=None, vpc_id=None):
        # The domain name of the cluster.
        self.cluster_domain = cluster_domain  # type: str
        # The security group IDs.
        self.security_group_ids = security_group_ids  # type: list[str]
        # The IDs of vSwitches to which the cluster belongs.
        self.v_switches = v_switches  # type: list[str]
        # The ID of the virtual private cloud (VPC) to which the cluster belongs.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClustersNetwork, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.security_group_ids is not None:
            result['SecurityGroupIDs'] = self.security_group_ids
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('SecurityGroupIDs') is not None:
            self.security_group_ids = m.get('SecurityGroupIDs')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeHubClustersResponseBodyClusters(TeaModel):
    def __init__(self, api_server=None, cluster_info=None, conditions=None, endpoints=None, log_config=None,
                 mesh_config=None, network=None):
        # The information about the API server.
        self.api_server = api_server  # type: DescribeHubClustersResponseBodyClustersApiServer
        # The details of the cluster.
        self.cluster_info = cluster_info  # type: DescribeHubClustersResponseBodyClustersClusterInfo
        # The deletion conditions of the cluster.
        self.conditions = conditions  # type: list[DescribeHubClustersResponseBodyClustersConditions]
        # The endpoints of the cluster.
        self.endpoints = endpoints  # type: DescribeHubClustersResponseBodyClustersEndpoints
        # The logging configurations.
        self.log_config = log_config  # type: DescribeHubClustersResponseBodyClustersLogConfig
        # The configurations of Alibaba Cloud Service Mesh (ASM).
        self.mesh_config = mesh_config  # type: DescribeHubClustersResponseBodyClustersMeshConfig
        # The network configurations of the cluster.
        self.network = network  # type: DescribeHubClustersResponseBodyClustersNetwork

    def validate(self):
        if self.api_server:
            self.api_server.validate()
        if self.cluster_info:
            self.cluster_info.validate()
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()
        if self.endpoints:
            self.endpoints.validate()
        if self.log_config:
            self.log_config.validate()
        if self.mesh_config:
            self.mesh_config.validate()
        if self.network:
            self.network.validate()

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server is not None:
            result['ApiServer'] = self.api_server.to_map()
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info.to_map()
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        if self.log_config is not None:
            result['LogConfig'] = self.log_config.to_map()
        if self.mesh_config is not None:
            result['MeshConfig'] = self.mesh_config.to_map()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiServer') is not None:
            temp_model = DescribeHubClustersResponseBodyClustersApiServer()
            self.api_server = temp_model.from_map(m['ApiServer'])
        if m.get('ClusterInfo') is not None:
            temp_model = DescribeHubClustersResponseBodyClustersClusterInfo()
            self.cluster_info = temp_model.from_map(m['ClusterInfo'])
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = DescribeHubClustersResponseBodyClustersConditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('Endpoints') is not None:
            temp_model = DescribeHubClustersResponseBodyClustersEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('LogConfig') is not None:
            temp_model = DescribeHubClustersResponseBodyClustersLogConfig()
            self.log_config = temp_model.from_map(m['LogConfig'])
        if m.get('MeshConfig') is not None:
            temp_model = DescribeHubClustersResponseBodyClustersMeshConfig()
            self.mesh_config = temp_model.from_map(m['MeshConfig'])
        if m.get('Network') is not None:
            temp_model = DescribeHubClustersResponseBodyClustersNetwork()
            self.network = temp_model.from_map(m['Network'])
        return self


class DescribeHubClustersResponseBody(TeaModel):
    def __init__(self, clusters=None, request_id=None):
        # The information about clusters.
        self.clusters = clusters  # type: list[DescribeHubClustersResponseBodyClusters]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHubClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = DescribeHubClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHubClustersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHubClustersResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHubClustersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHubClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeManagedClustersRequest(TeaModel):
    def __init__(self, cluster_id=None):
        # The status of the association between the clusters and Service Mesh (ASM).
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeManagedClustersRequest, self).to_map()
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


class DescribeManagedClustersResponseBodyClustersCluster(TeaModel):
    def __init__(self, cluster_id=None, cluster_spec=None, cluster_type=None, created=None, current_version=None,
                 init_version=None, name=None, profile=None, region=None, resource_group_id=None, state=None, updated=None,
                 v_switch_id=None, vpc_id=None):
        # Information about the master instance.
        self.cluster_id = cluster_id  # type: str
        # The ID of the master instance.
        self.cluster_spec = cluster_spec  # type: str
        # The time when the master instance was created.
        self.cluster_type = cluster_type  # type: str
        # The ID of the master instance.
        self.created = created  # type: str
        # The name of the master instance.
        self.current_version = current_version  # type: str
        # The specification of the master instance. Valid values: - ack.pro.small: ACK Pro.
        self.init_version = init_version  # type: str
        # The status information.
        self.name = name  # type: str
        # The ID of the request.
        self.profile = profile  # type: str
        # The ID of the master instance.
        self.region = region  # type: str
        # The name of the master instance.
        self.resource_group_id = resource_group_id  # type: str
        # The current Kubernetes version of the master instance.
        self.state = state  # type: str
        # The ID of the vSwitch.
        self.updated = updated  # type: str
        # The original Kubernetes version of the master instance.
        self.v_switch_id = v_switch_id  # type: str
        # The status of the association between the clusters and the master instance. Valid values: - Installing: The clusters are being associated with the master instance. - Successed: The clusters are associated with the master instance. - Failed: The clusters failed to be associated with the master instance. - Deleting: The clusters are being disassociated from the master instance. - Deleted: The clusters are disassociated from the master instance.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeManagedClustersResponseBodyClustersCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterID'] = self.cluster_id
        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.created is not None:
            result['Created'] = self.created
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.init_version is not None:
            result['InitVersion'] = self.init_version
        if self.name is not None:
            result['Name'] = self.name
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.v_switch_id is not None:
            result['VSwitchID'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcID'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterID') is not None:
            self.cluster_id = m.get('ClusterID')
        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('InitVersion') is not None:
            self.init_version = m.get('InitVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('VSwitchID') is not None:
            self.v_switch_id = m.get('VSwitchID')
        if m.get('VpcID') is not None:
            self.vpc_id = m.get('VpcID')
        return self


class DescribeManagedClustersResponseBodyClustersMeshStatus(TeaModel):
    def __init__(self, in_mesh=None):
        self.in_mesh = in_mesh  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeManagedClustersResponseBodyClustersMeshStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_mesh is not None:
            result['InMesh'] = self.in_mesh
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InMesh') is not None:
            self.in_mesh = m.get('InMesh')
        return self


class DescribeManagedClustersResponseBodyClustersStatus(TeaModel):
    def __init__(self, message=None, state=None):
        # Query the clusters that are associated with a master instance.
        self.message = message  # type: str
        # You can call the DescribeManagedClusters operation to query the clusters that are associated with a master instance.
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeManagedClustersResponseBodyClustersStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeManagedClustersResponseBodyClusters(TeaModel):
    def __init__(self, cluster=None, mesh_status=None, status=None):
        # The name of the master instance.
        self.cluster = cluster  # type: DescribeManagedClustersResponseBodyClustersCluster
        # Zhishi
        self.mesh_status = mesh_status  # type: DescribeManagedClustersResponseBodyClustersMeshStatus
        # Example 1
        self.status = status  # type: DescribeManagedClustersResponseBodyClustersStatus

    def validate(self):
        if self.cluster:
            self.cluster.validate()
        if self.mesh_status:
            self.mesh_status.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(DescribeManagedClustersResponseBodyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['Cluster'] = self.cluster.to_map()
        if self.mesh_status is not None:
            result['MeshStatus'] = self.mesh_status.to_map()
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cluster') is not None:
            temp_model = DescribeManagedClustersResponseBodyClustersCluster()
            self.cluster = temp_model.from_map(m['Cluster'])
        if m.get('MeshStatus') is not None:
            temp_model = DescribeManagedClustersResponseBodyClustersMeshStatus()
            self.mesh_status = temp_model.from_map(m['MeshStatus'])
        if m.get('Status') is not None:
            temp_model = DescribeManagedClustersResponseBodyClustersStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class DescribeManagedClustersResponseBody(TeaModel):
    def __init__(self, clusters=None, request_id=None):
        # The status of the associated clusters. Valid values: - initial: The associated clusters are being initialized. - failed: The associated clustersfailed to be created. - running: The associated clusters are running. - inactive: The associated clusters are inactive. - deleting: The associated clusters are being deleted. - deleted: The associated clusters are deleted.
        self.clusters = clusters  # type: list[DescribeManagedClustersResponseBodyClusters]
        # VPC ID
        self.request_id = request_id  # type: str

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeManagedClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = DescribeManagedClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeManagedClustersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeManagedClustersResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeManagedClustersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeManagedClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePoliciesResponseBodyPolicies(TeaModel):
    def __init__(self, category=None, names=None):
        # The policy type.
        self.category = category  # type: str
        # The names of the policies of each policy type.
        self.names = names  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePoliciesResponseBodyPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.names is not None:
            result['Names'] = self.names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        return self


class DescribePoliciesResponseBody(TeaModel):
    def __init__(self, policies=None, request_id=None):
        # A list of policies.
        self.policies = policies  # type: list[DescribePoliciesResponseBodyPolicies]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePoliciesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = DescribePoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePoliciesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePoliciesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyDetailsRequest(TeaModel):
    def __init__(self, policy_name=None):
        # The policy name.
        self.policy_name = policy_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyDetailsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class DescribePolicyDetailsResponseBodyPolicy(TeaModel):
    def __init__(self, action=None, category=None, created=None, description=None, name=None, no_config=None,
                 severity=None, template=None, updated=None):
        # The action of the policy. Valid values:
        # 
        # *   enforce: blocks deployments that match the policy.
        # *   inform: generates alerts for deployments that match the policy.
        self.action = action  # type: str
        # The type of the policy.
        self.category = category  # type: str
        # The time when the policy was created.
        self.created = created  # type: str
        # The description of the policy.
        self.description = description  # type: str
        # The name of the policy.
        self.name = name  # type: str
        # Indicates whether parameters are required. Valid values:
        # 
        # *   0: Parameters are required.
        # *   1: Parameters are not required.
        self.no_config = no_config  # type: int
        # The severity level of the policy.
        self.severity = severity  # type: str
        # The content of the policy.
        self.template = template  # type: str
        # The time when the policy was last updated.
        self.updated = updated  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyDetailsResponseBodyPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.category is not None:
            result['Category'] = self.category
        if self.created is not None:
            result['Created'] = self.created
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.no_config is not None:
            result['NoConfig'] = self.no_config
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.template is not None:
            result['Template'] = self.template
        if self.updated is not None:
            result['Updated'] = self.updated
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NoConfig') is not None:
            self.no_config = m.get('NoConfig')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        return self


class DescribePolicyDetailsResponseBody(TeaModel):
    def __init__(self, policy=None, request_id=None):
        # The policies.
        self.policy = policy  # type: DescribePolicyDetailsResponseBodyPolicy
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super(DescribePolicyDetailsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = DescribePolicyDetailsResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePolicyDetailsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePolicyDetailsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePolicyDetailsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePolicyDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyGovernanceInClusterRequest(TeaModel):
    def __init__(self, cluster_id=None):
        # The ID of the master instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterRequest, self).to_map()
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


class DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesCluster(TeaModel):
    def __init__(self, cluster_id=None, cluster_spec=None, cluster_type=None, name=None, profile=None,
                 region_id=None, state=None):
        # The ID of the associated cluster.
        self.cluster_id = cluster_id  # type: str
        # The specifications of the associated cluster.
        self.cluster_spec = cluster_spec  # type: str
        # The type of the associated cluster.
        self.cluster_type = cluster_type  # type: str
        # The name of the associated cluster.
        self.name = name  # type: str
        # The identifier of the associated cluster.
        self.profile = profile  # type: str
        # The region ID of the associated cluster.
        self.region_id = region_id  # type: str
        # The status of the associated cluster.
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.name is not None:
            result['Name'] = self.name
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceAdmitLog(TeaModel):
    def __init__(self, count=None, log_project=None, log_store=None, logs=None, progress=None):
        # The number of log entries in the query result.
        self.count = count  # type: str
        # The name of the Log Service project.
        self.log_project = log_project  # type: str
        # The name of the Logstore.
        self.log_store = log_store  # type: str
        # The content of the audit log.
        self.logs = logs  # type: list[dict[str, str]]
        # The status of the query. Valid values:
        # 
        # *   Complete: The query is successful, and the complete result is returned.
        # *   Incomplete: The query is successful, but the query result is incomplete. To obtain the complete result, you must call the operation again.
        self.progress = progress  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceAdmitLog, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.log_project is not None:
            result['LogProject'] = self.log_project
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('LogProject') is not None:
            self.log_project = m.get('LogProject')
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceOnState(TeaModel):
    def __init__(self, enabled_count=None, severity=None, total_count=None):
        # The types of policies that are enabled in the associated cluster.
        self.enabled_count = enabled_count  # type: long
        # The severity level.
        self.severity = severity  # type: str
        # The types of policies of each severity level.
        self.total_count = total_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceOnState, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled_count is not None:
            result['EnabledCount'] = self.enabled_count
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnabledCount') is not None:
            self.enabled_count = m.get('EnabledCount')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationTotalViolationsDeny(TeaModel):
    def __init__(self, severity=None, violations=None):
        # The severity level.
        self.severity = severity  # type: str
        # The number of deployments that are blocked.
        self.violations = violations  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationTotalViolationsDeny, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.violations is not None:
            result['Violations'] = self.violations
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Violations') is not None:
            self.violations = m.get('Violations')
        return self


class DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationTotalViolationsWarn(TeaModel):
    def __init__(self, severity=None, violations=None):
        # The severity level.
        self.severity = severity  # type: str
        # The number of deployments that have triggered alerting.
        self.violations = violations  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationTotalViolationsWarn, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.violations is not None:
            result['Violations'] = self.violations
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Violations') is not None:
            self.violations = m.get('Violations')
        return self


class DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationTotalViolations(TeaModel):
    def __init__(self, deny=None, warn=None):
        # The information about the deployments that are blocked.
        self.deny = deny  # type: list[DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationTotalViolationsDeny]
        # The information about the deployments that have triggered alerting.
        self.warn = warn  # type: list[DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationTotalViolationsWarn]

    def validate(self):
        if self.deny:
            for k in self.deny:
                if k:
                    k.validate()
        if self.warn:
            for k in self.warn:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationTotalViolations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Deny'] = []
        if self.deny is not None:
            for k in self.deny:
                result['Deny'].append(k.to_map() if k else None)
        result['Warn'] = []
        if self.warn is not None:
            for k in self.warn:
                result['Warn'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.deny = []
        if m.get('Deny') is not None:
            for k in m.get('Deny'):
                temp_model = DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationTotalViolationsDeny()
                self.deny.append(temp_model.from_map(k))
        self.warn = []
        if m.get('Warn') is not None:
            for k in m.get('Warn'):
                temp_model = DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationTotalViolationsWarn()
                self.warn.append(temp_model.from_map(k))
        return self


class DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationViolationsDeny(TeaModel):
    def __init__(self, policy_description=None, policy_name=None, severity=None, violations=None):
        # The description of the policy.
        self.policy_description = policy_description  # type: str
        # The name of the policy.
        self.policy_name = policy_name  # type: str
        # The severity level of the policy.
        self.severity = severity  # type: str
        # The number of times that the policy blocks deployments.
        self.violations = violations  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationViolationsDeny, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.violations is not None:
            result['Violations'] = self.violations
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Violations') is not None:
            self.violations = m.get('Violations')
        return self


class DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationViolationsWarn(TeaModel):
    def __init__(self, policy_description=None, policy_name=None, severity=None, violations=None):
        # The description of the policy.
        self.policy_description = policy_description  # type: str
        # The name of the policy.
        self.policy_name = policy_name  # type: str
        # The severity level of the policy.
        self.severity = severity  # type: str
        # The number of times that the policy generates alerts.
        self.violations = violations  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationViolationsWarn, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.violations is not None:
            result['Violations'] = self.violations
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Violations') is not None:
            self.violations = m.get('Violations')
        return self


class DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationViolations(TeaModel):
    def __init__(self, deny=None, warn=None):
        # The information about the deployments that are blocked.
        self.deny = deny  # type: list[DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationViolationsDeny]
        # The information about the deployments that have triggered alerting.
        self.warn = warn  # type: list[DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationViolationsWarn]

    def validate(self):
        if self.deny:
            for k in self.deny:
                if k:
                    k.validate()
        if self.warn:
            for k in self.warn:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationViolations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Deny'] = []
        if self.deny is not None:
            for k in self.deny:
                result['Deny'].append(k.to_map() if k else None)
        result['Warn'] = []
        if self.warn is not None:
            for k in self.warn:
                result['Warn'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.deny = []
        if m.get('Deny') is not None:
            for k in m.get('Deny'):
                temp_model = DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationViolationsDeny()
                self.deny.append(temp_model.from_map(k))
        self.warn = []
        if m.get('Warn') is not None:
            for k in m.get('Warn'):
                temp_model = DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationViolationsWarn()
                self.warn.append(temp_model.from_map(k))
        return self


class DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolation(TeaModel):
    def __init__(self, total_violations=None, violations=None):
        # The number of deployments that match the policies in the associated cluster, including deployments that are blocked and deployments that have triggered alerting. The deployments are classified by severity level.
        self.total_violations = total_violations  # type: DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationTotalViolations
        # The number of deployments that match the policies in the associated cluster, including deployments that are blocked and deployments that have triggered alerting. The deployments are classified by policy type.
        self.violations = violations  # type: DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationViolations

    def validate(self):
        if self.total_violations:
            self.total_violations.validate()
        if self.violations:
            self.violations.validate()

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_violations is not None:
            result['TotalViolations'] = self.total_violations.to_map()
        if self.violations is not None:
            result['Violations'] = self.violations.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalViolations') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationTotalViolations()
            self.total_violations = temp_model.from_map(m['TotalViolations'])
        if m.get('Violations') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolationViolations()
            self.violations = temp_model.from_map(m['Violations'])
        return self


class DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernance(TeaModel):
    def __init__(self, admit_log=None, on_state=None, violation=None):
        # The audit log generated by the associated cluster.
        self.admit_log = admit_log  # type: DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceAdmitLog
        # The number of policies of each severity level enabled in the associated cluster.
        self.on_state = on_state  # type: list[DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceOnState]
        # The number of deployments that match the policies in the associated cluster, including deployments that are blocked and deployments that have triggered alerting.
        self.violation = violation  # type: DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolation

    def validate(self):
        if self.admit_log:
            self.admit_log.validate()
        if self.on_state:
            for k in self.on_state:
                if k:
                    k.validate()
        if self.violation:
            self.violation.validate()

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernance, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admit_log is not None:
            result['AdmitLog'] = self.admit_log.to_map()
        result['OnState'] = []
        if self.on_state is not None:
            for k in self.on_state:
                result['OnState'].append(k.to_map() if k else None)
        if self.violation is not None:
            result['Violation'] = self.violation.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdmitLog') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceAdmitLog()
            self.admit_log = temp_model.from_map(m['AdmitLog'])
        self.on_state = []
        if m.get('OnState') is not None:
            for k in m.get('OnState'):
                temp_model = DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceOnState()
                self.on_state.append(temp_model.from_map(k))
        if m.get('Violation') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernanceViolation()
            self.violation = temp_model.from_map(m['Violation'])
        return self


class DescribePolicyGovernanceInClusterResponseBodyPolicyGovernances(TeaModel):
    def __init__(self, cluster=None, policy_governance=None):
        # The information about the associated clusters in which the policies are deployed.
        self.cluster = cluster  # type: DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesCluster
        # The detailed policy information.
        self.policy_governance = policy_governance  # type: DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernance

    def validate(self):
        if self.cluster:
            self.cluster.validate()
        if self.policy_governance:
            self.policy_governance.validate()

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBodyPolicyGovernances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['Cluster'] = self.cluster.to_map()
        if self.policy_governance is not None:
            result['PolicyGovernance'] = self.policy_governance.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cluster') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesCluster()
            self.cluster = temp_model.from_map(m['Cluster'])
        if m.get('PolicyGovernance') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyPolicyGovernancesPolicyGovernance()
            self.policy_governance = temp_model.from_map(m['PolicyGovernance'])
        return self


class DescribePolicyGovernanceInClusterResponseBody(TeaModel):
    def __init__(self, policy_governances=None, request_id=None):
        # The detailed information about the policies.
        self.policy_governances = policy_governances  # type: list[DescribePolicyGovernanceInClusterResponseBodyPolicyGovernances]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.policy_governances:
            for k in self.policy_governances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PolicyGovernances'] = []
        if self.policy_governances is not None:
            for k in self.policy_governances:
                result['PolicyGovernances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.policy_governances = []
        if m.get('PolicyGovernances') is not None:
            for k in m.get('PolicyGovernances'):
                temp_model = DescribePolicyGovernanceInClusterResponseBodyPolicyGovernances()
                self.policy_governances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePolicyGovernanceInClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePolicyGovernanceInClusterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePolicyGovernanceInClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyInstancesRequest(TeaModel):
    def __init__(self, cluster_id=None, policy_name=None):
        # The ID of the master instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str
        # The name of the policy.
        # 
        # This parameter is required.
        self.policy_name = policy_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class DescribePolicyInstancesResponseBodyPolicies(TeaModel):
    def __init__(self, cluster_id=None, instance_name=None, policy_action=None, policy_category=None,
                 policy_description=None, policy_name=None, policy_parameters=None, policy_scope=None, policy_severity=None,
                 total_violations=None):
        # The ID of the associated cluster.
        self.cluster_id = cluster_id  # type: str
        # The name of the policy instance.
        self.instance_name = instance_name  # type: str
        # The action of the policy. Valid values:
        # 
        # *   deny: blocks deployments that match the policy.
        # *   warn: generates alerts for deployments that match the policy.
        self.policy_action = policy_action  # type: str
        # The type of the policy.
        self.policy_category = policy_category  # type: str
        # The description of the policy.
        self.policy_description = policy_description  # type: str
        # The name of the policy.
        self.policy_name = policy_name  # type: str
        # The parameters of the policy instance.
        self.policy_parameters = policy_parameters  # type: dict[str, str]
        # The applicable scope of the policy instance.
        # 
        # A value of \\* indicates all namespaces. This is the default value.
        # 
        # Multiple namespaces are separated by commas (,).
        self.policy_scope = policy_scope  # type: str
        # The severity level of the policy.
        self.policy_severity = policy_severity  # type: str
        # The total number of deployments that match the policy in the associated cluster, including the deployments that are blocked and the deployments that have triggered alerting.
        self.total_violations = total_violations  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyInstancesResponseBodyPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action
        if self.policy_category is not None:
            result['PolicyCategory'] = self.policy_category
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_parameters is not None:
            result['PolicyParameters'] = self.policy_parameters
        if self.policy_scope is not None:
            result['PolicyScope'] = self.policy_scope
        if self.policy_severity is not None:
            result['PolicySeverity'] = self.policy_severity
        if self.total_violations is not None:
            result['TotalViolations'] = self.total_violations
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')
        if m.get('PolicyCategory') is not None:
            self.policy_category = m.get('PolicyCategory')
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyParameters') is not None:
            self.policy_parameters = m.get('PolicyParameters')
        if m.get('PolicyScope') is not None:
            self.policy_scope = m.get('PolicyScope')
        if m.get('PolicySeverity') is not None:
            self.policy_severity = m.get('PolicySeverity')
        if m.get('TotalViolations') is not None:
            self.total_violations = m.get('TotalViolations')
        return self


class DescribePolicyInstancesResponseBody(TeaModel):
    def __init__(self, policies=None, request_id=None):
        # A list of policy instances.
        self.policies = policies  # type: list[DescribePolicyInstancesResponseBodyPolicies]
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePolicyInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = DescribePolicyInstancesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePolicyInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePolicyInstancesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePolicyInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePolicyInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyInstancesStatusRequest(TeaModel):
    def __init__(self, cluster_id=None):
        # The ID of the master instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyInstancesStatusRequest, self).to_map()
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


class DescribePolicyInstancesStatusResponseBodyPoliciesPolicyInstancesPolicyClusters(TeaModel):
    def __init__(self, cluster_id=None, status=None):
        # The cluster ID.
        self.cluster_id = cluster_id  # type: str
        # The status of the policy deployment.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyInstancesStatusResponseBodyPoliciesPolicyInstancesPolicyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribePolicyInstancesStatusResponseBodyPoliciesPolicyInstances(TeaModel):
    def __init__(self, policy_category=None, policy_clusters=None, policy_description=None,
                 policy_instances_count=None, policy_name=None, policy_severity=None):
        # The type of the policy.
        self.policy_category = policy_category  # type: str
        # The associated clusters in which the policy instances are deployed.
        self.policy_clusters = policy_clusters  # type: list[DescribePolicyInstancesStatusResponseBodyPoliciesPolicyInstancesPolicyClusters]
        # The description of the policy.
        self.policy_description = policy_description  # type: str
        # The number of policy instances that are deployed. If this parameter is left empty, no policy instance is deployed.
        self.policy_instances_count = policy_instances_count  # type: long
        # The policy name.
        self.policy_name = policy_name  # type: str
        # The severity level of the policy.
        self.policy_severity = policy_severity  # type: str

    def validate(self):
        if self.policy_clusters:
            for k in self.policy_clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePolicyInstancesStatusResponseBodyPoliciesPolicyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_category is not None:
            result['PolicyCategory'] = self.policy_category
        result['PolicyClusters'] = []
        if self.policy_clusters is not None:
            for k in self.policy_clusters:
                result['PolicyClusters'].append(k.to_map() if k else None)
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description
        if self.policy_instances_count is not None:
            result['PolicyInstancesCount'] = self.policy_instances_count
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_severity is not None:
            result['PolicySeverity'] = self.policy_severity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyCategory') is not None:
            self.policy_category = m.get('PolicyCategory')
        self.policy_clusters = []
        if m.get('PolicyClusters') is not None:
            for k in m.get('PolicyClusters'):
                temp_model = DescribePolicyInstancesStatusResponseBodyPoliciesPolicyInstancesPolicyClusters()
                self.policy_clusters.append(temp_model.from_map(k))
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')
        if m.get('PolicyInstancesCount') is not None:
            self.policy_instances_count = m.get('PolicyInstancesCount')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicySeverity') is not None:
            self.policy_severity = m.get('PolicySeverity')
        return self


class DescribePolicyInstancesStatusResponseBodyPoliciesSeverityInfo(TeaModel):
    def __init__(self, severity_count=None, severity_type=None):
        # The number of policy instances.
        self.severity_count = severity_count  # type: str
        # The severity level of the policy.
        self.severity_type = severity_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePolicyInstancesStatusResponseBodyPoliciesSeverityInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.severity_count is not None:
            result['SeverityCount'] = self.severity_count
        if self.severity_type is not None:
            result['SeverityType'] = self.severity_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SeverityCount') is not None:
            self.severity_count = m.get('SeverityCount')
        if m.get('SeverityType') is not None:
            self.severity_type = m.get('SeverityType')
        return self


class DescribePolicyInstancesStatusResponseBodyPolicies(TeaModel):
    def __init__(self, policy_instances=None, severity_info=None):
        # The number of policy instances of each policy type.
        self.policy_instances = policy_instances  # type: list[DescribePolicyInstancesStatusResponseBodyPoliciesPolicyInstances]
        # The number of policy instances that are deployed in the cluster.
        self.severity_info = severity_info  # type: list[DescribePolicyInstancesStatusResponseBodyPoliciesSeverityInfo]

    def validate(self):
        if self.policy_instances:
            for k in self.policy_instances:
                if k:
                    k.validate()
        if self.severity_info:
            for k in self.severity_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePolicyInstancesStatusResponseBodyPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PolicyInstances'] = []
        if self.policy_instances is not None:
            for k in self.policy_instances:
                result['PolicyInstances'].append(k.to_map() if k else None)
        result['SeverityInfo'] = []
        if self.severity_info is not None:
            for k in self.severity_info:
                result['SeverityInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.policy_instances = []
        if m.get('PolicyInstances') is not None:
            for k in m.get('PolicyInstances'):
                temp_model = DescribePolicyInstancesStatusResponseBodyPoliciesPolicyInstances()
                self.policy_instances.append(temp_model.from_map(k))
        self.severity_info = []
        if m.get('SeverityInfo') is not None:
            for k in m.get('SeverityInfo'):
                temp_model = DescribePolicyInstancesStatusResponseBodyPoliciesSeverityInfo()
                self.severity_info.append(temp_model.from_map(k))
        return self


class DescribePolicyInstancesStatusResponseBody(TeaModel):
    def __init__(self, policies=None, request_id=None):
        # The number of policy instances of each policy type.
        self.policies = policies  # type: DescribePolicyInstancesStatusResponseBodyPolicies
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.policies:
            self.policies.validate()

    def to_map(self):
        _map = super(DescribePolicyInstancesStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policies is not None:
            result['Policies'] = self.policies.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Policies') is not None:
            temp_model = DescribePolicyInstancesStatusResponseBodyPolicies()
            self.policies = temp_model.from_map(m['Policies'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePolicyInstancesStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePolicyInstancesStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePolicyInstancesStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePolicyInstancesStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, language=None):
        # The language. Valid values: zh and en.
        self.language = language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        # The name of the region.
        self.local_name = local_name  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
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


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        # A list of available regions that are returned.
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]
        # The ID of the request.
        self.request_id = request_id  # type: str

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
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DescribeUserPermissionsRequest(TeaModel):
    def __init__(self, user_id=None):
        # The ID of the RAM user that you want to query.
        # 
        # This parameter is required.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserPermissionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeUserPermissionsResponseBodyPermissions(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, role_name=None, role_type=None):
        # The authorization setting. Valid values:
        # 
        # *   {cluster_id} is returned if the permissions are scoped to a cluster.
        # *   {cluster_id}/{namespace} is returned if the permissions are scoped to a namespace of a cluster.
        # *   all-clusters is returned if the permissions are scoped to all clusters.
        self.resource_id = resource_id  # type: str
        # The authorization type. Valid values:
        # 
        # *   cluster: indicates that the permissions are scoped to a cluster.
        # *   namespace: indicates that the permissions are scoped to a namespace of a cluster.
        self.resource_type = resource_type  # type: str
        # The name of the custom role. If a custom role is assigned, the value is the name of the assigned custom role.
        self.role_name = role_name  # type: str
        # The type of predefined role. Valid values:
        # 
        # *   admin: administrator
        # *   dev: developer
        self.role_type = role_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUserPermissionsResponseBodyPermissions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class DescribeUserPermissionsResponseBody(TeaModel):
    def __init__(self, permissions=None, request_id=None):
        # The details about the permissions of the RAM user.
        self.permissions = permissions  # type: list[DescribeUserPermissionsResponseBodyPermissions]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUserPermissionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['Permissions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.permissions = []
        if m.get('Permissions') is not None:
            for k in m.get('Permissions'):
                temp_model = DescribeUserPermissionsResponseBodyPermissions()
                self.permissions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserPermissionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUserPermissionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUserPermissionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachClusterFromHubRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_ids=None, detach_from_mesh=None):
        # The ID of the request.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str
        # The operation that you want to perform. Set the value to **DetachClusterFromHub**.
        # 
        # This parameter is required.
        self.cluster_ids = cluster_ids  # type: str
        # Example 1
        self.detach_from_mesh = detach_from_mesh  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachClusterFromHubRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids
        if self.detach_from_mesh is not None:
            result['DetachFromMesh'] = self.detach_from_mesh
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')
        if m.get('DetachFromMesh') is not None:
            self.detach_from_mesh = m.get('DetachFromMesh')
        return self


class DetachClusterFromHubResponseBody(TeaModel):
    def __init__(self, cluster_id=None, managed_cluster_ids=None, request_id=None, task_id=None):
        # Zhishi
        self.cluster_id = cluster_id  # type: str
        self.managed_cluster_ids = managed_cluster_ids  # type: list[str]
        # You can call the DetachClusterFromHub operation to disassociate clusters from a master instance.
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachClusterFromHubResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.managed_cluster_ids is not None:
            result['ManagedClusterIds'] = self.managed_cluster_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ManagedClusterIds') is not None:
            self.managed_cluster_ids = m.get('ManagedClusterIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DetachClusterFromHubResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachClusterFromHubResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachClusterFromHubResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachClusterFromHubResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantUserPermissionRequest(TeaModel):
    def __init__(self, cluster_id=None, is_ram_role=None, namespace=None, role_name=None, role_type=None,
                 user_id=None):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str
        # The entity to which the permissions are granted. A value of `true` indicates that the permissions are granted to a RAM user. A value of `false` indicates that the permissions are granted to a RAM role.
        self.is_ram_role = is_ram_role  # type: bool
        # The name of the namespace.
        # 
        # *   If **RoleType** is set to **cluster**, you do not need to specify this parameter.
        # *   This parameter is required if **RoleType** is set to **namespace**.
        # *   If **RoleType** is set to **namespace** and **RoleName** is set to **gitops-dev**, this parameter is required and must be set to **argocd**.
        self.namespace = namespace  # type: str
        # The predefined role. Valid values:
        # 
        # *   admin: administrator
        # *   dev: developer
        # *   gitops-dev: GitOps developer. The parameter is available only for Fleet instances.
        # 
        # The value of RoleName and that of RoleType must meet the following requirements:
        # 
        # *   If **RoleType** is set to **cluster**, this parameter must be set to **admin**.
        # *   If **RoleType** is set to **namespace**, this parameter must be set to **dev** or **gitops-dev**.
        # 
        # This parameter is required.
        self.role_name = role_name  # type: str
        # The authorization type. Valid values:
        # 
        # *   cluster: The permissions are granted to a cluster.
        # *   namespace: The permissions are granted to a namespace of a cluster.
        # 
        # This parameter is required.
        self.role_type = role_type  # type: str
        # The ID of the RAM user or RAM role.
        # 
        # This parameter is required.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantUserPermissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.is_ram_role is not None:
            result['IsRamRole'] = self.is_ram_role
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IsRamRole') is not None:
            self.is_ram_role = m.get('IsRamRole')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GrantUserPermissionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantUserPermissionResponseBody, self).to_map()
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


class GrantUserPermissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GrantUserPermissionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GrantUserPermissionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GrantUserPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantUserPermissionsRequestPermissions(TeaModel):
    def __init__(self, cluster_id=None, is_ram_role=None, namespace=None, role_name=None, role_type=None):
        # The master instance ID.
        # 
        # *   When the role_type parameter is set to all-clusters, set the parameter to an empty string.
        self.cluster_id = cluster_id  # type: str
        # The entity to which the permissions are granted. A value of `true` indicates that the permissions are granted to a RAM user. A value of `false` indicates that the permissions are granted to a RAM role.
        self.is_ram_role = is_ram_role  # type: bool
        # The namespace to which the permissions are scoped. By default, this parameter is empty when you set RoleType to cluster.
        self.namespace = namespace  # type: str
        # The predefined role that you want to assign. Valid values:
        # 
        # *   admin: the administrator role.
        # *   dev: the developer role.
        # 
        # This parameter is required.
        self.role_name = role_name  # type: str
        # The authorization type. Valid values:
        # 
        # *   cluster: specifies that the permissions are scoped to a master instance.
        # *   namespace: specifies that the permissions are scoped to a namespace of a cluster.
        # *   all-clusters: specifies that the permissions are scoped to all master instances.
        # 
        # This parameter is required.
        self.role_type = role_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantUserPermissionsRequestPermissions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.is_ram_role is not None:
            result['IsRamRole'] = self.is_ram_role
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IsRamRole') is not None:
            self.is_ram_role = m.get('IsRamRole')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class GrantUserPermissionsRequest(TeaModel):
    def __init__(self, permissions=None, user_id=None):
        # The list of permissions that you want to grant to the RAM user.
        self.permissions = permissions  # type: list[GrantUserPermissionsRequestPermissions]
        # The ID of the RAM user.
        # 
        # This parameter is required.
        self.user_id = user_id  # type: str

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GrantUserPermissionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['Permissions'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.permissions = []
        if m.get('Permissions') is not None:
            for k in m.get('Permissions'):
                temp_model = GrantUserPermissionsRequestPermissions()
                self.permissions.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GrantUserPermissionsShrinkRequest(TeaModel):
    def __init__(self, permissions_shrink=None, user_id=None):
        # The list of permissions that you want to grant to the RAM user.
        self.permissions_shrink = permissions_shrink  # type: str
        # The ID of the RAM user.
        # 
        # This parameter is required.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantUserPermissionsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions_shrink is not None:
            result['Permissions'] = self.permissions_shrink
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Permissions') is not None:
            self.permissions_shrink = m.get('Permissions')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GrantUserPermissionsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GrantUserPermissionsResponseBody, self).to_map()
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


class GrantUserPermissionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GrantUserPermissionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GrantUserPermissionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GrantUserPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHubClusterFeatureRequest(TeaModel):
    def __init__(self, access_control_list=None, api_server_eip_id=None, argo_cdenabled=None,
                 argo_cdhaenabled=None, argo_events_enabled=None, argo_server_enabled=None, audit_log_enabled=None, cluster_id=None,
                 deletion_protection=None, enable_mesh=None, gateway_enabled=None, monitor_enabled=None, name=None, price_limit=None,
                 public_access_enabled=None, public_api_server_enabled=None, v_switches=None, workflow_schedule_mode=None):
        # The Internet access control list (ACL). This parameter takes effect only if PublicAccessEnabled is set to true.
        self.access_control_list = access_control_list  # type: list[str]
        # The ID of the EIP.
        self.api_server_eip_id = api_server_eip_id  # type: str
        # Specifies whether to enable Argo CD. This parameter takes effect only if Profile is set to XFlow. Valid values:
        # 
        # *   true
        # *   false
        self.argo_cdenabled = argo_cdenabled  # type: bool
        # Specifies whether to enable high availability for Argo CD. Valid values:
        # 
        # *   true
        # *   false
        self.argo_cdhaenabled = argo_cdhaenabled  # type: bool
        # Specifies whether to enable ArgoEvents. Valid values:
        # 
        # - true
        # - false
        self.argo_events_enabled = argo_events_enabled  # type: bool
        # Specifies whether to enable the workflow instance UI. This parameter takes effect only if Profile is set to XFlow. Valid values:
        # 
        # *   true
        # *   false
        self.argo_server_enabled = argo_server_enabled  # type: bool
        # Specifies whether to enable the audit logging feature. Valid values:
        # 
        # *   true: enables the audit logging feature.
        # *   false: disables the audit logging feature.
        self.audit_log_enabled = audit_log_enabled  # type: bool
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str
        # Specifies whether to enable the deletion protection feature for the cluster. After you enable the deletion protection feature for the cluster, you cannot delete the cluster in the console or by calling the DeleteHubCluster operation. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.deletion_protection = deletion_protection  # type: bool
        # Specifies whether to enable Service Mesh (ASM). Valid values:
        # 
        # *   true
        # *   false
        self.enable_mesh = enable_mesh  # type: bool
        # Specifies whether to enable Gateway. Valid values:
        # - true
        # - false
        self.gateway_enabled = gateway_enabled  # type: bool
        # Specifies whether to enable the monitoring dashboard feature for the workflow instance. This parameter takes effect only if Profile is set to XFlow. Valid values:
        # 
        # *   true
        # *   false
        self.monitor_enabled = monitor_enabled  # type: bool
        # The name of the master instance. The name must be 1 to 63 characters in length. It must start with a letter, and can contain letters, digits, underscores (_), and hyphens (-).
        self.name = name  # type: str
        # The limit on the prices of containers in the workflow. This parameter takes effect only if the WorkflowScheduleMode parameter is set to cost-optimized.
        self.price_limit = price_limit  # type: str
        # Specifies whether to enable public domain name resolution in the Argo CD or Argo Workflow console. Valid values:
        # 
        # *   true
        # *   false
        self.public_access_enabled = public_access_enabled  # type: bool
        # Specifies whether to associate an elastic IP address (EIP) with the API server. Valid values:
        # 
        # *   true: associates an EIP with the API server. You can specify ApiServerEipId. If you do not specify ApiServerEipId, the system automatically creates an EIP.
        # *   false: disassociates an EIP from the API server.
        self.public_api_server_enabled = public_api_server_enabled  # type: bool
        # The vSwitches.
        self.v_switches = v_switches  # type: list[str]
        # The scheduling mode of the workflow. This parameter takes effect only if Profile is set to XFlow. Valid values:
        # 
        # *   cost-optimized: cost-prioritized scheduling mode.
        # *   stock-optimized: inventory-prioritized scheduling mode.
        self.workflow_schedule_mode = workflow_schedule_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHubClusterFeatureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_list is not None:
            result['AccessControlList'] = self.access_control_list
        if self.api_server_eip_id is not None:
            result['ApiServerEipId'] = self.api_server_eip_id
        if self.argo_cdenabled is not None:
            result['ArgoCDEnabled'] = self.argo_cdenabled
        if self.argo_cdhaenabled is not None:
            result['ArgoCDHAEnabled'] = self.argo_cdhaenabled
        if self.argo_events_enabled is not None:
            result['ArgoEventsEnabled'] = self.argo_events_enabled
        if self.argo_server_enabled is not None:
            result['ArgoServerEnabled'] = self.argo_server_enabled
        if self.audit_log_enabled is not None:
            result['AuditLogEnabled'] = self.audit_log_enabled
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.enable_mesh is not None:
            result['EnableMesh'] = self.enable_mesh
        if self.gateway_enabled is not None:
            result['GatewayEnabled'] = self.gateway_enabled
        if self.monitor_enabled is not None:
            result['MonitorEnabled'] = self.monitor_enabled
        if self.name is not None:
            result['Name'] = self.name
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        if self.public_access_enabled is not None:
            result['PublicAccessEnabled'] = self.public_access_enabled
        if self.public_api_server_enabled is not None:
            result['PublicApiServerEnabled'] = self.public_api_server_enabled
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.workflow_schedule_mode is not None:
            result['WorkflowScheduleMode'] = self.workflow_schedule_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessControlList') is not None:
            self.access_control_list = m.get('AccessControlList')
        if m.get('ApiServerEipId') is not None:
            self.api_server_eip_id = m.get('ApiServerEipId')
        if m.get('ArgoCDEnabled') is not None:
            self.argo_cdenabled = m.get('ArgoCDEnabled')
        if m.get('ArgoCDHAEnabled') is not None:
            self.argo_cdhaenabled = m.get('ArgoCDHAEnabled')
        if m.get('ArgoEventsEnabled') is not None:
            self.argo_events_enabled = m.get('ArgoEventsEnabled')
        if m.get('ArgoServerEnabled') is not None:
            self.argo_server_enabled = m.get('ArgoServerEnabled')
        if m.get('AuditLogEnabled') is not None:
            self.audit_log_enabled = m.get('AuditLogEnabled')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('EnableMesh') is not None:
            self.enable_mesh = m.get('EnableMesh')
        if m.get('GatewayEnabled') is not None:
            self.gateway_enabled = m.get('GatewayEnabled')
        if m.get('MonitorEnabled') is not None:
            self.monitor_enabled = m.get('MonitorEnabled')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        if m.get('PublicAccessEnabled') is not None:
            self.public_access_enabled = m.get('PublicAccessEnabled')
        if m.get('PublicApiServerEnabled') is not None:
            self.public_api_server_enabled = m.get('PublicApiServerEnabled')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('WorkflowScheduleMode') is not None:
            self.workflow_schedule_mode = m.get('WorkflowScheduleMode')
        return self


class UpdateHubClusterFeatureShrinkRequest(TeaModel):
    def __init__(self, access_control_list_shrink=None, api_server_eip_id=None, argo_cdenabled=None,
                 argo_cdhaenabled=None, argo_events_enabled=None, argo_server_enabled=None, audit_log_enabled=None, cluster_id=None,
                 deletion_protection=None, enable_mesh=None, gateway_enabled=None, monitor_enabled=None, name=None, price_limit=None,
                 public_access_enabled=None, public_api_server_enabled=None, v_switches_shrink=None, workflow_schedule_mode=None):
        # The Internet access control list (ACL). This parameter takes effect only if PublicAccessEnabled is set to true.
        self.access_control_list_shrink = access_control_list_shrink  # type: str
        # The ID of the EIP.
        self.api_server_eip_id = api_server_eip_id  # type: str
        # Specifies whether to enable Argo CD. This parameter takes effect only if Profile is set to XFlow. Valid values:
        # 
        # *   true
        # *   false
        self.argo_cdenabled = argo_cdenabled  # type: bool
        # Specifies whether to enable high availability for Argo CD. Valid values:
        # 
        # *   true
        # *   false
        self.argo_cdhaenabled = argo_cdhaenabled  # type: bool
        # Specifies whether to enable ArgoEvents. Valid values:
        # 
        # - true
        # - false
        self.argo_events_enabled = argo_events_enabled  # type: bool
        # Specifies whether to enable the workflow instance UI. This parameter takes effect only if Profile is set to XFlow. Valid values:
        # 
        # *   true
        # *   false
        self.argo_server_enabled = argo_server_enabled  # type: bool
        # Specifies whether to enable the audit logging feature. Valid values:
        # 
        # *   true: enables the audit logging feature.
        # *   false: disables the audit logging feature.
        self.audit_log_enabled = audit_log_enabled  # type: bool
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str
        # Specifies whether to enable the deletion protection feature for the cluster. After you enable the deletion protection feature for the cluster, you cannot delete the cluster in the console or by calling the DeleteHubCluster operation. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.deletion_protection = deletion_protection  # type: bool
        # Specifies whether to enable Service Mesh (ASM). Valid values:
        # 
        # *   true
        # *   false
        self.enable_mesh = enable_mesh  # type: bool
        # Specifies whether to enable Gateway. Valid values:
        # - true
        # - false
        self.gateway_enabled = gateway_enabled  # type: bool
        # Specifies whether to enable the monitoring dashboard feature for the workflow instance. This parameter takes effect only if Profile is set to XFlow. Valid values:
        # 
        # *   true
        # *   false
        self.monitor_enabled = monitor_enabled  # type: bool
        # The name of the master instance. The name must be 1 to 63 characters in length. It must start with a letter, and can contain letters, digits, underscores (_), and hyphens (-).
        self.name = name  # type: str
        # The limit on the prices of containers in the workflow. This parameter takes effect only if the WorkflowScheduleMode parameter is set to cost-optimized.
        self.price_limit = price_limit  # type: str
        # Specifies whether to enable public domain name resolution in the Argo CD or Argo Workflow console. Valid values:
        # 
        # *   true
        # *   false
        self.public_access_enabled = public_access_enabled  # type: bool
        # Specifies whether to associate an elastic IP address (EIP) with the API server. Valid values:
        # 
        # *   true: associates an EIP with the API server. You can specify ApiServerEipId. If you do not specify ApiServerEipId, the system automatically creates an EIP.
        # *   false: disassociates an EIP from the API server.
        self.public_api_server_enabled = public_api_server_enabled  # type: bool
        # The vSwitches.
        self.v_switches_shrink = v_switches_shrink  # type: str
        # The scheduling mode of the workflow. This parameter takes effect only if Profile is set to XFlow. Valid values:
        # 
        # *   cost-optimized: cost-prioritized scheduling mode.
        # *   stock-optimized: inventory-prioritized scheduling mode.
        self.workflow_schedule_mode = workflow_schedule_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHubClusterFeatureShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_list_shrink is not None:
            result['AccessControlList'] = self.access_control_list_shrink
        if self.api_server_eip_id is not None:
            result['ApiServerEipId'] = self.api_server_eip_id
        if self.argo_cdenabled is not None:
            result['ArgoCDEnabled'] = self.argo_cdenabled
        if self.argo_cdhaenabled is not None:
            result['ArgoCDHAEnabled'] = self.argo_cdhaenabled
        if self.argo_events_enabled is not None:
            result['ArgoEventsEnabled'] = self.argo_events_enabled
        if self.argo_server_enabled is not None:
            result['ArgoServerEnabled'] = self.argo_server_enabled
        if self.audit_log_enabled is not None:
            result['AuditLogEnabled'] = self.audit_log_enabled
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.enable_mesh is not None:
            result['EnableMesh'] = self.enable_mesh
        if self.gateway_enabled is not None:
            result['GatewayEnabled'] = self.gateway_enabled
        if self.monitor_enabled is not None:
            result['MonitorEnabled'] = self.monitor_enabled
        if self.name is not None:
            result['Name'] = self.name
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        if self.public_access_enabled is not None:
            result['PublicAccessEnabled'] = self.public_access_enabled
        if self.public_api_server_enabled is not None:
            result['PublicApiServerEnabled'] = self.public_api_server_enabled
        if self.v_switches_shrink is not None:
            result['VSwitches'] = self.v_switches_shrink
        if self.workflow_schedule_mode is not None:
            result['WorkflowScheduleMode'] = self.workflow_schedule_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessControlList') is not None:
            self.access_control_list_shrink = m.get('AccessControlList')
        if m.get('ApiServerEipId') is not None:
            self.api_server_eip_id = m.get('ApiServerEipId')
        if m.get('ArgoCDEnabled') is not None:
            self.argo_cdenabled = m.get('ArgoCDEnabled')
        if m.get('ArgoCDHAEnabled') is not None:
            self.argo_cdhaenabled = m.get('ArgoCDHAEnabled')
        if m.get('ArgoEventsEnabled') is not None:
            self.argo_events_enabled = m.get('ArgoEventsEnabled')
        if m.get('ArgoServerEnabled') is not None:
            self.argo_server_enabled = m.get('ArgoServerEnabled')
        if m.get('AuditLogEnabled') is not None:
            self.audit_log_enabled = m.get('AuditLogEnabled')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('EnableMesh') is not None:
            self.enable_mesh = m.get('EnableMesh')
        if m.get('GatewayEnabled') is not None:
            self.gateway_enabled = m.get('GatewayEnabled')
        if m.get('MonitorEnabled') is not None:
            self.monitor_enabled = m.get('MonitorEnabled')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        if m.get('PublicAccessEnabled') is not None:
            self.public_access_enabled = m.get('PublicAccessEnabled')
        if m.get('PublicApiServerEnabled') is not None:
            self.public_api_server_enabled = m.get('PublicApiServerEnabled')
        if m.get('VSwitches') is not None:
            self.v_switches_shrink = m.get('VSwitches')
        if m.get('WorkflowScheduleMode') is not None:
            self.workflow_schedule_mode = m.get('WorkflowScheduleMode')
        return self


class UpdateHubClusterFeatureResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHubClusterFeatureResponseBody, self).to_map()
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


class UpdateHubClusterFeatureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateHubClusterFeatureResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateHubClusterFeatureResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateHubClusterFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserPermissionRequest(TeaModel):
    def __init__(self, cluster_id=None, namespace=None, role_name=None, role_type=None, user_id=None):
        # The ID of the master instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id  # type: str
        # The namespace to which the permissions are scoped. By default, this parameter is empty when you set RoleType to cluster.
        self.namespace = namespace  # type: str
        # Specifies the predefined role that you want to assign. Valid values:
        # 
        # *   admin: the administrator role.
        # *   dev: the developer role.
        # 
        # This parameter is required.
        self.role_name = role_name  # type: str
        # The authorization type. Valid values:
        # 
        # *   cluster: specifies that the permissions are scoped to a master instance.
        # *   namespace: specifies that the permissions are scoped to a namespace of a cluster.
        # 
        # This parameter is required.
        self.role_type = role_type  # type: str
        # The ID of the RAM user.
        # 
        # This parameter is required.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserPermissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateUserPermissionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserPermissionResponseBody, self).to_map()
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


class UpdateUserPermissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateUserPermissionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserPermissionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateUserPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


