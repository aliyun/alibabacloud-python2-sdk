# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.converter import TeaConverter
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_opensearch20171225 import models as open_search_20171225_models
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
        self._endpoint = self.get_endpoint('opensearch', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def bind_esuser_analyzer(self, app_group_identity, es_instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.bind_esuser_analyzer_with_options(app_group_identity, es_instance_id, headers, runtime)

    def bind_esuser_analyzer_with_options(self, app_group_identity, es_instance_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        es_instance_id = OpenApiUtilClient.get_encode_param(es_instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='BindESUserAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/es/%s/actions/bind-analyzer' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(es_instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.BindESUserAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_es_instance(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.bind_es_instance_with_options(app_group_identity, headers, runtime)

    def bind_es_instance_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='BindEsInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/actions/bind-es-instance' % TeaConverter.to_unicode(app_group_identity),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.BindEsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def compile_sort_script(self, app_group_identity, script_name, app_version_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.compile_sort_script_with_options(app_group_identity, script_name, app_version_id, headers, runtime)

    def compile_sort_script_with_options(self, app_group_identity, script_name, app_version_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        script_name = OpenApiUtilClient.get_encode_param(script_name)
        app_version_id = OpenApiUtilClient.get_encode_param(app_version_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CompileSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/sort-scripts/%s/actions/compiling' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_version_id), TeaConverter.to_unicode(script_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CompileSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    def create_abtest_experiment(self, app_group_identity, scene_id, group_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_abtest_experiment_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    def create_abtest_experiment_with_options(self, app_group_identity, scene_id, group_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        scene_id = OpenApiUtilClient.get_encode_param(scene_id)
        group_id = OpenApiUtilClient.get_encode_param(group_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateABTestExperiment',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes/%s/groups/%s/experiments' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(scene_id), TeaConverter.to_unicode(group_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateABTestExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_abtest_group(self, app_group_identity, scene_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_abtest_group_with_options(app_group_identity, scene_id, headers, runtime)

    def create_abtest_group_with_options(self, app_group_identity, scene_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        scene_id = OpenApiUtilClient.get_encode_param(scene_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateABTestGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes/%s/groups' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(scene_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateABTestGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_abtest_scene(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_abtest_scene_with_options(app_group_identity, headers, runtime)

    def create_abtest_scene_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateABTestScene',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes' % TeaConverter.to_unicode(app_group_identity),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateABTestSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app(self, app_group_identity, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_app_with_options(app_group_identity, request, headers, runtime)

    def create_app_with_options(self, app_group_identity, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps' % TeaConverter.to_unicode(app_group_identity),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app_group(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_app_group_with_options(headers, runtime)

    def create_app_group_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateAppGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_collection(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_data_collection_with_options(app_group_identity, headers, runtime)

    def create_data_collection_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateDataCollection',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/data-collections' % TeaConverter.to_unicode(app_group_identity),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateDataCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_first_rank(self, app_group_identity, app_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_first_rank_with_options(app_group_identity, app_id, request, headers, runtime)

    def create_first_rank_with_options(self, app_group_identity, app_id, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFirstRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/first-ranks' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateFirstRankResponse(),
            self.call_api(params, req, runtime)
        )

    def create_function_instance(self, app_group_identity, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_function_instance_with_options(app_group_identity, function_name, request, headers, runtime)

    def create_function_instance_with_options(self, app_group_identity, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        body = {}
        if not UtilClient.is_unset(request.create_parameters):
            body['createParameters'] = request.create_parameters
        if not UtilClient.is_unset(request.cron):
            body['cron'] = request.cron
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.function_type):
            body['functionType'] = request.function_type
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.model_type):
            body['modelType'] = request.model_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFunctionInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/functions/%s/instances' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(function_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_function_task(self, app_group_identity, function_name, instance_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_function_task_with_options(app_group_identity, function_name, instance_name, headers, runtime)

    def create_function_task_with_options(self, app_group_identity, function_name, instance_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        instance_name = OpenApiUtilClient.get_encode_param(instance_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateFunctionTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/functions/%s/instances/%s/tasks' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(function_name), TeaConverter.to_unicode(instance_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateFunctionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_intervention_dictionary(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_intervention_dictionary_with_options(headers, runtime)

    def create_intervention_dictionary_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateInterventionDictionary',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/intervention-dictionaries',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateInterventionDictionaryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_model(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_model_with_options(app_group_identity, headers, runtime)

    def create_model_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateModel',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/algorithm/models' % TeaConverter.to_unicode(app_group_identity),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateModelResponse(),
            self.call_api(params, req, runtime)
        )

    def create_query_processor(self, app_group_identity, app_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_query_processor_with_options(app_group_identity, app_id, request, headers, runtime)

    def create_query_processor_with_options(self, app_group_identity, app_id, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQueryProcessor',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/query-processors' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateQueryProcessorResponse(),
            self.call_api(params, req, runtime)
        )

    def create_scheduled_task(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_scheduled_task_with_options(app_group_identity, headers, runtime)

    def create_scheduled_task_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateScheduledTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scheduled-tasks' % TeaConverter.to_unicode(app_group_identity),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_search_strategy(self, app_group_identity, app_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_search_strategy_with_options(app_group_identity, app_id, headers, runtime)

    def create_search_strategy_with_options(self, app_group_identity, app_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateSearchStrategy',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/search-strategies' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateSearchStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_second_rank(self, app_group_identity, app_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_second_rank_with_options(app_group_identity, app_id, request, headers, runtime)

    def create_second_rank_with_options(self, app_group_identity, app_id, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecondRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/second-ranks' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateSecondRankResponse(),
            self.call_api(params, req, runtime)
        )

    def create_sort_script(self, app_group_identity, app_version_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sort_script_with_options(app_group_identity, app_version_id, headers, runtime)

    def create_sort_script_with_options(self, app_group_identity, app_version_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_version_id = OpenApiUtilClient.get_encode_param(app_version_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/sort-scripts' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_version_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user_analyzer(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_user_analyzer_with_options(headers, runtime)

    def create_user_analyzer_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateUserAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/user-analyzers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.CreateUserAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_abtest_experiment(self, app_group_identity, scene_id, group_id, experiment_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_abtest_experiment_with_options(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    def delete_abtest_experiment_with_options(self, app_group_identity, scene_id, group_id, experiment_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        scene_id = OpenApiUtilClient.get_encode_param(scene_id)
        group_id = OpenApiUtilClient.get_encode_param(group_id)
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteABTestExperiment',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes/%s/groups/%s/experiments/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(scene_id), TeaConverter.to_unicode(group_id), TeaConverter.to_unicode(experiment_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteABTestExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_abtest_group(self, app_group_identity, scene_id, group_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_abtest_group_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    def delete_abtest_group_with_options(self, app_group_identity, scene_id, group_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        scene_id = OpenApiUtilClient.get_encode_param(scene_id)
        group_id = OpenApiUtilClient.get_encode_param(group_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteABTestGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes/%s/groups/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(scene_id), TeaConverter.to_unicode(group_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteABTestGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_abtest_scene(self, app_group_identity, scene_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_abtest_scene_with_options(app_group_identity, scene_id, headers, runtime)

    def delete_abtest_scene_with_options(self, app_group_identity, scene_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        scene_id = OpenApiUtilClient.get_encode_param(scene_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteABTestScene',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(scene_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteABTestSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_function_instance(self, app_group_identity, function_name, instance_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_function_instance_with_options(app_group_identity, function_name, instance_name, headers, runtime)

    def delete_function_instance_with_options(self, app_group_identity, function_name, instance_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        instance_name = OpenApiUtilClient.get_encode_param(instance_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFunctionInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/functions/%s/instances/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(function_name), TeaConverter.to_unicode(instance_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_model(self, app_group_identity, model_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_model_with_options(app_group_identity, model_name, headers, runtime)

    def delete_model_with_options(self, app_group_identity, model_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        model_name = OpenApiUtilClient.get_encode_param(model_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModel',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/algorithm/models/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(model_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteModelResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_sort_script(self, app_group_identity, script_name, app_version_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_sort_script_with_options(app_group_identity, script_name, app_version_id, headers, runtime)

    def delete_sort_script_with_options(self, app_group_identity, script_name, app_version_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        script_name = OpenApiUtilClient.get_encode_param(script_name)
        app_version_id = OpenApiUtilClient.get_encode_param(app_version_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/sort-scripts/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_version_id), TeaConverter.to_unicode(script_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_sort_script_file(self, app_group_identity, app_version_id, script_name, file_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_sort_script_file_with_options(app_group_identity, app_version_id, script_name, file_name, headers, runtime)

    def delete_sort_script_file_with_options(self, app_group_identity, app_version_id, script_name, file_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_version_id = OpenApiUtilClient.get_encode_param(app_version_id)
        script_name = OpenApiUtilClient.get_encode_param(script_name)
        file_name = OpenApiUtilClient.get_encode_param(file_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSortScriptFile',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/sort-scripts/%s/files/src/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_version_id), TeaConverter.to_unicode(script_name), TeaConverter.to_unicode(file_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DeleteSortScriptFileResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_abtest_experiment(self, app_group_identity, scene_id, group_id, experiment_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_abtest_experiment_with_options(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    def describe_abtest_experiment_with_options(self, app_group_identity, scene_id, group_id, experiment_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        scene_id = OpenApiUtilClient.get_encode_param(scene_id)
        group_id = OpenApiUtilClient.get_encode_param(group_id)
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeABTestExperiment',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes/%s/groups/%s/experiments/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(scene_id), TeaConverter.to_unicode(group_id), TeaConverter.to_unicode(experiment_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeABTestExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_abtest_group(self, app_group_identity, scene_id, group_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_abtest_group_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    def describe_abtest_group_with_options(self, app_group_identity, scene_id, group_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        scene_id = OpenApiUtilClient.get_encode_param(scene_id)
        group_id = OpenApiUtilClient.get_encode_param(group_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeABTestGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes/%s/groups/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(scene_id), TeaConverter.to_unicode(group_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeABTestGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_abtest_scene(self, app_group_identity, scene_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_abtest_scene_with_options(app_group_identity, scene_id, headers, runtime)

    def describe_abtest_scene_with_options(self, app_group_identity, scene_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        scene_id = OpenApiUtilClient.get_encode_param(scene_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeABTestScene',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(scene_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeABTestSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app(self, app_group_identity, app_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_with_options(app_group_identity, app_id, headers, runtime)

    def describe_app_with_options(self, app_group_identity, app_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeApp',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_group(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_group_with_options(app_group_identity, headers, runtime)

    def describe_app_group_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeAppGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s' % TeaConverter.to_unicode(app_group_identity),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_group_data_report(self, app_group_identity, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_group_data_report_with_options(app_group_identity, request, headers, runtime)

    def describe_app_group_data_report_with_options(self, app_group_identity, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppGroupDataReport',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/data-report' % TeaConverter.to_unicode(app_group_identity),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppGroupDataReportResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_group_statistics(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_group_statistics_with_options(app_group_identity, headers, runtime)

    def describe_app_group_statistics_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeAppGroupStatistics',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/statistics' % TeaConverter.to_unicode(app_group_identity),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppGroupStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_statistics(self, app_group_identity, app_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_statistics_with_options(app_group_identity, app_id, headers, runtime)

    def describe_app_statistics_with_options(self, app_group_identity, app_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeAppStatistics',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/statistics' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apps(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_apps_with_options(app_group_identity, headers, runtime)

    def describe_apps_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeApps',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps' % TeaConverter.to_unicode(app_group_identity),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_collction(self, app_group_identity, data_collection_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_data_collction_with_options(app_group_identity, data_collection_identity, headers, runtime)

    def describe_data_collction_with_options(self, app_group_identity, data_collection_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        data_collection_identity = OpenApiUtilClient.get_encode_param(data_collection_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeDataCollction',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/data-collections/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(data_collection_identity)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeDataCollctionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_first_rank(self, app_group_identity, app_id, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_first_rank_with_options(app_group_identity, app_id, name, headers, runtime)

    def describe_first_rank_with_options(self, app_group_identity, app_id, name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeFirstRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/first-ranks/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id), TeaConverter.to_unicode(name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeFirstRankResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_intervention_dictionary(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_intervention_dictionary_with_options(name, headers, runtime)

    def describe_intervention_dictionary_with_options(self, name, headers, runtime):
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInterventionDictionary',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/intervention-dictionaries/%s' % TeaConverter.to_unicode(name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeInterventionDictionaryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_model(self, app_group_identity, model_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_model_with_options(app_group_identity, model_name, headers, runtime)

    def describe_model_with_options(self, app_group_identity, model_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        model_name = OpenApiUtilClient.get_encode_param(model_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeModel',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/algorithm/models/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(model_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeModelResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_query_processor(self, app_group_identity, app_id, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_query_processor_with_options(app_group_identity, app_id, name, headers, runtime)

    def describe_query_processor_with_options(self, app_group_identity, app_id, name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeQueryProcessor',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/query-processors/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id), TeaConverter.to_unicode(name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeQueryProcessorResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_region(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_region_with_options(headers, runtime)

    def describe_region_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeRegion',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/region',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeRegionResponse(),
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
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_scheduled_task(self, app_group_identity, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_scheduled_task_with_options(app_group_identity, task_id, headers, runtime)

    def describe_scheduled_task_with_options(self, app_group_identity, task_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeScheduledTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scheduled-tasks/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(task_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_second_rank(self, app_group_identity, app_id, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_second_rank_with_options(app_group_identity, app_id, name, headers, runtime)

    def describe_second_rank_with_options(self, app_group_identity, app_id, name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSecondRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/second-ranks/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id), TeaConverter.to_unicode(name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeSecondRankResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_slow_query_status(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_slow_query_status_with_options(app_group_identity, headers, runtime)

    def describe_slow_query_status_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeSlowQueryStatus',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/optimizers/slow-query' % TeaConverter.to_unicode(app_group_identity),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeSlowQueryStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_analyzer(self, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_user_analyzer_with_options(name, request, headers, runtime)

    def describe_user_analyzer_with_options(self, name, request, headers, runtime):
        UtilClient.validate_model(request)
        name = OpenApiUtilClient.get_encode_param(name)
        query = {}
        if not UtilClient.is_unset(request.with_):
            query['with'] = request.with_
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/user-analyzers/%s' % TeaConverter.to_unicode(name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DescribeUserAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_slow_query(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_slow_query_with_options(app_group_identity, headers, runtime)

    def disable_slow_query_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DisableSlowQuery',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/optimizers/slow-query/actions/disable' % TeaConverter.to_unicode(app_group_identity),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.DisableSlowQueryResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_slow_query(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_slow_query_with_options(app_group_identity, headers, runtime)

    def enable_slow_query_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='EnableSlowQuery',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/optimizers/slow-query/actions/enable' % TeaConverter.to_unicode(app_group_identity),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.EnableSlowQueryResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_merged_table(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_merged_table_with_options(request, headers, runtime)

    def generate_merged_table_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.spec):
            query['spec'] = request.spec
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateMergedTable',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/assist/schema/actions/merge',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GenerateMergedTableResponse(),
            self.call_api(params, req, runtime)
        )

    def get_domain(self, domain_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_domain_with_options(domain_name, request, headers, runtime)

    def get_domain_with_options(self, domain_name, request, headers, runtime):
        UtilClient.validate_model(request)
        domain_name = OpenApiUtilClient.get_encode_param(domain_name)
        query = {}
        if not UtilClient.is_unset(request.app_group_identity):
            query['appGroupIdentity'] = request.app_group_identity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomain',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/domains/%s' % TeaConverter.to_unicode(domain_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def get_function_current_version(self, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_current_version_with_options(function_name, request, headers, runtime)

    def get_function_current_version_with_options(self, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['category'] = request.category
        if not UtilClient.is_unset(request.domain):
            query['domain'] = request.domain
        if not UtilClient.is_unset(request.function_type):
            query['functionType'] = request.function_type
        if not UtilClient.is_unset(request.model_type):
            query['modelType'] = request.model_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunctionCurrentVersion',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/functions/%s/current-version' % TeaConverter.to_unicode(function_name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetFunctionCurrentVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_function_default_instance(self, app_group_identity, function_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_default_instance_with_options(app_group_identity, function_name, headers, runtime)

    def get_function_default_instance_with_options(self, app_group_identity, function_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFunctionDefaultInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/functions/%s/default-instance' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(function_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetFunctionDefaultInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_function_instance(self, app_group_identity, function_name, instance_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_instance_with_options(app_group_identity, function_name, instance_name, request, headers, runtime)

    def get_function_instance_with_options(self, app_group_identity, function_name, instance_name, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        instance_name = OpenApiUtilClient.get_encode_param(instance_name)
        query = {}
        if not UtilClient.is_unset(request.output):
            query['output'] = request.output
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFunctionInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/functions/%s/instances/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(function_name), TeaConverter.to_unicode(instance_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_function_version(self, function_name, version_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_function_version_with_options(function_name, version_id, headers, runtime)

    def get_function_version_with_options(self, function_name, version_id, headers, runtime):
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        version_id = OpenApiUtilClient.get_encode_param(version_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFunctionVersion',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/functions/%s/versions/%s' % (TeaConverter.to_unicode(function_name), TeaConverter.to_unicode(version_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetFunctionVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_model_progress(self, app_group_identity, model_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_model_progress_with_options(app_group_identity, model_name, headers, runtime)

    def get_model_progress_with_options(self, app_group_identity, model_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        model_name = OpenApiUtilClient.get_encode_param(model_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelProgress',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/algorithm/models/%s/progress' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(model_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetModelProgressResponse(),
            self.call_api(params, req, runtime)
        )

    def get_model_report(self, app_group_identity, model_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_model_report_with_options(app_group_identity, model_name, headers, runtime)

    def get_model_report_with_options(self, app_group_identity, model_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        model_name = OpenApiUtilClient.get_encode_param(model_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelReport',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/algorithm/models/%s/report' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(model_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetModelReportResponse(),
            self.call_api(params, req, runtime)
        )

    def get_script_file_names(self, app_group_identity, app_version_id, script_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_script_file_names_with_options(app_group_identity, app_version_id, script_name, headers, runtime)

    def get_script_file_names_with_options(self, app_group_identity, app_version_id, script_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_version_id = OpenApiUtilClient.get_encode_param(app_version_id)
        script_name = OpenApiUtilClient.get_encode_param(script_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetScriptFileNames',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/sort-scripts/%s/file-names' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_version_id), TeaConverter.to_unicode(script_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetScriptFileNamesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_search_strategy(self, app_group_identity, app_id, strategy_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_search_strategy_with_options(app_group_identity, app_id, strategy_name, headers, runtime)

    def get_search_strategy_with_options(self, app_group_identity, app_id, strategy_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        strategy_name = OpenApiUtilClient.get_encode_param(strategy_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSearchStrategy',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/search-strategies/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id), TeaConverter.to_unicode(strategy_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetSearchStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sort_script(self, app_group_identity, script_name, app_version_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sort_script_with_options(app_group_identity, script_name, app_version_id, headers, runtime)

    def get_sort_script_with_options(self, app_group_identity, script_name, app_version_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        script_name = OpenApiUtilClient.get_encode_param(script_name)
        app_version_id = OpenApiUtilClient.get_encode_param(app_version_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/sort-scripts/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_version_id), TeaConverter.to_unicode(script_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sort_script_file(self, app_group_identity, script_name, app_version_id, file_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sort_script_file_with_options(app_group_identity, script_name, app_version_id, file_name, headers, runtime)

    def get_sort_script_file_with_options(self, app_group_identity, script_name, app_version_id, file_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        script_name = OpenApiUtilClient.get_encode_param(script_name)
        app_version_id = OpenApiUtilClient.get_encode_param(app_version_id)
        file_name = OpenApiUtilClient.get_encode_param(file_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSortScriptFile',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/sort-scripts/%s/files/src/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_version_id), TeaConverter.to_unicode(script_name), TeaConverter.to_unicode(file_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetSortScriptFileResponse(),
            self.call_api(params, req, runtime)
        )

    def get_validation_error(self, app_group_identity, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_validation_error_with_options(app_group_identity, request, headers, runtime)

    def get_validation_error_with_options(self, app_group_identity, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        query = {}
        if not UtilClient.is_unset(request.error_code):
            query['errorCode'] = request.error_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetValidationError',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/algorithm/data/validation-error' % TeaConverter.to_unicode(app_group_identity),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetValidationErrorResponse(),
            self.call_api(params, req, runtime)
        )

    def get_validation_report(self, app_group_identity, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_validation_report_with_options(app_group_identity, request, headers, runtime)

    def get_validation_report_with_options(self, app_group_identity, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetValidationReport',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/algorithm/data/validation-report' % TeaConverter.to_unicode(app_group_identity),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.GetValidationReportResponse(),
            self.call_api(params, req, runtime)
        )

    def list_abtest_experiments(self, app_group_identity, scene_id, group_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abtest_experiments_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    def list_abtest_experiments_with_options(self, app_group_identity, scene_id, group_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        scene_id = OpenApiUtilClient.get_encode_param(scene_id)
        group_id = OpenApiUtilClient.get_encode_param(group_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListABTestExperiments',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes/%s/groups/%s/experiments' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(scene_id), TeaConverter.to_unicode(group_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestExperimentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_abtest_fixed_flow_dividers(self, app_group_identity, scene_id, group_id, experiment_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abtest_fixed_flow_dividers_with_options(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    def list_abtest_fixed_flow_dividers_with_options(self, app_group_identity, scene_id, group_id, experiment_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        scene_id = OpenApiUtilClient.get_encode_param(scene_id)
        group_id = OpenApiUtilClient.get_encode_param(group_id)
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListABTestFixedFlowDividers',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes/%s/groups/%s/experiments/%s/fixed-flow-dividers' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(scene_id), TeaConverter.to_unicode(group_id), TeaConverter.to_unicode(experiment_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestFixedFlowDividersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_abtest_groups(self, app_group_identity, scene_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abtest_groups_with_options(app_group_identity, scene_id, headers, runtime)

    def list_abtest_groups_with_options(self, app_group_identity, scene_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        scene_id = OpenApiUtilClient.get_encode_param(scene_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListABTestGroups',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes/%s/groups' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(scene_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_abtest_metrics(self, app_group_identity, scene_id, group_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abtest_metrics_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    def list_abtest_metrics_with_options(self, app_group_identity, scene_id, group_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        scene_id = OpenApiUtilClient.get_encode_param(scene_id)
        group_id = OpenApiUtilClient.get_encode_param(group_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListABTestMetrics',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes/%s/groups/%s/metrics' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(scene_id), TeaConverter.to_unicode(group_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_abtest_scenes(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_abtest_scenes_with_options(app_group_identity, headers, runtime)

    def list_abtest_scenes_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListABTestScenes',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes' % TeaConverter.to_unicode(app_group_identity),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListABTestScenesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_group_errors(self, app_group_identity, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_app_group_errors_with_options(app_group_identity, request, headers, runtime)

    def list_app_group_errors_with_options(self, app_group_identity, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.stop_time):
            query['stopTime'] = request.stop_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppGroupErrors',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/errors' % TeaConverter.to_unicode(app_group_identity),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListAppGroupErrorsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_group_metrics(self, app_group_identity, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_app_group_metrics_with_options(app_group_identity, request, headers, runtime)

    def list_app_group_metrics_with_options(self, app_group_identity, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.indexes):
            query['indexes'] = request.indexes
        if not UtilClient.is_unset(request.metric_type):
            query['metricType'] = request.metric_type
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppGroupMetrics',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/metrics' % TeaConverter.to_unicode(app_group_identity),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListAppGroupMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_groups(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_app_groups_with_options(request, headers, runtime)

    def list_app_groups_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sort_by):
            query['sortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppGroups',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListAppGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_apps(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_apps_with_options(request, headers, runtime)

    def list_apps_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group):
            query['group'] = request.group
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/apps',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_collections(self, app_group_identity, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_collections_with_options(app_group_identity, request, headers, runtime)

    def list_data_collections_with_options(self, app_group_identity, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataCollections',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/data-collections' % TeaConverter.to_unicode(app_group_identity),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListDataCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_source_table_fields(self, data_source_type, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_source_table_fields_with_options(data_source_type, request, headers, runtime)

    def list_data_source_table_fields_with_options(self, data_source_type, request, headers, runtime):
        UtilClient.validate_model(request)
        data_source_type = OpenApiUtilClient.get_encode_param(data_source_type)
        query = {}
        if not UtilClient.is_unset(request.params):
            query['params'] = request.params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSourceTableFields',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/assist/data-sources/%s/fields' % TeaConverter.to_unicode(data_source_type),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListDataSourceTableFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_source_tables(self, data_source_type, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_source_tables_with_options(data_source_type, request, headers, runtime)

    def list_data_source_tables_with_options(self, data_source_type, request, headers, runtime):
        UtilClient.validate_model(request)
        data_source_type = OpenApiUtilClient.get_encode_param(data_source_type)
        query = {}
        if not UtilClient.is_unset(request.params):
            query['params'] = request.params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSourceTables',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/assist/data-sources/%s/tables' % TeaConverter.to_unicode(data_source_type),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListDataSourceTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_deployed_algorithm_models(self, app_group_identity, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_deployed_algorithm_models_with_options(app_group_identity, request, headers, runtime)

    def list_deployed_algorithm_models_with_options(self, app_group_identity, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        query = {}
        if not UtilClient.is_unset(request.algorithm_type):
            query['algorithmType'] = request.algorithm_type
        if not UtilClient.is_unset(request.in_service_only):
            query['inServiceOnly'] = request.in_service_only
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeployedAlgorithmModels',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/deployed-algorithm-models' % TeaConverter.to_unicode(app_group_identity),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListDeployedAlgorithmModelsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_first_ranks(self, app_group_identity, app_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_first_ranks_with_options(app_group_identity, app_id, headers, runtime)

    def list_first_ranks_with_options(self, app_group_identity, app_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFirstRanks',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/first-ranks' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListFirstRanksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_function_instances(self, app_group_identity, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_function_instances_with_options(app_group_identity, function_name, request, headers, runtime)

    def list_function_instances_with_options(self, app_group_identity, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        query = {}
        if not UtilClient.is_unset(request.function_type):
            query['functionType'] = request.function_type
        if not UtilClient.is_unset(request.model_type):
            query['modelType'] = request.model_type
        if not UtilClient.is_unset(request.output):
            query['output'] = request.output
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctionInstances',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/functions/%s/instances' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(function_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListFunctionInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_function_tasks(self, app_group_identity, function_name, instance_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_function_tasks_with_options(app_group_identity, function_name, instance_name, request, headers, runtime)

    def list_function_tasks_with_options(self, app_group_identity, function_name, instance_name, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        instance_name = OpenApiUtilClient.get_encode_param(instance_name)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctionTasks',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/functions/%s/instances/%s/tasks' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(function_name), TeaConverter.to_unicode(instance_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListFunctionTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_intervention_dictionaries(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_intervention_dictionaries_with_options(request, headers, runtime)

    def list_intervention_dictionaries_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.types):
            query['types'] = request.types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInterventionDictionaries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/intervention-dictionaries',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionariesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_intervention_dictionary_entries(self, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_intervention_dictionary_entries_with_options(name, request, headers, runtime)

    def list_intervention_dictionary_entries_with_options(self, name, request, headers, runtime):
        UtilClient.validate_model(request)
        name = OpenApiUtilClient.get_encode_param(name)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.word):
            query['word'] = request.word
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInterventionDictionaryEntries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/intervention-dictionaries/%s/entries' % TeaConverter.to_unicode(name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionaryEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_intervention_dictionary_ner_results(self, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_intervention_dictionary_ner_results_with_options(name, request, headers, runtime)

    def list_intervention_dictionary_ner_results_with_options(self, name, request, headers, runtime):
        UtilClient.validate_model(request)
        name = OpenApiUtilClient.get_encode_param(name)
        query = {}
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInterventionDictionaryNerResults',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/intervention-dictionaries/%s/ner-results' % TeaConverter.to_unicode(name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionaryNerResultsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_intervention_dictionary_related_entities(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_intervention_dictionary_related_entities_with_options(name, headers, runtime)

    def list_intervention_dictionary_related_entities_with_options(self, name, headers, runtime):
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListInterventionDictionaryRelatedEntities',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/intervention-dictionaries/%s/related' % TeaConverter.to_unicode(name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListInterventionDictionaryRelatedEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_models(self, app_group_identity, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_models_with_options(app_group_identity, request, headers, runtime)

    def list_models_with_options(self, app_group_identity, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModels',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/algorithm/models' % TeaConverter.to_unicode(app_group_identity),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListModelsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_proceedings(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_proceedings_with_options(app_group_identity, headers, runtime)

    def list_proceedings_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProceedings',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/proceedings' % TeaConverter.to_unicode(app_group_identity),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListProceedingsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_query_processor_analyzer_results(self, app_group_identity, app_id, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_query_processor_analyzer_results_with_options(app_group_identity, app_id, name, request, headers, runtime)

    def list_query_processor_analyzer_results_with_options(self, app_group_identity, app_id, name, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        name = OpenApiUtilClient.get_encode_param(name)
        query = {}
        if not UtilClient.is_unset(request.text):
            query['text'] = request.text
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueryProcessorAnalyzerResults',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/query-processors/%s/analyze' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id), TeaConverter.to_unicode(name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListQueryProcessorAnalyzerResultsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_query_processor_ners(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_query_processor_ners_with_options(request, headers, runtime)

    def list_query_processor_ners_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueryProcessorNers',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/query-processor/ner/default-priorities',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListQueryProcessorNersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_query_processors(self, app_group_identity, app_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_query_processors_with_options(app_group_identity, app_id, request, headers, runtime)

    def list_query_processors_with_options(self, app_group_identity, app_id, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        query = {}
        if not UtilClient.is_unset(request.is_active):
            query['isActive'] = request.is_active
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueryProcessors',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/query-processors' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListQueryProcessorsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_quota_review_tasks(self, app_group_identity, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_quota_review_tasks_with_options(app_group_identity, request, headers, runtime)

    def list_quota_review_tasks_with_options(self, app_group_identity, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotaReviewTasks',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/quota-review-tasks' % TeaConverter.to_unicode(app_group_identity),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListQuotaReviewTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ram_roles(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ram_roles_with_options(headers, runtime)

    def list_ram_roles_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRamRoles',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/assist/ram/roles',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListRamRolesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_scheduled_tasks(self, app_group_identity, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_scheduled_tasks_with_options(app_group_identity, request, headers, runtime)

    def list_scheduled_tasks_with_options(self, app_group_identity, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScheduledTasks',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scheduled-tasks' % TeaConverter.to_unicode(app_group_identity),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListScheduledTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_search_strategies(self, app_group_identity, app_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_search_strategies_with_options(app_group_identity, app_id, headers, runtime)

    def list_search_strategies_with_options(self, app_group_identity, app_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSearchStrategies',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/search-strategies' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSearchStrategiesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_second_ranks(self, app_group_identity, app_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_second_ranks_with_options(app_group_identity, app_id, headers, runtime)

    def list_second_ranks_with_options(self, app_group_identity, app_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSecondRanks',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/second-ranks' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSecondRanksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_slow_query_categories(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_slow_query_categories_with_options(app_group_identity, headers, runtime)

    def list_slow_query_categories_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSlowQueryCategories',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/optimizers/slow-query/categories' % TeaConverter.to_unicode(app_group_identity),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSlowQueryCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_slow_query_queries(self, app_group_identity, category_index):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_slow_query_queries_with_options(app_group_identity, category_index, headers, runtime)

    def list_slow_query_queries_with_options(self, app_group_identity, category_index, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        category_index = OpenApiUtilClient.get_encode_param(category_index)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSlowQueryQueries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/optimizers/slow-query/categories/%s/queries' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(category_index)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSlowQueryQueriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_sort_expressions(self, app_group_identity, app_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sort_expressions_with_options(app_group_identity, app_id, headers, runtime)

    def list_sort_expressions_with_options(self, app_group_identity, app_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSortExpressions',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/sort-expressions' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSortExpressionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_sort_scripts(self, app_group_identity, app_version_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sort_scripts_with_options(app_group_identity, app_version_id, headers, runtime)

    def list_sort_scripts_with_options(self, app_group_identity, app_version_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_version_id = OpenApiUtilClient.get_encode_param(app_version_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSortScripts',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/sort-scripts' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_version_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListSortScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_statistic_logs(self, app_group_identity, module_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_statistic_logs_with_options(app_group_identity, module_name, request, headers, runtime)

    def list_statistic_logs_with_options(self, app_group_identity, module_name, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        module_name = OpenApiUtilClient.get_encode_param(module_name)
        query = {}
        if not UtilClient.is_unset(request.columns):
            query['columns'] = request.columns
        if not UtilClient.is_unset(request.distinct):
            query['distinct'] = request.distinct
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.sort_by):
            query['sortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.stop_time):
            query['stopTime'] = request.stop_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStatisticLogs',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/statistic-logs/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(module_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListStatisticLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_statistic_report(self, app_group_identity, module_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_statistic_report_with_options(app_group_identity, module_name, request, headers, runtime)

    def list_statistic_report_with_options(self, app_group_identity, module_name, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        module_name = OpenApiUtilClient.get_encode_param(module_name)
        query = {}
        if not UtilClient.is_unset(request.columns):
            query['columns'] = request.columns
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStatisticReport',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/statistic-report/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(module_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListStatisticReportResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_analyzer_entries(self, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_analyzer_entries_with_options(name, request, headers, runtime)

    def list_user_analyzer_entries_with_options(self, name, request, headers, runtime):
        UtilClient.validate_model(request)
        name = OpenApiUtilClient.get_encode_param(name)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.word):
            query['word'] = request.word
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserAnalyzerEntries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/user-analyzers/%s/entries' % TeaConverter.to_unicode(name),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListUserAnalyzerEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_analyzers(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_analyzers_with_options(request, headers, runtime)

    def list_user_analyzers_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserAnalyzers',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/user-analyzers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ListUserAnalyzersResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_app_group(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_app_group_with_options(app_group_identity, headers, runtime)

    def modify_app_group_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyAppGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s' % TeaConverter.to_unicode(app_group_identity),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_app_group_quota(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_app_group_quota_with_options(app_group_identity, headers, runtime)

    def modify_app_group_quota_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyAppGroupQuota',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/quota' % TeaConverter.to_unicode(app_group_identity),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyAppGroupQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_first_rank(self, app_group_identity, app_id, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_first_rank_with_options(app_group_identity, app_id, name, request, headers, runtime)

    def modify_first_rank_with_options(self, app_group_identity, app_id, name, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        name = OpenApiUtilClient.get_encode_param(name)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFirstRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/first-ranks/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id), TeaConverter.to_unicode(name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyFirstRankResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_model(self, app_group_identity, model_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_model_with_options(app_group_identity, model_name, headers, runtime)

    def modify_model_with_options(self, app_group_identity, model_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        model_name = OpenApiUtilClient.get_encode_param(model_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyModel',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/algorithm/models/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(model_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyModelResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_query_processor(self, app_group_identity, app_id, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_query_processor_with_options(app_group_identity, app_id, name, request, headers, runtime)

    def modify_query_processor_with_options(self, app_group_identity, app_id, name, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        name = OpenApiUtilClient.get_encode_param(name)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyQueryProcessor',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/query-processors/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id), TeaConverter.to_unicode(name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyQueryProcessorResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_scheduled_task(self, app_group_identity, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_scheduled_task_with_options(app_group_identity, task_id, headers, runtime)

    def modify_scheduled_task_with_options(self, app_group_identity, task_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ModifyScheduledTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scheduled-tasks/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(task_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifyScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_second_rank(self, app_group_identity, app_id, name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_second_rank_with_options(app_group_identity, app_id, name, request, headers, runtime)

    def modify_second_rank_with_options(self, app_group_identity, app_id, name, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        name = OpenApiUtilClient.get_encode_param(name)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecondRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/second-ranks/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id), TeaConverter.to_unicode(name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ModifySecondRankResponse(),
            self.call_api(params, req, runtime)
        )

    def preview_model(self, app_group_identity, model_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.preview_model_with_options(app_group_identity, model_name, request, headers, runtime)

    def preview_model_with_options(self, app_group_identity, model_name, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        model_name = OpenApiUtilClient.get_encode_param(model_name)
        query = {}
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreviewModel',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/algorithm/models/%s/actions/preview' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(model_name)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.PreviewModelResponse(),
            self.call_api(params, req, runtime)
        )

    def push_intervention_dictionary_entries(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_intervention_dictionary_entries_with_options(name, headers, runtime)

    def push_intervention_dictionary_entries_with_options(self, name, headers, runtime):
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PushInterventionDictionaryEntries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/intervention-dictionaries/%s/entries/actions/bulk' % TeaConverter.to_unicode(name),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.PushInterventionDictionaryEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def push_user_analyzer_entries(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_user_analyzer_entries_with_options(name, headers, runtime)

    def push_user_analyzer_entries_with_options(self, name, headers, runtime):
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PushUserAnalyzerEntries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/user-analyzers/%s/entries/actions/bulk' % TeaConverter.to_unicode(name),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.PushUserAnalyzerEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    def rank_preview_query(self, app_group_identity, model_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rank_preview_query_with_options(app_group_identity, model_name, headers, runtime)

    def rank_preview_query_with_options(self, app_group_identity, model_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        model_name = OpenApiUtilClient.get_encode_param(model_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RankPreviewQuery',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/algorithm/models/%s/actions/query-rank' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(model_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RankPreviewQueryResponse(),
            self.call_api(params, req, runtime)
        )

    def release_sort_script(self, app_group_identity, script_name, app_version_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.release_sort_script_with_options(app_group_identity, script_name, app_version_id, headers, runtime)

    def release_sort_script_with_options(self, app_group_identity, script_name, app_version_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        script_name = OpenApiUtilClient.get_encode_param(script_name)
        app_version_id = OpenApiUtilClient.get_encode_param(app_version_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ReleaseSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/sort-scripts/%s/actions/release' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_version_id), TeaConverter.to_unicode(script_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ReleaseSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_app(self, app_group_identity, app_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_app_with_options(app_group_identity, app_id, headers, runtime)

    def remove_app_with_options(self, app_group_identity, app_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveApp',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveAppResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_app_group(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_app_group_with_options(app_group_identity, headers, runtime)

    def remove_app_group_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveAppGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s' % TeaConverter.to_unicode(app_group_identity),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_data_collection(self, app_group_identity, data_collection_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_data_collection_with_options(app_group_identity, data_collection_identity, headers, runtime)

    def remove_data_collection_with_options(self, app_group_identity, data_collection_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        data_collection_identity = OpenApiUtilClient.get_encode_param(data_collection_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveDataCollection',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/data-collections/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(data_collection_identity)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveDataCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_first_rank(self, app_group_identity, app_id, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_first_rank_with_options(app_group_identity, app_id, name, headers, runtime)

    def remove_first_rank_with_options(self, app_group_identity, app_id, name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveFirstRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/first-ranks/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id), TeaConverter.to_unicode(name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveFirstRankResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_intervention_dictionary(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_intervention_dictionary_with_options(name, headers, runtime)

    def remove_intervention_dictionary_with_options(self, name, headers, runtime):
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveInterventionDictionary',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/intervention-dictionaries/%s' % TeaConverter.to_unicode(name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveInterventionDictionaryResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_query_processor(self, app_group_identity, app_id, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_query_processor_with_options(app_group_identity, app_id, name, headers, runtime)

    def remove_query_processor_with_options(self, app_group_identity, app_id, name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveQueryProcessor',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/query-processors/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id), TeaConverter.to_unicode(name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveQueryProcessorResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_scheduled_task(self, app_group_identity, task_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_scheduled_task_with_options(app_group_identity, task_id, headers, runtime)

    def remove_scheduled_task_with_options(self, app_group_identity, task_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveScheduledTask',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scheduled-tasks/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(task_id)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_search_strategy(self, app_group_identity, app_id, strategy_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_search_strategy_with_options(app_group_identity, app_id, strategy_name, headers, runtime)

    def remove_search_strategy_with_options(self, app_group_identity, app_id, strategy_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        strategy_name = OpenApiUtilClient.get_encode_param(strategy_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveSearchStrategy',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/search-strategies/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id), TeaConverter.to_unicode(strategy_name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveSearchStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_second_rank(self, app_group_identity, app_id, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_second_rank_with_options(app_group_identity, app_id, name, headers, runtime)

    def remove_second_rank_with_options(self, app_group_identity, app_id, name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveSecondRank',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/second-ranks/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id), TeaConverter.to_unicode(name)),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveSecondRankResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_user_analyzer(self, name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_user_analyzer_with_options(name, headers, runtime)

    def remove_user_analyzer_with_options(self, name, headers, runtime):
        name = OpenApiUtilClient.get_encode_param(name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveUserAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/user-analyzers/%s' % TeaConverter.to_unicode(name),
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RemoveUserAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    def renew_app_group(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.renew_app_group_with_options(app_group_identity, headers, runtime)

    def renew_app_group_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RenewAppGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/actions/renew' % TeaConverter.to_unicode(app_group_identity),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.RenewAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def replace_app_group_commodity_code(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.replace_app_group_commodity_code_with_options(app_group_identity, headers, runtime)

    def replace_app_group_commodity_code_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ReplaceAppGroupCommodityCode',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/actions/to-instance-typed' % TeaConverter.to_unicode(app_group_identity),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ReplaceAppGroupCommodityCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def save_sort_script_file(self, app_group_identity, script_name, app_version_id, file_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.save_sort_script_file_with_options(app_group_identity, script_name, app_version_id, file_name, headers, runtime)

    def save_sort_script_file_with_options(self, app_group_identity, script_name, app_version_id, file_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        script_name = OpenApiUtilClient.get_encode_param(script_name)
        app_version_id = OpenApiUtilClient.get_encode_param(app_version_id)
        file_name = OpenApiUtilClient.get_encode_param(file_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SaveSortScriptFile',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/sort-scripts/%s/files/src/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_version_id), TeaConverter.to_unicode(script_name), TeaConverter.to_unicode(file_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.SaveSortScriptFileResponse(),
            self.call_api(params, req, runtime)
        )

    def start_slow_query_analyzer(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_slow_query_analyzer_with_options(app_group_identity, headers, runtime)

    def start_slow_query_analyzer_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartSlowQueryAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/optimizers/slow-query/actions/run' % TeaConverter.to_unicode(app_group_identity),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.StartSlowQueryAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    def train_model(self, app_group_identity, model_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.train_model_with_options(app_group_identity, model_name, headers, runtime)

    def train_model_with_options(self, app_group_identity, model_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        model_name = OpenApiUtilClient.get_encode_param(model_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='TrainModel',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/algorithm/models/%s/actions/train' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(model_name)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.TrainModelResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_esuser_analyzer(self, app_group_identity, es_instance_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.unbind_esuser_analyzer_with_options(app_group_identity, es_instance_id, headers, runtime)

    def unbind_esuser_analyzer_with_options(self, app_group_identity, es_instance_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        es_instance_id = OpenApiUtilClient.get_encode_param(es_instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UnbindESUserAnalyzer',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/es/%s/actions/unbind-analyzer' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(es_instance_id)),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UnbindESUserAnalyzerResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_es_instance(self, app_group_identity):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.unbind_es_instance_with_options(app_group_identity, headers, runtime)

    def unbind_es_instance_with_options(self, app_group_identity, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UnbindEsInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/actions/unbind-es-instance' % TeaConverter.to_unicode(app_group_identity),
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UnbindEsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_abtest_experiment(self, app_group_identity, scene_id, group_id, experiment_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_abtest_experiment_with_options(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    def update_abtest_experiment_with_options(self, app_group_identity, scene_id, group_id, experiment_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        scene_id = OpenApiUtilClient.get_encode_param(scene_id)
        group_id = OpenApiUtilClient.get_encode_param(group_id)
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateABTestExperiment',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes/%s/groups/%s/experiments/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(scene_id), TeaConverter.to_unicode(group_id), TeaConverter.to_unicode(experiment_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    def update_abtest_fixed_flow_dividers(self, app_group_identity, scene_id, group_id, experiment_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_abtest_fixed_flow_dividers_with_options(app_group_identity, scene_id, group_id, experiment_id, headers, runtime)

    def update_abtest_fixed_flow_dividers_with_options(self, app_group_identity, scene_id, group_id, experiment_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        scene_id = OpenApiUtilClient.get_encode_param(scene_id)
        group_id = OpenApiUtilClient.get_encode_param(group_id)
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateABTestFixedFlowDividers',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes/%s/groups/%s/experiments/%s/fixed-flow-dividers' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(scene_id), TeaConverter.to_unicode(group_id), TeaConverter.to_unicode(experiment_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestFixedFlowDividersResponse(),
            self.call_api(params, req, runtime)
        )

    def update_abtest_group(self, app_group_identity, scene_id, group_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_abtest_group_with_options(app_group_identity, scene_id, group_id, headers, runtime)

    def update_abtest_group_with_options(self, app_group_identity, scene_id, group_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        scene_id = OpenApiUtilClient.get_encode_param(scene_id)
        group_id = OpenApiUtilClient.get_encode_param(group_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateABTestGroup',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes/%s/groups/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(scene_id), TeaConverter.to_unicode(group_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_abtest_scene(self, app_group_identity, scene_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_abtest_scene_with_options(app_group_identity, scene_id, headers, runtime)

    def update_abtest_scene_with_options(self, app_group_identity, scene_id, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        scene_id = OpenApiUtilClient.get_encode_param(scene_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateABTestScene',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/scenes/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(scene_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateABTestSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def update_fetch_fields(self, app_group_identity, app_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_fetch_fields_with_options(app_group_identity, app_id, request, headers, runtime)

    def update_fetch_fields_with_options(self, app_group_identity, app_id, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFetchFields',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/fetch-fields' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateFetchFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_function_default_instance(self, app_group_identity, function_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_function_default_instance_with_options(app_group_identity, function_name, request, headers, runtime)

    def update_function_default_instance_with_options(self, app_group_identity, function_name, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunctionDefaultInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/functions/%s/default-instance' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(function_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateFunctionDefaultInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_function_instance(self, app_group_identity, function_name, instance_name, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_function_instance_with_options(app_group_identity, function_name, instance_name, request, headers, runtime)

    def update_function_instance_with_options(self, app_group_identity, function_name, instance_name, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        function_name = OpenApiUtilClient.get_encode_param(function_name)
        instance_name = OpenApiUtilClient.get_encode_param(instance_name)
        body = {}
        if not UtilClient.is_unset(request.create_parameters):
            body['createParameters'] = request.create_parameters
        if not UtilClient.is_unset(request.cron):
            body['cron'] = request.cron
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFunctionInstance',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/functions/%s/instances/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(function_name), TeaConverter.to_unicode(instance_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateFunctionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_search_strategy(self, app_group_identity, app_id, strategy_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_search_strategy_with_options(app_group_identity, app_id, strategy_name, headers, runtime)

    def update_search_strategy_with_options(self, app_group_identity, app_id, strategy_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        strategy_name = OpenApiUtilClient.get_encode_param(strategy_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateSearchStrategy',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/search-strategies/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id), TeaConverter.to_unicode(strategy_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateSearchStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_sort_script(self, app_group_identity, app_version_id, script_name):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_sort_script_with_options(app_group_identity, app_version_id, script_name, headers, runtime)

    def update_sort_script_with_options(self, app_group_identity, app_version_id, script_name, headers, runtime):
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_version_id = OpenApiUtilClient.get_encode_param(app_version_id)
        script_name = OpenApiUtilClient.get_encode_param(script_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateSortScript',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/sort-scripts/%s' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_version_id), TeaConverter.to_unicode(script_name)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateSortScriptResponse(),
            self.call_api(params, req, runtime)
        )

    def update_summaries(self, app_group_identity, app_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_summaries_with_options(app_group_identity, app_id, request, headers, runtime)

    def update_summaries_with_options(self, app_group_identity, app_id, request, headers, runtime):
        UtilClient.validate_model(request)
        app_group_identity = OpenApiUtilClient.get_encode_param(app_group_identity)
        app_id = OpenApiUtilClient.get_encode_param(app_id)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSummaries',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/app-groups/%s/apps/%s/summaries' % (TeaConverter.to_unicode(app_group_identity), TeaConverter.to_unicode(app_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.UpdateSummariesResponse(),
            self.call_api(params, req, runtime)
        )

    def validate_data_sources(self):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_data_sources_with_options(headers, runtime)

    def validate_data_sources_with_options(self, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ValidateDataSources',
            version='2017-12-25',
            protocol='HTTPS',
            pathname='/v4/openapi/assist/data-sources/validations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            open_search_20171225_models.ValidateDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )
