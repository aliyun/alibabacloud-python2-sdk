# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_xtee20210910 import models as xtee_20210910_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._signature_algorithm = 'v2'
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('xtee', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def bind_variable_with_options(self, request, runtime):
        """
        @summary 变量绑定操作
        

        @param request: BindVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BindVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.api_region_id):
            query['apiRegionId'] = request.api_region_id
        if not UtilClient.is_unset(request.api_type):
            query['apiType'] = request.api_type
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.define_id):
            query['defineId'] = request.define_id
        if not UtilClient.is_unset(request.define_ids):
            query['defineIds'] = request.define_ids
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.exception_value):
            query['exceptionValue'] = request.exception_value
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.output_field):
            query['outputField'] = request.output_field
        if not UtilClient.is_unset(request.output_type):
            query['outputType'] = request.output_type
        if not UtilClient.is_unset(request.params):
            query['params'] = request.params
        if not UtilClient.is_unset(request.params_list):
            query['paramsList'] = request.params_list
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.BindVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_variable(self, request):
        """
        @summary 变量绑定操作
        

        @param request: BindVariableRequest

        @return: BindVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_variable_with_options(request, runtime)

    def check_cust_variable_limit_with_options(self, request, runtime):
        """
        @summary 校验累计变量数目是否超过限定值
        

        @param request: CheckCustVariableLimitRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckCustVariableLimitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCustVariableLimit',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CheckCustVariableLimitResponse(),
            self.call_api(params, req, runtime)
        )

    def check_cust_variable_limit(self, request):
        """
        @summary 校验累计变量数目是否超过限定值
        

        @param request: CheckCustVariableLimitRequest

        @return: CheckCustVariableLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_cust_variable_limit_with_options(request, runtime)

    def check_expression_variable_limit_with_options(self, request, runtime):
        """
        @summary 校验创建变量是否超过上限
        

        @param request: CheckExpressionVariableLimitRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckExpressionVariableLimitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckExpressionVariableLimit',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CheckExpressionVariableLimitResponse(),
            self.call_api(params, req, runtime)
        )

    def check_expression_variable_limit(self, request):
        """
        @summary 校验创建变量是否超过上限
        

        @param request: CheckExpressionVariableLimitRequest

        @return: CheckExpressionVariableLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_expression_variable_limit_with_options(request, runtime)

    def check_field_limit_with_options(self, request, runtime):
        """
        @summary 校验字段数目是否操过限定值
        

        @param request: CheckFieldLimitRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckFieldLimitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckFieldLimit',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CheckFieldLimitResponse(),
            self.call_api(params, req, runtime)
        )

    def check_field_limit(self, request):
        """
        @summary 校验字段数目是否操过限定值
        

        @param request: CheckFieldLimitRequest

        @return: CheckFieldLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_field_limit_with_options(request, runtime)

    def check_permission_with_options(self, request, runtime):
        """
        @summary 运营权限检查
        

        @param request: CheckPermissionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckPermission',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CheckPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def check_permission(self, request):
        """
        @summary 运营权限检查
        

        @param request: CheckPermissionRequest

        @return: CheckPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_permission_with_options(request, runtime)

    def check_usage_variable_with_options(self, request, runtime):
        """
        @summary 校验变量引用
        

        @param request: CheckUsageVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckUsageVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckUsageVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CheckUsageVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def check_usage_variable(self, request):
        """
        @summary 校验变量引用
        

        @param request: CheckUsageVariableRequest

        @return: CheckUsageVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_usage_variable_with_options(request, runtime)

    def clear_name_list_with_options(self, request, runtime):
        """
        @summary 清除名单
        

        @param request: ClearNameListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ClearNameListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearNameList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.ClearNameListResponse(),
            self.call_api(params, req, runtime)
        )

    def clear_name_list(self, request):
        """
        @summary 清除名单
        

        @param request: ClearNameListRequest

        @return: ClearNameListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.clear_name_list_with_options(request, runtime)

    def create_analysis_condition_favorite_with_options(self, request, runtime):
        """
        @summary 新增查询条件
        

        @param request: CreateAnalysisConditionFavoriteRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAnalysisConditionFavoriteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.condition):
            query['condition'] = request.condition
        if not UtilClient.is_unset(request.event_begin_time):
            query['eventBeginTime'] = request.event_begin_time
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.event_end_time):
            query['eventEndTime'] = request.event_end_time
        if not UtilClient.is_unset(request.field_name):
            query['fieldName'] = request.field_name
        if not UtilClient.is_unset(request.field_value):
            query['fieldValue'] = request.field_value
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAnalysisConditionFavorite',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateAnalysisConditionFavoriteResponse(),
            self.call_api(params, req, runtime)
        )

    def create_analysis_condition_favorite(self, request):
        """
        @summary 新增查询条件
        

        @param request: CreateAnalysisConditionFavoriteRequest

        @return: CreateAnalysisConditionFavoriteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_analysis_condition_favorite_with_options(request, runtime)

    def create_analysis_export_task_with_options(self, request, runtime):
        """
        @summary 新建导出任务
        

        @param request: CreateAnalysisExportTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAnalysisExportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.columns):
            query['columns'] = request.columns
        if not UtilClient.is_unset(request.conditions):
            query['conditions'] = request.conditions
        if not UtilClient.is_unset(request.event_begin_time):
            query['eventBeginTime'] = request.event_begin_time
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.event_end_time):
            query['eventEndTime'] = request.event_end_time
        if not UtilClient.is_unset(request.field_name):
            query['fieldName'] = request.field_name
        if not UtilClient.is_unset(request.field_value):
            query['fieldValue'] = request.field_value
        if not UtilClient.is_unset(request.file_format):
            query['fileFormat'] = request.file_format
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAnalysisExportTask',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateAnalysisExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_analysis_export_task(self, request):
        """
        @summary 新建导出任务
        

        @param request: CreateAnalysisExportTaskRequest

        @return: CreateAnalysisExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_analysis_export_task_with_options(request, runtime)

    def create_app_key_with_options(self, request, runtime):
        """
        @summary 创建appKey
        

        @param request: CreateAppKeyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAppKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppKey',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app_key(self, request):
        """
        @summary 创建appKey
        

        @param request: CreateAppKeyRequest

        @return: CreateAppKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_key_with_options(request, runtime)

    def create_authorization_user_with_options(self, request, runtime):
        """
        @summary 新增用户授权
        

        @param request: CreateAuthorizationUserRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAuthorizationUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.bind_id):
            query['bindId'] = request.bind_id
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.event_template_id):
            query['eventTemplateId'] = request.event_template_id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAuthorizationUser',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateAuthorizationUserResponse(),
            self.call_api(params, req, runtime)
        )

    def create_authorization_user(self, request):
        """
        @summary 新增用户授权
        

        @param request: CreateAuthorizationUserRequest

        @return: CreateAuthorizationUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_authorization_user_with_options(request, runtime)

    def create_cust_variable_with_options(self, request, runtime):
        """
        @summary 创建累计变量
        

        @param request: CreateCustVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCustVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.condition):
            query['condition'] = request.condition
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.history_value_type):
            query['historyValueType'] = request.history_value_type
        if not UtilClient.is_unset(request.object):
            query['object'] = request.object
        if not UtilClient.is_unset(request.outputs):
            query['outputs'] = request.outputs
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.subject):
            query['subject'] = request.subject
        if not UtilClient.is_unset(request.time_type):
            query['timeType'] = request.time_type
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
        if not UtilClient.is_unset(request.tw_count):
            query['twCount'] = request.tw_count
        if not UtilClient.is_unset(request.velocity_fc):
            query['velocityFC'] = request.velocity_fc
        if not UtilClient.is_unset(request.velocity_tw):
            query['velocityTW'] = request.velocity_tw
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateCustVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cust_variable(self, request):
        """
        @summary 创建累计变量
        

        @param request: CreateCustVariableRequest

        @return: CreateCustVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cust_variable_with_options(request, runtime)

    def create_data_source_with_options(self, request, runtime):
        """
        @summary 新增数据源
        

        @param request: CreateDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.oss_key):
            query['ossKey'] = request.oss_key
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataSource',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_source(self, request):
        """
        @summary 新增数据源
        

        @param request: CreateDataSourceRequest

        @return: CreateDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_source_with_options(request, runtime)

    def create_event_with_options(self, request, runtime):
        """
        @summary 创建事件
        

        @param request: CreateEventRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.event_name):
            query['eventName'] = request.event_name
        if not UtilClient.is_unset(request.input_fields_str):
            query['inputFieldsStr'] = request.input_fields_str
        if not UtilClient.is_unset(request.memo):
            query['memo'] = request.memo
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.template_code):
            query['templateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_name):
            query['templateName'] = request.template_name
        if not UtilClient.is_unset(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEvent',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateEventResponse(),
            self.call_api(params, req, runtime)
        )

    def create_event(self, request):
        """
        @summary 创建事件
        

        @param request: CreateEventRequest

        @return: CreateEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_event_with_options(request, runtime)

    def create_expression_variable_with_options(self, request, runtime):
        """
        @summary 创建自定义变量
        

        @param request: CreateExpressionVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateExpressionVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.expression):
            query['expression'] = request.expression
        if not UtilClient.is_unset(request.expression_title):
            query['expressionTitle'] = request.expression_title
        if not UtilClient.is_unset(request.expression_variable):
            query['expressionVariable'] = request.expression_variable
        if not UtilClient.is_unset(request.outlier):
            query['outlier'] = request.outlier
        if not UtilClient.is_unset(request.outputs):
            query['outputs'] = request.outputs
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateExpressionVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateExpressionVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def create_expression_variable(self, request):
        """
        @summary 创建自定义变量
        

        @param request: CreateExpressionVariableRequest

        @return: CreateExpressionVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_expression_variable_with_options(request, runtime)

    def create_field_with_options(self, request, runtime):
        """
        @summary 新增字段
        

        @param request: CreateFieldRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateFieldResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.classify):
            query['classify'] = request.classify
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.enum_data):
            query['enumData'] = request.enum_data
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateField',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateFieldResponse(),
            self.call_api(params, req, runtime)
        )

    def create_field(self, request):
        """
        @summary 新增字段
        

        @param request: CreateFieldRequest

        @return: CreateFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_field_with_options(request, runtime)

    def create_group_sign_with_options(self, request, runtime):
        """
        @summary 社群打标
        

        @param request: CreateGroupSignRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateGroupSignResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.sign_list):
            query['SignList'] = request.sign_list
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupSign',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateGroupSignResponse(),
            self.call_api(params, req, runtime)
        )

    def create_group_sign(self, request):
        """
        @summary 社群打标
        

        @param request: CreateGroupSignRequest

        @return: CreateGroupSignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_group_sign_with_options(request, runtime)

    def create_monitor_task_with_options(self, request, runtime):
        """
        @summary 创建监控任务
        

        @param request: CreateMonitorTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateMonitorTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.biz_type):
            query['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.cycle_type):
            query['cycleType'] = request.cycle_type
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.file_path):
            query['filePath'] = request.file_path
        if not UtilClient.is_unset(request.listday_str):
            query['listdayStr'] = request.listday_str
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMonitorTask',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateMonitorTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_monitor_task(self, request):
        """
        @summary 创建监控任务
        

        @param request: CreateMonitorTaskRequest

        @return: CreateMonitorTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_task_with_options(request, runtime)

    def create_poc_with_options(self, request, runtime):
        """
        @summary 创建poc
        

        @param request: CreatePocRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreatePocResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.config_str):
            query['configStr'] = request.config_str
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            query['fileType'] = request.file_type
        if not UtilClient.is_unset(request.file_url):
            query['fileUrl'] = request.file_url
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.service_code):
            query['serviceCode'] = request.service_code
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        if not UtilClient.is_unset(request.task_name):
            query['taskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePoc',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreatePocResponse(),
            self.call_api(params, req, runtime)
        )

    def create_poc(self, request):
        """
        @summary 创建poc
        

        @param request: CreatePocRequest

        @return: CreatePocResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_poc_with_options(request, runtime)

    def create_poc_ev_with_options(self, request, runtime):
        """
        @summary 创建poc
        

        @param request: CreatePocEvRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreatePocEvResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date_format):
            query['DateFormat'] = request.date_format
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            query['FileType'] = request.file_type
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['RegId'] = request.reg_id
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.tab):
            query['Tab'] = request.tab
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePocEv',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreatePocEvResponse(),
            self.call_api(params, req, runtime)
        )

    def create_poc_ev(self, request):
        """
        @summary 创建poc
        

        @param request: CreatePocEvRequest

        @return: CreatePocEvResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_poc_ev_with_options(request, runtime)

    def create_query_variable_with_options(self, request, runtime):
        """
        @summary 自定义查询变量新增
        

        @param request: CreateQueryVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateQueryVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.data_source_code):
            query['dataSourceCode'] = request.data_source_code
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.expression):
            query['expression'] = request.expression
        if not UtilClient.is_unset(request.expression_title):
            query['expressionTitle'] = request.expression_title
        if not UtilClient.is_unset(request.expression_variable):
            query['expressionVariable'] = request.expression_variable
        if not UtilClient.is_unset(request.outlier):
            query['outlier'] = request.outlier
        if not UtilClient.is_unset(request.outputs):
            query['outputs'] = request.outputs
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQueryVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateQueryVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def create_query_variable(self, request):
        """
        @summary 自定义查询变量新增
        

        @param request: CreateQueryVariableRequest

        @return: CreateQueryVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_query_variable_with_options(request, runtime)

    def create_recommend_event_rule_with_options(self, request, runtime):
        """
        @summary 创建推荐事件策略
        

        @param request: CreateRecommendEventRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateRecommendEventRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.event_name):
            query['eventName'] = request.event_name
        if not UtilClient.is_unset(request.recommend_rule_ids_str):
            query['recommendRuleIdsStr'] = request.recommend_rule_ids_str
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRecommendEventRule',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateRecommendEventRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_recommend_event_rule(self, request):
        """
        @summary 创建推荐事件策略
        

        @param request: CreateRecommendEventRuleRequest

        @return: CreateRecommendEventRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_recommend_event_rule_with_options(request, runtime)

    def create_recommend_task_with_options(self, request, runtime):
        """
        @summary 创建推荐任务
        

        @param request: CreateRecommendTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateRecommendTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.sample_id):
            query['sampleId'] = request.sample_id
        if not UtilClient.is_unset(request.variables_str):
            query['variablesStr'] = request.variables_str
        if not UtilClient.is_unset(request.velocities_str):
            query['velocitiesStr'] = request.velocities_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRecommendTask',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateRecommendTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_recommend_task(self, request):
        """
        @summary 创建推荐任务
        

        @param request: CreateRecommendTaskRequest

        @return: CreateRecommendTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_recommend_task_with_options(request, runtime)

    def create_replenish_task_with_options(self, request, runtime):
        """
        @summary 补充上传
        

        @param request: CreateReplenishTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateReplenishTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_file_name):
            query['ClientFileName'] = request.client_file_name
        if not UtilClient.is_unset(request.client_path):
            query['ClientPath'] = request.client_path
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateReplenishTask',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateReplenishTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_replenish_task(self, request):
        """
        @summary 补充上传
        

        @param request: CreateReplenishTaskRequest

        @return: CreateReplenishTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_replenish_task_with_options(request, runtime)

    def create_rule_with_options(self, request, runtime):
        """
        @summary 创建策略&版本
        

        @param request: CreateRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.event_name):
            query['eventName'] = request.event_name
        if not UtilClient.is_unset(request.logic_expression):
            query['logicExpression'] = request.logic_expression
        if not UtilClient.is_unset(request.memo):
            query['memo'] = request.memo
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_actions):
            query['ruleActions'] = request.rule_actions
        if not UtilClient.is_unset(request.rule_expressions):
            query['ruleExpressions'] = request.rule_expressions
        if not UtilClient.is_unset(request.rule_name):
            query['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_status):
            query['ruleStatus'] = request.rule_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_rule(self, request):
        """
        @summary 创建策略&版本
        

        @param request: CreateRuleRequest

        @return: CreateRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    def create_sample_with_options(self, request, runtime):
        """
        @summary 添加样本
        

        @param request: CreateSampleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSampleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.client_file_name):
            query['clientFileName'] = request.client_file_name
        if not UtilClient.is_unset(request.client_path):
            query['clientPath'] = request.client_path
        if not UtilClient.is_unset(request.file_type):
            query['fileType'] = request.file_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.sample_tag):
            query['sampleTag'] = request.sample_tag
        if not UtilClient.is_unset(request.sample_type):
            query['sampleType'] = request.sample_type
        if not UtilClient.is_unset(request.sample_values):
            query['sampleValues'] = request.sample_values
        if not UtilClient.is_unset(request.upload_type):
            query['uploadType'] = request.upload_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSample',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateSampleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_sample(self, request):
        """
        @summary 添加样本
        

        @param request: CreateSampleRequest

        @return: CreateSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sample_with_options(request, runtime)

    def create_sample_api_with_options(self, request, runtime):
        """
        @summary 用户级别单API创建样本批
        

        @param request: CreateSampleApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSampleApiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.data_value):
            query['DataValue'] = request.data_value
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['RegId'] = request.reg_id
        if not UtilClient.is_unset(request.sample_batch_type):
            query['SampleBatchType'] = request.sample_batch_type
        if not UtilClient.is_unset(request.service_list):
            query['ServiceList'] = request.service_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSampleApi',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateSampleApiResponse(),
            self.call_api(params, req, runtime)
        )

    def create_sample_api(self, request):
        """
        @summary 用户级别单API创建样本批
        

        @param request: CreateSampleApiRequest

        @return: CreateSampleApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sample_api_with_options(request, runtime)

    def create_sample_data_with_options(self, request, runtime):
        """
        @summary 创建样本数据
        

        @param request: CreateSampleDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSampleDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.encrypt_type):
            query['encryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.risk_value):
            query['riskValue'] = request.risk_value
        if not UtilClient.is_unset(request.scene):
            query['scene'] = request.scene
        if not UtilClient.is_unset(request.store_path):
            query['storePath'] = request.store_path
        if not UtilClient.is_unset(request.store_type):
            query['storeType'] = request.store_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSampleData',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateSampleDataResponse(),
            self.call_api(params, req, runtime)
        )

    def create_sample_data(self, request):
        """
        @summary 创建样本数据
        

        @param request: CreateSampleDataRequest

        @return: CreateSampleDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sample_data_with_options(request, runtime)

    def create_simulation_task_with_options(self, request, runtime):
        """
        @summary 创建任务
        

        @param request: CreateSimulationTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSimulationTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.data_source_config):
            query['dataSourceConfig'] = request.data_source_config
        if not UtilClient.is_unset(request.data_source_type):
            query['dataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.filters_str):
            query['filtersStr'] = request.filters_str
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rules_str):
            query['rulesStr'] = request.rules_str
        if not UtilClient.is_unset(request.run_task):
            query['runTask'] = request.run_task
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.task_name):
            query['taskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSimulationTask',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateSimulationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_simulation_task(self, request):
        """
        @summary 创建任务
        

        @param request: CreateSimulationTaskRequest

        @return: CreateSimulationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_simulation_task_with_options(request, runtime)

    def create_task_with_options(self, request, runtime):
        """
        @summary 创建任务
        

        @param request: CreateTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_file_name):
            query['ClientFileName'] = request.client_file_name
        if not UtilClient.is_unset(request.client_path):
            query['ClientPath'] = request.client_path
        if not UtilClient.is_unset(request.describe):
            query['Describe'] = request.describe
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_task(self, request):
        """
        @summary 创建任务
        

        @param request: CreateTaskRequest

        @return: CreateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_task_with_options(request, runtime)

    def create_template_with_options(self, request, runtime):
        """
        @summary 创建模版
        

        @param request: CreateTemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.event_name):
            query['eventName'] = request.event_name
        if not UtilClient.is_unset(request.logic_expression):
            query['logicExpression'] = request.logic_expression
        if not UtilClient.is_unset(request.memo):
            query['memo'] = request.memo
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_actions):
            query['ruleActions'] = request.rule_actions
        if not UtilClient.is_unset(request.rule_expressions):
            query['ruleExpressions'] = request.rule_expressions
        if not UtilClient.is_unset(request.rule_name):
            query['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_status):
            query['ruleStatus'] = request.rule_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_template(self, request):
        """
        @summary 创建模版
        

        @param request: CreateTemplateRequest

        @return: CreateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    def delete_analysis_condition_favorite_with_options(self, request, runtime):
        """
        @summary 删除查询条件
        

        @param request: DeleteAnalysisConditionFavoriteRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAnalysisConditionFavoriteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAnalysisConditionFavorite',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DeleteAnalysisConditionFavoriteResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_analysis_condition_favorite(self, request):
        """
        @summary 删除查询条件
        

        @param request: DeleteAnalysisConditionFavoriteRequest

        @return: DeleteAnalysisConditionFavoriteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_analysis_condition_favorite_with_options(request, runtime)

    def delete_auth_user_with_options(self, request, runtime):
        """
        @summary 删除用户授权
        

        @param request: DeleteAuthUserRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAuthUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAuthUser',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DeleteAuthUserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_auth_user(self, request):
        """
        @summary 删除用户授权
        

        @param request: DeleteAuthUserRequest

        @return: DeleteAuthUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_auth_user_with_options(request, runtime)

    def delete_by_pass_shunt_event_with_options(self, request, runtime):
        """
        @summary 删除旁路事件
        

        @param request: DeleteByPassShuntEventRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteByPassShuntEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_id):
            query['eventId'] = request.event_id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteByPassShuntEvent',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DeleteByPassShuntEventResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_by_pass_shunt_event(self, request):
        """
        @summary 删除旁路事件
        

        @param request: DeleteByPassShuntEventRequest

        @return: DeleteByPassShuntEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_by_pass_shunt_event_with_options(request, runtime)

    def delete_cust_variable_with_options(self, request, runtime):
        """
        @summary 删除累计变量
        

        @param request: DeleteCustVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCustVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.data_version):
            query['dataVersion'] = request.data_version
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DeleteCustVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cust_variable(self, request):
        """
        @summary 删除累计变量
        

        @param request: DeleteCustVariableRequest

        @return: DeleteCustVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cust_variable_with_options(request, runtime)

    def delete_data_source_with_options(self, request, runtime):
        """
        @summary 删除数据源
        

        @param request: DeleteDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DeleteDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_source(self, request):
        """
        @summary 删除数据源
        

        @param request: DeleteDataSourceRequest

        @return: DeleteDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    def delete_expression_variable_with_options(self, request, runtime):
        """
        @summary 删除自定义变量
        

        @param request: DeleteExpressionVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteExpressionVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.data_version):
            query['dataVersion'] = request.data_version
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExpressionVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DeleteExpressionVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_expression_variable(self, request):
        """
        @summary 删除自定义变量
        

        @param request: DeleteExpressionVariableRequest

        @return: DeleteExpressionVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_expression_variable_with_options(request, runtime)

    def delete_field_with_options(self, request, runtime):
        """
        @summary 删除字段
        

        @param request: DeleteFieldRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteFieldResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteField',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DeleteFieldResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_field(self, request):
        """
        @summary 删除字段
        

        @param request: DeleteFieldRequest

        @return: DeleteFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_field_with_options(request, runtime)

    def delete_name_list_with_options(self, request, runtime):
        """
        @summary 删除名单
        

        @param request: DeleteNameListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteNameListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.ids):
            query['ids'] = request.ids
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNameList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DeleteNameListResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_name_list(self, request):
        """
        @summary 删除名单
        

        @param request: DeleteNameListRequest

        @return: DeleteNameListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_name_list_with_options(request, runtime)

    def delete_name_list_data_with_options(self, request, runtime):
        """
        @summary 删除(伪)名单变量数据
        

        @param request: DeleteNameListDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteNameListDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNameListData',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DeleteNameListDataResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_name_list_data(self, request):
        """
        @summary 删除(伪)名单变量数据
        

        @param request: DeleteNameListDataRequest

        @return: DeleteNameListDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_name_list_data_with_options(request, runtime)

    def delete_query_variable_with_options(self, request, runtime):
        """
        @summary 查询变量删除
        

        @param request: DeleteQueryVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteQueryVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQueryVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DeleteQueryVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_query_variable(self, request):
        """
        @summary 查询变量删除
        

        @param request: DeleteQueryVariableRequest

        @return: DeleteQueryVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_query_variable_with_options(request, runtime)

    def delete_rule_with_options(self, request, runtime):
        """
        @summary 删除策略版本
        

        @param request: DeleteRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_id):
            query['ruleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRule',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DeleteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_rule(self, request):
        """
        @summary 删除策略版本
        

        @param request: DeleteRuleRequest

        @return: DeleteRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    def delete_sample_batch_with_options(self, request, runtime):
        """
        @summary 批量删除样本
        

        @param request: DeleteSampleBatchRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteSampleBatchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.ids):
            query['ids'] = request.ids
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.versions):
            query['versions'] = request.versions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSampleBatch',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DeleteSampleBatchResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_sample_batch(self, request):
        """
        @summary 批量删除样本
        

        @param request: DeleteSampleBatchRequest

        @return: DeleteSampleBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_sample_batch_with_options(request, runtime)

    def delete_sample_data_with_options(self, request, runtime):
        """
        @summary 删除样本数据
        

        @param request: DeleteSampleDataRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteSampleDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSampleData',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DeleteSampleDataResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_sample_data(self, request):
        """
        @summary 删除样本数据
        

        @param request: DeleteSampleDataRequest

        @return: DeleteSampleDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_sample_data_with_options(request, runtime)

    def delete_task_with_options(self, request, runtime):
        """
        @summary 删除社群任务
        

        @param request: DeleteTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTask',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DeleteTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_task(self, request):
        """
        @summary 删除社群任务
        

        @param request: DeleteTaskRequest

        @return: DeleteTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_task_with_options(request, runtime)

    def describe_advance_search_left_variable_list_with_options(self, request, runtime):
        """
        @summary 高级查询获取左变量接口
        

        @param request: DescribeAdvanceSearchLeftVariableListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAdvanceSearchLeftVariableListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.scene):
            query['scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvanceSearchLeftVariableList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAdvanceSearchLeftVariableListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_advance_search_left_variable_list(self, request):
        """
        @summary 高级查询获取左变量接口
        

        @param request: DescribeAdvanceSearchLeftVariableListRequest

        @return: DescribeAdvanceSearchLeftVariableListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_advance_search_left_variable_list_with_options(request, runtime)

    def describe_advance_search_page_list_with_options(self, request, runtime):
        """
        @summary 高级查询
        

        @param request: DescribeAdvanceSearchPageListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAdvanceSearchPageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.condition):
            query['condition'] = request.condition
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_begin_time):
            query['eventBeginTime'] = request.event_begin_time
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.event_end_time):
            query['eventEndTime'] = request.event_end_time
        if not UtilClient.is_unset(request.field_name):
            query['fieldName'] = request.field_name
        if not UtilClient.is_unset(request.field_value):
            query['fieldValue'] = request.field_value
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvanceSearchPageList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAdvanceSearchPageListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_advance_search_page_list(self, request):
        """
        @summary 高级查询
        

        @param request: DescribeAdvanceSearchPageListRequest

        @return: DescribeAdvanceSearchPageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_advance_search_page_list_with_options(request, runtime)

    def describe_all_data_source_with_options(self, request, runtime):
        """
        @summary 数据源列表
        

        @param request: DescribeAllDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAllDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllDataSource',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAllDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_all_data_source(self, request):
        """
        @summary 数据源列表
        

        @param request: DescribeAllDataSourceRequest

        @return: DescribeAllDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_all_data_source_with_options(request, runtime)

    def describe_all_event_name_and_code_with_options(self, request, runtime):
        """
        @summary 事件列表查询
        

        @param request: DescribeAllEventNameAndCodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAllEventNameAndCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllEventNameAndCode',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAllEventNameAndCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_all_event_name_and_code(self, request):
        """
        @summary 事件列表查询
        

        @param request: DescribeAllEventNameAndCodeRequest

        @return: DescribeAllEventNameAndCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_all_event_name_and_code_with_options(request, runtime)

    def describe_all_root_variable_with_options(self, request, runtime):
        """
        @summary 自定义表达式测试时，展示所有的根变量
        

        @param request: DescribeAllRootVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAllRootVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.device_variable_ids):
            query['deviceVariableIds'] = request.device_variable_ids
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.expression_variable_ids):
            query['expressionVariableIds'] = request.expression_variable_ids
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.native_variable_ids):
            query['nativeVariableIds'] = request.native_variable_ids
        if not UtilClient.is_unset(request.query_variable_ids):
            query['queryVariableIds'] = request.query_variable_ids
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.velocity_variable_ids):
            query['velocityVariableIds'] = request.velocity_variable_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllRootVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAllRootVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_all_root_variable(self, request):
        """
        @summary 自定义表达式测试时，展示所有的根变量
        

        @param request: DescribeAllRootVariableRequest

        @return: DescribeAllRootVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_all_root_variable_with_options(request, runtime)

    def describe_analysis_column_field_list_with_options(self, request, runtime):
        """
        @summary 展示所有字段
        

        @param request: DescribeAnalysisColumnFieldListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAnalysisColumnFieldListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAnalysisColumnFieldList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAnalysisColumnFieldListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_analysis_column_field_list(self, request):
        """
        @summary 展示所有字段
        

        @param request: DescribeAnalysisColumnFieldListRequest

        @return: DescribeAnalysisColumnFieldListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_analysis_column_field_list_with_options(request, runtime)

    def describe_analysis_column_list_with_options(self, request, runtime):
        """
        @summary 查询自定义列
        

        @param request: DescribeAnalysisColumnListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAnalysisColumnListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAnalysisColumnList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAnalysisColumnListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_analysis_column_list(self, request):
        """
        @summary 查询自定义列
        

        @param request: DescribeAnalysisColumnListRequest

        @return: DescribeAnalysisColumnListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_analysis_column_list_with_options(request, runtime)

    def describe_analysis_condition_favorite_list_with_options(self, request, runtime):
        """
        @summary 查询条件列表
        

        @param request: DescribeAnalysisConditionFavoriteListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAnalysisConditionFavoriteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAnalysisConditionFavoriteList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAnalysisConditionFavoriteListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_analysis_condition_favorite_list(self, request):
        """
        @summary 查询条件列表
        

        @param request: DescribeAnalysisConditionFavoriteListRequest

        @return: DescribeAnalysisConditionFavoriteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_analysis_condition_favorite_list_with_options(request, runtime)

    def describe_analysis_export_task_download_url_with_options(self, request, runtime):
        """
        @summary 下载查询结果
        

        @param request: DescribeAnalysisExportTaskDownloadUrlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAnalysisExportTaskDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAnalysisExportTaskDownloadUrl',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAnalysisExportTaskDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_analysis_export_task_download_url(self, request):
        """
        @summary 下载查询结果
        

        @param request: DescribeAnalysisExportTaskDownloadUrlRequest

        @return: DescribeAnalysisExportTaskDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_analysis_export_task_download_url_with_options(request, runtime)

    def describe_api_with_options(self, request, runtime):
        """
        @summary 得到api详情
        

        @param request: DescribeApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.api_id):
            query['apiId'] = request.api_id
        if not UtilClient.is_unset(request.api_region_id):
            query['apiRegionId'] = request.api_region_id
        if not UtilClient.is_unset(request.api_type):
            query['apiType'] = request.api_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApi',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeApiResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api(self, request):
        """
        @summary 得到api详情
        

        @param request: DescribeApiRequest

        @return: DescribeApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_with_options(request, runtime)

    def describe_api_groups_with_options(self, request, runtime):
        """
        @summary 得到api分组包括用户购买的以及自定义的
        

        @param request: DescribeApiGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApiGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.api_region_id):
            query['apiRegionId'] = request.api_region_id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiGroups',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeApiGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_groups(self, request):
        """
        @summary 得到api分组包括用户购买的以及自定义的
        

        @param request: DescribeApiGroupsRequest

        @return: DescribeApiGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_groups_with_options(request, runtime)

    def describe_api_limit_with_options(self, request, runtime):
        """
        @summary 查询创建api任务的limit信息
        

        @param request: DescribeApiLimitRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApiLimitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiLimit',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeApiLimitResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_limit(self, request):
        """
        @summary 查询创建api任务的limit信息
        

        @param request: DescribeApiLimitRequest

        @return: DescribeApiLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_limit_with_options(request, runtime)

    def describe_api_name_list_with_options(self, request, runtime):
        """
        @summary 获取api服务名称
        

        @param request: DescribeApiNameListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApiNameListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiNameList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeApiNameListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_name_list(self, request):
        """
        @summary 获取api服务名称
        

        @param request: DescribeApiNameListRequest

        @return: DescribeApiNameListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_name_list_with_options(request, runtime)

    def describe_api_variable_with_options(self, request, runtime):
        """
        @summary 查询变量详情
        

        @param request: DescribeApiVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApiVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeApiVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_api_variable(self, request):
        """
        @summary 查询变量详情
        

        @param request: DescribeApiVariableRequest

        @return: DescribeApiVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_api_variable_with_options(request, runtime)

    def describe_apis_with_options(self, request, runtime):
        """
        @summary 得到api列表包括用户购买的以及自定义的
        

        @param request: DescribeApisRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.api_group_id):
            query['apiGroupId'] = request.api_group_id
        if not UtilClient.is_unset(request.api_region_id):
            query['apiRegionId'] = request.api_region_id
        if not UtilClient.is_unset(request.api_type):
            query['apiType'] = request.api_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApis',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeApisResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apis(self, request):
        """
        @summary 得到api列表包括用户购买的以及自定义的
        

        @param request: DescribeApisRequest

        @return: DescribeApisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_with_options(request, runtime)

    def describe_app_key_page_with_options(self, request, runtime):
        """
        @summary 查询appKey列表
        

        @param request: DescribeAppKeyPageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAppKeyPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppKeyPage',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAppKeyPageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_key_page(self, request):
        """
        @summary 查询appKey列表
        

        @param request: DescribeAppKeyPageRequest

        @return: DescribeAppKeyPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_app_key_page_with_options(request, runtime)

    def describe_audit_config_with_options(self, request, runtime):
        """
        @summary 审批开关
        

        @param request: DescribeAuditConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAuditConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.audit_relation_type):
            query['auditRelationType'] = request.audit_relation_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditConfig',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAuditConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_audit_config(self, request):
        """
        @summary 审批开关
        

        @param request: DescribeAuditConfigRequest

        @return: DescribeAuditConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_config_with_options(request, runtime)

    def describe_audit_details_with_options(self, request, runtime):
        """
        @summary 审批详情
        

        @param request: DescribeAuditDetailsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAuditDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditDetails',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAuditDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_audit_details(self, request):
        """
        @summary 审批详情
        

        @param request: DescribeAuditDetailsRequest

        @return: DescribeAuditDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_details_with_options(request, runtime)

    def describe_audit_page_list_with_options(self, request, runtime):
        """
        @summary 审核列表展示、查询
        

        @param request: DescribeAuditPageListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAuditPageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.audit_status):
            query['auditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_name):
            query['ruleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditPageList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAuditPageListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_audit_page_list(self, request):
        """
        @summary 审核列表展示、查询
        

        @param request: DescribeAuditPageListRequest

        @return: DescribeAuditPageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_page_list_with_options(request, runtime)

    def describe_auth_event_name_list_with_options(self, request, runtime):
        """
        @summary 查询当前用户的事件名列表
        

        @param request: DescribeAuthEventNameListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAuthEventNameListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuthEventNameList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAuthEventNameListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auth_event_name_list(self, request):
        """
        @summary 查询当前用户的事件名列表
        

        @param request: DescribeAuthEventNameListRequest

        @return: DescribeAuthEventNameListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auth_event_name_list_with_options(request, runtime)

    def describe_auth_rule_page_list_with_options(self, request, runtime):
        """
        @summary 策略列表
        

        @param request: DescribeAuthRulePageListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAuthRulePageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_name):
            query['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuthRulePageList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAuthRulePageListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auth_rule_page_list(self, request):
        """
        @summary 策略列表
        

        @param request: DescribeAuthRulePageListRequest

        @return: DescribeAuthRulePageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auth_rule_page_list_with_options(request, runtime)

    def describe_auth_scene_list_with_options(self, request, runtime):
        """
        @summary 场景列表
        

        @param request: DescribeAuthSceneListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAuthSceneListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuthSceneList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAuthSceneListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auth_scene_list(self, request):
        """
        @summary 场景列表
        

        @param request: DescribeAuthSceneListRequest

        @return: DescribeAuthSceneListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auth_scene_list_with_options(request, runtime)

    def describe_auth_scene_page_list_with_options(self, request, runtime):
        """
        @summary 场景列表
        

        @param request: DescribeAuthScenePageListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAuthScenePageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.scene_name):
            query['sceneName'] = request.scene_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuthScenePageList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAuthScenePageListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auth_scene_page_list(self, request):
        """
        @summary 场景列表
        

        @param request: DescribeAuthScenePageListRequest

        @return: DescribeAuthScenePageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auth_scene_page_list_with_options(request, runtime)

    def describe_auth_status_with_options(self, request, runtime):
        """
        @summary 查看是否授权
        

        @param request: DescribeAuthStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAuthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuthStatus',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAuthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auth_status(self, request):
        """
        @summary 查看是否授权
        

        @param request: DescribeAuthStatusRequest

        @return: DescribeAuthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auth_status_with_options(request, runtime)

    def describe_avg_execute_cost_report_with_options(self, request, runtime):
        """
        @summary 平均执行耗时
        

        @param request: DescribeAvgExecuteCostReportRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAvgExecuteCostReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvgExecuteCostReport',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeAvgExecuteCostReportResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_avg_execute_cost_report(self, request):
        """
        @summary 平均执行耗时
        

        @param request: DescribeAvgExecuteCostReportRequest

        @return: DescribeAvgExecuteCostReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_avg_execute_cost_report_with_options(request, runtime)

    def describe_basic_search_page_list_with_options(self, request, runtime):
        """
        @summary 基础查询
        

        @param request: DescribeBasicSearchPageListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeBasicSearchPageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_begin_time):
            query['eventBeginTime'] = request.event_begin_time
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.event_end_time):
            query['eventEndTime'] = request.event_end_time
        if not UtilClient.is_unset(request.field_name):
            query['fieldName'] = request.field_name
        if not UtilClient.is_unset(request.field_value):
            query['fieldValue'] = request.field_value
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBasicSearchPageList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeBasicSearchPageListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_basic_search_page_list(self, request):
        """
        @summary 基础查询
        

        @param request: DescribeBasicSearchPageListRequest

        @return: DescribeBasicSearchPageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_basic_search_page_list_with_options(request, runtime)

    def describe_basic_start_with_options(self, request, runtime):
        """
        @summary 基础统计
        

        @param request: DescribeBasicStartRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeBasicStartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['appKey'] = request.app_key
        if not UtilClient.is_unset(request.end_ds):
            query['endDs'] = request.end_ds
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.service):
            query['service'] = request.service
        if not UtilClient.is_unset(request.start_ds):
            query['startDs'] = request.start_ds
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBasicStart',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeBasicStartResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_basic_start(self, request):
        """
        @summary 基础统计
        

        @param request: DescribeBasicStartRequest

        @return: DescribeBasicStartResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_basic_start_with_options(request, runtime)

    def describe_by_pass_shunt_event_with_options(self, request, runtime):
        """
        @summary 查看旁路事件
        

        @param request: DescribeByPassShuntEventRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeByPassShuntEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_id):
            query['eventId'] = request.event_id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeByPassShuntEvent',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeByPassShuntEventResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_by_pass_shunt_event(self, request):
        """
        @summary 查看旁路事件
        

        @param request: DescribeByPassShuntEventRequest

        @return: DescribeByPassShuntEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_by_pass_shunt_event_with_options(request, runtime)

    def describe_cust_variable_config_list_with_options(self, request, runtime):
        """
        @summary 查询自定义累计变量的类型配置
        

        @param request: DescribeCustVariableConfigListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCustVariableConfigListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.biz_type):
            query['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.time_type):
            query['timeType'] = request.time_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustVariableConfigList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeCustVariableConfigListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cust_variable_config_list(self, request):
        """
        @summary 查询自定义累计变量的类型配置
        

        @param request: DescribeCustVariableConfigListRequest

        @return: DescribeCustVariableConfigListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cust_variable_config_list_with_options(request, runtime)

    def describe_cust_variable_detail_with_options(self, request, runtime):
        """
        @summary 累计变量详情
        

        @param request: DescribeCustVariableDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCustVariableDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustVariableDetail',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeCustVariableDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cust_variable_detail(self, request):
        """
        @summary 累计变量详情
        

        @param request: DescribeCustVariableDetailRequest

        @return: DescribeCustVariableDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cust_variable_detail_with_options(request, runtime)

    def describe_cust_variable_page_with_options(self, request, runtime):
        """
        @summary 查询自定义累计变量列表
        

        @param request: DescribeCustVariablePageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCustVariablePageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustVariablePage',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeCustVariablePageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cust_variable_page(self, request):
        """
        @summary 查询自定义累计变量列表
        

        @param request: DescribeCustVariablePageRequest

        @return: DescribeCustVariablePageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cust_variable_page_with_options(request, runtime)

    def describe_data_source_data_download_url_with_options(self, request, runtime):
        """
        @summary 获取数据源数据下载链接
        

        @param request: DescribeDataSourceDataDownloadUrlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDataSourceDataDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataSourceDataDownloadUrl',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeDataSourceDataDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_source_data_download_url(self, request):
        """
        @summary 获取数据源数据下载链接
        

        @param request: DescribeDataSourceDataDownloadUrlRequest

        @return: DescribeDataSourceDataDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_source_data_download_url_with_options(request, runtime)

    def describe_data_source_fields_with_options(self, request, runtime):
        """
        @summary 获取数据源所有字段
        

        @param request: DescribeDataSourceFieldsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDataSourceFieldsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.data_source_code):
            query['dataSourceCode'] = request.data_source_code
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataSourceFields',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeDataSourceFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_source_fields(self, request):
        """
        @summary 获取数据源所有字段
        

        @param request: DescribeDataSourceFieldsRequest

        @return: DescribeDataSourceFieldsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_source_fields_with_options(request, runtime)

    def describe_data_source_page_list_with_options(self, request, runtime):
        """
        @summary 数据源列表接口
        

        @param request: DescribeDataSourcePageListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDataSourcePageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataSourcePageList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeDataSourcePageListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_source_page_list(self, request):
        """
        @summary 数据源列表接口
        

        @param request: DescribeDataSourcePageListRequest

        @return: DescribeDataSourcePageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_source_page_list_with_options(request, runtime)

    def describe_decision_result_fluctuation_with_options(self, request, runtime):
        """
        @summary 决策结果波动检测
        

        @param request: DescribeDecisionResultFluctuationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDecisionResultFluctuationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDecisionResultFluctuation',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeDecisionResultFluctuationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_decision_result_fluctuation(self, request):
        """
        @summary 决策结果波动检测
        

        @param request: DescribeDecisionResultFluctuationRequest

        @return: DescribeDecisionResultFluctuationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_decision_result_fluctuation_with_options(request, runtime)

    def describe_decision_result_trend_with_options(self, request, runtime):
        """
        @summary 决策结果波动趋势
        

        @param request: DescribeDecisionResultTrendRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDecisionResultTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDecisionResultTrend',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeDecisionResultTrendResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_decision_result_trend(self, request):
        """
        @summary 决策结果波动趋势
        

        @param request: DescribeDecisionResultTrendRequest

        @return: DescribeDecisionResultTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_decision_result_trend_with_options(request, runtime)

    def describe_detail_start_with_options(self, request, runtime):
        """
        @summary 详细统计
        

        @param request: DescribeDetailStartRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDetailStartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['appKey'] = request.app_key
        if not UtilClient.is_unset(request.end_ds):
            query['endDs'] = request.end_ds
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.service):
            query['service'] = request.service
        if not UtilClient.is_unset(request.start_ds):
            query['startDs'] = request.start_ds
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDetailStart',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeDetailStartResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_detail_start(self, request):
        """
        @summary 详细统计
        

        @param request: DescribeDetailStartRequest

        @return: DescribeDetailStartResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_detail_start_with_options(request, runtime)

    def describe_download_url_with_options(self, request, runtime):
        """
        @summary 下载
        

        @param request: DescribeDownloadUrlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_type):
            query['FileType'] = request.file_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['RegId'] = request.reg_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadUrl',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_download_url(self, request):
        """
        @summary 下载
        

        @param request: DescribeDownloadUrlRequest

        @return: DescribeDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_download_url_with_options(request, runtime)

    def describe_event_base_info_by_event_code_with_options(self, request, runtime):
        """
        @summary 查询事件详情
        

        @param request: DescribeEventBaseInfoByEventCodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventBaseInfoByEventCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventBaseInfoByEventCode',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeEventBaseInfoByEventCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_base_info_by_event_code(self, request):
        """
        @summary 查询事件详情
        

        @param request: DescribeEventBaseInfoByEventCodeRequest

        @return: DescribeEventBaseInfoByEventCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_base_info_by_event_code_with_options(request, runtime)

    def describe_event_count_with_options(self, request, runtime):
        """
        @summary 查询事件总数量
        

        @param request: DescribeEventCountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventCount',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeEventCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_count(self, request):
        """
        @summary 查询事件总数量
        

        @param request: DescribeEventCountRequest

        @return: DescribeEventCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_count_with_options(request, runtime)

    def describe_event_detail_by_request_id_with_options(self, request, runtime):
        """
        @summary 根据requestId查询事件详情
        

        @param request: DescribeEventDetailByRequestIdRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventDetailByRequestIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.event_time):
            query['eventTime'] = request.event_time
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.s_request_id):
            query['sRequestId'] = request.s_request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventDetailByRequestId',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeEventDetailByRequestIdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_detail_by_request_id(self, request):
        """
        @summary 根据requestId查询事件详情
        

        @param request: DescribeEventDetailByRequestIdRequest

        @return: DescribeEventDetailByRequestIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_detail_by_request_id_with_options(request, runtime)

    def describe_event_log_detail_with_options(self, request, runtime):
        """
        @summary 查询事件历史详情
        

        @param request: DescribeEventLogDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventLogDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.req_id_by_log):
            query['reqIdByLog'] = request.req_id_by_log
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventLogDetail',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeEventLogDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_log_detail(self, request):
        """
        @summary 查询事件历史详情
        

        @param request: DescribeEventLogDetailRequest

        @return: DescribeEventLogDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_log_detail_with_options(request, runtime)

    def describe_event_log_page_with_options(self, request, runtime):
        """
        @summary 查询事件历史列表
        

        @param request: DescribeEventLogPageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventLogPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.account_id_prp):
            query['accountIdPRP'] = request.account_id_prp
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.condition_1al):
            query['condition1AL'] = request.condition_1al
        if not UtilClient.is_unset(request.condition_2al):
            query['condition2AL'] = request.condition_2al
        if not UtilClient.is_unset(request.condition_3al):
            query['condition3AL'] = request.condition_3al
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_type_lrp):
            query['deviceTypeLRP'] = request.device_type_lrp
        if not UtilClient.is_unset(request.email_prp):
            query['emailPRP'] = request.email_prp
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.fail_reason_lrp):
            query['failReasonLRP'] = request.fail_reason_lrp
        if not UtilClient.is_unset(request.ip_prp):
            query['ipPRP'] = request.ip_prp
        if not UtilClient.is_unset(request.login_result_arp):
            query['loginResultARP'] = request.login_result_arp
        if not UtilClient.is_unset(request.login_type_lrp):
            query['loginTypeLRP'] = request.login_type_lrp
        if not UtilClient.is_unset(request.mac_prp):
            query['macPRP'] = request.mac_prp
        if not UtilClient.is_unset(request.mobile_prp):
            query['mobilePRP'] = request.mobile_prp
        if not UtilClient.is_unset(request.nick_name_prp):
            query['nickNamePRP'] = request.nick_name_prp
        if not UtilClient.is_unset(request.operate_source_lrp):
            query['operateSourceLRP'] = request.operate_source_lrp
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.refer_prp):
            query['referPRP'] = request.refer_prp
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.register_ip_prp):
            query['registerIpPRP'] = request.register_ip_prp
        if not UtilClient.is_unset(request.req_id_pbs):
            query['reqIdPBS'] = request.req_id_pbs
        if not UtilClient.is_unset(request.score_ebs):
            query['scoreEBS'] = request.score_ebs
        if not UtilClient.is_unset(request.score_sbs):
            query['scoreSBS'] = request.score_sbs
        if not UtilClient.is_unset(request.service_abs):
            query['serviceABS'] = request.service_abs
        if not UtilClient.is_unset(request.tags_lbs):
            query['tagsLBS'] = request.tags_lbs
        if not UtilClient.is_unset(request.umid_pdi):
            query['umidPDI'] = request.umid_pdi
        if not UtilClient.is_unset(request.user_agent_prp):
            query['userAgentPRP'] = request.user_agent_prp
        if not UtilClient.is_unset(request.user_name_type_lrp):
            query['userNameTypeLRP'] = request.user_name_type_lrp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventLogPage',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeEventLogPageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_log_page(self, request):
        """
        @summary 查询事件历史列表
        

        @param request: DescribeEventLogPageRequest

        @return: DescribeEventLogPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_log_page_with_options(request, runtime)

    def describe_event_page_list_with_options(self, request, runtime):
        """
        @summary 事件分页查询
        

        @param request: DescribeEventPageListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventPageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.event_name):
            query['eventName'] = request.event_name
        if not UtilClient.is_unset(request.event_status):
            query['eventStatus'] = request.event_status
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventPageList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeEventPageListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_page_list(self, request):
        """
        @summary 事件分页查询
        

        @param request: DescribeEventPageListRequest

        @return: DescribeEventPageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_page_list_with_options(request, runtime)

    def describe_event_result_bar_chart_with_options(self, request, runtime):
        """
        @summary 风险大盘
        

        @param request: DescribeEventResultBarChartRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventResultBarChartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventResultBarChart',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeEventResultBarChartResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_result_bar_chart(self, request):
        """
        @summary 风险大盘
        

        @param request: DescribeEventResultBarChartRequest

        @return: DescribeEventResultBarChartResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_result_bar_chart_with_options(request, runtime)

    def describe_event_result_list_with_options(self, request, runtime):
        """
        @summary 事件概览列表
        

        @param request: DescribeEventResultListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventResultListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventResultList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeEventResultListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_result_list(self, request):
        """
        @summary 事件概览列表
        

        @param request: DescribeEventResultListRequest

        @return: DescribeEventResultListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_result_list_with_options(request, runtime)

    def describe_event_task_history_with_options(self, request, runtime):
        """
        @summary 查询策略下载列表
        

        @param request: DescribeEventTaskHistoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventTaskHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventTaskHistory',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeEventTaskHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_task_history(self, request):
        """
        @summary 查询策略下载列表
        

        @param request: DescribeEventTaskHistoryRequest

        @return: DescribeEventTaskHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_task_history_with_options(request, runtime)

    def describe_event_total_count_report_with_options(self, request, runtime):
        """
        @summary 调用事件次数
        

        @param request: DescribeEventTotalCountReportRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventTotalCountReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventTotalCountReport',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeEventTotalCountReportResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_total_count_report(self, request):
        """
        @summary 调用事件次数
        

        @param request: DescribeEventTotalCountReportRequest

        @return: DescribeEventTotalCountReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_total_count_report_with_options(request, runtime)

    def describe_event_upload_policy_with_options(self, request, runtime):
        """
        @summary 批量导入策略
        

        @param request: DescribeEventUploadPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventUploadPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventUploadPolicy',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeEventUploadPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_upload_policy(self, request):
        """
        @summary 批量导入策略
        

        @param request: DescribeEventUploadPolicyRequest

        @return: DescribeEventUploadPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_upload_policy_with_options(request, runtime)

    def describe_event_variable_list_with_options(self, request, runtime):
        """
        @summary 查询事件变量
        

        @param request: DescribeEventVariableListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventVariableListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.filter_dto):
            query['filterDTO'] = request.filter_dto
        if not UtilClient.is_unset(request.ref_obj_id):
            query['refObjId'] = request.ref_obj_id
        if not UtilClient.is_unset(request.ref_obj_type):
            query['refObjType'] = request.ref_obj_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventVariableList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeEventVariableListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_variable_list(self, request):
        """
        @summary 查询事件变量
        

        @param request: DescribeEventVariableListRequest

        @return: DescribeEventVariableListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_variable_list_with_options(request, runtime)

    def describe_event_variable_template_bind_with_options(self, request, runtime):
        """
        @summary 查询事件模版
        

        @param request: DescribeEventVariableTemplateBindRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventVariableTemplateBindResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.inputs):
            query['inputs'] = request.inputs
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.template_code):
            query['templateCode'] = request.template_code
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventVariableTemplateBind',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeEventVariableTemplateBindResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_variable_template_bind(self, request):
        """
        @summary 查询事件模版
        

        @param request: DescribeEventVariableTemplateBindRequest

        @return: DescribeEventVariableTemplateBindResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_variable_template_bind_with_options(request, runtime)

    def describe_event_variable_template_list_with_options(self, request, runtime):
        """
        @summary 查询事件模版
        

        @param request: DescribeEventVariableTemplateListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventVariableTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.inputs):
            query['inputs'] = request.inputs
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.template_code):
            query['templateCode'] = request.template_code
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventVariableTemplateList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeEventVariableTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_variable_template_list(self, request):
        """
        @summary 查询事件模版
        

        @param request: DescribeEventVariableTemplateListRequest

        @return: DescribeEventVariableTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_event_variable_template_list_with_options(request, runtime)

    def describe_events_variable_list_with_options(self, request, runtime):
        """
        @summary 查询事件变量
        

        @param request: DescribeEventsVariableListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeEventsVariableListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.filter_dto):
            query['filterDTO'] = request.filter_dto
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.scene):
            query['scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventsVariableList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeEventsVariableListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_events_variable_list(self, request):
        """
        @summary 查询事件变量
        

        @param request: DescribeEventsVariableListRequest

        @return: DescribeEventsVariableListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_events_variable_list_with_options(request, runtime)

    def describe_excute_num_with_options(self, request, runtime):
        """

        @param request: DescribeExcuteNumRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeExcuteNumResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.degree):
            query['Degree'] = request.degree
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExcuteNum',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeExcuteNumResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_excute_num(self, request):
        """

        @param request: DescribeExcuteNumRequest

        @return: DescribeExcuteNumResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_excute_num_with_options(request, runtime)

    def describe_exist_name_with_options(self, request, runtime):
        """
        @summary 校验字段名是否重复(基于用户单位)
        

        @param request: DescribeExistNameRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeExistNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExistName',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeExistNameResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_exist_name(self, request):
        """
        @summary 校验字段名是否重复(基于用户单位)
        

        @param request: DescribeExistNameRequest

        @return: DescribeExistNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_exist_name_with_options(request, runtime)

    def describe_exist_scene_with_options(self, request, runtime):
        """
        @summary 场景是否存在
        

        @param request: DescribeExistSceneRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeExistSceneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExistScene',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeExistSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_exist_scene(self, request):
        """
        @summary 场景是否存在
        

        @param request: DescribeExistSceneRequest

        @return: DescribeExistSceneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_exist_scene_with_options(request, runtime)

    def describe_expression_variable_detail_with_options(self, request, runtime):
        """
        @summary 自定义变量详情
        

        @param request: DescribeExpressionVariableDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeExpressionVariableDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExpressionVariableDetail',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeExpressionVariableDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_expression_variable_detail(self, request):
        """
        @summary 自定义变量详情
        

        @param request: DescribeExpressionVariableDetailRequest

        @return: DescribeExpressionVariableDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_expression_variable_detail_with_options(request, runtime)

    def describe_expression_variable_function_list_with_options(self, request, runtime):
        """
        @summary 函数列表
        

        @param request: DescribeExpressionVariableFunctionListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeExpressionVariableFunctionListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExpressionVariableFunctionList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeExpressionVariableFunctionListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_expression_variable_function_list(self, request):
        """
        @summary 函数列表
        

        @param request: DescribeExpressionVariableFunctionListRequest

        @return: DescribeExpressionVariableFunctionListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_expression_variable_function_list_with_options(request, runtime)

    def describe_expression_variable_page_with_options(self, request, runtime):
        """
        @summary 自定义变量分页查询
        

        @param request: DescribeExpressionVariablePageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeExpressionVariablePageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.outputs):
            query['outputs'] = request.outputs
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.value):
            query['value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExpressionVariablePage',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeExpressionVariablePageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_expression_variable_page(self, request):
        """
        @summary 自定义变量分页查询
        

        @param request: DescribeExpressionVariablePageRequest

        @return: DescribeExpressionVariablePageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_expression_variable_page_with_options(request, runtime)

    def describe_field_by_id_with_options(self, request, runtime):
        """
        @summary 获取字段详情
        

        @param request: DescribeFieldByIdRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeFieldByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFieldById',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeFieldByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_field_by_id(self, request):
        """
        @summary 获取字段详情
        

        @param request: DescribeFieldByIdRequest

        @return: DescribeFieldByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_field_by_id_with_options(request, runtime)

    def describe_field_list_with_options(self, request, runtime):
        """
        @summary 查询字段列表
        

        @param request: DescribeFieldListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeFieldListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.condition):
            query['condition'] = request.condition
        if not UtilClient.is_unset(request.inputs):
            query['inputs'] = request.inputs
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFieldList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeFieldListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_field_list(self, request):
        """
        @summary 查询字段列表
        

        @param request: DescribeFieldListRequest

        @return: DescribeFieldListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_field_list_with_options(request, runtime)

    def describe_field_page_with_options(self, request, runtime):
        """
        @summary 查询字段分页列表
        

        @param request: DescribeFieldPageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeFieldPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.classify):
            query['classify'] = request.classify
        if not UtilClient.is_unset(request.condition):
            query['condition'] = request.condition
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFieldPage',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeFieldPageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_field_page(self, request):
        """
        @summary 查询字段分页列表
        

        @param request: DescribeFieldPageRequest

        @return: DescribeFieldPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_field_page_with_options(request, runtime)

    def describe_group_account_page_with_options(self, request, runtime):
        """
        @summary 社群账户列表
        

        @param request: DescribeGroupAccountPageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeGroupAccountPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.community_no):
            query['communityNo'] = request.community_no
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.direction):
            query['direction'] = request.direction
        if not UtilClient.is_unset(request.field_key):
            query['fieldKey'] = request.field_key
        if not UtilClient.is_unset(request.field_val):
            query['fieldVal'] = request.field_val
        if not UtilClient.is_unset(request.is_page):
            query['isPage'] = request.is_page
        if not UtilClient.is_unset(request.order):
            query['order'] = request.order
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupAccountPage',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeGroupAccountPageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_group_account_page(self, request):
        """
        @summary 社群账户列表
        

        @param request: DescribeGroupAccountPageRequest

        @return: DescribeGroupAccountPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_group_account_page_with_options(request, runtime)

    def describe_group_condition_list_with_options(self, request, runtime):
        """
        @summary 社群列表查询条件
        

        @param request: DescribeGroupConditionListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeGroupConditionListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupConditionList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeGroupConditionListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_group_condition_list(self, request):
        """
        @summary 社群列表查询条件
        

        @param request: DescribeGroupConditionListRequest

        @return: DescribeGroupConditionListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_group_condition_list_with_options(request, runtime)

    def describe_group_page_with_options(self, request, runtime):
        """
        @summary 社群列表
        

        @param request: DescribeGroupPageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeGroupPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.direction):
            query['direction'] = request.direction
        if not UtilClient.is_unset(request.order):
            query['order'] = request.order
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        if not UtilClient.is_unset(request.time_type):
            query['timeType'] = request.time_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupPage',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeGroupPageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_group_page(self, request):
        """
        @summary 社群列表
        

        @param request: DescribeGroupPageRequest

        @return: DescribeGroupPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_group_page_with_options(request, runtime)

    def describe_group_statistics_by_today_with_options(self, request, runtime):
        """
        @summary 当日发现的风险社群
        

        @param request: DescribeGroupStatisticsByTodayRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeGroupStatisticsByTodayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupStatisticsByToday',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeGroupStatisticsByTodayResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_group_statistics_by_today(self, request):
        """
        @summary 当日发现的风险社群
        

        @param request: DescribeGroupStatisticsByTodayRequest

        @return: DescribeGroupStatisticsByTodayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_group_statistics_by_today_with_options(request, runtime)

    def describe_group_trend_with_options(self, request, runtime):
        """
        @summary 风险社群的近期趋势
        

        @param request: DescribeGroupTrendRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeGroupTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.day):
            query['day'] = request.day
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupTrend',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeGroupTrendResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_group_trend(self, request):
        """
        @summary 风险社群的近期趋势
        

        @param request: DescribeGroupTrendRequest

        @return: DescribeGroupTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_group_trend_with_options(request, runtime)

    def describe_has_rule_name_by_event_code_with_options(self, request, runtime):
        """
        @summary 查询事件名下的策略名是否存在
        

        @param request: DescribeHasRuleNameByEventCodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHasRuleNameByEventCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.exclude_rule_id):
            query['excludeRuleId'] = request.exclude_rule_id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_name):
            query['ruleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHasRuleNameByEventCode',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeHasRuleNameByEventCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_has_rule_name_by_event_code(self, request):
        """
        @summary 查询事件名下的策略名是否存在
        

        @param request: DescribeHasRuleNameByEventCodeRequest

        @return: DescribeHasRuleNameByEventCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_has_rule_name_by_event_code_with_options(request, runtime)

    def describe_high_risk_pie_chart_with_options(self, request, runtime):
        """
        @summary 风险地图概览图表(饼图)
        

        @param request: DescribeHighRiskPieChartRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHighRiskPieChartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHighRiskPieChart',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeHighRiskPieChartResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_high_risk_pie_chart(self, request):
        """
        @summary 风险地图概览图表(饼图)
        

        @param request: DescribeHighRiskPieChartRequest

        @return: DescribeHighRiskPieChartResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_high_risk_pie_chart_with_options(request, runtime)

    def describe_hit_rule_fluctuation_with_options(self, request, runtime):
        """
        @summary 策略命中波动检测
        

        @param request: DescribeHitRuleFluctuationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHitRuleFluctuationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_status):
            query['ruleStatus'] = request.rule_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHitRuleFluctuation',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeHitRuleFluctuationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hit_rule_fluctuation(self, request):
        """
        @summary 策略命中波动检测
        

        @param request: DescribeHitRuleFluctuationRequest

        @return: DescribeHitRuleFluctuationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hit_rule_fluctuation_with_options(request, runtime)

    def describe_hit_rule_list_with_options(self, request, runtime):
        """
        @summary 主事件/旁路/分流策略命中TOP20
        

        @param request: DescribeHitRuleListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHitRuleListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.event_type):
            query['eventType'] = request.event_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHitRuleList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeHitRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hit_rule_list(self, request):
        """
        @summary 主事件/旁路/分流策略命中TOP20
        

        @param request: DescribeHitRuleListRequest

        @return: DescribeHitRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hit_rule_list_with_options(request, runtime)

    def describe_hit_rule_trend_with_options(self, request, runtime):
        """
        @summary 策略命中趋势
        

        @param request: DescribeHitRuleTrendRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeHitRuleTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_status):
            query['ruleStatus'] = request.rule_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHitRuleTrend',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeHitRuleTrendResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hit_rule_trend(self, request):
        """
        @summary 策略命中趋势
        

        @param request: DescribeHitRuleTrendRequest

        @return: DescribeHitRuleTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hit_rule_trend_with_options(request, runtime)

    def describe_input_feild_count_by_event_code_with_options(self, request, runtime):
        """
        @summary 查询事件总数量
        

        @param request: DescribeInputFeildCountByEventCodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeInputFeildCountByEventCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInputFeildCountByEventCode',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeInputFeildCountByEventCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_input_feild_count_by_event_code(self, request):
        """
        @summary 查询事件总数量
        

        @param request: DescribeInputFeildCountByEventCodeRequest

        @return: DescribeInputFeildCountByEventCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_input_feild_count_by_event_code_with_options(request, runtime)

    def describe_list_poc_with_options(self, request, runtime):
        """
        @summary 任务列表
        

        @param request: DescribeListPocRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeListPocResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['RegId'] = request.reg_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeListPoc',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeListPocResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_list_poc(self, request):
        """
        @summary 任务列表
        

        @param request: DescribeListPocRequest

        @return: DescribeListPocResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_list_poc_with_options(request, runtime)

    def describe_loan_exec_list_with_options(self, request, runtime):
        """
        @summary 获取监控对象列表
        

        @param request: DescribeLoanExecListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeLoanExecListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.batch_no):
            query['batchNo'] = request.batch_no
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.monitor_obj):
            query['monitorObj'] = request.monitor_obj
        if not UtilClient.is_unset(request.monitor_status):
            query['monitorStatus'] = request.monitor_status
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoanExecList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeLoanExecListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_loan_exec_list(self, request):
        """
        @summary 获取监控对象列表
        

        @param request: DescribeLoanExecListRequest

        @return: DescribeLoanExecListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_loan_exec_list_with_options(request, runtime)

    def describe_loan_task_list_with_options(self, request, runtime):
        """
        @summary 获取贷中监控任务列表
        

        @param request: DescribeLoanTaskListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeLoanTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.batch_no):
            query['batchNo'] = request.batch_no
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.monitor_status):
            query['monitorStatus'] = request.monitor_status
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoanTaskList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeLoanTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_loan_task_list(self, request):
        """
        @summary 获取贷中监控任务列表
        

        @param request: DescribeLoanTaskListRequest

        @return: DescribeLoanTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_loan_task_list_with_options(request, runtime)

    def describe_mark_page_with_options(self, request, runtime):
        """
        @summary 打标列表
        

        @param request: DescribeMarkPageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMarkPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.direction):
            query['direction'] = request.direction
        if not UtilClient.is_unset(request.is_page):
            query['isPage'] = request.is_page
        if not UtilClient.is_unset(request.order):
            query['order'] = request.order
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.task_log_id):
            query['taskLogId'] = request.task_log_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMarkPage',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeMarkPageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_mark_page(self, request):
        """
        @summary 打标列表
        

        @param request: DescribeMarkPageRequest

        @return: DescribeMarkPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_mark_page_with_options(request, runtime)

    def describe_menu_permission_with_options(self, request, runtime):
        """
        @summary 查询是否有权限
        

        @param request: DescribeMenuPermissionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMenuPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.permission_type):
            query['permissionType'] = request.permission_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMenuPermission',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeMenuPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_menu_permission(self, request):
        """
        @summary 查询是否有权限
        

        @param request: DescribeMenuPermissionRequest

        @return: DescribeMenuPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_menu_permission_with_options(request, runtime)

    def describe_monitor_task_limit_with_options(self, request, runtime):
        """
        @summary 查询任务的限制
        

        @param request: DescribeMonitorTaskLimitRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeMonitorTaskLimitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorTaskLimit',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeMonitorTaskLimitResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_monitor_task_limit(self, request):
        """
        @summary 查询任务的限制
        

        @param request: DescribeMonitorTaskLimitRequest

        @return: DescribeMonitorTaskLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_task_limit_with_options(request, runtime)

    def describe_name_list_with_options(self, request, runtime):
        """
        @summary 查询名单分页
        

        @param request: DescribeNameListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeNameListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.value):
            query['value'] = request.value
        if not UtilClient.is_unset(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNameList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeNameListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_name_list(self, request):
        """
        @summary 查询名单分页
        

        @param request: DescribeNameListRequest

        @return: DescribeNameListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_name_list_with_options(request, runtime)

    def describe_name_list_download_url_with_options(self, request, runtime):
        """
        @summary 下载名单列表
        

        @param request: DescribeNameListDownloadUrlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeNameListDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNameListDownloadUrl',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeNameListDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_name_list_download_url(self, request):
        """
        @summary 下载名单列表
        

        @param request: DescribeNameListDownloadUrlRequest

        @return: DescribeNameListDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_name_list_download_url_with_options(request, runtime)

    def describe_name_list_limit_with_options(self, request, runtime):
        """
        @summary 查询名单限制数
        

        @param request: DescribeNameListLimitRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeNameListLimitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNameListLimit',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeNameListLimitResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_name_list_limit(self, request):
        """
        @summary 查询名单限制数
        

        @param request: DescribeNameListLimitRequest

        @return: DescribeNameListLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_name_list_limit_with_options(request, runtime)

    def describe_name_list_page_list_with_options(self, request, runtime):
        """
        @summary 名单内容查询
        

        @param request: DescribeNameListPageListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeNameListPageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.update_begin_time):
            query['updateBeginTime'] = request.update_begin_time
        if not UtilClient.is_unset(request.update_end_time):
            query['updateEndTime'] = request.update_end_time
        if not UtilClient.is_unset(request.value):
            query['value'] = request.value
        if not UtilClient.is_unset(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNameListPageList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeNameListPageListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_name_list_page_list(self, request):
        """
        @summary 名单内容查询
        

        @param request: DescribeNameListPageListRequest

        @return: DescribeNameListPageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_name_list_page_list_with_options(request, runtime)

    def describe_name_list_type_list_with_options(self, request, runtime):
        """
        @summary 名单类型列表
        

        @param request: DescribeNameListTypeListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeNameListTypeListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNameListTypeList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeNameListTypeListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_name_list_type_list(self, request):
        """
        @summary 名单类型列表
        

        @param request: DescribeNameListTypeListRequest

        @return: DescribeNameListTypeListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_name_list_type_list_with_options(request, runtime)

    def describe_name_list_variable_page_list_with_options(self, request, runtime):
        """
        @summary 名单列表
        

        @param request: DescribeNameListVariablePageListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeNameListVariablePageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.name_list_type):
            query['nameListType'] = request.name_list_type
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.value):
            query['value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNameListVariablePageList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeNameListVariablePageListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_name_list_variable_page_list(self, request):
        """
        @summary 名单列表
        

        @param request: DescribeNameListVariablePageListRequest

        @return: DescribeNameListVariablePageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_name_list_variable_page_list_with_options(request, runtime)

    def describe_operation_log_page_list_with_options(self, request, runtime):
        """
        @summary 根据事件名称查询事件列表
        

        @param request: DescribeOperationLogPageListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeOperationLogPageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.start_date):
            query['startDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOperationLogPageList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeOperationLogPageListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_operation_log_page_list(self, request):
        """
        @summary 根据事件名称查询事件列表
        

        @param request: DescribeOperationLogPageListRequest

        @return: DescribeOperationLogPageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_operation_log_page_list_with_options(request, runtime)

    def describe_operator_list_with_options(self, request, runtime):
        """
        @summary 根据客户ID查询操作符映射列表
        

        @param request: DescribeOperatorListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeOperatorListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOperatorList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeOperatorListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_operator_list(self, request):
        """
        @summary 根据客户ID查询操作符映射列表
        

        @param request: DescribeOperatorListRequest

        @return: DescribeOperatorListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_operator_list_with_options(request, runtime)

    def describe_operator_list_by_scene_with_options(self, request, runtime):
        """
        @summary 查询操作符映射列表
        

        @param request: DescribeOperatorListBySceneRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeOperatorListBySceneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.scene):
            query['scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOperatorListByScene',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeOperatorListBySceneResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_operator_list_by_scene(self, request):
        """
        @summary 查询操作符映射列表
        

        @param request: DescribeOperatorListBySceneRequest

        @return: DescribeOperatorListBySceneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_operator_list_by_scene_with_options(request, runtime)

    def describe_operator_list_by_type_with_options(self, request, runtime):
        """
        @summary 查询操作符映射列表
        

        @param request: DescribeOperatorListByTypeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeOperatorListByTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOperatorListByType',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeOperatorListByTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_operator_list_by_type(self, request):
        """
        @summary 查询操作符映射列表
        

        @param request: DescribeOperatorListByTypeRequest

        @return: DescribeOperatorListByTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_operator_list_by_type_with_options(request, runtime)

    def describe_oss_auth_status_with_options(self, request, runtime):
        """
        @summary 查看是否授权Oss
        

        @param request: DescribeOssAuthStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeOssAuthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssAuthStatus',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeOssAuthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_oss_auth_status(self, request):
        """
        @summary 查看是否授权Oss
        

        @param request: DescribeOssAuthStatusRequest

        @return: DescribeOssAuthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_auth_status_with_options(request, runtime)

    def describe_oss_policy_with_options(self, request, runtime):
        """
        @summary 获取OSS Policy
        

        @param request: DescribeOssPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeOssPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.scene):
            query['scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssPolicy',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeOssPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_oss_policy(self, request):
        """
        @summary 获取OSS Policy
        

        @param request: DescribeOssPolicyRequest

        @return: DescribeOssPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_policy_with_options(request, runtime)

    def describe_oss_token_with_options(self, request, runtime):
        """
        @summary 获取文件上传凭证
        

        @param request: DescribeOssTokenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeOssTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.upload_type):
            query['uploadType'] = request.upload_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOssToken',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeOssTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_oss_token(self, request):
        """
        @summary 获取文件上传凭证
        

        @param request: DescribeOssTokenRequest

        @return: DescribeOssTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_token_with_options(request, runtime)

    def describe_param_by_event_codes_with_options(self, request, runtime):
        """
        @summary 查询事件属性列表
        

        @param request: DescribeParamByEventCodesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeParamByEventCodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.parma):
            query['parma'] = request.parma
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParamByEventCodes',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeParamByEventCodesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_param_by_event_codes(self, request):
        """
        @summary 查询事件属性列表
        

        @param request: DescribeParamByEventCodesRequest

        @return: DescribeParamByEventCodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_param_by_event_codes_with_options(request, runtime)

    def describe_param_list_with_options(self, request, runtime):
        """
        @summary 获取映射关系
        

        @param request: DescribeParamListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeParamListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.file_url):
            query['fileUrl'] = request.file_url
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.service_code):
            query['serviceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParamList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeParamListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_param_list(self, request):
        """
        @summary 获取映射关系
        

        @param request: DescribeParamListRequest

        @return: DescribeParamListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_param_list_with_options(request, runtime)

    def describe_poc_detail_with_options(self, request, runtime):
        """
        @summary 获取任务详情
        

        @param request: DescribePocDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribePocDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePocDetail',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribePocDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_poc_detail(self, request):
        """
        @summary 获取任务详情
        

        @param request: DescribePocDetailRequest

        @return: DescribePocDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_poc_detail_with_options(request, runtime)

    def describe_poc_oss_token_with_options(self, request, runtime):
        """
        @summary 获取文件上传凭证
        

        @param request: DescribePocOssTokenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribePocOssTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePocOssToken',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribePocOssTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_poc_oss_token(self, request):
        """
        @summary 获取文件上传凭证
        

        @param request: DescribePocOssTokenRequest

        @return: DescribePocOssTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_poc_oss_token_with_options(request, runtime)

    def describe_poc_task_list_with_options(self, request, runtime):
        """
        @summary 获取poc任务列表
        

        @param request: DescribePocTaskListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribePocTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePocTaskList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribePocTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_poc_task_list(self, request):
        """
        @summary 获取poc任务列表
        

        @param request: DescribePocTaskListRequest

        @return: DescribePocTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_poc_task_list_with_options(request, runtime)

    def describe_private_stack_with_options(self, request, runtime):
        """
        @summary 判断是否开通Stack私域模式
        

        @param request: DescribePrivateStackRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribePrivateStackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrivateStack',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribePrivateStackResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_private_stack(self, request):
        """
        @summary 判断是否开通Stack私域模式
        

        @param request: DescribePrivateStackRequest

        @return: DescribePrivateStackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_private_stack_with_options(request, runtime)

    def describe_query_variable_detail_with_options(self, request, runtime):
        """
        @summary 查询变量详情查询
        

        @param request: DescribeQueryVariableDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeQueryVariableDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQueryVariableDetail',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeQueryVariableDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_query_variable_detail(self, request):
        """
        @summary 查询变量详情查询
        

        @param request: DescribeQueryVariableDetailRequest

        @return: DescribeQueryVariableDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_query_variable_detail_with_options(request, runtime)

    def describe_query_variable_page_list_with_options(self, request, runtime):
        """
        @summary 查询变量列表查询
        

        @param request: DescribeQueryVariablePageListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeQueryVariablePageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.data_source_code):
            query['dataSourceCode'] = request.data_source_code
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQueryVariablePageList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeQueryVariablePageListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_query_variable_page_list(self, request):
        """
        @summary 查询变量列表查询
        

        @param request: DescribeQueryVariablePageListRequest

        @return: DescribeQueryVariablePageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_query_variable_page_list_with_options(request, runtime)

    def describe_recommend_scene_variables_with_options(self, request, runtime):
        """
        @summary 查询样本&场景下的变量列表
        

        @param request: DescribeRecommendSceneVariablesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRecommendSceneVariablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.sample_id):
            query['sampleId'] = request.sample_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecommendSceneVariables',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeRecommendSceneVariablesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_recommend_scene_variables(self, request):
        """
        @summary 查询样本&场景下的变量列表
        

        @param request: DescribeRecommendSceneVariablesRequest

        @return: DescribeRecommendSceneVariablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_recommend_scene_variables_with_options(request, runtime)

    def describe_recommend_task_detail_with_options(self, request, runtime):
        """
        @summary 变量推荐详情查询接口
        

        @param request: DescribeRecommendTaskDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRecommendTaskDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecommendTaskDetail',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeRecommendTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_recommend_task_detail(self, request):
        """
        @summary 变量推荐详情查询接口
        

        @param request: DescribeRecommendTaskDetailRequest

        @return: DescribeRecommendTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_recommend_task_detail_with_options(request, runtime)

    def describe_recommend_task_page_list_with_options(self, request, runtime):
        """
        @summary 变量推荐列表查询接口
        

        @param request: DescribeRecommendTaskPageListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRecommendTaskPageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.task_name):
            query['taskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecommendTaskPageList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeRecommendTaskPageListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_recommend_task_page_list(self, request):
        """
        @summary 变量推荐列表查询接口
        

        @param request: DescribeRecommendTaskPageListRequest

        @return: DescribeRecommendTaskPageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_recommend_task_page_list_with_options(request, runtime)

    def describe_recommend_variables_velocity_with_options(self, request, runtime):
        """
        @summary 查询变量下的指标信息
        

        @param request: DescribeRecommendVariablesVelocityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRecommendVariablesVelocityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        if not UtilClient.is_unset(request.variable_ids_str):
            query['variableIdsStr'] = request.variable_ids_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecommendVariablesVelocity',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeRecommendVariablesVelocityResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_recommend_variables_velocity(self, request):
        """
        @summary 查询变量下的指标信息
        

        @param request: DescribeRecommendVariablesVelocityRequest

        @return: DescribeRecommendVariablesVelocityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_recommend_variables_velocity_with_options(request, runtime)

    def describe_recommend_velocities_with_options(self, request, runtime):
        """
        @summary 查询支持的指标列表
        

        @param request: DescribeRecommendVelocitiesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRecommendVelocitiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.code):
            query['code'] = request.code
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecommendVelocities',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeRecommendVelocitiesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_recommend_velocities(self, request):
        """
        @summary 查询支持的指标列表
        

        @param request: DescribeRecommendVelocitiesRequest

        @return: DescribeRecommendVelocitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_recommend_velocities_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        """
        @summary 查询ApiGateway支持的region列表
        

        @param request: DescribeRegionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        """
        @summary 查询ApiGateway支持的region列表
        

        @param request: DescribeRegionsRequest

        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_request_hit_with_options(self, request, runtime):
        """
        @summary 查询请求命中详情
        

        @param request: DescribeRequestHitRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRequestHitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.s_request_id):
            query['sRequestId'] = request.s_request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRequestHit',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeRequestHitResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_request_hit(self, request):
        """
        @summary 查询请求命中详情
        

        @param request: DescribeRequestHitRequest

        @return: DescribeRequestHitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_request_hit_with_options(request, runtime)

    def describe_request_peak_report_with_options(self, request, runtime):
        """
        @summary 请求峰值
        

        @param request: DescribeRequestPeakReportRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRequestPeakReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRequestPeakReport',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeRequestPeakReportResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_request_peak_report(self, request):
        """
        @summary 请求峰值
        

        @param request: DescribeRequestPeakReportRequest

        @return: DescribeRequestPeakReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_request_peak_report_with_options(request, runtime)

    def describe_result_count_with_options(self, request, runtime):
        """
        @summary 下钻分析
        

        @param request: DescribeResultCountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeResultCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResultCount',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeResultCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_result_count(self, request):
        """
        @summary 下钻分析
        

        @param request: DescribeResultCountRequest

        @return: DescribeResultCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_result_count_with_options(request, runtime)

    def describe_risk_line_chart_with_options(self, request, runtime):
        """
        @summary 风险地图概览图表(折线图)
        

        @param request: DescribeRiskLineChartRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRiskLineChartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskLineChart',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeRiskLineChartResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_risk_line_chart(self, request):
        """
        @summary 风险地图概览图表(折线图)
        

        @param request: DescribeRiskLineChartRequest

        @return: DescribeRiskLineChartResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_line_chart_with_options(request, runtime)

    def describe_rule_bar_chart_with_options(self, request, runtime):
        """
        @summary 策略概览列表
        

        @param request: DescribeRuleBarChartRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRuleBarChartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleBarChart',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeRuleBarChartResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rule_bar_chart(self, request):
        """
        @summary 策略概览列表
        

        @param request: DescribeRuleBarChartRequest

        @return: DescribeRuleBarChartResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_bar_chart_with_options(request, runtime)

    def describe_rule_count_by_user_id_with_options(self, request, runtime):
        """
        @summary 根据用户Id查询策略数
        

        @param request: DescribeRuleCountByUserIdRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRuleCountByUserIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleCountByUserId',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeRuleCountByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rule_count_by_user_id(self, request):
        """
        @summary 根据用户Id查询策略数
        

        @param request: DescribeRuleCountByUserIdRequest

        @return: DescribeRuleCountByUserIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_count_by_user_id_with_options(request, runtime)

    def describe_rule_detail_by_rule_id_with_options(self, request, runtime):
        """
        @summary 查询策略/版本详情
        

        @param request: DescribeRuleDetailByRuleIdRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRuleDetailByRuleIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_id):
            query['ruleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleDetailByRuleId',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeRuleDetailByRuleIdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rule_detail_by_rule_id(self, request):
        """
        @summary 查询策略/版本详情
        

        @param request: DescribeRuleDetailByRuleIdRequest

        @return: DescribeRuleDetailByRuleIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_detail_by_rule_id_with_options(request, runtime)

    def describe_rule_hit_with_options(self, request, runtime):
        """
        @summary 查询策略命中详情
        

        @param request: DescribeRuleHitRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRuleHitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_id):
            query['ruleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_snapshot_id):
            query['ruleSnapshotId'] = request.rule_snapshot_id
        if not UtilClient.is_unset(request.s_request_id):
            query['sRequestId'] = request.s_request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleHit',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeRuleHitResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rule_hit(self, request):
        """
        @summary 查询策略命中详情
        

        @param request: DescribeRuleHitRequest

        @return: DescribeRuleHitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_hit_with_options(request, runtime)

    def describe_rule_list_by_event_codes_list_with_options(self, request, runtime):
        """
        @summary 查询策略列表
        

        @param request: DescribeRuleListByEventCodesListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRuleListByEventCodesListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleListByEventCodesList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeRuleListByEventCodesListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rule_list_by_event_codes_list(self, request):
        """
        @summary 查询策略列表
        

        @param request: DescribeRuleListByEventCodesListRequest

        @return: DescribeRuleListByEventCodesListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_list_by_event_codes_list_with_options(request, runtime)

    def describe_rule_page_list_with_options(self, request, runtime):
        """
        @summary 查询策略列表
        

        @param request: DescribeRulePageListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRulePageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_auth_type):
            query['ruleAuthType'] = request.rule_auth_type
        if not UtilClient.is_unset(request.rule_name):
            query['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_status):
            query['ruleStatus'] = request.rule_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRulePageList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeRulePageListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rule_page_list(self, request):
        """
        @summary 查询策略列表
        

        @param request: DescribeRulePageListRequest

        @return: DescribeRulePageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_page_list_with_options(request, runtime)

    def describe_rule_snapshot_with_options(self, request, runtime):
        """
        @summary 根据ruleId+version查询历史快照
        

        @param request: DescribeRuleSnapshotRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRuleSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_id):
            query['ruleId'] = request.rule_id
        if not UtilClient.is_unset(request.snapshot_version):
            query['snapshotVersion'] = request.snapshot_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleSnapshot',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeRuleSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rule_snapshot(self, request):
        """
        @summary 根据ruleId+version查询历史快照
        

        @param request: DescribeRuleSnapshotRequest

        @return: DescribeRuleSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_snapshot_with_options(request, runtime)

    def describe_rule_version_list_with_options(self, request, runtime):
        """
        @summary 查询策略版本列表
        

        @param request: DescribeRuleVersionListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRuleVersionListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_id):
            query['ruleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleVersionList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeRuleVersionListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rule_version_list(self, request):
        """
        @summary 查询策略版本列表
        

        @param request: DescribeRuleVersionListRequest

        @return: DescribeRuleVersionListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_version_list_with_options(request, runtime)

    def describe_sdkdownload_list_with_options(self, request, runtime):
        """
        @summary 获取老旧版本sdk下载列表
        

        @param request: DescribeSDKDownloadListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSDKDownloadListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.device_type):
            query['deviceType'] = request.device_type
        if not UtilClient.is_unset(request.list_type):
            query['listType'] = request.list_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSDKDownloadList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSDKDownloadListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sdkdownload_list(self, request):
        """
        @summary 获取老旧版本sdk下载列表
        

        @param request: DescribeSDKDownloadListRequest

        @return: DescribeSDKDownloadListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sdkdownload_list_with_options(request, runtime)

    def describe_saf_console_with_options(self, request, runtime):
        """

        @param request: DescribeSafConsoleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSafConsoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.content):
            query['content'] = request.content
        if not UtilClient.is_unset(request.service):
            query['service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSafConsole',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSafConsoleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_saf_console(self, request):
        """

        @param request: DescribeSafConsoleRequest

        @return: DescribeSafConsoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_saf_console_with_options(request, runtime)

    def describe_saf_de_order_with_options(self, request, runtime):
        """
        @summary 查询saf_de订单
        

        @param request: DescribeSafDeOrderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSafDeOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.start_date):
            query['startDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSafDeOrder',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSafDeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_saf_de_order(self, request):
        """
        @summary 查询saf_de订单
        

        @param request: DescribeSafDeOrderRequest

        @return: DescribeSafDeOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_saf_de_order_with_options(request, runtime)

    def describe_saf_order_with_options(self, request, runtime):
        """
        @summary 查询订单信息
        

        @param request: DescribeSafOrderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSafOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        if not UtilClient.is_unset(request.exact_product_code):
            query['exactProductCode'] = request.exact_product_code
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.start_date):
            query['startDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSafOrder',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSafOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_saf_order(self, request):
        """
        @summary 查询订单信息
        

        @param request: DescribeSafOrderRequest

        @return: DescribeSafOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_saf_order_with_options(request, runtime)

    def describe_saf_start_config_with_options(self, request, runtime):
        """
        @summary 查询接入配置
        

        @param request: DescribeSafStartConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSafStartConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSafStartConfig',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSafStartConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_saf_start_config(self, request):
        """
        @summary 查询接入配置
        

        @param request: DescribeSafStartConfigRequest

        @return: DescribeSafStartConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_saf_start_config_with_options(request, runtime)

    def describe_saf_start_steps_with_options(self, request, runtime):
        """
        @summary 查询接入配置
        

        @param request: DescribeSafStartStepsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSafStartStepsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.aliyun_server):
            query['aliyunServer'] = request.aliyun_server
        if not UtilClient.is_unset(request.device_types_str):
            query['deviceTypesStr'] = request.device_types_str
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.language):
            query['language'] = request.language
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.server_region):
            query['serverRegion'] = request.server_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSafStartSteps',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSafStartStepsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_saf_start_steps(self, request):
        """
        @summary 查询接入配置
        

        @param request: DescribeSafStartStepsRequest

        @return: DescribeSafStartStepsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_saf_start_steps_with_options(request, runtime)

    def describe_saf_tag_list_with_options(self, request, runtime):
        """
        @summary 获取风险标签列表
        

        @param request: DescribeSafTagListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSafTagListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.api_id):
            query['apiId'] = request.api_id
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSafTagList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSafTagListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_saf_tag_list(self, request):
        """
        @summary 获取风险标签列表
        

        @param request: DescribeSafTagListRequest

        @return: DescribeSafTagListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_saf_tag_list_with_options(request, runtime)

    def describe_sample_data_list_with_options(self, request, runtime):
        """
        @summary 样本列表分页查询
        

        @param request: DescribeSampleDataListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSampleDataListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.delete_tag):
            query['deleteTag'] = request.delete_tag
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_content):
            query['queryContent'] = request.query_content
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.sample_id):
            query['sampleId'] = request.sample_id
        if not UtilClient.is_unset(request.scene):
            query['scene'] = request.scene
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSampleDataList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSampleDataListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sample_data_list(self, request):
        """
        @summary 样本列表分页查询
        

        @param request: DescribeSampleDataListRequest

        @return: DescribeSampleDataListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sample_data_list_with_options(request, runtime)

    def describe_sample_demo_download_url_with_options(self, request, runtime):
        """
        @summary 查询样本示例授权
        

        @param request: DescribeSampleDemoDownloadUrlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSampleDemoDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.scene):
            query['scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSampleDemoDownloadUrl',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSampleDemoDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sample_demo_download_url(self, request):
        """
        @summary 查询样本示例授权
        

        @param request: DescribeSampleDemoDownloadUrlRequest

        @return: DescribeSampleDemoDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sample_demo_download_url_with_options(request, runtime)

    def describe_sample_download_url_with_options(self, request, runtime):
        """
        @summary 查询样本下载授权信息
        

        @param request: DescribeSampleDownloadUrlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSampleDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.sample_id):
            query['sampleId'] = request.sample_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSampleDownloadUrl',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSampleDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sample_download_url(self, request):
        """
        @summary 查询样本下载授权信息
        

        @param request: DescribeSampleDownloadUrlRequest

        @return: DescribeSampleDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sample_download_url_with_options(request, runtime)

    def describe_sample_info_with_options(self, request, runtime):
        """
        @summary 查询样本详情
        

        @param request: DescribeSampleInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSampleInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.versions):
            query['versions'] = request.versions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSampleInfo',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSampleInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sample_info(self, request):
        """
        @summary 查询样本详情
        

        @param request: DescribeSampleInfoRequest

        @return: DescribeSampleInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sample_info_with_options(request, runtime)

    def describe_sample_list_with_options(self, request, runtime):
        """
        @summary 查询样本列表
        

        @param request: DescribeSampleListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSampleListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.sample_type):
            query['sampleType'] = request.sample_type
        if not UtilClient.is_unset(request.sample_value):
            query['sampleValue'] = request.sample_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSampleList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSampleListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sample_list(self, request):
        """
        @summary 查询样本列表
        

        @param request: DescribeSampleListRequest

        @return: DescribeSampleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sample_list_with_options(request, runtime)

    def describe_sample_scene_list_with_options(self, request, runtime):
        """
        @summary 查询场景列表
        

        @param request: DescribeSampleSceneListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSampleSceneListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSampleSceneList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSampleSceneListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sample_scene_list(self, request):
        """
        @summary 查询场景列表
        

        @param request: DescribeSampleSceneListRequest

        @return: DescribeSampleSceneListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sample_scene_list_with_options(request, runtime)

    def describe_sample_tag_list_with_options(self, request, runtime):
        """
        @summary 获取标签列表
        

        @param request: DescribeSampleTagListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSampleTagListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSampleTagList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSampleTagListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sample_tag_list(self, request):
        """
        @summary 获取标签列表
        

        @param request: DescribeSampleTagListRequest

        @return: DescribeSampleTagListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sample_tag_list_with_options(request, runtime)

    def describe_sample_upload_policy_with_options(self, request, runtime):
        """
        @summary 查询样本上传授权信息
        

        @param request: DescribeSampleUploadPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSampleUploadPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSampleUploadPolicy',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSampleUploadPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sample_upload_policy(self, request):
        """
        @summary 查询样本上传授权信息
        

        @param request: DescribeSampleUploadPolicyRequest

        @return: DescribeSampleUploadPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sample_upload_policy_with_options(request, runtime)

    def describe_scene_all_event_name_code_list_with_options(self, request, runtime):
        """
        @summary 场景化服务事件下拉列表
        

        @param request: DescribeSceneAllEventNameCodeListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSceneAllEventNameCodeListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSceneAllEventNameCodeList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSceneAllEventNameCodeListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scene_all_event_name_code_list(self, request):
        """
        @summary 场景化服务事件下拉列表
        

        @param request: DescribeSceneAllEventNameCodeListRequest

        @return: DescribeSceneAllEventNameCodeListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_all_event_name_code_list_with_options(request, runtime)

    def describe_scene_event_page_list_with_options(self, request, runtime):
        """
        @summary 场景化风控事件列表
        

        @param request: DescribeSceneEventPageListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSceneEventPageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.name_or_code):
            query['nameOrCode'] = request.name_or_code
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSceneEventPageList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSceneEventPageListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scene_event_page_list(self, request):
        """
        @summary 场景化风控事件列表
        

        @param request: DescribeSceneEventPageListRequest

        @return: DescribeSceneEventPageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_event_page_list_with_options(request, runtime)

    def describe_scene_rule_page_list_with_options(self, request, runtime):
        """
        @summary 风控服务白盒化策略列表
        

        @param request: DescribeSceneRulePageListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSceneRulePageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_auth_type):
            query['ruleAuthType'] = request.rule_auth_type
        if not UtilClient.is_unset(request.rule_name):
            query['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_status):
            query['ruleStatus'] = request.rule_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSceneRulePageList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSceneRulePageListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scene_rule_page_list(self, request):
        """
        @summary 风控服务白盒化策略列表
        

        @param request: DescribeSceneRulePageListRequest

        @return: DescribeSceneRulePageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scene_rule_page_list_with_options(request, runtime)

    def describe_score_section_num_line_chart_with_options(self, request, runtime):
        """
        @summary 分值区间数量分析
        

        @param request: DescribeScoreSectionNumLineChartRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeScoreSectionNumLineChartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.by_pass_event_codes):
            query['byPassEventCodes'] = request.by_pass_event_codes
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.main_event_codes):
            query['mainEventCodes'] = request.main_event_codes
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.shunt_event_codes):
            query['shuntEventCodes'] = request.shunt_event_codes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScoreSectionNumLineChart',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeScoreSectionNumLineChartResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_score_section_num_line_chart(self, request):
        """
        @summary 分值区间数量分析
        

        @param request: DescribeScoreSectionNumLineChartRequest

        @return: DescribeScoreSectionNumLineChartResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_score_section_num_line_chart_with_options(request, runtime)

    def describe_score_section_pie_chart_with_options(self, request, runtime):
        """
        @summary 主事件/旁路事件/分流事件分值区间占比
        

        @param request: DescribeScoreSectionPieChartRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeScoreSectionPieChartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.event_type):
            query['eventType'] = request.event_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScoreSectionPieChart',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeScoreSectionPieChartResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_score_section_pie_chart(self, request):
        """
        @summary 主事件/旁路事件/分流事件分值区间占比
        

        @param request: DescribeScoreSectionPieChartRequest

        @return: DescribeScoreSectionPieChartResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_score_section_pie_chart_with_options(request, runtime)

    def describe_score_section_ratio_line_chart_with_options(self, request, runtime):
        """
        @summary 分值区间占比分析
        

        @param request: DescribeScoreSectionRatioLineChartRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeScoreSectionRatioLineChartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.by_pass_event_codes):
            query['byPassEventCodes'] = request.by_pass_event_codes
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.main_event_codes):
            query['mainEventCodes'] = request.main_event_codes
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.shunt_event_codes):
            query['shuntEventCodes'] = request.shunt_event_codes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScoreSectionRatioLineChart',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeScoreSectionRatioLineChartResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_score_section_ratio_line_chart(self, request):
        """
        @summary 分值区间占比分析
        

        @param request: DescribeScoreSectionRatioLineChartRequest

        @return: DescribeScoreSectionRatioLineChartResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_score_section_ratio_line_chart_with_options(request, runtime)

    def describe_select_item_with_options(self, request, runtime):
        """
        @summary 查询任务ID列表
        

        @param request: DescribeSelectItemRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSelectItemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSelectItem',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSelectItemResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_select_item(self, request):
        """
        @summary 查询任务ID列表
        

        @param request: DescribeSelectItemRequest

        @return: DescribeSelectItemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_select_item_with_options(request, runtime)

    def describe_service_app_key_with_options(self, request, runtime):
        """
        @summary ServiceAppkey下拉
        

        @param request: DescribeServiceAppKeyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeServiceAppKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceAppKey',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeServiceAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_service_app_key(self, request):
        """
        @summary ServiceAppkey下拉
        

        @param request: DescribeServiceAppKeyRequest

        @return: DescribeServiceAppKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_service_app_key_with_options(request, runtime)

    def describe_service_consume_with_options(self, request, runtime):
        """
        @summary 获取服务调用量
        

        @param request: DescribeServiceConsumeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeServiceConsumeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.service_code):
            query['serviceCode'] = request.service_code
        if not UtilClient.is_unset(request.start_date):
            query['startDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceConsume',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeServiceConsumeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_service_consume(self, request):
        """
        @summary 获取服务调用量
        

        @param request: DescribeServiceConsumeRequest

        @return: DescribeServiceConsumeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_service_consume_with_options(request, runtime)

    def describe_service_consume_download_url_with_options(self, request, runtime):
        """
        @summary 下载服务调用量数据文件URL
        

        @param request: DescribeServiceConsumeDownloadUrlRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeServiceConsumeDownloadUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.service_code):
            query['serviceCode'] = request.service_code
        if not UtilClient.is_unset(request.start_date):
            query['startDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceConsumeDownloadUrl',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeServiceConsumeDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_service_consume_download_url(self, request):
        """
        @summary 下载服务调用量数据文件URL
        

        @param request: DescribeServiceConsumeDownloadUrlRequest

        @return: DescribeServiceConsumeDownloadUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_service_consume_download_url_with_options(request, runtime)

    def describe_service_list_with_options(self, request, runtime):
        """
        @summary 获取服务列表
        

        @param request: DescribeServiceListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeServiceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeServiceListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_service_list(self, request):
        """
        @summary 获取服务列表
        

        @param request: DescribeServiceListRequest

        @return: DescribeServiceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_service_list_with_options(request, runtime)

    def describe_simulation_predit_info_with_options(self, request, runtime):
        """
        @summary 预估调用信息
        

        @param request: DescribeSimulationPreditInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSimulationPreditInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rules_str):
            query['rulesStr'] = request.rules_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSimulationPreditInfo',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSimulationPreditInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_simulation_predit_info(self, request):
        """
        @summary 预估调用信息
        

        @param request: DescribeSimulationPreditInfoRequest

        @return: DescribeSimulationPreditInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_simulation_predit_info_with_options(request, runtime)

    def describe_simulation_task_count_with_options(self, request, runtime):
        """
        @summary 查询任务记录数
        

        @param request: DescribeSimulationTaskCountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSimulationTaskCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.data_source_config):
            query['dataSourceConfig'] = request.data_source_config
        if not UtilClient.is_unset(request.data_source_type):
            query['dataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.filters_str):
            query['filtersStr'] = request.filters_str
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSimulationTaskCount',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSimulationTaskCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_simulation_task_count(self, request):
        """
        @summary 查询任务记录数
        

        @param request: DescribeSimulationTaskCountRequest

        @return: DescribeSimulationTaskCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_simulation_task_count_with_options(request, runtime)

    def describe_simulation_task_list_with_options(self, request, runtime):
        """
        @summary 任务列表
        

        @param request: DescribeSimulationTaskListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSimulationTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSimulationTaskList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSimulationTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_simulation_task_list(self, request):
        """
        @summary 任务列表
        

        @param request: DescribeSimulationTaskListRequest

        @return: DescribeSimulationTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_simulation_task_list_with_options(request, runtime)

    def describe_sls_url_config_with_options(self, request, runtime):
        """
        @summary 获取project配置
        

        @param request: DescribeSlsUrlConfigRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSlsUrlConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlsUrlConfig',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSlsUrlConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sls_url_config(self, request):
        """
        @summary 获取project配置
        

        @param request: DescribeSlsUrlConfigRequest

        @return: DescribeSlsUrlConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_url_config_with_options(request, runtime)

    def describe_support_rule_list_with_options(self, request, runtime):
        """
        @summary 查询支持仿真的策略列表
        

        @param request: DescribeSupportRuleListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSupportRuleListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSupportRuleList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeSupportRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_support_rule_list(self, request):
        """
        @summary 查询支持仿真的策略列表
        

        @param request: DescribeSupportRuleListRequest

        @return: DescribeSupportRuleListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_support_rule_list_with_options(request, runtime)

    def describe_tag_list_with_options(self, request, runtime):
        """
        @summary 标签列表
        

        @param request: DescribeTagListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTagListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeTagListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tag_list(self, request):
        """
        @summary 标签列表
        

        @param request: DescribeTagListRequest

        @return: DescribeTagListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_list_with_options(request, runtime)

    def describe_tags_bar_chart_with_options(self, request, runtime):
        """
        @summary 标签概览列表
        

        @param request: DescribeTagsBarChartRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTagsBarChartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.result):
            query['result'] = request.result
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagsBarChart',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeTagsBarChartResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tags_bar_chart(self, request):
        """
        @summary 标签概览列表
        

        @param request: DescribeTagsBarChartRequest

        @return: DescribeTagsBarChartResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_bar_chart_with_options(request, runtime)

    def describe_tags_fluctuation_with_options(self, request, runtime):
        """
        @summary 标签波动检测
        

        @param request: DescribeTagsFluctuationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTagsFluctuationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagsFluctuation',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeTagsFluctuationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tags_fluctuation(self, request):
        """
        @summary 标签波动检测
        

        @param request: DescribeTagsFluctuationRequest

        @return: DescribeTagsFluctuationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_fluctuation_with_options(request, runtime)

    def describe_tags_list_with_options(self, request, runtime):
        """
        @summary 获取标签列表
        

        @param request: DescribeTagsListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTagsListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagsList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeTagsListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tags_list(self, request):
        """
        @summary 获取标签列表
        

        @param request: DescribeTagsListRequest

        @return: DescribeTagsListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_list_with_options(request, runtime)

    def describe_tags_num_line_chart_with_options(self, request, runtime):
        """
        @summary 标签命中数量分析
        

        @param request: DescribeTagsNumLineChartRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTagsNumLineChartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.by_pass_event_codes):
            query['byPassEventCodes'] = request.by_pass_event_codes
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.main_event_codes):
            query['mainEventCodes'] = request.main_event_codes
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.shunt_event_codes):
            query['shuntEventCodes'] = request.shunt_event_codes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagsNumLineChart',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeTagsNumLineChartResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tags_num_line_chart(self, request):
        """
        @summary 标签命中数量分析
        

        @param request: DescribeTagsNumLineChartRequest

        @return: DescribeTagsNumLineChartResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_num_line_chart_with_options(request, runtime)

    def describe_tags_ratio_line_chart_with_options(self, request, runtime):
        """
        @summary 标签命中占比分析
        

        @param request: DescribeTagsRatioLineChartRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTagsRatioLineChartResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.by_pass_event_codes):
            query['byPassEventCodes'] = request.by_pass_event_codes
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.main_event_codes):
            query['mainEventCodes'] = request.main_event_codes
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.shunt_event_codes):
            query['shuntEventCodes'] = request.shunt_event_codes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagsRatioLineChart',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeTagsRatioLineChartResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tags_ratio_line_chart(self, request):
        """
        @summary 标签命中占比分析
        

        @param request: DescribeTagsRatioLineChartRequest

        @return: DescribeTagsRatioLineChartResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_ratio_line_chart_with_options(request, runtime)

    def describe_tags_trend_with_options(self, request, runtime):
        """
        @summary 标签命中趋势
        

        @param request: DescribeTagsTrendRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTagsTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.result):
            query['result'] = request.result
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTagsTrend',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeTagsTrendResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tags_trend(self, request):
        """
        @summary 标签命中趋势
        

        @param request: DescribeTagsTrendRequest

        @return: DescribeTagsTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_trend_with_options(request, runtime)

    def describe_task_list_with_options(self, request, runtime):
        """
        @summary 任务列表
        

        @param request: DescribeTaskListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.is_page):
            query['IsPage'] = request.is_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTaskList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_task_list(self, request):
        """
        @summary 任务列表
        

        @param request: DescribeTaskListRequest

        @return: DescribeTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_task_list_with_options(request, runtime)

    def describe_task_log_list_with_options(self, request, runtime):
        """
        @summary 任务日志列表
        

        @param request: DescribeTaskLogListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTaskLogListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.is_page):
            query['IsPage'] = request.is_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_log_id):
            query['TaskLogId'] = request.task_log_id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTaskLogList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeTaskLogListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_task_log_list(self, request):
        """
        @summary 任务日志列表
        

        @param request: DescribeTaskLogListRequest

        @return: DescribeTaskLogListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_task_log_list_with_options(request, runtime)

    def describe_template_base_info_by_template_id_with_options(self, request, runtime):
        """
        @summary 查询事件模版详情
        

        @param request: DescribeTemplateBaseInfoByTemplateIdRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTemplateBaseInfoByTemplateIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplateBaseInfoByTemplateId',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeTemplateBaseInfoByTemplateIdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_template_base_info_by_template_id(self, request):
        """
        @summary 查询事件模版详情
        

        @param request: DescribeTemplateBaseInfoByTemplateIdRequest

        @return: DescribeTemplateBaseInfoByTemplateIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_template_base_info_by_template_id_with_options(request, runtime)

    def describe_template_count_with_options(self, request, runtime):
        """
        @summary 查询事件总数量
        

        @param request: DescribeTemplateCountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTemplateCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplateCount',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeTemplateCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_template_count(self, request):
        """
        @summary 查询事件总数量
        

        @param request: DescribeTemplateCountRequest

        @return: DescribeTemplateCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_template_count_with_options(request, runtime)

    def describe_template_download_with_options(self, request, runtime):
        """
        @summary 模版下载
        

        @param request: DescribeTemplateDownloadRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTemplateDownloadResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplateDownload',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeTemplateDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_template_download(self, request):
        """
        @summary 模版下载
        

        @param request: DescribeTemplateDownloadRequest

        @return: DescribeTemplateDownloadResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_template_download_with_options(request, runtime)

    def describe_template_page_list_with_options(self, request, runtime):
        """
        @summary 根据事件名称查询事件列表
        

        @param request: DescribeTemplatePageListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTemplatePageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.template_name):
            query['templateName'] = request.template_name
        if not UtilClient.is_unset(request.template_search_item):
            query['templateSearchItem'] = request.template_search_item
        if not UtilClient.is_unset(request.template_status):
            query['templateStatus'] = request.template_status
        if not UtilClient.is_unset(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplatePageList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeTemplatePageListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_template_page_list(self, request):
        """
        @summary 根据事件名称查询事件列表
        

        @param request: DescribeTemplatePageListRequest

        @return: DescribeTemplatePageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_template_page_list_with_options(request, runtime)

    def describe_used_service_with_options(self, request, runtime):
        """
        @summary 获取用户使用过服务列表
        

        @param request: DescribeUsedServiceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeUsedServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsedService',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeUsedServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_used_service(self, request):
        """
        @summary 获取用户使用过服务列表
        

        @param request: DescribeUsedServiceRequest

        @return: DescribeUsedServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_used_service_with_options(request, runtime)

    def describe_user_info_with_options(self, request, runtime):
        """
        @summary 获取当前登录用户信息
        

        @param request: DescribeUserInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeUserInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserInfo',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_info(self, request):
        """
        @summary 获取当前登录用户信息
        

        @param request: DescribeUserInfoRequest

        @return: DescribeUserInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_info_with_options(request, runtime)

    def describe_variable_bind_detail_with_options(self, request, runtime):
        """
        @summary 查询变量绑定信息
        

        @param request: DescribeVariableBindDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVariableBindDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.define_id):
            query['defineId'] = request.define_id
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVariableBindDetail',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeVariableBindDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_variable_bind_detail(self, request):
        """
        @summary 查询变量绑定信息
        

        @param request: DescribeVariableBindDetailRequest

        @return: DescribeVariableBindDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_variable_bind_detail_with_options(request, runtime)

    def describe_variable_detail_with_options(self, request, runtime):
        """
        @summary 查询变量详情
        

        @param request: DescribeVariableDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVariableDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVariableDetail',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeVariableDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_variable_detail(self, request):
        """
        @summary 查询变量详情
        

        @param request: DescribeVariableDetailRequest

        @return: DescribeVariableDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_variable_detail_with_options(request, runtime)

    def describe_variable_fee_with_options(self, request, runtime):
        """
        @summary 查询变量收费信息
        

        @param request: DescribeVariableFeeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVariableFeeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.ids):
            query['ids'] = request.ids
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVariableFee',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeVariableFeeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_variable_fee(self, request):
        """
        @summary 查询变量收费信息
        

        @param request: DescribeVariableFeeRequest

        @return: DescribeVariableFeeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_variable_fee_with_options(request, runtime)

    def describe_variable_list_with_options(self, request, runtime):
        """
        @summary 查询变量详情
        

        @param request: DescribeVariableListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVariableListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.ref_obj_id):
            query['refObjId'] = request.ref_obj_id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.types_str):
            query['typesStr'] = request.types_str
        if not UtilClient.is_unset(request.value):
            query['value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVariableList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeVariableListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_variable_list(self, request):
        """
        @summary 查询变量详情
        

        @param request: DescribeVariableListRequest

        @return: DescribeVariableListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_variable_list_with_options(request, runtime)

    def describe_variable_market_list_with_options(self, request, runtime):
        """
        @summary 查询变量定义
        

        @param request: DescribeVariableMarketListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVariableMarketListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.charging_mode):
            query['chargingMode'] = request.charging_mode
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.paging):
            query['paging'] = request.paging
        if not UtilClient.is_unset(request.query_content):
            query['queryContent'] = request.query_content
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.scenes_str):
            query['scenesStr'] = request.scenes_str
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVariableMarketList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeVariableMarketListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_variable_market_list(self, request):
        """
        @summary 查询变量定义
        

        @param request: DescribeVariableMarketListRequest

        @return: DescribeVariableMarketListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_variable_market_list_with_options(request, runtime)

    def describe_variable_scene_list_with_options(self, request, runtime):
        """
        @summary 查询配置信息
        

        @param request: DescribeVariableSceneListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeVariableSceneListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.biz_type):
            query['bizType'] = request.biz_type
        if not UtilClient.is_unset(request.config_key):
            query['configKey'] = request.config_key
        if not UtilClient.is_unset(request.current_page):
            query['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.paging):
            query['paging'] = request.paging
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVariableSceneList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.DescribeVariableSceneListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_variable_scene_list(self, request):
        """
        @summary 查询配置信息
        

        @param request: DescribeVariableSceneListRequest

        @return: DescribeVariableSceneListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_variable_scene_list_with_options(request, runtime)

    def expression_test_with_options(self, request, runtime):
        """
        @summary 自定义变量测试
        

        @param request: ExpressionTestRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ExpressionTestResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.expression):
            query['expression'] = request.expression
        if not UtilClient.is_unset(request.expression_variable):
            query['expressionVariable'] = request.expression_variable
        if not UtilClient.is_unset(request.expression_variable_ids):
            query['expressionVariableIds'] = request.expression_variable_ids
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.scene):
            query['scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExpressionTest',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.ExpressionTestResponse(),
            self.call_api(params, req, runtime)
        )

    def expression_test(self, request):
        """
        @summary 自定义变量测试
        

        @param request: ExpressionTestRequest

        @return: ExpressionTestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.expression_test_with_options(request, runtime)

    def file_upload_with_options(self, request, runtime):
        """
        @summary 文件上传
        

        @param request: FileUploadRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: FileUploadResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.tab):
            query['Tab'] = request.tab
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FileUpload',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.FileUploadResponse(),
            self.call_api(params, req, runtime)
        )

    def file_upload(self, request):
        """
        @summary 文件上传
        

        @param request: FileUploadRequest

        @return: FileUploadResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.file_upload_with_options(request, runtime)

    def import_name_list_with_options(self, request, runtime):
        """
        @summary 创建或导入名单
        

        @param request: ImportNameListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ImportNameListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.data):
            query['data'] = request.data
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.import_type):
            query['importType'] = request.import_type
        if not UtilClient.is_unset(request.name_list_type):
            query['nameListType'] = request.name_list_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
        if not UtilClient.is_unset(request.variable_id):
            query['variableId'] = request.variable_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportNameList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.ImportNameListResponse(),
            self.call_api(params, req, runtime)
        )

    def import_name_list(self, request):
        """
        @summary 创建或导入名单
        

        @param request: ImportNameListRequest

        @return: ImportNameListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_name_list_with_options(request, runtime)

    def import_template_event_with_options(self, request, runtime):
        """
        @summary 导入模板事件
        

        @param request: ImportTemplateEventRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ImportTemplateEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_template_ids):
            query['eventTemplateIds'] = request.event_template_ids
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportTemplateEvent',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.ImportTemplateEventResponse(),
            self.call_api(params, req, runtime)
        )

    def import_template_event(self, request):
        """
        @summary 导入模板事件
        

        @param request: ImportTemplateEventRequest

        @return: ImportTemplateEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_template_event_with_options(request, runtime)

    def modify_app_key_with_options(self, request, runtime):
        """
        @summary 更新备注
        

        @param request: ModifyAppKeyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyAppKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.app_key):
            query['appKey'] = request.app_key
        if not UtilClient.is_unset(request.memo):
            query['memo'] = request.memo
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppKey',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.ModifyAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_app_key(self, request):
        """
        @summary 更新备注
        

        @param request: ModifyAppKeyRequest

        @return: ModifyAppKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_app_key_with_options(request, runtime)

    def modify_cust_variable_with_options(self, request, runtime):
        """
        @summary 编辑累计变量
        

        @param request: ModifyCustVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyCustVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.condition):
            query['condition'] = request.condition
        if not UtilClient.is_unset(request.data_version):
            query['dataVersion'] = request.data_version
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.event_codes):
            query['eventCodes'] = request.event_codes
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.outputs):
            query['outputs'] = request.outputs
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCustVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.ModifyCustVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cust_variable(self, request):
        """
        @summary 编辑累计变量
        

        @param request: ModifyCustVariableRequest

        @return: ModifyCustVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cust_variable_with_options(request, runtime)

    def modify_event_with_options(self, request, runtime):
        """
        @summary 编辑事件
        

        @param request: ModifyEventRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.biz_version):
            query['bizVersion'] = request.biz_version
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.input_fields_str):
            query['inputFieldsStr'] = request.input_fields_str
        if not UtilClient.is_unset(request.memo):
            query['memo'] = request.memo
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.template_type):
            query['templateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEvent',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.ModifyEventResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_event(self, request):
        """
        @summary 编辑事件
        

        @param request: ModifyEventRequest

        @return: ModifyEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_event_with_options(request, runtime)

    def modify_event_status_with_options(self, request, runtime):
        """
        @summary 修改事件状态
        

        @param request: ModifyEventStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyEventStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.from_event_satus):
            query['fromEventSatus'] = request.from_event_satus
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.to_event_satus):
            query['toEventSatus'] = request.to_event_satus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEventStatus',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.ModifyEventStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_event_status(self, request):
        """
        @summary 修改事件状态
        

        @param request: ModifyEventStatusRequest

        @return: ModifyEventStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_event_status_with_options(request, runtime)

    def modify_expression_variable_with_options(self, request, runtime):
        """
        @summary 编辑自定义变量
        

        @param request: ModifyExpressionVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyExpressionVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.data_version):
            query['dataVersion'] = request.data_version
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.expression):
            query['expression'] = request.expression
        if not UtilClient.is_unset(request.expression_title):
            query['expressionTitle'] = request.expression_title
        if not UtilClient.is_unset(request.expression_variable):
            query['expressionVariable'] = request.expression_variable
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.outlier):
            query['outlier'] = request.outlier
        if not UtilClient.is_unset(request.outputs):
            query['outputs'] = request.outputs
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyExpressionVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.ModifyExpressionVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_expression_variable(self, request):
        """
        @summary 编辑自定义变量
        

        @param request: ModifyExpressionVariableRequest

        @return: ModifyExpressionVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_expression_variable_with_options(request, runtime)

    def modify_field_with_options(self, request, runtime):
        """
        @summary 修改字段
        

        @param request: ModifyFieldRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyFieldResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.classify):
            query['classify'] = request.classify
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.enum_data):
            query['enumData'] = request.enum_data
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyField',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.ModifyFieldResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_field(self, request):
        """
        @summary 修改字段
        

        @param request: ModifyFieldRequest

        @return: ModifyFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_field_with_options(request, runtime)

    def modify_poc_task_with_options(self, request, runtime):
        """
        @summary 修改poc任务
        

        @param request: ModifyPocTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyPocTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.access_type):
            query['accessType'] = request.access_type
        if not UtilClient.is_unset(request.config):
            query['config'] = request.config
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            query['fileType'] = request.file_type
        if not UtilClient.is_unset(request.file_url):
            query['fileUrl'] = request.file_url
        if not UtilClient.is_unset(request.reason):
            query['reason'] = request.reason
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.service_code):
            query['serviceCode'] = request.service_code
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            query['taskName'] = request.task_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPocTask',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.ModifyPocTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_poc_task(self, request):
        """
        @summary 修改poc任务
        

        @param request: ModifyPocTaskRequest

        @return: ModifyPocTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_poc_task_with_options(request, runtime)

    def modify_rule_priority_with_options(self, request, runtime):
        """
        @summary 策略修改优先级
        

        @param request: ModifyRulePriorityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyRulePriorityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not UtilClient.is_unset(request.priority):
            query['priority'] = request.priority
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_id):
            query['ruleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRulePriority',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.ModifyRulePriorityResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_rule_priority(self, request):
        """
        @summary 策略修改优先级
        

        @param request: ModifyRulePriorityRequest

        @return: ModifyRulePriorityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_rule_priority_with_options(request, runtime)

    def modify_rule_status_with_options(self, request, runtime):
        """
        @summary 策略版本申请状态变更
        

        @param request: ModifyRuleStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyRuleStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.apply_user_id):
            query['applyUserId'] = request.apply_user_id
        if not UtilClient.is_unset(request.apply_user_name):
            query['applyUserName'] = request.apply_user_name
        if not UtilClient.is_unset(request.audit_remark):
            query['auditRemark'] = request.audit_remark
        if not UtilClient.is_unset(request.audit_user_id):
            query['auditUserId'] = request.audit_user_id
        if not UtilClient.is_unset(request.audit_user_name):
            query['auditUserName'] = request.audit_user_name
        if not UtilClient.is_unset(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not UtilClient.is_unset(request.event_type):
            query['eventType'] = request.event_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_audit_type):
            query['ruleAuditType'] = request.rule_audit_type
        if not UtilClient.is_unset(request.rule_id):
            query['ruleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRuleStatus',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.ModifyRuleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_rule_status(self, request):
        """
        @summary 策略版本申请状态变更
        

        @param request: ModifyRuleStatusRequest

        @return: ModifyRuleStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_rule_status_with_options(request, runtime)

    def modify_template_with_options(self, request, runtime):
        """
        @summary 修改模版
        

        @param request: ModifyTemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.input_fields):
            query['inputFields'] = request.input_fields
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['templateType'] = request.template_type
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTemplate',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.ModifyTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_template(self, request):
        """
        @summary 修改模版
        

        @param request: ModifyTemplateRequest

        @return: ModifyTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_template_with_options(request, runtime)

    def modify_template_status_with_options(self, request, runtime):
        """
        @summary 更新模版状态
        

        @param request: ModifyTemplateStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyTemplateStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.from_template_satus):
            query['fromTemplateSatus'] = request.from_template_satus
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        if not UtilClient.is_unset(request.to_template_satus):
            query['toTemplateSatus'] = request.to_template_satus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTemplateStatus',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.ModifyTemplateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_template_status(self, request):
        """
        @summary 更新模版状态
        

        @param request: ModifyTemplateStatusRequest

        @return: ModifyTemplateStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_template_status_with_options(request, runtime)

    def modify_variable_with_options(self, request, runtime):
        """
        @summary 修改变量信息
        

        @param request: ModifyVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.ModifyVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_variable(self, request):
        """
        @summary 修改变量信息
        

        @param request: ModifyVariableRequest

        @return: ModifyVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_variable_with_options(request, runtime)

    def open_console_sls_with_options(self, request, runtime):
        """
        @summary 开通服务
        

        @param request: OpenConsoleSlsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: OpenConsoleSlsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.scene):
            query['scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenConsoleSls',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.OpenConsoleSlsResponse(),
            self.call_api(params, req, runtime)
        )

    def open_console_sls(self, request):
        """
        @summary 开通服务
        

        @param request: OpenConsoleSlsRequest

        @return: OpenConsoleSlsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_console_sls_with_options(request, runtime)

    def operate_favorite_variable_with_options(self, request, runtime):
        """
        @summary 操作收藏
        

        @param request: OperateFavoriteVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: OperateFavoriteVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.operate):
            query['operate'] = request.operate
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateFavoriteVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.OperateFavoriteVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_favorite_variable(self, request):
        """
        @summary 操作收藏
        

        @param request: OperateFavoriteVariableRequest

        @return: OperateFavoriteVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_favorite_variable_with_options(request, runtime)

    def permission_check_with_options(self, request, runtime):
        """
        @summary 企业认证
        

        @param request: PermissionCheckRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PermissionCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['RegId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PermissionCheck',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.PermissionCheckResponse(),
            self.call_api(params, req, runtime)
        )

    def permission_check(self, request):
        """
        @summary 企业认证
        

        @param request: PermissionCheckRequest

        @return: PermissionCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.permission_check_with_options(request, runtime)

    def query_auth_rule_detail_by_rule_id_with_options(self, request, runtime):
        """
        @summary 白盒化策略详情查询
        

        @param request: QueryAuthRuleDetailByRuleIdRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryAuthRuleDetailByRuleIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_id):
            query['ruleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAuthRuleDetailByRuleId',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.QueryAuthRuleDetailByRuleIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_auth_rule_detail_by_rule_id(self, request):
        """
        @summary 白盒化策略详情查询
        

        @param request: QueryAuthRuleDetailByRuleIdRequest

        @return: QueryAuthRuleDetailByRuleIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_auth_rule_detail_by_rule_id_with_options(request, runtime)

    def query_auth_user_name_with_options(self, request, runtime):
        """
        @summary 获取授权用户名
        

        @param request: QueryAuthUserNameRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryAuthUserNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.bind_id):
            query['bindId'] = request.bind_id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAuthUserName',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.QueryAuthUserNameResponse(),
            self.call_api(params, req, runtime)
        )

    def query_auth_user_name(self, request):
        """
        @summary 获取授权用户名
        

        @param request: QueryAuthUserNameRequest

        @return: QueryAuthUserNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_auth_user_name_with_options(request, runtime)

    def query_authorization_user_list_with_options(self, request, runtime):
        """
        @summary 事件模版授权用户列表
        

        @param request: QueryAuthorizationUserListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryAuthorizationUserListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAuthorizationUserList',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.QueryAuthorizationUserListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_authorization_user_list(self, request):
        """
        @summary 事件模版授权用户列表
        

        @param request: QueryAuthorizationUserListRequest

        @return: QueryAuthorizationUserListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_authorization_user_list_with_options(request, runtime)

    def recall_rule_audit_with_options(self, request, runtime):
        """
        @summary 撤回
        

        @param request: RecallRuleAuditRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RecallRuleAuditResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecallRuleAudit',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.RecallRuleAuditResponse(),
            self.call_api(params, req, runtime)
        )

    def recall_rule_audit(self, request):
        """
        @summary 撤回
        

        @param request: RecallRuleAuditRequest

        @return: RecallRuleAuditResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recall_rule_audit_with_options(request, runtime)

    def remove_event_with_options(self, request, runtime):
        """
        @summary 删除事件
        

        @param request: RemoveEventRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.create_type):
            query['createType'] = request.create_type
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.template_code):
            query['templateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveEvent',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.RemoveEventResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_event(self, request):
        """
        @summary 删除事件
        

        @param request: RemoveEventRequest

        @return: RemoveEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_event_with_options(request, runtime)

    def remove_template_with_options(self, request, runtime):
        """
        @summary 删除模版事件
        

        @param request: RemoveTemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTemplate',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.RemoveTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_template(self, request):
        """
        @summary 删除模版事件
        

        @param request: RemoveTemplateRequest

        @return: RemoveTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_template_with_options(request, runtime)

    def sample_file_download_with_options(self, request, runtime):
        """
        @summary 模板下载
        

        @param request: SampleFileDownloadRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SampleFileDownloadResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['RegId'] = request.reg_id
        if not UtilClient.is_unset(request.tab):
            query['Tab'] = request.tab
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SampleFileDownload',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.SampleFileDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    def sample_file_download(self, request):
        """
        @summary 模板下载
        

        @param request: SampleFileDownloadRequest

        @return: SampleFileDownloadResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sample_file_download_with_options(request, runtime)

    def save_analysis_column_with_options(self, request, runtime):
        """
        @summary 保存自定义列
        

        @param request: SaveAnalysisColumnRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SaveAnalysisColumnResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.columns):
            query['columns'] = request.columns
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveAnalysisColumn',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.SaveAnalysisColumnResponse(),
            self.call_api(params, req, runtime)
        )

    def save_analysis_column(self, request):
        """
        @summary 保存自定义列
        

        @param request: SaveAnalysisColumnRequest

        @return: SaveAnalysisColumnResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_analysis_column_with_options(request, runtime)

    def save_by_pass_or_shunt_event_with_options(self, request, runtime):
        """
        @summary 旁路/分流配置
        

        @param request: SaveByPassOrShuntEventRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SaveByPassOrShuntEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_id):
            query['eventId'] = request.event_id
        if not UtilClient.is_unset(request.event_name):
            query['eventName'] = request.event_name
        if not UtilClient.is_unset(request.event_type):
            query['eventType'] = request.event_type
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveByPassOrShuntEvent',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.SaveByPassOrShuntEventResponse(),
            self.call_api(params, req, runtime)
        )

    def save_by_pass_or_shunt_event(self, request):
        """
        @summary 旁路/分流配置
        

        @param request: SaveByPassOrShuntEventRequest

        @return: SaveByPassOrShuntEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.save_by_pass_or_shunt_event_with_options(request, runtime)

    def start_or_stop_by_pass_shunt_event_with_options(self, request, runtime):
        """
        @summary 开启/停止旁路事件
        

        @param request: StartOrStopByPassShuntEventRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartOrStopByPassShuntEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_id):
            query['eventId'] = request.event_id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartOrStopByPassShuntEvent',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.StartOrStopByPassShuntEventResponse(),
            self.call_api(params, req, runtime)
        )

    def start_or_stop_by_pass_shunt_event(self, request):
        """
        @summary 开启/停止旁路事件
        

        @param request: StartOrStopByPassShuntEventRequest

        @return: StartOrStopByPassShuntEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_or_stop_by_pass_shunt_event_with_options(request, runtime)

    def start_simulation_task_with_options(self, request, runtime):
        """
        @summary 开始执行任务
        

        @param request: StartSimulationTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartSimulationTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSimulationTask',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.StartSimulationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def start_simulation_task(self, request):
        """
        @summary 开始执行任务
        

        @param request: StartSimulationTaskRequest

        @return: StartSimulationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_simulation_task_with_options(request, runtime)

    def stop_simulation_task_with_options(self, request, runtime):
        """
        @summary 停止任务
        

        @param request: StopSimulationTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopSimulationTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopSimulationTask',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.StopSimulationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_simulation_task(self, request):
        """
        @summary 停止任务
        

        @param request: StopSimulationTaskRequest

        @return: StopSimulationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_simulation_task_with_options(request, runtime)

    def submit_import_task_with_options(self, request, runtime):
        """
        @summary 批量创建策略
        

        @param request: SubmitImportTaskRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubmitImportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.url):
            query['url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitImportTask',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.SubmitImportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_import_task(self, request):
        """
        @summary 批量创建策略
        

        @param request: SubmitImportTaskRequest

        @return: SubmitImportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_import_task_with_options(request, runtime)

    def switch_expression_variable_with_options(self, request, runtime):
        """
        @summary 自定义变量开关
        

        @param request: SwitchExpressionVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SwitchExpressionVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.data_version):
            query['dataVersion'] = request.data_version
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchExpressionVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.SwitchExpressionVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_expression_variable(self, request):
        """
        @summary 自定义变量开关
        

        @param request: SwitchExpressionVariableRequest

        @return: SwitchExpressionVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_expression_variable_with_options(request, runtime)

    def switch_field_with_options(self, request, runtime):
        """
        @summary 字段开关
        

        @param request: SwitchFieldRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SwitchFieldResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchField',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.SwitchFieldResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_field(self, request):
        """
        @summary 字段开关
        

        @param request: SwitchFieldRequest

        @return: SwitchFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_field_with_options(request, runtime)

    def switch_query_variable_with_options(self, request, runtime):
        """
        @summary 查询变量启用/禁用
        

        @param request: SwitchQueryVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SwitchQueryVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchQueryVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.SwitchQueryVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_query_variable(self, request):
        """
        @summary 查询变量启用/禁用
        

        @param request: SwitchQueryVariableRequest

        @return: SwitchQueryVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_query_variable_with_options(request, runtime)

    def switch_to_online_with_options(self, request, runtime):
        """
        @summary 一键切换上线
        

        @param request: SwitchToOnlineRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SwitchToOnlineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_id):
            query['eventId'] = request.event_id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchToOnline',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.SwitchToOnlineResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_to_online(self, request):
        """
        @summary 一键切换上线
        

        @param request: SwitchToOnlineRequest

        @return: SwitchToOnlineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_to_online_with_options(request, runtime)

    def switch_variable_with_options(self, request, runtime):
        """
        @summary 累计变量开关
        

        @param request: SwitchVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SwitchVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.data_version):
            query['dataVersion'] = request.data_version
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.SwitchVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_variable(self, request):
        """
        @summary 累计变量开关
        

        @param request: SwitchVariableRequest

        @return: SwitchVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_variable_with_options(request, runtime)

    def task_name_by_user_id_with_options(self, request, runtime):
        """
        @summary 判断任务名是否重复
        

        @param request: TaskNameByUserIdRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TaskNameByUserIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.reg_id):
            query['RegId'] = request.reg_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TaskNameByUserId',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.TaskNameByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    def task_name_by_user_id(self, request):
        """
        @summary 判断任务名是否重复
        

        @param request: TaskNameByUserIdRequest

        @return: TaskNameByUserIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.task_name_by_user_id_with_options(request, runtime)

    def update_analysis_condition_favorite_with_options(self, request, runtime):
        """
        @summary 修改查询条件
        

        @param request: UpdateAnalysisConditionFavoriteRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAnalysisConditionFavoriteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.condition):
            query['condition'] = request.condition
        if not UtilClient.is_unset(request.event_begin_time):
            query['eventBeginTime'] = request.event_begin_time
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.event_end_time):
            query['eventEndTime'] = request.event_end_time
        if not UtilClient.is_unset(request.field_name):
            query['fieldName'] = request.field_name
        if not UtilClient.is_unset(request.field_value):
            query['fieldValue'] = request.field_value
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAnalysisConditionFavorite',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.UpdateAnalysisConditionFavoriteResponse(),
            self.call_api(params, req, runtime)
        )

    def update_analysis_condition_favorite(self, request):
        """
        @summary 修改查询条件
        

        @param request: UpdateAnalysisConditionFavoriteRequest

        @return: UpdateAnalysisConditionFavoriteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_analysis_condition_favorite_with_options(request, runtime)

    def update_audit_with_options(self, request, runtime):
        """
        @summary 审批
        

        @param request: UpdateAuditRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAuditResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.audit_msg):
            query['auditMsg'] = request.audit_msg
        if not UtilClient.is_unset(request.audit_relation_type):
            query['auditRelationType'] = request.audit_relation_type
        if not UtilClient.is_unset(request.audit_status):
            query['auditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAudit',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.UpdateAuditResponse(),
            self.call_api(params, req, runtime)
        )

    def update_audit(self, request):
        """
        @summary 审批
        

        @param request: UpdateAuditRequest

        @return: UpdateAuditResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_audit_with_options(request, runtime)

    def update_auth_rule_with_options(self, request, runtime):
        """
        @summary 修改授权策略
        

        @param request: UpdateAuthRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAuthRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_actions):
            query['ruleActions'] = request.rule_actions
        if not UtilClient.is_unset(request.rule_expressions):
            query['ruleExpressions'] = request.rule_expressions
        if not UtilClient.is_unset(request.rule_id):
            query['ruleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuthRule',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.UpdateAuthRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_auth_rule(self, request):
        """
        @summary 修改授权策略
        

        @param request: UpdateAuthRuleRequest

        @return: UpdateAuthRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_auth_rule_with_options(request, runtime)

    def update_by_pass_shunt_event_with_options(self, request, runtime):
        """
        @summary 编辑旁路事件
        

        @param request: UpdateByPassShuntEventRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateByPassShuntEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.event_id):
            query['eventId'] = request.event_id
        if not UtilClient.is_unset(request.event_name):
            query['eventName'] = request.event_name
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateByPassShuntEvent',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.UpdateByPassShuntEventResponse(),
            self.call_api(params, req, runtime)
        )

    def update_by_pass_shunt_event(self, request):
        """
        @summary 编辑旁路事件
        

        @param request: UpdateByPassShuntEventRequest

        @return: UpdateByPassShuntEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_by_pass_shunt_event_with_options(request, runtime)

    def update_data_source_with_options(self, request, runtime):
        """
        @summary 修改数据源
        

        @param request: UpdateDataSourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.oss_key):
            query['ossKey'] = request.oss_key
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataSource',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.UpdateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_data_source(self, request):
        """
        @summary 修改数据源
        

        @param request: UpdateDataSourceRequest

        @return: UpdateDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_source_with_options(request, runtime)

    def update_query_variable_with_options(self, request, runtime):
        """
        @summary 自定义查询变量修改
        

        @param request: UpdateQueryVariableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateQueryVariableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.data_source_code):
            query['dataSourceCode'] = request.data_source_code
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.expression):
            query['expression'] = request.expression
        if not UtilClient.is_unset(request.expression_title):
            query['expressionTitle'] = request.expression_title
        if not UtilClient.is_unset(request.expression_variable):
            query['expressionVariable'] = request.expression_variable
        if not UtilClient.is_unset(request.id):
            query['id'] = request.id
        if not UtilClient.is_unset(request.outlier):
            query['outlier'] = request.outlier
        if not UtilClient.is_unset(request.outputs):
            query['outputs'] = request.outputs
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.title):
            query['title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateQueryVariable',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.UpdateQueryVariableResponse(),
            self.call_api(params, req, runtime)
        )

    def update_query_variable(self, request):
        """
        @summary 自定义查询变量修改
        

        @param request: UpdateQueryVariableRequest

        @return: UpdateQueryVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_query_variable_with_options(request, runtime)

    def update_rule_with_options(self, request, runtime):
        """
        @summary 更新策略
        

        @param request: UpdateRuleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.logic_expression):
            query['logicExpression'] = request.logic_expression
        if not UtilClient.is_unset(request.memo):
            query['memo'] = request.memo
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_actions):
            query['ruleActions'] = request.rule_actions
        if not UtilClient.is_unset(request.rule_expressions):
            query['ruleExpressions'] = request.rule_expressions
        if not UtilClient.is_unset(request.rule_id):
            query['ruleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_status):
            query['ruleStatus'] = request.rule_status
        if not UtilClient.is_unset(request.rule_version_id):
            query['ruleVersionId'] = request.rule_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRule',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.UpdateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_rule(self, request):
        """
        @summary 更新策略
        

        @param request: UpdateRuleRequest

        @return: UpdateRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_rule_with_options(request, runtime)

    def update_rule_base_with_options(self, request, runtime):
        """
        @summary 更新策略基础信息
        

        @param request: UpdateRuleBaseRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateRuleBaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.console_rule_id):
            query['consoleRuleId'] = request.console_rule_id
        if not UtilClient.is_unset(request.event_code):
            query['eventCode'] = request.event_code
        if not UtilClient.is_unset(request.memo):
            query['memo'] = request.memo
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.rule_id):
            query['ruleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['ruleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRuleBase',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.UpdateRuleBaseResponse(),
            self.call_api(params, req, runtime)
        )

    def update_rule_base(self, request):
        """
        @summary 更新策略基础信息
        

        @param request: UpdateRuleBaseRequest

        @return: UpdateRuleBaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_rule_base_with_options(request, runtime)

    def update_sample_batch_with_options(self, request, runtime):
        """
        @summary 批量修改样本
        

        @param request: UpdateSampleBatchRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateSampleBatchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.ids):
            query['ids'] = request.ids
        if not UtilClient.is_unset(request.reg_id):
            query['regId'] = request.reg_id
        if not UtilClient.is_unset(request.tags):
            query['tags'] = request.tags
        if not UtilClient.is_unset(request.versions):
            query['versions'] = request.versions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSampleBatch',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.UpdateSampleBatchResponse(),
            self.call_api(params, req, runtime)
        )

    def update_sample_batch(self, request):
        """
        @summary 批量修改样本
        

        @param request: UpdateSampleBatchRequest

        @return: UpdateSampleBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_sample_batch_with_options(request, runtime)

    def upload_sample_api_with_options(self, request, runtime):
        """
        @summary 单用户API创建样本
        

        @param request: UploadSampleApiRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UploadSampleApiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.data_value):
            query['DataValue'] = request.data_value
        if not UtilClient.is_unset(request.sample_type):
            query['SampleType'] = request.sample_type
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadSampleApi',
            version='2021-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            xtee_20210910_models.UploadSampleApiResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_sample_api(self, request):
        """
        @summary 单用户API创建样本
        

        @param request: UploadSampleApiRequest

        @return: UploadSampleApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_sample_api_with_options(request, runtime)
