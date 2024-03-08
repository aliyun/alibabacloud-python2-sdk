# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore
from Tea.converter import TeaConverter

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paiautoml20220828 import models as pai_auto_ml20220828_models
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
        self._endpoint = self.get_endpoint('paiautoml', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_hpo_experiment_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accessibility):
            body['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.hpo_experiment_configuration):
            body['HpoExperimentConfiguration'] = request.hpo_experiment_configuration
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHpoExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname='/api/automl/v1/hpo/experiment',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.CreateHpoExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_hpo_experiment(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_hpo_experiment_with_options(request, headers, runtime)

    def delete_hpo_experiment_with_options(self, experiment_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteHpoExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname='/api/automl/v1/hpo/experiment/%s/delete' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.DeleteHpoExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_hpo_experiment(self, experiment_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_hpo_experiment_with_options(experiment_id, headers, runtime)

    def get_hpo_experiment_with_options(self, experiment_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHpoExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname='/api/automl/v1/hpo/experiment/%s' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.GetHpoExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hpo_experiment(self, experiment_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_hpo_experiment_with_options(experiment_id, headers, runtime)

    def get_hpo_trial_with_options(self, experiment_id, trial_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetHpoTrial',
            version='2022-08-28',
            protocol='HTTPS',
            pathname='/api/automl/v1/hpo/experiment/%s/trial/%s' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(trial_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.GetHpoTrialResponse(),
            self.call_api(params, req, runtime)
        )

    def get_hpo_trial(self, experiment_id, trial_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_hpo_trial_with_options(experiment_id, trial_id, headers, runtime)

    def list_hpo_experiments_with_options(self, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accessibility):
            query['Accessibility'] = request.accessibility
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.include_config_data):
            query['IncludeConfigData'] = request.include_config_data
        if not UtilClient.is_unset(request.max_create_time):
            query['MaxCreateTime'] = request.max_create_time
        if not UtilClient.is_unset(request.min_create_time):
            query['MinCreateTime'] = request.min_create_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHpoExperiments',
            version='2022-08-28',
            protocol='HTTPS',
            pathname='/api/automl/v1/hpo/experiments',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.ListHpoExperimentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hpo_experiments(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_hpo_experiments_with_options(request, headers, runtime)

    def list_hpo_trial_logs_with_options(self, experiment_id, trial_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_name):
            query['LogName'] = request.log_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHpoTrialLogs',
            version='2022-08-28',
            protocol='HTTPS',
            pathname='/api/automl/v1/hpo/experiment/%s/trial/%s/logs' % (TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_id)), TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(trial_id))),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.ListHpoTrialLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hpo_trial_logs(self, experiment_id, trial_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_hpo_trial_logs_with_options(experiment_id, trial_id, request, headers, runtime)

    def list_hpo_trials_with_options(self, experiment_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHpoTrials',
            version='2022-08-28',
            protocol='HTTPS',
            pathname='/api/automl/v1/hpo/experiment/%s/trials' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_id)),
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.ListHpoTrialsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hpo_trials(self, experiment_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_hpo_trials_with_options(experiment_id, request, headers, runtime)

    def restart_hpo_trials_with_options(self, experiment_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.trial_hyper_parameters):
            body['TrialHyperParameters'] = request.trial_hyper_parameters
        if not UtilClient.is_unset(request.trial_ids):
            body['TrialIds'] = request.trial_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestartHpoTrials',
            version='2022-08-28',
            protocol='HTTPS',
            pathname='/api/automl/v1/hpo/experiment/%s/restart_trials' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.RestartHpoTrialsResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_hpo_trials(self, experiment_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_hpo_trials_with_options(experiment_id, request, headers, runtime)

    def stop_hpo_experiment_with_options(self, experiment_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopHpoExperiment',
            version='2022-08-28',
            protocol='HTTPS',
            pathname='/api/automl/v1/hpo/experiment/%s/stop' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.StopHpoExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_hpo_experiment(self, experiment_id):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_hpo_experiment_with_options(experiment_id, headers, runtime)

    def stop_hpo_trials_with_options(self, experiment_id, request, headers, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.trial_ids):
            body['TrialIds'] = request.trial_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopHpoTrials',
            version='2022-08-28',
            protocol='HTTPS',
            pathname='/api/automl/v1/hpo/experiment/%s/stop_trials' % TeaConverter.to_unicode(OpenApiUtilClient.get_encode_param(experiment_id)),
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_auto_ml20220828_models.StopHpoTrialsResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_hpo_trials(self, experiment_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_hpo_trials_with_options(experiment_id, request, headers, runtime)
