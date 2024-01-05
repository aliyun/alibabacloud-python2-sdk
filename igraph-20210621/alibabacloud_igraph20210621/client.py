# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_igraph20210621 import models as igraph_20210621_models
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
        self._endpoint = self.get_endpoint('igraph', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_graph_with_options(self, instance_id, graph_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateGraph',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s/graphs/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(graph_name))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.CreateGraphResponse(),
            self.call_api(params, req, runtime)
        )

    def create_graph(self, instance_id, graph_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_graph_with_options(instance_id, graph_name, request, headers, runtime)

    def create_graph_schema_with_options(self, instance_id, graph_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateGraphSchema',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s/graphs/%s/schemas' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(graph_name))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.CreateGraphSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    def create_graph_schema(self, instance_id, graph_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_graph_schema_with_options(instance_id, graph_name, request, headers, runtime)

    def delete_graph_with_options(self, instance_id, graph_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGraph',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s/graphs/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(graph_name))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.DeleteGraphResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_graph(self, instance_id, graph_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_graph_with_options(instance_id, graph_name, request, headers, runtime)

    def get_graph_with_options(self, instance_id, graph_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGraph',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s/graphs/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(graph_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetGraphResponse(),
            self.call_api(params, req, runtime)
        )

    def get_graph(self, instance_id, graph_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_graph_with_options(instance_id, graph_name, request, headers, runtime)

    def get_graph_schema_with_options(self, instance_id, graph_name, graph_schema_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGraphSchema',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s/graphs/%s/schemas/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(graph_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(graph_schema_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetGraphSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    def get_graph_schema(self, instance_id, graph_name, graph_schema_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_graph_schema_with_options(instance_id, graph_name, graph_schema_name, request, headers, runtime)

    def get_igraph_label_back_flow_with_options(self, graph_name, instance_id, label_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIgraphLabelBackFlow',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s/graphs/%s/label/%s/backflow' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(graph_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(label_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetIgraphLabelBackFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def get_igraph_label_back_flow(self, graph_name, instance_id, label_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_igraph_label_back_flow_with_options(graph_name, instance_id, label_name, headers, runtime)

    def get_igraph_label_last_backflow_with_options(self, instance_id, graph_name, label_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIgraphLabelLastBackflow',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s/graphs/%s/label/%s/backflow/last' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(graph_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(label_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetIgraphLabelLastBackflowResponse(),
            self.call_api(params, req, runtime)
        )

    def get_igraph_label_last_backflow(self, instance_id, graph_name, label_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_igraph_label_last_backflow_with_options(instance_id, graph_name, label_name, headers, runtime)

    def get_igraph_table_detail_with_options(self, instance_id, graph_name, table_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIgraphTableDetail',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s/graphs/%s/tables/%s/detail' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(graph_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(table_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetIgraphTableDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_igraph_table_detail(self, instance_id, graph_name, table_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_igraph_table_detail_with_options(instance_id, graph_name, table_name, headers, runtime)

    def get_igraph_tables_back_flow_with_options(self, instance_id, graph_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIgraphTablesBackFlow',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s/graphs/%s/backflows' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(graph_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetIgraphTablesBackFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def get_igraph_tables_back_flow(self, instance_id, graph_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_igraph_tables_back_flow_with_options(instance_id, graph_name, request, headers, runtime)

    def get_instance_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, request, headers, runtime)

    def get_instance_digest_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceDigest',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s/digest' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetInstanceDigestResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_digest(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_digest_with_options(instance_id, request, headers, runtime)

    def get_table_detail_with_options(self, instance_id, table_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTableDetail',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s/tables/%s/detail' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(table_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetTableDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_table_detail(self, instance_id, table_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_detail_with_options(instance_id, table_name, headers, runtime)

    def get_table_last_backflow_with_options(self, instance_id, table_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.partition):
            query['partition'] = request.partition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableLastBackflow',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s/table/%s/backflow/last' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(table_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.GetTableLastBackflowResponse(),
            self.call_api(params, req, runtime)
        )

    def get_table_last_backflow(self, instance_id, table_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_last_backflow_with_options(instance_id, table_name, request, headers, runtime)

    def list_demo_graph_schemas_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDemoGraphSchemas',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/demo/schemas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.ListDemoGraphSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    def list_demo_graph_schemas(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_demo_graph_schemas_with_options(headers, runtime)

    def list_graph_schemas_with_options(self, instance_id, graph_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_limit):
            query['pageLimit'] = request.page_limit
        if not UtilClient.is_unset(request.page_start):
            query['pageStart'] = request.page_start
        if not UtilClient.is_unset(request.return_spec):
            query['returnSpec'] = request.return_spec
        if not UtilClient.is_unset(request.schema_status):
            query['schemaStatus'] = request.schema_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGraphSchemas',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s/graphs/%s/schemas' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(graph_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.ListGraphSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    def list_graph_schemas(self, instance_id, graph_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_graph_schemas_with_options(instance_id, graph_name, request, headers, runtime)

    def list_igraph_instances_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = igraph_20210621_models.ListIgraphInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_continue):
            query['pageContinue'] = request.page_continue
        if not UtilClient.is_unset(request.page_limit):
            query['pageLimit'] = request.page_limit
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIgraphInstances',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.ListIgraphInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_igraph_instances(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_igraph_instances_with_options(request, headers, runtime)

    def list_instance_graph_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceGraph',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s/graphs' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.ListInstanceGraphResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instance_graph(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_graph_with_options(instance_id, request, headers, runtime)

    def publish_graph_schema_with_options(self, instance_id, graph_name, graph_schema_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishGraphSchema',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s/graphs/%s/schemas/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(graph_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(graph_schema_name))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.PublishGraphSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_graph_schema(self, instance_id, graph_name, graph_schema_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_graph_schema_with_options(instance_id, graph_name, graph_schema_name, request, headers, runtime)

    def search_igraph_demo_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SearchIgraphDemo',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/tool/actions/search_demo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.SearchIgraphDemoResponse(),
            self.call_api(params, req, runtime)
        )

    def search_igraph_demo(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_igraph_demo_with_options(headers, runtime)

    def trigger_label_backflow_with_options(self, instance_id, graph_name, label_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.odps_partition):
            query['odpsPartition'] = request.odps_partition
        if not UtilClient.is_unset(request.timestamp):
            query['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerLabelBackflow',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s/graphs/%s/label/%s/backflow' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(graph_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(label_name))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.TriggerLabelBackflowResponse(),
            self.call_api(params, req, runtime)
        )

    def trigger_label_backflow(self, instance_id, graph_name, label_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.trigger_label_backflow_with_options(instance_id, graph_name, label_name, request, headers, runtime)

    def update_graph_description_with_options(self, instance_id, graph_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGraphDescription',
            version='2021-06-21',
            protocol='HTTPS',
            pathname='/openapi/igraph/instances/%s/graphs/%s/description' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(graph_name))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            igraph_20210621_models.UpdateGraphDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_graph_description(self, instance_id, graph_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_graph_description_with_options(instance_id, graph_name, request, headers, runtime)
