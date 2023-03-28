# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ChangeResourceGroupRequest(TeaModel):
    def __init__(self, resource_group_id=None, resource_id=None, resource_region_id=None):
        self.resource_group_id = resource_group_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_region_id = resource_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class CreateClusterRequestComponentsComponentConfig(TeaModel):
    def __init__(self, basic_args=None, node_units=None):
        self.basic_args = basic_args  # type: any
        self.node_units = node_units  # type: list[any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequestComponentsComponentConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_args is not None:
            result['BasicArgs'] = self.basic_args
        if self.node_units is not None:
            result['NodeUnits'] = self.node_units
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BasicArgs') is not None:
            self.basic_args = m.get('BasicArgs')
        if m.get('NodeUnits') is not None:
            self.node_units = m.get('NodeUnits')
        return self


class CreateClusterRequestComponents(TeaModel):
    def __init__(self, component_config=None, component_type=None):
        self.component_config = component_config  # type: CreateClusterRequestComponentsComponentConfig
        self.component_type = component_type  # type: str

    def validate(self):
        if self.component_config:
            self.component_config.validate()

    def to_map(self):
        _map = super(CreateClusterRequestComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_config is not None:
            result['ComponentConfig'] = self.component_config.to_map()
        if self.component_type is not None:
            result['ComponentType'] = self.component_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentConfig') is not None:
            temp_model = CreateClusterRequestComponentsComponentConfig()
            self.component_config = temp_model.from_map(m['ComponentConfig'])
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')
        return self


class CreateClusterRequestNetworksIpAllocationPolicyBondPolicyBonds(TeaModel):
    def __init__(self, name=None, subnet=None):
        self.name = name  # type: str
        self.subnet = subnet  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequestNetworksIpAllocationPolicyBondPolicyBonds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.subnet is not None:
            result['Subnet'] = self.subnet
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Subnet') is not None:
            self.subnet = m.get('Subnet')
        return self


class CreateClusterRequestNetworksIpAllocationPolicyBondPolicy(TeaModel):
    def __init__(self, bond_default_subnet=None, bonds=None):
        self.bond_default_subnet = bond_default_subnet  # type: str
        self.bonds = bonds  # type: list[CreateClusterRequestNetworksIpAllocationPolicyBondPolicyBonds]

    def validate(self):
        if self.bonds:
            for k in self.bonds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateClusterRequestNetworksIpAllocationPolicyBondPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond_default_subnet is not None:
            result['BondDefaultSubnet'] = self.bond_default_subnet
        result['Bonds'] = []
        if self.bonds is not None:
            for k in self.bonds:
                result['Bonds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BondDefaultSubnet') is not None:
            self.bond_default_subnet = m.get('BondDefaultSubnet')
        self.bonds = []
        if m.get('Bonds') is not None:
            for k in m.get('Bonds'):
                temp_model = CreateClusterRequestNetworksIpAllocationPolicyBondPolicyBonds()
                self.bonds.append(temp_model.from_map(k))
        return self


class CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicyBonds(TeaModel):
    def __init__(self, name=None, subnet=None):
        self.name = name  # type: str
        self.subnet = subnet  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicyBonds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.subnet is not None:
            result['Subnet'] = self.subnet
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Subnet') is not None:
            self.subnet = m.get('Subnet')
        return self


class CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicy(TeaModel):
    def __init__(self, bonds=None, machine_type=None):
        self.bonds = bonds  # type: list[CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicyBonds]
        self.machine_type = machine_type  # type: str

    def validate(self):
        if self.bonds:
            for k in self.bonds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bonds'] = []
        if self.bonds is not None:
            for k in self.bonds:
                result['Bonds'].append(k.to_map() if k else None)
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bonds = []
        if m.get('Bonds') is not None:
            for k in m.get('Bonds'):
                temp_model = CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicyBonds()
                self.bonds.append(temp_model.from_map(k))
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        return self


class CreateClusterRequestNetworksIpAllocationPolicyNodePolicyBonds(TeaModel):
    def __init__(self, name=None, subnet=None):
        self.name = name  # type: str
        self.subnet = subnet  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequestNetworksIpAllocationPolicyNodePolicyBonds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.subnet is not None:
            result['Subnet'] = self.subnet
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Subnet') is not None:
            self.subnet = m.get('Subnet')
        return self


class CreateClusterRequestNetworksIpAllocationPolicyNodePolicy(TeaModel):
    def __init__(self, bonds=None, node_id=None):
        self.bonds = bonds  # type: list[CreateClusterRequestNetworksIpAllocationPolicyNodePolicyBonds]
        self.node_id = node_id  # type: str

    def validate(self):
        if self.bonds:
            for k in self.bonds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateClusterRequestNetworksIpAllocationPolicyNodePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bonds'] = []
        if self.bonds is not None:
            for k in self.bonds:
                result['Bonds'].append(k.to_map() if k else None)
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bonds = []
        if m.get('Bonds') is not None:
            for k in m.get('Bonds'):
                temp_model = CreateClusterRequestNetworksIpAllocationPolicyNodePolicyBonds()
                self.bonds.append(temp_model.from_map(k))
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class CreateClusterRequestNetworksIpAllocationPolicy(TeaModel):
    def __init__(self, bond_policy=None, machine_type_policy=None, node_policy=None):
        self.bond_policy = bond_policy  # type: CreateClusterRequestNetworksIpAllocationPolicyBondPolicy
        self.machine_type_policy = machine_type_policy  # type: list[CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicy]
        self.node_policy = node_policy  # type: list[CreateClusterRequestNetworksIpAllocationPolicyNodePolicy]

    def validate(self):
        if self.bond_policy:
            self.bond_policy.validate()
        if self.machine_type_policy:
            for k in self.machine_type_policy:
                if k:
                    k.validate()
        if self.node_policy:
            for k in self.node_policy:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateClusterRequestNetworksIpAllocationPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond_policy is not None:
            result['BondPolicy'] = self.bond_policy.to_map()
        result['MachineTypePolicy'] = []
        if self.machine_type_policy is not None:
            for k in self.machine_type_policy:
                result['MachineTypePolicy'].append(k.to_map() if k else None)
        result['NodePolicy'] = []
        if self.node_policy is not None:
            for k in self.node_policy:
                result['NodePolicy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BondPolicy') is not None:
            temp_model = CreateClusterRequestNetworksIpAllocationPolicyBondPolicy()
            self.bond_policy = temp_model.from_map(m['BondPolicy'])
        self.machine_type_policy = []
        if m.get('MachineTypePolicy') is not None:
            for k in m.get('MachineTypePolicy'):
                temp_model = CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicy()
                self.machine_type_policy.append(temp_model.from_map(k))
        self.node_policy = []
        if m.get('NodePolicy') is not None:
            for k in m.get('NodePolicy'):
                temp_model = CreateClusterRequestNetworksIpAllocationPolicyNodePolicy()
                self.node_policy.append(temp_model.from_map(k))
        return self


class CreateClusterRequestNetworksNewVpdInfoVpdSubnets(TeaModel):
    def __init__(self, subnet_cidr=None, subnet_type=None, zone_id=None):
        self.subnet_cidr = subnet_cidr  # type: str
        self.subnet_type = subnet_type  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequestNetworksNewVpdInfoVpdSubnets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subnet_cidr is not None:
            result['SubnetCidr'] = self.subnet_cidr
        if self.subnet_type is not None:
            result['SubnetType'] = self.subnet_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubnetCidr') is not None:
            self.subnet_cidr = m.get('SubnetCidr')
        if m.get('SubnetType') is not None:
            self.subnet_type = m.get('SubnetType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateClusterRequestNetworksNewVpdInfo(TeaModel):
    def __init__(self, cen_id=None, cloud_link_cidr=None, cloud_link_id=None, monitor_vpc_id=None,
                 monitor_vswitch_id=None, vpd_cidr=None, vpd_subnets=None):
        self.cen_id = cen_id  # type: str
        self.cloud_link_cidr = cloud_link_cidr  # type: str
        self.cloud_link_id = cloud_link_id  # type: str
        self.monitor_vpc_id = monitor_vpc_id  # type: str
        self.monitor_vswitch_id = monitor_vswitch_id  # type: str
        self.vpd_cidr = vpd_cidr  # type: str
        self.vpd_subnets = vpd_subnets  # type: list[CreateClusterRequestNetworksNewVpdInfoVpdSubnets]

    def validate(self):
        if self.vpd_subnets:
            for k in self.vpd_subnets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateClusterRequestNetworksNewVpdInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cloud_link_cidr is not None:
            result['CloudLinkCidr'] = self.cloud_link_cidr
        if self.cloud_link_id is not None:
            result['CloudLinkId'] = self.cloud_link_id
        if self.monitor_vpc_id is not None:
            result['MonitorVpcId'] = self.monitor_vpc_id
        if self.monitor_vswitch_id is not None:
            result['MonitorVswitchId'] = self.monitor_vswitch_id
        if self.vpd_cidr is not None:
            result['VpdCidr'] = self.vpd_cidr
        result['VpdSubnets'] = []
        if self.vpd_subnets is not None:
            for k in self.vpd_subnets:
                result['VpdSubnets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CloudLinkCidr') is not None:
            self.cloud_link_cidr = m.get('CloudLinkCidr')
        if m.get('CloudLinkId') is not None:
            self.cloud_link_id = m.get('CloudLinkId')
        if m.get('MonitorVpcId') is not None:
            self.monitor_vpc_id = m.get('MonitorVpcId')
        if m.get('MonitorVswitchId') is not None:
            self.monitor_vswitch_id = m.get('MonitorVswitchId')
        if m.get('VpdCidr') is not None:
            self.vpd_cidr = m.get('VpdCidr')
        self.vpd_subnets = []
        if m.get('VpdSubnets') is not None:
            for k in m.get('VpdSubnets'):
                temp_model = CreateClusterRequestNetworksNewVpdInfoVpdSubnets()
                self.vpd_subnets.append(temp_model.from_map(k))
        return self


class CreateClusterRequestNetworksVpdInfo(TeaModel):
    def __init__(self, vpd_id=None, vpd_subnets=None):
        self.vpd_id = vpd_id  # type: str
        self.vpd_subnets = vpd_subnets  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequestNetworksVpdInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        if self.vpd_subnets is not None:
            result['VpdSubnets'] = self.vpd_subnets
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        if m.get('VpdSubnets') is not None:
            self.vpd_subnets = m.get('VpdSubnets')
        return self


class CreateClusterRequestNetworks(TeaModel):
    def __init__(self, ip_allocation_policy=None, new_vpd_info=None, vpd_info=None):
        self.ip_allocation_policy = ip_allocation_policy  # type: list[CreateClusterRequestNetworksIpAllocationPolicy]
        self.new_vpd_info = new_vpd_info  # type: CreateClusterRequestNetworksNewVpdInfo
        self.vpd_info = vpd_info  # type: CreateClusterRequestNetworksVpdInfo

    def validate(self):
        if self.ip_allocation_policy:
            for k in self.ip_allocation_policy:
                if k:
                    k.validate()
        if self.new_vpd_info:
            self.new_vpd_info.validate()
        if self.vpd_info:
            self.vpd_info.validate()

    def to_map(self):
        _map = super(CreateClusterRequestNetworks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpAllocationPolicy'] = []
        if self.ip_allocation_policy is not None:
            for k in self.ip_allocation_policy:
                result['IpAllocationPolicy'].append(k.to_map() if k else None)
        if self.new_vpd_info is not None:
            result['NewVpdInfo'] = self.new_vpd_info.to_map()
        if self.vpd_info is not None:
            result['VpdInfo'] = self.vpd_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ip_allocation_policy = []
        if m.get('IpAllocationPolicy') is not None:
            for k in m.get('IpAllocationPolicy'):
                temp_model = CreateClusterRequestNetworksIpAllocationPolicy()
                self.ip_allocation_policy.append(temp_model.from_map(k))
        if m.get('NewVpdInfo') is not None:
            temp_model = CreateClusterRequestNetworksNewVpdInfo()
            self.new_vpd_info = temp_model.from_map(m['NewVpdInfo'])
        if m.get('VpdInfo') is not None:
            temp_model = CreateClusterRequestNetworksVpdInfo()
            self.vpd_info = temp_model.from_map(m['VpdInfo'])
        return self


class CreateClusterRequestNodeGroupsNodes(TeaModel):
    def __init__(self, hostname=None, login_password=None, node_id=None):
        self.hostname = hostname  # type: str
        self.login_password = login_password  # type: str
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequestNodeGroupsNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.login_password is not None:
            result['LoginPassword'] = self.login_password
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class CreateClusterRequestNodeGroups(TeaModel):
    def __init__(self, image_id=None, machine_type=None, node_group_description=None, node_group_name=None,
                 nodes=None, zone_id=None):
        self.image_id = image_id  # type: str
        self.machine_type = machine_type  # type: str
        self.node_group_description = node_group_description  # type: str
        self.node_group_name = node_group_name  # type: str
        self.nodes = nodes  # type: list[CreateClusterRequestNodeGroupsNodes]
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateClusterRequestNodeGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        if self.node_group_description is not None:
            result['NodeGroupDescription'] = self.node_group_description
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('NodeGroupDescription') is not None:
            self.node_group_description = m.get('NodeGroupDescription')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = CreateClusterRequestNodeGroupsNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateClusterRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequestTag, self).to_map()
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


class CreateClusterRequest(TeaModel):
    def __init__(self, cluster_description=None, cluster_name=None, cluster_type=None, components=None,
                 ignore_failed_node_tasks=None, networks=None, node_groups=None, resource_group_id=None, tag=None):
        self.cluster_description = cluster_description  # type: str
        self.cluster_name = cluster_name  # type: str
        self.cluster_type = cluster_type  # type: str
        self.components = components  # type: list[CreateClusterRequestComponents]
        self.ignore_failed_node_tasks = ignore_failed_node_tasks  # type: bool
        self.networks = networks  # type: CreateClusterRequestNetworks
        self.node_groups = node_groups  # type: list[CreateClusterRequestNodeGroups]
        self.resource_group_id = resource_group_id  # type: str
        self.tag = tag  # type: list[CreateClusterRequestTag]

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()
        if self.networks:
            self.networks.validate()
        if self.node_groups:
            for k in self.node_groups:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        if self.networks is not None:
            result['Networks'] = self.networks.to_map()
        result['NodeGroups'] = []
        if self.node_groups is not None:
            for k in self.node_groups:
                result['NodeGroups'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = CreateClusterRequestComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        if m.get('Networks') is not None:
            temp_model = CreateClusterRequestNetworks()
            self.networks = temp_model.from_map(m['Networks'])
        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k in m.get('NodeGroups'):
                temp_model = CreateClusterRequestNodeGroups()
                self.node_groups.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateClusterRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateClusterShrinkRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterShrinkRequestTag, self).to_map()
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


class CreateClusterShrinkRequest(TeaModel):
    def __init__(self, cluster_description=None, cluster_name=None, cluster_type=None, components_shrink=None,
                 ignore_failed_node_tasks=None, networks_shrink=None, node_groups_shrink=None, resource_group_id=None, tag=None):
        self.cluster_description = cluster_description  # type: str
        self.cluster_name = cluster_name  # type: str
        self.cluster_type = cluster_type  # type: str
        self.components_shrink = components_shrink  # type: str
        self.ignore_failed_node_tasks = ignore_failed_node_tasks  # type: bool
        self.networks_shrink = networks_shrink  # type: str
        self.node_groups_shrink = node_groups_shrink  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.tag = tag  # type: list[CreateClusterShrinkRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateClusterShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.components_shrink is not None:
            result['Components'] = self.components_shrink
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        if self.networks_shrink is not None:
            result['Networks'] = self.networks_shrink
        if self.node_groups_shrink is not None:
            result['NodeGroups'] = self.node_groups_shrink
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Components') is not None:
            self.components_shrink = m.get('Components')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        if m.get('Networks') is not None:
            self.networks_shrink = m.get('Networks')
        if m.get('NodeGroups') is not None:
            self.node_groups_shrink = m.get('NodeGroups')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateClusterShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None, task_id=None):
        self.cluster_id = cluster_id  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

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


class DeleteClusterRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteClusterRequest, self).to_map()
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


