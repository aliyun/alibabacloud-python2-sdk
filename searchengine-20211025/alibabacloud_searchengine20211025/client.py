# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_searchengine20211025 import models as searchengine_20211025_models
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
        self._endpoint = self.get_endpoint('searchengine', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def build_index_with_options(self, instance_id, request, headers, runtime):
        """
        ## Method
        POST
        ## URI
        /openapi/ha3/instances/{instanceId}/actions/build-index
        

        @param request: BuildIndexRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: BuildIndexResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.build_mode):
            body['buildMode'] = request.build_mode
        if not UtilClient.is_unset(request.data_source_name):
            body['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_type):
            body['dataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.data_time_sec):
            body['dataTimeSec'] = request.data_time_sec
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.generation):
            body['generation'] = request.generation
        if not UtilClient.is_unset(request.partition):
            body['partition'] = request.partition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BuildIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/actions/build-index' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.BuildIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def build_index(self, instance_id, request):
        """
        ## Method
        POST
        ## URI
        /openapi/ha3/instances/{instanceId}/actions/build-index
        

        @param request: BuildIndexRequest

        @return: BuildIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.build_index_with_options(instance_id, request, headers, runtime)

    def create_cluster_with_options(self, instance_id, request, headers, runtime):
        """
        ### Method
        `POST`
        ### URI
        `/openapi/ha3/instances/{instanceId}/clusters`
        

        @param request: CreateClusterRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_load):
            body['autoLoad'] = request.auto_load
        if not UtilClient.is_unset(request.data_node):
            body['dataNode'] = request.data_node
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.query_node):
            body['queryNode'] = request.query_node
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/clusters' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cluster(self, instance_id, request):
        """
        ### Method
        `POST`
        ### URI
        `/openapi/ha3/instances/{instanceId}/clusters`
        

        @param request: CreateClusterRequest

        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_cluster_with_options(instance_id, request, headers, runtime)

    def create_data_source_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.auto_build_index):
            body['autoBuildIndex'] = request.auto_build_index
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.saro_config):
            body['saroConfig'] = request.saro_config
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataSource',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/data-sources' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_source(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_data_source_with_options(instance_id, request, headers, runtime)

    def create_index_with_options(self, instance_id, request, headers, runtime):
        """
        ### Method
        ```java
        POST
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/indexes
        ```
        

        @param request: CreateIndexRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateIndexResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.data_source):
            body['dataSource'] = request.data_source
        if not UtilClient.is_unset(request.data_source_info):
            body['dataSourceInfo'] = request.data_source_info
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.extend):
            body['extend'] = request.extend
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.partition):
            body['partition'] = request.partition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/indexes' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def create_index(self, instance_id, request):
        """
        ### Method
        ```java
        POST
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/indexes
        ```
        

        @param request: CreateIndexRequest

        @return: CreateIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_index_with_options(instance_id, request, headers, runtime)

    def create_instance_with_options(self, request, headers, runtime):
        """
        ### Method
        `POST`
        ### URI
        `/api/instances?dryRun=false`
        

        @param request: CreateInstanceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.charge_type):
            body['chargeType'] = request.charge_type
        if not UtilClient.is_unset(request.components):
            body['components'] = request.components
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance(self, request):
        """
        ### Method
        `POST`
        ### URI
        `/api/instances?dryRun=false`
        

        @param request: CreateInstanceRequest

        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    def delete_advance_config_with_options(self, instance_id, config_name, headers, runtime):
        """
        ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAdvanceConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAdvanceConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/advanced-configs/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(config_name))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteAdvanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_advance_config(self, instance_id, config_name):
        """
        ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}
        

        @return: DeleteAdvanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_advance_config_with_options(instance_id, config_name, headers, runtime)

    def delete_data_source_with_options(self, instance_id, data_source_name, headers, runtime):
        """
        ## Method
        `DELETE`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/data-sources/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(data_source_name))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_source(self, instance_id, data_source_name):
        """
        ## Method
        `DELETE`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        

        @return: DeleteDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_data_source_with_options(instance_id, data_source_name, headers, runtime)

    def delete_index_with_options(self, instance_id, index_name, request, headers, runtime):
        """
        ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}?dataSource=xxx
        

        @param request: DeleteIndexRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteIndexResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source):
            query['dataSource'] = request.data_source
        if not UtilClient.is_unset(request.delete_data_source):
            query['deleteDataSource'] = request.delete_data_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/indexes/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(index_name))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_index(self, instance_id, index_name, request):
        """
        ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}?dataSource=xxx
        

        @param request: DeleteIndexRequest

        @return: DeleteIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_index_with_options(instance_id, index_name, request, headers, runtime)

    def delete_index_version_with_options(self, instance_id, index_name, version_name, headers, runtime):
        """
        ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteIndexVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteIndexVersion',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/indexes/%s/versions/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(index_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(version_name))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteIndexVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_index_version(self, instance_id, index_name, version_name):
        """
        ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}
        

        @return: DeleteIndexVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_index_version_with_options(instance_id, index_name, version_name, headers, runtime)

    def delete_instance_with_options(self, instance_id, headers, runtime):
        """
        ### Method
        `DELETE`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance(self, instance_id):
        """
        ### Method
        `DELETE`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        

        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, headers, runtime)

    def force_switch_with_options(self, instance_id, fsm_id, headers, runtime):
        """
        \\### Method
        ```java
        PUT
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/force-switch/{fsmId}
        ```
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ForceSwitchResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ForceSwitch',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/force-switch/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(fsm_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ForceSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    def force_switch(self, instance_id, fsm_id):
        """
        \\### Method
        ```java
        PUT
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/force-switch/{fsmId}
        ```
        

        @return: ForceSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.force_switch_with_options(instance_id, fsm_id, headers, runtime)

    def get_advance_config_with_options(self, instance_id, config_name, request, headers, runtime):
        """
        ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}
        

        @param request: GetAdvanceConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAdvanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAdvanceConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/advanced-configs/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(config_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetAdvanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_advance_config(self, instance_id, config_name, request):
        """
        ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}
        

        @param request: GetAdvanceConfigRequest

        @return: GetAdvanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_advance_config_with_options(instance_id, config_name, request, headers, runtime)

    def get_advance_config_file_with_options(self, instance_id, config_name, request, headers, runtime):
        """
        ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/file?fileName={fileName}
        

        @param request: GetAdvanceConfigFileRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAdvanceConfigFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAdvanceConfigFile',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/advanced-configs/%s/file' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(config_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetAdvanceConfigFileResponse(),
            self.call_api(params, req, runtime)
        )

    def get_advance_config_file(self, instance_id, config_name, request):
        """
        ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/file?fileName={fileName}
        

        @param request: GetAdvanceConfigFileRequest

        @return: GetAdvanceConfigFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_advance_config_file_with_options(instance_id, config_name, request, headers, runtime)

    def get_cluster_with_options(self, instance_id, cluster_name, headers, runtime):
        """
        ### Method
        `GET`
        ### URI
        `/openapi/ha3/instance/{instanceId}/clusters/{clusterName}`
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetClusterResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/clusters/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cluster(self, instance_id, cluster_name):
        """
        ### Method
        `GET`
        ### URI
        `/openapi/ha3/instance/{instanceId}/clusters/{clusterName}`
        

        @return: GetClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_with_options(instance_id, cluster_name, headers, runtime)

    def get_cluster_run_time_info_with_options(self, instance_id, headers, runtime):
        """
        ### Method
        GET
        ### URI
        /openapi/ha3/instances/{instanceId}/cluster-run-time-info
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetClusterRunTimeInfoResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetClusterRunTimeInfo',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/cluster-run-time-info' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetClusterRunTimeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cluster_run_time_info(self, instance_id):
        """
        ### Method
        GET
        ### URI
        /openapi/ha3/instances/{instanceId}/cluster-run-time-info
        

        @return: GetClusterRunTimeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_run_time_info_with_options(instance_id, headers, runtime)

    def get_data_source_with_options(self, instance_id, data_source_name, headers, runtime):
        """
        ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDataSource',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/data-sources/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(data_source_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_source(self, instance_id, data_source_name):
        """
        ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        

        @return: GetDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_data_source_with_options(instance_id, data_source_name, headers, runtime)

    def get_data_source_deploy_with_options(self, instance_id, deploy_name, data_source_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDataSourceDeploy',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/data-sources/%s/deploys/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(data_source_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(deploy_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetDataSourceDeployResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_source_deploy(self, instance_id, deploy_name, data_source_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_data_source_deploy_with_options(instance_id, deploy_name, data_source_name, headers, runtime)

    def get_deploy_graph_with_options(self, instance_id, headers, runtime):
        """
        ## Method
        GET
        ## URI
        ```java
        /openapi/ha3/instances/{instanceId}/deploy-graph
        ```
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDeployGraphResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDeployGraph',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/deploy-graph' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetDeployGraphResponse(),
            self.call_api(params, req, runtime)
        )

    def get_deploy_graph(self, instance_id):
        """
        ## Method
        GET
        ## URI
        ```java
        /openapi/ha3/instances/{instanceId}/deploy-graph
        ```
        

        @return: GetDeployGraphResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_deploy_graph_with_options(instance_id, headers, runtime)

    def get_file_with_options(self, instance_id, index_name, version_name, request, headers, runtime):
        """
        ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}/file?fileName=/root/test.txt
        

        @param request: GetFileRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFile',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/indexes/%s/versions/%s/file' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(index_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(version_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetFileResponse(),
            self.call_api(params, req, runtime)
        )

    def get_file(self, instance_id, index_name, version_name, request):
        """
        ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}/file?fileName=/root/test.txt
        

        @param request: GetFileRequest

        @return: GetFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_with_options(instance_id, index_name, version_name, request, headers, runtime)

    def get_index_with_options(self, instance_id, index_name, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/indexes/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(index_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def get_index(self, instance_id, index_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_index_with_options(instance_id, index_name, headers, runtime)

    def get_index_version_with_options(self, instance_id, cluster_name, headers, runtime):
        """
        ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}/index-version
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetIndexVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIndexVersion',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/clusters/%s/index-version' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetIndexVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_index_version(self, instance_id, cluster_name):
        """
        ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}/index-version
        

        @return: GetIndexVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_index_version_with_options(instance_id, cluster_name, headers, runtime)

    def get_instance_with_options(self, instance_id, headers, runtime):
        """
        ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance(self, instance_id):
        """
        ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        

        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    def get_node_config_with_options(self, instance_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_name):
            query['clusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNodeConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/node-config' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetNodeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_node_config(self, instance_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_node_config_with_options(instance_id, request, headers, runtime)

    def list_advance_config_dir_with_options(self, instance_id, config_name, request, headers, runtime):
        """
        ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/dir?dirName={dirName}`
        

        @param request: ListAdvanceConfigDirRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAdvanceConfigDirResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dir_name):
            query['dirName'] = request.dir_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAdvanceConfigDir',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/advanced-configs/%s/dir' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(config_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListAdvanceConfigDirResponse(),
            self.call_api(params, req, runtime)
        )

    def list_advance_config_dir(self, instance_id, config_name, request):
        """
        ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/dir?dirName={dirName}`
        

        @param request: ListAdvanceConfigDirRequest

        @return: ListAdvanceConfigDirResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_advance_config_dir_with_options(instance_id, config_name, request, headers, runtime)

    def list_advance_configs_with_options(self, instance_id, request, headers, runtime):
        """
        ## Sample requests
        `GET /openapi/ha3/instances/ose-test1/advanced-configs`
        

        @param request: ListAdvanceConfigsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAdvanceConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_name):
            query['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.index_name):
            query['indexName'] = request.index_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAdvanceConfigs',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/advanced-configs' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListAdvanceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_advance_configs(self, instance_id, request):
        """
        ## Sample requests
        `GET /openapi/ha3/instances/ose-test1/advanced-configs`
        

        @param request: ListAdvanceConfigsRequest

        @return: ListAdvanceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_advance_configs_with_options(instance_id, request, headers, runtime)

    def list_cluster_names_with_options(self, headers, runtime):
        """
        ### Method
        GET
        ### URI
        /openapi/ha3/instances/{instanceId}/cluster-names
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListClusterNamesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListClusterNames',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/cluster-names',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListClusterNamesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cluster_names(self):
        """
        ### Method
        GET
        ### URI
        /openapi/ha3/instances/{instanceId}/cluster-names
        

        @return: ListClusterNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_cluster_names_with_options(headers, runtime)

    def list_cluster_tasks_with_options(self, instance_id, headers, runtime):
        """
        ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/cluster-tasks
        ```
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListClusterTasksResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListClusterTasks',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/cluster-tasks' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListClusterTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cluster_tasks(self, instance_id):
        """
        ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/cluster-tasks
        ```
        

        @return: ListClusterTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_cluster_tasks_with_options(instance_id, headers, runtime)

    def list_clusters_with_options(self, instance_id, headers, runtime):
        """
        ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/clusters
        ```
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListClustersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/clusters' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_clusters(self, instance_id):
        """
        ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/clusters
        ```
        

        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_clusters_with_options(instance_id, headers, runtime)

    def list_data_source_schemas_with_options(self, instance_id, data_source_name, headers, runtime):
        """
        ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}/schemas`
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDataSourceSchemasResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSourceSchemas',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/data-sources/%s/schemas' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(data_source_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListDataSourceSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_source_schemas(self, instance_id, data_source_name):
        """
        ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}/schemas`
        

        @return: ListDataSourceSchemasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_source_schemas_with_options(instance_id, data_source_name, headers, runtime)

    def list_data_source_tasks_with_options(self, instance_id, headers, runtime):
        """
        ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/data-source-tasks
        ```
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDataSourceTasksResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSourceTasks',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/data-source-tasks' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListDataSourceTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_source_tasks(self, instance_id):
        """
        ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/data-source-tasks
        ```
        

        @return: ListDataSourceTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_source_tasks_with_options(instance_id, headers, runtime)

    def list_data_sources_with_options(self, instance_id, headers, runtime):
        """
        ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources`
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDataSourcesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSources',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/data-sources' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_sources(self, instance_id):
        """
        ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources`
        

        @return: ListDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_sources_with_options(instance_id, headers, runtime)

    def list_date_source_generations_with_options(self, instance_id, data_source_name, request, headers, runtime):
        """
        ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}/generations?domainName={domainName}`
        

        @param request: ListDateSourceGenerationsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDateSourceGenerationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['domainName'] = request.domain_name
        if not UtilClient.is_unset(request.valid_status):
            query['validStatus'] = request.valid_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDateSourceGenerations',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/data-sources/%s/generations' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(data_source_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListDateSourceGenerationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_date_source_generations(self, instance_id, data_source_name, request):
        """
        ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}/generations?domainName={domainName}`
        

        @param request: ListDateSourceGenerationsRequest

        @return: ListDateSourceGenerationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_date_source_generations_with_options(instance_id, data_source_name, request, headers, runtime)

    def list_indexes_with_options(self, instance_id, request, headers, runtime):
        """
        ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes
        

        @param request: ListIndexesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListIndexesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_mode):
            query['newMode'] = request.new_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIndexes',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/indexes' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListIndexesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_indexes(self, instance_id, request):
        """
        ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes
        

        @param request: ListIndexesRequest

        @return: ListIndexesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_indexes_with_options(instance_id, request, headers, runtime)

    def list_instance_specs_with_options(self, instance_id, request, headers, runtime):
        """
        ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/specs?type=qrs`
        

        @param request: ListInstanceSpecsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListInstanceSpecsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceSpecs',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/specs' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListInstanceSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instance_specs(self, instance_id, request):
        """
        ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/specs?type=qrs`
        

        @param request: ListInstanceSpecsRequest

        @return: ListInstanceSpecsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_specs_with_options(instance_id, request, headers, runtime)

    def list_instances_with_options(self, tmp_req, headers, runtime):
        """
        ### Method
        `GET`
        ### URI
        `/openapi/[code]/instances`
        

        @param tmp_req: ListInstancesRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = searchengine_20211025_models.ListInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.edition):
            query['edition'] = request.edition
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instances(self, request):
        """
        ### Method
        `GET`
        ### URI
        `/openapi/[code]/instances`
        

        @param request: ListInstancesRequest

        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    def list_online_configs_with_options(self, instance_id, node_name, request, headers, runtime):
        """
        ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node/{nodeName}/online-configs?domain={domain}
        ```
        

        @param request: ListOnlineConfigsRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListOnlineConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOnlineConfigs',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/node/%s/online-configs' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(node_name))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListOnlineConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_online_configs(self, instance_id, node_name, request):
        """
        ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node/{nodeName}/online-configs?domain={domain}
        ```
        

        @param request: ListOnlineConfigsRequest

        @return: ListOnlineConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_online_configs_with_options(instance_id, node_name, request, headers, runtime)

    def list_query_result_with_options(self, instance_id, request, headers, runtime):
        """
        ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/query?query=xxxx`
        

        @param request: ListQueryResultRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListQueryResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.sql):
            query['sql'] = request.sql
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueryResult',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/query' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListQueryResultResponse(),
            self.call_api(params, req, runtime)
        )

    def list_query_result(self, instance_id, request):
        """
        ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/query?query=xxxx`
        

        @param request: ListQueryResultRequest

        @return: ListQueryResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_query_result_with_options(instance_id, request, headers, runtime)

    def modify_advance_config_file_with_options(self, instance_id, config_name, request, headers, runtime):
        """
        ## Method
        put
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/file?fileName={fileName}
        

        @param request: ModifyAdvanceConfigFileRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyAdvanceConfigFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyAdvanceConfigFile',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/advanced-configs/%s/file' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(config_name))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyAdvanceConfigFileResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_advance_config_file(self, instance_id, config_name, request):
        """
        ## Method
        put
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/file?fileName={fileName}
        

        @param request: ModifyAdvanceConfigFileRequest

        @return: ModifyAdvanceConfigFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_advance_config_file_with_options(instance_id, config_name, request, headers, runtime)

    def modify_cluster_desc_with_options(self, instance_id, cluster_name, request, headers, runtime):
        """
        ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/clusters/{clusterName}/desc`
        

        @param request: ModifyClusterDescRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyClusterDescResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterDesc',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/clusters/%s/desc' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_name))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyClusterDescResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cluster_desc(self, instance_id, cluster_name, request):
        """
        ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/clusters/{clusterName}/desc`
        

        @param request: ModifyClusterDescRequest

        @return: ModifyClusterDescResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_desc_with_options(instance_id, cluster_name, request, headers, runtime)

    def modify_cluster_offline_config_with_options(self, instance_id, request, headers, runtime):
        """
        ## Request syntax
        PUT /openapi/ha3/instances/{instanceId}/cluster-offline-config
        

        @param request: ModifyClusterOfflineConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyClusterOfflineConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.build_mode):
            body['buildMode'] = request.build_mode
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.data_source_name):
            body['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_type):
            body['dataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.data_time_sec):
            body['dataTimeSec'] = request.data_time_sec
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.generation):
            body['generation'] = request.generation
        if not UtilClient.is_unset(request.partition):
            body['partition'] = request.partition
        if not UtilClient.is_unset(request.push_mode):
            body['pushMode'] = request.push_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterOfflineConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/cluster-offline-config' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyClusterOfflineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cluster_offline_config(self, instance_id, request):
        """
        ## Request syntax
        PUT /openapi/ha3/instances/{instanceId}/cluster-offline-config
        

        @param request: ModifyClusterOfflineConfigRequest

        @return: ModifyClusterOfflineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_offline_config_with_options(instance_id, request, headers, runtime)

    def modify_cluster_online_config_with_options(self, instance_id, request, headers, runtime):
        """
        ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/cluster-online-config`
        

        @param request: ModifyClusterOnlineConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyClusterOnlineConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.clusters):
            body['clusters'] = request.clusters
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterOnlineConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/cluster-online-config' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyClusterOnlineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_cluster_online_config(self, instance_id, request):
        """
        ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/cluster-online-config`
        

        @param request: ModifyClusterOnlineConfigRequest

        @return: ModifyClusterOnlineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_online_config_with_options(instance_id, request, headers, runtime)

    def modify_data_source_with_options(self, instance_id, data_source_name, request, headers, runtime):
        """
        ## Method
        `PUT`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        

        @param request: ModifyDataSourceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDataSource',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/data-sources/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(data_source_name))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_data_source(self, instance_id, data_source_name, request):
        """
        ## Method
        `PUT`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        

        @param request: ModifyDataSourceRequest

        @return: ModifyDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_data_source_with_options(instance_id, data_source_name, request, headers, runtime)

    def modify_file_with_options(self, instance_id, index_name, version_name, request, headers, runtime):
        """
        ## Method
        PUT
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}/file?fileName=/root/test.txt
        

        @param request: ModifyFileRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.partition):
            body['partition'] = request.partition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyFile',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/indexes/%s/versions/%s/file' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(index_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(version_name))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyFileResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_file(self, instance_id, index_name, version_name, request):
        """
        ## Method
        PUT
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}/file?fileName=/root/test.txt
        

        @param request: ModifyFileRequest

        @return: ModifyFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_file_with_options(instance_id, index_name, version_name, request, headers, runtime)

    def modify_index_partition_with_options(self, instance_id, request, headers, runtime):
        """
        ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/index-partition`
        

        @param request: ModifyIndexPartitionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyIndexPartitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_name):
            body['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.domain_name):
            body['domainName'] = request.domain_name
        if not UtilClient.is_unset(request.generation):
            body['generation'] = request.generation
        if not UtilClient.is_unset(request.index_infos):
            body['indexInfos'] = request.index_infos
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyIndexPartition',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/index-partition' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyIndexPartitionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_index_partition(self, instance_id, request):
        """
        ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/index-partition`
        

        @param request: ModifyIndexPartitionRequest

        @return: ModifyIndexPartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_index_partition_with_options(instance_id, request, headers, runtime)

    def modify_index_version_with_options(self, instance_id, cluster_name, request, headers, runtime):
        """
        ## Method
        PUT
        ## URI
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}/index-version
        

        @param request: ModifyIndexVersionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyIndexVersionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='ModifyIndexVersion',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/clusters/%s/index-version' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_name))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyIndexVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_index_version(self, instance_id, cluster_name, request):
        """
        ## Method
        PUT
        ## URI
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}/index-version
        

        @param request: ModifyIndexVersionRequest

        @return: ModifyIndexVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_index_version_with_options(instance_id, cluster_name, request, headers, runtime)

    def modify_node_config_with_options(self, instance_id, request, headers, runtime):
        """
        ### Method
        ```java
        PUT
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node-config?type=qrs&name=test
        ```
        

        @param request: ModifyNodeConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyNodeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_name):
            query['clusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.data_source_name):
            query['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.active):
            body['active'] = request.active
        if not UtilClient.is_unset(request.data_duplicate_number):
            body['dataDuplicateNumber'] = request.data_duplicate_number
        if not UtilClient.is_unset(request.data_fragment_number):
            body['dataFragmentNumber'] = request.data_fragment_number
        if not UtilClient.is_unset(request.flow_ratio):
            body['flowRatio'] = request.flow_ratio
        if not UtilClient.is_unset(request.min_service_percent):
            body['minServicePercent'] = request.min_service_percent
        if not UtilClient.is_unset(request.published):
            body['published'] = request.published
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyNodeConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/node-config' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyNodeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_node_config(self, instance_id, request):
        """
        ### Method
        ```java
        PUT
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node-config?type=qrs&name=test
        ```
        

        @param request: ModifyNodeConfigRequest

        @return: ModifyNodeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_node_config_with_options(instance_id, request, headers, runtime)

    def modify_online_config_with_options(self, instance_id, node_name, index_name, request, headers, runtime):
        """
        ### Method
        ```java
        put
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node/{nodeName}/online-configs/{indexName}
        ```
        

        @param request: ModifyOnlineConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyOnlineConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyOnlineConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/node/%s/online-configs/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(node_name)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(index_name))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyOnlineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_online_config(self, instance_id, node_name, index_name, request):
        """
        ### Method
        ```java
        put
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node/{nodeName}/online-configs/{indexName}
        ```
        

        @param request: ModifyOnlineConfigRequest

        @return: ModifyOnlineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_online_config_with_options(instance_id, node_name, index_name, request, headers, runtime)

    def modify_password_with_options(self, instance_id, request, headers, runtime):
        """
        ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/password`
        

        @param request: ModifyPasswordRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyPasswordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPassword',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/password' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_password(self, instance_id, request):
        """
        ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/password`
        

        @param request: ModifyPasswordRequest

        @return: ModifyPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_password_with_options(instance_id, request, headers, runtime)

    def publish_advance_config_with_options(self, instance_id, config_name, request, headers, runtime):
        """
        ## Method
        ~~~
        POST
        ~~~
        ## URI
        ~~~
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/actions/publish
        ~~~
        

        @param request: PublishAdvanceConfigRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: PublishAdvanceConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishAdvanceConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/advanced-configs/%s/actions/publish' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(config_name))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.PublishAdvanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_advance_config(self, instance_id, config_name, request):
        """
        ## Method
        ~~~
        POST
        ~~~
        ## URI
        ~~~
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/actions/publish
        ~~~
        

        @param request: PublishAdvanceConfigRequest

        @return: PublishAdvanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_advance_config_with_options(instance_id, config_name, request, headers, runtime)

    def publish_index_version_with_options(self, instance_id, index_name, request, headers, runtime):
        """
        ## Method
        POST
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/actions/publish
        

        @param request: PublishIndexVersionRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: PublishIndexVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishIndexVersion',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/indexes/%s/actions/publish' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(index_name))),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.PublishIndexVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_index_version(self, instance_id, index_name, request):
        """
        ## Method
        POST
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/actions/publish
        

        @param request: PublishIndexVersionRequest

        @return: PublishIndexVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_index_version_with_options(instance_id, index_name, request, headers, runtime)

    def recover_index_with_options(self, instance_id, request, headers, runtime):
        """
        ### Method
        `POST`
        ### URI
        `/openapi/ha3/instances/{instanceId}/recover-index`
        

        @param request: RecoverIndexRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RecoverIndexResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.build_deploy_id):
            body['buildDeployId'] = request.build_deploy_id
        if not UtilClient.is_unset(request.data_source_name):
            body['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.generation):
            body['generation'] = request.generation
        if not UtilClient.is_unset(request.index_name):
            body['indexName'] = request.index_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecoverIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/recover-index' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.RecoverIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def recover_index(self, instance_id, request):
        """
        ### Method
        `POST`
        ### URI
        `/openapi/ha3/instances/{instanceId}/recover-index`
        

        @param request: RecoverIndexRequest

        @return: RecoverIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recover_index_with_options(instance_id, request, headers, runtime)

    def remove_cluster_with_options(self, instance_id, cluster_name, headers, runtime):
        """
        ### Method
        ```java
        DELETE
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}
        ```
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveClusterResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveCluster',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/clusters/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(cluster_name))),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.RemoveClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_cluster(self, instance_id, cluster_name):
        """
        ### Method
        ```java
        DELETE
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}
        ```
        

        @return: RemoveClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_cluster_with_options(instance_id, cluster_name, headers, runtime)

    def stop_task_with_options(self, instance_id, fsm_id, headers, runtime):
        """
        ### Method
        ```java
        PUT
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/stop-task/{fsmId}
        ```
        

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopTask',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s/stop-task/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(fsm_id))),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.StopTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_task(self, instance_id, fsm_id):
        """
        ### Method
        ```java
        PUT
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/stop-task/{fsmId}
        ```
        

        @return: StopTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_task_with_options(instance_id, fsm_id, headers, runtime)

    def update_instance_with_options(self, instance_id, request, headers, runtime):
        """
        ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        

        @param request: UpdateInstanceRequest

        @type headers: dict
        @param headers: map

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.components):
            body['components'] = request.components
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.order_type):
            body['orderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname='/openapi/ha3/instances/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(instance_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance(self, instance_id, request):
        """
        ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        

        @param request: UpdateInstanceRequest

        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(instance_id, request, headers, runtime)
