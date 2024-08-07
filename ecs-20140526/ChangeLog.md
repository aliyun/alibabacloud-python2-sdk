2024-04-24 Version: 4.1.2
- Update API DescribeInstanceTypes: update response param.


2024-04-12 Version: 4.1.1
- Update API DescribeDedicatedHosts: add param MaxResults.
- Update API DescribeDedicatedHosts: add param NextToken.
- Update API DescribeDedicatedHosts: update response param.
- Update API DescribeInstanceTypes: add param CpuArchitectures.
- Update API DescribeInstanceTypes: add param GpuSpecs.
- Update API DescribeInstanceTypes: add param InstanceCategories.
- Update API DescribeInstanceTypes: add param InstanceTypeFamilies.
- Update API DescribeInstanceTypes: add param LocalStorageCategories.
- Update API DescribeInstanceTypes: add param PhysicalProcessorModels.
- Update API DescribeInstanceTypes: update param InstanceCategory.
- Update API DescribeInstanceTypes: update response param.
- Update API InvokeCommand: update param InstanceId.
- Update API RunCommand: update param InstanceId.


2024-04-10 Version: 4.1.0
- Support API DescribeCloudAssistantSettings.
- Support API DescribeTerminalSessions.
- Support API ModifyCloudAssistantSettings.


2024-04-10 Version: 4.0.4
- Update API DescribeAvailableResource: update param SpotDuration.
- Update API ImportImage: add param StorageLocationArn.
- Update API ImportImage: update response param.


2024-03-12 Version: 4.0.3
- Update API CreateAutoProvisioningGroup: add param Tag.
- Update API CreateAutoSnapshotPolicy: add param CopyEncryptionConfiguration.
- Update API CreateAutoSnapshotPolicy: update response param.
- Update API DescribeAutoProvisioningGroups: add param Tag.
- Update API DescribeAutoProvisioningGroups: update response param.
- Update API DescribeAutoSnapshotPolicyEx: update response param.
- Update API ModifyAutoSnapshotPolicyEx: add param CopyEncryptionConfiguration.
- Update API RunInstances: update param NetworkInterface.
- Update API StartTerminalSession: add param Username.


2024-02-29 Version: 4.0.2
- Update API CreateAutoProvisioningGroup: add param Tag.
- Update API CreateAutoSnapshotPolicy: add param CopyEncryptionConfiguration.
- Update API CreateAutoSnapshotPolicy: update response param.
- Update API DescribeAutoProvisioningGroups: add param Tag.
- Update API DescribeAutoProvisioningGroups: update response param.
- Update API DescribeAutoSnapshotPolicyEx: update response param.
- Update API ModifyAutoSnapshotPolicyEx: add param CopyEncryptionConfiguration.
- Update API RunInstances: update param NetworkInterface.


2024-02-28 Version: 4.0.1
- Update API CreateAutoSnapshotPolicy: add param CopyEncryptionConfiguration.
- Update API CreateAutoSnapshotPolicy: update response param.
- Update API DescribeAutoSnapshotPolicyEx: update response param.
- Update API ModifyAutoSnapshotPolicyEx: add param CopyEncryptionConfiguration.
- Update API RunInstances: update param NetworkInterface.


