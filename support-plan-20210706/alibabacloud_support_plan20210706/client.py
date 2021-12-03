# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_support_plan20210706 import models as support_plan_20210706_models
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
        self._endpoint = self.get_endpoint('support-plan', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def close_task_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OrderId'] = request.order_id
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CloseTaskOrder',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.CloseTaskOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def close_task_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_task_order_with_options(request, runtime)

    def create_task_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CustomerRealName'] = request.customer_real_name
        query['CustomerUserId'] = request.customer_user_id
        query['ImportantDescription'] = request.important_description
        query['IsImportant'] = request.is_important
        query['OpenGroupId'] = request.open_group_id
        query['ProductType'] = request.product_type
        query['ProductTypeName'] = request.product_type_name
        query['TaskTitle'] = request.task_title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTaskOrder',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.CreateTaskOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_task_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_task_order_with_options(request, runtime)

    def create_task_order_by_event_report_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = support_plan_20210706_models.CreateTaskOrderByEventReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.event_body):
            request.event_body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.event_body), 'EventBody', 'json')
        if not UtilClient.is_unset(tmp_req.extinfo):
            request.extinfo_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extinfo, 'Extinfo', 'json')
        query = {}
        query['Business'] = request.business
        query['CreateRealName'] = request.create_real_name
        query['CreateUserId'] = request.create_user_id
        query['EventBody'] = request.event_body_shrink
        query['Extinfo'] = request.extinfo_shrink
        query['ImportantDesc'] = request.important_desc
        query['JoinChildGroupUserIds'] = request.join_child_group_user_ids
        query['MonitorCongregation'] = request.monitor_congregation
        query['OpenGroupId'] = request.open_group_id
        query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTaskOrderByEventReport',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.CreateTaskOrderByEventReportResponse(),
            self.call_api(params, req, runtime)
        )

    def create_task_order_by_event_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_task_order_by_event_report_with_options(request, runtime)

    def delete_enterprise_dingtalk_group_customer_member_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.mobiles):
            request.mobiles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.mobiles, 'Mobiles', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteEnterpriseDingtalkGroupCustomerMember',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_enterprise_dingtalk_group_customer_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_enterprise_dingtalk_group_customer_member_with_options(request, runtime)

    def get_enterprise_dingtalk_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDingtalkGroup',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.GetEnterpriseDingtalkGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_enterprise_dingtalk_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_enterprise_dingtalk_group_with_options(request, runtime)

    def get_enterprise_dingtalk_group_customer_member_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDingtalkGroupCustomerMember',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def get_enterprise_dingtalk_group_customer_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_enterprise_dingtalk_group_customer_member_with_options(request, runtime)

    def list_dd_task_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['CallerParentId'] = request.caller_parent_id
        query['CallerType'] = request.caller_type
        query['CallerUid'] = request.caller_uid
        query['OpenGroupId'] = request.open_group_id
        query['OrderId'] = request.order_id
        query['RequestId'] = request.request_id
        query['TaskStatus'] = request.task_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDdTaskOrder',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.ListDdTaskOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dd_task_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dd_task_order_with_options(request, runtime)

    def list_enterprise_dingtalk_group_customer_members_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListEnterpriseDingtalkGroupCustomerMembers',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_enterprise_dingtalk_group_customer_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_enterprise_dingtalk_group_customer_members_with_options(request, runtime)

    def list_enterprise_dingtalk_groups_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListEnterpriseDingtalkGroups',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.ListEnterpriseDingtalkGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_enterprise_dingtalk_groups(self):
        runtime = util_models.RuntimeOptions()
        return self.list_enterprise_dingtalk_groups_with_options(runtime)

    def list_product_by_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OpenGroupId'] = request.open_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListProductByGroup',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.ListProductByGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_product_by_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_product_by_group_with_options(request, runtime)

    def query_task_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryTaskInfo',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.QueryTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_task_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_task_info_with_options(request, runtime)

    def reply_message_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['MsgContent'] = request.msg_content
        query['MsgType'] = request.msg_type
        query['OpenGroupId'] = request.open_group_id
        query['OrderId'] = request.order_id
        query['UserId'] = request.user_id
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReplyMessageApi',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.ReplyMessageApiResponse(),
            self.call_api(params, req, runtime)
        )

    def reply_message_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reply_message_api_with_options(request, runtime)

    def rest_open_task_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['OpenGroupId'] = request.open_group_id
        query['OrderId'] = request.order_id
        query['ResetContent'] = request.reset_content
        query['ResetType'] = request.reset_type
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestOpenTaskOrder',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.RestOpenTaskOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def rest_open_task_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rest_open_task_order_with_options(request, runtime)
