# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dts20190901 import models as dts_20190901_models
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
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
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
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20190901_models.ConfigureSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def configure_synchronization_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.configure_synchronization_job_with_options(request, runtime)

    def configure_synchronization_job_alert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not UtilClient.is_unset(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not UtilClient.is_unset(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not UtilClient.is_unset(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not UtilClient.is_unset(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSynchronizationJobAlert',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20190901_models.ConfigureSynchronizationJobAlertResponse(),
            self.call_api(params, req, runtime)
        )

    def configure_synchronization_job_alert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.configure_synchronization_job_alert_with_options(request, runtime)

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
        if not UtilClient.is_unset(request.topology):
            query['Topology'] = request.topology
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
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20190901_models.CreateSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_synchronization_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_synchronization_job_with_options(request, runtime)

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
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20190901_models.DeleteSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_synchronization_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_synchronization_job_with_options(request, runtime)

    def describe_endpoint_switch_status_with_options(self, request, runtime):
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
            action='DescribeEndpointSwitchStatus',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20190901_models.DescribeEndpointSwitchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_endpoint_switch_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_endpoint_switch_status_with_options(request, runtime)

    def describe_synchronization_job_alert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobAlert',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20190901_models.DescribeSynchronizationJobAlertResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_synchronization_job_alert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_alert_with_options(request, runtime)

    def describe_synchronization_job_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobStatus',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20190901_models.DescribeSynchronizationJobStatusResponse(),
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
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20190901_models.DescribeSynchronizationJobsResponse(),
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
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20190901_models.DescribeSynchronizationObjectModifyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_synchronization_object_modify_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_object_modify_status_with_options(request, runtime)

    def modify_synchronization_object_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.synchronization_objects):
            query['SynchronizationObjects'] = request.synchronization_objects
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySynchronizationObject',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20190901_models.ModifySynchronizationObjectResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_synchronization_object(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_synchronization_object_with_options(request, runtime)

    def reset_synchronization_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSynchronizationJob',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20190901_models.ResetSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_synchronization_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_synchronization_job_with_options(request, runtime)

    def start_synchronization_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSynchronizationJob',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20190901_models.StartSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def start_synchronization_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_synchronization_job_with_options(request, runtime)

    def suspend_synchronization_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendSynchronizationJob',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20190901_models.SuspendSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    def suspend_synchronization_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.suspend_synchronization_job_with_options(request, runtime)

    def switch_synchronization_endpoint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchSynchronizationEndpoint',
            version='2019-09-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20190901_models.SwitchSynchronizationEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_synchronization_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_synchronization_endpoint_with_options(request, runtime)
