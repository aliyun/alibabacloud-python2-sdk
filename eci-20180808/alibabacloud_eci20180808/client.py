# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eci20180808 import models as eci_20180808_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('eci', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def commit_container_with_options(self, request, runtime):
        """
        You must specify the Alibaba Cloud Resource Name (ARN) of the RAM role of the Container Registry Enterprise Edition instance to grant the elastic container instance to assume the RAM role to push images.
        

        @param request: CommitContainerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CommitContainerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_registry_info):
            query['AcrRegistryInfo'] = request.acr_registry_info
        if not UtilClient.is_unset(request.arn):
            query['Arn'] = request.arn
        if not UtilClient.is_unset(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not UtilClient.is_unset(request.container_name):
            query['ContainerName'] = request.container_name
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CommitContainer',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.CommitContainerResponse(),
            self.call_api(params, req, runtime)
        )

    def commit_container(self, request):
        """
        You must specify the Alibaba Cloud Resource Name (ARN) of the RAM role of the Container Registry Enterprise Edition instance to grant the elastic container instance to assume the RAM role to push images.
        

        @param request: CommitContainerRequest

        @return: CommitContainerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.commit_container_with_options(request, runtime)

    def copy_data_cache_with_options(self, request, runtime):
        """
        You cannot directly use a DataCache across regions. You can call this operation to copy a DataCache from one region to another region. This operation is suitable for the following scenarios:
        *   If you want to use a DataCache across regions and the DataCache exists in Region A, you can call this operation to quickly copy the DataCache to Region B.
        *   If you directly pull data from a region outside China to a region inside the Chinese mainland when you create a DataCache, the data may be pulled at a slow speed due to network limits. In this case, you can create a DataCache in a region outside the Chinese mainland but inside China, such as the China (Hong Kong) region, and call this operation to copy the data to the region inside the Chinese mainland.
        > The process of copying a DataCache is equivalent to copying a snapshot. You are charged for the traffic generated during the copy process and the storage of the generated DataCache.
        

        @param request: CopyDataCacheRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CopyDataCacheResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_cache_id):
            query['DataCacheId'] = request.data_cache_id
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyDataCache',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.CopyDataCacheResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_data_cache(self, request):
        """
        You cannot directly use a DataCache across regions. You can call this operation to copy a DataCache from one region to another region. This operation is suitable for the following scenarios:
        *   If you want to use a DataCache across regions and the DataCache exists in Region A, you can call this operation to quickly copy the DataCache to Region B.
        *   If you directly pull data from a region outside China to a region inside the Chinese mainland when you create a DataCache, the data may be pulled at a slow speed due to network limits. In this case, you can create a DataCache in a region outside the Chinese mainland but inside China, such as the China (Hong Kong) region, and call this operation to copy the data to the region inside the Chinese mainland.
        > The process of copying a DataCache is equivalent to copying a snapshot. You are charged for the traffic generated during the copy process and the storage of the generated DataCache.
        

        @param request: CopyDataCacheRequest

        @return: CopyDataCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.copy_data_cache_with_options(request, runtime)

    def create_container_group_with_options(self, request, runtime):
        """
        When you call the CreateContainerGroup operation to create an elastic container instance, the system creates a service-linked role named AliyunServiceRoleForECI. This role is used to access other Alibaba Cloud services such as Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). For more information, see [Elastic Container Instance service-linked role](~~212914~~).
        When you create an elastic container instance, you can configure features such as instances, images, and storage based on your business requirements. For information about parameters configured for the features and the description of the parameters, see the following documents:
        **Instances** You can use one of the following methods to create an elastic container instance:
        *   [Specify the number of vCPUs and memory size to create an elastic container instance](~~114662~~)
        *   [Specify ECS instance types to create an elastic container instance](~~114664~~)
        Both the preceding creation methods support the following features:
        *   [Specify CPU options](~~197781~~)
        *   [Create a preemptible elastic container instance](~~157759~~)
        *   [Configure multiple zones](~~157290~~)
        *   [Configure multiple specifications](~~146468~~)
        *   [Use tags to manage elastic container instances](~~146608~~)
        **Images**\
        *   [Configure a container image](~~461311~~)
        *   [Use the image cache feature to accelerate the creation of an elastic container instance](~~141281~~)
        *   [Specify a Container Registry Enterprise Edition instance](~~194250~~)
        *   [Use self-managed image repositories](~~378059~~)
        **Networking**\
        *   [Create and Associate an EIP](~~99146~~)
        *   [Assign a security group](~~176237~~)
        *   [Assign an IPv6 address to an elastic container instance](~~451282~~)
        *   [Configure maximum bandwidth](~~190635~~)
        **Storage**\
        *   [Mount a disk volume](~~144571~~)
        *   [Mount a NAS volume](~~464075~~)
        *   [Mount an OSS bucket to an elastic container instance as a volume](~~464076~~)
        *   [Mount an emptyDir volume](~~464078~~)
        *   [Mount a ConfigFile volume](~~464080~~)
        *   [Increase the size of the temporary storage space](~~204066~~)
        **Container configuration**\
        *   [Configure startup commands and arguments for a container](~~94593~~)
        *   [Use probes to perform health checks on a container](~~99053~~)
        *   [Obtain metadata by using environment variables](~~141788~~)
        *   [Configure a security context for an elastic container instance or a container](~~462313~~)
        *   [Configure the NTP service](~~462768~~)
        **Logging and O\\&M**\
        *   [Use environment variables to configure log collection](~~121973~~)
        *   [Save core files to volumes](~~167801~~)
        

        @param request: CreateContainerGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateContainerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_registry_info):
            query['AcrRegistryInfo'] = request.acr_registry_info
        if not UtilClient.is_unset(request.active_deadline_seconds):
            query['ActiveDeadlineSeconds'] = request.active_deadline_seconds
        if not UtilClient.is_unset(request.auto_create_eip):
            query['AutoCreateEip'] = request.auto_create_eip
        if not UtilClient.is_unset(request.auto_match_image_cache):
            query['AutoMatchImageCache'] = request.auto_match_image_cache
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compute_category):
            query['ComputeCategory'] = request.compute_category
        if not UtilClient.is_unset(request.container):
            query['Container'] = request.container
        if not UtilClient.is_unset(request.container_group_name):
            query['ContainerGroupName'] = request.container_group_name
        if not UtilClient.is_unset(request.container_resource_view):
            query['ContainerResourceView'] = request.container_resource_view
        if not UtilClient.is_unset(request.core_pattern):
            query['CorePattern'] = request.core_pattern
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.cpu_architecture):
            query['CpuArchitecture'] = request.cpu_architecture
        if not UtilClient.is_unset(request.cpu_options_core):
            query['CpuOptionsCore'] = request.cpu_options_core
        if not UtilClient.is_unset(request.cpu_options_numa):
            query['CpuOptionsNuma'] = request.cpu_options_numa
        if not UtilClient.is_unset(request.cpu_options_threads_per_core):
            query['CpuOptionsThreadsPerCore'] = request.cpu_options_threads_per_core
        if not UtilClient.is_unset(request.data_cache_bucket):
            query['DataCacheBucket'] = request.data_cache_bucket
        if not UtilClient.is_unset(request.data_cache_bursting_enabled):
            query['DataCacheBurstingEnabled'] = request.data_cache_bursting_enabled
        if not UtilClient.is_unset(request.data_cache_pl):
            query['DataCachePL'] = request.data_cache_pl
        if not UtilClient.is_unset(request.data_cache_provisioned_iops):
            query['DataCacheProvisionedIops'] = request.data_cache_provisioned_iops
        if not UtilClient.is_unset(request.dns_policy):
            query['DnsPolicy'] = request.dns_policy
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.egress_bandwidth):
            query['EgressBandwidth'] = request.egress_bandwidth
        if not UtilClient.is_unset(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not UtilClient.is_unset(request.eip_common_bandwidth_package):
            query['EipCommonBandwidthPackage'] = request.eip_common_bandwidth_package
        if not UtilClient.is_unset(request.eip_isp):
            query['EipISP'] = request.eip_isp
        if not UtilClient.is_unset(request.eip_instance_id):
            query['EipInstanceId'] = request.eip_instance_id
        if not UtilClient.is_unset(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not UtilClient.is_unset(request.fixed_ip):
            query['FixedIp'] = request.fixed_ip
        if not UtilClient.is_unset(request.fixed_ip_retain_hour):
            query['FixedIpRetainHour'] = request.fixed_ip_retain_hour
        if not UtilClient.is_unset(request.gpu_driver_version):
            query['GpuDriverVersion'] = request.gpu_driver_version
        if not UtilClient.is_unset(request.host_aliase):
            query['HostAliase'] = request.host_aliase
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.image_accelerate_mode):
            query['ImageAccelerateMode'] = request.image_accelerate_mode
        if not UtilClient.is_unset(request.image_registry_credential):
            query['ImageRegistryCredential'] = request.image_registry_credential
        if not UtilClient.is_unset(request.image_snapshot_id):
            query['ImageSnapshotId'] = request.image_snapshot_id
        if not UtilClient.is_unset(request.ingress_bandwidth):
            query['IngressBandwidth'] = request.ingress_bandwidth
        if not UtilClient.is_unset(request.init_container):
            query['InitContainer'] = request.init_container
        if not UtilClient.is_unset(request.insecure_registry):
            query['InsecureRegistry'] = request.insecure_registry
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.ipv_6gateway_bandwidth):
            query['Ipv6GatewayBandwidth'] = request.ipv_6gateway_bandwidth
        if not UtilClient.is_unset(request.ipv_6gateway_bandwidth_enable):
            query['Ipv6GatewayBandwidthEnable'] = request.ipv_6gateway_bandwidth_enable
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.ntp_server):
            query['NtpServer'] = request.ntp_server
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.overhead_reservation_option):
            query['OverheadReservationOption'] = request.overhead_reservation_option
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plain_http_registry):
            query['PlainHttpRegistry'] = request.plain_http_registry
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restart_policy):
            query['RestartPolicy'] = request.restart_policy
        if not UtilClient.is_unset(request.schedule_strategy):
            query['ScheduleStrategy'] = request.schedule_strategy
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.share_process_namespace):
            query['ShareProcessNamespace'] = request.share_process_namespace
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.strict_spot):
            query['StrictSpot'] = request.strict_spot
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.dns_config):
            query['DnsConfig'] = request.dns_config
        if not UtilClient.is_unset(request.host_security_context):
            query['HostSecurityContext'] = request.host_security_context
        if not UtilClient.is_unset(request.security_context):
            query['SecurityContext'] = request.security_context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateContainerGroup',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.CreateContainerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_container_group(self, request):
        """
        When you call the CreateContainerGroup operation to create an elastic container instance, the system creates a service-linked role named AliyunServiceRoleForECI. This role is used to access other Alibaba Cloud services such as Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). For more information, see [Elastic Container Instance service-linked role](~~212914~~).
        When you create an elastic container instance, you can configure features such as instances, images, and storage based on your business requirements. For information about parameters configured for the features and the description of the parameters, see the following documents:
        **Instances** You can use one of the following methods to create an elastic container instance:
        *   [Specify the number of vCPUs and memory size to create an elastic container instance](~~114662~~)
        *   [Specify ECS instance types to create an elastic container instance](~~114664~~)
        Both the preceding creation methods support the following features:
        *   [Specify CPU options](~~197781~~)
        *   [Create a preemptible elastic container instance](~~157759~~)
        *   [Configure multiple zones](~~157290~~)
        *   [Configure multiple specifications](~~146468~~)
        *   [Use tags to manage elastic container instances](~~146608~~)
        **Images**\
        *   [Configure a container image](~~461311~~)
        *   [Use the image cache feature to accelerate the creation of an elastic container instance](~~141281~~)
        *   [Specify a Container Registry Enterprise Edition instance](~~194250~~)
        *   [Use self-managed image repositories](~~378059~~)
        **Networking**\
        *   [Create and Associate an EIP](~~99146~~)
        *   [Assign a security group](~~176237~~)
        *   [Assign an IPv6 address to an elastic container instance](~~451282~~)
        *   [Configure maximum bandwidth](~~190635~~)
        **Storage**\
        *   [Mount a disk volume](~~144571~~)
        *   [Mount a NAS volume](~~464075~~)
        *   [Mount an OSS bucket to an elastic container instance as a volume](~~464076~~)
        *   [Mount an emptyDir volume](~~464078~~)
        *   [Mount a ConfigFile volume](~~464080~~)
        *   [Increase the size of the temporary storage space](~~204066~~)
        **Container configuration**\
        *   [Configure startup commands and arguments for a container](~~94593~~)
        *   [Use probes to perform health checks on a container](~~99053~~)
        *   [Obtain metadata by using environment variables](~~141788~~)
        *   [Configure a security context for an elastic container instance or a container](~~462313~~)
        *   [Configure the NTP service](~~462768~~)
        **Logging and O\\&M**\
        *   [Use environment variables to configure log collection](~~121973~~)
        *   [Save core files to volumes](~~167801~~)
        

        @param request: CreateContainerGroupRequest

        @return: CreateContainerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_container_group_with_options(request, runtime)

    def create_data_cache_with_options(self, request, runtime):
        """
        You are charged for the creation of image caches. We recommend that you learn the relevant billing information in advance. For more information, see [DataCaches](~~2503093~~).
        *   Before you create an image cache, you must evaluate the size of the data to be cached. If the size of the data exceeds the specified cache size, the image cache fails to be created.
        *   When a data cache is being created, the system automatically creates a temporary elastic container instance (ECI) and an enhanced SSD (ESSD) for the data cache. During the creation, do not delete the ECI and ESSD. Otherwise, the data cache fails to be created.
        *   When a data cache is being created, a snapshot is generated for the data cache. Do not delete the snapshot. Otherwise, the data cache becomes invalid.
        

        @param request: CreateDataCacheRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDataCacheResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_source):
            query['DataSource'] = request.data_source
        if not UtilClient.is_unset(request.eip_create_param):
            query['EipCreateParam'] = request.eip_create_param
        if not UtilClient.is_unset(request.eip_instance_id):
            query['EipInstanceId'] = request.eip_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataCache',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.CreateDataCacheResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_cache(self, request):
        """
        You are charged for the creation of image caches. We recommend that you learn the relevant billing information in advance. For more information, see [DataCaches](~~2503093~~).
        *   Before you create an image cache, you must evaluate the size of the data to be cached. If the size of the data exceeds the specified cache size, the image cache fails to be created.
        *   When a data cache is being created, the system automatically creates a temporary elastic container instance (ECI) and an enhanced SSD (ESSD) for the data cache. During the creation, do not delete the ECI and ESSD. Otherwise, the data cache fails to be created.
        *   When a data cache is being created, a snapshot is generated for the data cache. Do not delete the snapshot. Otherwise, the data cache becomes invalid.
        

        @param request: CreateDataCacheRequest

        @return: CreateDataCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_cache_with_options(request, runtime)

    def create_image_cache_with_options(self, request, runtime):
        """
        **Precautions**\
        *   You are charged for creation of image caches. We recommend that you learn the relevant billing information in advance. For more information about billing of image caches, see [Image caches](~~447682~~).
        *   Before you create an image cache, you must estimate the total size of the images that you want to cache. If the total size of the images exceeds the specified cache size, the image cache cannot be created.
        *   When an image cache is being created, the system creates an intermediate elastic container instance and an intermediate enhanced SSD (ESSD) at performance level 1 (PL1). Do not delete the intermediate instance and the ESSD while the image cache is being created. If you delete the intermediate instance or the ESSD, the image cache cannot be created.
        *   A temporary local snapshot and a specific number of regular snapshots are generated during the creation of the image cache. Do not delete these snapshots. If you delete these snapshots, the image cache becomes invalid.
        *   If you use SDKs, SDK for Java 1.0.10 or later and SDK for Python 1.0.7 or later are supported.
        *   **Usage notes**\
        *   For images that are created based on Container Registry Enterprise Edition instances and use custom domain names, if you want to configure password-free access to the image caches, you must use AcrRegistryInfo-related parameters to specify Container Registry instances. When you configure AcrRegistryInfo-related parameters, you must set the AcrRegistryInfo.N.InstanceId parameter.
        *   If the image cache that you created will be used to create more than 1,000 elastic container instances at a time, we recommend that you use the StandardCopyCount and FlashCopyCount parameters to create multiple temporary local snapshots and regular snapshots of the image. The multiple snapshots are billed based on incremental data. If no incremental data exists on the multiple snapshots, you are not charged for the multiple snapshots.
        >  When you call the CreateImageCache operation to create an image cache, the system automatically creates a service-linked role named AliyunServiceRoleForECI. The role is used to access other Alibaba Cloud services such as Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). For more information, see [Elastic Container Instance service-linked role](~~212914~~).
        

        @param request: CreateImageCacheRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateImageCacheResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_registry_info):
            query['AcrRegistryInfo'] = request.acr_registry_info
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.auto_match_image_cache):
            query['AutoMatchImageCache'] = request.auto_match_image_cache
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.eip_instance_id):
            query['EipInstanceId'] = request.eip_instance_id
        if not UtilClient.is_unset(request.elimination_strategy):
            query['EliminationStrategy'] = request.elimination_strategy
        if not UtilClient.is_unset(request.flash):
            query['Flash'] = request.flash
        if not UtilClient.is_unset(request.flash_copy_count):
            query['FlashCopyCount'] = request.flash_copy_count
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.image_cache_name):
            query['ImageCacheName'] = request.image_cache_name
        if not UtilClient.is_unset(request.image_cache_size):
            query['ImageCacheSize'] = request.image_cache_size
        if not UtilClient.is_unset(request.image_registry_credential):
            query['ImageRegistryCredential'] = request.image_registry_credential
        if not UtilClient.is_unset(request.insecure_registry):
            query['InsecureRegistry'] = request.insecure_registry
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plain_http_registry):
            query['PlainHttpRegistry'] = request.plain_http_registry
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.standard_copy_count):
            query['StandardCopyCount'] = request.standard_copy_count
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageCache',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.CreateImageCacheResponse(),
            self.call_api(params, req, runtime)
        )

    def create_image_cache(self, request):
        """
        **Precautions**\
        *   You are charged for creation of image caches. We recommend that you learn the relevant billing information in advance. For more information about billing of image caches, see [Image caches](~~447682~~).
        *   Before you create an image cache, you must estimate the total size of the images that you want to cache. If the total size of the images exceeds the specified cache size, the image cache cannot be created.
        *   When an image cache is being created, the system creates an intermediate elastic container instance and an intermediate enhanced SSD (ESSD) at performance level 1 (PL1). Do not delete the intermediate instance and the ESSD while the image cache is being created. If you delete the intermediate instance or the ESSD, the image cache cannot be created.
        *   A temporary local snapshot and a specific number of regular snapshots are generated during the creation of the image cache. Do not delete these snapshots. If you delete these snapshots, the image cache becomes invalid.
        *   If you use SDKs, SDK for Java 1.0.10 or later and SDK for Python 1.0.7 or later are supported.
        *   **Usage notes**\
        *   For images that are created based on Container Registry Enterprise Edition instances and use custom domain names, if you want to configure password-free access to the image caches, you must use AcrRegistryInfo-related parameters to specify Container Registry instances. When you configure AcrRegistryInfo-related parameters, you must set the AcrRegistryInfo.N.InstanceId parameter.
        *   If the image cache that you created will be used to create more than 1,000 elastic container instances at a time, we recommend that you use the StandardCopyCount and FlashCopyCount parameters to create multiple temporary local snapshots and regular snapshots of the image. The multiple snapshots are billed based on incremental data. If no incremental data exists on the multiple snapshots, you are not charged for the multiple snapshots.
        >  When you call the CreateImageCache operation to create an image cache, the system automatically creates a service-linked role named AliyunServiceRoleForECI. The role is used to access other Alibaba Cloud services such as Elastic Compute Service (ECS) and Virtual Private Cloud (VPC). For more information, see [Elastic Container Instance service-linked role](~~212914~~).
        

        @param request: CreateImageCacheRequest

        @return: CreateImageCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_image_cache_with_options(request, runtime)

    def create_instance_ops_task_with_options(self, request, runtime):
        """
        O&M tasks are classified into:
        *   coredump: After you enable coredump, the system generates a core dump file when a container unexpectedly stops. You can use the core dump file to analyze the exception and find out the cause of the problem. For more information, see [Enable coredump](~~167801~~).
        *   tcpdump: After you enable tcpdump, the system captures network packets when a container unexpectedly stops. You can analyze the packets and locate network problems. For more information, see Enable [tcpdump](~~429749~~).
        

        @param request: CreateInstanceOpsTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateInstanceOpsTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not UtilClient.is_unset(request.ops_type):
            query['OpsType'] = request.ops_type
        if not UtilClient.is_unset(request.ops_value):
            query['OpsValue'] = request.ops_value
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstanceOpsTask',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.CreateInstanceOpsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance_ops_task(self, request):
        """
        O&M tasks are classified into:
        *   coredump: After you enable coredump, the system generates a core dump file when a container unexpectedly stops. You can use the core dump file to analyze the exception and find out the cause of the problem. For more information, see [Enable coredump](~~167801~~).
        *   tcpdump: After you enable tcpdump, the system captures network packets when a container unexpectedly stops. You can analyze the packets and locate network problems. For more information, see Enable [tcpdump](~~429749~~).
        

        @param request: CreateInstanceOpsTaskRequest

        @return: CreateInstanceOpsTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instance_ops_task_with_options(request, runtime)

    def create_virtual_node_with_options(self, request, runtime):
        """
        When you call this operation to create a virtual node, the system automatically creates a service-linked role AliyunServiceRoleForECIVnode. This way, you can use the service-linked role to access relevant cloud services such as Elastic Container Instance, Elastic Compute Service (ECS), and Virtual Private Cloud (VPC). For more information, see [Service-linked role for virtual nodes](~~311014~~).
        *   You are charged for virtual nodes based on number of virtual nodes that you use. Each virtual node has a resident node, which is equivalent to an ECI instance with 2 vCPU cores and 8 GiB memory. You are charged for virtual nodes based on elastic container instances.
        

        @param request: CreateVirtualNodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateVirtualNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_dns):
            query['ClusterDNS'] = request.cluster_dns
        if not UtilClient.is_unset(request.cluster_domain):
            query['ClusterDomain'] = request.cluster_domain
        if not UtilClient.is_unset(request.custom_resources):
            query['CustomResources'] = request.custom_resources
        if not UtilClient.is_unset(request.eip_instance_id):
            query['EipInstanceId'] = request.eip_instance_id
        if not UtilClient.is_unset(request.enable_public_network):
            query['EnablePublicNetwork'] = request.enable_public_network
        if not UtilClient.is_unset(request.kube_config):
            query['KubeConfig'] = request.kube_config
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.taint):
            query['Taint'] = request.taint
        if not UtilClient.is_unset(request.tls_bootstrap_enabled):
            query['TlsBootstrapEnabled'] = request.tls_bootstrap_enabled
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.virtual_node_name):
            query['VirtualNodeName'] = request.virtual_node_name
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVirtualNode',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.CreateVirtualNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_virtual_node(self, request):
        """
        When you call this operation to create a virtual node, the system automatically creates a service-linked role AliyunServiceRoleForECIVnode. This way, you can use the service-linked role to access relevant cloud services such as Elastic Container Instance, Elastic Compute Service (ECS), and Virtual Private Cloud (VPC). For more information, see [Service-linked role for virtual nodes](~~311014~~).
        *   You are charged for virtual nodes based on number of virtual nodes that you use. Each virtual node has a resident node, which is equivalent to an ECI instance with 2 vCPU cores and 8 GiB memory. You are charged for virtual nodes based on elastic container instances.
        

        @param request: CreateVirtualNodeRequest

        @return: CreateVirtualNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_node_with_options(request, runtime)

    def delete_container_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContainerGroup',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DeleteContainerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_container_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_container_group_with_options(request, runtime)

    def delete_data_cache_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_cache_id):
            query['DataCacheId'] = request.data_cache_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataCache',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DeleteDataCacheResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_cache(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_cache_with_options(request, runtime)

    def delete_image_cache_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_cache_id):
            query['ImageCacheId'] = request.image_cache_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImageCache',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DeleteImageCacheResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_image_cache(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_image_cache_with_options(request, runtime)

    def delete_virtual_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.virtual_node_id):
            query['VirtualNodeId'] = request.virtual_node_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVirtualNode',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DeleteVirtualNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_virtual_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_node_with_options(request, runtime)

    def describe_available_resource_with_options(self, request, runtime):
        """
        When you call the CreateContainerGroup operation to create an elastic container instance, you can use the InstanceType parameter to specify ECS instance types that fit your specific needs. To ensure that the elastic container instance can be created, you can call the DescribeAvailableResource operation to query which ECS instance types and instance families are available in the specified region and zone before you create the elastic container instance.
        

        @param request: DescribeAvailableResourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAvailableResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_resource):
            query['DestinationResource'] = request.destination_resource
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spot_resource):
            query['SpotResource'] = request.spot_resource
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_resource(self, request):
        """
        When you call the CreateContainerGroup operation to create an elastic container instance, you can use the InstanceType parameter to specify ECS instance types that fit your specific needs. To ensure that the elastic container instance can be created, you can call the DescribeAvailableResource operation to query which ECS instance types and instance families are available in the specified region and zone before you create the elastic container instance.
        

        @param request: DescribeAvailableResourceRequest

        @return: DescribeAvailableResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    def describe_commit_container_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCommitContainerTask',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeCommitContainerTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_commit_container_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_commit_container_task_with_options(request, runtime)

    def describe_container_group_events_with_options(self, request, runtime):
        """
        You can call this operation to query the event information about multiple elastic container instances at a time. By default, the most recent 50 entries of events of each elastic container instance are returned.
        

        @param request: DescribeContainerGroupEventsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeContainerGroupEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.container_group_ids):
            query['ContainerGroupIds'] = request.container_group_ids
        if not UtilClient.is_unset(request.event_source):
            query['EventSource'] = request.event_source
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.since_second):
            query['SinceSecond'] = request.since_second
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerGroupEvents',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeContainerGroupEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_container_group_events(self, request):
        """
        You can call this operation to query the event information about multiple elastic container instances at a time. By default, the most recent 50 entries of events of each elastic container instance are returned.
        

        @param request: DescribeContainerGroupEventsRequest

        @return: DescribeContainerGroupEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_container_group_events_with_options(request, runtime)

    def describe_container_group_metric_with_options(self, request, runtime):
        """
        A maximum of 50 monitoring data entries can be returned. If the number of monitoring data entries exceeds this limit, an error message is returned.
        *   You can query real-time monitoring data (data generated within the last 5 minutes) and historical data (data generated more than 5 minutes ago). If the time range to query starts or ends later than the current time, historical monitoring data generated more than 5 minutes ago is returned.
        *   The elastic container instance whose monitoring data you want to query must be created after April 3, 2019, 15:00 UTC+8.
        

        @param request: DescribeContainerGroupMetricRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeContainerGroupMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerGroupMetric',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeContainerGroupMetricResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_container_group_metric(self, request):
        """
        A maximum of 50 monitoring data entries can be returned. If the number of monitoring data entries exceeds this limit, an error message is returned.
        *   You can query real-time monitoring data (data generated within the last 5 minutes) and historical data (data generated more than 5 minutes ago). If the time range to query starts or ends later than the current time, historical monitoring data generated more than 5 minutes ago is returned.
        *   The elastic container instance whose monitoring data you want to query must be created after April 3, 2019, 15:00 UTC+8.
        

        @param request: DescribeContainerGroupMetricRequest

        @return: DescribeContainerGroupMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_container_group_metric_with_options(request, runtime)

    def describe_container_group_price_with_options(self, request, runtime):
        """
        When you call this operation, you cannot use resource groups to control the permissions of a RAM user.
        *   You can create an elastic container instance by specifying vCPU and memory resource specifications or by specifying ECS instance types. When you call this operation to query the prices of elastic container instances, pass in specifications of the elastic container instances.
        *   [vCPU and memory specifications](~~114662~~).
        *   [ECS instance types that are supported by Elastic Container Instance](~~114664~~).
        

        @param request: DescribeContainerGroupPriceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeContainerGroupPriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compute_category):
            query['ComputeCategory'] = request.compute_category
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerGroupPrice',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeContainerGroupPriceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_container_group_price(self, request):
        """
        When you call this operation, you cannot use resource groups to control the permissions of a RAM user.
        *   You can create an elastic container instance by specifying vCPU and memory resource specifications or by specifying ECS instance types. When you call this operation to query the prices of elastic container instances, pass in specifications of the elastic container instances.
        *   [vCPU and memory specifications](~~114662~~).
        *   [ECS instance types that are supported by Elastic Container Instance](~~114664~~).
        

        @param request: DescribeContainerGroupPriceRequest

        @return: DescribeContainerGroupPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_container_group_price_with_options(request, runtime)

    def describe_container_group_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.container_group_ids):
            query['ContainerGroupIds'] = request.container_group_ids
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.since_second):
            query['SinceSecond'] = request.since_second
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerGroupStatus',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeContainerGroupStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_container_group_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_container_group_status_with_options(request, runtime)

    def describe_container_groups_with_options(self, request, runtime):
        """
        After an elastic container instance is terminated, its underlying computing resources are recycled. By default, other resources, such as elastic IP addresses (EIPs), that are created together with the instance are released together with the instance.
        *   The metadata of an instance in the final status (Failed, Succeeded, or Expired) is retained based on the following rules:
        *   All metadata information is retained within 1 hour since the instance enters the final status.
        *   One hour after the instance enters the final status, only the latest 100 entries of metadata information in each region are retained.
        

        @param request: DescribeContainerGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeContainerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compute_category):
            query['ComputeCategory'] = request.compute_category
        if not UtilClient.is_unset(request.container_group_ids):
            query['ContainerGroupIds'] = request.container_group_ids
        if not UtilClient.is_unset(request.container_group_name):
            query['ContainerGroupName'] = request.container_group_name
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.with_event):
            query['WithEvent'] = request.with_event
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerGroups',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeContainerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_container_groups(self, request):
        """
        After an elastic container instance is terminated, its underlying computing resources are recycled. By default, other resources, such as elastic IP addresses (EIPs), that are created together with the instance are released together with the instance.
        *   The metadata of an instance in the final status (Failed, Succeeded, or Expired) is retained based on the following rules:
        *   All metadata information is retained within 1 hour since the instance enters the final status.
        *   One hour after the instance enters the final status, only the latest 100 entries of metadata information in each region are retained.
        

        @param request: DescribeContainerGroupsRequest

        @return: DescribeContainerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_container_groups_with_options(request, runtime)

    def describe_container_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not UtilClient.is_unset(request.container_name):
            query['ContainerName'] = request.container_name
        if not UtilClient.is_unset(request.last_time):
            query['LastTime'] = request.last_time
        if not UtilClient.is_unset(request.limit_bytes):
            query['LimitBytes'] = request.limit_bytes
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.since_seconds):
            query['SinceSeconds'] = request.since_seconds
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tail):
            query['Tail'] = request.tail
        if not UtilClient.is_unset(request.timestamps):
            query['Timestamps'] = request.timestamps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerLog',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeContainerLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_container_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_container_log_with_options(request, runtime)

    def describe_data_caches_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.data_cache_id):
            query['DataCacheId'] = request.data_cache_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataCaches',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeDataCachesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_caches(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_caches_with_options(request, runtime)

    def describe_image_caches_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.image_cache_id):
            query['ImageCacheId'] = request.image_cache_id
        if not UtilClient.is_unset(request.image_cache_name):
            query['ImageCacheName'] = request.image_cache_name
        if not UtilClient.is_unset(request.image_full_match):
            query['ImageFullMatch'] = request.image_full_match
        if not UtilClient.is_unset(request.image_match_count_request):
            query['ImageMatchCountRequest'] = request.image_match_count_request
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.match_image):
            query['MatchImage'] = request.match_image
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageCaches',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeImageCachesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_image_caches(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_caches_with_options(request, runtime)

    def describe_instance_ops_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not UtilClient.is_unset(request.ops_type):
            query['OpsType'] = request.ops_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceOpsRecords',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeInstanceOpsRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_ops_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_ops_records_with_options(request, runtime)

    def describe_multi_container_group_metric_with_options(self, request, runtime):
        """
        Only the latest entry of monitoring data of each elastic container instance is returned.
        *   You can query only the monitoring data of elastic container instances that are created after April 3, 2019 15:00:00 UTC+8.
        

        @param request: DescribeMultiContainerGroupMetricRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMultiContainerGroupMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.container_group_ids):
            query['ContainerGroupIds'] = request.container_group_ids
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMultiContainerGroupMetric',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeMultiContainerGroupMetricResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_multi_container_group_metric(self, request):
        """
        Only the latest entry of monitoring data of each elastic container instance is returned.
        *   You can query only the monitoring data of elastic container instances that are created after April 3, 2019 15:00:00 UTC+8.
        

        @param request: DescribeMultiContainerGroupMetricRequest

        @return: DescribeMultiContainerGroupMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_multi_container_group_metric_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_virtual_nodes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.virtual_node_ids):
            query['VirtualNodeIds'] = request.virtual_node_ids
        if not UtilClient.is_unset(request.virtual_node_name):
            query['VirtualNodeName'] = request.virtual_node_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVirtualNodes',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeVirtualNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_virtual_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_nodes_with_options(request, runtime)

    def exec_container_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not UtilClient.is_unset(request.container_name):
            query['ContainerName'] = request.container_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.stdin):
            query['Stdin'] = request.stdin
        if not UtilClient.is_unset(request.sync):
            query['Sync'] = request.sync
        if not UtilClient.is_unset(request.tty):
            query['TTY'] = request.tty
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecContainerCommand',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.ExecContainerCommandResponse(),
            self.call_api(params, req, runtime)
        )

    def exec_container_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.exec_container_command_with_options(request, runtime)

    def list_usage_with_options(self, request, runtime):
        """
        This operation does not support resource group authentication.
        

        @param request: ListUsageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsage',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.ListUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def list_usage(self, request):
        """
        This operation does not support resource group authentication.
        

        @param request: ListUsageRequest

        @return: ListUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_usage_with_options(request, runtime)

    def resize_container_group_volume_with_options(self, request, runtime):
        """
        You can scale up volumes by calling this operation. You cannot scale down volumes by calling this operation. Only volumes of Alibaba Cloud disks can be scaled up.
        

        @param request: ResizeContainerGroupVolumeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResizeContainerGroupVolumeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not UtilClient.is_unset(request.new_size):
            query['NewSize'] = request.new_size
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.volume_name):
            query['VolumeName'] = request.volume_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeContainerGroupVolume',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.ResizeContainerGroupVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    def resize_container_group_volume(self, request):
        """
        You can scale up volumes by calling this operation. You cannot scale down volumes by calling this operation. Only volumes of Alibaba Cloud disks can be scaled up.
        

        @param request: ResizeContainerGroupVolumeRequest

        @return: ResizeContainerGroupVolumeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resize_container_group_volume_with_options(request, runtime)

    def restart_container_group_with_options(self, request, runtime):
        """
        Only elastic container instances that are in the Pending or Running state can be restarted. Instances that are in the Succeeded or Failed state cannot be restarted.
        *   Elastic container instances that were created before 15:00:00 on March 7, 2019 cannot be restarted.
        *   When an elastic container instance is being restarted, its status changes into Restarting.
        

        @param request: RestartContainerGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RestartContainerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartContainerGroup',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.RestartContainerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_container_group(self, request):
        """
        Only elastic container instances that are in the Pending or Running state can be restarted. Instances that are in the Succeeded or Failed state cannot be restarted.
        *   Elastic container instances that were created before 15:00:00 on March 7, 2019 cannot be restarted.
        *   When an elastic container instance is being restarted, its status changes into Restarting.
        

        @param request: RestartContainerGroupRequest

        @return: RestartContainerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_container_group_with_options(request, runtime)

    def update_container_group_with_options(self, request, runtime):
        """
        Only elastic container instances that are in the Pending or Running state can be updated. After you call this operation to update an elastic container instance, the instance enters the Updating state.
        *   If the RestartPolicy parameter is set to Never for the elastic container instance that you are updating, the containers of the instance may fail. Exercise caution if you want to update the kind of instances.
        

        @param request: UpdateContainerGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateContainerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_registry_info):
            query['AcrRegistryInfo'] = request.acr_registry_info
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.container):
            query['Container'] = request.container
        if not UtilClient.is_unset(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.image_registry_credential):
            query['ImageRegistryCredential'] = request.image_registry_credential
        if not UtilClient.is_unset(request.init_container):
            query['InitContainer'] = request.init_container
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restart_policy):
            query['RestartPolicy'] = request.restart_policy
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.update_type):
            query['UpdateType'] = request.update_type
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        if not UtilClient.is_unset(request.dns_config):
            query['DnsConfig'] = request.dns_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateContainerGroup',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.UpdateContainerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_container_group(self, request):
        """
        Only elastic container instances that are in the Pending or Running state can be updated. After you call this operation to update an elastic container instance, the instance enters the Updating state.
        *   If the RestartPolicy parameter is set to Never for the elastic container instance that you are updating, the containers of the instance may fail. Exercise caution if you want to update the kind of instances.
        

        @param request: UpdateContainerGroupRequest

        @return: UpdateContainerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_container_group_with_options(request, runtime)

    def update_data_cache_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_cache_id):
            query['DataCacheId'] = request.data_cache_id
        if not UtilClient.is_unset(request.data_source):
            query['DataSource'] = request.data_source
        if not UtilClient.is_unset(request.eip_create_param):
            query['EipCreateParam'] = request.eip_create_param
        if not UtilClient.is_unset(request.eip_instance_id):
            query['EipInstanceId'] = request.eip_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataCache',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.UpdateDataCacheResponse(),
            self.call_api(params, req, runtime)
        )

    def update_data_cache(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_data_cache_with_options(request, runtime)

    def update_image_cache_with_options(self, request, runtime):
        """
        Only image caches that are in the Ready or UpdateFailed state can be updated.
        

        @param request: UpdateImageCacheRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateImageCacheResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_registry_info):
            query['AcrRegistryInfo'] = request.acr_registry_info
        if not UtilClient.is_unset(request.auto_match_image_cache):
            query['AutoMatchImageCache'] = request.auto_match_image_cache
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.eip_instance_id):
            query['EipInstanceId'] = request.eip_instance_id
        if not UtilClient.is_unset(request.elimination_strategy):
            query['EliminationStrategy'] = request.elimination_strategy
        if not UtilClient.is_unset(request.flash):
            query['Flash'] = request.flash
        if not UtilClient.is_unset(request.flash_copy_count):
            query['FlashCopyCount'] = request.flash_copy_count
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.image_cache_id):
            query['ImageCacheId'] = request.image_cache_id
        if not UtilClient.is_unset(request.image_cache_name):
            query['ImageCacheName'] = request.image_cache_name
        if not UtilClient.is_unset(request.image_cache_size):
            query['ImageCacheSize'] = request.image_cache_size
        if not UtilClient.is_unset(request.image_registry_credential):
            query['ImageRegistryCredential'] = request.image_registry_credential
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.standard_copy_count):
            query['StandardCopyCount'] = request.standard_copy_count
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateImageCache',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.UpdateImageCacheResponse(),
            self.call_api(params, req, runtime)
        )

    def update_image_cache(self, request):
        """
        Only image caches that are in the Ready or UpdateFailed state can be updated.
        

        @param request: UpdateImageCacheRequest

        @return: UpdateImageCacheResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_image_cache_with_options(request, runtime)

    def update_virtual_node_with_options(self, request, runtime):
        """
        ## Usage notes
        Only virtual nodes that are in the Ready state can be updated.
        

        @param request: UpdateVirtualNodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateVirtualNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_dns):
            query['ClusterDNS'] = request.cluster_dns
        if not UtilClient.is_unset(request.cluster_domain):
            query['ClusterDomain'] = request.cluster_domain
        if not UtilClient.is_unset(request.custom_resources):
            query['CustomResources'] = request.custom_resources
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.virtual_node_id):
            query['VirtualNodeId'] = request.virtual_node_id
        if not UtilClient.is_unset(request.virtual_node_name):
            query['VirtualNodeName'] = request.virtual_node_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVirtualNode',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.UpdateVirtualNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_virtual_node(self, request):
        """
        ## Usage notes
        Only virtual nodes that are in the Ready state can be updated.
        

        @param request: UpdateVirtualNodeRequest

        @return: UpdateVirtualNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_virtual_node_with_options(request, runtime)
