# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_gateway_spi.client import Client as SPIClient
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_sls.client import Client as GatewayClientClient
from alibabacloud_sls20201230 import models as sls_20201230_models
from alibabacloud_tea_util import models as util_models
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

    def apply_config_to_machine_group(self, project, machine_group, config_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.apply_config_to_machine_group_with_options(project, machine_group, config_name, headers, runtime)

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
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.ApplyConfigToMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    def batch_create_etl_meta(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_create_etl_meta_with_options(project, request, headers, runtime)

    def batch_create_etl_meta_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.etl_meta_list):
            body['etlMetaList'] = request.etl_meta_list
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateEtlMeta',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etlmetas',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.BatchCreateEtlMetaResponse(),
            self.execute(params, req, runtime)
        )

    def batch_modify_etl_meta_status(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_modify_etl_meta_status_with_options(project, request, headers, runtime)

    def batch_modify_etl_meta_status_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.etl_meta_key_list):
            body['etlMetaKeyList'] = request.etl_meta_key_list
        if not UtilClient.is_unset(request.etl_meta_name):
            body['etlMetaName'] = request.etl_meta_name
        if not UtilClient.is_unset(request.etl_meta_tag):
            body['etlMetaTag'] = request.etl_meta_tag
        if not UtilClient.is_unset(request.range):
            body['range'] = request.range
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchModifyEtlMetaStatus',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etlmetas',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.BatchModifyEtlMetaStatusResponse(),
            self.execute(params, req, runtime)
        )

    def batch_update_etl_meta(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_update_etl_meta_with_options(project, request, headers, runtime)

    def batch_update_etl_meta_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.etl_meta_list):
            body['etlMetaList'] = request.etl_meta_list
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUpdateEtlMeta',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etlmetas',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.BatchUpdateEtlMetaResponse(),
            self.execute(params, req, runtime)
        )

    def create_consumer_group(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_consumer_group_with_options(project, logstore, request, headers, runtime)

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

    def create_domain(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_domain_with_options(project, request, headers, runtime)

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

    def create_etl_job(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_etl_job_with_options(project, request, headers, runtime)

    def create_etl_job_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.etl_job_name):
            body['etlJobName'] = request.etl_job_name
        if not UtilClient.is_unset(request.function_config):
            body['functionConfig'] = request.function_config
        if not UtilClient.is_unset(request.function_parameter):
            body['functionParameter'] = request.function_parameter
        if not UtilClient.is_unset(request.log_config):
            body['logConfig'] = request.log_config
        if not UtilClient.is_unset(request.source_config):
            body['sourceConfig'] = request.source_config
        if not UtilClient.is_unset(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEtlJob',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etljobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateEtlJobResponse(),
            self.execute(params, req, runtime)
        )

    def create_etl_meta(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_etl_meta_with_options(project, request, headers, runtime)

    def create_etl_meta_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.etl_meta_key):
            body['etlMetaKey'] = request.etl_meta_key
        if not UtilClient.is_unset(request.etl_meta_name):
            body['etlMetaName'] = request.etl_meta_name
        if not UtilClient.is_unset(request.etl_meta_tag):
            body['etlMetaTag'] = request.etl_meta_tag
        if not UtilClient.is_unset(request.etl_meta_value):
            body['etlMetaValue'] = request.etl_meta_value
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEtlMeta',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etlmetas',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateEtlMetaResponse(),
            self.execute(params, req, runtime)
        )

    def create_index(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_index_with_options(project, logstore, request, headers, runtime)

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

    def create_log_store(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_log_store_with_options(project, request, headers, runtime)

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

    def create_logging(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_logging_with_options(project, request, headers, runtime)

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

    def create_machine_group(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_machine_group_with_options(project, request, headers, runtime)

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

    def create_odps_shipper(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_odps_shipper_with_options(project, logstore, request, headers, runtime)

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

    def create_oss_external_store(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_oss_external_store_with_options(project, request, headers, runtime)

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

    def create_oss_shipper(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_oss_shipper_with_options(project, logstore, request, headers, runtime)

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

    def create_project(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    def create_project_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
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

    def create_rds_external_store(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_rds_external_store_with_options(project, request, headers, runtime)

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

    def create_saved_search(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_saved_search_with_options(project, request, headers, runtime)

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

    def delete_consumer_group(self, project, logstore, consumer_group):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_consumer_group_with_options(project, logstore, consumer_group, headers, runtime)

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

    def delete_domain(self, project, domain_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_domain_with_options(project, domain_name, headers, runtime)

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

    def delete_etl_job(self, project, etl_job_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_etl_job_with_options(project, etl_job_name, headers, runtime)

    def delete_etl_job_with_options(self, project, etl_job_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEtlJob',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etljobs/%s' % TeaConverter.to_unicode(etl_job_name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteEtlJobResponse(),
            self.execute(params, req, runtime)
        )

    def delete_etl_meta(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_etl_meta_with_options(project, request, headers, runtime)

    def delete_etl_meta_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.etl_meta_key):
            query['etlMetaKey'] = request.etl_meta_key
        if not UtilClient.is_unset(request.etl_meta_name):
            query['etlMetaName'] = request.etl_meta_name
        if not UtilClient.is_unset(request.etl_meta_tag):
            query['etlMetaTag'] = request.etl_meta_tag
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEtlMeta',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etlmetas',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteEtlMetaResponse(),
            self.execute(params, req, runtime)
        )

    def delete_external_store(self, project, external_store_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_external_store_with_options(project, external_store_name, headers, runtime)

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

    def delete_index(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_index_with_options(project, logstore, headers, runtime)

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

    def delete_log_store(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_log_store_with_options(project, logstore, headers, runtime)

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

    def delete_logging(self, project):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_logging_with_options(project, headers, runtime)

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

    def delete_machine_group(self, project, machine_group):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_machine_group_with_options(project, machine_group, headers, runtime)

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

    def delete_project(self, project):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(project, headers, runtime)

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

    def delete_saved_search(self, project, savedsearch_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_saved_search_with_options(project, savedsearch_name, headers, runtime)

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

    def delete_shipper(self, project, logstore, shipper_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_shipper_with_options(project, logstore, shipper_name, headers, runtime)

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

    def get_applied_configs(self, project, machine_group):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_applied_configs_with_options(project, machine_group, headers, runtime)

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

    def get_applied_machine_groups(self, project, config_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_applied_machine_groups_with_options(project, config_name, headers, runtime)

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

    def get_check_point(self, project, logstore, consumer_group, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_check_point_with_options(project, logstore, consumer_group, request, headers, runtime)

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

    def get_context_logs(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_context_logs_with_options(project, logstore, request, headers, runtime)

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

    def get_cursor(self, project, logstore, shard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cursor_with_options(project, logstore, shard_id, request, headers, runtime)

    def get_cursor_with_options(self, project, logstore, shard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCursor',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shard_id)),
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

    def get_cursor_time(self, project, logstore, shard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cursor_time_with_options(project, logstore, shard_id, request, headers, runtime)

    def get_cursor_time_with_options(self, project, logstore, shard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.cursor):
            query['cursor'] = request.cursor
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCursorTime',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shard_id)),
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

    def get_etl_job(self, project, etl_job_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_etl_job_with_options(project, etl_job_name, headers, runtime)

    def get_etl_job_with_options(self, project, etl_job_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEtlJob',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etljobs/%s' % TeaConverter.to_unicode(etl_job_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetEtlJobResponse(),
            self.execute(params, req, runtime)
        )

    def get_etl_meta(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_etl_meta_with_options(project, request, headers, runtime)

    def get_etl_meta_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.etl_meta_key):
            query['etlMetaKey'] = request.etl_meta_key
        if not UtilClient.is_unset(request.etl_meta_name):
            query['etlMetaName'] = request.etl_meta_name
        if not UtilClient.is_unset(request.etl_meta_tag):
            query['etlMetaTag'] = request.etl_meta_tag
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEtlMeta',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etlmetas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetEtlMetaResponse(),
            self.execute(params, req, runtime)
        )

    def get_external_store(self, project, external_store_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_external_store_with_options(project, external_store_name, headers, runtime)

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

    def get_histograms(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_histograms_with_options(project, logstore, request, headers, runtime)

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

    def get_index(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_index_with_options(project, logstore, headers, runtime)

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

    def get_log_store(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_log_store_with_options(project, logstore, headers, runtime)

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

    def get_logging(self, project):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_logging_with_options(project, headers, runtime)

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

    def get_logs(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_logs_with_options(project, logstore, request, headers, runtime)

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

    def get_machine_group(self, project, machine_group):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_machine_group_with_options(project, machine_group, headers, runtime)

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

    def get_project(self, project):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(project, headers, runtime)

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

    def get_project_logs(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_logs_with_options(project, request, headers, runtime)

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

    def get_saved_search(self, project, savedsearch_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_saved_search_with_options(project, savedsearch_name, headers, runtime)

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

    def get_shipper_config(self, project, logstore, shipper_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_shipper_config_with_options(project, logstore, shipper_name, headers, runtime)

    def get_shipper_config_with_options(self, project, logstore, shipper_name, headers, runtime):
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetShipperConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shipper/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shipper_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetShipperConfigResponse(),
            self.execute(params, req, runtime)
        )

    def get_shipper_status(self, project, logstore, shipper_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_shipper_status_with_options(project, logstore, shipper_name, request, headers, runtime)

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

    def list_consumer_group(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_consumer_group_with_options(project, logstore, headers, runtime)

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

    def list_domains(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_domains_with_options(project, request, headers, runtime)

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

    def list_etl_job(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_etl_job_with_options(project, request, headers, runtime)

    def list_etl_job_with_options(self, project, request, headers, runtime):
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
            action='ListEtlJob',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etljobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListEtlJobResponse(),
            self.execute(params, req, runtime)
        )

    def list_etl_meta(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_etl_meta_with_options(project, request, headers, runtime)

    def list_etl_meta_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.etl_meta_key):
            query['etlMetaKey'] = request.etl_meta_key
        if not UtilClient.is_unset(request.etl_meta_name):
            query['etlMetaName'] = request.etl_meta_name
        if not UtilClient.is_unset(request.etl_meta_tag):
            query['etlMetaTag'] = request.etl_meta_tag
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
            action='ListEtlMeta',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etlmetas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListEtlMetaResponse(),
            self.execute(params, req, runtime)
        )

    def list_etl_meta_name(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_etl_meta_name_with_options(project, request, headers, runtime)

    def list_etl_meta_name_with_options(self, project, request, headers, runtime):
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
            action='ListEtlMetaName',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etlmetanames',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListEtlMetaNameResponse(),
            self.execute(params, req, runtime)
        )

    def list_external_store(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_external_store_with_options(project, request, headers, runtime)

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

    def list_log_stores(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_log_stores_with_options(project, request, headers, runtime)

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

    def list_machine_group(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_machine_group_with_options(project, request, headers, runtime)

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

    def list_machines(self, project, machine_group, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_machines_with_options(project, machine_group, request, headers, runtime)

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

    def list_project(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_with_options(request, headers, runtime)

    def list_project_with_options(self, request, headers, runtime):
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

    def list_saved_search(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_saved_search_with_options(project, request, headers, runtime)

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

    def list_shards(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_shards_with_options(project, logstore, headers, runtime)

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

    def list_shipper(self, project, logstore):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_shipper_with_options(project, logstore, headers, runtime)

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

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

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

    def merge_shards(self, project, logstore, shard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.merge_shards_with_options(project, logstore, shard_id, request, headers, runtime)

    def merge_shards_with_options(self, project, logstore, shard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MergeShards',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/shards/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shard_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.MergeShardsResponse(),
            self.execute(params, req, runtime)
        )

    def remove_config_from_machine_group(self, project, machine_group, config_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_config_from_machine_group_with_options(project, machine_group, config_name, headers, runtime)

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

    def split_shard(self, project, logstore, shard_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.split_shard_with_options(project, logstore, shard_id, request, headers, runtime)

    def split_shard_with_options(self, project, logstore, shard_id, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
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
            pathname='/logstores/%s/shards/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(shard_id)),
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

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

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

    def un_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.un_tag_resources_with_options(request, headers, runtime)

    def un_tag_resources_with_options(self, request, headers, runtime):
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
            action='UnTagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/untag',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UnTagResourcesResponse(),
            self.execute(params, req, runtime)
        )

    def update_check_point(self, project, logstore, consumer_group, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_check_point_with_options(project, logstore, consumer_group, request, headers, runtime)

    def update_check_point_with_options(self, project, logstore, consumer_group, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.consumer):
            query['consumer'] = request.consumer
        if not UtilClient.is_unset(request.force_success):
            query['forceSuccess'] = request.force_success
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.checkpoint):
            body['checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.shard):
            body['shard'] = request.shard
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCheckPoint',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/logstores/%s/consumergroups/%s' % (TeaConverter.to_unicode(logstore), TeaConverter.to_unicode(consumer_group)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateCheckPointResponse(),
            self.execute(params, req, runtime)
        )

    def update_consumer_group(self, project, logstore, consumer_group, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_consumer_group_with_options(project, logstore, consumer_group, request, headers, runtime)

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

    def update_etl_job(self, project, etl_job_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_etl_job_with_options(project, etl_job_name, request, headers, runtime)

    def update_etl_job_with_options(self, project, etl_job_name, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.etl_job_name):
            body['etlJobName'] = request.etl_job_name
        if not UtilClient.is_unset(request.function_config):
            body['functionConfig'] = request.function_config
        if not UtilClient.is_unset(request.function_parameter):
            body['functionParameter'] = request.function_parameter
        if not UtilClient.is_unset(request.log_config):
            body['logConfig'] = request.log_config
        if not UtilClient.is_unset(request.source_config):
            body['sourceConfig'] = request.source_config
        if not UtilClient.is_unset(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEtlJob',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etljobs/%s' % TeaConverter.to_unicode(etl_job_name),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateEtlJobResponse(),
            self.execute(params, req, runtime)
        )

    def update_etl_meta(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_etl_meta_with_options(project, request, headers, runtime)

    def update_etl_meta_with_options(self, project, request, headers, runtime):
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.enable):
            body['enable'] = request.enable
        if not UtilClient.is_unset(request.etl_meta_key):
            body['etlMetaKey'] = request.etl_meta_key
        if not UtilClient.is_unset(request.etl_meta_name):
            body['etlMetaName'] = request.etl_meta_name
        if not UtilClient.is_unset(request.etl_meta_tag):
            body['etlMetaTag'] = request.etl_meta_tag
        if not UtilClient.is_unset(request.etl_meta_value):
            body['etlMetaValue'] = request.etl_meta_value
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEtlMeta',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/etlmetas',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateEtlMetaResponse(),
            self.execute(params, req, runtime)
        )

    def update_index(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_index_with_options(project, logstore, request, headers, runtime)

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

    def update_log_store(self, project, logstore, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_log_store_with_options(project, logstore, request, headers, runtime)

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

    def update_logging(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logging_with_options(project, request, headers, runtime)

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

    def update_machine_group(self, project, group_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_machine_group_with_options(project, group_name, request, headers, runtime)

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

    def update_odps_shipper(self, project, logstore, shipper_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_odps_shipper_with_options(project, logstore, shipper_name, request, headers, runtime)

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

    def update_oss_external_store(self, project, external_store_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_oss_external_store_with_options(project, external_store_name, request, headers, runtime)

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

    def update_oss_shipper(self, project, logstore, shipper_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_oss_shipper_with_options(project, logstore, shipper_name, request, headers, runtime)

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

    def update_project(self, project, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_with_options(project, request, headers, runtime)

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

    def update_rds_external_store(self, project, external_store_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_rds_external_store_with_options(project, external_store_name, request, headers, runtime)

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

    def update_saved_search(self, project, savedsearch_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_saved_search_with_options(project, savedsearch_name, request, headers, runtime)

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