2024-02-02 Version: 4.0.0
- Support API CreateSavingsPlan.
- Support API DescribeSavingsPlanEstimation.
- Support API DescribeSavingsPlanPrice.
- Support API ModifyInvocationAttribute.
- Delete API DescribeInstanceVncPasswd.
- Delete API ImportSnapshot.
- Update API AuthorizeSecurityGroupupdate Description param.
update DestCidrIp param.
update IpProtocol param.
update Ipv6DestCidrIp param.
update Ipv6SourceCidrIp param.
update NicType param.
update Policy param.
update PortRange param.
update Priority param.
update SourceCidrIp param.
update SourceGroupId param.
update SourceGroupOwnerAccount param.
update SourceGroupOwnerId param.
update SourcePortRange param.
update SourcePrefixListId param.
- Update API AuthorizeSecurityGroupEgressupdate Description param.
update DestCidrIp param.
update DestGroupId param.
update DestGroupOwnerAccount param.
update DestGroupOwnerId param.
update DestPrefixListId param.
update IpProtocol param.
update Ipv6DestCidrIp param.
update Ipv6SourceCidrIp param.
update NicType param.
update Policy param.
update PortRange param.
update Priority param.
update SourceCidrIp param.
update SourcePortRange param.
- Update API CreateAutoProvisioningGroupadd LaunchConfiguration.ImageFamily param.
- Update API CreateNetworkInterfaceadd RxQueueSize param.
add TxQueueSize param.
- Update API DeleteAutoProvisioningGroupupdate TerminateInstances param.
- Update API DeleteInstanceadd DryRun param.
- Update API DeleteLaunchTemplateupdate response param.
- Update API DeregisterManagedInstanceupdate response param.
- Update API DescribeActivationsadd MaxResults param.
add NextToken param.
update response param.
- Update API DescribeAutoProvisioningGroupsadd ResourceGroupId param.
update response param.
- Update API DescribeAutoSnapshotPolicyExupdate response param.
- Update API DescribeBandwidthLimitationupdate RegionId param.
- Update API DescribeCapacityReservationsupdate response param.
- Update API DescribeCloudAssistantStatusadd MaxResults param.
add NextToken param.
update response param.
- Update API DescribeCommandsadd MaxResults param.
add NextToken param.
update response param.
- Update API DescribeDisksupdate response param.
- Update API DescribeInstanceTypesupdate response param.
- Update API DescribeInstancesupdate response param.
- Update API DescribeInvocationResultsadd MaxResults param.
add NextToken param.
update response param.
- Update API DescribeInvocationsadd MaxResults param.
add NextToken param.
update response param.
- Update API DescribeKeyPairsadd IncludePublicKey param.
update response param.
- Update API DescribeManagedInstancesadd MaxResults param.
add NextToken param.
add ResourceGroupId param.
update response param.
- Update API DescribeNetworkInterfaceAttributeupdate response param.
- Update API DescribeNetworkInterfacesupdate PageNumber param.
update PageSize param.
- Update API DescribeSecurityGroupsadd ServiceManaged param.
- Update API DescribeSendFileResultsadd MaxResults param.
add NextToken param.
update response param.
- Update API DescribeSnapshotsupdate response param.
- Update API InvokeCommandadd ResourceTag param.
update InstanceId param.
- Update API JoinResourceGroupupdate response param.
- Update API ListPluginStatusadd MaxResults param.
add NextToken param.
update response param.
- Update API ModifyInstanceAttributeadd CpuOptions.TopologyType param.
- Update API ModifyInstanceSpecadd DryRun param.
- Update API ModifyNetworkInterfaceAttributeadd RxQueueSize param.
add TxQueueSize param.
- Update API RevokeSecurityGroupupdate Description param.
update DestCidrIp param.
update IpProtocol param.
update Ipv6DestCidrIp param.
update Ipv6SourceCidrIp param.
update NicType param.
update Policy param.
update PortRange param.
update Priority param.
update SourceCidrIp param.
update SourceGroupId param.
update SourceGroupOwnerAccount param.
update SourceGroupOwnerId param.
update SourcePortRange param.
update SourcePrefixListId param.
- Update API RevokeSecurityGroupEgressupdate Description param.
update DestCidrIp param.
update DestGroupId param.
update DestGroupOwnerAccount param.
update DestGroupOwnerId param.
update DestPrefixListId param.
update IpProtocol param.
update Ipv6DestCidrIp param.
update Ipv6SourceCidrIp param.
update NicType param.
update Policy param.
update PortRange param.
update Priority param.
update SourceCidrIp param.
update SourcePortRange param.
- Update API RunCommandadd ResourceTag param.
update InstanceId param.
- Update API RunInstancesadd CpuOptions.TopologyType param.
update NetworkInterface param.


2023-10-24 Version: 3.0.15
- Generated python2 2014-05-26 for Ecs.

2023-10-18 Version: 3.0.14
- Generated python2 2014-05-26 for Ecs.

2023-10-16 Version: 3.0.13
- Generated python2 2014-05-26 for Ecs.

2023-10-09 Version: 3.0.12
- Generated python2 2014-05-26 for Ecs.

2023-09-19 Version: 3.0.11
- Generated python2 2014-05-26 for Ecs.

2023-09-18 Version: 3.0.10
- Generated python2 2014-05-26 for Ecs.

2023-08-09 Version: 3.0.9
- Generated python2 2014-05-26 for Ecs.

2023-05-25 Version: 3.0.8
- DescribeDemands add PrivatePoolId.

2023-04-17 Version: 3.0.7
- Add ModifyDiskDeployment.

2023-03-28 Version: 3.0.6
- Change visibility of param ActionType in DescribeImageSupportInstanceTypes.

2023-03-27 Version: 3.0.5
- Suppoort jumbo frame.

2023-02-13 Version: 3.0.4
- Support TagPolicy Verify NoTag.
- Fixed bugs for DescribeDemands error code.
- Add encrypted disk ErrorCode.
- DescribeDedicatedHosts supports SocketDetails param to check socket capacities of specified dedicated hosts.

2023-02-06 Version: 3.0.3
- Add OpenAPI DescribeReservedInstanceAutoRenewAttribute, ModifyReservedInstanceAutoRenewAttribute.

2023-01-11 Version: 3.0.2
- Add error code for ModifyInstanceNetworkSpec.
- Add invalid account buying spot error code.
- Support ip prefix for eni.
- Update the StorageLocationArn to private.
- Security Group Rule support rule id.

2022-10-14 Version: 3.0.1
- Add GPUMemorySize to DescribeInstanceTypes api.

2022-09-27 Version: 3.0.0
- Modify Size type form int32 to int64 of `DescribePriceRequest` `DataDisk` param.

2022-04-27 Version: 2.1.1
- Support systemdisk encrypt and arns.

2021-08-27 Version: 1.1.0
- DescribeSecurityGroups support query by next token.

2021-03-22 Version: 1.0.0
- Generated python2 2014-05-26 for Ecs.

