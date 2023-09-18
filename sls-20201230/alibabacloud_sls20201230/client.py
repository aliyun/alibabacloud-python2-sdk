# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_gateway_spi.client import Client as SPIClient
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_sls.client import Client as GatewayClientClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_sls20201230 import models as sls_20201230_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    _client = None  # type: SPIClient

    def __init__(self, config):
        super(Client, self).__init__(config)
        self._client = GatewayClientClient()
        self._spi = self._client
        self._endpoint_rule = 'central'

    def apply_config_to_machine_group_with_options(self, project, machine_group, config_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ApplyConfigToMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups/%s/configs/%s' % (TeaConverter.to_unicode(machine_group), TeaConverter.to_unicode(config_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ApplyConfigToMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    def apply_config_to_machine_group(self, project, machine_group, config_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.apply_config_to_machine_group_with_options(project, machine_group, config_name, headers, runtime)

    def change_resource_group_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/resourcegroup',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.ChangeResourceGroupResponse(),
            self.execute(params, req, runtime)
        )

    def change_resource_group(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(project, request, headers, runtime)

    def consumer_group_heart_beat_with_options(self, project, logstore, consumer_group, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.consumer):
            query['consumer'] = request.consumer
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='ConsumerGroupHeartBeat',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/consumergroups/%s?type=heartbeat' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(consumer_group)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.ConsumerGroupHeartBeatResponse(),
            self.execute(params, req, runtime)
        )

    def consumer_group_heart_beat(self, project, logstore, consumer_group, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.consumer_group_heart_beat_with_options(project, logstore, consumer_group, request, headers, runtime)

    def create_annotation_data_set_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['datasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateAnnotationDataSet',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateAnnotationDataSetResponse(),
            self.execute(params, req, runtime)
        )

    def create_annotation_data_set(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_annotation_data_set_with_options(request, headers, runtime)

    def create_annotation_label_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateAnnotationLabel',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationlabel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateAnnotationLabelResponse(),
            self.execute(params, req, runtime)
        )

    def create_annotation_label(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_annotation_label_with_options(request, headers, runtime)

    def create_config_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/configs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateConfigResponse(),
            self.execute(params, req, runtime)
        )

    def create_config(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_config_with_options(project, request, headers, runtime)

    def create_consumer_group_with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.consumer_group):
            body['consumerGroup'] = request.consumer_group
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/consumergroups' % TeaConverter.to_unicode(logstore),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    def create_consumer_group(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_consumer_group_with_options(project, logstore, request, headers, runtime)

    def create_dashboard_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/dashboards',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateDashboardResponse(),
            self.execute(params, req, runtime)
        )

    def create_dashboard(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_dashboard_with_options(project, request, headers, runtime)

    def create_domain_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['domainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/domains',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateDomainResponse(),
            self.execute(params, req, runtime)
        )

    def create_domain(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_domain_with_options(project, request, headers, runtime)

    def create_index_with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.keys):
            body['keys'] = request.keys
        if not UtilClient.is_unset(request.line):
            body['line'] = request.line
        if not UtilClient.is_unset(request.log_reduce):
            body['log_reduce'] = request.log_reduce
        if not UtilClient.is_unset(request.log_reduce_black_list):
            body['log_reduce_black_list'] = request.log_reduce_black_list
        if not UtilClient.is_unset(request.log_reduce_white_list):
            body['log_reduce_white_list'] = request.log_reduce_white_list
        if not UtilClient.is_unset(request.max_text_len):
            body['max_text_len'] = request.max_text_len
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/index' % TeaConverter.to_unicode(logstore),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateIndexResponse(),
            self.execute(params, req, runtime)
        )

    def create_index(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_index_with_options(project, logstore, request, headers, runtime)

    def create_log_store_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not UtilClient.is_unset(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not UtilClient.is_unset(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not UtilClient.is_unset(request.encrypt_conf):
            body['encrypt_conf'] = request.encrypt_conf
        if not UtilClient.is_unset(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not UtilClient.is_unset(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not UtilClient.is_unset(request.mode):
            body['mode'] = request.mode
        if not UtilClient.is_unset(request.shard_count):
            body['shardCount'] = request.shard_count
        if not UtilClient.is_unset(request.telemetry_type):
            body['telemetryType'] = request.telemetry_type
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    def create_log_store(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_log_store_with_options(project, request, headers, runtime)

    def create_logging_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.logging_details):
            body['loggingDetails'] = request.logging_details
        if not UtilClient.is_unset(request.logging_project):
            body['loggingProject'] = request.logging_project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogging',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logging',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateLoggingResponse(),
            self.execute(params, req, runtime)
        )

    def create_logging(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_logging_with_options(project, request, headers, runtime)

    def create_logtail_pipeline_config_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.aggregators):
            body['aggregators'] = request.aggregators
        if not UtilClient.is_unset(request.config_name):
            body['configName'] = request.config_name
        if not UtilClient.is_unset(request.flushers):
            body['flushers'] = request.flushers
        if not UtilClient.is_unset(request.global_):
            body['global'] = request.global_
        if not UtilClient.is_unset(request.inputs):
            body['inputs'] = request.inputs
        if not UtilClient.is_unset(request.log_sample):
            body['logSample'] = request.log_sample
        if not UtilClient.is_unset(request.processors):
            body['processors'] = request.processors
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/pipelineconfigs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    def create_logtail_pipeline_config(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_logtail_pipeline_config_with_options(project, request, headers, runtime)

    def create_machine_group_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.group_attribute):
            body['groupAttribute'] = request.group_attribute
        if not UtilClient.is_unset(request.group_name):
            body['groupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            body['groupType'] = request.group_type
        if not UtilClient.is_unset(request.machine_identify_type):
            body['machineIdentifyType'] = request.machine_identify_type
        if not UtilClient.is_unset(request.machine_list):
            body['machineList'] = request.machine_list
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    def create_machine_group(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_machine_group_with_options(project, request, headers, runtime)

    def create_odps_shipper_with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.shipper_name):
            body['shipperName'] = request.shipper_name
        if not UtilClient.is_unset(request.target_configuration):
            body['targetConfiguration'] = request.target_configuration
        if not UtilClient.is_unset(request.target_type):
            body['targetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOdpsShipper',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shipper' % TeaConverter.to_unicode(logstore),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateOdpsShipperResponse(),
            self.execute(params, req, runtime)
        )

    def create_odps_shipper(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_odps_shipper_with_options(project, logstore, request, headers, runtime)

    def create_oss_external_store_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.external_store_name):
            body['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.parameter):
            body['parameter'] = request.parameter
        if not UtilClient.is_unset(request.store_type):
            body['storeType'] = request.store_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOssExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/externalstores',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateOssExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    def create_oss_external_store(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_oss_external_store_with_options(project, request, headers, runtime)

    def create_oss_shipper_with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.shipper_name):
            body['shipperName'] = request.shipper_name
        if not UtilClient.is_unset(request.target_configuration):
            body['targetConfiguration'] = request.target_configuration
        if not UtilClient.is_unset(request.target_type):
            body['targetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOssShipper',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shipper' % TeaConverter.to_unicode(logstore),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateOssShipperResponse(),
            self.execute(params, req, runtime)
        )

    def create_oss_shipper(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_oss_shipper_with_options(project, logstore, request, headers, runtime)

    def create_project_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_redundancy_type):
            body['dataRedundancyType'] = request.data_redundancy_type
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateProjectResponse(),
            self.execute(params, req, runtime)
        )

    def create_project(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    def create_rds_external_store_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.external_store_name):
            body['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.parameter):
            body['parameter'] = request.parameter
        if not UtilClient.is_unset(request.store_type):
            body['storeType'] = request.store_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRdsExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/externalstores',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateRdsExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    def create_rds_external_store(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_rds_external_store_with_options(project, request, headers, runtime)

    def create_saved_search_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.logstore):
            body['logstore'] = request.logstore
        if not UtilClient.is_unset(request.savedsearch_name):
            body['savedsearchName'] = request.savedsearch_name
        if not UtilClient.is_unset(request.search_query):
            body['searchQuery'] = request.search_query
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/savedsearches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    def create_saved_search(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_saved_search_with_options(project, request, headers, runtime)

    def delete_annotation_data_with_options(self, dataset_id, annotationdata_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAnnotationData',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset/%s/annotationdata/%s' % (TeaConverter.to_unicode(dataset_id), TeaConverter.to_unicode(annotationdata_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteAnnotationDataResponse(),
            self.execute(params, req, runtime)
        )

    def delete_annotation_data(self, dataset_id, annotationdata_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_annotation_data_with_options(dataset_id, annotationdata_id, headers, runtime)

    def delete_annotation_data_set_with_options(self, dataset_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAnnotationDataSet',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset/%s' % TeaConverter.to_unicode(dataset_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteAnnotationDataSetResponse(),
            self.execute(params, req, runtime)
        )

    def delete_annotation_data_set(self, dataset_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_annotation_data_set_with_options(dataset_id, headers, runtime)

    def delete_annotation_label_with_options(self, label_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAnnotationLabel',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationlabel/%s' % TeaConverter.to_unicode(label_id),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteAnnotationLabelResponse(),
            self.execute(params, req, runtime)
        )

    def delete_annotation_label(self, label_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_annotation_label_with_options(label_id, headers, runtime)

    def delete_config_with_options(self, project, config_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/configs/%s' % TeaConverter.to_unicode(config_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteConfigResponse(),
            self.execute(params, req, runtime)
        )

    def delete_config(self, project, config_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_config_with_options(project, config_name, headers, runtime)

    def delete_consumer_group_with_options(self, project, logstore, consumer_group, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/consumergroups/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(consumer_group)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    def delete_consumer_group(self, project, logstore, consumer_group):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_consumer_group_with_options(project, logstore, consumer_group, headers, runtime)

    def delete_dashboard_with_options(self, project, dashboard_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/dashboards/%s' % TeaConverter.to_unicode(dashboard_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteDashboardResponse(),
            self.execute(params, req, runtime)
        )

    def delete_dashboard(self, project, dashboard_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_dashboard_with_options(project, dashboard_name, headers, runtime)

    def delete_domain_with_options(self, project, domain_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/domains/%s' % TeaConverter.to_unicode(domain_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteDomainResponse(),
            self.execute(params, req, runtime)
        )

    def delete_domain(self, project, domain_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_domain_with_options(project, domain_name, headers, runtime)

    def delete_external_store_with_options(self, project, external_store_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/externalstores/%s' % TeaConverter.to_unicode(external_store_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    def delete_external_store(self, project, external_store_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_external_store_with_options(project, external_store_name, headers, runtime)

    def delete_index_with_options(self, project, logstore, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/index' % TeaConverter.to_unicode(logstore),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteIndexResponse(),
            self.execute(params, req, runtime)
        )

    def delete_index(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_index_with_options(project, logstore, headers, runtime)

    def delete_log_store_with_options(self, project, logstore, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s' % TeaConverter.to_unicode(logstore),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    def delete_log_store(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_log_store_with_options(project, logstore, headers, runtime)

    def delete_logging_with_options(self, project, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLogging',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logging',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteLoggingResponse(),
            self.execute(params, req, runtime)
        )

    def delete_logging(self, project):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_logging_with_options(project, headers, runtime)

    def delete_logtail_pipeline_config_with_options(self, project, config_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/pipelineconfigs/%s' % TeaConverter.to_unicode(config_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    def delete_logtail_pipeline_config(self, project, config_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_logtail_pipeline_config_with_options(project, config_name, headers, runtime)

    def delete_machine_group_with_options(self, project, machine_group, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups/%s' % TeaConverter.to_unicode(machine_group),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    def delete_machine_group(self, project, machine_group):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_machine_group_with_options(project, machine_group, headers, runtime)

    def delete_project_with_options(self, project, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteProjectResponse(),
            self.execute(params, req, runtime)
        )

    def delete_project(self, project):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(project, headers, runtime)

    def delete_project_policy_with_options(self, project, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProjectPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/policy',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteProjectPolicyResponse(),
            self.execute(params, req, runtime)
        )

    def delete_project_policy(self, project):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_policy_with_options(project, headers, runtime)

    def delete_saved_search_with_options(self, project, savedsearch_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/savedsearches/%s' % TeaConverter.to_unicode(savedsearch_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    def delete_saved_search(self, project, savedsearch_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_saved_search_with_options(project, savedsearch_name, headers, runtime)

    def delete_shipper_with_options(self, project, logstore, shipper_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteShipper',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shipper/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shipper_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteShipperResponse(),
            self.execute(params, req, runtime)
        )

    def delete_shipper(self, project, logstore, shipper_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_shipper_with_options(project, logstore, shipper_name, headers, runtime)

    def get_annotation_data_with_options(self, dataset_id, annotationdata_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAnnotationData',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset/%s/annotationdata/%s' % (TeaConverter.to_unicode(dataset_id), TeaConverter.to_unicode(annotationdata_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAnnotationDataResponse(),
            self.execute(params, req, runtime)
        )

    def get_annotation_data(self, dataset_id, annotationdata_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_annotation_data_with_options(dataset_id, annotationdata_id, headers, runtime)

    def get_annotation_data_set_with_options(self, dataset_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAnnotationDataSet',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset/%s' % TeaConverter.to_unicode(dataset_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAnnotationDataSetResponse(),
            self.execute(params, req, runtime)
        )

    def get_annotation_data_set(self, dataset_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_annotation_data_set_with_options(dataset_id, headers, runtime)

    def get_annotation_label_with_options(self, label_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAnnotationLabel',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationlabel/%s' % TeaConverter.to_unicode(label_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAnnotationLabelResponse(),
            self.execute(params, req, runtime)
        )

    def get_annotation_label(self, label_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_annotation_label_with_options(label_id, headers, runtime)

    def get_applied_configs_with_options(self, project, machine_group, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAppliedConfigs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups/%s/configs' % TeaConverter.to_unicode(machine_group),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAppliedConfigsResponse(),
            self.execute(params, req, runtime)
        )

    def get_applied_configs(self, project, machine_group):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_applied_configs_with_options(project, machine_group, headers, runtime)

    def get_applied_machine_groups_with_options(self, project, config_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAppliedMachineGroups',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/configs/%s/machinegroups' % TeaConverter.to_unicode(config_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAppliedMachineGroupsResponse(),
            self.execute(params, req, runtime)
        )

    def get_applied_machine_groups(self, project, config_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_applied_machine_groups_with_options(project, config_name, headers, runtime)

    def get_check_point_with_options(self, project, logstore, consumer_group, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.shard):
            query['shard'] = request.shard
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCheckPoint',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/consumergroups/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(consumer_group)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetCheckPointResponse(),
            self.execute(params, req, runtime)
        )

    def get_check_point(self, project, logstore, consumer_group, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_check_point_with_options(project, logstore, consumer_group, request, headers, runtime)

    def get_config_with_options(self, project, config_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/configs/%s' % TeaConverter.to_unicode(config_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetConfigResponse(),
            self.execute(params, req, runtime)
        )

    def get_config(self, project, config_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_config_with_options(project, config_name, headers, runtime)

    def get_context_logs_with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.back_lines):
            query['back_lines'] = request.back_lines
        if not UtilClient.is_unset(request.forward_lines):
            query['forward_lines'] = request.forward_lines
        if not UtilClient.is_unset(request.pack_id):
            query['pack_id'] = request.pack_id
        if not UtilClient.is_unset(request.pack_meta):
            query['pack_meta'] = request.pack_meta
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetContextLogs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetContextLogsResponse(),
            self.execute(params, req, runtime)
        )

    def get_context_logs(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_context_logs_with_options(project, logstore, request, headers, runtime)

    def get_cursor_with_options(self, project, logstore, shard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCursor',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards/%s?type=cursor' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shard_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetCursorResponse(),
            self.execute(params, req, runtime)
        )

    def get_cursor(self, project, logstore, shard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cursor_with_options(project, logstore, shard_id, request, headers, runtime)

    def get_cursor_time_with_options(self, project, logstore, shard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.cursor):
            query['cursor'] = request.cursor
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCursorTime',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards/%s?type=cursor_time' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shard_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetCursorTimeResponse(),
            self.execute(params, req, runtime)
        )

    def get_cursor_time(self, project, logstore, shard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cursor_time_with_options(project, logstore, shard_id, request, headers, runtime)

    def get_dashboard_with_options(self, project, dashboard_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/dashboards/%s' % TeaConverter.to_unicode(dashboard_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetDashboardResponse(),
            self.execute(params, req, runtime)
        )

    def get_dashboard(self, project, dashboard_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_dashboard_with_options(project, dashboard_name, headers, runtime)

    def get_external_store_with_options(self, project, external_store_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/externalstores/%s' % TeaConverter.to_unicode(external_store_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    def get_external_store(self, project, external_store_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_external_store_with_options(project, external_store_name, headers, runtime)

    def get_histograms_with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        if not UtilClient.is_unset(request.topic):
            query['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistograms',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/index?type=histogram' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetHistogramsResponse(),
            self.execute(params, req, runtime)
        )

    def get_histograms(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_histograms_with_options(project, logstore, request, headers, runtime)

    def get_index_with_options(self, project, logstore, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/index' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetIndexResponse(),
            self.execute(params, req, runtime)
        )

    def get_index(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_index_with_options(project, logstore, headers, runtime)

    def get_log_store_with_options(self, project, logstore, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    def get_log_store(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_log_store_with_options(project, logstore, headers, runtime)

    def get_logging_with_options(self, project, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogging',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logging',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLoggingResponse(),
            self.execute(params, req, runtime)
        )

    def get_logging(self, project):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_logging_with_options(project, headers, runtime)

    def get_logs_with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.line):
            query['line'] = request.line
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.power_sql):
            query['powerSql'] = request.power_sql
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.reverse):
            query['reverse'] = request.reverse
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        if not UtilClient.is_unset(request.topic):
            query['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLogs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s?type=log' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogsResponse(),
            self.execute(params, req, runtime)
        )

    def get_logs(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_logs_with_options(project, logstore, request, headers, runtime)

    def get_logs_v2with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.forward):
            body['forward'] = request.forward
        if not UtilClient.is_unset(request.from_):
            body['from'] = request.from_
        if not UtilClient.is_unset(request.line):
            body['line'] = request.line
        if not UtilClient.is_unset(request.offset):
            body['offset'] = request.offset
        if not UtilClient.is_unset(request.power_sql):
            body['powerSql'] = request.power_sql
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.reverse):
            body['reverse'] = request.reverse
        if not UtilClient.is_unset(request.session):
            body['session'] = request.session
        if not UtilClient.is_unset(request.shard):
            body['shard'] = request.shard
        if not UtilClient.is_unset(request.to):
            body['to'] = request.to
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.accept_encoding):
            real_headers['Accept-Encoding'] = UtilClient.to_jsonstring(headers.accept_encoding)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLogsV2',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/logs' % TeaConverter.to_unicode(logstore),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogsV2Response(),
            self.execute(params, req, runtime)
        )

    def get_logs_v2(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = sls_20201230_models.GetLogsV2Headers()
        return self.get_logs_v2with_options(project, logstore, request, headers, runtime)

    def get_logtail_pipeline_config_with_options(self, project, config_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/pipelineconfigs/%s' % TeaConverter.to_unicode(config_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    def get_logtail_pipeline_config(self, project, config_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_logtail_pipeline_config_with_options(project, config_name, headers, runtime)

    def get_machine_group_with_options(self, project, machine_group, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups/%s' % TeaConverter.to_unicode(machine_group),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    def get_machine_group(self, project, machine_group):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_machine_group_with_options(project, machine_group, headers, runtime)

    def get_project_with_options(self, project, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetProjectResponse(),
            self.execute(params, req, runtime)
        )

    def get_project(self, project):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(project, headers, runtime)

    def get_project_logs_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.power_sql):
            query['powerSql'] = request.power_sql
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectLogs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetProjectLogsResponse(),
            self.execute(params, req, runtime)
        )

    def get_project_logs(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_logs_with_options(project, request, headers, runtime)

    def get_project_policy_with_options(self, project, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/policy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetProjectPolicyResponse(),
            self.execute(params, req, runtime)
        )

    def get_project_policy(self, project):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_policy_with_options(project, headers, runtime)

    def get_saved_search_with_options(self, project, savedsearch_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/savedsearches/%s' % TeaConverter.to_unicode(savedsearch_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    def get_saved_search(self, project, savedsearch_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_saved_search_with_options(project, savedsearch_name, headers, runtime)

    def get_shipper_status_with_options(self, project, logstore, shipper_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetShipperStatus',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shipper/%s/tasks' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shipper_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetShipperStatusResponse(),
            self.execute(params, req, runtime)
        )

    def get_shipper_status(self, project, logstore, shipper_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_shipper_status_with_options(project, logstore, shipper_name, request, headers, runtime)

    def list_annotation_data_with_options(self, dataset_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnnotationData',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset/%s/annotationdata' % TeaConverter.to_unicode(dataset_id),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListAnnotationDataResponse(),
            self.execute(params, req, runtime)
        )

    def list_annotation_data(self, dataset_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_annotation_data_with_options(dataset_id, request, headers, runtime)

    def list_annotation_data_sets_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnnotationDataSets',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListAnnotationDataSetsResponse(),
            self.execute(params, req, runtime)
        )

    def list_annotation_data_sets(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_annotation_data_sets_with_options(request, headers, runtime)

    def list_annotation_labels_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnnotationLabels',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationlabel',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListAnnotationLabelsResponse(),
            self.execute(params, req, runtime)
        )

    def list_annotation_labels(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_annotation_labels_with_options(request, headers, runtime)

    def list_config_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['configName'] = request.config_name
        if not UtilClient.is_unset(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListConfigResponse(),
            self.execute(params, req, runtime)
        )

    def list_config(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_config_with_options(project, request, headers, runtime)

    def list_consumer_group_with_options(self, project, logstore, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ListConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/consumergroups' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    def list_consumer_group(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_consumer_group_with_options(project, logstore, headers, runtime)

    def list_dashboard_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/dashboards',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListDashboardResponse(),
            self.execute(params, req, runtime)
        )

    def list_dashboard(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_with_options(project, request, headers, runtime)

    def list_domains_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['domainName'] = request.domain_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/domains',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListDomainsResponse(),
            self.execute(params, req, runtime)
        )

    def list_domains(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_domains_with_options(project, request, headers, runtime)

    def list_external_store_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.external_store_name):
            query['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.sizs):
            query['sizs'] = request.sizs
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/externalstores',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    def list_external_store(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_external_store_with_options(project, request, headers, runtime)

    def list_log_stores_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.mode):
            query['mode'] = request.mode
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.telemetry_type):
            query['telemetryType'] = request.telemetry_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogStores',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListLogStoresResponse(),
            self.execute(params, req, runtime)
        )

    def list_log_stores(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_log_stores_with_options(project, request, headers, runtime)

    def list_logtail_pipeline_config_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['configName'] = request.config_name
        if not UtilClient.is_unset(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/pipelineconfigs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    def list_logtail_pipeline_config(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logtail_pipeline_config_with_options(project, request, headers, runtime)

    def list_machine_group_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['groupName'] = request.group_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    def list_machine_group(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_machine_group_with_options(project, request, headers, runtime)

    def list_machines_with_options(self, project, machine_group, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMachines',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups/%s/machines' % TeaConverter.to_unicode(machine_group),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListMachinesResponse(),
            self.execute(params, req, runtime)
        )

    def list_machines(self, project, machine_group, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_machines_with_options(project, machine_group, request, headers, runtime)

    def list_project_with_options(self, resource_group_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.project_name):
            query['projectName'] = request.project_name
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListProjectResponse(),
            self.execute(params, req, runtime)
        )

    def list_project(self, resource_group_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_with_options(resource_group_id, request, headers, runtime)

    def list_saved_search_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/savedsearches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    def list_saved_search(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_saved_search_with_options(project, request, headers, runtime)

    def list_shards_with_options(self, project, logstore, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ListShards',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListShardsResponse(),
            self.execute(params, req, runtime)
        )

    def list_shards(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_shards_with_options(project, logstore, headers, runtime)

    def list_shipper_with_options(self, project, logstore, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ListShipper',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shipper' % TeaConverter.to_unicode(logstore),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListShipperResponse(),
            self.execute(params, req, runtime)
        )

    def list_shipper(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_shipper_with_options(project, logstore, headers, runtime)

    def list_tag_resources_with_options(self, tmp_req, headers, runtime):
        UtilClient.validate_model(tmp_req)
        request = sls_20201230_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListTagResourcesResponse(),
            self.execute(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    def pull_data_with_options(self, project, logstore, shard, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.cursor):
            query['cursor'] = request.cursor
        if not UtilClient.is_unset(request.end_cursor):
            query['endCursor'] = request.end_cursor
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PullData',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards/%s?type=log' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shard)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.PullDataResponse(),
            self.execute(params, req, runtime)
        )

    def pull_data(self, project, logstore, shard, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pull_data_with_options(project, logstore, shard, request, headers, runtime)

    def put_annotation_data_with_options(self, dataset_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotationdata_id):
            query['annotationdataId'] = request.annotationdata_id
        body = {}
        if not UtilClient.is_unset(request.ml_data_param):
            body['mlDataParam'] = request.ml_data_param
        if not UtilClient.is_unset(request.raw_log):
            body['rawLog'] = request.raw_log
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAnnotationData',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset/%s/annotationdata' % TeaConverter.to_unicode(dataset_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.PutAnnotationDataResponse(),
            self.execute(params, req, runtime)
        )

    def put_annotation_data(self, dataset_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_annotation_data_with_options(dataset_id, request, headers, runtime)

    def put_project_policy_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='PutProjectPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/policy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.PutProjectPolicyResponse(),
            self.execute(params, req, runtime)
        )

    def put_project_policy(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_project_policy_with_options(project, request, headers, runtime)

    def put_webtracking_with_options(self, project, logstore_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.logs):
            body['__logs__'] = request.logs
        if not UtilClient.is_unset(request.source):
            body['__source__'] = request.source
        if not UtilClient.is_unset(request.tags):
            body['__tags__'] = request.tags
        if not UtilClient.is_unset(request.topic):
            body['__topic__'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutWebtracking',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/track' % TeaConverter.to_unicode(logstore_name),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.PutWebtrackingResponse(),
            self.execute(params, req, runtime)
        )

    def put_webtracking(self, project, logstore_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_webtracking_with_options(project, logstore_name, request, headers, runtime)

    def query_mlservice_results_with_options(self, service_name, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_builtin):
            query['allowBuiltin'] = request.allow_builtin
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryMLServiceResults',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/service/%s/analysis' % TeaConverter.to_unicode(service_name),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.QueryMLServiceResultsResponse(),
            self.execute(params, req, runtime)
        )

    def query_mlservice_results(self, service_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_mlservice_results_with_options(service_name, request, headers, runtime)

    def remove_config_from_machine_group_with_options(self, project, machine_group, config_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveConfigFromMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups/%s/configs/%s' % (TeaConverter.to_unicode(machine_group), TeaConverter.to_unicode(config_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.RemoveConfigFromMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    def remove_config_from_machine_group(self, project, machine_group, config_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_config_from_machine_group_with_options(project, machine_group, config_name, headers, runtime)

    def split_shard_with_options(self, project, logstore, shard, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        if not UtilClient.is_unset(request.shard_count):
            query['shardCount'] = request.shard_count
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SplitShard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards/%s?action=split' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shard)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.SplitShardResponse(),
            self.execute(params, req, runtime)
        )

    def split_shard(self, project, logstore, shard, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.split_shard_with_options(project, logstore, shard, request, headers, runtime)

    def tag_resources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/tag',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.TagResourcesResponse(),
            self.execute(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    def untag_resources_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all):
            body['all'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/untag',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.UntagResourcesResponse(),
            self.execute(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    def update_annotation_data_set_with_options(self, dataset_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateAnnotationDataSet',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationdataset/%s' % TeaConverter.to_unicode(dataset_id),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateAnnotationDataSetResponse(),
            self.execute(params, req, runtime)
        )

    def update_annotation_data_set(self, dataset_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_annotation_data_set_with_options(dataset_id, request, headers, runtime)

    def update_annotation_label_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateAnnotationLabel',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/ml/annotationlabel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateAnnotationLabelResponse(),
            self.execute(params, req, runtime)
        )

    def update_annotation_label(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_annotation_label_with_options(request, headers, runtime)

    def update_config_with_options(self, project, config_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/configs/%s' % TeaConverter.to_unicode(config_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateConfigResponse(),
            self.execute(params, req, runtime)
        )

    def update_config(self, project, config_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_config_with_options(project, config_name, request, headers, runtime)

    def update_consumer_group_with_options(self, project, logstore, consumer_group, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/consumergroups/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(consumer_group)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    def update_consumer_group(self, project, logstore, consumer_group, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_consumer_group_with_options(project, logstore, consumer_group, request, headers, runtime)

    def update_dashboard_with_options(self, project, dashboard_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.attribute):
            body['attribute'] = request.attribute
        if not UtilClient.is_unset(request.charts):
            body['charts'] = request.charts
        if not UtilClient.is_unset(request.dashboard_name):
            body['dashboardName'] = request.dashboard_name
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/dashboards/%s' % TeaConverter.to_unicode(dashboard_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateDashboardResponse(),
            self.execute(params, req, runtime)
        )

    def update_dashboard(self, project, dashboard_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_dashboard_with_options(project, dashboard_name, request, headers, runtime)

    def update_index_with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.keys):
            body['keys'] = request.keys
        if not UtilClient.is_unset(request.line):
            body['line'] = request.line
        if not UtilClient.is_unset(request.log_reduce):
            body['log_reduce'] = request.log_reduce
        if not UtilClient.is_unset(request.log_reduce_black_list):
            body['log_reduce_black_list'] = request.log_reduce_black_list
        if not UtilClient.is_unset(request.log_reduce_white_list):
            body['log_reduce_white_list'] = request.log_reduce_white_list
        if not UtilClient.is_unset(request.max_text_len):
            body['max_text_len'] = request.max_text_len
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/index' % TeaConverter.to_unicode(logstore),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateIndexResponse(),
            self.execute(params, req, runtime)
        )

    def update_index(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_index_with_options(project, logstore, request, headers, runtime)

    def update_log_store_with_options(self, project, logstore, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not UtilClient.is_unset(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not UtilClient.is_unset(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not UtilClient.is_unset(request.encrypt_conf):
            body['encrypt_conf'] = request.encrypt_conf
        if not UtilClient.is_unset(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not UtilClient.is_unset(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not UtilClient.is_unset(request.mode):
            body['mode'] = request.mode
        if not UtilClient.is_unset(request.shard_count):
            body['shardCount'] = request.shard_count
        if not UtilClient.is_unset(request.telemetry_type):
            body['telemetryType'] = request.telemetry_type
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s' % TeaConverter.to_unicode(logstore),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    def update_log_store(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_log_store_with_options(project, logstore, request, headers, runtime)

    def update_logging_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.logging_details):
            body['loggingDetails'] = request.logging_details
        if not UtilClient.is_unset(request.logging_project):
            body['loggingProject'] = request.logging_project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogging',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logging',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLoggingResponse(),
            self.execute(params, req, runtime)
        )

    def update_logging(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logging_with_options(project, request, headers, runtime)

    def update_logtail_pipeline_config_with_options(self, project, config_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.aggregators):
            body['aggregators'] = request.aggregators
        if not UtilClient.is_unset(request.config_name):
            body['configName'] = request.config_name
        if not UtilClient.is_unset(request.flushers):
            body['flushers'] = request.flushers
        if not UtilClient.is_unset(request.global_):
            body['global'] = request.global_
        if not UtilClient.is_unset(request.inputs):
            body['inputs'] = request.inputs
        if not UtilClient.is_unset(request.log_sample):
            body['logSample'] = request.log_sample
        if not UtilClient.is_unset(request.processors):
            body['processors'] = request.processors
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/pipelineconfigs/%s' % TeaConverter.to_unicode(config_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    def update_logtail_pipeline_config(self, project, config_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logtail_pipeline_config_with_options(project, config_name, request, headers, runtime)

    def update_machine_group_with_options(self, project, group_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.group_attribute):
            body['groupAttribute'] = request.group_attribute
        if not UtilClient.is_unset(request.group_name):
            body['groupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            body['groupType'] = request.group_type
        if not UtilClient.is_unset(request.machine_identify_type):
            body['machineIdentifyType'] = request.machine_identify_type
        if not UtilClient.is_unset(request.machine_list):
            body['machineList'] = request.machine_list
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups/%s' % TeaConverter.to_unicode(group_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    def update_machine_group(self, project, group_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_machine_group_with_options(project, group_name, request, headers, runtime)

    def update_machine_group_machine_with_options(self, project, machine_group, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateMachineGroupMachine',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/machinegroups/%s/machines' % TeaConverter.to_unicode(machine_group),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateMachineGroupMachineResponse(),
            self.execute(params, req, runtime)
        )

    def update_machine_group_machine(self, project, machine_group, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_machine_group_machine_with_options(project, machine_group, request, headers, runtime)

    def update_odps_shipper_with_options(self, project, logstore, shipper_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.shipper_name):
            body['shipperName'] = request.shipper_name
        if not UtilClient.is_unset(request.target_configuration):
            body['targetConfiguration'] = request.target_configuration
        if not UtilClient.is_unset(request.target_type):
            body['targetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateOdpsShipper',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shipper/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shipper_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateOdpsShipperResponse(),
            self.execute(params, req, runtime)
        )

    def update_odps_shipper(self, project, logstore, shipper_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_odps_shipper_with_options(project, logstore, shipper_name, request, headers, runtime)

    def update_oss_external_store_with_options(self, project, external_store_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.external_store_name):
            body['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.parameter):
            body['parameter'] = request.parameter
        if not UtilClient.is_unset(request.store_type):
            body['storeType'] = request.store_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateOssExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/externalstores/%s' % TeaConverter.to_unicode(external_store_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateOssExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    def update_oss_external_store(self, project, external_store_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_oss_external_store_with_options(project, external_store_name, request, headers, runtime)

    def update_oss_shipper_with_options(self, project, logstore, shipper_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.shipper_name):
            body['shipperName'] = request.shipper_name
        if not UtilClient.is_unset(request.target_configuration):
            body['targetConfiguration'] = request.target_configuration
        if not UtilClient.is_unset(request.target_type):
            body['targetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateOssShipper',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shipper/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shipper_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateOssShipperResponse(),
            self.execute(params, req, runtime)
        )

    def update_oss_shipper(self, project, logstore, shipper_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_oss_shipper_with_options(project, logstore, shipper_name, request, headers, runtime)

    def update_project_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateProjectResponse(),
            self.execute(params, req, runtime)
        )

    def update_project(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_with_options(project, request, headers, runtime)

    def update_rds_external_store_with_options(self, project, external_store_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.external_store_name):
            body['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.parameter):
            body['parameter'] = request.parameter
        if not UtilClient.is_unset(request.store_type):
            body['storeType'] = request.store_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRdsExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/externalstores/%s' % TeaConverter.to_unicode(external_store_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateRdsExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    def update_rds_external_store(self, project, external_store_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_rds_external_store_with_options(project, external_store_name, request, headers, runtime)

    def update_saved_search_with_options(self, project, savedsearch_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.logstore):
            body['logstore'] = request.logstore
        if not UtilClient.is_unset(request.savedsearch_name):
            body['savedsearchName'] = request.savedsearch_name
        if not UtilClient.is_unset(request.search_query):
            body['searchQuery'] = request.search_query
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/savedsearches/%s' % TeaConverter.to_unicode(savedsearch_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    def update_saved_search(self, project, savedsearch_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_saved_search_with_options(project, savedsearch_name, request, headers, runtime)
