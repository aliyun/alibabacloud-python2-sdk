# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sddp20190103 import models as sddp_20190103_models
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
            'cn-hongkong': 'sddp-api.cn-hongkong.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('sddp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_config_with_options(self, request, runtime):
        """
        You can call this operation to create or restore configurations based on the codes of common configuration items. This allows you to manage the configurations of common configuration items.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: CreateConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConfig',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def create_config(self, request):
        """
        You can call this operation to create or restore configurations based on the codes of common configuration items. This allows you to manage the configurations of common configuration items.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: CreateConfigRequest

        @return: CreateConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_config_with_options(request, runtime)

    def create_data_limit_with_options(self, request, runtime):
        """
        You can call this operation to authorize DSC to scan data assets to ensure the security of the data assets.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: CreateDataLimitRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDataLimitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.auto_scan):
            query['AutoScan'] = request.auto_scan
        if not UtilClient.is_unset(request.certificate_permission):
            query['CertificatePermission'] = request.certificate_permission
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.engine_type):
            query['EngineType'] = request.engine_type
        if not UtilClient.is_unset(request.event_status):
            query['EventStatus'] = request.event_status
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_store_day):
            query['LogStoreDay'] = request.log_store_day
        if not UtilClient.is_unset(request.ocr_status):
            query['OcrStatus'] = request.ocr_status
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sampling_size):
            query['SamplingSize'] = request.sampling_size
        if not UtilClient.is_unset(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataLimit',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateDataLimitResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_limit(self, request):
        """
        You can call this operation to authorize DSC to scan data assets to ensure the security of the data assets.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: CreateDataLimitRequest

        @return: CreateDataLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_limit_with_options(request, runtime)

    def create_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.content_category):
            query['ContentCategory'] = request.content_category
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.stat_express):
            query['StatExpress'] = request.stat_express
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.support_form):
            query['SupportForm'] = request.support_form
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.warn_level):
            query['WarnLevel'] = request.warn_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    def create_scan_task_with_options(self, request, runtime):
        """
        You can call this operation to create a custom scan task for authorized data assets. You can customize the interval between two consecutive scan tasks and the time when the scan task is executed next time.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: CreateScanTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateScanTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_limit_id):
            query['DataLimitId'] = request.data_limit_id
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.interval_day):
            query['IntervalDay'] = request.interval_day
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.oss_scan_path):
            query['OssScanPath'] = request.oss_scan_path
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.run_hour):
            query['RunHour'] = request.run_hour
        if not UtilClient.is_unset(request.run_minute):
            query['RunMinute'] = request.run_minute
        if not UtilClient.is_unset(request.scan_range):
            query['ScanRange'] = request.scan_range
        if not UtilClient.is_unset(request.scan_range_content):
            query['ScanRangeContent'] = request.scan_range_content
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_user_name):
            query['TaskUserName'] = request.task_user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScanTask',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_scan_task(self, request):
        """
        You can call this operation to create a custom scan task for authorized data assets. You can customize the interval between two consecutive scan tasks and the time when the scan task is executed next time.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: CreateScanTaskRequest

        @return: CreateScanTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scan_task_with_options(request, runtime)

    def create_slr_role_with_options(self, request, runtime):
        """
        You can call this operation to allow DSC to access the data assets in services such as Object Storage Service (OSS), ApsaraDB RDS, and MaxCompute. After you call this operation, the system automatically creates a service-linked role named AliyunServiceRoleForSDDP and attaches the AliyunServiceRolePolicyForSDDP policy to the role.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: CreateSlrRoleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSlrRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSlrRole',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateSlrRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_slr_role(self, request):
        """
        You can call this operation to allow DSC to access the data assets in services such as Object Storage Service (OSS), ApsaraDB RDS, and MaxCompute. After you call this operation, the system automatically creates a service-linked role named AliyunServiceRoleForSDDP and attaches the AliyunServiceRolePolicyForSDDP policy to the role.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: CreateSlrRoleRequest

        @return: CreateSlrRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_slr_role_with_options(request, runtime)

    def delete_data_limit_with_options(self, request, runtime):
        """
        You can call this operation to revoke the permissions on a data asset from Data Security Center (DSC).
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DeleteDataLimitRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDataLimitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataLimit',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DeleteDataLimitResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_limit(self, request):
        """
        You can call this operation to revoke the permissions on a data asset from Data Security Center (DSC).
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DeleteDataLimitRequest

        @return: DeleteDataLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_limit_with_options(request, runtime)

    def delete_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRule',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DeleteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    def describe_category_template_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.usage_scenario):
            query['UsageScenario'] = request.usage_scenario
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCategoryTemplateList',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeCategoryTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_category_template_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_category_template_list_with_options(request, runtime)

    def describe_category_template_rule_list_with_options(self, request, runtime):
        """
        You can call this operation to query rules in a classification template.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeCategoryTemplateRuleListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCategoryTemplateRuleListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCategoryTemplateRuleList',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeCategoryTemplateRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_category_template_rule_list(self, request):
        """
        You can call this operation to query rules in a classification template.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeCategoryTemplateRuleListRequest

        @return: DescribeCategoryTemplateRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_category_template_rule_list_with_options(request, runtime)

    def describe_columns_with_options(self, request, runtime):
        """
        You can call this operation to query the data in columns of a table that may contain sensitive data. This helps you analyze sensitive data.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeColumnsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeColumnsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.sens_level_name):
            query['SensLevelName'] = request.sens_level_name
        if not UtilClient.is_unset(request.table_id):
            query['TableId'] = request.table_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColumns',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_columns(self, request):
        """
        You can call this operation to query the data in columns of a table that may contain sensitive data. This helps you analyze sensitive data.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeColumnsRequest

        @return: DescribeColumnsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_columns_with_options(request, runtime)

    def describe_columns_v2with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.sens_level_name):
            query['SensLevelName'] = request.sens_level_name
        if not UtilClient.is_unset(request.table_id):
            query['TableId'] = request.table_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeColumnsV2',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeColumnsV2Response(),
            self.call_api(params, req, runtime)
        )

    def describe_columns_v2(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_columns_v2with_options(request, runtime)

    def describe_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfigs',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_configs_with_options(request, runtime)

    def describe_data_assets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.range_id):
            query['RangeId'] = request.range_id
        if not UtilClient.is_unset(request.risk_levels):
            query['RiskLevels'] = request.risk_levels
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataAssets',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_assets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_assets_with_options(request, runtime)

    def describe_data_limit_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataLimitDetail',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataLimitDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_limit_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_limit_detail_with_options(request, runtime)

    def describe_data_limit_set_with_options(self, request, runtime):
        """
        You can call this operation to query the data assets that are authorized to be scanned. This facilitates resource search and aggregation.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDataLimitSetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDataLimitSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataLimitSet',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataLimitSetResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_limit_set(self, request):
        """
        You can call this operation to query the data assets that are authorized to be scanned. This facilitates resource search and aggregation.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDataLimitSetRequest

        @return: DescribeDataLimitSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_limit_set_with_options(request, runtime)

    def describe_data_limits_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.check_status):
            query['CheckStatus'] = request.check_status
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.datamask_status):
            query['DatamaskStatus'] = request.datamask_status
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.engine_type):
            query['EngineType'] = request.engine_type
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataLimits',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataLimitsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_limits(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_limits_with_options(request, runtime)

    def describe_data_masking_run_history_with_options(self, request, runtime):
        """
        You can call this operation to query the execution information of a static de-identification task, including the status and progress.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDataMaskingRunHistoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDataMaskingRunHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dst_type):
            query['DstType'] = request.dst_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.main_process_id):
            query['MainProcessId'] = request.main_process_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.src_table_name):
            query['SrcTableName'] = request.src_table_name
        if not UtilClient.is_unset(request.src_type):
            query['SrcType'] = request.src_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataMaskingRunHistory',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataMaskingRunHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_masking_run_history(self, request):
        """
        You can call this operation to query the execution information of a static de-identification task, including the status and progress.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDataMaskingRunHistoryRequest

        @return: DescribeDataMaskingRunHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_masking_run_history_with_options(request, runtime)

    def describe_data_masking_tasks_with_options(self, request, runtime):
        """
        You can call this operation to query static de-identification tasks. This facilitates task queries and management.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDataMaskingTasksRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDataMaskingTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dst_type):
            query['DstType'] = request.dst_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataMaskingTasks',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataMaskingTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_masking_tasks(self, request):
        """
        You can call this operation to query static de-identification tasks. This facilitates task queries and management.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeDataMaskingTasksRequest

        @return: DescribeDataMaskingTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_masking_tasks_with_options(request, runtime)

    def describe_data_object_column_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataObjectColumnDetail',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataObjectColumnDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_object_column_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_object_column_detail_with_options(request, runtime)

    def describe_data_object_column_detail_v2with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataObjectColumnDetailV2',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataObjectColumnDetailV2Response(),
            self.call_api(params, req, runtime)
        )

    def describe_data_object_column_detail_v2(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_object_column_detail_v2with_options(request, runtime)

    def describe_data_objects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.file_category_code):
            query['FileCategoryCode'] = request.file_category_code
        if not UtilClient.is_unset(request.file_type):
            query['FileType'] = request.file_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.model_ids):
            query['ModelIds'] = request.model_ids
        if not UtilClient.is_unset(request.model_tag_ids):
            query['ModelTagIds'] = request.model_tag_ids
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_category_ids):
            query['ParentCategoryIds'] = request.parent_category_ids
        if not UtilClient.is_unset(request.product_ids):
            query['ProductIds'] = request.product_ids
        if not UtilClient.is_unset(request.query_name):
            query['QueryName'] = request.query_name
        if not UtilClient.is_unset(request.risk_levels):
            query['RiskLevels'] = request.risk_levels
        if not UtilClient.is_unset(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataObjects',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_objects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_objects_with_options(request, runtime)

    def describe_doc_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDocTypes',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDocTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_doc_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_doc_types_with_options(request, runtime)

    def describe_event_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventDetail',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_event_detail_with_options(request, runtime)

    def describe_event_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.parent_type_id):
            query['ParentTypeId'] = request.parent_type_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventTypes',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeEventTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_event_types_with_options(request, runtime)

    def describe_events_with_options(self, request, runtime):
        """
        You can call this operation to query anomalous events that may involve data leaks. This helps you search for and handle anomalous events.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeEventsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.deal_user_id):
            query['DealUserId'] = request.deal_user_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.sub_type_code):
            query['SubTypeCode'] = request.sub_type_code
        if not UtilClient.is_unset(request.target_product_code):
            query['TargetProductCode'] = request.target_product_code
        if not UtilClient.is_unset(request.type_code):
            query['TypeCode'] = request.type_code
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEvents',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_events(self, request):
        """
        You can call this operation to query anomalous events that may involve data leaks. This helps you search for and handle anomalous events.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeEventsRequest

        @return: DescribeEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_events_with_options(request, runtime)

    def describe_instance_sources_with_options(self, request, runtime):
        """
        You can call this operation to query the data assets that DSC is not authorized to access. This helps you obtain information about the data assets.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeInstanceSourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeInstanceSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.auth_status):
            query['AuthStatus'] = request.auth_status
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.engine_type):
            query['EngineType'] = request.engine_type
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.search_type):
            query['SearchType'] = request.search_type
        if not UtilClient.is_unset(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSources',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeInstanceSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_sources(self, request):
        """
        You can call this operation to query the data assets that DSC is not authorized to access. This helps you obtain information about the data assets.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeInstanceSourcesRequest

        @return: DescribeInstanceSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_sources_with_options(request, runtime)

    def describe_instances_with_options(self, request, runtime):
        """
        When you call the DescribeInstances operation, you can specify parameters such as Name and RiskLevelId to query data assets that meet filter conditions.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeInstancesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instances(self, request):
        """
        When you call the DescribeInstances operation, you can specify parameters such as Name and RiskLevelId to query data assets that meet filter conditions.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeInstancesRequest

        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    def describe_oss_object_detail_with_options(self, request, runtime):
        """
        You can call this operation to query the details of an OSS object. This helps you locate sensitive data detected in OSS.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeOssObjectDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeOssObjectDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssObjectDetail',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeOssObjectDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_oss_object_detail(self, request):
        """
        You can call this operation to query the details of an OSS object. This helps you locate sensitive data detected in OSS.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeOssObjectDetailRequest

        @return: DescribeOssObjectDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_object_detail_with_options(request, runtime)

    def describe_oss_object_detail_v2with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssObjectDetailV2',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeOssObjectDetailV2Response(),
            self.call_api(params, req, runtime)
        )

    def describe_oss_object_detail_v2(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_object_detail_v2with_options(request, runtime)

    def describe_oss_objects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.file_category_code):
            query['FileCategoryCode'] = request.file_category_code
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.last_scan_time_end):
            query['LastScanTimeEnd'] = request.last_scan_time_end
        if not UtilClient.is_unset(request.last_scan_time_start):
            query['LastScanTimeStart'] = request.last_scan_time_start
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssObjects',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeOssObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_oss_objects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_objects_with_options(request, runtime)

    def describe_packages_with_options(self, request, runtime):
        """
        You can call this operation to query MaxCompute packages that are scanned by DSC. This helps you search for MaxCompute packages and view the summary of MaxCompute packages.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribePackagesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribePackagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePackages',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribePackagesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_packages(self, request):
        """
        You can call this operation to query MaxCompute packages that are scanned by DSC. This helps you search for MaxCompute packages and view the summary of MaxCompute packages.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribePackagesRequest

        @return: DescribePackagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_packages_with_options(request, runtime)

    def describe_risk_levels_with_options(self, request, runtime):
        """
        You can call this operation to query the sensitivity levels that are defined in the current rule template provided by DSC. This helps you learn about the number of times that each sensitivity level is referenced in the rule template and the highest sensitivity level.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeRiskLevelsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRiskLevelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskLevels',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeRiskLevelsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_risk_levels(self, request):
        """
        You can call this operation to query the sensitivity levels that are defined in the current rule template provided by DSC. This helps you learn about the number of times that each sensitivity level is referenced in the rule template and the highest sensitivity level.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeRiskLevelsRequest

        @return: DescribeRiskLevelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_levels_with_options(request, runtime)

    def describe_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.content_category):
            query['ContentCategory'] = request.content_category
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.custom_type):
            query['CustomType'] = request.custom_type
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.keyword_compatible):
            query['KeywordCompatible'] = request.keyword_compatible
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.support_form):
            query['SupportForm'] = request.support_form
        if not UtilClient.is_unset(request.warn_level):
            query['WarnLevel'] = request.warn_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRules',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rules_with_options(request, runtime)

    def describe_tables_with_options(self, request, runtime):
        """
        When you call the DescribeTables operation to query tables, you can specify parameters such as Name and RiskLevelId to filter tables.
        # Limits
        You can send up to 10 requests per second to call this operation by using your Alibaba Cloud account. If you send excessive requests, throttling is implemented, and your business may be affected.
        

        @param request: DescribeTablesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.package_id):
            query['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTables',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tables(self, request):
        """
        When you call the DescribeTables operation to query tables, you can specify parameters such as Name and RiskLevelId to filter tables.
        # Limits
        You can send up to 10 requests per second to call this operation by using your Alibaba Cloud account. If you send excessive requests, throttling is implemented, and your business may be affected.
        

        @param request: DescribeTablesRequest

        @return: DescribeTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tables_with_options(request, runtime)

    def describe_template_all_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplateAllRules',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeTemplateAllRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_template_all_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_template_all_rules_with_options(request, runtime)

    def describe_user_status_with_options(self, request, runtime):
        """
        You can call this operation to query the information about the current account. This helps you get familiar with your account that accesses Data Security Center (DSC).
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeUserStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeUserStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserStatus',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_status(self, request):
        """
        You can call this operation to query the information about the current account. This helps you get familiar with your account that accesses Data Security Center (DSC).
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DescribeUserStatusRequest

        @return: DescribeUserStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_status_with_options(request, runtime)

    def disable_user_config_with_options(self, request, runtime):
        """
        You can call this operation to disable a configuration item based on the code of the configuration item. This helps you modify configurations at the earliest opportunity.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DisableUserConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DisableUserConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableUserConfig',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DisableUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_user_config(self, request):
        """
        You can call this operation to disable a configuration item based on the code of the configuration item. This helps you modify configurations at the earliest opportunity.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DisableUserConfigRequest

        @return: DisableUserConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_user_config_with_options(request, runtime)

    def exec_datamask_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecDatamask',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ExecDatamaskResponse(),
            self.call_api(params, req, runtime)
        )

    def exec_datamask(self, request):
        runtime = util_models.RuntimeOptions()
        return self.exec_datamask_with_options(request, runtime)

    def manual_trigger_masking_process_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ManualTriggerMaskingProcess',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ManualTriggerMaskingProcessResponse(),
            self.call_api(params, req, runtime)
        )

    def manual_trigger_masking_process(self, request):
        runtime = util_models.RuntimeOptions()
        return self.manual_trigger_masking_process_with_options(request, runtime)

    def modify_data_limit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.auto_scan):
            query['AutoScan'] = request.auto_scan
        if not UtilClient.is_unset(request.engine_type):
            query['EngineType'] = request.engine_type
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.log_store_day):
            query['LogStoreDay'] = request.log_store_day
        if not UtilClient.is_unset(request.modify_password):
            query['ModifyPassword'] = request.modify_password
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sampling_size):
            query['SamplingSize'] = request.sampling_size
        if not UtilClient.is_unset(request.security_group_id_list):
            query['SecurityGroupIdList'] = request.security_group_id_list
        if not UtilClient.is_unset(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.v_switch_id_list):
            query['VSwitchIdList'] = request.v_switch_id_list
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDataLimit',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyDataLimitResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_data_limit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_data_limit_with_options(request, runtime)

    def modify_default_level_with_options(self, request, runtime):
        """
        You can call this operation to modify the sensitivity levels of data. This helps you manage the sensitivity levels.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifyDefaultLevelRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDefaultLevelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_id):
            query['DefaultId'] = request.default_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.sensitive_ids):
            query['SensitiveIds'] = request.sensitive_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefaultLevel',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyDefaultLevelResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_default_level(self, request):
        """
        You can call this operation to modify the sensitivity levels of data. This helps you manage the sensitivity levels.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifyDefaultLevelRequest

        @return: ModifyDefaultLevelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_default_level_with_options(request, runtime)

    def modify_event_status_with_options(self, request, runtime):
        """
        You can call this operation to handle anomalous events that involve data leaks. This helps protect your data assets at the earliest opportunity.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifyEventStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyEventStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backed):
            query['Backed'] = request.backed
        if not UtilClient.is_unset(request.deal_reason):
            query['DealReason'] = request.deal_reason
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEventStatus',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyEventStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_event_status(self, request):
        """
        You can call this operation to handle anomalous events that involve data leaks. This helps protect your data assets at the earliest opportunity.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifyEventStatusRequest

        @return: ModifyEventStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_event_status_with_options(request, runtime)

    def modify_event_type_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.sub_type_ids):
            query['SubTypeIds'] = request.sub_type_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEventTypeStatus',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyEventTypeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_event_type_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_event_type_status_with_options(request, runtime)

    def modify_report_task_status_with_options(self, request, runtime):
        """
        You can call this operation to enable or disable the report task. After you activate Data Security Center (DSC), the report task is enabled by default. After you disable the report task, you cannot view statistics that are newly generated in the Report Center module, on the Overview page of the Cloud Native Data Audit module, and in the Data security lab module. Existing statistics are not affected.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifyReportTaskStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyReportTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.report_task_status):
            query['ReportTaskStatus'] = request.report_task_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyReportTaskStatus',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyReportTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_report_task_status(self, request):
        """
        You can call this operation to enable or disable the report task. After you activate Data Security Center (DSC), the report task is enabled by default. After you disable the report task, you cannot view statistics that are newly generated in the Report Center module, on the Overview page of the Cloud Native Data Audit module, and in the Data security lab module. Existing statistics are not affected.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifyReportTaskStatusRequest

        @return: ModifyReportTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_report_task_status_with_options(request, runtime)

    def modify_rule_with_options(self, request, runtime):
        """
        When you call this operation, you must configure request parameters to specify the rule name, rule ID, and rule content.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifyRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_id):
            query['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.support_form):
            query['SupportForm'] = request.support_form
        if not UtilClient.is_unset(request.warn_level):
            query['WarnLevel'] = request.warn_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRule',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_rule(self, request):
        """
        When you call this operation, you must configure request parameters to specify the rule name, rule ID, and rule content.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ModifyRuleRequest

        @return: ModifyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_rule_with_options(request, runtime)

    def modify_rule_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRuleStatus',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyRuleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_rule_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_rule_status_with_options(request, runtime)

    def stop_masking_process_with_options(self, request, runtime):
        """
        You can call this operation to stop a de-identification task that is running. For example, you can stop a de-identification task that is used to de-identify specific data.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: StopMaskingProcessRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopMaskingProcessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMaskingProcess',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.StopMaskingProcessResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_masking_process(self, request):
        """
        You can call this operation to stop a de-identification task that is running. For example, you can stop a de-identification task that is used to de-identify specific data.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: StopMaskingProcessRequest

        @return: StopMaskingProcessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_masking_process_with_options(request, runtime)
