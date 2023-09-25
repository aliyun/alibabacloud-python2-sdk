# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dts20160801 import models as dts_20160801_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'dts.aliyuncs.com',
            'cn-beijing': 'dts.aliyuncs.com',
            'cn-zhangjiakou': 'dts.aliyuncs.com',
            'cn-huhehaote': 'dts.aliyuncs.com',
            'cn-hangzhou': 'dts.aliyuncs.com',
            'cn-shanghai': 'dts.aliyuncs.com',
            'cn-shenzhen': 'dts.aliyuncs.com',
            'cn-hongkong': 'dts.aliyuncs.com',
            'ap-southeast-1': 'dts.aliyuncs.com',
            'ap-southeast-2': 'dts.aliyuncs.com',
            'ap-southeast-3': 'dts.aliyuncs.com',
            'ap-southeast-5': 'dts.aliyuncs.com',
            'eu-west-1': 'dts.aliyuncs.com',
            'us-west-1': 'dts.aliyuncs.com',
            'us-east-1': 'dts.aliyuncs.com',
            'eu-central-1': 'dts.aliyuncs.com',
            'me-east-1': 'dts.aliyuncs.com',
            'ap-south-1': 'dts.aliyuncs.com',
            'cn-hangzhou-finance': 'dts.aliyuncs.com',
            'cn-shanghai-finance-1': 'dts.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dts.aliyuncs.com',
            'cn-north-2-gov-1': 'dts.aliyuncs.com',
            'ap-northeast-2-pop': 'dts.aliyuncs.com',
            'cn-beijing-finance-1': 'dts.aliyuncs.com',
            'cn-beijing-finance-pop': 'dts.aliyuncs.com',
            'cn-beijing-gov-1': 'dts.aliyuncs.com',
            'cn-beijing-nu16-b01': 'dts.aliyuncs.com',
            'cn-chengdu': 'dts.aliyuncs.com',
            'cn-edge-1': 'dts.aliyuncs.com',
            'cn-fujian': 'dts.aliyuncs.com',
            'cn-haidian-cm12-c01': 'dts.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'dts.aliyuncs.com',
            'cn-hangzhou-test-306': 'dts.aliyuncs.com',
            'cn-hongkong-finance-pop': 'dts.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'dts.aliyuncs.com',
            'cn-qingdao-nebula': 'dts.aliyuncs.com',
            'cn-shanghai-et15-b01': 'dts.aliyuncs.com',
            'cn-shanghai-et2-b01': 'dts.aliyuncs.com',
            'cn-shanghai-inner': 'dts.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'dts.aliyuncs.com',
            'cn-shenzhen-inner': 'dts.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'dts.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'dts.aliyuncs.com',
            'cn-wuhan': 'dts.aliyuncs.com',
            'cn-wulanchabu': 'dts.aliyuncs.com',
            'cn-yushanfang': 'dts.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'dts.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'dts.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'dts.aliyuncs.com',
            'eu-west-1-oxs': 'dts.aliyuncs.com',
            'rus-west-1-pop': 'dts.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dts', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def configuration_synchronization_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.synchronization_job_name):
            query['SynchronizationJobName'] = request.synchronization_job_name
        if not UtilClient.is_unset(request.synchronization_object):
            query['SynchronizationObject'] = request.synchronization_object
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.initialization):
            query['Initialization'] = request.initialization
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigurationSynchronizationJob',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.ConfigurationSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def configuration_synchronization_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.configuration_synchronization_job_with_options(request, runtime)

    def configure_migration_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not UtilClient.is_unset(request.migration_object):
            query['MigrationObject'] = request.migration_object
        if not UtilClient.is_unset(request.migration_reserved):
            query['MigrationReserved'] = request.migration_reserved
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureMigrationJob',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.ConfigureMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def configure_migration_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.configure_migration_job_with_options(request, runtime)

    def configure_subscription_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not UtilClient.is_unset(request.subscription_instance_name):
            query['SubscriptionInstanceName'] = request.subscription_instance_name
        if not UtilClient.is_unset(request.subscription_object):
            query['SubscriptionObject'] = request.subscription_object
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        if not UtilClient.is_unset(request.subscription_data_type):
            query['SubscriptionDataType'] = request.subscription_data_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSubscriptionInstance',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.ConfigureSubscriptionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def configure_subscription_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.configure_subscription_instance_with_options(request, runtime)

    def configure_synchronization_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not UtilClient.is_unset(request.migration_reserved):
            query['MigrationReserved'] = request.migration_reserved
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.synchronization_job_name):
            query['SynchronizationJobName'] = request.synchronization_job_name
        if not UtilClient.is_unset(request.synchronization_objects):
            query['SynchronizationObjects'] = request.synchronization_objects
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.partition_key):
            query['PartitionKey'] = request.partition_key
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSynchronizationJob',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.ConfigureSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def configure_synchronization_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.configure_synchronization_job_with_options(request, runtime)

    def create_migration_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_class):
            query['MigrationJobClass'] = request.migration_job_class
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMigrationJob',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.CreateMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_migration_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_migration_job_with_options(request, runtime)

    def create_subscription_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubscriptionInstance',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.CreateSubscriptionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_subscription_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_subscription_instance_with_options(request, runtime)

    def create_synchronization_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.source_region):
            query['SourceRegion'] = request.source_region
        if not UtilClient.is_unset(request.synchronization_job_class):
            query['SynchronizationJobClass'] = request.synchronization_job_class
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.network_type):
            query['networkType'] = request.network_type
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSynchronizationJob',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.CreateSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_synchronization_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_synchronization_job_with_options(request, runtime)

    def delete_migration_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMigrationJob',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.DeleteMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_migration_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_migration_job_with_options(request, runtime)

    def delete_subscription_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubscriptionInstance',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.DeleteSubscriptionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_subscription_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_subscription_instance_with_options(request, runtime)

    def delete_synchronization_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSynchronizationJob',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.DeleteSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_synchronization_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_synchronization_job_with_options(request, runtime)

    def descirbe_migration_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescirbeMigrationJobs',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.DescirbeMigrationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def descirbe_migration_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.descirbe_migration_jobs_with_options(request, runtime)

    def describe_initialization_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInitializationStatus',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.DescribeInitializationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_initialization_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_initialization_status_with_options(request, runtime)

    def describe_migration_job_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobDetail',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.DescribeMigrationJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_migration_job_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_job_detail_with_options(request, runtime)

    def describe_migration_job_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobStatus',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.DescribeMigrationJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_migration_job_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_job_status_with_options(request, runtime)

    def describe_migration_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobs',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.DescribeMigrationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_migration_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_jobs_with_options(request, runtime)

    def describe_subscription_instance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInstanceStatus',
            version='2016-08-01',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.DescribeSubscriptionInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_subscription_instance_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_instance_status_with_options(request, runtime)

    def describe_subscription_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.subscription_instance_name):
            query['SubscriptionInstanceName'] = request.subscription_instance_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInstances',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.DescribeSubscriptionInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_subscription_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_instances_with_options(request, runtime)

    def describe_subscription_object_modify_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionObjectModifyStatus',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.DescribeSubscriptionObjectModifyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_subscription_object_modify_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_object_modify_status_with_options(request, runtime)

    def describe_synchronization_job_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobStatus',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.DescribeSynchronizationJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_synchronization_job_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_status_with_options(request, runtime)

    def describe_synchronization_jobs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.synchronization_job_name):
            query['SynchronizationJobName'] = request.synchronization_job_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobs',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.DescribeSynchronizationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_synchronization_jobs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_jobs_with_options(request, runtime)

    def describe_synchronization_object_modify_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationObjectModifyStatus',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.DescribeSynchronizationObjectModifyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_synchronization_object_modify_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_object_modify_status_with_options(request, runtime)

    def modify_consumption_timestamp_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumption_timestamp):
            query['ConsumptionTimestamp'] = request.consumption_timestamp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyConsumptionTimestamp',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.ModifyConsumptionTimestampResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_consumption_timestamp(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_consumption_timestamp_with_options(request, runtime)

    def modify_migration_object_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.migration_object):
            query['MigrationObject'] = request.migration_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMigrationObject',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.ModifyMigrationObjectResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_migration_object(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_migration_object_with_options(request, runtime)

    def modify_subscription_object_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not UtilClient.is_unset(request.subscription_object):
            query['SubscriptionObject'] = request.subscription_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySubscriptionObject',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.ModifySubscriptionObjectResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_subscription_object(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_subscription_object_with_options(request, runtime)

    def modify_synchronization_object_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.synchronization_objects):
            query['SynchronizationObjects'] = request.synchronization_objects
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySynchronizationObject',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.ModifySynchronizationObjectResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_synchronization_object(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_synchronization_object_with_options(request, runtime)

    def start_migration_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartMigrationJob',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.StartMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def start_migration_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_migration_job_with_options(request, runtime)

    def start_subscription_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSubscriptionInstance',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.StartSubscriptionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_subscription_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_subscription_instance_with_options(request, runtime)

    def start_synchronization_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSynchronizationJob',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.StartSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def start_synchronization_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_synchronization_job_with_options(request, runtime)

    def stop_migration_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMigrationJob',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.StopMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_migration_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_migration_job_with_options(request, runtime)

    def suspend_migration_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendMigrationJob',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.SuspendMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def suspend_migration_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.suspend_migration_job_with_options(request, runtime)

    def suspend_synchronization_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendSynchronizationJob',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20160801_models.SuspendSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def suspend_synchronization_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.suspend_synchronization_job_with_options(request, runtime)
