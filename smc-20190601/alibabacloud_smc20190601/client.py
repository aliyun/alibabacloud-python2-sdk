# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_smc20190601 import models as smc_20190601_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('smc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_access_token_with_options(self, request, runtime):
        """
        If you want to import the information of migration sources by using an activation code, you can call this operation to create one.
        

        @param request: CreateAccessTokenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAccessTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.time_to_live_in_days):
            query['TimeToLiveInDays'] = request.time_to_live_in_days
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessToken',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.CreateAccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def create_access_token(self, request):
        """
        If you want to import the information of migration sources by using an activation code, you can call this operation to create one.
        

        @param request: CreateAccessTokenRequest

        @return: CreateAccessTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_access_token_with_options(request, runtime)

    def create_replication_job_with_options(self, request, runtime):
        """
        ## Usage notes
        *   You can create migration jobs only for source servers that are in the Available state.
        *   Each source server can be associated with only one migration job that is in the Ready, Running, Stopped, Waiting, InError, or Expired state.
        *   You can create a maximum of 1,000 migration jobs within each Alibaba Cloud account.
        *   If you migrate a source server to an image, you must specify the ImageName, SystemDiskSize, and DataDisk parameters.
        *   If you use a virtual private cloud (VPC) to migrate data, the VSwitchId parameter is required and the VpcId parameter is optional.
        *   Server Migration Center (SMC) allows you to migrate source servers to Docker container images. This allows you to migrate containerized applications in a cost-effective way.
        

        @param request: CreateReplicationJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateReplicationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.container_namespace):
            query['ContainerNamespace'] = request.container_namespace
        if not UtilClient.is_unset(request.container_repository):
            query['ContainerRepository'] = request.container_repository
        if not UtilClient.is_unset(request.container_tag):
            query['ContainerTag'] = request.container_tag
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.frequency):
            query['Frequency'] = request.frequency
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_ram_role):
            query['InstanceRamRole'] = request.instance_ram_role
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.license_type):
            query['LicenseType'] = request.license_type
        if not UtilClient.is_unset(request.max_number_of_image_to_keep):
            query['MaxNumberOfImageToKeep'] = request.max_number_of_image_to_keep
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.net_mode):
            query['NetMode'] = request.net_mode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replication_parameters):
            query['ReplicationParameters'] = request.replication_parameters
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.run_once):
            query['RunOnce'] = request.run_once
        if not UtilClient.is_unset(request.scheduled_start_time):
            query['ScheduledStartTime'] = request.scheduled_start_time
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.system_disk_part):
            query['SystemDiskPart'] = request.system_disk_part
        if not UtilClient.is_unset(request.system_disk_size):
            query['SystemDiskSize'] = request.system_disk_size
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.valid_time):
            query['ValidTime'] = request.valid_time
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateReplicationJob',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.CreateReplicationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_replication_job(self, request):
        """
        ## Usage notes
        *   You can create migration jobs only for source servers that are in the Available state.
        *   Each source server can be associated with only one migration job that is in the Ready, Running, Stopped, Waiting, InError, or Expired state.
        *   You can create a maximum of 1,000 migration jobs within each Alibaba Cloud account.
        *   If you migrate a source server to an image, you must specify the ImageName, SystemDiskSize, and DataDisk parameters.
        *   If you use a virtual private cloud (VPC) to migrate data, the VSwitchId parameter is required and the VpcId parameter is optional.
        *   Server Migration Center (SMC) allows you to migrate source servers to Docker container images. This allows you to migrate containerized applications in a cost-effective way.
        

        @param request: CreateReplicationJobRequest

        @return: CreateReplicationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_replication_job_with_options(request, runtime)

    def cut_over_replication_job_with_options(self, request, runtime):
        """
        ## Usage notes
        *   The incremental migration job must be in the Waiting state.
        *   After you call this operation, the incremental migration job no longer periodically runs. In the meantime, Server Migration Center (SMC) determines whether to perform a full data migration for the last time based on the value of the `SyncData` parameter. If you set the SyncData parameter to `false`, SMC releases intermediate resources without data migration before the migration job is complete. If you set the SyncData parameter to `true`, SMC performs a full data migration and releases intermediate resources before the migration job is complete.
        

        @param request: CutOverReplicationJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CutOverReplicationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.sync_data):
            query['SyncData'] = request.sync_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CutOverReplicationJob',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.CutOverReplicationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def cut_over_replication_job(self, request):
        """
        ## Usage notes
        *   The incremental migration job must be in the Waiting state.
        *   After you call this operation, the incremental migration job no longer periodically runs. In the meantime, Server Migration Center (SMC) determines whether to perform a full data migration for the last time based on the value of the `SyncData` parameter. If you set the SyncData parameter to `false`, SMC releases intermediate resources without data migration before the migration job is complete. If you set the SyncData parameter to `true`, SMC performs a full data migration and releases intermediate resources before the migration job is complete.
        

        @param request: CutOverReplicationJobRequest

        @return: CutOverReplicationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cut_over_replication_job_with_options(request, runtime)

    def delete_access_token_with_options(self, request, runtime):
        """
        You can call this operation to delete an activation code if you no longer need to import the information about migration sources by using the activation code or if the activation code has expired.
        

        @param request: DeleteAccessTokenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAccessTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token_id):
            query['AccessTokenId'] = request.access_token_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessToken',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.DeleteAccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_access_token(self, request):
        """
        You can call this operation to delete an activation code if you no longer need to import the information about migration sources by using the activation code or if the activation code has expired.
        

        @param request: DeleteAccessTokenRequest

        @return: DeleteAccessTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_access_token_with_options(request, runtime)

    def delete_replication_job_with_options(self, request, runtime):
        """
        ## Usage notes
        *   Deleted migration jobs cannot be restored.
        *   After a migration job is deleted, associated resources, such as the intermediate instance, are automatically released.
        

        @param request: DeleteReplicationJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteReplicationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteReplicationJob',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.DeleteReplicationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_replication_job(self, request):
        """
        ## Usage notes
        *   Deleted migration jobs cannot be restored.
        *   After a migration job is deleted, associated resources, such as the intermediate instance, are automatically released.
        

        @param request: DeleteReplicationJobRequest

        @return: DeleteReplicationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_replication_job_with_options(request, runtime)

    def delete_source_server_with_options(self, request, runtime):
        """
        ## Usage notes
        *   If a migration job is created for the migration source and the migration job is in the Running state, the migration source cannot be deleted.
        *   If a migration job is created for the migration source but the migration job is not in the Running state, you can set the `Force` parameter to true to delete the migration source.
        

        @param request: DeleteSourceServerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteSourceServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSourceServer',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.DeleteSourceServerResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_source_server(self, request):
        """
        ## Usage notes
        *   If a migration job is created for the migration source and the migration job is in the Running state, the migration source cannot be deleted.
        *   If a migration job is created for the migration source but the migration job is not in the Running state, you can set the `Force` parameter to true to delete the migration source.
        

        @param request: DeleteSourceServerRequest

        @return: DeleteSourceServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_source_server_with_options(request, runtime)

    def describe_replication_jobs_with_options(self, request, runtime):
        """
        ## Usage notes
        *   You can specify multiple request parameters to be queried. Specified parameters are evaluated by using the AND operator. Only the specified parameters are used as filter conditions.
        *   Server Migration Center (SMC) allows you to migrate source servers to Docker container images. You can use SMC to migrate containerized applications in a cost-effective way. For more information, see [Terms](~~60744~~).
        

        @param request: DescribeReplicationJobsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeReplicationJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_status):
            query['BusinessStatus'] = request.business_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeReplicationJobs',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.DescribeReplicationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_replication_jobs(self, request):
        """
        ## Usage notes
        *   You can specify multiple request parameters to be queried. Specified parameters are evaluated by using the AND operator. Only the specified parameters are used as filter conditions.
        *   Server Migration Center (SMC) allows you to migrate source servers to Docker container images. You can use SMC to migrate containerized applications in a cost-effective way. For more information, see [Terms](~~60744~~).
        

        @param request: DescribeReplicationJobsRequest

        @return: DescribeReplicationJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_replication_jobs_with_options(request, runtime)

    def describe_source_servers_with_options(self, request, runtime):
        """
        ## Usage notes
        You can specify multiple request parameters to be queried. Specified parameters are evaluated by using the AND operator. Only the specified parameters are used as filter conditions.
        

        @param request: DescribeSourceServersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSourceServersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSourceServers',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.DescribeSourceServersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_source_servers(self, request):
        """
        ## Usage notes
        You can specify multiple request parameters to be queried. Specified parameters are evaluated by using the AND operator. Only the specified parameters are used as filter conditions.
        

        @param request: DescribeSourceServersRequest

        @return: DescribeSourceServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_source_servers_with_options(request, runtime)

    def disable_access_token_with_options(self, request, runtime):
        """
        To prevent an activation code from being leaked, you can call this operation to disable the activation code. Disabled activation codes can no longer be used to import the information about migration sources. However, migration sources whose information has been imported are not affected.
        

        @param request: DisableAccessTokenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DisableAccessTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token_id):
            query['AccessTokenId'] = request.access_token_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAccessToken',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.DisableAccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_access_token(self, request):
        """
        To prevent an activation code from being leaked, you can call this operation to disable the activation code. Disabled activation codes can no longer be used to import the information about migration sources. However, migration sources whose information has been imported are not affected.
        

        @param request: DisableAccessTokenRequest

        @return: DisableAccessTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_access_token_with_options(request, runtime)

    def list_access_tokens_with_options(self, request, runtime):
        """
        You can call this operation to query activation codes and the usage details of the activation codes. An activation code can be in the activated, unactivated, or expired state.
        

        @param request: ListAccessTokensRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAccessTokensResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token_id):
            query['AccessTokenId'] = request.access_token_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessTokens',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.ListAccessTokensResponse(),
            self.call_api(params, req, runtime)
        )

    def list_access_tokens(self, request):
        """
        You can call this operation to query activation codes and the usage details of the activation codes. An activation code can be in the activated, unactivated, or expired state.
        

        @param request: ListAccessTokensRequest

        @return: ListAccessTokensResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_access_tokens_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def modify_replication_job_attribute_with_options(self, request, runtime):
        """
        ## Usage notes
        Before you modify the parameters of a migration job, take note of the following information:
        *   The `Name` and `Description` parameters can be modified during the lifecycle of the migration job.
        *   The `Frequency` and `MaxNumberOfImageToKeep` parameters can be modified only before the migration job is executed or when the migration job is in the `Waiting` state.
        *   Other parameters can be modified only before the migration job is executed.
        

        @param request: ModifyReplicationJobAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyReplicationJobAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.container_namespace):
            query['ContainerNamespace'] = request.container_namespace
        if not UtilClient.is_unset(request.container_repository):
            query['ContainerRepository'] = request.container_repository
        if not UtilClient.is_unset(request.container_tag):
            query['ContainerTag'] = request.container_tag
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.frequency):
            query['Frequency'] = request.frequency
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_ram_role):
            query['InstanceRamRole'] = request.instance_ram_role
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.license_type):
            query['LicenseType'] = request.license_type
        if not UtilClient.is_unset(request.max_number_of_image_to_keep):
            query['MaxNumberOfImageToKeep'] = request.max_number_of_image_to_keep
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.net_mode):
            query['NetMode'] = request.net_mode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.replication_parameters):
            query['ReplicationParameters'] = request.replication_parameters
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scheduled_start_time):
            query['ScheduledStartTime'] = request.scheduled_start_time
        if not UtilClient.is_unset(request.system_disk_part):
            query['SystemDiskPart'] = request.system_disk_part
        if not UtilClient.is_unset(request.system_disk_size):
            query['SystemDiskSize'] = request.system_disk_size
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.valid_time):
            query['ValidTime'] = request.valid_time
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyReplicationJobAttribute',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.ModifyReplicationJobAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_replication_job_attribute(self, request):
        """
        ## Usage notes
        Before you modify the parameters of a migration job, take note of the following information:
        *   The `Name` and `Description` parameters can be modified during the lifecycle of the migration job.
        *   The `Frequency` and `MaxNumberOfImageToKeep` parameters can be modified only before the migration job is executed or when the migration job is in the `Waiting` state.
        *   Other parameters can be modified only before the migration job is executed.
        

        @param request: ModifyReplicationJobAttributeRequest

        @return: ModifyReplicationJobAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_replication_job_attribute_with_options(request, runtime)

    def modify_source_server_attribute_with_options(self, request, runtime):
        """
        ## Usage notes
        You can call this operation regardless of the status of the migration source.
        

        @param request: ModifySourceServerAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifySourceServerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySourceServerAttribute',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.ModifySourceServerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_source_server_attribute(self, request):
        """
        ## Usage notes
        You can call this operation regardless of the status of the migration source.
        

        @param request: ModifySourceServerAttributeRequest

        @return: ModifySourceServerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_source_server_attribute_with_options(request, runtime)

    def start_replication_job_with_options(self, request, runtime):
        """
        ## Usage notes
        This operation can only be used to start the migration jobs that are in the Ready, Stopped, or InError state.
        

        @param request: StartReplicationJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartReplicationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartReplicationJob',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.StartReplicationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def start_replication_job(self, request):
        """
        ## Usage notes
        This operation can only be used to start the migration jobs that are in the Ready, Stopped, or InError state.
        

        @param request: StartReplicationJobRequest

        @return: StartReplicationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_replication_job_with_options(request, runtime)

    def stop_replication_job_with_options(self, request, runtime):
        """
        ## Usage notes
        You can call this operation to pause only a migration job whose primary status is Running and business status is Syncing.
        

        @param request: StopReplicationJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopReplicationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopReplicationJob',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.StopReplicationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_replication_job(self, request):
        """
        ## Usage notes
        You can call this operation to pause only a migration job whose primary status is Running and business status is Syncing.
        

        @param request: StopReplicationJobRequest

        @return: StopReplicationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_replication_job_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        """
        ## Usage notes
        Up to 20 tags can be added to each SMC resource.
        Before you add tags to an SMC resource, Alibaba Cloud checks the number of the tags that have been added to the resource. If the maximum number is reached, an error message is returned.
        

        @param request: TagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        """
        ## Usage notes
        Up to 20 tags can be added to each SMC resource.
        Before you add tags to an SMC resource, Alibaba Cloud checks the number of the tags that have been added to the resource. If the maximum number is reached, an error message is returned.
        

        @param request: TagResourcesRequest

        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        """
        You can call this operation to remove tags that are added to one or more SMC resources and deletes the tags if the tags are no longer used.
        

        @param request: UntagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        """
        You can call this operation to remove tags that are added to one or more SMC resources and deletes the tags if the tags are no longer used.
        

        @param request: UntagResourcesRequest

        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)
