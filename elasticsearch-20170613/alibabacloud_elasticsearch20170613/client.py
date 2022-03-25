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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('elasticsearch', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def activate_zones(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.activate_zones_with_options(instance_id, request, headers, runtime)

    def activate_zones_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateZones',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/recover-zones' % TeaConverter.to_unicode(instance_id),
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

    def add_connectable_cluster(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_connectable_cluster_with_options(instance_id, request, headers, runtime)

    def add_connectable_cluster_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddConnectableCluster',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/connected-clusters' % TeaConverter.to_unicode(instance_id),
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

    def add_snapshot_repo(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_snapshot_repo_with_options(instance_id, headers, runtime)

    def add_snapshot_repo_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AddSnapshotRepo',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/snapshot-repos' % TeaConverter.to_unicode(instance_id),
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

    def cancel_deletion(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_deletion_with_options(instance_id, request, headers, runtime)

    def cancel_deletion_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/actions/cancel-deletion' % TeaConverter.to_unicode(instance_id),
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

    def cancel_logstash_deletion(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_logstash_deletion_with_options(instance_id, request, headers, runtime)

    def cancel_logstash_deletion_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/logstashes/%s/actions/cancel-deletion' % TeaConverter.to_unicode(instance_id),
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

    def cancel_task(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_task_with_options(instance_id, request, headers, runtime)

    def cancel_task_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/actions/cancel-task' % TeaConverter.to_unicode(instance_id),
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

    def capacity_plan(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.capacity_plan_with_options(request, headers, runtime)

    def capacity_plan_with_options(self, request, headers, runtime):
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

    def close_diagnosis(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.close_diagnosis_with_options(instance_id, request, headers, runtime)

    def close_diagnosis_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/diagnosis/instances/%s/actions/close-diagnosis' % TeaConverter.to_unicode(instance_id),
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

    def close_https(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.close_https_with_options(instance_id, request, headers, runtime)

    def close_https_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/actions/close-https' % TeaConverter.to_unicode(instance_id),
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

    def close_managed_index(self, instance_id, index, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.close_managed_index_with_options(instance_id, index, request, headers, runtime)

    def close_managed_index_with_options(self, instance_id, index, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        index = OpenApiUtilClient.get_encode_param(index)
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
            pathname='/openapi/instances/%s/indices/%s/close-managed' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(index)),
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

    def create_collector(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_collector_with_options(request, headers, runtime)

    def create_collector_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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

    def create_component_index(self, instance_id, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_component_index_with_options(instance_id, name, request, headers, runtime)

    def create_component_index_with_options(self, instance_id, name, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        name = OpenApiUtilClient.get_encode_param(name)
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
            pathname='/openapi/instances/%s/component-index/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(name)),
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

    def create_data_stream(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_data_stream_with_options(instance_id, request, headers, runtime)

    def create_data_stream_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataStream',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/data-streams' % TeaConverter.to_unicode(instance_id),
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

    def create_data_tasks(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_data_tasks_with_options(instance_id, request, headers, runtime)

    def create_data_tasks_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataTasks',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/data-task' % TeaConverter.to_unicode(instance_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateDataTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def create_ilmpolicy(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ilmpolicy_with_options(instance_id, request, headers, runtime)

    def create_ilmpolicy_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateILMPolicy',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/ilm-policies' % TeaConverter.to_unicode(instance_id),
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

    def create_index_template(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_index_template_with_options(instance_id, request, headers, runtime)

    def create_index_template_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIndexTemplate',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/index-templates' % TeaConverter.to_unicode(instance_id),
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

    def create_logstash(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_logstash_with_options(request, headers, runtime)

    def create_logstash_with_options(self, request, headers, runtime):
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

    def create_pipelines(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipelines_with_options(instance_id, request, headers, runtime)

    def create_pipelines_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePipelines',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/pipelines' % TeaConverter.to_unicode(instance_id),
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

    def create_snapshot(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_snapshot_with_options(instance_id, request, headers, runtime)

    def create_snapshot_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/snapshots' % TeaConverter.to_unicode(instance_id),
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

    def create_vpc_endpoint(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_vpc_endpoint_with_options(instance_id, request, headers, runtime)

    def create_vpc_endpoint_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/vpc-endpoints' % TeaConverter.to_unicode(instance_id),
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

    def deactivate_zones(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deactivate_zones_with_options(instance_id, request, headers, runtime)

    def deactivate_zones_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactivateZones',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/down-zones' % TeaConverter.to_unicode(instance_id),
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

    def delete_collector(self, res_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_collector_with_options(res_id, request, headers, runtime)

    def delete_collector_with_options(self, res_id, request, headers, runtime):
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
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
            pathname='/openapi/collectors/%s' % TeaConverter.to_unicode(res_id),
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

    def delete_component_index(self, instance_id, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_component_index_with_options(instance_id, name, headers, runtime)

    def delete_component_index_with_options(self, instance_id, name, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteComponentIndex',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/component-index/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(name)),
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

    def delete_connected_cluster(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_connected_cluster_with_options(instance_id, request, headers, runtime)

    def delete_connected_cluster_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/connected-clusters' % TeaConverter.to_unicode(instance_id),
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

    def delete_data_stream(self, instance_id, data_stream, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_data_stream_with_options(instance_id, data_stream, request, headers, runtime)

    def delete_data_stream_with_options(self, instance_id, data_stream, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        data_stream = OpenApiUtilClient.get_encode_param(data_stream)
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
            pathname='/openapi/instances/%s/data-streams/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(data_stream)),
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

    def delete_data_task(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_data_task_with_options(instance_id, request, headers, runtime)

    def delete_data_task_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/data-task' % TeaConverter.to_unicode(instance_id),
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

    def delete_deprecated_template(self, instance_id, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_deprecated_template_with_options(instance_id, name, headers, runtime)

    def delete_deprecated_template_with_options(self, instance_id, name, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDeprecatedTemplate',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/deprecated-templates/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(name)),
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

    def delete_ilmpolicy(self, instance_id, policy_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ilmpolicy_with_options(instance_id, policy_name, headers, runtime)

    def delete_ilmpolicy_with_options(self, instance_id, policy_name, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        policy_name = OpenApiUtilClient.get_encode_param(policy_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteILMPolicy',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/ilm-policies/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(policy_name)),
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

    def delete_index_template(self, instance_id, index_template):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_index_template_with_options(instance_id, index_template, headers, runtime)

    def delete_index_template_with_options(self, instance_id, index_template, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        index_template = OpenApiUtilClient.get_encode_param(index_template)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteIndexTemplate',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/index-templates/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(index_template)),
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

    def delete_instance(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, request, headers, runtime)

    def delete_instance_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s' % TeaConverter.to_unicode(instance_id),
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

    def delete_logstash(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_logstash_with_options(instance_id, request, headers, runtime)

    def delete_logstash_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/logstashes/%s' % TeaConverter.to_unicode(instance_id),
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

    def delete_pipelines(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_pipelines_with_options(instance_id, request, headers, runtime)

    def delete_pipelines_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/logstashes/%s/pipelines' % TeaConverter.to_unicode(instance_id),
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

    def delete_snapshot_repo(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_snapshot_repo_with_options(instance_id, request, headers, runtime)

    def delete_snapshot_repo_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/snapshot-repos' % TeaConverter.to_unicode(instance_id),
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

    def delete_vpc_endpoint(self, instance_id, endpoint_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_vpc_endpoint_with_options(instance_id, endpoint_id, request, headers, runtime)

    def delete_vpc_endpoint_with_options(self, instance_id, endpoint_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        endpoint_id = OpenApiUtilClient.get_encode_param(endpoint_id)
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
            pathname='/openapi/instances/%s/vpc-endpoints/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(endpoint_id)),
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

    def describe_ack_operator(self, cluster_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_ack_operator_with_options(cluster_id, headers, runtime)

    def describe_ack_operator_with_options(self, cluster_id, headers, runtime):
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeAckOperator',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/ack-clusters/%s/operator' % TeaConverter.to_unicode(cluster_id),
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

    def describe_apm(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_apm_with_options(instance_id, headers, runtime)

    def describe_apm_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeApm',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/apm/%s' % TeaConverter.to_unicode(instance_id),
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

    def describe_collector(self, res_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_collector_with_options(res_id, headers, runtime)

    def describe_collector_with_options(self, res_id, headers, runtime):
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeCollector',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/collectors/%s' % TeaConverter.to_unicode(res_id),
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

    def describe_component_index(self, instance_id, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_component_index_with_options(instance_id, name, headers, runtime)

    def describe_component_index_with_options(self, instance_id, name, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeComponentIndex',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/component-index/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(name)),
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

    def describe_connectable_clusters(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_connectable_clusters_with_options(instance_id, request, headers, runtime)

    def describe_connectable_clusters_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/connectable-clusters' % TeaConverter.to_unicode(instance_id),
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

    def describe_deprecated_template(self, instance_id, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_deprecated_template_with_options(instance_id, name, headers, runtime)

    def describe_deprecated_template_with_options(self, instance_id, name, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDeprecatedTemplate',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/deprecated-templates/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(name)),
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

    def describe_diagnose_report(self, instance_id, report_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_diagnose_report_with_options(instance_id, report_id, request, headers, runtime)

    def describe_diagnose_report_with_options(self, instance_id, report_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        report_id = OpenApiUtilClient.get_encode_param(report_id)
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
            pathname='/openapi/diagnosis/instances/%s/reports/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(report_id)),
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

    def describe_diagnosis_settings(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_diagnosis_settings_with_options(instance_id, request, headers, runtime)

    def describe_diagnosis_settings_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/diagnosis/instances/%s/settings' % TeaConverter.to_unicode(instance_id),
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

    def describe_elasticsearch_health(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_elasticsearch_health_with_options(instance_id, headers, runtime)

    def describe_elasticsearch_health_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeElasticsearchHealth',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/elasticsearch-health' % TeaConverter.to_unicode(instance_id),
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

    def describe_ilmpolicy(self, instance_id, policy_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_ilmpolicy_with_options(instance_id, policy_name, headers, runtime)

    def describe_ilmpolicy_with_options(self, instance_id, policy_name, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        policy_name = OpenApiUtilClient.get_encode_param(policy_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeILMPolicy',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/ilm-policies/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(policy_name)),
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

    def describe_index_template(self, instance_id, index_template):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_index_template_with_options(instance_id, index_template, headers, runtime)

    def describe_index_template_with_options(self, instance_id, index_template, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        index_template = OpenApiUtilClient.get_encode_param(index_template)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeIndexTemplate',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/index-templates/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(index_template)),
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

    def describe_instance(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instance_with_options(instance_id, headers, runtime)

    def describe_instance_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s' % TeaConverter.to_unicode(instance_id),
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

    def describe_kibana_settings(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_kibana_settings_with_options(instance_id, headers, runtime)

    def describe_kibana_settings_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeKibanaSettings',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/kibana-settings' % TeaConverter.to_unicode(instance_id),
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

    def describe_logstash(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_logstash_with_options(instance_id, headers, runtime)

    def describe_logstash_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeLogstash',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s' % TeaConverter.to_unicode(instance_id),
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

    def describe_pipeline(self, instance_id, pipeline_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_pipeline_with_options(instance_id, pipeline_id, headers, runtime)

    def describe_pipeline_with_options(self, instance_id, pipeline_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        pipeline_id = OpenApiUtilClient.get_encode_param(pipeline_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribePipeline',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/pipelines/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(pipeline_id)),
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

    def describe_pipeline_management_config(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_pipeline_management_config_with_options(instance_id, request, headers, runtime)

    def describe_pipeline_management_config_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/logstashes/%s/pipeline-management-config' % TeaConverter.to_unicode(instance_id),
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

    def describe_regions(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    def describe_regions_with_options(self, headers, runtime):
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

    def describe_snapshot_setting(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_snapshot_setting_with_options(instance_id, headers, runtime)

    def describe_snapshot_setting_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSnapshotSetting',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/snapshot-setting' % TeaConverter.to_unicode(instance_id),
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

    def describe_templates(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_templates_with_options(instance_id, headers, runtime)

    def describe_templates_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeTemplates',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/templates' % TeaConverter.to_unicode(instance_id),
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

    def describe_xpack_monitor_config(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_xpack_monitor_config_with_options(instance_id, headers, runtime)

    def describe_xpack_monitor_config_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeXpackMonitorConfig',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/xpack-monitor-config' % TeaConverter.to_unicode(instance_id),
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

    def diagnose_instance(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.diagnose_instance_with_options(instance_id, request, headers, runtime)

    def diagnose_instance_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            action='DiagnoseInstance',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/diagnosis/instances/%s/actions/diagnose' % TeaConverter.to_unicode(instance_id),
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

    def estimated_logstash_restart_time(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.estimated_logstash_restart_time_with_options(instance_id, request, headers, runtime)

    def estimated_logstash_restart_time_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EstimatedLogstashRestartTime',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/estimated-time/restart-time' % TeaConverter.to_unicode(instance_id),
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

    def estimated_restart_time(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.estimated_restart_time_with_options(instance_id, request, headers, runtime)

    def estimated_restart_time_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EstimatedRestartTime',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/estimated-time/restart-time' % TeaConverter.to_unicode(instance_id),
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

    def get_cluster_data_information(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_data_information_with_options(headers, runtime)

    def get_cluster_data_information_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
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

    def get_elastictask(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_elastictask_with_options(instance_id, headers, runtime)

    def get_elastictask_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetElastictask',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/elastic-task' % TeaConverter.to_unicode(instance_id),
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

    def get_emon_grafana_alerts(self, project_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_emon_grafana_alerts_with_options(project_id, headers, runtime)

    def get_emon_grafana_alerts_with_options(self, project_id, headers, runtime):
        project_id = OpenApiUtilClient.get_encode_param(project_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEmonGrafanaAlerts',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/emon/projects/%s/grafana/proxy/api/alerts' % TeaConverter.to_unicode(project_id),
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

    def get_emon_grafana_dashboards(self, project_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_emon_grafana_dashboards_with_options(project_id, headers, runtime)

    def get_emon_grafana_dashboards_with_options(self, project_id, headers, runtime):
        project_id = OpenApiUtilClient.get_encode_param(project_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEmonGrafanaDashboards',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/emon/projects/%s/grafana/proxy/api/search' % TeaConverter.to_unicode(project_id),
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

    def get_emon_monitor_data(self, project_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_emon_monitor_data_with_options(project_id, headers, runtime)

    def get_emon_monitor_data_with_options(self, project_id, headers, runtime):
        project_id = OpenApiUtilClient.get_encode_param(project_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEmonMonitorData',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/emon/projects/%s/metrics/query' % TeaConverter.to_unicode(project_id),
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

    def get_open_store_usage(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_open_store_usage_with_options(instance_id, headers, runtime)

    def get_open_store_usage_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOpenStoreUsage',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/openstore/usage' % TeaConverter.to_unicode(instance_id),
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

    def get_region_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_region_configuration_with_options(request, headers, runtime)

    def get_region_configuration_with_options(self, request, headers, runtime):
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

    def get_suggest_shrinkable_nodes(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_suggest_shrinkable_nodes_with_options(instance_id, request, headers, runtime)

    def get_suggest_shrinkable_nodes_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/suggest-shrinkable-nodes' % TeaConverter.to_unicode(instance_id),
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

    def get_transferable_nodes(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_transferable_nodes_with_options(instance_id, request, headers, runtime)

    def get_transferable_nodes_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/transferable-nodes' % TeaConverter.to_unicode(instance_id),
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

    def initialize_operation_role(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.initialize_operation_role_with_options(request, headers, runtime)

    def initialize_operation_role_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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

    def install_ack_operator(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_ack_operator_with_options(cluster_id, request, headers, runtime)

    def install_ack_operator_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallAckOperator',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/ack-clusters/%s/operator' % TeaConverter.to_unicode(cluster_id),
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

    def install_kibana_system_plugin(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_kibana_system_plugin_with_options(instance_id, request, headers, runtime)

    def install_kibana_system_plugin_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallKibanaSystemPlugin',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/kibana-plugins/system/actions/install' % TeaConverter.to_unicode(instance_id),
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

    def install_logstash_system_plugin(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_logstash_system_plugin_with_options(instance_id, request, headers, runtime)

    def install_logstash_system_plugin_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallLogstashSystemPlugin',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/plugins/system/actions/install' % TeaConverter.to_unicode(instance_id),
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

    def install_system_plugin(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_system_plugin_with_options(instance_id, request, headers, runtime)

    def install_system_plugin_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallSystemPlugin',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/plugins/system/actions/install' % TeaConverter.to_unicode(instance_id),
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

    def install_user_plugins(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_user_plugins_with_options(instance_id, headers, runtime)

    def install_user_plugins_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='InstallUserPlugins',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/plugins/user/actions/install' % TeaConverter.to_unicode(instance_id),
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

    def interrupt_elasticsearch_task(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.interrupt_elasticsearch_task_with_options(instance_id, request, headers, runtime)

    def interrupt_elasticsearch_task_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/actions/interrupt' % TeaConverter.to_unicode(instance_id),
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

    def interrupt_logstash_task(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.interrupt_logstash_task_with_options(instance_id, request, headers, runtime)

    def interrupt_logstash_task_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/logstashes/%s/actions/interrupt' % TeaConverter.to_unicode(instance_id),
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

    def list_ack_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ack_clusters_with_options(request, headers, runtime)

    def list_ack_clusters_with_options(self, request, headers, runtime):
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

    def list_ack_namespaces(self, cluster_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ack_namespaces_with_options(cluster_id, request, headers, runtime)

    def list_ack_namespaces_with_options(self, cluster_id, request, headers, runtime):
        UtilClient.validate_model(request)
        cluster_id = OpenApiUtilClient.get_encode_param(cluster_id)
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
            pathname='/openapi/ack-clusters/%s/namespaces' % TeaConverter.to_unicode(cluster_id),
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

    def list_all_node(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_all_node_with_options(instance_id, request, headers, runtime)

    def list_all_node_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/nodes' % TeaConverter.to_unicode(instance_id),
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

    def list_alternative_snapshot_repos(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_alternative_snapshot_repos_with_options(instance_id, request, headers, runtime)

    def list_alternative_snapshot_repos_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/alternative-snapshot-repos' % TeaConverter.to_unicode(instance_id),
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

    def list_apm(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_apm_with_options(request, headers, runtime)

    def list_apm_with_options(self, request, headers, runtime):
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

    def list_available_es_instance_ids(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_available_es_instance_ids_with_options(instance_id, headers, runtime)

    def list_available_es_instance_ids_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListAvailableEsInstanceIds',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/available-elasticsearch-for-centralized-management' % TeaConverter.to_unicode(instance_id),
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

    def list_collectors(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_collectors_with_options(request, headers, runtime)

    def list_collectors_with_options(self, request, headers, runtime):
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

    def list_component_indices(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_component_indices_with_options(instance_id, request, headers, runtime)

    def list_component_indices_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/component-index' % TeaConverter.to_unicode(instance_id),
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

    def list_connected_clusters(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_connected_clusters_with_options(instance_id, headers, runtime)

    def list_connected_clusters_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListConnectedClusters',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/connected-clusters' % TeaConverter.to_unicode(instance_id),
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

    def list_data_streams(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_streams_with_options(instance_id, request, headers, runtime)

    def list_data_streams_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/data-streams' % TeaConverter.to_unicode(instance_id),
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

    def list_data_tasks(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_tasks_with_options(instance_id, headers, runtime)

    def list_data_tasks_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataTasks',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/data-task' % TeaConverter.to_unicode(instance_id),
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

    def list_default_collector_configurations(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_default_collector_configurations_with_options(request, headers, runtime)

    def list_default_collector_configurations_with_options(self, request, headers, runtime):
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

    def list_deprecated_templates(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_deprecated_templates_with_options(instance_id, request, headers, runtime)

    def list_deprecated_templates_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/deprecated-templates' % TeaConverter.to_unicode(instance_id),
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

    def list_diagnose_indices(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_diagnose_indices_with_options(instance_id, request, headers, runtime)

    def list_diagnose_indices_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/diagnosis/instances/%s/indices' % TeaConverter.to_unicode(instance_id),
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

    def list_diagnose_report(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_diagnose_report_with_options(instance_id, request, headers, runtime)

    def list_diagnose_report_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/diagnosis/instances/%s/reports' % TeaConverter.to_unicode(instance_id),
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

    def list_diagnose_report_ids(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_diagnose_report_ids_with_options(instance_id, request, headers, runtime)

    def list_diagnose_report_ids_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/diagnosis/instances/%s/report-ids' % TeaConverter.to_unicode(instance_id),
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

    def list_dict_information(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dict_information_with_options(instance_id, request, headers, runtime)

    def list_dict_information_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/dict/_info' % TeaConverter.to_unicode(instance_id),
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

    def list_dicts(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dicts_with_options(instance_id, request, headers, runtime)

    def list_dicts_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/dicts' % TeaConverter.to_unicode(instance_id),
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

    def list_ecs_instances(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ecs_instances_with_options(request, headers, runtime)

    def list_ecs_instances_with_options(self, request, headers, runtime):
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

    def list_extendfiles(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_extendfiles_with_options(instance_id, headers, runtime)

    def list_extendfiles_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListExtendfiles',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/extendfiles' % TeaConverter.to_unicode(instance_id),
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

    def list_ilmpolicies(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ilmpolicies_with_options(instance_id, request, headers, runtime)

    def list_ilmpolicies_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/ilm-policies' % TeaConverter.to_unicode(instance_id),
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

    def list_index_templates(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_index_templates_with_options(instance_id, request, headers, runtime)

    def list_index_templates_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/index-templates' % TeaConverter.to_unicode(instance_id),
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

    def list_instance(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_with_options(request, headers, runtime)

    def list_instance_with_options(self, request, headers, runtime):
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

    def list_instance_history_events(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_history_events_with_options(request, headers, runtime)

    def list_instance_history_events_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_create_end_time):
            query['eventCreateEndTime'] = request.event_create_end_time
        if not UtilClient.is_unset(request.event_create_start_time):
            query['eventCreateStartTime'] = request.event_create_start_time
        if not UtilClient.is_unset(request.event_execute_end_time):
            query['eventExecuteEndTime'] = request.event_execute_end_time
        if not UtilClient.is_unset(request.event_execute_start_time):
            query['eventExecuteStartTime'] = request.event_execute_start_time
        if not UtilClient.is_unset(request.event_finash_end_time):
            query['eventFinashEndTime'] = request.event_finash_end_time
        if not UtilClient.is_unset(request.event_finash_start_time):
            query['eventFinashStartTime'] = request.event_finash_start_time
        if not UtilClient.is_unset(request.event_level):
            query['eventLevel'] = request.event_level
        if not UtilClient.is_unset(request.event_type):
            query['eventType'] = request.event_type
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_ip):
            query['nodeIP'] = request.node_ip
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

    def list_instance_indices(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_indices_with_options(instance_id, request, headers, runtime)

    def list_instance_indices_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/indices' % TeaConverter.to_unicode(instance_id),
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

    def list_kibana_plugins(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_kibana_plugins_with_options(instance_id, request, headers, runtime)

    def list_kibana_plugins_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/kibana-plugins' % TeaConverter.to_unicode(instance_id),
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

    def list_logstash(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logstash_with_options(request, headers, runtime)

    def list_logstash_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['ownerId'] = request.owner_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
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

    def list_logstash_log(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logstash_log_with_options(instance_id, request, headers, runtime)

    def list_logstash_log_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/logstashes/%s/search-log' % TeaConverter.to_unicode(instance_id),
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

    def list_logstash_plugins(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logstash_plugins_with_options(instance_id, request, headers, runtime)

    def list_logstash_plugins_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/logstashes/%s/plugins' % TeaConverter.to_unicode(instance_id),
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

    def list_nodes(self, res_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_nodes_with_options(res_id, request, headers, runtime)

    def list_nodes_with_options(self, res_id, request, headers, runtime):
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
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
            pathname='/openapi/collectors/%s/nodes' % TeaConverter.to_unicode(res_id),
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

    def list_pipeline(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_with_options(instance_id, request, headers, runtime)

    def list_pipeline_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/logstashes/%s/pipelines' % TeaConverter.to_unicode(instance_id),
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

    def list_pipeline_ids(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_ids_with_options(instance_id, headers, runtime)

    def list_pipeline_ids_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListPipelineIds',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/pipeline-ids' % TeaConverter.to_unicode(instance_id),
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

    def list_plugins(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_plugins_with_options(instance_id, request, headers, runtime)

    def list_plugins_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/plugins' % TeaConverter.to_unicode(instance_id),
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

    def list_search_log(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_search_log_with_options(instance_id, request, headers, runtime)

    def list_search_log_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/search-log' % TeaConverter.to_unicode(instance_id),
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

    def list_shard_recoveries(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_shard_recoveries_with_options(instance_id, request, headers, runtime)

    def list_shard_recoveries_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/cat-recovery' % TeaConverter.to_unicode(instance_id),
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

    def list_snapshot_repos_by_instance_id(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_snapshot_repos_by_instance_id_with_options(instance_id, headers, runtime)

    def list_snapshot_repos_by_instance_id_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSnapshotReposByInstanceId',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/snapshot-repos' % TeaConverter.to_unicode(instance_id),
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

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    def list_tag_resources_with_options(self, request, headers, runtime):
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

    def list_tags(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tags_with_options(request, headers, runtime)

    def list_tags_with_options(self, request, headers, runtime):
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

    def list_vpc_endpoints(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_vpc_endpoints_with_options(instance_id, request, headers, runtime)

    def list_vpc_endpoints_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/vpc-endpoints' % TeaConverter.to_unicode(instance_id),
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

    def migrate_to_other_zone(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.migrate_to_other_zone_with_options(instance_id, request, headers, runtime)

    def migrate_to_other_zone_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateToOtherZone',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/migrate-zones' % TeaConverter.to_unicode(instance_id),
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

    def modify_deploy_machine(self, res_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_deploy_machine_with_options(res_id, request, headers, runtime)

    def modify_deploy_machine_with_options(self, res_id, request, headers, runtime):
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDeployMachine',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/collectors/%s/actions/modify-deploy-machines' % TeaConverter.to_unicode(res_id),
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

    def modify_elastictask(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_elastictask_with_options(instance_id, headers, runtime)

    def modify_elastictask_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyElastictask',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/elastic-task' % TeaConverter.to_unicode(instance_id),
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

    def modify_instance_maintain_time(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_instance_maintain_time_with_options(instance_id, request, headers, runtime)

    def modify_instance_maintain_time_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceMaintainTime',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/modify-maintaintime' % TeaConverter.to_unicode(instance_id),
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

    def modify_white_ips(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_white_ips_with_options(instance_id, request, headers, runtime)

    def modify_white_ips_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/actions/modify-white-ips' % TeaConverter.to_unicode(instance_id),
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

    def move_resource_group(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.move_resource_group_with_options(instance_id, request, headers, runtime)

    def move_resource_group_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/resourcegroup' % TeaConverter.to_unicode(instance_id),
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

    def open_diagnosis(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.open_diagnosis_with_options(instance_id, request, headers, runtime)

    def open_diagnosis_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/diagnosis/instances/%s/actions/open-diagnosis' % TeaConverter.to_unicode(instance_id),
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

    def open_https(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.open_https_with_options(instance_id, request, headers, runtime)

    def open_https_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/actions/open-https' % TeaConverter.to_unicode(instance_id),
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

    def post_emon_try_alarm_rule(self, project_id, alarm_group_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.post_emon_try_alarm_rule_with_options(project_id, alarm_group_id, headers, runtime)

    def post_emon_try_alarm_rule_with_options(self, project_id, alarm_group_id, headers, runtime):
        project_id = OpenApiUtilClient.get_encode_param(project_id)
        alarm_group_id = OpenApiUtilClient.get_encode_param(alarm_group_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PostEmonTryAlarmRule',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/emon/projects/%s/alarm-groups/%s/alarm-rules/_test' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(alarm_group_id)),
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

    def recommend_templates(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recommend_templates_with_options(instance_id, request, headers, runtime)

    def recommend_templates_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/recommended-templates' % TeaConverter.to_unicode(instance_id),
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

    def reinstall_collector(self, res_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reinstall_collector_with_options(res_id, request, headers, runtime)

    def reinstall_collector_with_options(self, res_id, request, headers, runtime):
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReinstallCollector',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/collectors/%s/actions/reinstall' % TeaConverter.to_unicode(res_id),
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

    def remove_apm(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_apm_with_options(instance_id, headers, runtime)

    def remove_apm_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveApm',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/apm/%s' % TeaConverter.to_unicode(instance_id),
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

    def renew_instance(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.renew_instance_with_options(instance_id, request, headers, runtime)

    def renew_instance_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/renew' % TeaConverter.to_unicode(instance_id),
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

    def renew_logstash(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.renew_logstash_with_options(instance_id, request, headers, runtime)

    def renew_logstash_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewLogstash',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/actions/renew' % TeaConverter.to_unicode(instance_id),
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

    def restart_collector(self, res_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_collector_with_options(res_id, request, headers, runtime)

    def restart_collector_with_options(self, res_id, request, headers, runtime):
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
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
            pathname='/openapi/collectors/%s/actions/restart' % TeaConverter.to_unicode(res_id),
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

    def restart_instance(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_instance_with_options(instance_id, request, headers, runtime)

    def restart_instance_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/restart' % TeaConverter.to_unicode(instance_id),
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

    def restart_logstash(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_logstash_with_options(instance_id, request, headers, runtime)

    def restart_logstash_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartLogstash',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/actions/restart' % TeaConverter.to_unicode(instance_id),
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

    def resume_elasticsearch_task(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_elasticsearch_task_with_options(instance_id, request, headers, runtime)

    def resume_elasticsearch_task_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/actions/resume' % TeaConverter.to_unicode(instance_id),
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

    def resume_logstash_task(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_logstash_task_with_options(instance_id, request, headers, runtime)

    def resume_logstash_task_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/logstashes/%s/actions/resume' % TeaConverter.to_unicode(instance_id),
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

    def rollover_data_stream(self, instance_id, data_stream, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rollover_data_stream_with_options(instance_id, data_stream, request, headers, runtime)

    def rollover_data_stream_with_options(self, instance_id, data_stream, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        data_stream = OpenApiUtilClient.get_encode_param(data_stream)
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
            pathname='/openapi/instances/%s/data-streams/%s/rollover' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(data_stream)),
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

    def run_pipelines(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_pipelines_with_options(instance_id, request, headers, runtime)

    def run_pipelines_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunPipelines',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/pipelines/action/run' % TeaConverter.to_unicode(instance_id),
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

    def shrink_node(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.shrink_node_with_options(instance_id, request, headers, runtime)

    def shrink_node_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
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
            pathname='/openapi/instances/%s/actions/shrink' % TeaConverter.to_unicode(instance_id),
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

    def start_apm(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_apm_with_options(instance_id, headers, runtime)

    def start_apm_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartApm',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/apm/%s/actions/start' % TeaConverter.to_unicode(instance_id),
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

    def start_collector(self, res_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_collector_with_options(res_id, request, headers, runtime)

    def start_collector_with_options(self, res_id, request, headers, runtime):
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
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
            pathname='/openapi/collectors/%s/actions/start' % TeaConverter.to_unicode(res_id),
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

    def stop_apm(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_apm_with_options(instance_id, headers, runtime)

    def stop_apm_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopApm',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/apm/%s/actions/stop' % TeaConverter.to_unicode(instance_id),
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

    def stop_collector(self, res_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_collector_with_options(res_id, request, headers, runtime)

    def stop_collector_with_options(self, res_id, request, headers, runtime):
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
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
            pathname='/openapi/collectors/%s/actions/stop' % TeaConverter.to_unicode(res_id),
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

    def stop_pipelines(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_pipelines_with_options(instance_id, request, headers, runtime)

    def stop_pipelines_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopPipelines',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/pipelines/action/stop' % TeaConverter.to_unicode(instance_id),
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

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    def tag_resources_with_options(self, request, headers, runtime):
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

    def transfer_node(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.transfer_node_with_options(instance_id, request, headers, runtime)

    def transfer_node_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/actions/transfer' % TeaConverter.to_unicode(instance_id),
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

    def trigger_network(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.trigger_network_with_options(instance_id, request, headers, runtime)

    def trigger_network_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/actions/network-trigger' % TeaConverter.to_unicode(instance_id),
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

    def uninstall_kibana_plugin(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.uninstall_kibana_plugin_with_options(instance_id, request, headers, runtime)

    def uninstall_kibana_plugin_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallKibanaPlugin',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/kibana-plugins/actions/uninstall' % TeaConverter.to_unicode(instance_id),
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

    def uninstall_logstash_plugin(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.uninstall_logstash_plugin_with_options(instance_id, request, headers, runtime)

    def uninstall_logstash_plugin_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallLogstashPlugin',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/plugins/actions/uninstall' % TeaConverter.to_unicode(instance_id),
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

    def uninstall_plugin(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.uninstall_plugin_with_options(instance_id, request, headers, runtime)

    def uninstall_plugin_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallPlugin',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/plugins/actions/uninstall' % TeaConverter.to_unicode(instance_id),
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

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    def untag_resources_with_options(self, request, headers, runtime):
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
            query=OpenApiUtilClient.query(query)
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

    def update_admin_password(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_admin_password_with_options(instance_id, request, headers, runtime)

    def update_admin_password_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAdminPassword',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/admin-pwd' % TeaConverter.to_unicode(instance_id),
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

    def update_advanced_setting(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_advanced_setting_with_options(instance_id, request, headers, runtime)

    def update_advanced_setting_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAdvancedSetting',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/update-advanced-setting' % TeaConverter.to_unicode(instance_id),
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

    def update_aliws_dict(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_aliws_dict_with_options(instance_id, request, headers, runtime)

    def update_aliws_dict_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAliwsDict',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/aliws-dict' % TeaConverter.to_unicode(instance_id),
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

    def update_apm(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_apm_with_options(instance_id, request, headers, runtime)

    def update_apm_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/apm/%s' % TeaConverter.to_unicode(instance_id),
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

    def update_black_ips(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_black_ips_with_options(instance_id, request, headers, runtime)

    def update_black_ips_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.es_ipblacklist):
            body['esIPBlacklist'] = request.es_ipblacklist
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBlackIps',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/black-ips' % TeaConverter.to_unicode(instance_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateBlackIpsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_collector(self, res_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_collector_with_options(res_id, request, headers, runtime)

    def update_collector_with_options(self, res_id, request, headers, runtime):
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCollector',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/collectors/%s' % TeaConverter.to_unicode(res_id),
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

    def update_collector_name(self, res_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_collector_name_with_options(res_id, request, headers, runtime)

    def update_collector_name_with_options(self, res_id, request, headers, runtime):
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCollectorName',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/collectors/%s/actions/rename' % TeaConverter.to_unicode(res_id),
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

    def update_component_index(self, instance_id, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_component_index_with_options(instance_id, name, request, headers, runtime)

    def update_component_index_with_options(self, instance_id, name, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        name = OpenApiUtilClient.get_encode_param(name)
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
            pathname='/openapi/instances/%s/component-index/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(name)),
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

    def update_description(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_description_with_options(instance_id, request, headers, runtime)

    def update_description_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/description' % TeaConverter.to_unicode(instance_id),
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

    def update_diagnosis_settings(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_diagnosis_settings_with_options(instance_id, request, headers, runtime)

    def update_diagnosis_settings_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            action='UpdateDiagnosisSettings',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/diagnosis/instances/%s/settings' % TeaConverter.to_unicode(instance_id),
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

    def update_dict(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_dict_with_options(instance_id, request, headers, runtime)

    def update_dict_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDict',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/dict' % TeaConverter.to_unicode(instance_id),
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

    def update_extend_config(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_extend_config_with_options(instance_id, request, headers, runtime)

    def update_extend_config_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateExtendConfig',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/extend-configs/actions/update' % TeaConverter.to_unicode(instance_id),
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

    def update_extendfiles(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_extendfiles_with_options(instance_id, request, headers, runtime)

    def update_extendfiles_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateExtendfiles',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/extendfiles' % TeaConverter.to_unicode(instance_id),
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

    def update_hot_ik_dicts(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_hot_ik_dicts_with_options(instance_id, request, headers, runtime)

    def update_hot_ik_dicts_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHotIkDicts',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/ik-hot-dict' % TeaConverter.to_unicode(instance_id),
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

    def update_ilmpolicy(self, instance_id, policy_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_ilmpolicy_with_options(instance_id, policy_name, request, headers, runtime)

    def update_ilmpolicy_with_options(self, instance_id, policy_name, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        policy_name = OpenApiUtilClient.get_encode_param(policy_name)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateILMPolicy',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/ilm-policies/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(policy_name)),
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

    def update_index_template(self, instance_id, index_template, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_index_template_with_options(instance_id, index_template, request, headers, runtime)

    def update_index_template_with_options(self, instance_id, index_template, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        index_template = OpenApiUtilClient.get_encode_param(index_template)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIndexTemplate',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/index-templates/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(index_template)),
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

    def update_instance(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(instance_id, request, headers, runtime)

    def update_instance_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        if not UtilClient.is_unset(request.order_action_type):
            query['orderActionType'] = request.order_action_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s' % TeaConverter.to_unicode(instance_id),
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

    def update_instance_charge_type(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_charge_type_with_options(instance_id, request, headers, runtime)

    def update_instance_charge_type_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceChargeType',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/convert-pay-type' % TeaConverter.to_unicode(instance_id),
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

    def update_instance_settings(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_settings_with_options(instance_id, request, headers, runtime)

    def update_instance_settings_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceSettings',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/instance-settings' % TeaConverter.to_unicode(instance_id),
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

    def update_kibana_settings(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_kibana_settings_with_options(instance_id, request, headers, runtime)

    def update_kibana_settings_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateKibanaSettings',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/update-kibana-settings' % TeaConverter.to_unicode(instance_id),
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

    def update_kibana_white_ips(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_kibana_white_ips_with_options(instance_id, request, headers, runtime)

    def update_kibana_white_ips_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateKibanaWhiteIps',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/kibana-white-ips' % TeaConverter.to_unicode(instance_id),
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

    def update_logstash(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logstash_with_options(instance_id, request, headers, runtime)

    def update_logstash_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
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
            pathname='/openapi/logstashes/%s' % TeaConverter.to_unicode(instance_id),
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

    def update_logstash_charge_type(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logstash_charge_type_with_options(instance_id, request, headers, runtime)

    def update_logstash_charge_type_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.payment_info):
            body['paymentInfo'] = request.payment_info
        if not UtilClient.is_unset(request.payment_type):
            body['paymentType'] = request.payment_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogstashChargeType',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/actions/convert-pay-type' % TeaConverter.to_unicode(instance_id),
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

    def update_logstash_description(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logstash_description_with_options(instance_id, request, headers, runtime)

    def update_logstash_description_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/logstashes/%s/description' % TeaConverter.to_unicode(instance_id),
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

    def update_logstash_settings(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logstash_settings_with_options(instance_id, request, headers, runtime)

    def update_logstash_settings_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogstashSettings',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/instance-settings' % TeaConverter.to_unicode(instance_id),
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

    def update_pipeline_management_config(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipeline_management_config_with_options(instance_id, request, headers, runtime)

    def update_pipeline_management_config_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipelineManagementConfig',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/pipeline-management-config' % TeaConverter.to_unicode(instance_id),
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

    def update_pipelines(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipelines_with_options(instance_id, request, headers, runtime)

    def update_pipelines_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipelines',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/pipelines' % TeaConverter.to_unicode(instance_id),
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

    def update_private_network_white_ips(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_private_network_white_ips_with_options(instance_id, request, headers, runtime)

    def update_private_network_white_ips_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrivateNetworkWhiteIps',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/private-network-white-ips' % TeaConverter.to_unicode(instance_id),
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

    def update_public_network(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_public_network_with_options(instance_id, request, headers, runtime)

    def update_public_network_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePublicNetwork',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/public-network' % TeaConverter.to_unicode(instance_id),
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

    def update_public_white_ips(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_public_white_ips_with_options(instance_id, request, headers, runtime)

    def update_public_white_ips_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.modify_mode):
            query['modifyMode'] = request.modify_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePublicWhiteIps',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/public-white-ips' % TeaConverter.to_unicode(instance_id),
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

    def update_read_write_policy(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_read_write_policy_with_options(instance_id, request, headers, runtime)

    def update_read_write_policy_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateReadWritePolicy',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/actions/update-read-write-policy' % TeaConverter.to_unicode(instance_id),
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

    def update_snapshot_setting(self, instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_snapshot_setting_with_options(instance_id, headers, runtime)

    def update_snapshot_setting_with_options(self, instance_id, headers, runtime):
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateSnapshotSetting',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/snapshot-setting' % TeaConverter.to_unicode(instance_id),
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

    def update_synonyms_dicts(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_synonyms_dicts_with_options(instance_id, request, headers, runtime)

    def update_synonyms_dicts_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSynonymsDicts',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/synonymsDict' % TeaConverter.to_unicode(instance_id),
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

    def update_template(self, instance_id, template_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_template_with_options(instance_id, template_name, request, headers, runtime)

    def update_template_with_options(self, instance_id, template_name, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        template_name = OpenApiUtilClient.get_encode_param(template_name)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/instances/%s/templates/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(template_name)),
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

    def update_white_ips(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_white_ips_with_options(instance_id, request, headers, runtime)

    def update_white_ips_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/white-ips' % TeaConverter.to_unicode(instance_id),
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

    def update_xpack_monitor_config(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_xpack_monitor_config_with_options(instance_id, request, headers, runtime)

    def update_xpack_monitor_config_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateXpackMonitorConfig',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/xpack-monitor-config' % TeaConverter.to_unicode(instance_id),
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

    def upgrade_engine_version(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_engine_version_with_options(instance_id, request, headers, runtime)

    def upgrade_engine_version_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
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
            pathname='/openapi/instances/%s/actions/upgrade-version' % TeaConverter.to_unicode(instance_id),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpgradeEngineVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def validate_connection(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_connection_with_options(instance_id, request, headers, runtime)

    def validate_connection_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateConnection',
            version='2017-06-13',
            protocol='HTTPS',
            pathname='/openapi/logstashes/%s/validate-connection' % TeaConverter.to_unicode(instance_id),
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

    def validate_shrink_nodes(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_shrink_nodes_with_options(instance_id, request, headers, runtime)

    def validate_shrink_nodes_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
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
            pathname='/openapi/instances/%s/validate-shrink-nodes' % TeaConverter.to_unicode(instance_id),
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

    def validate_slr_permission(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_slr_permission_with_options(request, headers, runtime)

    def validate_slr_permission_with_options(self, request, headers, runtime):
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

    def validate_transferable_nodes(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_transferable_nodes_with_options(instance_id, request, headers, runtime)

    def validate_transferable_nodes_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
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
            pathname='/openapi/instances/%s/validate-transfer-nodes' % TeaConverter.to_unicode(instance_id),
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

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    def create_instance_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
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
            body_type='json'
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )
