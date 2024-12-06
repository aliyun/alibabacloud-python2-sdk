# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_elasticsearch20170613 import models as elasticsearch_20170613_models
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
        self._endpoint = self.get_endpoint('elasticsearch', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def activate_zones_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Restores nodes in disabled zones. This operation is available only for multi-zone Elasticsearch clusters.
        

        @param request: ActivateZonesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ActivateZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='ActivateZones',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/recover-zones' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ActivateZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def activate_zones(self, instance_id, request):
        """
        @summary Restores nodes in disabled zones. This operation is available only for multi-zone Elasticsearch clusters.
        

        @param request: ActivateZonesRequest

        @return: ActivateZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.activate_zones_with_options(instance_id, request, headers, runtime)

    def add_connectable_cluster_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: AddConnectableClusterRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddConnectableClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='AddConnectableCluster',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/connected-clusters' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.AddConnectableClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def add_connectable_cluster(self, instance_id, request):
        """

        @param request: AddConnectableClusterRequest

        @return: AddConnectableClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_connectable_cluster_with_options(instance_id, request, headers, runtime)

    def add_snapshot_repo_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Call the AddSnapshotRepo to create a reference repository when configuring a cross-cluster OSS repository.
        

        @param request: AddSnapshotRepoRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddSnapshotRepoResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='AddSnapshotRepo',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/snapshot-repos' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.AddSnapshotRepoResponse(),
            self.call_api(params, req, runtime)
        )

    def add_snapshot_repo(self, instance_id, request):
        """
        @summary Call the AddSnapshotRepo to create a reference repository when configuring a cross-cluster OSS repository.
        

        @param request: AddSnapshotRepoRequest

        @return: AddSnapshotRepoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_snapshot_repo_with_options(instance_id, request, headers, runtime)

    def cancel_deletion_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Restores an Elasticsearch cluster that is frozen after it is released.
        

        @param request: CancelDeletionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelDeletionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDeletion',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/cancel-deletion' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CancelDeletionResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_deletion(self, instance_id, request):
        """
        @summary Restores an Elasticsearch cluster that is frozen after it is released.
        

        @param request: CancelDeletionRequest

        @return: CancelDeletionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_deletion_with_options(instance_id, request, headers, runtime)

    def cancel_logstash_deletion_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Restores a Logstash cluster that is frozen after it is released.
        

        @param request: CancelLogstashDeletionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelLogstashDeletionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelLogstashDeletion',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/actions/cancel-deletion' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CancelLogstashDeletionResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_logstash_deletion(self, instance_id, request):
        """
        @summary Restores a Logstash cluster that is frozen after it is released.
        

        @param request: CancelLogstashDeletionRequest

        @return: CancelLogstashDeletionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_logstash_deletion_with_options(instance_id, request, headers, runtime)

    def cancel_task_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: CancelTaskRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/cancel-task' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_task(self, instance_id, request):
        """

        @param request: CancelTaskRequest

        @return: CancelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_task_with_options(instance_id, request, headers, runtime)

    def capacity_plan_with_options(self, request, headers, runtime):
        """
        @summary Capacity Planning
        

        @param request: CapacityPlanRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CapacityPlanResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.complex_query_available):
            body['complexQueryAvailable'] = request.complex_query_available
        if not UtilClient.is_unset(request.data_info):
            body['dataInfo'] = request.data_info
        if not UtilClient.is_unset(request.metric):
            body['metric'] = request.metric
        if not UtilClient.is_unset(request.usage_scenario):
            body['usageScenario'] = request.usage_scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CapacityPlan',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/assist/actions/capacity-plan',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CapacityPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def capacity_plan(self, request):
        """
        @summary Capacity Planning
        

        @param request: CapacityPlanRequest

        @return: CapacityPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.capacity_plan_with_options(request, headers, runtime)

    def close_diagnosis_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 关闭实例的智能运维功能
        

        @param request: CloseDiagnosisRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CloseDiagnosisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseDiagnosis',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/diagnosis/instances/%s/actions/close-diagnosis' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CloseDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    def close_diagnosis(self, instance_id, request):
        """
        @summary 关闭实例的智能运维功能
        

        @param request: CloseDiagnosisRequest

        @return: CloseDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.close_diagnosis_with_options(instance_id, request, headers, runtime)

    def close_https_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: CloseHttpsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CloseHttpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseHttps',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/close-https' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CloseHttpsResponse(),
            self.call_api(params, req, runtime)
        )

    def close_https(self, instance_id, request):
        """

        @param request: CloseHttpsRequest

        @return: CloseHttpsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.close_https_with_options(instance_id, request, headers, runtime)

    def close_managed_index_with_options(self, instance_id, index, request, headers, runtime):
        """
        @summary Disable Managed Index
        

        @param request: CloseManagedIndexRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CloseManagedIndexResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseManagedIndex',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/indices/%s/close-managed' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(index))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CloseManagedIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def close_managed_index(self, instance_id, index, request):
        """
        @summary Disable Managed Index
        

        @param request: CloseManagedIndexRequest

        @return: CloseManagedIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.close_managed_index_with_options(instance_id, index, request, headers, runtime)

    def create_collector_with_options(self, request, headers, runtime):
        """
        @summary 创建收集器
        

        @param request: CreateCollectorRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCollectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.collector_paths):
            body['collectorPaths'] = request.collector_paths
        if not UtilClient.is_unset(request.configs):
            body['configs'] = request.configs
        if not UtilClient.is_unset(request.dry_run):
            body['dryRun'] = request.dry_run
        if not UtilClient.is_unset(request.extend_configs):
            body['extendConfigs'] = request.extend_configs
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.res_type):
            body['resType'] = request.res_type
        if not UtilClient.is_unset(request.res_version):
            body['resVersion'] = request.res_version
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCollector',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/collectors',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    def create_collector(self, request):
        """
        @summary 创建收集器
        

        @param request: CreateCollectorRequest

        @return: CreateCollectorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_collector_with_options(request, headers, runtime)

    def create_component_index_with_options(self, instance_id, name, request, headers, runtime):
        """
        @summary 创建Elasticsearch组合模板
        

        @param request: CreateComponentIndexRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateComponentIndexResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.meta):
            body['_meta'] = request.meta
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateComponentIndex',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/component-index/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateComponentIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def create_component_index(self, instance_id, name, request):
        """
        @summary 创建Elasticsearch组合模板
        

        @param request: CreateComponentIndexRequest

        @return: CreateComponentIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_component_index_with_options(instance_id, name, request, headers, runtime)

    def create_data_stream_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 创建数据流
        

        @param request: CreateDataStreamRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateDataStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateDataStream',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/data-streams' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateDataStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_stream(self, instance_id, request):
        """
        @summary 创建数据流
        

        @param request: CreateDataStreamRequest

        @return: CreateDataStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_data_stream_with_options(instance_id, request, headers, runtime)

    def create_ilmpolicy_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 创建索引生命周期策略
        

        @param request: CreateILMPolicyRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateILMPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateILMPolicy',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/ilm-policies' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateILMPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ilmpolicy(self, instance_id, request):
        """
        @summary 创建索引生命周期策略
        

        @param request: CreateILMPolicyRequest

        @return: CreateILMPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ilmpolicy_with_options(instance_id, request, headers, runtime)

    def create_index_template_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 创建索引模版
        

        @param request: CreateIndexTemplateRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateIndexTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.data_stream):
            body['dataStream'] = request.data_stream
        if not UtilClient.is_unset(request.ilm_policy):
            body['ilmPolicy'] = request.ilm_policy
        if not UtilClient.is_unset(request.index_patterns):
            body['indexPatterns'] = request.index_patterns
        if not UtilClient.is_unset(request.index_template):
            body['indexTemplate'] = request.index_template
        if not UtilClient.is_unset(request.priority):
            body['priority'] = request.priority
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIndexTemplate',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/index-templates' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateIndexTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_index_template(self, instance_id, request):
        """
        @summary 创建索引模版
        

        @param request: CreateIndexTemplateRequest

        @return: CreateIndexTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_index_template_with_options(instance_id, request, headers, runtime)

    def create_logstash_with_options(self, request, headers, runtime):
        """
        @summary 创建logstash实例
        

        @param request: CreateLogstashRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateLogstashResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.network_config):
            body['networkConfig'] = request.network_config
        if not UtilClient.is_unset(request.node_amount):
            body['nodeAmount'] = request.node_amount
        if not UtilClient.is_unset(request.node_spec):
            body['nodeSpec'] = request.node_spec
        if not UtilClient.is_unset(request.payment_info):
            body['paymentInfo'] = request.payment_info
        if not UtilClient.is_unset(request.payment_type):
            body['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogstash',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateLogstashResponse(),
            self.call_api(params, req, runtime)
        )

    def create_logstash(self, request):
        """
        @summary 创建logstash实例
        

        @param request: CreateLogstashRequest

        @return: CreateLogstashResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_logstash_with_options(request, headers, runtime)

    def create_pipelines_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 创建Logstash管道任务
        

        @param request: CreatePipelinesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreatePipelinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='CreatePipelines',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/pipelines' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreatePipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_pipelines(self, instance_id, request):
        """
        @summary 创建Logstash管道任务
        

        @param request: CreatePipelinesRequest

        @return: CreatePipelinesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipelines_with_options(instance_id, request, headers, runtime)

    def create_snapshot_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: CreateSnapshotRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/snapshots' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def create_snapshot(self, instance_id, request):
        """

        @param request: CreateSnapshotRequest

        @return: CreateSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_snapshot_with_options(instance_id, request, headers, runtime)

    def create_vpc_endpoint_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 创建私网链接VPC终端节点
        
        @description 5FFD9ED4-C2EC-4E89-B22B-1ACB6FE1D\\\\*\\*\
        

        @param request: CreateVpcEndpointRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateVpcEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.service_id):
            body['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.zone_id):
            body['zoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVpcEndpoint',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/vpc-endpoints' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def create_vpc_endpoint(self, instance_id, request):
        """
        @summary 创建私网链接VPC终端节点
        
        @description 5FFD9ED4-C2EC-4E89-B22B-1ACB6FE1D\\\\*\\*\
        

        @param request: CreateVpcEndpointRequest

        @return: CreateVpcEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_vpc_endpoint_with_options(instance_id, request, headers, runtime)

    def deactivate_zones_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Invoke DeactivateZones to offline certain zones when there are multiple availability zones, and migrate nodes in the offline zones to other availability zones.
        

        @param request: DeactivateZonesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeactivateZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='DeactivateZones',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/down-zones' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeactivateZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def deactivate_zones(self, instance_id, request):
        """
        @summary Invoke DeactivateZones to offline certain zones when there are multiple availability zones, and migrate nodes in the offline zones to other availability zones.
        

        @param request: DeactivateZonesRequest

        @return: DeactivateZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deactivate_zones_with_options(instance_id, request, headers, runtime)

    def delete_collector_with_options(self, res_id, request, headers, runtime):
        """
        @summary Deletes a shipper.
        

        @param request: DeleteCollectorRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCollectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCollector',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/collectors/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(res_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_collector(self, res_id, request):
        """
        @summary Deletes a shipper.
        

        @param request: DeleteCollectorRequest

        @return: DeleteCollectorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_collector_with_options(res_id, request, headers, runtime)

    def delete_component_index_with_options(self, instance_id, name, headers, runtime):
        """
        @summary 删除组合索引模板
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteComponentIndexResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteComponentIndex',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/component-index/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteComponentIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_component_index(self, instance_id, name):
        """
        @summary 删除组合索引模板
        

        @return: DeleteComponentIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_component_index_with_options(instance_id, name, headers, runtime)

    def delete_connected_cluster_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: DeleteConnectedClusterRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteConnectedClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.connected_instance_id):
            query['connectedInstanceId'] = request.connected_instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConnectedCluster',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/connected-clusters' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteConnectedClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_connected_cluster(self, instance_id, request):
        """

        @param request: DeleteConnectedClusterRequest

        @return: DeleteConnectedClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_connected_cluster_with_options(instance_id, request, headers, runtime)

    def delete_data_stream_with_options(self, instance_id, data_stream, request, headers, runtime):
        """
        @summary 删除数据流
        

        @param request: DeleteDataStreamRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDataStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataStream',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/data-streams/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(data_stream))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteDataStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_stream(self, instance_id, data_stream, request):
        """
        @summary 删除数据流
        

        @param request: DeleteDataStreamRequest

        @return: DeleteDataStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_data_stream_with_options(instance_id, data_stream, request, headers, runtime)

    def delete_data_task_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: DeleteDataTaskRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDataTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataTask',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/data-task' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteDataTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_task(self, instance_id, request):
        """

        @param request: DeleteDataTaskRequest

        @return: DeleteDataTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_data_task_with_options(instance_id, request, headers, runtime)

    def delete_deprecated_template_with_options(self, instance_id, name, headers, runtime):
        """
        @summary 删除历史索引模板
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDeprecatedTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDeprecatedTemplate',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/deprecated-templates/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteDeprecatedTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_deprecated_template(self, instance_id, name):
        """
        @summary 删除历史索引模板
        

        @return: DeleteDeprecatedTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_deprecated_template_with_options(instance_id, name, headers, runtime)

    def delete_ilmpolicy_with_options(self, instance_id, policy_name, headers, runtime):
        """

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteILMPolicyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteILMPolicy',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/ilm-policies/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(policy_name))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteILMPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_ilmpolicy(self, instance_id, policy_name):
        """

        @return: DeleteILMPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ilmpolicy_with_options(instance_id, policy_name, headers, runtime)

    def delete_index_template_with_options(self, instance_id, index_template, headers, runtime):
        """
        @summary 删除ES集群索引模版
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteIndexTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteIndexTemplate',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/index-templates/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(index_template))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteIndexTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_index_template(self, instance_id, index_template):
        """
        @summary 删除ES集群索引模版
        

        @return: DeleteIndexTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_index_template_with_options(instance_id, index_template, headers, runtime)

    def delete_instance_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: DeleteInstanceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.delete_type):
            query['deleteType'] = request.delete_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance(self, instance_id, request):
        """

        @param request: DeleteInstanceRequest

        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, request, headers, runtime)

    def delete_logstash_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Releases a Logstash cluster.
        
        @description Before you call this operation, take note of the following information: After the cluster is released, the physical resources used by the cluster are reclaimed. The data stored in the cluster is deleted and cannot be recovered. The disks attached to the nodes in the cluster and the snapshots created for the cluster are released.
        

        @param request: DeleteLogstashRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteLogstashResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.delete_type):
            query['deleteType'] = request.delete_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLogstash',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteLogstashResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_logstash(self, instance_id, request):
        """
        @summary Releases a Logstash cluster.
        
        @description Before you call this operation, take note of the following information: After the cluster is released, the physical resources used by the cluster are reclaimed. The data stored in the cluster is deleted and cannot be recovered. The disks attached to the nodes in the cluster and the snapshots created for the cluster are released.
        

        @param request: DeleteLogstashRequest

        @return: DeleteLogstashResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_logstash_with_options(instance_id, request, headers, runtime)

    def delete_pipelines_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Deletes a pipeline that is configured for a Logstash cluster.
        

        @param request: DeletePipelinesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeletePipelinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.pipeline_ids):
            query['pipelineIds'] = request.pipeline_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePipelines',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/pipelines' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeletePipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_pipelines(self, instance_id, request):
        """
        @summary Deletes a pipeline that is configured for a Logstash cluster.
        

        @param request: DeletePipelinesRequest

        @return: DeletePipelinesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipelines_with_options(instance_id, request, headers, runtime)

    def delete_snapshot_repo_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: DeleteSnapshotRepoRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteSnapshotRepoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.repo_path):
            query['repoPath'] = request.repo_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshotRepo',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/snapshot-repos' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteSnapshotRepoResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_snapshot_repo(self, instance_id, request):
        """

        @param request: DeleteSnapshotRepoRequest

        @return: DeleteSnapshotRepoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_snapshot_repo_with_options(instance_id, request, headers, runtime)

    def delete_vpc_endpoint_with_options(self, instance_id, endpoint_id, request, headers, runtime):
        """
        @summary 删除服务账号vpc下的终端节点
        

        @param request: DeleteVpcEndpointRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteVpcEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVpcEndpoint',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/vpc-endpoints/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(endpoint_id))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vpc_endpoint(self, instance_id, endpoint_id, request):
        """
        @summary 删除服务账号vpc下的终端节点
        

        @param request: DeleteVpcEndpointRequest

        @return: DeleteVpcEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_vpc_endpoint_with_options(instance_id, endpoint_id, request, headers, runtime)

    def describe_ack_operator_with_options(self, cluster_id, headers, runtime):
        """
        @summary Queries the information of ES-operator that is installed for a specified Container Service for Kubernetes (ACK) cluster.
        
        @description > Before you install a shipper on an ACK cluster, you can call this operation to query the installation status of ES-operator for the ACK cluster.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAckOperatorResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeAckOperator',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/ack-clusters/%s/operator' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeAckOperatorResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ack_operator(self, cluster_id):
        """
        @summary Queries the information of ES-operator that is installed for a specified Container Service for Kubernetes (ACK) cluster.
        
        @description > Before you install a shipper on an ACK cluster, you can call this operation to query the installation status of ES-operator for the ACK cluster.
        

        @return: DescribeAckOperatorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_ack_operator_with_options(cluster_id, headers, runtime)

    def describe_apm_with_options(self, instance_id, headers, runtime):
        """
        @summary Describe APM
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeApmResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeApm',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/apm/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeApmResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apm(self, instance_id):
        """
        @summary Describe APM
        

        @return: DescribeApmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_apm_with_options(instance_id, headers, runtime)

    def describe_collector_with_options(self, res_id, headers, runtime):
        """
        @summary Queries the details of a shipper.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCollectorResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeCollector',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/collectors/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(res_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_collector(self, res_id):
        """
        @summary Queries the details of a shipper.
        

        @return: DescribeCollectorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_collector_with_options(res_id, headers, runtime)

    def describe_component_index_with_options(self, instance_id, name, headers, runtime):
        """
        @summary 查看组合索引模板详情
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeComponentIndexResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeComponentIndex',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/component-index/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeComponentIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_component_index(self, instance_id, name):
        """
        @summary 查看组合索引模板详情
        

        @return: DescribeComponentIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_component_index_with_options(instance_id, name, headers, runtime)

    def describe_connectable_clusters_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: DescribeConnectableClustersRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeConnectableClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.already_set_items):
            query['alreadySetItems'] = request.already_set_items
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConnectableClusters',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/connectable-clusters' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeConnectableClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_connectable_clusters(self, instance_id, request):
        """

        @param request: DescribeConnectableClustersRequest

        @return: DescribeConnectableClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_connectable_clusters_with_options(instance_id, request, headers, runtime)

    def describe_deprecated_template_with_options(self, instance_id, name, headers, runtime):
        """
        @summary DescribeDeprecatedTemplate
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDeprecatedTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDeprecatedTemplate',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/deprecated-templates/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeDeprecatedTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_deprecated_template(self, instance_id, name):
        """
        @summary DescribeDeprecatedTemplate
        

        @return: DescribeDeprecatedTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_deprecated_template_with_options(instance_id, name, headers, runtime)

    def describe_diagnose_report_with_options(self, instance_id, report_id, request, headers, runtime):
        """

        @param request: DescribeDiagnoseReportRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDiagnoseReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnoseReport',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/diagnosis/instances/%s/reports/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(report_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeDiagnoseReportResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_diagnose_report(self, instance_id, report_id, request):
        """

        @param request: DescribeDiagnoseReportRequest

        @return: DescribeDiagnoseReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_diagnose_report_with_options(instance_id, report_id, request, headers, runtime)

    def describe_diagnosis_settings_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: DescribeDiagnosisSettingsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDiagnosisSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisSettings',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/diagnosis/instances/%s/settings' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeDiagnosisSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_diagnosis_settings(self, instance_id, request):
        """

        @param request: DescribeDiagnosisSettingsRequest

        @return: DescribeDiagnosisSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_diagnosis_settings_with_options(instance_id, request, headers, runtime)

    def describe_dynamic_settings_with_options(self, instance_id, headers, runtime):
        """
        @summary 获取集群动态指标
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeDynamicSettingsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDynamicSettings',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/dynamic-settings' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeDynamicSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dynamic_settings(self, instance_id):
        """
        @summary 获取集群动态指标
        

        @return: DescribeDynamicSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_dynamic_settings_with_options(instance_id, headers, runtime)

    def describe_elasticsearch_health_with_options(self, instance_id, headers, runtime):
        """
        @summary Queries the health status of an Elasticsearch cluster.
        
        @description An Elasticsearch cluster can be in a health state indicated by one of the following colors:
        GREEN: Primary shards and replica shards for the primary shards are normally allocated.
        YELLOW: Primary shards are normally allocated, but replica shards for the primary shards are not normally allocated.
        RED: Primary shards are not normally allocated.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeElasticsearchHealthResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeElasticsearchHealth',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/elasticsearch-health' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeElasticsearchHealthResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_elasticsearch_health(self, instance_id):
        """
        @summary Queries the health status of an Elasticsearch cluster.
        
        @description An Elasticsearch cluster can be in a health state indicated by one of the following colors:
        GREEN: Primary shards and replica shards for the primary shards are normally allocated.
        YELLOW: Primary shards are normally allocated, but replica shards for the primary shards are not normally allocated.
        RED: Primary shards are not normally allocated.
        

        @return: DescribeElasticsearchHealthResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_elasticsearch_health_with_options(instance_id, headers, runtime)

    def describe_ilmpolicy_with_options(self, instance_id, policy_name, headers, runtime):
        """

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeILMPolicyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeILMPolicy',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/ilm-policies/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(policy_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeILMPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ilmpolicy(self, instance_id, policy_name):
        """

        @return: DescribeILMPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_ilmpolicy_with_options(instance_id, policy_name, headers, runtime)

    def describe_index_template_with_options(self, instance_id, index_template, headers, runtime):
        """

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeIndexTemplateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeIndexTemplate',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/index-templates/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(index_template))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeIndexTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_index_template(self, instance_id, index_template):
        """

        @return: DescribeIndexTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_index_template_with_options(instance_id, index_template, headers, runtime)

    def describe_instance_with_options(self, instance_id, headers, runtime):
        """
        @summary The name of the dictionary file.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance(self, instance_id):
        """
        @summary The name of the dictionary file.
        

        @return: DescribeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instance_with_options(instance_id, headers, runtime)

    def describe_kibana_settings_with_options(self, instance_id, headers, runtime):
        """
        @summary 获取Elasticsearch集群Kibana节点settings配置
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeKibanaSettingsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeKibanaSettings',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/kibana-settings' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeKibanaSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_kibana_settings(self, instance_id):
        """
        @summary 获取Elasticsearch集群Kibana节点settings配置
        

        @return: DescribeKibanaSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_kibana_settings_with_options(instance_id, headers, runtime)

    def describe_logstash_with_options(self, instance_id, headers, runtime):
        """
        @summary 查看Logstash实例详情
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeLogstashResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeLogstash',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeLogstashResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_logstash(self, instance_id):
        """
        @summary 查看Logstash实例详情
        

        @return: DescribeLogstashResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_logstash_with_options(instance_id, headers, runtime)

    def describe_pipeline_with_options(self, instance_id, pipeline_id, headers, runtime):
        """

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribePipelineResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribePipeline',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/pipelines/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(pipeline_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pipeline(self, instance_id, pipeline_id):
        """

        @return: DescribePipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_pipeline_with_options(instance_id, pipeline_id, headers, runtime)

    def describe_pipeline_management_config_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Queries the management configurations of pipelines in a Logstash cluster.
        

        @param request: DescribePipelineManagementConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribePipelineManagementConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePipelineManagementConfig',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/pipeline-management-config' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribePipelineManagementConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pipeline_management_config(self, instance_id, request):
        """
        @summary Queries the management configurations of pipelines in a Logstash cluster.
        

        @param request: DescribePipelineManagementConfigRequest

        @return: DescribePipelineManagementConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_pipeline_management_config_with_options(instance_id, request, headers, runtime)

    def describe_regions_with_options(self, headers, runtime):
        """

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeRegionsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self):
        """

        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    def describe_snapshot_setting_with_options(self, instance_id, headers, runtime):
        """

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeSnapshotSettingResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSnapshotSetting',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/snapshot-setting' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeSnapshotSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_snapshot_setting(self, instance_id):
        """

        @return: DescribeSnapshotSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_snapshot_setting_with_options(instance_id, headers, runtime)

    def describe_templates_with_options(self, instance_id, headers, runtime):
        """

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTemplatesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeTemplates',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/templates' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_templates(self, instance_id):
        """

        @return: DescribeTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_templates_with_options(instance_id, headers, runtime)

    def describe_xpack_monitor_config_with_options(self, instance_id, headers, runtime):
        """
        @summary Queries the configurations of the X-Pack Monitoring feature of a Logstash cluster.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeXpackMonitorConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeXpackMonitorConfig',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/xpack-monitor-config' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeXpackMonitorConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_xpack_monitor_config(self, instance_id):
        """
        @summary Queries the configurations of the X-Pack Monitoring feature of a Logstash cluster.
        

        @return: DescribeXpackMonitorConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_xpack_monitor_config_with_options(instance_id, headers, runtime)

    def diagnose_instance_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 触发ES实例智能诊断
        

        @param request: DiagnoseInstanceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DiagnoseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        body = {}
        if not UtilClient.is_unset(request.diagnose_items):
            body['diagnoseItems'] = request.diagnose_items
        if not UtilClient.is_unset(request.indices):
            body['indices'] = request.indices
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DiagnoseInstance',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/diagnosis/instances/%s/actions/diagnose' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DiagnoseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def diagnose_instance(self, instance_id, request):
        """
        @summary 触发ES实例智能诊断
        

        @param request: DiagnoseInstanceRequest

        @return: DiagnoseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.diagnose_instance_with_options(instance_id, request, headers, runtime)

    def disable_kibana_pvl_network_with_options(self, instance_id, headers, runtime):
        """
        @summary 关闭kibana私网
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DisableKibanaPvlNetworkResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DisableKibanaPvlNetwork',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/disable-kibana-private' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DisableKibanaPvlNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_kibana_pvl_network(self, instance_id):
        """
        @summary 关闭kibana私网
        

        @return: DisableKibanaPvlNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_kibana_pvl_network_with_options(instance_id, headers, runtime)

    def enable_kibana_pvl_network_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 开启v3 kibana私网
        

        @param request: EnableKibanaPvlNetworkRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: EnableKibanaPvlNetworkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.endpoint_name):
            body['endpointName'] = request.endpoint_name
        if not UtilClient.is_unset(request.security_groups):
            body['securityGroups'] = request.security_groups
        if not UtilClient.is_unset(request.v_switch_ids_zone):
            body['vSwitchIdsZone'] = request.v_switch_ids_zone
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableKibanaPvlNetwork',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/enable-kibana-private' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.EnableKibanaPvlNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_kibana_pvl_network(self, instance_id, request):
        """
        @summary 开启v3 kibana私网
        

        @param request: EnableKibanaPvlNetworkRequest

        @return: EnableKibanaPvlNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_kibana_pvl_network_with_options(instance_id, request, headers, runtime)

    def estimated_logstash_restart_time_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Queries the estimated time that is required to restart a Logstash cluster.
        

        @param request: EstimatedLogstashRestartTimeRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: EstimatedLogstashRestartTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='EstimatedLogstashRestartTime',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/estimated-time/restart-time' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.EstimatedLogstashRestartTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def estimated_logstash_restart_time(self, instance_id, request):
        """
        @summary Queries the estimated time that is required to restart a Logstash cluster.
        

        @param request: EstimatedLogstashRestartTimeRequest

        @return: EstimatedLogstashRestartTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.estimated_logstash_restart_time_with_options(instance_id, request, headers, runtime)

    def estimated_restart_time_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Queries the estimated time that is required to restart an Elasticsearch cluster.
        

        @param request: EstimatedRestartTimeRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: EstimatedRestartTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='EstimatedRestartTime',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/estimated-time/restart-time' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.EstimatedRestartTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def estimated_restart_time(self, instance_id, request):
        """
        @summary Queries the estimated time that is required to restart an Elasticsearch cluster.
        

        @param request: EstimatedRestartTimeRequest

        @return: EstimatedRestartTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.estimated_restart_time_with_options(instance_id, request, headers, runtime)

    def get_cluster_data_information_with_options(self, request, headers, runtime):
        """
        @summary Call GetClusterDataInformation to obtain the data information about the cluster.
        

        @param request: GetClusterDataInformationRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetClusterDataInformationResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='GetClusterDataInformation',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/cluster/data-information',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetClusterDataInformationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cluster_data_information(self, request):
        """
        @summary Call GetClusterDataInformation to obtain the data information about the cluster.
        

        @param request: GetClusterDataInformationRequest

        @return: GetClusterDataInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_data_information_with_options(request, headers, runtime)

    def get_elastictask_with_options(self, instance_id, headers, runtime):
        """

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetElastictaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetElastictask',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/elastic-task' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetElastictaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_elastictask(self, instance_id):
        """

        @return: GetElastictaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_elastictask_with_options(instance_id, headers, runtime)

    def get_emon_grafana_alerts_with_options(self, project_id, request, headers, runtime):
        """
        @summary 获取高级监控报警自定义Grafana监控报警项
        

        @param request: GetEmonGrafanaAlertsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetEmonGrafanaAlertsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='GetEmonGrafanaAlerts',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/emon/projects/%s/grafana/proxy/api/alerts' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetEmonGrafanaAlertsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_emon_grafana_alerts(self, project_id, request):
        """
        @summary 获取高级监控报警自定义Grafana监控报警项
        

        @param request: GetEmonGrafanaAlertsRequest

        @return: GetEmonGrafanaAlertsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_emon_grafana_alerts_with_options(project_id, request, headers, runtime)

    def get_emon_grafana_dashboards_with_options(self, project_id, request, headers, runtime):
        """
        @summary 获取高级监控报警自定义Grafana监控大盘列表
        

        @param request: GetEmonGrafanaDashboardsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetEmonGrafanaDashboardsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='GetEmonGrafanaDashboards',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/emon/projects/%s/grafana/proxy/api/search' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetEmonGrafanaDashboardsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_emon_grafana_dashboards(self, project_id, request):
        """
        @summary 获取高级监控报警自定义Grafana监控大盘列表
        

        @param request: GetEmonGrafanaDashboardsRequest

        @return: GetEmonGrafanaDashboardsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_emon_grafana_dashboards_with_options(project_id, request, headers, runtime)

    def get_emon_monitor_data_with_options(self, project_id, request, headers, runtime):
        """

        @param request: GetEmonMonitorDataRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetEmonMonitorDataResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='GetEmonMonitorData',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/emon/projects/%s/metrics/query' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetEmonMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_emon_monitor_data(self, project_id, request):
        """

        @param request: GetEmonMonitorDataRequest

        @return: GetEmonMonitorDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_emon_monitor_data_with_options(project_id, request, headers, runtime)

    def get_open_store_usage_with_options(self, instance_id, headers, runtime):
        """
        @summary 统计OpenStore实例的存储容量和使用情况
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetOpenStoreUsageResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOpenStoreUsage',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/openstore/usage' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetOpenStoreUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_open_store_usage(self, instance_id):
        """
        @summary 统计OpenStore实例的存储容量和使用情况
        

        @return: GetOpenStoreUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_open_store_usage_with_options(instance_id, headers, runtime)

    def get_region_configuration_with_options(self, request, headers, runtime):
        """
        @summary The maximum number of nodes.
        

        @param request: GetRegionConfigurationRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetRegionConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.zone_id):
            query['zoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegionConfiguration',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/region',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetRegionConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_region_configuration(self, request):
        """
        @summary The maximum number of nodes.
        

        @param request: GetRegionConfigurationRequest

        @return: GetRegionConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_region_configuration_with_options(request, headers, runtime)

    def get_regional_instance_config_with_options(self, headers, runtime):
        """
        @summary 实例区域商品化配置
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetRegionalInstanceConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRegionalInstanceConfig',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/regions/instance-config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetRegionalInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_regional_instance_config(self):
        """
        @summary 实例区域商品化配置
        

        @return: GetRegionalInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_regional_instance_config_with_options(headers, runtime)

    def get_suggest_shrinkable_nodes_with_options(self, instance_id, request, headers, runtime):
        """
        @summary ES集群可缩容节点
        

        @param request: GetSuggestShrinkableNodesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetSuggestShrinkableNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSuggestShrinkableNodes',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/suggest-shrinkable-nodes' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetSuggestShrinkableNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_suggest_shrinkable_nodes(self, instance_id, request):
        """
        @summary ES集群可缩容节点
        

        @param request: GetSuggestShrinkableNodesRequest

        @return: GetSuggestShrinkableNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_suggest_shrinkable_nodes_with_options(instance_id, request, headers, runtime)

    def get_transferable_nodes_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 获取可数据迁移节点
        

        @param request: GetTransferableNodesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetTransferableNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTransferableNodes',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/transferable-nodes' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetTransferableNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_transferable_nodes(self, instance_id, request):
        """
        @summary 获取可数据迁移节点
        

        @param request: GetTransferableNodesRequest

        @return: GetTransferableNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_transferable_nodes_with_options(instance_id, request, headers, runtime)

    def initialize_operation_role_with_options(self, request, headers, runtime):
        """
        @summary Creates a service-linked role.
        
        @description > Before you perform auto scaling for a cluster at the China site (aliyun.com) or you use shippers to collect logs, you must create a service-linked role.
        

        @param request: InitializeOperationRoleRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: InitializeOperationRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='InitializeOperationRole',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/user/slr',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InitializeOperationRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def initialize_operation_role(self, request):
        """
        @summary Creates a service-linked role.
        
        @description > Before you perform auto scaling for a cluster at the China site (aliyun.com) or you use shippers to collect logs, you must create a service-linked role.
        

        @param request: InitializeOperationRoleRequest

        @return: InitializeOperationRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.initialize_operation_role_with_options(request, headers, runtime)

    def install_ack_operator_with_options(self, cluster_id, request, headers, runtime):
        """
        @summary Installs ES-operator for a Container Service for Kubernetes (ACK) cluster.
        
        @description > Before you install a shipper for an ACK cluster, you must call this operation to install ES-operator for the cluster.
        

        @param request: InstallAckOperatorRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: InstallAckOperatorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='InstallAckOperator',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/ack-clusters/%s/operator' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallAckOperatorResponse(),
            self.call_api(params, req, runtime)
        )

    def install_ack_operator(self, cluster_id, request):
        """
        @summary Installs ES-operator for a Container Service for Kubernetes (ACK) cluster.
        
        @description > Before you install a shipper for an ACK cluster, you must call this operation to install ES-operator for the cluster.
        

        @param request: InstallAckOperatorRequest

        @return: InstallAckOperatorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_ack_operator_with_options(cluster_id, request, headers, runtime)

    def install_kibana_system_plugin_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Call InstallKibanaSystemPlugin to install the Kibana plug-in. The Kibana specification must be 2-Core 4 GB or higher.
        

        @param request: InstallKibanaSystemPluginRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: InstallKibanaSystemPluginResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='InstallKibanaSystemPlugin',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/kibana-plugins/system/actions/install' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallKibanaSystemPluginResponse(),
            self.call_api(params, req, runtime)
        )

    def install_kibana_system_plugin(self, instance_id, request):
        """
        @summary Call InstallKibanaSystemPlugin to install the Kibana plug-in. The Kibana specification must be 2-Core 4 GB or higher.
        

        @param request: InstallKibanaSystemPluginRequest

        @return: InstallKibanaSystemPluginResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_kibana_system_plugin_with_options(instance_id, request, headers, runtime)

    def install_logstash_system_plugin_with_options(self, instance_id, request, headers, runtime):
        """
        @summary The returned data also contains *Headers** parameters, indicating that header information is returned.
        
        @description ls-cn-oew1qbgl\\\\*\\*\\*\
        

        @param request: InstallLogstashSystemPluginRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: InstallLogstashSystemPluginResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='InstallLogstashSystemPlugin',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/plugins/system/actions/install' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallLogstashSystemPluginResponse(),
            self.call_api(params, req, runtime)
        )

    def install_logstash_system_plugin(self, instance_id, request):
        """
        @summary The returned data also contains *Headers** parameters, indicating that header information is returned.
        
        @description ls-cn-oew1qbgl\\\\*\\*\\*\
        

        @param request: InstallLogstashSystemPluginRequest

        @return: InstallLogstashSystemPluginResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_logstash_system_plugin_with_options(instance_id, request, headers, runtime)

    def install_system_plugin_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Call InstallSystemPlugin to install a system preset plug-in.
        

        @param request: InstallSystemPluginRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: InstallSystemPluginResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='InstallSystemPlugin',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/plugins/system/actions/install' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallSystemPluginResponse(),
            self.call_api(params, req, runtime)
        )

    def install_system_plugin(self, instance_id, request):
        """
        @summary Call InstallSystemPlugin to install a system preset plug-in.
        

        @param request: InstallSystemPluginRequest

        @return: InstallSystemPluginResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_system_plugin_with_options(instance_id, request, headers, runtime)

    def install_user_plugins_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Installs custom plug-ins that are uploaded to the Elasticsearch console.
        

        @param request: InstallUserPluginsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: InstallUserPluginsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='InstallUserPlugins',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/plugins/user/actions/install' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallUserPluginsResponse(),
            self.call_api(params, req, runtime)
        )

    def install_user_plugins(self, instance_id, request):
        """
        @summary Installs custom plug-ins that are uploaded to the Elasticsearch console.
        

        @param request: InstallUserPluginsRequest

        @return: InstallUserPluginsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_user_plugins_with_options(instance_id, request, headers, runtime)

    def interrupt_elasticsearch_task_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: InterruptElasticsearchTaskRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: InterruptElasticsearchTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InterruptElasticsearchTask',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/interrupt' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InterruptElasticsearchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def interrupt_elasticsearch_task(self, instance_id, request):
        """

        @param request: InterruptElasticsearchTaskRequest

        @return: InterruptElasticsearchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.interrupt_elasticsearch_task_with_options(instance_id, request, headers, runtime)

    def interrupt_logstash_task_with_options(self, instance_id, request, headers, runtime):
        """
        @summary After the task is suspended, the Logstash cluster is in the suspended state.
        

        @param request: InterruptLogstashTaskRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: InterruptLogstashTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InterruptLogstashTask',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/actions/interrupt' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.InterruptLogstashTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def interrupt_logstash_task(self, instance_id, request):
        """
        @summary After the task is suspended, the Logstash cluster is in the suspended state.
        

        @param request: InterruptLogstashTaskRequest

        @return: InterruptLogstashTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.interrupt_logstash_task_with_options(instance_id, request, headers, runtime)

    def list_ack_clusters_with_options(self, request, headers, runtime):
        """
        @summary Queries a list of Container Service for Kubernetes (ACK) clusters.
        

        @param request: ListAckClustersRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAckClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAckClusters',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/ack-clusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAckClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ack_clusters(self, request):
        """
        @summary Queries a list of Container Service for Kubernetes (ACK) clusters.
        

        @param request: ListAckClustersRequest

        @return: ListAckClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ack_clusters_with_options(request, headers, runtime)

    def list_ack_namespaces_with_options(self, cluster_id, request, headers, runtime):
        """
        @summary Queries all namespaces in a specified Container Service for Kubernetes (ACK) cluster.
        
        @description > When you install a shipper on an ACK cluster, you must specify a namespace. You can call this operation to query all namespaces in the ACK cluster, and select a namespace based on your business requirements.
        

        @param request: ListAckNamespacesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAckNamespacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAckNamespaces',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/ack-clusters/%s/namespaces' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAckNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ack_namespaces(self, cluster_id, request):
        """
        @summary Queries all namespaces in a specified Container Service for Kubernetes (ACK) cluster.
        
        @description > When you install a shipper on an ACK cluster, you must specify a namespace. You can call this operation to query all namespaces in the ACK cluster, and select a namespace based on your business requirements.
        

        @param request: ListAckNamespacesRequest

        @return: ListAckNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ack_namespaces_with_options(cluster_id, request, headers, runtime)

    def list_action_records_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 变更记录 变更详情
        

        @param request: ListActionRecordsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListActionRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_names):
            query['actionNames'] = request.action_names
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.user_id):
            query['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListActionRecords',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/action-records' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListActionRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_action_records(self, instance_id, request):
        """
        @summary 变更记录 变更详情
        

        @param request: ListActionRecordsRequest

        @return: ListActionRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_action_records_with_options(instance_id, request, headers, runtime)

    def list_all_node_with_options(self, instance_id, request, headers, runtime):
        """
        @summary es-cn-tl32cpgwa002l\\\\*\\*\\*\
        

        @param request: ListAllNodeRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAllNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extended):
            query['extended'] = request.extended
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllNode',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/nodes' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAllNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_all_node(self, instance_id, request):
        """
        @summary es-cn-tl32cpgwa002l\\\\*\\*\\*\
        

        @param request: ListAllNodeRequest

        @return: ListAllNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_all_node_with_options(instance_id, request, headers, runtime)

    def list_alternative_snapshot_repos_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 实例可添加的OSS引用仓库
        

        @param request: ListAlternativeSnapshotReposRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAlternativeSnapshotReposResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.already_set_items):
            query['alreadySetItems'] = request.already_set_items
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlternativeSnapshotRepos',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/alternative-snapshot-repos' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAlternativeSnapshotReposResponse(),
            self.call_api(params, req, runtime)
        )

    def list_alternative_snapshot_repos(self, instance_id, request):
        """
        @summary 实例可添加的OSS引用仓库
        

        @param request: ListAlternativeSnapshotReposRequest

        @return: ListAlternativeSnapshotReposResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_alternative_snapshot_repos_with_options(instance_id, request, headers, runtime)

    def list_apm_with_options(self, request, headers, runtime):
        """
        @summary ListApm
        

        @param request: ListApmRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListApmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.output):
            query['output'] = request.output
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApm',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/apm',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListApmResponse(),
            self.call_api(params, req, runtime)
        )

    def list_apm(self, request):
        """
        @summary ListApm
        

        @param request: ListApmRequest

        @return: ListApmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_apm_with_options(request, headers, runtime)

    def list_available_es_instance_ids_with_options(self, instance_id, headers, runtime):
        """
        @summary Queries the Elasticsearch clusters that can be associated with a Logstash cluster when you configure the X-Pack Monitoring feature for the Logstash cluster.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAvailableEsInstanceIdsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListAvailableEsInstanceIds',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/available-elasticsearch-for-centralized-management' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAvailableEsInstanceIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_available_es_instance_ids(self, instance_id):
        """
        @summary Queries the Elasticsearch clusters that can be associated with a Logstash cluster when you configure the X-Pack Monitoring feature for the Logstash cluster.
        

        @return: ListAvailableEsInstanceIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_available_es_instance_ids_with_options(instance_id, headers, runtime)

    def list_collectors_with_options(self, request, headers, runtime):
        """
        @summary Queries shippers.
        

        @param request: ListCollectorsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListCollectorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.res_id):
            query['resId'] = request.res_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCollectors',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/collectors',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListCollectorsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_collectors(self, request):
        """
        @summary Queries shippers.
        

        @param request: ListCollectorsRequest

        @return: ListCollectorsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_collectors_with_options(request, headers, runtime)

    def list_component_indices_with_options(self, instance_id, request, headers, runtime):
        """
        @summary ES集群组合索引列表
        

        @param request: ListComponentIndicesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListComponentIndicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListComponentIndices',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/component-index' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListComponentIndicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_component_indices(self, instance_id, request):
        """
        @summary ES集群组合索引列表
        

        @param request: ListComponentIndicesRequest

        @return: ListComponentIndicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_component_indices_with_options(instance_id, request, headers, runtime)

    def list_connected_clusters_with_options(self, instance_id, headers, runtime):
        """
        @summary 获取与当前实例进行网络互通的实例列表
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListConnectedClustersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListConnectedClusters',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/connected-clusters' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListConnectedClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_connected_clusters(self, instance_id):
        """
        @summary 获取与当前实例进行网络互通的实例列表
        

        @return: ListConnectedClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_connected_clusters_with_options(instance_id, headers, runtime)

    def list_data_streams_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: ListDataStreamsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDataStreamsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_managed):
            query['isManaged'] = request.is_managed
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataStreams',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/data-streams' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDataStreamsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_streams(self, instance_id, request):
        """

        @param request: ListDataStreamsRequest

        @return: ListDataStreamsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_streams_with_options(instance_id, request, headers, runtime)

    def list_data_tasks_with_options(self, instance_id, headers, runtime):
        """

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDataTasksResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataTasks',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/data-task' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDataTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_tasks(self, instance_id):
        """

        @return: ListDataTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_tasks_with_options(instance_id, headers, runtime)

    def list_default_collector_configurations_with_options(self, request, headers, runtime):
        """
        @summary Queries the default configuration files of shippers.
        

        @param request: ListDefaultCollectorConfigurationsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDefaultCollectorConfigurationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.res_type):
            query['resType'] = request.res_type
        if not UtilClient.is_unset(request.res_version):
            query['resVersion'] = request.res_version
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDefaultCollectorConfigurations',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/beats/default-configurations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDefaultCollectorConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_default_collector_configurations(self, request):
        """
        @summary Queries the default configuration files of shippers.
        

        @param request: ListDefaultCollectorConfigurationsRequest

        @return: ListDefaultCollectorConfigurationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_default_collector_configurations_with_options(request, headers, runtime)

    def list_deprecated_templates_with_options(self, instance_id, request, headers, runtime):
        """
        @summary ListDeprecatedTemplates
        

        @param request: ListDeprecatedTemplatesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDeprecatedTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeprecatedTemplates',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/deprecated-templates' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDeprecatedTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_deprecated_templates(self, instance_id, request):
        """
        @summary ListDeprecatedTemplates
        

        @param request: ListDeprecatedTemplatesRequest

        @return: ListDeprecatedTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_deprecated_templates_with_options(instance_id, request, headers, runtime)

    def list_diagnose_indices_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Queries the indexes for health diagnosis performed on an Elasticsearch cluster.
        

        @param request: ListDiagnoseIndicesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDiagnoseIndicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDiagnoseIndices',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/diagnosis/instances/%s/indices' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDiagnoseIndicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_diagnose_indices(self, instance_id, request):
        """
        @summary Queries the indexes for health diagnosis performed on an Elasticsearch cluster.
        

        @param request: ListDiagnoseIndicesRequest

        @return: ListDiagnoseIndicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_diagnose_indices_with_options(instance_id, request, headers, runtime)

    def list_diagnose_report_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 获取集群诊断报告列表
        

        @param request: ListDiagnoseReportRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDiagnoseReportResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detail):
            query['detail'] = request.detail
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDiagnoseReport',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/diagnosis/instances/%s/reports' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDiagnoseReportResponse(),
            self.call_api(params, req, runtime)
        )

    def list_diagnose_report(self, instance_id, request):
        """
        @summary 获取集群诊断报告列表
        

        @param request: ListDiagnoseReportRequest

        @return: ListDiagnoseReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_diagnose_report_with_options(instance_id, request, headers, runtime)

    def list_diagnose_report_ids_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Queries the IDs of the historical intelligent O&M reports of an Elasticsearch cluster.
        

        @param request: ListDiagnoseReportIdsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDiagnoseReportIdsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDiagnoseReportIds',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/diagnosis/instances/%s/report-ids' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDiagnoseReportIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_diagnose_report_ids(self, instance_id, request):
        """
        @summary Queries the IDs of the historical intelligent O&M reports of an Elasticsearch cluster.
        

        @param request: ListDiagnoseReportIdsRequest

        @return: ListDiagnoseReportIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_diagnose_report_ids_with_options(instance_id, request, headers, runtime)

    def list_diagnosis_items_with_options(self, request, headers, runtime):
        """
        @summary The diagnostic item is used to check whether data write requests of a cluster are accumulated. If data write requests are accumulated, a bulk rejection occurs. This may cause data loss and severely consume system resources.
        

        @param request: ListDiagnosisItemsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDiagnosisItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDiagnosisItems',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/diagnosis/items',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDiagnosisItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_diagnosis_items(self, request):
        """
        @summary The diagnostic item is used to check whether data write requests of a cluster are accumulated. If data write requests are accumulated, a bulk rejection occurs. This may cause data loss and severely consume system resources.
        

        @param request: ListDiagnosisItemsRequest

        @return: ListDiagnosisItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_diagnosis_items_with_options(request, headers, runtime)

    def list_dict_information_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: ListDictInformationRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDictInformationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analyzer_type):
            query['analyzerType'] = request.analyzer_type
        if not UtilClient.is_unset(request.bucket_name):
            query['bucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDictInformation',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/dict/_info' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDictInformationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dict_information(self, instance_id, request):
        """

        @param request: ListDictInformationRequest

        @return: ListDictInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dict_information_with_options(instance_id, request, headers, runtime)

    def list_dicts_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Queries the details of a specified type of dictionary.
        

        @param request: ListDictsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDictsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analyzer_type):
            query['analyzerType'] = request.analyzer_type
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDicts',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/dicts' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDictsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dicts(self, instance_id, request):
        """
        @summary Queries the details of a specified type of dictionary.
        

        @param request: ListDictsRequest

        @return: ListDictsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dicts_with_options(instance_id, request, headers, runtime)

    def list_ecs_instances_with_options(self, request, headers, runtime):
        """
        @description *Important** To call this operation, you must create the Aliyun Elasticsearch AccessingOOSRole and the system service role AliyunOOSAccessingECS 4ESRole to Elasticsearch the service account to obtain the ECS access permissions of the primary account. For more information, see [Collect ECS service logs](https://help.aliyun.com/document_detail/146446.html).
        

        @param request: ListEcsInstancesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListEcsInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_instance_ids):
            query['ecsInstanceIds'] = request.ecs_instance_ids
        if not UtilClient.is_unset(request.ecs_instance_name):
            query['ecsInstanceName'] = request.ecs_instance_name
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.tags):
            query['tags'] = request.tags
        if not UtilClient.is_unset(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEcsInstances',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/ecs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListEcsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ecs_instances(self, request):
        """
        @description *Important** To call this operation, you must create the Aliyun Elasticsearch AccessingOOSRole and the system service role AliyunOOSAccessingECS 4ESRole to Elasticsearch the service account to obtain the ECS access permissions of the primary account. For more information, see [Collect ECS service logs](https://help.aliyun.com/document_detail/146446.html).
        

        @param request: ListEcsInstancesRequest

        @return: ListEcsInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ecs_instances_with_options(request, headers, runtime)

    def list_extendfiles_with_options(self, instance_id, headers, runtime):
        """
        @summary Queries the driver files of a Logstash cluster.
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListExtendfilesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListExtendfiles',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/extendfiles' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListExtendfilesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_extendfiles(self, instance_id):
        """
        @summary Queries the driver files of a Logstash cluster.
        

        @return: ListExtendfilesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_extendfiles_with_options(instance_id, headers, runtime)

    def list_ilmpolicies_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: ListILMPoliciesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListILMPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['policyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListILMPolicies',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/ilm-policies' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListILMPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ilmpolicies(self, instance_id, request):
        """

        @param request: ListILMPoliciesRequest

        @return: ListILMPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ilmpolicies_with_options(instance_id, request, headers, runtime)

    def list_index_templates_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: ListIndexTemplatesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListIndexTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.index_template):
            query['indexTemplate'] = request.index_template
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIndexTemplates',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/index-templates' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListIndexTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_index_templates(self, instance_id, request):
        """

        @param request: ListIndexTemplatesRequest

        @return: ListIndexTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_index_templates_with_options(instance_id, request, headers, runtime)

    def list_instance_with_options(self, request, headers, runtime):
        """
        @summary 查询Elasticsearch实例列表
        

        @param request: ListInstanceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.es_version):
            query['esVersion'] = request.es_version
        if not UtilClient.is_unset(request.instance_category):
            query['instanceCategory'] = request.instance_category
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.payment_type):
            query['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.tags):
            query['tags'] = request.tags
        if not UtilClient.is_unset(request.vpc_id):
            query['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['zoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instance(self, request):
        """
        @summary 查询Elasticsearch实例列表
        

        @param request: ListInstanceRequest

        @return: ListInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_with_options(request, headers, runtime)

    def list_instance_history_events_with_options(self, tmp_req, headers, runtime):
        """
        @summary 集群触发的硬件运维事件列表
        

        @param tmp_req: ListInstanceHistoryEventsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListInstanceHistoryEventsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = elasticsearch_20170613_models.ListInstanceHistoryEventsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.event_cycle_status):
            request.event_cycle_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.event_cycle_status, 'eventCycleStatus', 'simple')
        if not UtilClient.is_unset(tmp_req.event_level):
            request.event_level_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.event_level, 'eventLevel', 'simple')
        if not UtilClient.is_unset(tmp_req.event_type):
            request.event_type_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.event_type, 'eventType', 'simple')
        query = {}
        if not UtilClient.is_unset(request.event_create_end_time):
            query['eventCreateEndTime'] = request.event_create_end_time
        if not UtilClient.is_unset(request.event_create_start_time):
            query['eventCreateStartTime'] = request.event_create_start_time
        if not UtilClient.is_unset(request.event_cycle_status_shrink):
            query['eventCycleStatus'] = request.event_cycle_status_shrink
        if not UtilClient.is_unset(request.event_execute_end_time):
            query['eventExecuteEndTime'] = request.event_execute_end_time
        if not UtilClient.is_unset(request.event_execute_start_time):
            query['eventExecuteStartTime'] = request.event_execute_start_time
        if not UtilClient.is_unset(request.event_finash_end_time):
            query['eventFinashEndTime'] = request.event_finash_end_time
        if not UtilClient.is_unset(request.event_finash_start_time):
            query['eventFinashStartTime'] = request.event_finash_start_time
        if not UtilClient.is_unset(request.event_level_shrink):
            query['eventLevel'] = request.event_level_shrink
        if not UtilClient.is_unset(request.event_type_shrink):
            query['eventType'] = request.event_type_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_ip):
            query['nodeIP'] = request.node_ip
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='ListInstanceHistoryEvents',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/events',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListInstanceHistoryEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instance_history_events(self, request):
        """
        @summary 集群触发的硬件运维事件列表
        

        @param request: ListInstanceHistoryEventsRequest

        @return: ListInstanceHistoryEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_history_events_with_options(request, headers, runtime)

    def list_instance_indices_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 获取当前实例先特定的索引列表
        

        @param request: ListInstanceIndicesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListInstanceIndicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['all'] = request.all
        if not UtilClient.is_unset(request.is_managed):
            query['isManaged'] = request.is_managed
        if not UtilClient.is_unset(request.is_openstore):
            query['isOpenstore'] = request.is_openstore
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceIndices',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/indices' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListInstanceIndicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instance_indices(self, instance_id, request):
        """
        @summary 获取当前实例先特定的索引列表
        

        @param request: ListInstanceIndicesRequest

        @return: ListInstanceIndicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_indices_with_options(instance_id, request, headers, runtime)

    def list_kibana_plugins_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Queries a list of Kibana plug-ins.
        

        @param request: ListKibanaPluginsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListKibanaPluginsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKibanaPlugins',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/kibana-plugins' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListKibanaPluginsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_kibana_plugins(self, instance_id, request):
        """
        @summary Queries a list of Kibana plug-ins.
        

        @param request: ListKibanaPluginsRequest

        @return: ListKibanaPluginsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_kibana_plugins_with_options(instance_id, request, headers, runtime)

    def list_kibana_pvl_network_with_options(self, instance_id, headers, runtime):
        """
        @summary 查询kibana私网连接信息
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListKibanaPvlNetworkResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListKibanaPvlNetwork',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/get-kibana-private' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListKibanaPvlNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    def list_kibana_pvl_network(self, instance_id):
        """
        @summary 查询kibana私网连接信息
        

        @return: ListKibanaPvlNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_kibana_pvl_network_with_options(instance_id, headers, runtime)

    def list_logstash_with_options(self, request, headers, runtime):
        """
        @summary Logstash集群列表
        

        @param request: ListLogstashRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListLogstashResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.tags):
            query['tags'] = request.tags
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogstash',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListLogstashResponse(),
            self.call_api(params, req, runtime)
        )

    def list_logstash(self, request):
        """
        @summary Logstash集群列表
        

        @param request: ListLogstashRequest

        @return: ListLogstashResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logstash_with_options(request, headers, runtime)

    def list_logstash_log_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 获取Logstash日志
        

        @param request: ListLogstashLogRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListLogstashLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogstashLog',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/search-log' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListLogstashLogResponse(),
            self.call_api(params, req, runtime)
        )

    def list_logstash_log(self, instance_id, request):
        """
        @summary 获取Logstash日志
        

        @param request: ListLogstashLogRequest

        @return: ListLogstashLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logstash_log_with_options(instance_id, request, headers, runtime)

    def list_logstash_plugins_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Logstash插件列表
        

        @param request: ListLogstashPluginsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListLogstashPluginsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogstashPlugins',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/plugins' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListLogstashPluginsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_logstash_plugins(self, instance_id, request):
        """
        @summary Logstash插件列表
        

        @param request: ListLogstashPluginsRequest

        @return: ListLogstashPluginsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logstash_plugins_with_options(instance_id, request, headers, runtime)

    def list_nodes_with_options(self, res_id, request, headers, runtime):
        """
        @summary Queries the statuses of Elastic Compute Service (ECS) instances on which a shipper is installed.
        

        @param request: ListNodesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_instance_ids):
            query['ecsInstanceIds'] = request.ecs_instance_ids
        if not UtilClient.is_unset(request.ecs_instance_name):
            query['ecsInstanceName'] = request.ecs_instance_name
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.tags):
            query['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/collectors/%s/nodes' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(res_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_nodes(self, res_id, request):
        """
        @summary Queries the statuses of Elastic Compute Service (ECS) instances on which a shipper is installed.
        

        @param request: ListNodesRequest

        @return: ListNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_nodes_with_options(res_id, request, headers, runtime)

    def list_pipeline_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: ListPipelineRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListPipelineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.pipeline_id):
            query['pipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipeline',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/pipelines' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pipeline(self, instance_id, request):
        """

        @param request: ListPipelineRequest

        @return: ListPipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_with_options(instance_id, request, headers, runtime)

    def list_pipeline_ids_with_options(self, instance_id, request, headers, runtime):
        """
        @summary The error message returned.
        

        @param request: ListPipelineIdsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListPipelineIdsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='ListPipelineIds',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/pipeline-ids' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListPipelineIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pipeline_ids(self, instance_id, request):
        """
        @summary The error message returned.
        

        @param request: ListPipelineIdsRequest

        @return: ListPipelineIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_ids_with_options(instance_id, request, headers, runtime)

    def list_plugins_with_options(self, instance_id, request, headers, runtime):
        """
        @summary ES系统插件列表
        

        @param request: ListPluginsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListPluginsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPlugins',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/plugins' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListPluginsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_plugins(self, instance_id, request):
        """
        @summary ES系统插件列表
        

        @param request: ListPluginsRequest

        @return: ListPluginsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_plugins_with_options(instance_id, request, headers, runtime)

    def list_search_log_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 查看Elasticsearch集群各种类型的日志
        

        @param request: ListSearchLogRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListSearchLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSearchLog',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/search-log' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListSearchLogResponse(),
            self.call_api(params, req, runtime)
        )

    def list_search_log(self, instance_id, request):
        """
        @summary 查看Elasticsearch集群各种类型的日志
        

        @param request: ListSearchLogRequest

        @return: ListSearchLogResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_search_log_with_options(instance_id, request, headers, runtime)

    def list_shard_recoveries_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Queries the information about shards that are being restored or shards that are restored. By default, this operation returns only the information about shards that are being restored after you call this operation.
        
        @description > The restoration of a shard is a process of synchronizing data from a primary shard to a replica shard. After the restoration is complete, the replica shard is available for data searches.
        

        @param request: ListShardRecoveriesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListShardRecoveriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_only):
            query['activeOnly'] = request.active_only
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListShardRecoveries',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/cat-recovery' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListShardRecoveriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_shard_recoveries(self, instance_id, request):
        """
        @summary Queries the information about shards that are being restored or shards that are restored. By default, this operation returns only the information about shards that are being restored after you call this operation.
        
        @description > The restoration of a shard is a process of synchronizing data from a primary shard to a replica shard. After the restoration is complete, the replica shard is available for data searches.
        

        @param request: ListShardRecoveriesRequest

        @return: ListShardRecoveriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_shard_recoveries_with_options(instance_id, request, headers, runtime)

    def list_snapshot_repos_by_instance_id_with_options(self, instance_id, headers, runtime):
        """
        @summary 获取跨集群索引仓库列表
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListSnapshotReposByInstanceIdResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSnapshotReposByInstanceId',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/snapshot-repos' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListSnapshotReposByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    def list_snapshot_repos_by_instance_id(self, instance_id):
        """
        @summary 获取跨集群索引仓库列表
        

        @return: ListSnapshotReposByInstanceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_snapshot_repos_by_instance_id_with_options(instance_id, headers, runtime)

    def list_tag_resources_with_options(self, request, headers, runtime):
        """
        @summary 查看资源和标签关系
        

        @param request: ListTagResourcesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        """
        @summary 查看资源和标签关系
        

        @param request: ListTagResourcesRequest

        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    def list_tags_with_options(self, request, headers, runtime):
        """
        @summary 查看所有已常见的标签
        

        @param request: ListTagsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/tags/all-tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tags(self, request):
        """
        @summary 查看所有已常见的标签
        

        @param request: ListTagsRequest

        @return: ListTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tags_with_options(request, headers, runtime)

    def list_vpc_endpoints_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Queries the statuses of endpoints in the virtual private cloud (VPC) within the Elasticsearch service account.
        

        @param request: ListVpcEndpointsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListVpcEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcEndpoints',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/vpc-endpoints' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListVpcEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_vpc_endpoints(self, instance_id, request):
        """
        @summary Queries the statuses of endpoints in the virtual private cloud (VPC) within the Elasticsearch service account.
        

        @param request: ListVpcEndpointsRequest

        @return: ListVpcEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_vpc_endpoints_with_options(instance_id, request, headers, runtime)

    def migrate_to_other_zone_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Call the MigrateToOtherZone to migrate the nodes in the specified zone to the destination zone.
        
        @description If the specifications in your zone are insufficient, you can upgrade your instance to nodes in another zone. Before calling this interface, you must ensure that:
        The error message returned because the current account is in a zone that has sufficient resources.
        After migrating nodes with current specifications to another zone, you need to manually [upgrade cluster](https://help.aliyun.com/document_detail/96650.html) because the cluster will not be upgraded during the migration process. Therefore, select a zone with sufficient resources to avoid cluster upgrade failure. We recommend that you choose new zones that are in lower alphabetical order. For example, for cn-hangzhou-e and cn-hangzhou-h zones, choose cn-hangzhou-h first.
        The cluster is in the healthy state.
        Can be passed`  GET _cat/health?v  `command to view the health status of the cluster.
        

        @param request: MigrateToOtherZoneRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: MigrateToOtherZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='MigrateToOtherZone',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/migrate-zones' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.MigrateToOtherZoneResponse(),
            self.call_api(params, req, runtime)
        )

    def migrate_to_other_zone(self, instance_id, request):
        """
        @summary Call the MigrateToOtherZone to migrate the nodes in the specified zone to the destination zone.
        
        @description If the specifications in your zone are insufficient, you can upgrade your instance to nodes in another zone. Before calling this interface, you must ensure that:
        The error message returned because the current account is in a zone that has sufficient resources.
        After migrating nodes with current specifications to another zone, you need to manually [upgrade cluster](https://help.aliyun.com/document_detail/96650.html) because the cluster will not be upgraded during the migration process. Therefore, select a zone with sufficient resources to avoid cluster upgrade failure. We recommend that you choose new zones that are in lower alphabetical order. For example, for cn-hangzhou-e and cn-hangzhou-h zones, choose cn-hangzhou-h first.
        The cluster is in the healthy state.
        Can be passed`  GET _cat/health?v  `command to view the health status of the cluster.
        

        @param request: MigrateToOtherZoneRequest

        @return: MigrateToOtherZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.migrate_to_other_zone_with_options(instance_id, request, headers, runtime)

    def modify_deploy_machine_with_options(self, res_id, request, headers, runtime):
        """
        @summary Changes the Elastic Compute Service (ECS) instances on which a shipper is installed.
        

        @param request: ModifyDeployMachineRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDeployMachineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='ModifyDeployMachine',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/collectors/%s/actions/modify-deploy-machines' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(res_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ModifyDeployMachineResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_deploy_machine(self, res_id, request):
        """
        @summary Changes the Elastic Compute Service (ECS) instances on which a shipper is installed.
        

        @param request: ModifyDeployMachineRequest

        @return: ModifyDeployMachineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_deploy_machine_with_options(res_id, request, headers, runtime)

    def modify_elastictask_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: ModifyElastictaskRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyElastictaskResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='ModifyElastictask',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/elastic-task' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ModifyElastictaskResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_elastictask(self, instance_id, request):
        """

        @param request: ModifyElastictaskRequest

        @return: ModifyElastictaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_elastictask_with_options(instance_id, request, headers, runtime)

    def modify_instance_maintain_time_with_options(self, instance_id, request, headers, runtime):
        """
        @summary ## RequestBody
        You must also specify the following parameters in the RequestBody parameter to specify the maintenance window information.
        | Parameter | Type | Required | Example | Description |
        | --------- | ---- | -------- | ------- | ----------- |
        | maintainStartTime | String | No | 02:00Z | The start time of the maintenance window. Specify the time in the HH:mmZ format. The time must be in UTC. |
        | maintainEndTime | String | No | 06:00Z | The end time of the maintenance window. Specify the time in the HH:mmZ format. The time must be displayed in UTC. |
        | openMaintainTime | boolean | Yes | true | Specifies whether to enable the maintenance window feature. Only *true** is supported, indicating that the feature is enabled. |
        Examples:
        ```
        {
        "openMaintainTime": true,
        "maintainStartTime": "03:00Z",
        "maintainEndTime": "04:00Z"
        }
        ```
        
        @description es-cn-n6w1o1x0w001c\\\\*\\*\\*\
        

        @param request: ModifyInstanceMaintainTimeRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyInstanceMaintainTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='ModifyInstanceMaintainTime',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/modify-maintaintime' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ModifyInstanceMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_maintain_time(self, instance_id, request):
        """
        @summary ## RequestBody
        You must also specify the following parameters in the RequestBody parameter to specify the maintenance window information.
        | Parameter | Type | Required | Example | Description |
        | --------- | ---- | -------- | ------- | ----------- |
        | maintainStartTime | String | No | 02:00Z | The start time of the maintenance window. Specify the time in the HH:mmZ format. The time must be in UTC. |
        | maintainEndTime | String | No | 06:00Z | The end time of the maintenance window. Specify the time in the HH:mmZ format. The time must be displayed in UTC. |
        | openMaintainTime | boolean | Yes | true | Specifies whether to enable the maintenance window feature. Only *true** is supported, indicating that the feature is enabled. |
        Examples:
        ```
        {
        "openMaintainTime": true,
        "maintainStartTime": "03:00Z",
        "maintainEndTime": "04:00Z"
        }
        ```
        
        @description es-cn-n6w1o1x0w001c\\\\*\\*\\*\
        

        @param request: ModifyInstanceMaintainTimeRequest

        @return: ModifyInstanceMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_instance_maintain_time_with_options(instance_id, request, headers, runtime)

    def modify_white_ips_with_options(self, instance_id, request, headers, runtime):
        """
        @summary >  If you want to add an IP address whitelist, you can set the modifyMode parameter only to Cover. If you set this parameter to Delete or Append, you can only update an IP address whitelist.
        If you set the modifyMode parameter to Cover and leave the ips parameter empty, the system deletes the specified whitelist. If the whitelist specified by using the groupName parameter does not exist, the system creates such a whitelist.
        If you set the modifyMode parameter to Delete, at least one IP address must be retained for the specified whitelist.
        If you set the modifyMode parameter to Append, you must make sure that the specified whitelist exists. Otherwise, the system reports the NotFound error.
        
        @description The ID of the cluster.
        

        @param request: ModifyWhiteIpsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyWhiteIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.modify_mode):
            body['modifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.network_type):
            body['networkType'] = request.network_type
        if not UtilClient.is_unset(request.node_type):
            body['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.white_ip_group):
            body['whiteIpGroup'] = request.white_ip_group
        if not UtilClient.is_unset(request.white_ip_list):
            body['whiteIpList'] = request.white_ip_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyWhiteIps',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/modify-white-ips' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ModifyWhiteIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_white_ips(self, instance_id, request):
        """
        @summary >  If you want to add an IP address whitelist, you can set the modifyMode parameter only to Cover. If you set this parameter to Delete or Append, you can only update an IP address whitelist.
        If you set the modifyMode parameter to Cover and leave the ips parameter empty, the system deletes the specified whitelist. If the whitelist specified by using the groupName parameter does not exist, the system creates such a whitelist.
        If you set the modifyMode parameter to Delete, at least one IP address must be retained for the specified whitelist.
        If you set the modifyMode parameter to Append, you must make sure that the specified whitelist exists. Otherwise, the system reports the NotFound error.
        
        @description The ID of the cluster.
        

        @param request: ModifyWhiteIpsRequest

        @return: ModifyWhiteIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_white_ips_with_options(instance_id, request, headers, runtime)

    def move_resource_group_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Migrates an Elasticsearch cluster to a specified resource group.
        

        @param request: MoveResourceGroupRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: MoveResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/resourcegroup' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def move_resource_group(self, instance_id, request):
        """
        @summary Migrates an Elasticsearch cluster to a specified resource group.
        

        @param request: MoveResourceGroupRequest

        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.move_resource_group_with_options(instance_id, request, headers, runtime)

    def open_diagnosis_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: OpenDiagnosisRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: OpenDiagnosisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenDiagnosis',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/diagnosis/instances/%s/actions/open-diagnosis' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.OpenDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    def open_diagnosis(self, instance_id, request):
        """

        @param request: OpenDiagnosisRequest

        @return: OpenDiagnosisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.open_diagnosis_with_options(instance_id, request, headers, runtime)

    def open_https_with_options(self, instance_id, request, headers, runtime):
        """
        @description >  To ensure data security, we recommend that you enable HTTPS.
        

        @param request: OpenHttpsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: OpenHttpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenHttps',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/open-https' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.OpenHttpsResponse(),
            self.call_api(params, req, runtime)
        )

    def open_https(self, instance_id, request):
        """
        @description >  To ensure data security, we recommend that you enable HTTPS.
        

        @param request: OpenHttpsRequest

        @return: OpenHttpsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.open_https_with_options(instance_id, request, headers, runtime)

    def post_emon_try_alarm_rule_with_options(self, project_id, alarm_group_id, request, headers, runtime):
        """

        @param request: PostEmonTryAlarmRuleRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: PostEmonTryAlarmRuleResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='PostEmonTryAlarmRule',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/emon/projects/%s/alarm-groups/%s/alarm-rules/_test' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(project_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(alarm_group_id))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.PostEmonTryAlarmRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def post_emon_try_alarm_rule(self, project_id, alarm_group_id, request):
        """

        @param request: PostEmonTryAlarmRuleRequest

        @return: PostEmonTryAlarmRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.post_emon_try_alarm_rule_with_options(project_id, alarm_group_id, request, headers, runtime)

    def recommend_templates_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: RecommendTemplatesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RecommendTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.usage_scenario):
            query['usageScenario'] = request.usage_scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecommendTemplates',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/recommended-templates' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RecommendTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def recommend_templates(self, instance_id, request):
        """

        @param request: RecommendTemplatesRequest

        @return: RecommendTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recommend_templates_with_options(instance_id, request, headers, runtime)

    def reinstall_collector_with_options(self, res_id, request, headers, runtime):
        """
        @summary Installs a shipper that failed to be installed when you create the shipper.
        

        @param request: ReinstallCollectorRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ReinstallCollectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='ReinstallCollector',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/collectors/%s/actions/reinstall' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(res_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ReinstallCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    def reinstall_collector(self, res_id, request):
        """
        @summary Installs a shipper that failed to be installed when you create the shipper.
        

        @param request: ReinstallCollectorRequest

        @return: ReinstallCollectorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reinstall_collector_with_options(res_id, request, headers, runtime)

    def remove_apm_with_options(self, instance_id, headers, runtime):
        """
        @summary RemoveApm
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveApmResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveApm',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/apm/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RemoveApmResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_apm(self, instance_id):
        """
        @summary RemoveApm
        

        @return: RemoveApmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_apm_with_options(instance_id, headers, runtime)

    def renew_instance_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Call RenewInstance to renew a subscription instance.
        

        @param request: RenewInstanceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RenewInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/renew' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_instance(self, instance_id, request):
        """
        @summary Call RenewInstance to renew a subscription instance.
        

        @param request: RenewInstanceRequest

        @return: RenewInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.renew_instance_with_options(instance_id, request, headers, runtime)

    def renew_logstash_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Renews a Logstash cluster.
        

        @param request: RenewLogstashRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RenewLogstashResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='RenewLogstash',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/actions/renew' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RenewLogstashResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_logstash(self, instance_id, request):
        """
        @summary Renews a Logstash cluster.
        

        @param request: RenewLogstashRequest

        @return: RenewLogstashResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.renew_logstash_with_options(instance_id, request, headers, runtime)

    def restart_collector_with_options(self, res_id, request, headers, runtime):
        """
        @summary Restarts a shipper.
        

        @param request: RestartCollectorRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RestartCollectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartCollector',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/collectors/%s/actions/restart' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(res_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RestartCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_collector(self, res_id, request):
        """
        @summary Restarts a shipper.
        

        @param request: RestartCollectorRequest

        @return: RestartCollectorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_collector_with_options(res_id, request, headers, runtime)

    def restart_instance_with_options(self, instance_id, request, headers, runtime):
        """
        @summary You can call this operation to restart a specified Elasticsearch instance.
        
        @description >  After the instance is restarted, the instance enters the activating state. After the instance is restarted, its status changes to active. Alibaba Cloud Elasticsearch supports restarting a single node. Restarting a node can be divided into normal restart and blue-green restart.
        

        @param request: RestartInstanceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RestartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/restart' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_instance(self, instance_id, request):
        """
        @summary You can call this operation to restart a specified Elasticsearch instance.
        
        @description >  After the instance is restarted, the instance enters the activating state. After the instance is restarted, its status changes to active. Alibaba Cloud Elasticsearch supports restarting a single node. Restarting a node can be divided into normal restart and blue-green restart.
        

        @param request: RestartInstanceRequest

        @return: RestartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_instance_with_options(instance_id, request, headers, runtime)

    def restart_logstash_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 重启Logstash集群
        

        @param request: RestartLogstashRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RestartLogstashResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        body = {}
        if not UtilClient.is_unset(request.batch_count):
            body['batchCount'] = request.batch_count
        if not UtilClient.is_unset(request.blue_green_dep):
            body['blueGreenDep'] = request.blue_green_dep
        if not UtilClient.is_unset(request.node_types):
            body['nodeTypes'] = request.node_types
        if not UtilClient.is_unset(request.nodes):
            body['nodes'] = request.nodes
        if not UtilClient.is_unset(request.restart_type):
            body['restartType'] = request.restart_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestartLogstash',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/actions/restart' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RestartLogstashResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_logstash(self, instance_id, request):
        """
        @summary 重启Logstash集群
        

        @param request: RestartLogstashRequest

        @return: RestartLogstashResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_logstash_with_options(instance_id, request, headers, runtime)

    def resume_elasticsearch_task_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: ResumeElasticsearchTaskRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResumeElasticsearchTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeElasticsearchTask',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/resume' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ResumeElasticsearchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_elasticsearch_task(self, instance_id, request):
        """

        @param request: ResumeElasticsearchTaskRequest

        @return: ResumeElasticsearchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_elasticsearch_task_with_options(instance_id, request, headers, runtime)

    def resume_logstash_task_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Resumes a change task of a Logstash cluster. After the task is resumed, the Logstash cluster is in the activating state.
        

        @param request: ResumeLogstashTaskRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ResumeLogstashTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeLogstashTask',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/actions/resume' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ResumeLogstashTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_logstash_task(self, instance_id, request):
        """
        @summary Resumes a change task of a Logstash cluster. After the task is resumed, the Logstash cluster is in the activating state.
        

        @param request: ResumeLogstashTaskRequest

        @return: ResumeLogstashTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_logstash_task_with_options(instance_id, request, headers, runtime)

    def rollover_data_stream_with_options(self, instance_id, data_stream, request, headers, runtime):
        """
        @summary 滚动数据流，生成新索引
        

        @param request: RolloverDataStreamRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RolloverDataStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RolloverDataStream',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/data-streams/%s/rollover' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(data_stream))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RolloverDataStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def rollover_data_stream(self, instance_id, data_stream, request):
        """
        @summary 滚动数据流，生成新索引
        

        @param request: RolloverDataStreamRequest

        @return: RolloverDataStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rollover_data_stream_with_options(instance_id, data_stream, request, headers, runtime)

    def run_pipelines_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Runs pipelines in a Logstash cluster.
        

        @param request: RunPipelinesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RunPipelinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='RunPipelines',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/pipelines/action/run' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RunPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    def run_pipelines(self, instance_id, request):
        """
        @summary Runs pipelines in a Logstash cluster.
        

        @param request: RunPipelinesRequest

        @return: RunPipelinesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_pipelines_with_options(instance_id, request, headers, runtime)

    def shrink_node_with_options(self, instance_id, request, headers, runtime):
        """
        @summary ES集群缩节点
        

        @param request: ShrinkNodeRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ShrinkNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='ShrinkNode',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/shrink' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ShrinkNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def shrink_node(self, instance_id, request):
        """
        @summary ES集群缩节点
        

        @param request: ShrinkNodeRequest

        @return: ShrinkNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.shrink_node_with_options(instance_id, request, headers, runtime)

    def start_apm_with_options(self, instance_id, headers, runtime):
        """
        @summary StartApm
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartApmResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartApm',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/apm/%s/actions/start' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.StartApmResponse(),
            self.call_api(params, req, runtime)
        )

    def start_apm(self, instance_id):
        """
        @summary StartApm
        

        @return: StartApmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_apm_with_options(instance_id, headers, runtime)

    def start_collector_with_options(self, res_id, request, headers, runtime):
        """
        @summary Starts a collector to collect data.
        

        @param request: StartCollectorRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartCollectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCollector',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/collectors/%s/actions/start' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(res_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.StartCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    def start_collector(self, res_id, request):
        """
        @summary Starts a collector to collect data.
        

        @param request: StartCollectorRequest

        @return: StartCollectorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_collector_with_options(res_id, request, headers, runtime)

    def stop_apm_with_options(self, instance_id, headers, runtime):
        """
        @summary StopApm
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopApmResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopApm',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/apm/%s/actions/stop' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.StopApmResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_apm(self, instance_id):
        """
        @summary StopApm
        

        @return: StopApmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_apm_with_options(instance_id, headers, runtime)

    def stop_collector_with_options(self, res_id, request, headers, runtime):
        """
        @summary Stops a shipper.
        

        @param request: StopCollectorRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopCollectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCollector',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/collectors/%s/actions/stop' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(res_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.StopCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_collector(self, res_id, request):
        """
        @summary Stops a shipper.
        

        @param request: StopCollectorRequest

        @return: StopCollectorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_collector_with_options(res_id, request, headers, runtime)

    def stop_pipelines_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Stops pipelines in a Logstash cluster.
        

        @param request: StopPipelinesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopPipelinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='StopPipelines',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/pipelines/action/stop' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.StopPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_pipelines(self, instance_id, request):
        """
        @summary Stops pipelines in a Logstash cluster.
        

        @param request: StopPipelinesRequest

        @return: StopPipelinesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_pipelines_with_options(instance_id, request, headers, runtime)

    def tag_resources_with_options(self, request, headers, runtime):
        """
        @summary The information about the clusters and tags.
        

        @param request: TagResourcesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        """
        @summary The information about the clusters and tags.
        

        @param request: TagResourcesRequest

        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    def transfer_node_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 缩节点，数据迁移
        

        @param request: TransferNodeRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: TransferNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='TransferNode',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/transfer' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.TransferNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def transfer_node(self, instance_id, request):
        """
        @summary 缩节点，数据迁移
        

        @param request: TransferNodeRequest

        @return: TransferNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.transfer_node_with_options(instance_id, request, headers, runtime)

    def trigger_network_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 开关ES集群及Kibana节点公私网访问
        

        @param request: TriggerNetworkRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: TriggerNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.action_type):
            body['actionType'] = request.action_type
        if not UtilClient.is_unset(request.network_type):
            body['networkType'] = request.network_type
        if not UtilClient.is_unset(request.node_type):
            body['nodeType'] = request.node_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TriggerNetwork',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/network-trigger' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.TriggerNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    def trigger_network(self, instance_id, request):
        """
        @summary 开关ES集群及Kibana节点公私网访问
        

        @param request: TriggerNetworkRequest

        @return: TriggerNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.trigger_network_with_options(instance_id, request, headers, runtime)

    def uninstall_kibana_plugin_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Call the UninstallKibanaPlugin to uninstall the Kibana plug-in.
        

        @param request: UninstallKibanaPluginRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UninstallKibanaPluginResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UninstallKibanaPlugin',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/kibana-plugins/actions/uninstall' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UninstallKibanaPluginResponse(),
            self.call_api(params, req, runtime)
        )

    def uninstall_kibana_plugin(self, instance_id, request):
        """
        @summary Call the UninstallKibanaPlugin to uninstall the Kibana plug-in.
        

        @param request: UninstallKibanaPluginRequest

        @return: UninstallKibanaPluginResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.uninstall_kibana_plugin_with_options(instance_id, request, headers, runtime)

    def uninstall_logstash_plugin_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 卸载Logstash实例已安装的插件
        

        @param request: UninstallLogstashPluginRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UninstallLogstashPluginResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UninstallLogstashPlugin',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/plugins/actions/uninstall' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UninstallLogstashPluginResponse(),
            self.call_api(params, req, runtime)
        )

    def uninstall_logstash_plugin(self, instance_id, request):
        """
        @summary 卸载Logstash实例已安装的插件
        

        @param request: UninstallLogstashPluginRequest

        @return: UninstallLogstashPluginResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.uninstall_logstash_plugin_with_options(instance_id, request, headers, runtime)

    def uninstall_plugin_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Call UninstallPlugin to uninstall the preset plug-in.
        

        @param request: UninstallPluginRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UninstallPluginResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UninstallPlugin',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/plugins/actions/uninstall' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UninstallPluginResponse(),
            self.call_api(params, req, runtime)
        )

    def uninstall_plugin(self, instance_id, request):
        """
        @summary Call UninstallPlugin to uninstall the preset plug-in.
        

        @param request: UninstallPluginRequest

        @return: UninstallPluginResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.uninstall_plugin_with_options(instance_id, request, headers, runtime)

    def untag_resources_with_options(self, request, headers, runtime):
        """
        @summary 删除ES集群实例的用户可见标签
        
        @description When you call this operation, take note of the following items:
        You can only delete user tags.
        > User labels are manually added to instances by users. A system Tag is a tag that Alibaba Cloud services add to instances. System labels are divided into visible labels and invisible labels.
        If you delete a resource tag relationship that is not associated with any resources, you must delete the tags.
        

        @param request: UntagResourcesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        """
        @summary 删除ES集群实例的用户可见标签
        
        @description When you call this operation, take note of the following items:
        You can only delete user tags.
        > User labels are manually added to instances by users. A system Tag is a tag that Alibaba Cloud services add to instances. System labels are divided into visible labels and invisible labels.
        If you delete a resource tag relationship that is not associated with any resources, you must delete the tags.
        

        @param request: UntagResourcesRequest

        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    def update_admin_password_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 修改ES集群密码
        
        @description 5A2CFF0E-5718-45B5-9D4D-70B3FF\\\\*\\*\\*\
        

        @param request: UpdateAdminPasswordRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAdminPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.es_admin_password):
            body['esAdminPassword'] = request.es_admin_password
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAdminPassword',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/admin-pwd' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateAdminPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def update_admin_password(self, instance_id, request):
        """
        @summary 修改ES集群密码
        
        @description 5A2CFF0E-5718-45B5-9D4D-70B3FF\\\\*\\*\\*\
        

        @param request: UpdateAdminPasswordRequest

        @return: UpdateAdminPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_admin_password_with_options(instance_id, request, headers, runtime)

    def update_advanced_setting_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Call UpdateAdvancedSetting to change the garbage collector configuration for the specified instance.
        

        @param request: UpdateAdvancedSettingRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAdvancedSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateAdvancedSetting',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/update-advanced-setting' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateAdvancedSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def update_advanced_setting(self, instance_id, request):
        """
        @summary Call UpdateAdvancedSetting to change the garbage collector configuration for the specified instance.
        

        @param request: UpdateAdvancedSettingRequest

        @return: UpdateAdvancedSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_advanced_setting_with_options(instance_id, request, headers, runtime)

    def update_aliws_dict_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Updates the dictionary file of the analysis-aliws plug-in.
        
        @description Before you call this operation, take note of the following items:
        Elasticsearch V5.X clusters do not support the analysis-aliws plug-in.
        If the dictionary file is stored in an Object Storage Service (OSS) bucket, you must make sure that the access control list (ACL) of the bucket is public read.
        If you do not set sourceType to ORIGIN for an uploaded dictionary file, the file will be deleted after you call this operation.
        

        @param request: UpdateAliwsDictRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAliwsDictResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateAliwsDict',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/aliws-dict' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateAliwsDictResponse(),
            self.call_api(params, req, runtime)
        )

    def update_aliws_dict(self, instance_id, request):
        """
        @summary Updates the dictionary file of the analysis-aliws plug-in.
        
        @description Before you call this operation, take note of the following items:
        Elasticsearch V5.X clusters do not support the analysis-aliws plug-in.
        If the dictionary file is stored in an Object Storage Service (OSS) bucket, you must make sure that the access control list (ACL) of the bucket is public read.
        If you do not set sourceType to ORIGIN for an uploaded dictionary file, the file will be deleted after you call this operation.
        

        @param request: UpdateAliwsDictRequest

        @return: UpdateAliwsDictResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_aliws_dict_with_options(instance_id, request, headers, runtime)

    def update_apm_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 修改APM实规格配置
        

        @param request: UpdateApmRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateApmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.output_es):
            body['outputES'] = request.output_es
        if not UtilClient.is_unset(request.output_espassword):
            body['outputESPassword'] = request.output_espassword
        if not UtilClient.is_unset(request.output_esuser_name):
            body['outputESUserName'] = request.output_esuser_name
        if not UtilClient.is_unset(request.token):
            body['token'] = request.token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateApm',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/apm/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateApmResponse(),
            self.call_api(params, req, runtime)
        )

    def update_apm(self, instance_id, request):
        """
        @summary 修改APM实规格配置
        

        @param request: UpdateApmRequest

        @return: UpdateApmResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_apm_with_options(instance_id, request, headers, runtime)

    def update_black_ips_with_options(self, instance_id, request, headers, runtime):
        """
        @deprecated OpenAPI UpdateBlackIps is deprecated
        
        @summary 修改ES实例访问黑名单，已废弃
        

        @param request: UpdateBlackIpsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateBlackIpsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBlackIps',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/black-ips' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateBlackIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_black_ips(self, instance_id, request):
        """
        @deprecated OpenAPI UpdateBlackIps is deprecated
        
        @summary 修改ES实例访问黑名单，已废弃
        

        @param request: UpdateBlackIpsRequest

        @return: UpdateBlackIpsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_black_ips_with_options(instance_id, request, headers, runtime)

    def update_collector_with_options(self, res_id, request, headers, runtime):
        """
        @summary Updates the configurations of a shipper.
        

        @param request: UpdateCollectorRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateCollectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateCollector',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/collectors/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(res_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    def update_collector(self, res_id, request):
        """
        @summary Updates the configurations of a shipper.
        

        @param request: UpdateCollectorRequest

        @return: UpdateCollectorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_collector_with_options(res_id, request, headers, runtime)

    def update_collector_name_with_options(self, res_id, request, headers, runtime):
        """
        @summary Changes the name of a shipper.
        

        @param request: UpdateCollectorNameRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateCollectorNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateCollectorName',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/collectors/%s/actions/rename' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(res_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateCollectorNameResponse(),
            self.call_api(params, req, runtime)
        )

    def update_collector_name(self, res_id, request):
        """
        @summary Changes the name of a shipper.
        

        @param request: UpdateCollectorNameRequest

        @return: UpdateCollectorNameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_collector_name_with_options(res_id, request, headers, runtime)

    def update_component_index_with_options(self, instance_id, name, request, headers, runtime):
        """
        @summary 修改ES集群动态索引
        

        @param request: UpdateComponentIndexRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateComponentIndexResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.meta):
            body['_meta'] = request.meta
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateComponentIndex',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/component-index/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(name))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateComponentIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def update_component_index(self, instance_id, name, request):
        """
        @summary 修改ES集群动态索引
        

        @param request: UpdateComponentIndexRequest

        @return: UpdateComponentIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_component_index_with_options(instance_id, name, request, headers, runtime)

    def update_description_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 修改elasticsearch实例名称名称
        

        @param request: UpdateDescriptionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDescription',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/description' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_description(self, instance_id, request):
        """
        @summary 修改elasticsearch实例名称名称
        

        @param request: UpdateDescriptionRequest

        @return: UpdateDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_description_with_options(instance_id, request, headers, runtime)

    def update_diagnosis_settings_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Call UpdateDiagnosisSettings to update the instance of intelligent operation&maintenance (O&M) scene settings.
        

        @param request: UpdateDiagnosisSettingsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateDiagnosisSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateDiagnosisSettings',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/diagnosis/instances/%s/settings' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateDiagnosisSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_diagnosis_settings(self, instance_id, request):
        """
        @summary Call UpdateDiagnosisSettings to update the instance of intelligent operation&maintenance (O&M) scene settings.
        

        @param request: UpdateDiagnosisSettingsRequest

        @return: UpdateDiagnosisSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_diagnosis_settings_with_options(instance_id, request, headers, runtime)

    def update_dict_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Updates a dictionary of an Elasticsearch cluster.
        
        @description Before you call this operation, take note of the following items:
        If the dictionary file is stored in an Object Storage Service (OSS) bucket, you must make sure that the access control list (ACL) of the bucket is public read.
        If you do not set sourceType to ORIGIN for an uploaded dictionary file, the file will be deleted after you call this operation.
        

        @param request: UpdateDictRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateDictResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateDict',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/dict' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateDictResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dict(self, instance_id, request):
        """
        @summary Updates a dictionary of an Elasticsearch cluster.
        
        @description Before you call this operation, take note of the following items:
        If the dictionary file is stored in an Object Storage Service (OSS) bucket, you must make sure that the access control list (ACL) of the bucket is public read.
        If you do not set sourceType to ORIGIN for an uploaded dictionary file, the file will be deleted after you call this operation.
        

        @param request: UpdateDictRequest

        @return: UpdateDictResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_dict_with_options(instance_id, request, headers, runtime)

    def update_dynamic_settings_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 修改集群动态配置
        

        @param request: UpdateDynamicSettingsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateDynamicSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.mode):
            query['mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateDynamicSettings',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/dynamic-settings' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateDynamicSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dynamic_settings(self, instance_id, request):
        """
        @summary 修改集群动态配置
        

        @param request: UpdateDynamicSettingsRequest

        @return: UpdateDynamicSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_dynamic_settings_with_options(instance_id, request, headers, runtime)

    def update_extend_config_with_options(self, instance_id, request, headers, runtime):
        """

        @param request: UpdateExtendConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateExtendConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateExtendConfig',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/extend-configs/actions/update' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateExtendConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_extend_config(self, instance_id, request):
        """

        @param request: UpdateExtendConfigRequest

        @return: UpdateExtendConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_extend_config_with_options(instance_id, request, headers, runtime)

    def update_extendfiles_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Updates the driver files of a Logstash cluster.
        
        @description When you call this operation, take note of the following items: You can call this operation only to delete the driver files that are uploaded to a Logstash cluster in the Alibaba Cloud Management Console. You can add or modify driver files only in the Alibaba Cloud Management Console.
        

        @param request: UpdateExtendfilesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateExtendfilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateExtendfiles',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/extendfiles' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateExtendfilesResponse(),
            self.call_api(params, req, runtime)
        )

    def update_extendfiles(self, instance_id, request):
        """
        @summary Updates the driver files of a Logstash cluster.
        
        @description When you call this operation, take note of the following items: You can call this operation only to delete the driver files that are uploaded to a Logstash cluster in the Alibaba Cloud Management Console. You can add or modify driver files only in the Alibaba Cloud Management Console.
        

        @param request: UpdateExtendfilesRequest

        @return: UpdateExtendfilesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_extendfiles_with_options(instance_id, request, headers, runtime)

    def update_hot_ik_dicts_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Performs a rolling update for the IK dictionaries of an Elasticsearch cluster.
        
        @description Before you call this operation, take note of the following items:
        If the dictionary file is stored in an Object Storage Service (OSS) bucket, you must make sure that the access control list (ACL) of the bucket is public read.
        If you do not set sourceType to ORIGIN for an uploaded dictionary file, the file will be deleted after you call this operation.
        

        @param request: UpdateHotIkDictsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateHotIkDictsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateHotIkDicts',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/ik-hot-dict' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateHotIkDictsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_hot_ik_dicts(self, instance_id, request):
        """
        @summary Performs a rolling update for the IK dictionaries of an Elasticsearch cluster.
        
        @description Before you call this operation, take note of the following items:
        If the dictionary file is stored in an Object Storage Service (OSS) bucket, you must make sure that the access control list (ACL) of the bucket is public read.
        If you do not set sourceType to ORIGIN for an uploaded dictionary file, the file will be deleted after you call this operation.
        

        @param request: UpdateHotIkDictsRequest

        @return: UpdateHotIkDictsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_hot_ik_dicts_with_options(instance_id, request, headers, runtime)

    def update_ilmpolicy_with_options(self, instance_id, policy_name, request, headers, runtime):
        """
        @summary 修改ES集群索引生命周期策略
        

        @param request: UpdateILMPolicyRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateILMPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateILMPolicy',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/ilm-policies/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(policy_name))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateILMPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_ilmpolicy(self, instance_id, policy_name, request):
        """
        @summary 修改ES集群索引生命周期策略
        

        @param request: UpdateILMPolicyRequest

        @return: UpdateILMPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_ilmpolicy_with_options(instance_id, policy_name, request, headers, runtime)

    def update_index_template_with_options(self, instance_id, index_template, request, headers, runtime):
        """
        @summary 修改ES集群索引模版配置
        

        @param request: UpdateIndexTemplateRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateIndexTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateIndexTemplate',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/index-templates/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(index_template))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateIndexTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_index_template(self, instance_id, index_template, request):
        """
        @summary 修改ES集群索引模版配置
        

        @param request: UpdateIndexTemplateRequest

        @return: UpdateIndexTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_index_template_with_options(instance_id, index_template, request, headers, runtime)

    def update_instance_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 修改ES集群节点配置
        
        @description es-cn-n6w1ptcb30009\\\\*\\*\\*\
        

        @param request: UpdateInstanceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        if not UtilClient.is_unset(request.order_action_type):
            query['orderActionType'] = request.order_action_type
        body = {}
        if not UtilClient.is_unset(request.client_node_configuration):
            body['clientNodeConfiguration'] = request.client_node_configuration
        if not UtilClient.is_unset(request.elastic_data_node_configuration):
            body['elasticDataNodeConfiguration'] = request.elastic_data_node_configuration
        if not UtilClient.is_unset(request.instance_category):
            body['instanceCategory'] = request.instance_category
        if not UtilClient.is_unset(request.kibana_configuration):
            body['kibanaConfiguration'] = request.kibana_configuration
        if not UtilClient.is_unset(request.master_configuration):
            body['masterConfiguration'] = request.master_configuration
        if not UtilClient.is_unset(request.node_amount):
            body['nodeAmount'] = request.node_amount
        if not UtilClient.is_unset(request.node_spec):
            body['nodeSpec'] = request.node_spec
        if not UtilClient.is_unset(request.warm_node_configuration):
            body['warmNodeConfiguration'] = request.warm_node_configuration
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance(self, instance_id, request):
        """
        @summary 修改ES集群节点配置
        
        @description es-cn-n6w1ptcb30009\\\\*\\*\\*\
        

        @param request: UpdateInstanceRequest

        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(instance_id, request, headers, runtime)

    def update_instance_charge_type_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Call UpdateInstanceChargeType to change the billing method of a pay-as-you-go instance to subscription.
        

        @param request: UpdateInstanceChargeTypeRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateInstanceChargeTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateInstanceChargeType',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/convert-pay-type' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateInstanceChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance_charge_type(self, instance_id, request):
        """
        @summary Call UpdateInstanceChargeType to change the billing method of a pay-as-you-go instance to subscription.
        

        @param request: UpdateInstanceChargeTypeRequest

        @return: UpdateInstanceChargeTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_charge_type_with_options(instance_id, request, headers, runtime)

    def update_instance_settings_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Call UpdateInstanceSettings to update the YML configuration of a specified instance.
        
        @description When you call this operation, take note of the following items:
        When the instance is in the activating, invalid, or inactive state, you cannot update the configuration.
        

        @param request: UpdateInstanceSettingsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateInstanceSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateInstanceSettings',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/instance-settings' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateInstanceSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance_settings(self, instance_id, request):
        """
        @summary Call UpdateInstanceSettings to update the YML configuration of a specified instance.
        
        @description When you call this operation, take note of the following items:
        When the instance is in the activating, invalid, or inactive state, you cannot update the configuration.
        

        @param request: UpdateInstanceSettingsRequest

        @return: UpdateInstanceSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_settings_with_options(instance_id, request, headers, runtime)

    def update_kibana_pvl_network_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 更新kibana私网链接
        

        @param request: UpdateKibanaPvlNetworkRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateKibanaPvlNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pvl_id):
            query['pvlId'] = request.pvl_id
        body = {}
        if not UtilClient.is_unset(request.endpoint_name):
            body['endpointName'] = request.endpoint_name
        if not UtilClient.is_unset(request.security_groups):
            body['securityGroups'] = request.security_groups
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateKibanaPvlNetwork',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/update-kibana-private' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateKibanaPvlNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    def update_kibana_pvl_network(self, instance_id, request):
        """
        @summary 更新kibana私网链接
        

        @param request: UpdateKibanaPvlNetworkRequest

        @return: UpdateKibanaPvlNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_kibana_pvl_network_with_options(instance_id, request, headers, runtime)

    def update_kibana_settings_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Call UpdateKibanaSettings to modify the Kibana configuration. Currently, you can only modify the Kibana language configuration.
        

        @param request: UpdateKibanaSettingsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateKibanaSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateKibanaSettings',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/update-kibana-settings' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateKibanaSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_kibana_settings(self, instance_id, request):
        """
        @summary Call UpdateKibanaSettings to modify the Kibana configuration. Currently, you can only modify the Kibana language configuration.
        

        @param request: UpdateKibanaSettingsRequest

        @return: UpdateKibanaSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_kibana_settings_with_options(instance_id, request, headers, runtime)

    def update_kibana_white_ips_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Updates an IP address whitelist for access to the Kibana console of a specified Elasticsearch cluster.
        
        @description    Before you call this operation, you must make sure that the cluster is not in the activating, invalid, or inactive state.
        You can update an IP address whitelist by using the following parameters:
        kibanaIPWhitelist
        modifyMode and whiteIpGroup
        You cannot specify private IP addresses for public IP address whitelists and cannot specify public IP addresses for private IP address whitelists.
        

        @param request: UpdateKibanaWhiteIpsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateKibanaWhiteIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        body = {}
        if not UtilClient.is_unset(request.kibana_ipwhitelist):
            body['kibanaIPWhitelist'] = request.kibana_ipwhitelist
        if not UtilClient.is_unset(request.white_ip_group):
            body['whiteIpGroup'] = request.white_ip_group
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateKibanaWhiteIps',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/kibana-white-ips' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateKibanaWhiteIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_kibana_white_ips(self, instance_id, request):
        """
        @summary Updates an IP address whitelist for access to the Kibana console of a specified Elasticsearch cluster.
        
        @description    Before you call this operation, you must make sure that the cluster is not in the activating, invalid, or inactive state.
        You can update an IP address whitelist by using the following parameters:
        kibanaIPWhitelist
        modifyMode and whiteIpGroup
        You cannot specify private IP addresses for public IP address whitelists and cannot specify public IP addresses for private IP address whitelists.
        

        @param request: UpdateKibanaWhiteIpsRequest

        @return: UpdateKibanaWhiteIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_kibana_white_ips_with_options(instance_id, request, headers, runtime)

    def update_logstash_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 修改Logstash节点规格磁盘配置
        

        @param request: UpdateLogstashRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateLogstashResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.node_amount):
            body['nodeAmount'] = request.node_amount
        if not UtilClient.is_unset(request.node_spec):
            body['nodeSpec'] = request.node_spec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogstash',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateLogstashResponse(),
            self.call_api(params, req, runtime)
        )

    def update_logstash(self, instance_id, request):
        """
        @summary 修改Logstash节点规格磁盘配置
        

        @param request: UpdateLogstashRequest

        @return: UpdateLogstashResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logstash_with_options(instance_id, request, headers, runtime)

    def update_logstash_charge_type_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Switches the billing method of a Logstash cluster from pay-as-you-go to subscription.
        

        @param request: UpdateLogstashChargeTypeRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateLogstashChargeTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateLogstashChargeType',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/actions/convert-pay-type' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateLogstashChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_logstash_charge_type(self, instance_id, request):
        """
        @summary Switches the billing method of a Logstash cluster from pay-as-you-go to subscription.
        

        @param request: UpdateLogstashChargeTypeRequest

        @return: UpdateLogstashChargeTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logstash_charge_type_with_options(instance_id, request, headers, runtime)

    def update_logstash_description_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Changes the name of a specified Logstash cluster.
        
        @description When you call this operation, take note of the following items: You cannot change the name of a cluster that is in the activating, invalid, or inactive state.
        

        @param request: UpdateLogstashDescriptionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateLogstashDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogstashDescription',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/description' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateLogstashDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_logstash_description(self, instance_id, request):
        """
        @summary Changes the name of a specified Logstash cluster.
        
        @description When you call this operation, take note of the following items: You cannot change the name of a cluster that is in the activating, invalid, or inactive state.
        

        @param request: UpdateLogstashDescriptionRequest

        @return: UpdateLogstashDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logstash_description_with_options(instance_id, request, headers, runtime)

    def update_logstash_settings_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Updates the configuration of a specified Logstash cluster.
        
        @description When you call this operation, take note of the following items:
        If the instance is in the Active (activating), Invalid (invalid), and Inactive (inactive) state, the information cannot be updated.
        

        @param request: UpdateLogstashSettingsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateLogstashSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateLogstashSettings',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/instance-settings' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateLogstashSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_logstash_settings(self, instance_id, request):
        """
        @summary Updates the configuration of a specified Logstash cluster.
        
        @description When you call this operation, take note of the following items:
        If the instance is in the Active (activating), Invalid (invalid), and Inactive (inactive) state, the information cannot be updated.
        

        @param request: UpdateLogstashSettingsRequest

        @return: UpdateLogstashSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logstash_settings_with_options(instance_id, request, headers, runtime)

    def update_pipeline_management_config_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 修改Logstash管道配置
        

        @param request: UpdatePipelineManagementConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdatePipelineManagementConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.endpoints):
            body['endpoints'] = request.endpoints
        if not UtilClient.is_unset(request.es_instance_id):
            body['esInstanceId'] = request.es_instance_id
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.pipeline_ids):
            body['pipelineIds'] = request.pipeline_ids
        if not UtilClient.is_unset(request.pipeline_management_type):
            body['pipelineManagementType'] = request.pipeline_management_type
        if not UtilClient.is_unset(request.user_name):
            body['userName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePipelineManagementConfig',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/pipeline-management-config' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePipelineManagementConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_pipeline_management_config(self, instance_id, request):
        """
        @summary 修改Logstash管道配置
        

        @param request: UpdatePipelineManagementConfigRequest

        @return: UpdatePipelineManagementConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipeline_management_config_with_options(instance_id, request, headers, runtime)

    def update_pipelines_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Updates a pipeline of a Logstash cluster.
        

        @param request: UpdatePipelinesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdatePipelinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdatePipelines',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/pipelines' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    def update_pipelines(self, instance_id, request):
        """
        @summary Updates a pipeline of a Logstash cluster.
        

        @param request: UpdatePipelinesRequest

        @return: UpdatePipelinesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipelines_with_options(instance_id, request, headers, runtime)

    def update_private_network_white_ips_with_options(self, instance_id, request, headers, runtime):
        """
        @summary ## RequestBody
        | Property | Type | Required | Example | Description |
        | -------- | ---- | -------- | ------- | ----------- |
        | privateNetworkIpWhiteList | List<String> | No | ["0.0.XX.XX","10.2.XX.XX","192.168.XX.XX/25"] | The list of IP address whitelists. This parameter is available if whiteIpGroup is left empty. The value of this parameter updates the IP address whitelist configurations in the Default whitelist group.
        You cannot configure both privateNetworkIpWhiteList and whiteIpGroup. |
        | whiteIpGroup | Object | No |  | You can update the whitelist configurations of an instance by using a whitelist group. You can update only one whitelist group.
        You cannot configure both privateNetworkIpWhiteList and whiteIpGroup. |
        | └ groupName | String | No | test_group_name | The group name of the whitelist group. This parameter is required if the whiteIpGroup parameter is optional. |
        | └ ips | List<String> | No | ["0.0.0.0", "10.2.XX.XX"] | The list of IP addresses in the whitelist group. This parameter is required if the whiteIpGroup parameter is optional. |
        > *Notice**  The addition and deletion of whitelist groups are implemented by calling modifyMode to Cover. Delete and Append cannot add or delete whitelist groups at the same time. You can only modify the IP address list in the whitelist group. Take note of the following items: - If the modifyMode parameter is set to Cover, the whitelist group is deleted if ips is empty. If groupName is not in the list of existing whitelist group names, a whitelist group is created.
        - If the modifyMode parameter is set to Delete, you must retain at least one IP address for the deleted ips.
        - If the modifyMode parameter is set to Append, make sure that the whitelist group name has been created. Otherwise, the NotFound error message appears.
        
        @description >  In the following returned example, only the parameters in the returned data list are guaranteed to be included, and the parameters not mentioned are for reference only. For more information about the parameters, see [ListInstance](https://help.aliyun.com/document_detail/142230.html). You cannot force a dependency in a program to get these parameters.
        

        @param request: UpdatePrivateNetworkWhiteIpsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdatePrivateNetworkWhiteIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdatePrivateNetworkWhiteIps',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/private-network-white-ips' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePrivateNetworkWhiteIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_private_network_white_ips(self, instance_id, request):
        """
        @summary ## RequestBody
        | Property | Type | Required | Example | Description |
        | -------- | ---- | -------- | ------- | ----------- |
        | privateNetworkIpWhiteList | List<String> | No | ["0.0.XX.XX","10.2.XX.XX","192.168.XX.XX/25"] | The list of IP address whitelists. This parameter is available if whiteIpGroup is left empty. The value of this parameter updates the IP address whitelist configurations in the Default whitelist group.
        You cannot configure both privateNetworkIpWhiteList and whiteIpGroup. |
        | whiteIpGroup | Object | No |  | You can update the whitelist configurations of an instance by using a whitelist group. You can update only one whitelist group.
        You cannot configure both privateNetworkIpWhiteList and whiteIpGroup. |
        | └ groupName | String | No | test_group_name | The group name of the whitelist group. This parameter is required if the whiteIpGroup parameter is optional. |
        | └ ips | List<String> | No | ["0.0.0.0", "10.2.XX.XX"] | The list of IP addresses in the whitelist group. This parameter is required if the whiteIpGroup parameter is optional. |
        > *Notice**  The addition and deletion of whitelist groups are implemented by calling modifyMode to Cover. Delete and Append cannot add or delete whitelist groups at the same time. You can only modify the IP address list in the whitelist group. Take note of the following items: - If the modifyMode parameter is set to Cover, the whitelist group is deleted if ips is empty. If groupName is not in the list of existing whitelist group names, a whitelist group is created.
        - If the modifyMode parameter is set to Delete, you must retain at least one IP address for the deleted ips.
        - If the modifyMode parameter is set to Append, make sure that the whitelist group name has been created. Otherwise, the NotFound error message appears.
        
        @description >  In the following returned example, only the parameters in the returned data list are guaranteed to be included, and the parameters not mentioned are for reference only. For more information about the parameters, see [ListInstance](https://help.aliyun.com/document_detail/142230.html). You cannot force a dependency in a program to get these parameters.
        

        @param request: UpdatePrivateNetworkWhiteIpsRequest

        @return: UpdatePrivateNetworkWhiteIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_private_network_white_ips_with_options(instance_id, request, headers, runtime)

    def update_public_network_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Call UpdatePublicNetwork to open or close the public network address of the specified elasticsearch instance.
        
        @description When you call this operation, take note of the following items:
        When the instance is in the activating, invalid, or inactive state, its configuration cannot be updated.
        

        @param request: UpdatePublicNetworkRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdatePublicNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdatePublicNetwork',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/public-network' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePublicNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    def update_public_network(self, instance_id, request):
        """
        @summary Call UpdatePublicNetwork to open or close the public network address of the specified elasticsearch instance.
        
        @description When you call this operation, take note of the following items:
        When the instance is in the activating, invalid, or inactive state, its configuration cannot be updated.
        

        @param request: UpdatePublicNetworkRequest

        @return: UpdatePublicNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_public_network_with_options(instance_id, request, headers, runtime)

    def update_public_white_ips_with_options(self, instance_id, request, headers, runtime):
        """
        @summary ## RequestBody
        | Property | Type | Required | Example | Description |
        | -------- | ---- | -------- | ------- | ----------- |
        | publicIpWhitelist | List<String> | Yes | ["0.0.0.0/0","0.0.0.0/1"] | The list of IP address whitelists. This parameter is available if whiteIpGroup is left empty. The value of this parameter updates the IP address whitelist configurations in the Default whitelist group.
        You cannot configure both publicIpWhitelist and whiteIpGroup. |
        | whiteIpGroup | Object | No |  | You can update the whitelist configurations of an instance by using a whitelist group. You can update only one whitelist group.
        You cannot configure both publicIpWhitelist and whiteIpGroup. |
        | └ groupName | String | No | test_group_name | The group name of the whitelist group. This parameter is required if the whiteIpGroup parameter is optional. |
        | └ ips | List<String> | No | ["0.0.0.0", "10.2.XX.XX"] | The list of IP addresses in the whitelist group. This parameter is required if the whiteIpGroup parameter is optional. |
        > *Notice**  The addition and deletion of whitelist groups are implemented by calling modifyMode to Cover. Delete and Append cannot add or delete whitelist groups at the same time. You can only modify the IP address list in the whitelist group. Take note of the following items: - If the modifyMode parameter is set to Cover, the whitelist group is deleted if ips is empty. If groupName is not in the list of existing whitelist group names, a whitelist group is created.
        - If the modifyMode parameter is set to Delete, you must retain at least one IP address for the deleted ips.
        - If the modifyMode parameter is set to Append, make sure that the whitelist group name has been created. Otherwise, the NotFound error message appears.
        
        @description >  In the following example, only the parameters in the returned data list are guaranteed to be included. The parameters that are not mentioned are for reference only. For more information about the parameters, see [ListInstance](https://help.aliyun.com/document_detail/142230.html). You cannot force a dependency in a program to get these parameters.
        

        @param request: UpdatePublicWhiteIpsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdatePublicWhiteIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdatePublicWhiteIps',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/public-white-ips' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePublicWhiteIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_public_white_ips(self, instance_id, request):
        """
        @summary ## RequestBody
        | Property | Type | Required | Example | Description |
        | -------- | ---- | -------- | ------- | ----------- |
        | publicIpWhitelist | List<String> | Yes | ["0.0.0.0/0","0.0.0.0/1"] | The list of IP address whitelists. This parameter is available if whiteIpGroup is left empty. The value of this parameter updates the IP address whitelist configurations in the Default whitelist group.
        You cannot configure both publicIpWhitelist and whiteIpGroup. |
        | whiteIpGroup | Object | No |  | You can update the whitelist configurations of an instance by using a whitelist group. You can update only one whitelist group.
        You cannot configure both publicIpWhitelist and whiteIpGroup. |
        | └ groupName | String | No | test_group_name | The group name of the whitelist group. This parameter is required if the whiteIpGroup parameter is optional. |
        | └ ips | List<String> | No | ["0.0.0.0", "10.2.XX.XX"] | The list of IP addresses in the whitelist group. This parameter is required if the whiteIpGroup parameter is optional. |
        > *Notice**  The addition and deletion of whitelist groups are implemented by calling modifyMode to Cover. Delete and Append cannot add or delete whitelist groups at the same time. You can only modify the IP address list in the whitelist group. Take note of the following items: - If the modifyMode parameter is set to Cover, the whitelist group is deleted if ips is empty. If groupName is not in the list of existing whitelist group names, a whitelist group is created.
        - If the modifyMode parameter is set to Delete, you must retain at least one IP address for the deleted ips.
        - If the modifyMode parameter is set to Append, make sure that the whitelist group name has been created. Otherwise, the NotFound error message appears.
        
        @description >  In the following example, only the parameters in the returned data list are guaranteed to be included. The parameters that are not mentioned are for reference only. For more information about the parameters, see [ListInstance](https://help.aliyun.com/document_detail/142230.html). You cannot force a dependency in a program to get these parameters.
        

        @param request: UpdatePublicWhiteIpsRequest

        @return: UpdatePublicWhiteIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_public_white_ips_with_options(instance_id, request, headers, runtime)

    def update_read_write_policy_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 更改ES集群高可用策略
        

        @param request: UpdateReadWritePolicyRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateReadWritePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateReadWritePolicy',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/update-read-write-policy' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateReadWritePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_read_write_policy(self, instance_id, request):
        """
        @summary 更改ES集群高可用策略
        

        @param request: UpdateReadWritePolicyRequest

        @return: UpdateReadWritePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_read_write_policy_with_options(instance_id, request, headers, runtime)

    def update_snapshot_setting_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Call UpdateSnapshotSetting to update the data backup configuration of the specified instance.
        

        @param request: UpdateSnapshotSettingRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateSnapshotSettingResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateSnapshotSetting',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/snapshot-setting' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateSnapshotSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def update_snapshot_setting(self, instance_id, request):
        """
        @summary Call UpdateSnapshotSetting to update the data backup configuration of the specified instance.
        

        @param request: UpdateSnapshotSettingRequest

        @return: UpdateSnapshotSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_snapshot_setting_with_options(instance_id, request, headers, runtime)

    def update_synonyms_dicts_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Updates the synonym dictionaries of an Elasticsearch cluster.
        
        @description Before you call this operation, take note of the following items:
        If the dictionary file is stored in an Object Storage Service (OSS) bucket, you must make sure that the access control list (ACL) of the bucket is public read.
        If you do not set sourceType to ORIGIN for an uploaded dictionary file, the file will be deleted after you call this operation.
        

        @param request: UpdateSynonymsDictsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateSynonymsDictsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateSynonymsDicts',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/synonymsDict' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateSynonymsDictsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_synonyms_dicts(self, instance_id, request):
        """
        @summary Updates the synonym dictionaries of an Elasticsearch cluster.
        
        @description Before you call this operation, take note of the following items:
        If the dictionary file is stored in an Object Storage Service (OSS) bucket, you must make sure that the access control list (ACL) of the bucket is public read.
        If you do not set sourceType to ORIGIN for an uploaded dictionary file, the file will be deleted after you call this operation.
        

        @param request: UpdateSynonymsDictsRequest

        @return: UpdateSynonymsDictsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_synonyms_dicts_with_options(instance_id, request, headers, runtime)

    def update_template_with_options(self, instance_id, template_name, request, headers, runtime):
        """

        @param request: UpdateTemplateRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/templates/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(template_name))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_template(self, instance_id, template_name, request):
        """

        @param request: UpdateTemplateRequest

        @return: UpdateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_template_with_options(instance_id, template_name, request, headers, runtime)

    def update_white_ips_with_options(self, instance_id, request, headers, runtime):
        """
        @summary >  If you want to add an IP address whitelist, you can set the modifyMode parameter only to Cover. If you set this parameter to Delete or Append, you can only update an IP address whitelist.
        If you set the modifyMode parameter to Cover and leave the ips parameter empty, the system deletes the specified whitelist. If the whitelist specified by using the groupName parameter does not exist, the system creates such a whitelist.
        If you set the modifyMode parameter to Delete, at least one IP address must be retained for the specified whitelist.
        If you set the modifyMode parameter to Append, you must make sure that the specified whitelist exists. Otherwise, the system reports the NotFound error.
        
        @description > For more information about the parameters displayed in the following sample code but not provided in the preceding tables, see [ListInstance](https://help.aliyun.com/document_detail/142230.html). You cannot force your program to obtain these parameters.
        

        @param request: UpdateWhiteIpsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateWhiteIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        body = {}
        if not UtilClient.is_unset(request.es_ipwhitelist):
            body['esIPWhitelist'] = request.es_ipwhitelist
        if not UtilClient.is_unset(request.white_ip_group):
            body['whiteIpGroup'] = request.white_ip_group
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWhiteIps',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/white-ips' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateWhiteIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_white_ips(self, instance_id, request):
        """
        @summary >  If you want to add an IP address whitelist, you can set the modifyMode parameter only to Cover. If you set this parameter to Delete or Append, you can only update an IP address whitelist.
        If you set the modifyMode parameter to Cover and leave the ips parameter empty, the system deletes the specified whitelist. If the whitelist specified by using the groupName parameter does not exist, the system creates such a whitelist.
        If you set the modifyMode parameter to Delete, at least one IP address must be retained for the specified whitelist.
        If you set the modifyMode parameter to Append, you must make sure that the specified whitelist exists. Otherwise, the system reports the NotFound error.
        
        @description > For more information about the parameters displayed in the following sample code but not provided in the preceding tables, see [ListInstance](https://help.aliyun.com/document_detail/142230.html). You cannot force your program to obtain these parameters.
        

        @param request: UpdateWhiteIpsRequest

        @return: UpdateWhiteIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_white_ips_with_options(instance_id, request, headers, runtime)

    def update_xpack_monitor_config_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 修改Logstash实例的X-Pack监控报警配置。
        

        @param request: UpdateXpackMonitorConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateXpackMonitorConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.endpoints):
            body['endpoints'] = request.endpoints
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.user_name):
            body['userName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateXpackMonitorConfig',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/xpack-monitor-config' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateXpackMonitorConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_xpack_monitor_config(self, instance_id, request):
        """
        @summary 修改Logstash实例的X-Pack监控报警配置。
        

        @param request: UpdateXpackMonitorConfigRequest

        @return: UpdateXpackMonitorConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_xpack_monitor_config_with_options(instance_id, request, headers, runtime)

    def upgrade_engine_version_with_options(self, instance_id, request, headers, runtime):
        """
        @summary ES集群版本升级
        
        @description 5A2CFF0E-5718-45B5-9D4D-70B3FF\\\\*\\*\\*\
        

        @param request: UpgradeEngineVersionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpgradeEngineVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.plugins):
            body['plugins'] = request.plugins
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeEngineVersion',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/upgrade-version' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpgradeEngineVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_engine_version(self, instance_id, request):
        """
        @summary ES集群版本升级
        
        @description 5A2CFF0E-5718-45B5-9D4D-70B3FF\\\\*\\*\\*\
        

        @param request: UpgradeEngineVersionRequest

        @return: UpgradeEngineVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_engine_version_with_options(instance_id, request, headers, runtime)

    def validate_connection_with_options(self, instance_id, request, headers, runtime):
        """
        @summary Tests the connectivity between a Logstash cluster and its associated Elasticsearch cluster when you configure the X-Pack Monitoring feature for the Logstash cluster.
        
        @description > Before you enable the X-Pack Monitoring feature for a Logstash cluster, you must associate the Logstash cluster with an Elasticsearch cluster. This way, you can view the monitoring data of the Logstash cluster in the Kibana console of the Elasticsearch cluster.
        

        @param request: ValidateConnectionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ValidateConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='ValidateConnection',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/validate-connection' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ValidateConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    def validate_connection(self, instance_id, request):
        """
        @summary Tests the connectivity between a Logstash cluster and its associated Elasticsearch cluster when you configure the X-Pack Monitoring feature for the Logstash cluster.
        
        @description > Before you enable the X-Pack Monitoring feature for a Logstash cluster, you must associate the Logstash cluster with an Elasticsearch cluster. This way, you can view the monitoring data of the Logstash cluster in the Kibana console of the Elasticsearch cluster.
        

        @param request: ValidateConnectionRequest

        @return: ValidateConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_connection_with_options(instance_id, request, headers, runtime)

    def validate_shrink_nodes_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 校验缩节点合法性
        

        @param request: ValidateShrinkNodesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ValidateShrinkNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='ValidateShrinkNodes',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/validate-shrink-nodes' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ValidateShrinkNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def validate_shrink_nodes(self, instance_id, request):
        """
        @summary 校验缩节点合法性
        

        @param request: ValidateShrinkNodesRequest

        @return: ValidateShrinkNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_shrink_nodes_with_options(instance_id, request, headers, runtime)

    def validate_slr_permission_with_options(self, request, headers, runtime):
        """

        @param request: ValidateSlrPermissionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ValidateSlrPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.rolename):
            query['rolename'] = request.rolename
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateSlrPermission',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/user/servicerolepermission',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ValidateSlrPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def validate_slr_permission(self, request):
        """

        @param request: ValidateSlrPermissionRequest

        @return: ValidateSlrPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_slr_permission_with_options(request, headers, runtime)

    def validate_transferable_nodes_with_options(self, instance_id, request, headers, runtime):
        """
        @summary 缩节点校验数据迁移合法性
        

        @param request: ValidateTransferableNodesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ValidateTransferableNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='ValidateTransferableNodes',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/validate-transfer-nodes' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ValidateTransferableNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def validate_transferable_nodes(self, instance_id, request):
        """
        @summary 缩节点校验数据迁移合法性
        

        @param request: ValidateTransferableNodesRequest

        @return: ValidateTransferableNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_transferable_nodes_with_options(instance_id, request, headers, runtime)

    def create_instance_with_options(self, request, headers, runtime):
        """
        @summary The configurations of dedicated master nodes.
        
        @description The configurations of warm nodes.
        

        @param request: CreateInstanceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.client_node_configuration):
            body['clientNodeConfiguration'] = request.client_node_configuration
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.elastic_data_node_configuration):
            body['elasticDataNodeConfiguration'] = request.elastic_data_node_configuration
        if not UtilClient.is_unset(request.es_admin_password):
            body['esAdminPassword'] = request.es_admin_password
        if not UtilClient.is_unset(request.es_version):
            body['esVersion'] = request.es_version
        if not UtilClient.is_unset(request.instance_category):
            body['instanceCategory'] = request.instance_category
        if not UtilClient.is_unset(request.kibana_configuration):
            body['kibanaConfiguration'] = request.kibana_configuration
        if not UtilClient.is_unset(request.master_configuration):
            body['masterConfiguration'] = request.master_configuration
        if not UtilClient.is_unset(request.network_config):
            body['networkConfig'] = request.network_config
        if not UtilClient.is_unset(request.node_amount):
            body['nodeAmount'] = request.node_amount
        if not UtilClient.is_unset(request.node_spec):
            body['nodeSpec'] = request.node_spec
        if not UtilClient.is_unset(request.payment_info):
            body['paymentInfo'] = request.payment_info
        if not UtilClient.is_unset(request.payment_type):
            body['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.warm_node_configuration):
            body['warmNodeConfiguration'] = request.warm_node_configuration
        if not UtilClient.is_unset(request.zone_count):
            body['zoneCount'] = request.zone_count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='createInstance',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance(self, request):
        """
        @summary The configurations of dedicated master nodes.
        
        @description The configurations of warm nodes.
        

        @param request: CreateInstanceRequest

        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)
