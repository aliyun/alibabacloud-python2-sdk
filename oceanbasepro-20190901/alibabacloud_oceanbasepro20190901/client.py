# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_oceanbasepro20190901 import models as ocean_base_pro_20190901_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('oceanbasepro', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.collation):
            body['Collation'] = request.collation
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.encoding):
            body['Encoding'] = request.encoding
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatabase',
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
            ocean_base_pro_20190901_models.CreateDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def create_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_database_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            body['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.disk_size):
            body['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            body['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.instance_class):
            body['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.ob_version):
            body['ObVersion'] = request.ob_version
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            body['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.series):
            body['Series'] = request.series
        if not UtilClient.is_unset(request.zones):
            body['Zones'] = request.zones
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
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
            ocean_base_pro_20190901_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    def create_oms_mysql_data_source_with_options(self, request, runtime):
        """
        The description of the data source.
        It must be 2 to 256 characters in length. The default value is null.
        

        @param request: CreateOmsMysqlDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateOmsMysqlDataSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dg_database_id):
            body['DgDatabaseId'] = request.dg_database_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.schema):
            body['Schema'] = request.schema
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOmsMysqlDataSource',
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
            ocean_base_pro_20190901_models.CreateOmsMysqlDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_oms_mysql_data_source(self, request):
        """
        The description of the data source.
        It must be 2 to 256 characters in length. The default value is null.
        

        @param request: CreateOmsMysqlDataSourceRequest

        @return: CreateOmsMysqlDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_oms_mysql_data_source_with_options(request, runtime)

    def create_oms_open_apiproject_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.CreateOmsOpenAPIProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dest_config):
            request.dest_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dest_config, 'DestConfig', 'json')
        if not UtilClient.is_unset(tmp_req.label_ids):
            request.label_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_ids, 'LabelIds', 'json')
        if not UtilClient.is_unset(tmp_req.source_config):
            request.source_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_config, 'SourceConfig', 'json')
        if not UtilClient.is_unset(tmp_req.transfer_mapping):
            request.transfer_mapping_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transfer_mapping, 'TransferMapping', 'json')
        if not UtilClient.is_unset(tmp_req.transfer_step_config):
            request.transfer_step_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transfer_step_config, 'TransferStepConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.business_name):
            body['BusinessName'] = request.business_name
        if not UtilClient.is_unset(request.dest_config_shrink):
            body['DestConfig'] = request.dest_config_shrink
        if not UtilClient.is_unset(request.label_ids_shrink):
            body['LabelIds'] = request.label_ids_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_config_shrink):
            body['SourceConfig'] = request.source_config_shrink
        if not UtilClient.is_unset(request.transfer_mapping_shrink):
            body['TransferMapping'] = request.transfer_mapping_shrink
        if not UtilClient.is_unset(request.transfer_step_config_shrink):
            body['TransferStepConfig'] = request.transfer_step_config_shrink
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOmsOpenAPIProject',
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
            ocean_base_pro_20190901_models.CreateOmsOpenAPIProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def create_oms_open_apiproject(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_oms_open_apiproject_with_options(request, runtime)

    def create_security_ip_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_ip_group_name):
            body['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.security_ips):
            body['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSecurityIpGroup',
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
            ocean_base_pro_20190901_models.CreateSecurityIpGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_security_ip_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_security_ip_group_with_options(request, runtime)

    def create_tenant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.charset):
            body['Charset'] = request.charset
        if not UtilClient.is_unset(request.cpu):
            body['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.memory):
            body['Memory'] = request.memory
        if not UtilClient.is_unset(request.primary_zone):
            body['PrimaryZone'] = request.primary_zone
        if not UtilClient.is_unset(request.tenant_mode):
            body['TenantMode'] = request.tenant_mode
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        if not UtilClient.is_unset(request.time_zone):
            body['TimeZone'] = request.time_zone
        if not UtilClient.is_unset(request.unit_num):
            body['UnitNum'] = request.unit_num
        if not UtilClient.is_unset(request.user_vswitch_id):
            body['UserVSwitchId'] = request.user_vswitch_id
        if not UtilClient.is_unset(request.user_vpc_id):
            body['UserVpcId'] = request.user_vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTenant',
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
            ocean_base_pro_20190901_models.CreateTenantResponse(),
            self.call_api(params, req, runtime)
        )

    def create_tenant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_tenant_with_options(request, runtime)

    def create_tenant_read_only_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTenantReadOnlyConnection',
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
            ocean_base_pro_20190901_models.CreateTenantReadOnlyConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_tenant_read_only_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_tenant_read_only_connection_with_options(request, runtime)

    def create_tenant_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.encryption_type):
            body['EncryptionType'] = request.encryption_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.roles):
            body['Roles'] = request.roles
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_password):
            body['UserPassword'] = request.user_password
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTenantUser',
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
            ocean_base_pro_20190901_models.CreateTenantUserResponse(),
            self.call_api(params, req, runtime)
        )

    def create_tenant_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_tenant_user_with_options(request, runtime)

    def delete_databases_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database_names):
            body['DatabaseNames'] = request.database_names
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDatabases',
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
            ocean_base_pro_20190901_models.DeleteDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_databases(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_databases_with_options(request, runtime)

    def delete_instances_with_options(self, request, runtime):
        """
        Alibaba Cloud provides SDKs in different languages to help you quickly integrate Alibaba Cloud products and services by using APIs. We recommend that you use an SDK to call APIs. In this way, you do not need to sign for verification.
        

        @param request: DeleteInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteInstancesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backup_retain_mode):
            body['BackupRetainMode'] = request.backup_retain_mode
        if not UtilClient.is_unset(request.instance_ids):
            body['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteInstances',
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
            ocean_base_pro_20190901_models.DeleteInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instances(self, request):
        """
        Alibaba Cloud provides SDKs in different languages to help you quickly integrate Alibaba Cloud products and services by using APIs. We recommend that you use an SDK to call APIs. In this way, you do not need to sign for verification.
        

        @param request: DeleteInstancesRequest

        @return: DeleteInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_instances_with_options(request, runtime)

    def delete_oms_open_apiproject_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteOmsOpenAPIProject',
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
            ocean_base_pro_20190901_models.DeleteOmsOpenAPIProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_oms_open_apiproject(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_oms_open_apiproject_with_options(request, runtime)

    def delete_security_ip_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_ip_group_name):
            body['SecurityIpGroupName'] = request.security_ip_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSecurityIpGroup',
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
            ocean_base_pro_20190901_models.DeleteSecurityIpGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_security_ip_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_security_ip_group_with_options(request, runtime)

    def delete_tenant_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTenantUsers',
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
            ocean_base_pro_20190901_models.DeleteTenantUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_tenant_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_tenant_users_with_options(request, runtime)

    def delete_tenants_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_ids):
            body['TenantIds'] = request.tenant_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTenants',
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
            ocean_base_pro_20190901_models.DeleteTenantsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_tenants(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_tenants_with_options(request, runtime)

    def describe_anomaly_sqllist_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.DescribeAnomalySQLListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_condition):
            request.filter_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_condition, 'FilterCondition', 'json')
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_condition_shrink):
            body['FilterCondition'] = request.filter_condition_shrink
        if not UtilClient.is_unset(request.node_ip):
            body['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.search_key_word):
            body['SearchKeyWord'] = request.search_key_word
        if not UtilClient.is_unset(request.search_parameter):
            body['SearchParameter'] = request.search_parameter
        if not UtilClient.is_unset(request.search_rule):
            body['SearchRule'] = request.search_rule
        if not UtilClient.is_unset(request.search_value):
            body['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.sort_column):
            body['SortColumn'] = request.sort_column
        if not UtilClient.is_unset(request.sort_order):
            body['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAnomalySQLList',
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
            ocean_base_pro_20190901_models.DescribeAnomalySQLListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_anomaly_sqllist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_anomaly_sqllist_with_options(request, runtime)

    def describe_available_cpu_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAvailableCpuResource',
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
            ocean_base_pro_20190901_models.DescribeAvailableCpuResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_cpu_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_cpu_resource_with_options(request, runtime)

    def describe_available_mem_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu_num):
            body['CpuNum'] = request.cpu_num
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.unit_num):
            body['UnitNum'] = request.unit_num
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAvailableMemResource',
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
            ocean_base_pro_20190901_models.DescribeAvailableMemResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_mem_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_mem_resource_with_options(request, runtime)

    def describe_charset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.series):
            body['Series'] = request.series
        if not UtilClient.is_unset(request.tenant_mode):
            body['TenantMode'] = request.tenant_mode
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCharset',
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
            ocean_base_pro_20190901_models.DescribeCharsetResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_charset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_charset_with_options(request, runtime)

    def describe_databases_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.with_tables):
            body['WithTables'] = request.with_tables
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDatabases',
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
            ocean_base_pro_20190901_models.DescribeDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_databases(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_databases_with_options(request, runtime)

    def describe_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
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
            ocean_base_pro_20190901_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    def describe_instance_creatable_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceCreatableZone',
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
            ocean_base_pro_20190901_models.DescribeInstanceCreatableZoneResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_creatable_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_creatable_zone_with_options(request, runtime)

    def describe_instance_security_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSecurityConfigs',
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
            ocean_base_pro_20190901_models.DescribeInstanceSecurityConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_security_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_security_configs_with_options(request, runtime)

    def describe_instance_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_ids):
            body['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTags',
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
            ocean_base_pro_20190901_models.DescribeInstanceTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_tags_with_options(request, runtime)

    def describe_instance_tenant_modes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTenantModes',
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
            ocean_base_pro_20190901_models.DescribeInstanceTenantModesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_tenant_modes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_tenant_modes_with_options(request, runtime)

    def describe_instance_topology_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceTopology',
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
            ocean_base_pro_20190901_models.DescribeInstanceTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_topology(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_topology_with_options(request, runtime)

    def describe_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
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
            ocean_base_pro_20190901_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    def describe_node_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metrics):
            body['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.node_id_list):
            body['NodeIdList'] = request.node_id_list
        if not UtilClient.is_unset(request.node_name):
            body['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNodeMetrics',
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
            ocean_base_pro_20190901_models.DescribeNodeMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_node_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_node_metrics_with_options(request, runtime)

    def describe_oms_open_apiproject_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOmsOpenAPIProject',
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
            ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_oms_open_apiproject(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_oms_open_apiproject_with_options(request, runtime)

    def describe_oms_open_apiproject_steps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOmsOpenAPIProjectSteps',
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
            ocean_base_pro_20190901_models.DescribeOmsOpenAPIProjectStepsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_oms_open_apiproject_steps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_oms_open_apiproject_steps_with_options(request, runtime)

    def describe_outline_binding_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_concurrent_limit):
            body['IsConcurrentLimit'] = request.is_concurrent_limit
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.table_name):
            body['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeOutlineBinding',
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
            ocean_base_pro_20190901_models.DescribeOutlineBindingResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_outline_binding(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_outline_binding_with_options(request, runtime)

    def describe_parameters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimension):
            body['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.dimension_value):
            body['DimensionValue'] = request.dimension_value
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeParameters',
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
            ocean_base_pro_20190901_models.DescribeParametersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_parameters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    def describe_parameters_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimension):
            body['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.dimension_value):
            body['DimensionValue'] = request.dimension_value
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeParametersHistory',
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
            ocean_base_pro_20190901_models.DescribeParametersHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_parameters_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_history_with_options(request, runtime)

    def describe_recommend_index_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRecommendIndex',
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
            ocean_base_pro_20190901_models.DescribeRecommendIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_recommend_index(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_recommend_index_with_options(request, runtime)

    def describe_sqldetails_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSQLDetails',
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
            ocean_base_pro_20190901_models.DescribeSQLDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sqldetails(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqldetails_with_options(request, runtime)

    def describe_sqlhistory_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSQLHistoryList',
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
            ocean_base_pro_20190901_models.DescribeSQLHistoryListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sqlhistory_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlhistory_list_with_options(request, runtime)

    def describe_sqlplans_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSQLPlans',
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
            ocean_base_pro_20190901_models.DescribeSQLPlansResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sqlplans(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlplans_with_options(request, runtime)

    def describe_security_ip_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSecurityIpGroups',
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
            ocean_base_pro_20190901_models.DescribeSecurityIpGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_security_ip_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_ip_groups_with_options(request, runtime)

    def describe_slow_sqlhistory_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSlowSQLHistoryList',
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
            ocean_base_pro_20190901_models.DescribeSlowSQLHistoryListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_slow_sqlhistory_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_sqlhistory_list_with_options(request, runtime)

    def describe_slow_sqllist_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.DescribeSlowSQLListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_condition):
            request.filter_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_condition, 'FilterCondition', 'json')
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_condition_shrink):
            body['FilterCondition'] = request.filter_condition_shrink
        if not UtilClient.is_unset(request.node_ip):
            body['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.search_key_word):
            body['SearchKeyWord'] = request.search_key_word
        if not UtilClient.is_unset(request.search_parameter):
            body['SearchParameter'] = request.search_parameter
        if not UtilClient.is_unset(request.search_rule):
            body['SearchRule'] = request.search_rule
        if not UtilClient.is_unset(request.search_value):
            body['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.sort_column):
            body['SortColumn'] = request.sort_column
        if not UtilClient.is_unset(request.sort_order):
            body['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSlowSQLList',
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
            ocean_base_pro_20190901_models.DescribeSlowSQLListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_slow_sqllist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_sqllist_with_options(request, runtime)

    def describe_tenant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenant',
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
            ocean_base_pro_20190901_models.DescribeTenantResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tenant(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_with_options(request, runtime)

    def describe_tenant_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metrics):
            body['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.tenant_id_list):
            body['TenantIdList'] = request.tenant_id_list
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantMetrics',
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
            ocean_base_pro_20190901_models.DescribeTenantMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tenant_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_metrics_with_options(request, runtime)

    def describe_tenant_security_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantSecurityConfigs',
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
            ocean_base_pro_20190901_models.DescribeTenantSecurityConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tenant_security_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_security_configs_with_options(request, runtime)

    def describe_tenant_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.tenant_ids):
            body['TenantIds'] = request.tenant_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantTags',
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
            ocean_base_pro_20190901_models.DescribeTenantTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tenant_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_tags_with_options(request, runtime)

    def describe_tenant_user_roles_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeTenantUserRoles',
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
            ocean_base_pro_20190901_models.DescribeTenantUserRolesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tenant_user_roles(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_user_roles_with_options(runtime)

    def describe_tenant_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantUsers',
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
            ocean_base_pro_20190901_models.DescribeTenantUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tenant_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_users_with_options(request, runtime)

    def describe_tenant_zones_read_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenantZonesRead',
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
            ocean_base_pro_20190901_models.DescribeTenantZonesReadResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tenant_zones_read(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tenant_zones_read_with_options(request, runtime)

    def describe_tenants_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTenants',
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
            ocean_base_pro_20190901_models.DescribeTenantsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tenants(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tenants_with_options(request, runtime)

    def describe_time_zones_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeTimeZones',
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
            ocean_base_pro_20190901_models.DescribeTimeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_time_zones(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_time_zones_with_options(runtime)

    def describe_top_sqllist_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.DescribeTopSQLListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_condition):
            request.filter_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_condition, 'FilterCondition', 'json')
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_condition_shrink):
            body['FilterCondition'] = request.filter_condition_shrink
        if not UtilClient.is_unset(request.node_ip):
            body['NodeIp'] = request.node_ip
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqlid):
            body['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.search_key_word):
            body['SearchKeyWord'] = request.search_key_word
        if not UtilClient.is_unset(request.search_parameter):
            body['SearchParameter'] = request.search_parameter
        if not UtilClient.is_unset(request.search_rule):
            body['SearchRule'] = request.search_rule
        if not UtilClient.is_unset(request.search_value):
            body['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.sort_column):
            body['SortColumn'] = request.sort_column
        if not UtilClient.is_unset(request.sort_order):
            body['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTopSQLList',
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
            ocean_base_pro_20190901_models.DescribeTopSQLListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_top_sqllist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_top_sqllist_with_options(request, runtime)

    def describe_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.deploy_type):
            body['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.series):
            body['Series'] = request.series
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeZones',
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
            ocean_base_pro_20190901_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    def kill_process_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.session_list):
            body['SessionList'] = request.session_list
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KillProcessList',
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
            ocean_base_pro_20190901_models.KillProcessListResponse(),
            self.call_api(params, req, runtime)
        )

    def kill_process_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.kill_process_list_with_options(request, runtime)

    def modify_database_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseDescription',
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
            ocean_base_pro_20190901_models.ModifyDatabaseDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_database_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_database_description_with_options(request, runtime)

    def modify_database_user_roles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.database_name):
            body['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseUserRoles',
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
            ocean_base_pro_20190901_models.ModifyDatabaseUserRolesResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_database_user_roles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_database_user_roles_with_options(request, runtime)

    def modify_instance_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceName',
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
            ocean_base_pro_20190901_models.ModifyInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_name_with_options(request, runtime)

    def modify_instance_node_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_num):
            body['NodeNum'] = request.node_num
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceNodeNum',
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
            ocean_base_pro_20190901_models.ModifyInstanceNodeNumResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_node_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_node_num_with_options(request, runtime)

    def modify_instance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.disk_size):
            body['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.instance_class):
            body['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSpec',
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
            ocean_base_pro_20190901_models.ModifyInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_spec_with_options(request, runtime)

    def modify_instance_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceTags',
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
            ocean_base_pro_20190901_models.ModifyInstanceTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_tags_with_options(request, runtime)

    def modify_parameters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dimension):
            body['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.dimension_value):
            body['DimensionValue'] = request.dimension_value
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyParameters',
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
            ocean_base_pro_20190901_models.ModifyParametersResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_parameters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_parameters_with_options(request, runtime)

    def modify_security_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.security_ip_group_name):
            body['SecurityIpGroupName'] = request.security_ip_group_name
        if not UtilClient.is_unset(request.security_ips):
            body['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
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
            ocean_base_pro_20190901_models.ModifySecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_security_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    def modify_tenant_primary_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.master_intranet_address_zone):
            body['MasterIntranetAddressZone'] = request.master_intranet_address_zone
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.primary_zone):
            body['PrimaryZone'] = request.primary_zone
        if not UtilClient.is_unset(request.primary_zone_deploy_type):
            body['PrimaryZoneDeployType'] = request.primary_zone_deploy_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_vswitch_id):
            body['UserVSwitchId'] = request.user_vswitch_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantPrimaryZone',
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
            ocean_base_pro_20190901_models.ModifyTenantPrimaryZoneResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_tenant_primary_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_primary_zone_with_options(request, runtime)

    def modify_tenant_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu):
            body['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.memory):
            body['Memory'] = request.memory
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantResource',
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
            ocean_base_pro_20190901_models.ModifyTenantResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_tenant_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_resource_with_options(request, runtime)

    def modify_tenant_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantTags',
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
            ocean_base_pro_20190901_models.ModifyTenantTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_tenant_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_tags_with_options(request, runtime)

    def modify_tenant_user_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantUserDescription',
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
            ocean_base_pro_20190901_models.ModifyTenantUserDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_tenant_user_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_user_description_with_options(request, runtime)

    def modify_tenant_user_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.encryption_type):
            body['EncryptionType'] = request.encryption_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_password):
            body['UserPassword'] = request.user_password
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantUserPassword',
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
            ocean_base_pro_20190901_models.ModifyTenantUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_tenant_user_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_user_password_with_options(request, runtime)

    def modify_tenant_user_roles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_role):
            body['UserRole'] = request.user_role
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantUserRoles',
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
            ocean_base_pro_20190901_models.ModifyTenantUserRolesResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_tenant_user_roles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_user_roles_with_options(request, runtime)

    def modify_tenant_user_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_status):
            body['UserStatus'] = request.user_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTenantUserStatus',
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
            ocean_base_pro_20190901_models.ModifyTenantUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_tenant_user_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_tenant_user_status_with_options(request, runtime)

    def release_oms_open_apiproject_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseOmsOpenAPIProject',
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
            ocean_base_pro_20190901_models.ReleaseOmsOpenAPIProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def release_oms_open_apiproject(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_oms_open_apiproject_with_options(request, runtime)

    def reset_oms_open_apiproject_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetOmsOpenAPIProject',
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
            ocean_base_pro_20190901_models.ResetOmsOpenAPIProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_oms_open_apiproject(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_oms_open_apiproject_with_options(request, runtime)

    def resume_oms_open_apiproject_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeOmsOpenAPIProject',
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
            ocean_base_pro_20190901_models.ResumeOmsOpenAPIProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_oms_open_apiproject(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_oms_open_apiproject_with_options(request, runtime)

    def search_oms_open_apimonitor_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.begin_time):
            body['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_point_num):
            body['MaxPointNum'] = request.max_point_num
        if not UtilClient.is_unset(request.metric):
            body['Metric'] = request.metric
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchOmsOpenAPIMonitorMetric',
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
            ocean_base_pro_20190901_models.SearchOmsOpenAPIMonitorMetricResponse(),
            self.call_api(params, req, runtime)
        )

    def search_oms_open_apimonitor_metric(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_oms_open_apimonitor_metric_with_options(request, runtime)

    def search_oms_open_apiprojects_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = ocean_base_pro_20190901_models.SearchOmsOpenAPIProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dest_db_types):
            request.dest_db_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dest_db_types, 'DestDbTypes', 'json')
        if not UtilClient.is_unset(tmp_req.label_ids):
            request.label_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_ids, 'LabelIds', 'json')
        if not UtilClient.is_unset(tmp_req.source_db_types):
            request.source_db_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_db_types, 'SourceDbTypes', 'json')
        if not UtilClient.is_unset(tmp_req.status_list):
            request.status_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        body = {}
        if not UtilClient.is_unset(request.dest_db_types_shrink):
            body['DestDbTypes'] = request.dest_db_types_shrink
        if not UtilClient.is_unset(request.label_ids_shrink):
            body['LabelIds'] = request.label_ids_shrink
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            body['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.source_db_types_shrink):
            body['SourceDbTypes'] = request.source_db_types_shrink
        if not UtilClient.is_unset(request.status_list_shrink):
            body['StatusList'] = request.status_list_shrink
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchOmsOpenAPIProjects',
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
            ocean_base_pro_20190901_models.SearchOmsOpenAPIProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    def search_oms_open_apiprojects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_oms_open_apiprojects_with_options(request, runtime)

    def start_oms_open_apiproject_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartOmsOpenAPIProject',
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
            ocean_base_pro_20190901_models.StartOmsOpenAPIProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def start_oms_open_apiproject(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_oms_open_apiproject_with_options(request, runtime)

    def stop_oms_open_apiproject_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.worker_grade_id):
            body['WorkerGradeId'] = request.worker_grade_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopOmsOpenAPIProject',
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
            ocean_base_pro_20190901_models.StopOmsOpenAPIProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_oms_open_apiproject(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_oms_open_apiproject_with_options(request, runtime)