class DescribeClusterResponseBodyComponents(TeaModel):
    def __init__(self, component_id=None, component_type=None):
        self.component_id = component_id  # type: str
        self.component_type = component_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterResponseBodyComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_id is not None:
            result['ComponentId'] = self.component_id
        if self.component_type is not None:
            result['ComponentType'] = self.component_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')
        return self


class DescribeClusterResponseBodyNetworks(TeaModel):
    def __init__(self, vpd_id=None):
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterResponseBodyNetworks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class DescribeClusterResponseBody(TeaModel):
    def __init__(self, cluster_description=None, cluster_id=None, cluster_name=None, cluster_type=None,
                 components=None, create_time=None, networks=None, node_count=None, node_group_count=None,
                 operating_state=None, request_id=None, resource_group_id=None, task_id=None, update_time=None):
        self.cluster_description = cluster_description  # type: str
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.cluster_type = cluster_type  # type: str
        self.components = components  # type: list[DescribeClusterResponseBodyComponents]
        self.create_time = create_time  # type: str
        self.networks = networks  # type: list[DescribeClusterResponseBodyNetworks]
        self.node_count = node_count  # type: long
        self.node_group_count = node_group_count  # type: long
        self.operating_state = operating_state  # type: str
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.task_id = task_id  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()
        if self.networks:
            for k in self.networks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['Networks'] = []
        if self.networks is not None:
            for k in self.networks:
                result['Networks'].append(k.to_map() if k else None)
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_group_count is not None:
            result['NodeGroupCount'] = self.node_group_count
        if self.operating_state is not None:
            result['OperatingState'] = self.operating_state
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = DescribeClusterResponseBodyComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.networks = []
        if m.get('Networks') is not None:
            for k in m.get('Networks'):
                temp_model = DescribeClusterResponseBodyNetworks()
                self.networks.append(temp_model.from_map(k))
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeGroupCount') is not None:
            self.node_group_count = m.get('NodeGroupCount')
        if m.get('OperatingState') is not None:
            self.operating_state = m.get('OperatingState')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
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


