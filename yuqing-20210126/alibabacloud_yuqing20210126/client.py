# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_yuqing20210126 import models as yuqing_20210126_models
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
        self._endpoint = self.get_endpoint('yuqing', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def aggregate_search_yuqing(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.aggregate_search_yuqing_with_options(request, headers, runtime)

    def aggregate_search_yuqing_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        body = {}
        if not UtilClient.is_unset(request.aggregate_function):
            body['aggregateFunction'] = request.aggregate_function
        if not UtilClient.is_unset(request.group_by_key):
            body['groupByKey'] = request.group_by_key
        if not UtilClient.is_unset(request.group_limits):
            body['groupLimits'] = request.group_limits
        if not UtilClient.is_unset(request.search_condition):
            body['searchCondition'] = request.search_condition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AggregateSearchYuqing',
            version='2021-01-26',
            protocol='HTTPS',
            pathname='/openapi/aliyun/aggSearch.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20210126_models.AggregateSearchYuqingResponse(),
            self.call_api(params, req, runtime)
        )

    def create_project(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    def create_project_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        body = {}
        if not UtilClient.is_unset(request.create_user_id):
            body['createUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.create_user_name):
            body['createUserName'] = request.create_user_name
        if not UtilClient.is_unset(request.project):
            body['project'] = request.project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2021-01-26',
            protocol='HTTPS',
            pathname='/openapi/aliyun/createProject.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20210126_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_project(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(request, headers, runtime)

    def delete_project_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        body = {}
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.modified_user_id):
            body['modifiedUserId'] = request.modified_user_id
        if not UtilClient.is_unset(request.modified_user_name):
            body['modifiedUserName'] = request.modified_user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2021-01-26',
            protocol='HTTPS',
            pathname='/openapi/aliyun/deleteProject.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20210126_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def get_analysis_component_result(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_analysis_component_result_with_options(request, headers, runtime)

    def get_analysis_component_result_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_id):
            query['analysisId'] = request.analysis_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAnalysisComponentResult',
            version='2021-01-26',
            protocol='HTTPS',
            pathname='/openapi/aliyun/getAnalysisComponentResult.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20210126_models.GetAnalysisComponentResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_message_detail(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_message_detail_with_options(request, headers, runtime)

    def get_message_detail_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.doc_id):
            query['docId'] = request.doc_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMessageDetail',
            version='2021-01-26',
            protocol='HTTPS',
            pathname='/openapi/aliyun/getMessageFromHbase.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20210126_models.GetMessageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hotspot_message(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_hotspot_message_with_options(request, headers, runtime)

    def list_hotspot_message_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        body = {}
        if not UtilClient.is_unset(request.hotspot_search_condition):
            body['hotspotSearchCondition'] = request.hotspot_search_condition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListHotspotMessage',
            version='2021-01-26',
            protocol='HTTPS',
            pathname='/openapi/aliyun/searchHotspotDetail.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20210126_models.ListHotspotMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def list_yuqing_messages(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_yuqing_messages_with_options(request, headers, runtime)

    def list_yuqing_messages_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        body = {}
        if not UtilClient.is_unset(request.search_condition):
            body['searchCondition'] = request.search_condition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListYuqingMessages',
            version='2021-01-26',
            protocol='HTTPS',
            pathname='/openapi/aliyun/searchMessages.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20210126_models.ListYuqingMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_alarm_data_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_alarm_data_list_with_options(request, headers, runtime)

    def query_alarm_data_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_query):
            query['alarmQuery'] = request.alarm_query
        if not UtilClient.is_unset(request.order_by_key):
            query['orderByKey'] = request.order_by_key
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAlarmDataList',
            version='2021-01-26',
            protocol='HTTPS',
            pathname='/openapi/aliyun/queryAlarmDataList.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20210126_models.QueryAlarmDataListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_analysis_component(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_analysis_component_with_options(request, headers, runtime)

    def query_analysis_component_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        body = {}
        if not UtilClient.is_unset(request.analyse_type):
            body['analyseType'] = request.analyse_type
        if not UtilClient.is_unset(request.search_condition):
            body['searchCondition'] = request.search_condition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAnalysisComponent',
            version='2021-01-26',
            protocol='HTTPS',
            pathname='/openapi/aliyun/queryAnalysisComponent.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20210126_models.QueryAnalysisComponentResponse(),
            self.call_api(params, req, runtime)
        )

    def query_filter_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_filter_list_with_options(request, headers, runtime)

    def query_filter_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_id):
            query['filterId'] = request.filter_id
        if not UtilClient.is_unset(request.page_now):
            query['pageNow'] = request.page_now
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFilterList',
            version='2021-01-26',
            protocol='HTTPS',
            pathname='/openapi/aliyun/queryFilterList.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20210126_models.QueryFilterListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_project_list(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_project_list_with_options(request, headers, runtime)

    def query_project_list_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_now):
            query['pageNow'] = request.page_now
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_group_id):
            query['projectGroupId'] = request.project_group_id
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProjectList',
            version='2021-01-26',
            protocol='HTTPS',
            pathname='/openapi/aliyun/queryProjectList.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20210126_models.QueryProjectListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_report_notifies(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_report_notifies_with_options(request, headers, runtime)

    def query_report_notifies_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cp_id):
            query['cpId'] = request.cp_id
        if not UtilClient.is_unset(request.create_end_timestamp):
            query['createEndTimestamp'] = request.create_end_timestamp
        if not UtilClient.is_unset(request.create_start_timestamp):
            query['createStartTimestamp'] = request.create_start_timestamp
        if not UtilClient.is_unset(request.page_now):
            query['pageNow'] = request.page_now
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.subject):
            query['subject'] = request.subject
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryReportNotifies',
            version='2021-01-26',
            protocol='HTTPS',
            pathname='/openapi/aliyun/queryReportNotifies.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20210126_models.QueryReportNotifiesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_tag_nodes(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_tag_nodes_with_options(request, headers, runtime)

    def query_tag_nodes_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTagNodes',
            version='2021-01-26',
            protocol='HTTPS',
            pathname='/openapi/aliyun/queryTagNodes.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20210126_models.QueryTagNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def update_project(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_with_options(request, headers, runtime)

    def update_project_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        body = {}
        if not UtilClient.is_unset(request.is_info):
            body['isInfo'] = request.is_info
        if not UtilClient.is_unset(request.project):
            body['project'] = request.project
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.update_user_id):
            body['updateUserId'] = request.update_user_id
        if not UtilClient.is_unset(request.update_user_name):
            body['updateUserName'] = request.update_user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2021-01-26',
            protocol='HTTPS',
            pathname='/openapi/aliyun/updateProject.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20210126_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def update_propagation(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_propagation_with_options(request, headers, runtime)

    def update_propagation_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        body = {}
        if not UtilClient.is_unset(request.weibo_urls):
            body['weiboUrls'] = request.weibo_urls
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePropagation',
            version='2021-01-26',
            protocol='HTTPS',
            pathname='/openapi/aliyun/updatePropagation.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20210126_models.UpdatePropagationResponse(),
            self.call_api(params, req, runtime)
        )
