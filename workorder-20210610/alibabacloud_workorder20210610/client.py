# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_workorder20210610 import models as workorder_20210610_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'ap-northeast-1': 'workorder.ap-northeast-1.aliyuncs.com',
            'ap-southeast-1': 'workorder.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('workorder', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def close_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ticket_id):
            body['TicketId'] = request.ticket_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseTicket',
            version='2021-06-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            workorder_20210610_models.CloseTicketResponse(),
            self.call_api(params, req, runtime)
        )

    def close_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_ticket_with_options(request, runtime)

    def create_ticket_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = workorder_20210610_models.CreateTicketShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file_name_list):
            request.file_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file_name_list, 'FileNameList', 'simple')
        if not UtilClient.is_unset(tmp_req.secret_info):
            request.secret_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.secret_info), 'SecretInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.secret_info_shrink):
            query['SecretInfo'] = request.secret_info_shrink
        body = {}
        if not UtilClient.is_unset(request.category_id):
            body['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.file_name_list_shrink):
            body['FileNameList'] = request.file_name_list_shrink
        if not UtilClient.is_unset(request.severity):
            body['Severity'] = request.severity
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTicket',
            version='2021-06-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            workorder_20210610_models.CreateTicketResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ticket_with_options(request, runtime)

    def evaluate_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.score):
            body['Score'] = request.score
        if not UtilClient.is_unset(request.solved):
            body['Solved'] = request.solved
        if not UtilClient.is_unset(request.ticket_id):
            body['TicketId'] = request.ticket_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EvaluateTicket',
            version='2021-06-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            workorder_20210610_models.EvaluateTicketResponse(),
            self.call_api(params, req, runtime)
        )

    def evaluate_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.evaluate_ticket_with_options(request, runtime)

    def get_attachment_upload_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAttachmentUploadUrl',
            version='2021-06-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            workorder_20210610_models.GetAttachmentUploadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_attachment_upload_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_attachment_upload_url_with_options(request, runtime)

    def get_mq_consumer_tag_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetMqConsumerTag',
            version='2021-06-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            workorder_20210610_models.GetMqConsumerTagResponse(),
            self.call_api(params, req, runtime)
        )

    def get_mq_consumer_tag(self):
        runtime = util_models.RuntimeOptions()
        return self.get_mq_consumer_tag_with_options(runtime)

    def get_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ticket_id):
            body['TicketId'] = request.ticket_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTicket',
            version='2021-06-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            workorder_20210610_models.GetTicketResponse(),
            self.call_api(params, req, runtime)
        )

    def get_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ticket_with_options(request, runtime)

    def list_categories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCategories',
            version='2021-06-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            workorder_20210610_models.ListCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_categories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_categories_with_options(request, runtime)

    def list_products_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2021-06-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            workorder_20210610_models.ListProductsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_products(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_products_with_options(request, runtime)

    def list_ticket_notes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ticket_id):
            query['TicketId'] = request.ticket_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTicketNotes',
            version='2021-06-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            workorder_20210610_models.ListTicketNotesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ticket_notes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ticket_notes_with_options(request, runtime)

    def list_tickets_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = workorder_20210610_models.ListTicketsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ticket_id_list):
            request.ticket_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ticket_id_list, 'TicketIdList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.status_list):
            body['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.ticket_id):
            body['TicketId'] = request.ticket_id
        if not UtilClient.is_unset(request.ticket_id_list_shrink):
            body['TicketIdList'] = request.ticket_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTickets',
            version='2021-06-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            workorder_20210610_models.ListTicketsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tickets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tickets_with_options(request, runtime)

    def reopen_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.ticket_id):
            body['TicketId'] = request.ticket_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReopenTicket',
            version='2021-06-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            workorder_20210610_models.ReopenTicketResponse(),
            self.call_api(params, req, runtime)
        )

    def reopen_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reopen_ticket_with_options(request, runtime)

    def reply_ticket_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = workorder_20210610_models.ReplyTicketShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file_name_list):
            request.file_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file_name_list, 'FileNameList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.file_name_list_shrink):
            query['FileNameList'] = request.file_name_list_shrink
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.encrypt):
            body['Encrypt'] = request.encrypt
        if not UtilClient.is_unset(request.ticket_id):
            body['TicketId'] = request.ticket_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReplyTicket',
            version='2021-06-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            workorder_20210610_models.ReplyTicketResponse(),
            self.call_api(params, req, runtime)
        )

    def reply_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reply_ticket_with_options(request, runtime)
