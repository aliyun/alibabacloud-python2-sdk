# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

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
        self._endpoint_map = {
            'ap-northeast-2-pop': 'elasticsearch.aliyuncs.com',
            'cn-beijing-finance-1': 'elasticsearch.aliyuncs.com',
            'cn-beijing-finance-pop': 'elasticsearch.aliyuncs.com',
            'cn-beijing-gov-1': 'elasticsearch.aliyuncs.com',
            'cn-beijing-nu16-b01': 'elasticsearch.aliyuncs.com',
            'cn-chengdu': 'elasticsearch.aliyuncs.com',
            'cn-edge-1': 'elasticsearch.aliyuncs.com',
            'cn-fujian': 'elasticsearch.aliyuncs.com',
            'cn-haidian-cm12-c01': 'elasticsearch.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'elasticsearch.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'elasticsearch.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'elasticsearch.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'elasticsearch.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'elasticsearch.aliyuncs.com',
            'cn-hangzhou-test-306': 'elasticsearch.aliyuncs.com',
            'cn-hongkong-finance-pop': 'elasticsearch.aliyuncs.com',
            'cn-huhehaote': 'elasticsearch.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'elasticsearch.aliyuncs.com',
            'cn-qingdao-nebula': 'elasticsearch.aliyuncs.com',
            'cn-shanghai-et15-b01': 'elasticsearch.aliyuncs.com',
            'cn-shanghai-et2-b01': 'elasticsearch.aliyuncs.com',
            'cn-shanghai-inner': 'elasticsearch.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'elasticsearch.aliyuncs.com',
            'cn-shenzhen-finance-1': 'elasticsearch.aliyuncs.com',
            'cn-shenzhen-inner': 'elasticsearch.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'elasticsearch.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'elasticsearch.aliyuncs.com',
            'cn-wuhan': 'elasticsearch.aliyuncs.com',
            'cn-wulanchabu': 'elasticsearch.aliyuncs.com',
            'cn-yushanfang': 'elasticsearch.aliyuncs.com',
            'cn-zhangbei': 'elasticsearch.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'elasticsearch.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'elasticsearch.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'elasticsearch.aliyuncs.com',
            'eu-west-1-oxs': 'elasticsearch.aliyuncs.com',
            'me-east-1': 'elasticsearch.aliyuncs.com',
            'rus-west-1-pop': 'elasticsearch.aliyuncs.com'
        }
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ActivateZonesResponse(),
            self.do_roarequest('ActivateZones', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/recover-zones' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.AddConnectableClusterResponse(),
            self.do_roarequest('AddConnectableCluster', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/connected-clusters' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.AddSnapshotRepoResponse(),
            self.do_roarequest('AddSnapshotRepo', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/snapshot-repos' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.CancelDeletionResponse(),
            self.do_roarequest('CancelDeletion', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/cancel-deletion' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.CancelLogstashDeletionResponse(),
            self.do_roarequest('CancelLogstashDeletion', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes/%s/actions/cancel-deletion' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def cancel_task(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_task_with_options(instance_id, request, headers, runtime)

    def cancel_task_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CancelTaskResponse(),
            self.do_roarequest('CancelTask', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/cancel-task' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.CapacityPlanResponse(),
            self.do_roarequest('CapacityPlan', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/assist/actions/capacity-plan', 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.CloseDiagnosisResponse(),
            self.do_roarequest('CloseDiagnosis', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/diagnosis/instances/%s/actions/close-diagnosis' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.CloseHttpsResponse(),
            self.do_roarequest('CloseHttps', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/close-https' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.CloseManagedIndexResponse(),
            self.do_roarequest('CloseManagedIndex', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/indices/%s/close-managed' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(index)), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateCollectorResponse(),
            self.do_roarequest('CreateCollector', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/collectors', 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateDataStreamResponse(),
            self.do_roarequest('CreateDataStream', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/data-streams' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateDataTasksResponse(),
            self.do_roarequest('CreateDataTasks', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/data-task' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateILMPolicyResponse(),
            self.do_roarequest('CreateILMPolicy', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/ilm-policies' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateIndexTemplateResponse(),
            self.do_roarequest('CreateIndexTemplate', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/index-templates' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateInstanceResponse(),
            self.do_roarequest('createInstance', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateLogstashResponse(),
            self.do_roarequest('CreateLogstash', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes', 'json', req, runtime)
        )

    def create_pipelines(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_pipelines_with_options(instance_id, request, headers, runtime)

    def create_pipelines_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreatePipelinesResponse(),
            self.do_roarequest('CreatePipelines', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes/%s/pipelines' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateSnapshotResponse(),
            self.do_roarequest('CreateSnapshot', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/snapshots' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.CreateVpcEndpointResponse(),
            self.do_roarequest('CreateVpcEndpoint', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/vpc-endpoints' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeactivateZonesResponse(),
            self.do_roarequest('DeactivateZones', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/down-zones' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteCollectorResponse(),
            self.do_roarequest('DeleteCollector', '2017-06-13', 'HTTPS', 'DELETE', 'AK', '/openapi/collectors/%s' % TeaConverter.to_unicode(res_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteConnectedClusterResponse(),
            self.do_roarequest('DeleteConnectedCluster', '2017-06-13', 'HTTPS', 'DELETE', 'AK', '/openapi/instances/%s/connected-clusters' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteDataStreamResponse(),
            self.do_roarequest('DeleteDataStream', '2017-06-13', 'HTTPS', 'DELETE', 'AK', '/openapi/instances/%s/data-streams/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(data_stream)), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteDataTaskResponse(),
            self.do_roarequest('DeleteDataTask', '2017-06-13', 'HTTPS', 'DELETE', 'AK', '/openapi/instances/%s/data-task' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteILMPolicyResponse(),
            self.do_roarequest('DeleteILMPolicy', '2017-06-13', 'HTTPS', 'DELETE', 'AK', '/openapi/instances/%s/ilm-policies/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(policy_name)), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteIndexTemplateResponse(),
            self.do_roarequest('DeleteIndexTemplate', '2017-06-13', 'HTTPS', 'DELETE', 'AK', '/openapi/instances/%s/index-templates/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(index_template)), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteInstanceResponse(),
            self.do_roarequest('DeleteInstance', '2017-06-13', 'HTTPS', 'DELETE', 'AK', '/openapi/instances/%s' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteLogstashResponse(),
            self.do_roarequest('DeleteLogstash', '2017-06-13', 'HTTPS', 'DELETE', 'AK', '/openapi/logstashes/%s' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeletePipelinesResponse(),
            self.do_roarequest('DeletePipelines', '2017-06-13', 'HTTPS', 'DELETE', 'AK', '/openapi/logstashes/%s/pipelines' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def delete_snapshot_repo(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_snapshot_repo_with_options(instance_id, request, headers, runtime)

    def delete_snapshot_repo_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.repo_path):
            query['repoPath'] = request.repo_path
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteSnapshotRepoResponse(),
            self.do_roarequest('DeleteSnapshotRepo', '2017-06-13', 'HTTPS', 'DELETE', 'AK', '/openapi/instances/%s/snapshot-repos' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DeleteVpcEndpointResponse(),
            self.do_roarequest('DeleteVpcEndpoint', '2017-06-13', 'HTTPS', 'DELETE', 'AK', '/openapi/instances/%s/vpc-endpoints/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(endpoint_id)), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeAckOperatorResponse(),
            self.do_roarequest('DescribeAckOperator', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/ack-clusters/%s/operator' % TeaConverter.to_unicode(cluster_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeCollectorResponse(),
            self.do_roarequest('DescribeCollector', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/collectors/%s' % TeaConverter.to_unicode(res_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeConnectableClustersResponse(),
            self.do_roarequest('DescribeConnectableClusters', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/connectable-clusters' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeDiagnoseReportResponse(),
            self.do_roarequest('DescribeDiagnoseReport', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/diagnosis/instances/%s/reports/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(report_id)), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeDiagnosisSettingsResponse(),
            self.do_roarequest('DescribeDiagnosisSettings', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/diagnosis/instances/%s/settings' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeElasticsearchHealthResponse(),
            self.do_roarequest('DescribeElasticsearchHealth', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/elasticsearch-health' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeILMPolicyResponse(),
            self.do_roarequest('DescribeILMPolicy', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/ilm-policies/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(policy_name)), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeIndexTemplateResponse(),
            self.do_roarequest('DescribeIndexTemplate', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/index-templates/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(index_template)), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeInstanceResponse(),
            self.do_roarequest('DescribeInstance', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeKibanaSettingsResponse(),
            self.do_roarequest('DescribeKibanaSettings', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/kibana-settings' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeLogstashResponse(),
            self.do_roarequest('DescribeLogstash', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/logstashes/%s' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribePipelineResponse(),
            self.do_roarequest('DescribePipeline', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/logstashes/%s/pipelines/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(pipeline_id)), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribePipelineManagementConfigResponse(),
            self.do_roarequest('DescribePipelineManagementConfig', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/logstashes/%s/pipeline-management-config' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def describe_regions(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    def describe_regions_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeRegionsResponse(),
            self.do_roarequest('DescribeRegions', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/regions', 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeSnapshotSettingResponse(),
            self.do_roarequest('DescribeSnapshotSetting', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/snapshot-setting' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeTemplatesResponse(),
            self.do_roarequest('DescribeTemplates', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/templates' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.DescribeXpackMonitorConfigResponse(),
            self.do_roarequest('DescribeXpackMonitorConfig', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/logstashes/%s/xpack-monitor-config' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def diagnose_instance(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.diagnose_instance_with_options(instance_id, request, headers, runtime)

    def diagnose_instance_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.DiagnoseInstanceResponse(),
            self.do_roarequest('DiagnoseInstance', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/diagnosis/instances/%s/actions/diagnose' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.EstimatedLogstashRestartTimeResponse(),
            self.do_roarequest('EstimatedLogstashRestartTime', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes/%s/estimated-time/restart-time' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.EstimatedRestartTimeResponse(),
            self.do_roarequest('EstimatedRestartTime', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/estimated-time/restart-time' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def get_cluster_data_information(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_data_information_with_options(headers, runtime)

    def get_cluster_data_information_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetClusterDataInformationResponse(),
            self.do_roarequest('GetClusterDataInformation', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/cluster/data-information', 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetElastictaskResponse(),
            self.do_roarequest('GetElastictask', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/elastic-task' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetEmonGrafanaAlertsResponse(),
            self.do_roarequest('GetEmonGrafanaAlerts', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/emon/projects/%s/grafana/proxy/api/alerts' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetEmonGrafanaDashboardsResponse(),
            self.do_roarequest('GetEmonGrafanaDashboards', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/emon/projects/%s/grafana/proxy/api/search' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetEmonMonitorDataResponse(),
            self.do_roarequest('GetEmonMonitorData', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/emon/projects/%s/metrics/query' % TeaConverter.to_unicode(project_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetOpenStoreUsageResponse(),
            self.do_roarequest('GetOpenStoreUsage', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/openstore/usage' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetRegionConfigurationResponse(),
            self.do_roarequest('GetRegionConfiguration', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/region', 'json', req, runtime)
        )

    def get_suggest_shrinkable_nodes(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_suggest_shrinkable_nodes_with_options(instance_id, request, headers, runtime)

    def get_suggest_shrinkable_nodes_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetSuggestShrinkableNodesResponse(),
            self.do_roarequest('GetSuggestShrinkableNodes', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/suggest-shrinkable-nodes' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def get_transferable_nodes(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_transferable_nodes_with_options(instance_id, request, headers, runtime)

    def get_transferable_nodes_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.GetTransferableNodesResponse(),
            self.do_roarequest('GetTransferableNodes', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/transferable-nodes' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.InitializeOperationRoleResponse(),
            self.do_roarequest('InitializeOperationRole', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/user/slr', 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallAckOperatorResponse(),
            self.do_roarequest('InstallAckOperator', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/ack-clusters/%s/operator' % TeaConverter.to_unicode(cluster_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallKibanaSystemPluginResponse(),
            self.do_roarequest('InstallKibanaSystemPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/kibana-plugins/system/actions/install' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallLogstashSystemPluginResponse(),
            self.do_roarequest('InstallLogstashSystemPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes/%s/plugins/system/actions/install' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallSystemPluginResponse(),
            self.do_roarequest('InstallSystemPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/plugins/system/actions/install' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.InstallUserPluginsResponse(),
            self.do_roarequest('InstallUserPlugins', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/plugins/user/actions/install' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.InterruptElasticsearchTaskResponse(),
            self.do_roarequest('InterruptElasticsearchTask', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/interrupt' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.InterruptLogstashTaskResponse(),
            self.do_roarequest('InterruptLogstashTask', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes/%s/actions/interrupt' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAckClustersResponse(),
            self.do_roarequest('ListAckClusters', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/ack-clusters', 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAckNamespacesResponse(),
            self.do_roarequest('ListAckNamespaces', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/ack-clusters/%s/namespaces' % TeaConverter.to_unicode(cluster_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAllNodeResponse(),
            self.do_roarequest('ListAllNode', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/nodes' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAlternativeSnapshotReposResponse(),
            self.do_roarequest('ListAlternativeSnapshotRepos', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/alternative-snapshot-repos' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListAvailableEsInstanceIdsResponse(),
            self.do_roarequest('ListAvailableEsInstanceIds', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/logstashes/%s/available-elasticsearch-for-centralized-management' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def list_collectors(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_collectors_with_options(request, headers, runtime)

    def list_collectors_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.res_id):
            query['resId'] = request.res_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListCollectorsResponse(),
            self.do_roarequest('ListCollectors', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/collectors', 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListConnectedClustersResponse(),
            self.do_roarequest('ListConnectedClusters', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/connected-clusters' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDataStreamsResponse(),
            self.do_roarequest('ListDataStreams', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/data-streams' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDataTasksResponse(),
            self.do_roarequest('ListDataTasks', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/data-task' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDefaultCollectorConfigurationsResponse(),
            self.do_roarequest('ListDefaultCollectorConfigurations', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/beats/default-configurations', 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDiagnoseIndicesResponse(),
            self.do_roarequest('ListDiagnoseIndices', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/diagnosis/instances/%s/indices' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def list_diagnose_report(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_diagnose_report_with_options(instance_id, request, headers, runtime)

    def list_diagnose_report_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.detail):
            query['detail'] = request.detail
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDiagnoseReportResponse(),
            self.do_roarequest('ListDiagnoseReport', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/diagnosis/instances/%s/reports' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def list_diagnose_report_ids(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_diagnose_report_ids_with_options(instance_id, request, headers, runtime)

    def list_diagnose_report_ids_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDiagnoseReportIdsResponse(),
            self.do_roarequest('ListDiagnoseReportIds', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/diagnosis/instances/%s/report-ids' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def list_dict_information(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dict_information_with_options(instance_id, request, headers, runtime)

    def list_dict_information_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['bucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        if not UtilClient.is_unset(request.analyzer_type):
            query['analyzerType'] = request.analyzer_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDictInformationResponse(),
            self.do_roarequest('ListDictInformation', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/dict/_info' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListDictsResponse(),
            self.do_roarequest('ListDicts', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/dicts' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def list_ecs_instances(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ecs_instances_with_options(request, headers, runtime)

    def list_ecs_instances_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.ecs_instance_ids):
            query['ecsInstanceIds'] = request.ecs_instance_ids
        if not UtilClient.is_unset(request.ecs_instance_name):
            query['ecsInstanceName'] = request.ecs_instance_name
        if not UtilClient.is_unset(request.tags):
            query['tags'] = request.tags
        if not UtilClient.is_unset(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListEcsInstancesResponse(),
            self.do_roarequest('ListEcsInstances', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/ecs', 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListExtendfilesResponse(),
            self.do_roarequest('ListExtendfiles', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/logstashes/%s/extendfiles' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListILMPoliciesResponse(),
            self.do_roarequest('ListILMPolicies', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/ilm-policies' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListIndexTemplatesResponse(),
            self.do_roarequest('ListIndexTemplates', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/index-templates' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def list_instance(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_with_options(request, headers, runtime)

    def list_instance_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.es_version):
            query['esVersion'] = request.es_version
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['tags'] = request.tags
        if not UtilClient.is_unset(request.vpc_id):
            query['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['zoneId'] = request.zone_id
        if not UtilClient.is_unset(request.payment_type):
            query['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.instance_category):
            query['instanceCategory'] = request.instance_category
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListInstanceResponse(),
            self.do_roarequest('ListInstance', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances', 'json', req, runtime)
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
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.is_managed):
            query['isManaged'] = request.is_managed
        if not UtilClient.is_unset(request.is_openstore):
            query['isOpenstore'] = request.is_openstore
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListInstanceIndicesResponse(),
            self.do_roarequest('ListInstanceIndices', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/indices' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListKibanaPluginsResponse(),
            self.do_roarequest('ListKibanaPlugins', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/kibana-plugins' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def list_logstash(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logstash_with_options(request, headers, runtime)

    def list_logstash_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        if not UtilClient.is_unset(request.owner_id):
            query['ownerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListLogstashResponse(),
            self.do_roarequest('ListLogstash', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/logstashes', 'json', req, runtime)
        )

    def list_logstash_log(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logstash_log_with_options(instance_id, request, headers, runtime)

    def list_logstash_log_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListLogstashLogResponse(),
            self.do_roarequest('ListLogstashLog', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/logstashes/%s/search-log' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListLogstashPluginsResponse(),
            self.do_roarequest('ListLogstashPlugins', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/logstashes/%s/plugins' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def list_nodes(self, res_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_nodes_with_options(res_id, request, headers, runtime)

    def list_nodes_with_options(self, res_id, request, headers, runtime):
        UtilClient.validate_model(request)
        res_id = OpenApiUtilClient.get_encode_param(res_id)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.ecs_instance_ids):
            query['ecsInstanceIds'] = request.ecs_instance_ids
        if not UtilClient.is_unset(request.ecs_instance_name):
            query['ecsInstanceName'] = request.ecs_instance_name
        if not UtilClient.is_unset(request.tags):
            query['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListNodesResponse(),
            self.do_roarequest('ListNodes', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/collectors/%s/nodes' % TeaConverter.to_unicode(res_id), 'json', req, runtime)
        )

    def list_pipeline(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pipeline_with_options(instance_id, request, headers, runtime)

    def list_pipeline_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.pipeline_id):
            query['pipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListPipelineResponse(),
            self.do_roarequest('ListPipeline', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/logstashes/%s/pipelines' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListPipelineIdsResponse(),
            self.do_roarequest('ListPipelineIds', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/pipeline-ids' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListPluginsResponse(),
            self.do_roarequest('ListPlugins', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/plugins' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def list_search_log(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_search_log_with_options(instance_id, request, headers, runtime)

    def list_search_log_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.begin_time):
            query['beginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListSearchLogResponse(),
            self.do_roarequest('ListSearchLog', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/search-log' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListShardRecoveriesResponse(),
            self.do_roarequest('ListShardRecoveries', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/cat-recovery' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListSnapshotReposByInstanceIdResponse(),
            self.do_roarequest('ListSnapshotReposByInstanceId', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/snapshot-repos' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    def list_tag_resources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListTagResourcesResponse(),
            self.do_roarequest('ListTagResources', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/tags', 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListTagsResponse(),
            self.do_roarequest('ListTags', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/tags/all-tags', 'json', req, runtime)
        )

    def list_vpc_endpoints(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_vpc_endpoints_with_options(instance_id, request, headers, runtime)

    def list_vpc_endpoints_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ListVpcEndpointsResponse(),
            self.do_roarequest('ListVpcEndpoints', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/vpc-endpoints' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.MigrateToOtherZoneResponse(),
            self.do_roarequest('MigrateToOtherZone', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/migrate-zones' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ModifyDeployMachineResponse(),
            self.do_roarequest('ModifyDeployMachine', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/collectors/%s/actions/modify-deploy-machines' % TeaConverter.to_unicode(res_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ModifyElastictaskResponse(),
            self.do_roarequest('ModifyElastictask', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/elastic-task' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ModifyInstanceMaintainTimeResponse(),
            self.do_roarequest('ModifyInstanceMaintainTime', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/modify-maintaintime' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        if not UtilClient.is_unset(request.node_type):
            body['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.network_type):
            body['networkType'] = request.network_type
        if not UtilClient.is_unset(request.modify_mode):
            body['modifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.white_ip_list):
            body['whiteIpList'] = request.white_ip_list
        if not UtilClient.is_unset(request.white_ip_group):
            body['whiteIpGroup'] = request.white_ip_group
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ModifyWhiteIpsResponse(),
            self.do_roarequest_with_form('ModifyWhiteIps', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/modify-white-ips' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.MoveResourceGroupResponse(),
            self.do_roarequest('MoveResourceGroup', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/resourcegroup' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.OpenDiagnosisResponse(),
            self.do_roarequest('OpenDiagnosis', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/diagnosis/instances/%s/actions/open-diagnosis' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.OpenHttpsResponse(),
            self.do_roarequest('OpenHttps', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/open-https' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.PostEmonTryAlarmRuleResponse(),
            self.do_roarequest('PostEmonTryAlarmRule', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/emon/projects/%s/alarm-groups/%s/alarm-rules/_test' % (TeaConverter.to_unicode(project_id), TeaConverter.to_unicode(alarm_group_id)), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.RecommendTemplatesResponse(),
            self.do_roarequest('RecommendTemplates', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/instances/%s/recommended-templates' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ReinstallCollectorResponse(),
            self.do_roarequest('ReinstallCollector', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/collectors/%s/actions/reinstall' % TeaConverter.to_unicode(res_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.RenewInstanceResponse(),
            self.do_roarequest('RenewInstance', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/renew' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.RenewLogstashResponse(),
            self.do_roarequest('RenewLogstash', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes/%s/actions/renew' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.RestartCollectorResponse(),
            self.do_roarequest('RestartCollector', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/collectors/%s/actions/restart' % TeaConverter.to_unicode(res_id), 'json', req, runtime)
        )

    def restart_instance(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_instance_with_options(instance_id, request, headers, runtime)

    def restart_instance_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RestartInstanceResponse(),
            self.do_roarequest('RestartInstance', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/restart' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def restart_logstash(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_logstash_with_options(instance_id, request, headers, runtime)

    def restart_logstash_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.RestartLogstashResponse(),
            self.do_roarequest('RestartLogstash', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes/%s/actions/restart' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ResumeElasticsearchTaskResponse(),
            self.do_roarequest('ResumeElasticsearchTask', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/resume' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ResumeLogstashTaskResponse(),
            self.do_roarequest('ResumeLogstashTask', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes/%s/actions/resume' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.RolloverDataStreamResponse(),
            self.do_roarequest('RolloverDataStream', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/data-streams/%s/rollover' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(data_stream)), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.RunPipelinesResponse(),
            self.do_roarequest('RunPipelines', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes/%s/pipelines/action/run' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def shrink_node(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.shrink_node_with_options(instance_id, request, headers, runtime)

    def shrink_node_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ShrinkNodeResponse(),
            self.do_roarequest('ShrinkNode', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/shrink' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.StartCollectorResponse(),
            self.do_roarequest('StartCollector', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/collectors/%s/actions/start' % TeaConverter.to_unicode(res_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.StopCollectorResponse(),
            self.do_roarequest('StopCollector', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/collectors/%s/actions/stop' % TeaConverter.to_unicode(res_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.StopPipelinesResponse(),
            self.do_roarequest('StopPipelines', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes/%s/pipelines/action/stop' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def tag_resources(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(headers, runtime)

    def tag_resources_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.TagResourcesResponse(),
            self.do_roarequest('TagResources', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/tags', 'json', req, runtime)
        )

    def transfer_node(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.transfer_node_with_options(instance_id, request, headers, runtime)

    def transfer_node_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.TransferNodeResponse(),
            self.do_roarequest('TransferNode', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/transfer' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        if not UtilClient.is_unset(request.node_type):
            body['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.network_type):
            body['networkType'] = request.network_type
        if not UtilClient.is_unset(request.action_type):
            body['actionType'] = request.action_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.TriggerNetworkResponse(),
            self.do_roarequest_with_form('TriggerNetwork', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/network-trigger' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UninstallKibanaPluginResponse(),
            self.do_roarequest('UninstallKibanaPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/kibana-plugins/actions/uninstall' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UninstallLogstashPluginResponse(),
            self.do_roarequest('UninstallLogstashPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes/%s/plugins/actions/uninstall' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UninstallPluginResponse(),
            self.do_roarequest('UninstallPlugin', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/plugins/actions/uninstall' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    def untag_resources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UntagResourcesResponse(),
            self.do_roarequest('UntagResources', '2017-06-13', 'HTTPS', 'DELETE', 'AK', '/openapi/tags', 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateAdminPasswordResponse(),
            self.do_roarequest('UpdateAdminPassword', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/admin-pwd' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateAdvancedSettingResponse(),
            self.do_roarequest('UpdateAdvancedSetting', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/update-advanced-setting' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateAliwsDictResponse(),
            self.do_roarequest('UpdateAliwsDict', '2017-06-13', 'HTTPS', 'PUT', 'AK', '/openapi/instances/%s/aliws-dict' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateBlackIpsResponse(),
            self.do_roarequest_with_form('UpdateBlackIps', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/black-ips' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateCollectorResponse(),
            self.do_roarequest('UpdateCollector', '2017-06-13', 'HTTPS', 'PUT', 'AK', '/openapi/collectors/%s' % TeaConverter.to_unicode(res_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateCollectorNameResponse(),
            self.do_roarequest('UpdateCollectorName', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/collectors/%s/actions/rename' % TeaConverter.to_unicode(res_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateDescriptionResponse(),
            self.do_roarequest('UpdateDescription', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/description' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateDiagnosisSettingsResponse(),
            self.do_roarequest('UpdateDiagnosisSettings', '2017-06-13', 'HTTPS', 'PUT', 'AK', '/openapi/diagnosis/instances/%s/settings' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateDictResponse(),
            self.do_roarequest('UpdateDict', '2017-06-13', 'HTTPS', 'PUT', 'AK', '/openapi/instances/%s/dict' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateExtendConfigResponse(),
            self.do_roarequest('UpdateExtendConfig', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/extend-configs/actions/update' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateExtendfilesResponse(),
            self.do_roarequest('UpdateExtendfiles', '2017-06-13', 'HTTPS', 'PUT', 'AK', '/openapi/logstashes/%s/extendfiles' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateHotIkDictsResponse(),
            self.do_roarequest('UpdateHotIkDicts', '2017-06-13', 'HTTPS', 'PUT', 'AK', '/openapi/instances/%s/ik-hot-dict' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateILMPolicyResponse(),
            self.do_roarequest('UpdateILMPolicy', '2017-06-13', 'HTTPS', 'PUT', 'AK', '/openapi/instances/%s/ilm-policies/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(policy_name)), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateIndexTemplateResponse(),
            self.do_roarequest('UpdateIndexTemplate', '2017-06-13', 'HTTPS', 'PUT', 'AK', '/openapi/instances/%s/index-templates/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(index_template)), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateInstanceResponse(),
            self.do_roarequest('UpdateInstance', '2017-06-13', 'HTTPS', 'PUT', 'AK', '/openapi/instances/%s' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateInstanceChargeTypeResponse(),
            self.do_roarequest('UpdateInstanceChargeType', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/convert-pay-type' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateInstanceSettingsResponse(),
            self.do_roarequest('UpdateInstanceSettings', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/instance-settings' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateKibanaSettingsResponse(),
            self.do_roarequest('UpdateKibanaSettings', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/update-kibana-settings' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateKibanaWhiteIpsResponse(),
            self.do_roarequest('UpdateKibanaWhiteIps', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/kibana-white-ips' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateLogstashResponse(),
            self.do_roarequest('UpdateLogstash', '2017-06-13', 'HTTPS', 'PUT', 'AK', '/openapi/logstashes/%s' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateLogstashChargeTypeResponse(),
            self.do_roarequest('UpdateLogstashChargeType', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes/%s/actions/convert-pay-type' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateLogstashDescriptionResponse(),
            self.do_roarequest('UpdateLogstashDescription', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes/%s/description' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateLogstashSettingsResponse(),
            self.do_roarequest('UpdateLogstashSettings', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes/%s/instance-settings' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePipelineManagementConfigResponse(),
            self.do_roarequest('UpdatePipelineManagementConfig', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes/%s/pipeline-management-config' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def update_pipelines(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_pipelines_with_options(instance_id, request, headers, runtime)

    def update_pipelines_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.trigger):
            query['trigger'] = request.trigger
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePipelinesResponse(),
            self.do_roarequest('UpdatePipelines', '2017-06-13', 'HTTPS', 'PUT', 'AK', '/openapi/logstashes/%s/pipelines' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePrivateNetworkWhiteIpsResponse(),
            self.do_roarequest('UpdatePrivateNetworkWhiteIps', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/private-network-white-ips' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePublicNetworkResponse(),
            self.do_roarequest('UpdatePublicNetwork', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/public-network' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdatePublicWhiteIpsResponse(),
            self.do_roarequest('UpdatePublicWhiteIps', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/public-white-ips' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateReadWritePolicyResponse(),
            self.do_roarequest('UpdateReadWritePolicy', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/update-read-write-policy' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateSnapshotSettingResponse(),
            self.do_roarequest('UpdateSnapshotSetting', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/snapshot-setting' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateSynonymsDictsResponse(),
            self.do_roarequest('UpdateSynonymsDicts', '2017-06-13', 'HTTPS', 'PUT', 'AK', '/openapi/instances/%s/synonymsDict' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateTemplateResponse(),
            self.do_roarequest('UpdateTemplate', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/templates/%s' % (TeaConverter.to_unicode(instance_id), TeaConverter.to_unicode(template_name)), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateWhiteIpsResponse(),
            self.do_roarequest_with_form('UpdateWhiteIps', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/white-ips' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpdateXpackMonitorConfigResponse(),
            self.do_roarequest('UpdateXpackMonitorConfig', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes/%s/xpack-monitor-config' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.UpgradeEngineVersionResponse(),
            self.do_roarequest_with_form('UpgradeEngineVersion', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/actions/upgrade-version' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ValidateConnectionResponse(),
            self.do_roarequest('ValidateConnection', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/logstashes/%s/validate-connection' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )

    def validate_shrink_nodes(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_shrink_nodes_with_options(instance_id, request, headers, runtime)

    def validate_shrink_nodes_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.node_type):
            query['nodeType'] = request.node_type
        if not UtilClient.is_unset(request.ignore_status):
            query['ignoreStatus'] = request.ignore_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ValidateShrinkNodesResponse(),
            self.do_roarequest('ValidateShrinkNodes', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/validate-shrink-nodes' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
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
        return TeaCore.from_map(
            elasticsearch_20170613_models.ValidateSlrPermissionResponse(),
            self.do_roarequest('ValidateSlrPermission', '2017-06-13', 'HTTPS', 'GET', 'AK', '/openapi/user/servicerolepermission', 'json', req, runtime)
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
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            elasticsearch_20170613_models.ValidateTransferableNodesResponse(),
            self.do_roarequest('ValidateTransferableNodes', '2017-06-13', 'HTTPS', 'POST', 'AK', '/openapi/instances/%s/validate-transfer-nodes' % TeaConverter.to_unicode(instance_id), 'json', req, runtime)
        )
