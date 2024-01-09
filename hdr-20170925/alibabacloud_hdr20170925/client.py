# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_hdr20170925 import models as hdr_20170925_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('hdr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def change_recovery_point_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.eip_address_id):
            query['EipAddressId'] = request.eip_address_id
        if not UtilClient.is_unset(request.recovery_cpu):
            query['RecoveryCpu'] = request.recovery_cpu
        if not UtilClient.is_unset(request.recovery_essd_performance_level):
            query['RecoveryEssdPerformanceLevel'] = request.recovery_essd_performance_level
        if not UtilClient.is_unset(request.recovery_instance_name):
            query['RecoveryInstanceName'] = request.recovery_instance_name
        if not UtilClient.is_unset(request.recovery_instance_type):
            query['RecoveryInstanceType'] = request.recovery_instance_type
        if not UtilClient.is_unset(request.recovery_ip_address):
            query['RecoveryIpAddress'] = request.recovery_ip_address
        if not UtilClient.is_unset(request.recovery_memory):
            query['RecoveryMemory'] = request.recovery_memory
        if not UtilClient.is_unset(request.recovery_network):
            query['RecoveryNetwork'] = request.recovery_network
        if not UtilClient.is_unset(request.recovery_point_id):
            query['RecoveryPointId'] = request.recovery_point_id
        if not UtilClient.is_unset(request.recovery_point_time):
            query['RecoveryPointTime'] = request.recovery_point_time
        if not UtilClient.is_unset(request.recovery_post_script_content):
            query['RecoveryPostScriptContent'] = request.recovery_post_script_content
        if not UtilClient.is_unset(request.recovery_post_script_type):
            query['RecoveryPostScriptType'] = request.recovery_post_script_type
        if not UtilClient.is_unset(request.recovery_reserve_ip):
            query['RecoveryReserveIp'] = request.recovery_reserve_ip
        if not UtilClient.is_unset(request.recovery_use_dhcp):
            query['RecoveryUseDhcp'] = request.recovery_use_dhcp
        if not UtilClient.is_unset(request.recovery_use_essd):
            query['RecoveryUseEssd'] = request.recovery_use_essd
        if not UtilClient.is_unset(request.recovery_use_ssd):
            query['RecoveryUseSsd'] = request.recovery_use_ssd
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeRecoveryPoint',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.ChangeRecoveryPointResponse(),
            self.call_api(params, req, runtime)
        )

    def change_recovery_point(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_recovery_point_with_options(request, runtime)

    def commit_failover_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CommitFailover',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.CommitFailoverResponse(),
            self.call_api(params, req, runtime)
        )

    def commit_failover(self, request):
        runtime = util_models.RuntimeOptions()
        return self.commit_failover_with_options(request, runtime)

    def create_recovery_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.site_pair_id):
            query['SitePairId'] = request.site_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRecoveryPlan',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.CreateRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def create_recovery_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_recovery_plan_with_options(request, runtime)

    def create_site_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.primary_site_name):
            query['PrimarySiteName'] = request.primary_site_name
        if not UtilClient.is_unset(request.primary_site_region_id):
            query['PrimarySiteRegionId'] = request.primary_site_region_id
        if not UtilClient.is_unset(request.primary_site_type):
            query['PrimarySiteType'] = request.primary_site_type
        if not UtilClient.is_unset(request.primary_site_vpc_id):
            query['PrimarySiteVpcId'] = request.primary_site_vpc_id
        if not UtilClient.is_unset(request.primary_site_zone_id):
            query['PrimarySiteZoneId'] = request.primary_site_zone_id
        if not UtilClient.is_unset(request.secondary_site_name):
            query['SecondarySiteName'] = request.secondary_site_name
        if not UtilClient.is_unset(request.secondary_site_region_id):
            query['SecondarySiteRegionId'] = request.secondary_site_region_id
        if not UtilClient.is_unset(request.secondary_site_type):
            query['SecondarySiteType'] = request.secondary_site_type
        if not UtilClient.is_unset(request.secondary_site_vpc_id):
            query['SecondarySiteVpcId'] = request.secondary_site_vpc_id
        if not UtilClient.is_unset(request.secondary_site_zone_id):
            query['SecondarySiteZoneId'] = request.secondary_site_zone_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.site_pair_type):
            query['SitePairType'] = request.site_pair_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSitePair',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.CreateSitePairResponse(),
            self.call_api(params, req, runtime)
        )

    def create_site_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_site_pair_with_options(request, runtime)

    def delete_recovery_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRecoveryPlan',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.DeleteRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_recovery_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_recovery_plan_with_options(request, runtime)

    def delete_site_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.site_pair_id):
            query['SitePairId'] = request.site_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSitePair',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.DeleteSitePairResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_site_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_site_pair_with_options(request, runtime)

    def describe_available_instance_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.user_client):
            query['UserClient'] = request.user_client
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableInstanceTypes',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.DescribeAvailableInstanceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_instance_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_instance_types_with_options(request, runtime)

    def describe_infrastructures_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInfrastructures',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.DescribeInfrastructuresResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_infrastructures(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_infrastructures_with_options(request, runtime)

    def describe_recovery_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecoveryPlan',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.DescribeRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_recovery_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_recovery_plan_with_options(request, runtime)

    def describe_recovery_plans_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.site_pair_id):
            query['SitePairId'] = request.site_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecoveryPlans',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.DescribeRecoveryPlansResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_recovery_plans(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_recovery_plans_with_options(request, runtime)

    def describe_recovery_points_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecoveryPoints',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.DescribeRecoveryPointsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_recovery_points(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_recovery_points_with_options(request, runtime)

    def describe_server_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServer',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.DescribeServerResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_server(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_server_with_options(request, runtime)

    def describe_servers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_ids):
            query['ServerIds'] = request.server_ids
        if not UtilClient.is_unset(request.site_pair_id):
            query['SitePairId'] = request.site_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServers',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.DescribeServersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_servers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_servers_with_options(request, runtime)

    def describe_site_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSite',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.DescribeSiteResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_site(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_site_with_options(request, runtime)

    def describe_site_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.site_pair_id):
            query['SitePairId'] = request.site_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSitePair',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.DescribeSitePairResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_site_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_site_pair_with_options(request, runtime)

    def describe_site_pair_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.site_pair_id):
            query['SitePairId'] = request.site_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSitePairStatistics',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.DescribeSitePairStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_site_pair_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_site_pair_statistics_with_options(request, runtime)

    def describe_site_pairs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.site_pair_type):
            query['SitePairType'] = request.site_pair_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSitePairs',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.DescribeSitePairsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_site_pairs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_site_pairs_with_options(request, runtime)

    def describe_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSummary',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.DescribeSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_summary_with_options(request, runtime)

    def describe_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTask',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.DescribeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_task_with_options(request, runtime)

    def describe_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.site_pair_id):
            query['SitePairId'] = request.site_pair_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    def disable_replication_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableReplication',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.DisableReplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_replication(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_replication_with_options(request, runtime)

    def enable_replication_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.crash_consistent_point_policy):
            query['CrashConsistentPointPolicy'] = request.crash_consistent_point_policy
        if not UtilClient.is_unset(request.recovery_network):
            query['RecoveryNetwork'] = request.recovery_network
        if not UtilClient.is_unset(request.replication_network):
            query['ReplicationNetwork'] = request.replication_network
        if not UtilClient.is_unset(request.replication_use_essd):
            query['ReplicationUseEssd'] = request.replication_use_essd
        if not UtilClient.is_unset(request.replication_use_ssd):
            query['ReplicationUseSsd'] = request.replication_use_ssd
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableReplication',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.EnableReplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_replication(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_replication_with_options(request, runtime)

    def failback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.recovery_cpu):
            query['RecoveryCpu'] = request.recovery_cpu
        if not UtilClient.is_unset(request.recovery_infrastructure_id):
            query['RecoveryInfrastructureId'] = request.recovery_infrastructure_id
        if not UtilClient.is_unset(request.recovery_instance_name):
            query['RecoveryInstanceName'] = request.recovery_instance_name
        if not UtilClient.is_unset(request.recovery_instance_type):
            query['RecoveryInstanceType'] = request.recovery_instance_type
        if not UtilClient.is_unset(request.recovery_ip_address):
            query['RecoveryIpAddress'] = request.recovery_ip_address
        if not UtilClient.is_unset(request.recovery_memory):
            query['RecoveryMemory'] = request.recovery_memory
        if not UtilClient.is_unset(request.recovery_network):
            query['RecoveryNetwork'] = request.recovery_network
        if not UtilClient.is_unset(request.recovery_point_id):
            query['RecoveryPointId'] = request.recovery_point_id
        if not UtilClient.is_unset(request.recovery_post_script_content):
            query['RecoveryPostScriptContent'] = request.recovery_post_script_content
        if not UtilClient.is_unset(request.recovery_post_script_type):
            query['RecoveryPostScriptType'] = request.recovery_post_script_type
        if not UtilClient.is_unset(request.recovery_reserve_ip):
            query['RecoveryReserveIp'] = request.recovery_reserve_ip
        if not UtilClient.is_unset(request.recovery_use_dhcp):
            query['RecoveryUseDhcp'] = request.recovery_use_dhcp
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Failback',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.FailbackResponse(),
            self.call_api(params, req, runtime)
        )

    def failback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.failback_with_options(request, runtime)

    def forced_failover_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.eip_address_id):
            query['EipAddressId'] = request.eip_address_id
        if not UtilClient.is_unset(request.recovery_cpu):
            query['RecoveryCpu'] = request.recovery_cpu
        if not UtilClient.is_unset(request.recovery_essd_performance_level):
            query['RecoveryEssdPerformanceLevel'] = request.recovery_essd_performance_level
        if not UtilClient.is_unset(request.recovery_instance_name):
            query['RecoveryInstanceName'] = request.recovery_instance_name
        if not UtilClient.is_unset(request.recovery_instance_type):
            query['RecoveryInstanceType'] = request.recovery_instance_type
        if not UtilClient.is_unset(request.recovery_ip_address):
            query['RecoveryIpAddress'] = request.recovery_ip_address
        if not UtilClient.is_unset(request.recovery_memory):
            query['RecoveryMemory'] = request.recovery_memory
        if not UtilClient.is_unset(request.recovery_network):
            query['RecoveryNetwork'] = request.recovery_network
        if not UtilClient.is_unset(request.recovery_point_id):
            query['RecoveryPointId'] = request.recovery_point_id
        if not UtilClient.is_unset(request.recovery_point_time):
            query['RecoveryPointTime'] = request.recovery_point_time
        if not UtilClient.is_unset(request.recovery_post_script_content):
            query['RecoveryPostScriptContent'] = request.recovery_post_script_content
        if not UtilClient.is_unset(request.recovery_post_script_type):
            query['RecoveryPostScriptType'] = request.recovery_post_script_type
        if not UtilClient.is_unset(request.recovery_reserve_ip):
            query['RecoveryReserveIp'] = request.recovery_reserve_ip
        if not UtilClient.is_unset(request.recovery_use_dhcp):
            query['RecoveryUseDhcp'] = request.recovery_use_dhcp
        if not UtilClient.is_unset(request.recovery_use_essd):
            query['RecoveryUseEssd'] = request.recovery_use_essd
        if not UtilClient.is_unset(request.recovery_use_ssd):
            query['RecoveryUseSsd'] = request.recovery_use_ssd
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ForcedFailover',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.ForcedFailoverResponse(),
            self.call_api(params, req, runtime)
        )

    def forced_failover(self, request):
        runtime = util_models.RuntimeOptions()
        return self.forced_failover_with_options(request, runtime)

    def register_servers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_port):
            query['AgentPort'] = request.agent_port
        if not UtilClient.is_unset(request.server_instances_info):
            query['ServerInstancesInfo'] = request.server_instances_info
        if not UtilClient.is_unset(request.site_pair_id):
            query['SitePairId'] = request.site_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterServers',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.RegisterServersResponse(),
            self.call_api(params, req, runtime)
        )

    def register_servers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_servers_with_options(request, runtime)

    def reversed_disable_replication_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReversedDisableReplication',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.ReversedDisableReplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def reversed_disable_replication(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reversed_disable_replication_with_options(request, runtime)

    def reversed_enable_replication_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_consistent_point_policy):
            query['AppConsistentPointPolicy'] = request.app_consistent_point_policy
        if not UtilClient.is_unset(request.crash_consistent_point_policy):
            query['CrashConsistentPointPolicy'] = request.crash_consistent_point_policy
        if not UtilClient.is_unset(request.recovery_network):
            query['RecoveryNetwork'] = request.recovery_network
        if not UtilClient.is_unset(request.replication_compute_resource):
            query['ReplicationComputeResource'] = request.replication_compute_resource
        if not UtilClient.is_unset(request.replication_datastore):
            query['ReplicationDatastore'] = request.replication_datastore
        if not UtilClient.is_unset(request.replication_dns):
            query['ReplicationDns'] = request.replication_dns
        if not UtilClient.is_unset(request.replication_gateway):
            query['ReplicationGateway'] = request.replication_gateway
        if not UtilClient.is_unset(request.replication_infrastructure_id):
            query['ReplicationInfrastructureId'] = request.replication_infrastructure_id
        if not UtilClient.is_unset(request.replication_ip_address):
            query['ReplicationIpAddress'] = request.replication_ip_address
        if not UtilClient.is_unset(request.replication_location):
            query['ReplicationLocation'] = request.replication_location
        if not UtilClient.is_unset(request.replication_net_mask):
            query['ReplicationNetMask'] = request.replication_net_mask
        if not UtilClient.is_unset(request.replication_network):
            query['ReplicationNetwork'] = request.replication_network
        if not UtilClient.is_unset(request.replication_use_dhcp):
            query['ReplicationUseDhcp'] = request.replication_use_dhcp
        if not UtilClient.is_unset(request.replication_use_original_instance):
            query['ReplicationUseOriginalInstance'] = request.replication_use_original_instance
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        if not UtilClient.is_unset(request.shadow_instance_type):
            query['ShadowInstanceType'] = request.shadow_instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReversedEnableReplication',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.ReversedEnableReplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def reversed_enable_replication(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reversed_enable_replication_with_options(request, runtime)

    def test_cleanup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TestCleanup',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.TestCleanupResponse(),
            self.call_api(params, req, runtime)
        )

    def test_cleanup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.test_cleanup_with_options(request, runtime)

    def test_failover_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.eip_address_id):
            query['EipAddressId'] = request.eip_address_id
        if not UtilClient.is_unset(request.recovery_cpu):
            query['RecoveryCpu'] = request.recovery_cpu
        if not UtilClient.is_unset(request.recovery_essd_performance_level):
            query['RecoveryEssdPerformanceLevel'] = request.recovery_essd_performance_level
        if not UtilClient.is_unset(request.recovery_instance_name):
            query['RecoveryInstanceName'] = request.recovery_instance_name
        if not UtilClient.is_unset(request.recovery_instance_type):
            query['RecoveryInstanceType'] = request.recovery_instance_type
        if not UtilClient.is_unset(request.recovery_ip_address):
            query['RecoveryIpAddress'] = request.recovery_ip_address
        if not UtilClient.is_unset(request.recovery_memory):
            query['RecoveryMemory'] = request.recovery_memory
        if not UtilClient.is_unset(request.recovery_network):
            query['RecoveryNetwork'] = request.recovery_network
        if not UtilClient.is_unset(request.recovery_point_id):
            query['RecoveryPointId'] = request.recovery_point_id
        if not UtilClient.is_unset(request.recovery_point_time):
            query['RecoveryPointTime'] = request.recovery_point_time
        if not UtilClient.is_unset(request.recovery_post_script_content):
            query['RecoveryPostScriptContent'] = request.recovery_post_script_content
        if not UtilClient.is_unset(request.recovery_post_script_type):
            query['RecoveryPostScriptType'] = request.recovery_post_script_type
        if not UtilClient.is_unset(request.recovery_reserve_ip):
            query['RecoveryReserveIp'] = request.recovery_reserve_ip
        if not UtilClient.is_unset(request.recovery_use_dhcp):
            query['RecoveryUseDhcp'] = request.recovery_use_dhcp
        if not UtilClient.is_unset(request.recovery_use_essd):
            query['RecoveryUseEssd'] = request.recovery_use_essd
        if not UtilClient.is_unset(request.recovery_use_ssd):
            query['RecoveryUseSsd'] = request.recovery_use_ssd
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TestFailover',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.TestFailoverResponse(),
            self.call_api(params, req, runtime)
        )

    def test_failover(self, request):
        runtime = util_models.RuntimeOptions()
        return self.test_failover_with_options(request, runtime)

    def trigger_reversed_register_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerReversedRegister',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.TriggerReversedRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    def trigger_reversed_register(self, request):
        runtime = util_models.RuntimeOptions()
        return self.trigger_reversed_register_with_options(request, runtime)

    def unregister_server_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnregisterServer',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.UnregisterServerResponse(),
            self.call_api(params, req, runtime)
        )

    def unregister_server(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unregister_server_with_options(request, runtime)

    def update_recovery_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.recovery_plan_id):
            query['RecoveryPlanId'] = request.recovery_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRecoveryPlan',
            version='2017-09-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hdr_20170925_models.UpdateRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def update_recovery_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_recovery_plan_with_options(request, runtime)