class DescribeNodeRequest(TeaModel):
    def __init__(self, node_id=None):
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeNodeResponseBodyNetworks(TeaModel):
    def __init__(self, bond_name=None, ip=None, subnet_id=None, vpd_id=None):
        self.bond_name = bond_name  # type: str
        self.ip = ip  # type: str
        self.subnet_id = subnet_id  # type: str
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNodeResponseBodyNetworks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond_name is not None:
            result['BondName'] = self.bond_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BondName') is not None:
            self.bond_name = m.get('BondName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class DescribeNodeResponseBody(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, create_time=None, expired_time=None, hostname=None,
                 image_id=None, machine_type=None, networks=None, node_group_id=None, node_group_name=None, node_id=None,
                 operating_state=None, request_id=None, sn=None, zone_id=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.create_time = create_time  # type: str
        self.expired_time = expired_time  # type: str
        self.hostname = hostname  # type: str
        self.image_id = image_id  # type: str
        self.machine_type = machine_type  # type: str
        self.networks = networks  # type: list[DescribeNodeResponseBodyNetworks]
        self.node_group_id = node_group_id  # type: str
        self.node_group_name = node_group_name  # type: str
        self.node_id = node_id  # type: str
        self.operating_state = operating_state  # type: str
        self.request_id = request_id  # type: str
        self.sn = sn  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.networks:
            for k in self.networks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeNodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        result['Networks'] = []
        if self.networks is not None:
            for k in self.networks:
                result['Networks'].append(k.to_map() if k else None)
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.operating_state is not None:
            result['OperatingState'] = self.operating_state
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        self.networks = []
        if m.get('Networks') is not None:
            for k in m.get('Networks'):
                temp_model = DescribeNodeResponseBodyNetworks()
                self.networks.append(temp_model.from_map(k))
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OperatingState') is not None:
            self.operating_state = m.get('OperatingState')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeNodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None):
        self.accept_language = accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        self.local_name = local_name  # type: str
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
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class DescribeTaskRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTaskResponseBodyStepsSubTasks(TeaModel):
    def __init__(self, create_time=None, message=None, task_id=None, task_state=None, task_type=None,
                 update_time=None):
        self.create_time = create_time  # type: str
        self.message = message  # type: str
        self.task_id = task_id  # type: str
        self.task_state = task_state  # type: str
        self.task_type = task_type  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeTaskResponseBodyStepsSubTasks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.message is not None:
            result['Message'] = self.message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeTaskResponseBodySteps(TeaModel):
    def __init__(self, message=None, stage_tag=None, start_time=None, step_name=None, step_state=None,
                 step_type=None, sub_tasks=None, update_time=None):
        self.message = message  # type: str
        self.stage_tag = stage_tag  # type: str
        self.start_time = start_time  # type: str
        self.step_name = step_name  # type: str
        self.step_state = step_state  # type: str
        self.step_type = step_type  # type: str
        self.sub_tasks = sub_tasks  # type: list[DescribeTaskResponseBodyStepsSubTasks]
        self.update_time = update_time  # type: str

    def validate(self):
        if self.sub_tasks:
            for k in self.sub_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTaskResponseBodySteps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.stage_tag is not None:
            result['StageTag'] = self.stage_tag
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.step_name is not None:
            result['StepName'] = self.step_name
        if self.step_state is not None:
            result['StepState'] = self.step_state
        if self.step_type is not None:
            result['StepType'] = self.step_type
        result['SubTasks'] = []
        if self.sub_tasks is not None:
            for k in self.sub_tasks:
                result['SubTasks'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('StageTag') is not None:
            self.stage_tag = m.get('StageTag')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')
        if m.get('StepState') is not None:
            self.step_state = m.get('StepState')
        if m.get('StepType') is not None:
            self.step_type = m.get('StepType')
        self.sub_tasks = []
        if m.get('SubTasks') is not None:
            for k in m.get('SubTasks'):
                temp_model = DescribeTaskResponseBodyStepsSubTasks()
                self.sub_tasks.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeTaskResponseBody(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, create_time=None, message=None, request_id=None,
                 steps=None, task_state=None, task_type=None, update_time=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.create_time = create_time  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.steps = steps  # type: list[DescribeTaskResponseBodySteps]
        self.task_state = task_state  # type: str
        self.task_type = task_type  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        if self.steps:
            for k in self.steps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Steps'] = []
        if self.steps is not None:
            for k in self.steps:
                result['Steps'].append(k.to_map() if k else None)
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.steps = []
        if m.get('Steps') is not None:
            for k in m.get('Steps'):
                temp_model = DescribeTaskResponseBodySteps()
                self.steps.append(temp_model.from_map(k))
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(self, accept_language=None):
        self.accept_language = accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(self, local_name=None, zone_id=None):
        self.local_name = local_name  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeZonesResponseBodyZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtendClusterRequestIpAllocationPolicyBondPolicyBonds(TeaModel):
    def __init__(self, name=None, subnet=None):
        self.name = name  # type: str
        self.subnet = subnet  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtendClusterRequestIpAllocationPolicyBondPolicyBonds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.subnet is not None:
            result['Subnet'] = self.subnet
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Subnet') is not None:
            self.subnet = m.get('Subnet')
        return self


class ExtendClusterRequestIpAllocationPolicyBondPolicy(TeaModel):
    def __init__(self, bond_default_subnet=None, bonds=None):
        self.bond_default_subnet = bond_default_subnet  # type: str
        self.bonds = bonds  # type: list[ExtendClusterRequestIpAllocationPolicyBondPolicyBonds]

    def validate(self):
        if self.bonds:
            for k in self.bonds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ExtendClusterRequestIpAllocationPolicyBondPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond_default_subnet is not None:
            result['BondDefaultSubnet'] = self.bond_default_subnet
        result['Bonds'] = []
        if self.bonds is not None:
            for k in self.bonds:
                result['Bonds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BondDefaultSubnet') is not None:
            self.bond_default_subnet = m.get('BondDefaultSubnet')
        self.bonds = []
        if m.get('Bonds') is not None:
            for k in m.get('Bonds'):
                temp_model = ExtendClusterRequestIpAllocationPolicyBondPolicyBonds()
                self.bonds.append(temp_model.from_map(k))
        return self


class ExtendClusterRequestIpAllocationPolicyMachineTypePolicyBonds(TeaModel):
    def __init__(self, name=None, subnet=None):
        self.name = name  # type: str
        self.subnet = subnet  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtendClusterRequestIpAllocationPolicyMachineTypePolicyBonds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.subnet is not None:
            result['Subnet'] = self.subnet
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Subnet') is not None:
            self.subnet = m.get('Subnet')
        return self


class ExtendClusterRequestIpAllocationPolicyMachineTypePolicy(TeaModel):
    def __init__(self, bonds=None, machine_type=None):
        self.bonds = bonds  # type: list[ExtendClusterRequestIpAllocationPolicyMachineTypePolicyBonds]
        self.machine_type = machine_type  # type: str

    def validate(self):
        if self.bonds:
            for k in self.bonds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ExtendClusterRequestIpAllocationPolicyMachineTypePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bonds'] = []
        if self.bonds is not None:
            for k in self.bonds:
                result['Bonds'].append(k.to_map() if k else None)
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bonds = []
        if m.get('Bonds') is not None:
            for k in m.get('Bonds'):
                temp_model = ExtendClusterRequestIpAllocationPolicyMachineTypePolicyBonds()
                self.bonds.append(temp_model.from_map(k))
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        return self


class ExtendClusterRequestIpAllocationPolicyNodePolicyBonds(TeaModel):
    def __init__(self, name=None, subnet=None):
        self.name = name  # type: str
        self.subnet = subnet  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtendClusterRequestIpAllocationPolicyNodePolicyBonds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.subnet is not None:
            result['Subnet'] = self.subnet
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Subnet') is not None:
            self.subnet = m.get('Subnet')
        return self


class ExtendClusterRequestIpAllocationPolicyNodePolicy(TeaModel):
    def __init__(self, bonds=None, node_id=None):
        self.bonds = bonds  # type: list[ExtendClusterRequestIpAllocationPolicyNodePolicyBonds]
        self.node_id = node_id  # type: str

    def validate(self):
        if self.bonds:
            for k in self.bonds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ExtendClusterRequestIpAllocationPolicyNodePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bonds'] = []
        if self.bonds is not None:
            for k in self.bonds:
                result['Bonds'].append(k.to_map() if k else None)
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.bonds = []
        if m.get('Bonds') is not None:
            for k in m.get('Bonds'):
                temp_model = ExtendClusterRequestIpAllocationPolicyNodePolicyBonds()
                self.bonds.append(temp_model.from_map(k))
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ExtendClusterRequestIpAllocationPolicy(TeaModel):
    def __init__(self, bond_policy=None, machine_type_policy=None, node_policy=None):
        self.bond_policy = bond_policy  # type: ExtendClusterRequestIpAllocationPolicyBondPolicy
        self.machine_type_policy = machine_type_policy  # type: list[ExtendClusterRequestIpAllocationPolicyMachineTypePolicy]
        self.node_policy = node_policy  # type: list[ExtendClusterRequestIpAllocationPolicyNodePolicy]

    def validate(self):
        if self.bond_policy:
            self.bond_policy.validate()
        if self.machine_type_policy:
            for k in self.machine_type_policy:
                if k:
                    k.validate()
        if self.node_policy:
            for k in self.node_policy:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ExtendClusterRequestIpAllocationPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond_policy is not None:
            result['BondPolicy'] = self.bond_policy.to_map()
        result['MachineTypePolicy'] = []
        if self.machine_type_policy is not None:
            for k in self.machine_type_policy:
                result['MachineTypePolicy'].append(k.to_map() if k else None)
        result['NodePolicy'] = []
        if self.node_policy is not None:
            for k in self.node_policy:
                result['NodePolicy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BondPolicy') is not None:
            temp_model = ExtendClusterRequestIpAllocationPolicyBondPolicy()
            self.bond_policy = temp_model.from_map(m['BondPolicy'])
        self.machine_type_policy = []
        if m.get('MachineTypePolicy') is not None:
            for k in m.get('MachineTypePolicy'):
                temp_model = ExtendClusterRequestIpAllocationPolicyMachineTypePolicy()
                self.machine_type_policy.append(temp_model.from_map(k))
        self.node_policy = []
        if m.get('NodePolicy') is not None:
            for k in m.get('NodePolicy'):
                temp_model = ExtendClusterRequestIpAllocationPolicyNodePolicy()
                self.node_policy.append(temp_model.from_map(k))
        return self


class ExtendClusterRequestNodeGroupsNodes(TeaModel):
    def __init__(self, hostname=None, login_password=None, node_id=None):
        self.hostname = hostname  # type: str
        self.login_password = login_password  # type: str
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtendClusterRequestNodeGroupsNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.login_password is not None:
            result['LoginPassword'] = self.login_password
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ExtendClusterRequestNodeGroups(TeaModel):
    def __init__(self, node_group_id=None, nodes=None):
        self.node_group_id = node_group_id  # type: str
        self.nodes = nodes  # type: list[ExtendClusterRequestNodeGroupsNodes]

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ExtendClusterRequestNodeGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ExtendClusterRequestNodeGroupsNodes()
                self.nodes.append(temp_model.from_map(k))
        return self


class ExtendClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, ignore_failed_node_tasks=None, ip_allocation_policy=None, node_groups=None,
                 vpd_subnets=None):
        self.cluster_id = cluster_id  # type: str
        self.ignore_failed_node_tasks = ignore_failed_node_tasks  # type: bool
        self.ip_allocation_policy = ip_allocation_policy  # type: list[ExtendClusterRequestIpAllocationPolicy]
        self.node_groups = node_groups  # type: list[ExtendClusterRequestNodeGroups]
        self.vpd_subnets = vpd_subnets  # type: list[str]

    def validate(self):
        if self.ip_allocation_policy:
            for k in self.ip_allocation_policy:
                if k:
                    k.validate()
        if self.node_groups:
            for k in self.node_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ExtendClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        result['IpAllocationPolicy'] = []
        if self.ip_allocation_policy is not None:
            for k in self.ip_allocation_policy:
                result['IpAllocationPolicy'].append(k.to_map() if k else None)
        result['NodeGroups'] = []
        if self.node_groups is not None:
            for k in self.node_groups:
                result['NodeGroups'].append(k.to_map() if k else None)
        if self.vpd_subnets is not None:
            result['VpdSubnets'] = self.vpd_subnets
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        self.ip_allocation_policy = []
        if m.get('IpAllocationPolicy') is not None:
            for k in m.get('IpAllocationPolicy'):
                temp_model = ExtendClusterRequestIpAllocationPolicy()
                self.ip_allocation_policy.append(temp_model.from_map(k))
        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k in m.get('NodeGroups'):
                temp_model = ExtendClusterRequestNodeGroups()
                self.node_groups.append(temp_model.from_map(k))
        if m.get('VpdSubnets') is not None:
            self.vpd_subnets = m.get('VpdSubnets')
        return self


class ExtendClusterShrinkRequest(TeaModel):
    def __init__(self, cluster_id=None, ignore_failed_node_tasks=None, ip_allocation_policy_shrink=None,
                 node_groups_shrink=None, vpd_subnets_shrink=None):
        self.cluster_id = cluster_id  # type: str
        self.ignore_failed_node_tasks = ignore_failed_node_tasks  # type: bool
        self.ip_allocation_policy_shrink = ip_allocation_policy_shrink  # type: str
        self.node_groups_shrink = node_groups_shrink  # type: str
        self.vpd_subnets_shrink = vpd_subnets_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtendClusterShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        if self.ip_allocation_policy_shrink is not None:
            result['IpAllocationPolicy'] = self.ip_allocation_policy_shrink
        if self.node_groups_shrink is not None:
            result['NodeGroups'] = self.node_groups_shrink
        if self.vpd_subnets_shrink is not None:
            result['VpdSubnets'] = self.vpd_subnets_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        if m.get('IpAllocationPolicy') is not None:
            self.ip_allocation_policy_shrink = m.get('IpAllocationPolicy')
        if m.get('NodeGroups') is not None:
            self.node_groups_shrink = m.get('NodeGroups')
        if m.get('VpdSubnets') is not None:
            self.vpd_subnets_shrink = m.get('VpdSubnets')
        return self


class ExtendClusterResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtendClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ExtendClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExtendClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExtendClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExtendClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterNodesRequest(TeaModel):
    def __init__(self, cluster_id=None, max_results=None, next_token=None, node_group_id=None):
        self.cluster_id = cluster_id  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.node_group_id = node_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        return self


class ListClusterNodesResponseBodyNodesNetworks(TeaModel):
    def __init__(self, bond_name=None, ip=None, subnet_id=None, vpd_id=None):
        self.bond_name = bond_name  # type: str
        self.ip = ip  # type: str
        self.subnet_id = subnet_id  # type: str
        self.vpd_id = vpd_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClusterNodesResponseBodyNodesNetworks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond_name is not None:
            result['BondName'] = self.bond_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BondName') is not None:
            self.bond_name = m.get('BondName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class ListClusterNodesResponseBodyNodes(TeaModel):
    def __init__(self, create_time=None, expired_time=None, hostname=None, image_id=None, machine_type=None,
                 networks=None, node_group_id=None, node_group_name=None, node_id=None, operating_state=None, sn=None,
                 zone_id=None):
        self.create_time = create_time  # type: str
        self.expired_time = expired_time  # type: str
        self.hostname = hostname  # type: str
        self.image_id = image_id  # type: str
        self.machine_type = machine_type  # type: str
        self.networks = networks  # type: list[ListClusterNodesResponseBodyNodesNetworks]
        self.node_group_id = node_group_id  # type: str
        self.node_group_name = node_group_name  # type: str
        self.node_id = node_id  # type: str
        self.operating_state = operating_state  # type: str
        self.sn = sn  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.networks:
            for k in self.networks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClusterNodesResponseBodyNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        result['Networks'] = []
        if self.networks is not None:
            for k in self.networks:
                result['Networks'].append(k.to_map() if k else None)
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.operating_state is not None:
            result['OperatingState'] = self.operating_state
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        self.networks = []
        if m.get('Networks') is not None:
            for k in m.get('Networks'):
                temp_model = ListClusterNodesResponseBodyNodesNetworks()
                self.networks.append(temp_model.from_map(k))
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OperatingState') is not None:
            self.operating_state = m.get('OperatingState')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListClusterNodesResponseBody(TeaModel):
    def __init__(self, next_token=None, nodes=None, request_id=None):
        self.next_token = next_token  # type: str
        self.nodes = nodes  # type: list[ListClusterNodesResponseBodyNodes]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClusterNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ListClusterNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListClusterNodesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListClusterNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListClusterNodesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListClusterNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, resource_group_id=None):
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListClustersResponseBodyClusters(TeaModel):
    def __init__(self, cluster_description=None, cluster_id=None, cluster_name=None, cluster_type=None,
                 components=None, create_time=None, node_count=None, node_group_count=None, operating_state=None,
                 resource_group_id=None, task_id=None, update_time=None):
        self.cluster_description = cluster_description  # type: str
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.cluster_type = cluster_type  # type: str
        self.components = components  # type: any
        self.create_time = create_time  # type: str
        self.node_count = node_count  # type: long
        self.node_group_count = node_group_count  # type: long
        self.operating_state = operating_state  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.task_id = task_id  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListClustersResponseBodyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.components is not None:
            result['Components'] = self.components
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_group_count is not None:
            result['NodeGroupCount'] = self.node_group_count
        if self.operating_state is not None:
            result['OperatingState'] = self.operating_state
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Components') is not None:
            self.components = m.get('Components')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeGroupCount') is not None:
            self.node_group_count = m.get('NodeGroupCount')
        if m.get('OperatingState') is not None:
            self.operating_state = m.get('OperatingState')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListClustersResponseBody(TeaModel):
    def __init__(self, clusters=None, next_token=None, request_id=None):
        self.clusters = clusters  # type: list[ListClustersResponseBodyClusters]
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = ListClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class ListFreeNodesRequest(TeaModel):
    def __init__(self, machine_type=None, max_results=None, next_token=None):
        self.machine_type = machine_type  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFreeNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListFreeNodesResponseBodyNodes(TeaModel):
    def __init__(self, create_time=None, expired_time=None, machine_type=None, node_id=None, sn=None, zone_id=None):
        self.create_time = create_time  # type: str
        self.expired_time = expired_time  # type: str
        self.machine_type = machine_type  # type: str
        self.node_id = node_id  # type: str
        self.sn = sn  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFreeNodesResponseBodyNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListFreeNodesResponseBody(TeaModel):
    def __init__(self, next_token=None, nodes=None, request_id=None):
        self.next_token = next_token  # type: str
        self.nodes = nodes  # type: list[ListFreeNodesResponseBodyNodes]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFreeNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ListFreeNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFreeNodesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFreeNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFreeNodesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFreeNodesResponseBody()
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
    def __init__(self, next_token=None, region_id=None, resource_id=None, resource_type=None, tag=None):
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
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
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: str
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
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
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


class RebootNodesRequest(TeaModel):
    def __init__(self, cluster_id=None, ignore_failed_node_tasks=None, nodes=None):
        self.cluster_id = cluster_id  # type: str
        self.ignore_failed_node_tasks = ignore_failed_node_tasks  # type: bool
        self.nodes = nodes  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebootNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        return self


class RebootNodesShrinkRequest(TeaModel):
    def __init__(self, cluster_id=None, ignore_failed_node_tasks=None, nodes_shrink=None):
        self.cluster_id = cluster_id  # type: str
        self.ignore_failed_node_tasks = ignore_failed_node_tasks  # type: bool
        self.nodes_shrink = nodes_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebootNodesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        if self.nodes_shrink is not None:
            result['Nodes'] = self.nodes_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        if m.get('Nodes') is not None:
            self.nodes_shrink = m.get('Nodes')
        return self


class RebootNodesResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebootNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RebootNodesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RebootNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RebootNodesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RebootNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReimageNodesRequestNodes(TeaModel):
    def __init__(self, hostname=None, image_id=None, login_password=None, node_id=None):
        self.hostname = hostname  # type: str
        self.image_id = image_id  # type: str
        self.login_password = login_password  # type: str
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReimageNodesRequestNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.login_password is not None:
            result['LoginPassword'] = self.login_password
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ReimageNodesRequest(TeaModel):
    def __init__(self, cluster_id=None, ignore_failed_node_tasks=None, nodes=None):
        self.cluster_id = cluster_id  # type: str
        self.ignore_failed_node_tasks = ignore_failed_node_tasks  # type: bool
        self.nodes = nodes  # type: list[ReimageNodesRequestNodes]

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ReimageNodesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ReimageNodesRequestNodes()
                self.nodes.append(temp_model.from_map(k))
        return self


class ReimageNodesShrinkRequest(TeaModel):
    def __init__(self, cluster_id=None, ignore_failed_node_tasks=None, nodes_shrink=None):
        self.cluster_id = cluster_id  # type: str
        self.ignore_failed_node_tasks = ignore_failed_node_tasks  # type: bool
        self.nodes_shrink = nodes_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReimageNodesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        if self.nodes_shrink is not None:
            result['Nodes'] = self.nodes_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        if m.get('Nodes') is not None:
            self.nodes_shrink = m.get('Nodes')
        return self


class ReimageNodesResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReimageNodesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ReimageNodesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReimageNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReimageNodesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReimageNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ShrinkClusterRequestNodeGroupsNodes(TeaModel):
    def __init__(self, node_id=None):
        self.node_id = node_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ShrinkClusterRequestNodeGroupsNodes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ShrinkClusterRequestNodeGroups(TeaModel):
    def __init__(self, node_group_id=None, nodes=None):
        self.node_group_id = node_group_id  # type: str
        self.nodes = nodes  # type: list[ShrinkClusterRequestNodeGroupsNodes]

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ShrinkClusterRequestNodeGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ShrinkClusterRequestNodeGroupsNodes()
                self.nodes.append(temp_model.from_map(k))
        return self


class ShrinkClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, ignore_failed_node_tasks=None, node_groups=None):
        self.cluster_id = cluster_id  # type: str
        self.ignore_failed_node_tasks = ignore_failed_node_tasks  # type: bool
        self.node_groups = node_groups  # type: list[ShrinkClusterRequestNodeGroups]

    def validate(self):
        if self.node_groups:
            for k in self.node_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ShrinkClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        result['NodeGroups'] = []
        if self.node_groups is not None:
            for k in self.node_groups:
                result['NodeGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k in m.get('NodeGroups'):
                temp_model = ShrinkClusterRequestNodeGroups()
                self.node_groups.append(temp_model.from_map(k))
        return self


class ShrinkClusterShrinkRequest(TeaModel):
    def __init__(self, cluster_id=None, ignore_failed_node_tasks=None, node_groups_shrink=None):
        self.cluster_id = cluster_id  # type: str
        self.ignore_failed_node_tasks = ignore_failed_node_tasks  # type: bool
        self.node_groups_shrink = node_groups_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ShrinkClusterShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        if self.node_groups_shrink is not None:
            result['NodeGroups'] = self.node_groups_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        if m.get('NodeGroups') is not None:
            self.node_groups_shrink = m.get('NodeGroups')
        return self


class ShrinkClusterResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ShrinkClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ShrinkClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ShrinkClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ShrinkClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ShrinkClusterResponseBody()
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
    def __init__(self, region_id=None, resource_id=None, resource_type=None, tag=None):
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
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
        # Id of the request
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


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, region_id=None, resource_id=None, resource_type=None, tag_key=None):
        self.all = all  # type: bool
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
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
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
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


